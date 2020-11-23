import autograd.numpy as np
from autograd.scipy.stats import norm


def line_search(objective, c1, c2, wp_thresh, y0, t_guess):
    
    # Newton budget
    newton_budget = 10
    
    # Log noise to signal ratio grid for marginalisation
    log_nsr_grid = np.linspace(-20., 20., 21)
    
    # Make initial guess, initialise t and y arrays
    y_guess = objective(t_guess)
    
    t = np.array([0, t_])
    y = np.concatenate([y0, y_guess], axis=0)
    
    # Loop until a WP acceptable point is found
    while True:
        
        # Kalman filtering and smoothing for all models
        # results = (mf, Vf, ms, Vs, iVC, theta2, nlml)
        results = [kalman_filter_smoother(t, y, log_nsr) \
                  for log_nsr in log_nsr_grid]
        results = list(zip(*results))
        
        # Compute posterior likelihood of each model
        post_probs = np.array([np.exp(-nlml) for nlml in results[-1]])
        post_probs = post_probs / np.sum(post_probs)
        
        # Check for WP acceptable points
        wp_probs = [marg_lik * wolfe_powell(c1, c2, t, ms, Vs, iVC, theta2) \
                    for post_prob, ms, Vs, iVC in zip(post_probs, *results[2:5])]
        wp_probs = np.sum(wp_probs, axis=0)
        
        # If most probable WP point passes the probability threshold, return it
        idx_most_probable = np.argmax(wp_probs)
        if wp_probs[idx_most_probable] >= wp_thresh:
            return t[idx_most_probable+1], y[idx_most_probable+1]
        
        # Optimise EI mixture over each interval separately
        t_opts, f_opts = newton_mixture_on_intervals(budget=newton_budget, 
                                                     t=t,
                                                     ms=ms,
                                                     Vs=Vs,
                                                     iVC=iVC,
                                                     post_probs=post_probs)
            
        # Acquire new points
        y_new = [objective(t_opt) for t_opt in t_opts]
        
        t = np.insert(t, idx_acq, t_news, axis=0)
        y = np.insert(y, idx_acq, y_news, axis=0)
        
        

#     for idx in num_points_to_idx(20):

#         mf, Vf, ms, Vs, iVC, theta2, nlml = kalman_filter_smoother(t=t, y=y, log_nsr=log_nsr)

#         tmin = None
#         tmax = None
#         t0 = None

#         if idx == y.shape[0] - 1:

#             tmin = t[idx]
#             tmax = t[idx] + 2e-1 * (t[-1] - t[0])

#         else:
#             tmin = t[idx]
#             tmax = t[idx+1]

#         t0 = (tmax + tmin) / 2

#         t_opt, f_opt = newton(objective=objective,
#                               budget=budget,
#                               t0=t0,
#                               tmin=tmin,
#                               tmax=tmax,
#                               t_data=t,
#                               ms=ms,
#                               Vs=Vs,
#                               iVC=iVC)

#         x_new, y_new = sample_sine_data(t=np.array([t_opt]), omega=omega, R=R)
#         x_new, y_new = x_new[0], y_new[0]

#         t = np.insert(t, idx + 1, t_opt)

#         x = np.insert(x, idx + 1, x_new, axis=0)
#         y = np.insert(y, idx + 1, y_new, axis=0)


def kalman_filter_smoother(t, y, log_nsr):
    
    # Set arrays to store means and variances, compute time differences
    T = t.shape[0]
    mf = np.zeros(shape=(T, 3))
    Vf = np.zeros(shape=(T, 3, 3))
    ms = np.zeros(shape=(T, 3))
    Vs = np.zeros(shape=(T, 3, 3))
    S = np.zeros(shape=(T, 3, 3))
    iVC = np.zeros(shape=(T - 1, 3, 3))
    dt = t[1:] - t[:-1]
    
    # Noise variance to signal variance ratio
    n2 = np.exp(log_nsr)
    
    # Time independent state space model matrices
    C = np.eye(3)[:2, :]
    R = np.array([[n2, 0], [0, 0]])
    
    # Compute first two filtered posteriors
    mf[0], mf[1], Vf[0], Vf[1] = filter_initialise(dt[0], y, A(dt[0]), C, n2)
    
    # Forward filtering steps
    mf, Vf, S, theta2, nlml = filter_forward(dt, y, mf, Vf, S, C, R)
    
    # Backward smoothing steps
    ms, Vs, iVC = smooth_backward(dt, y, mf, Vf, S, ms, Vs, iVC, C, R)
    
    # Compute the first smoothed posterior
    ms, Vs, iVC = smoother_finalise(dt, y, mf, ms, Vs, iVC, n2)
    
    # Adjust variances by overal scale parameter
    Vf = theta2 * Vf
    Vs = theta2 * Vs
        
    return mf, Vf, ms, Vs, iVC, theta2, nlml


def A(dt):
    
    Adt = np.array([[1, dt, dt ** 2 / 2],
                    [0, 1, dt],
                    [0, 0, 1]])
    return Adt


def Q(dt):
    
    Qdt = np.array([[dt ** 5 / 20, dt ** 4 / 8, dt ** 3 / 6],
                    [dt ** 4 / 8, dt ** 3 / 3, dt ** 2 / 2],
                    [dt ** 3 / 6, dt ** 2 / 2, dt]])
    return Qdt


def filter_initialise(dt0, y, A0, C, n2):
    
    # Hard coded filtered variances (V11 is not used in smoothing pass)
    Vf1 = np.array([[n2, 0, 0],
                    [0, 0, 0],
                    [0, 0, float('inf')]])
    
    Vf2 = np.array([[n2 * dt0 ** 5 + 120 * n2 ** 2, 0, - 5 * n2 * dt0 ** 3],
                    [0, 0, 0],
                    [- 5 * n2 * dt0 ** 3, 0, dt0 ** 6 / 8 + 80 * n2 * dt0]])
    
    Vf2 = Vf2 / (dt0 ** 5 + 240 * n2)

    # Hard coded Kalman matrices for computing means
    K1 = np.eye(3)[:, :-1]
    K2 = np.array([[dt0 ** 6 + 120 * n2 * dt0, 60 * n2 * dt0 ** 2],
                   [0, dt0 ** 6 + 240 * n2 * dt0],
                   [- 5 * dt0 ** 4, 7 / 2 * dt0 ** 5 + 60 * n2]])
    K2 = K2 / (dt0 ** 6 + 240 * n2 * dt0)
    
    # Filtered means for first two states
    L = np.dot(np.eye(3) - np.dot(K2, C), np.dot(A0, K1))
    
    mf1 = np.dot(K1, y[0, :])
    mf2 = np.dot(L, y[0, :]) + np.dot(K2, y[1, :])
    
    return mf1, mf2, Vf1, Vf2


def filter_forward(dt, y, mf, Vf, S, C, R):
    
    T = y.shape[0]
    
    diff = y[1, :] - np.dot(C, np.dot(A(dt[0]), mf[0, :]))
    quad = np.dot(np.array([[1, - dt[0] / 2]]), diff) ** 2 / (dt[0] ** 5 / 120 + 2 * R[0, 0])
    logdet = 2 * np.log(dt[0]) + np.log(dt[0] ** 5 + 240 * R[0, 0]) - np.log(120)
    
    for i in range(2, T):
        
        # Set A and Q matrices for current time
        At = A(dt[i-1])
        Qt = Q(dt[i-1])
        
        S[i] = np.dot(At, np.dot(Vf[i-1], At.T)) + Qt
        diff = y[i, :] - np.dot(C, np.dot(At, mf[i-1, :]))
        
        mf[i, :] = np.dot(At, mf[i-1, :]) + kalman_dot(diff, S[i], C, R)
        Vf[i, :] = S[i] - kalman_dot(np.dot(C, S[i]), S[i], C, R)
        
        R_CSCT = R + np.dot(C, np.dot(S[i], C.T))
        
        quad = quad + np.dot(diff, np.linalg.solve(R_CSCT, diff))
        logdet = logdet + np.linalg.slogdet(R_CSCT)[1]
        
    theta2 = quad / (2 * T - 3)
    nlml = logdet / 2 + (2 * T - 3) * np.log(quad) / 2
        
    return mf, Vf, S, theta2, nlml


def smooth_backward(dt, y, mf, Vf, S, ms, Vs, iVC, C, R):
    
    T = y.shape[0]
        
    # Last-time smoothed posterior is equal to last-time filtered posterior
    ms[-1, :] = mf[-1, :]
    Vs[-1, :, :] = Vf[-1, :, :]
        
    # Smoothing steps
    for i in range(T - 2, 0, -1):
        
        # Set A and Q matrices for current time
        At = A(dt[i])
        Qt = Q(dt[i])
        
        J = np.linalg.solve(S[i+1], np.dot(At, Vf[i])).T
        Vs[i] = Vf[i] + np.dot(J, np.dot(Vs[i+1] - S[i+1], J.T))
        ms[i] = mf[i] + np.dot(J, ms[i+1] - np.dot(At, mf[i]))
        iVC[i] = J.T
        
    return ms, Vs, iVC


def smoother_finalise(dt, y, mf, ms, Vs, iVC, n2):
        
    # Hard coded smoothing step
    J = np.array([[960 * n2, - 600 * n2 * dt[0], 120 * n2 * dt[0] ** 2],
                  [0, 0, 0],
                  [20 * dt[0] ** 3, - 8 * dt[0] ** 4 + 1440 * n2 / dt[0], dt[0] ** 5 - 480 * n2]])
    J = J / (3 * dt[0] ** 5 + 960 * n2)
    
    ms[0] = mf[0] + np.dot(J, ms[1] - np.dot(A(dt[0]), mf[0]))
    
    Vs[0] = np.array([[9 * n2 * dt[0] ** 5, 0, - 60 * n2 * dt[0] ** 3],
                      [0, 0, 0],
                      [-60 * n2 * dt[0] ** 3, 0, dt[0] ** 6 + 720 * n2 * dt[0]]])
    Vs[0] = np.dot(J, np.dot(Vs[1], J.T)) + Vs[0] / (9 * dt[0] ** 5 + 2880 * n2)
    
    iVC[0] = J.T
    
    return ms, Vs, iVC
    
    
def kalman_dot(array, V, C, R):
    
    R_CVCT = R + np.dot(C, np.dot(V, C.T))
    R_CVCT_inv_array = np.linalg.solve(R_CVCT, array)
    
    K_array = np.dot(V, np.dot(C.T, R_CVCT_inv_array))
    
    return K_array


def post_pred(t, t_data, ms, Vs, iVC):
    
    # Index of first datapoint to the right of time t (datapoint 2)
    i = np.searchsorted(t_data, t)
    
    # Time difference from datapoint to left of t
    dt1 = t - t_data[i-1]
    
    # Check if interpolating or extrapolating
    if i < t_data.shape[0]:
        
        # Time difference to datapoint to right of t
        dt2 = t_data[i] - t
        
        # If interpolating, use interpolating posterior
        return int_post_pred(dt1, ms[i-1], Vs[i-1], dt2, ms[i], Vs[i], iVC[i-1])
    
    else:
        # Otherwise, use extrapolating posterior
        return ext_post_pred(dt1, ms[-1], Vs[-1])
    

def int_post_pred(dt1, m1, V1, dt2, m2, V2, iVC):
    """
    Computes the predictive mean and variance for an input point *t*. It is
    assumed that *t* lies between two observation points at *t1* and *t2* and
    that no other observation points lie in the interval (t1, t2).
    """
    
    # Compute state-space matrices
    A1 = A(dt1)
    A2 = A(dt2)
    Q1 = Q(dt1)
    Q2 = Q(dt2)

    # Compute Sigma, the variance matrix of p(x | x1, x2)
    A2Q1 = np.dot(A2, Q1)
    Q2_plus_A2Q1A2T = Q2 + np.dot(A2Q1, A2.T)
    Sigma = Q1 - np.dot(A2Q1.T, np.linalg.solve(Q2_plus_A2Q1A2T, A2Q1))

    # Compute the mean of p(x | data)
    m = np.linalg.solve(Q1, np.dot(A1, m1)) + np.dot(A2.T, np.linalg.solve(Q2, m2))
    m = np.dot(Sigma, m)

    # Compute the variance of p(x | data)
    iQ2A2 = np.linalg.solve(Q2, A2)
    iQ1A1 = np.linalg.solve(Q1, A1)
    
    # Compute covariance from inverse variance times covariance matrix
    C = V2 @ iVC

    V = np.dot(iQ2A2.T, np.dot(V2, iQ2A2))
    V = V + np.dot(iQ1A1, np.dot(V1, iQ1A1.T))
    V = V + np.dot(iQ2A2.T, np.dot(C, iQ1A1.T))
    V = V + np.dot(iQ1A1, np.dot(C.T, iQ2A2))
    V = Sigma + np.dot(Sigma, np.dot(V, Sigma))

    return m, V
    
    
def ext_post_pred(dt1, m1, V1):
        
    # Compute state-space matrices
    A1 = A(dt1)
    Q1 = Q(dt1)

    # Compute the mean of p(x | data)
    m = np.dot(A1, m1)

    # Compute the variance of p(x | data)
    V = np.dot(A1, np.dot(V1, A1.T)) + Q1

    return m, V
    
    
def newton(objective, budget, t0, tmin, tmax, t_data, *args):
    
    min_t = tmin + 2e-1 * (tmax - tmin)
    max_t = tmax - 2e-1 * (tmax - tmin)
    
    f0, df0, ddf0 = objective(t0, t_data, *args)
    budget = budget - 1
    
    t, f, df, ddf = t0, f0, df0, ddf0
    
    while budget > 1:
        
        # If ddf +ve, then newton is looking for a minimum, so accept it
        if ddf > 0:
            
            # Compute Newton step and ensure it's withing alloed range
            t = t - df / ddf
            t = max(min_t, min(t, max_t))
            
        # Elif df and ddf -ve, move to right boundary
        elif df < 0:
            t = max_t
            
        # Elif df +ve and ddf -ve, move to left boundary
        elif df > 0:
            t = min_t
            
        # If df >= 0.0 we have moved to the left, so update tmax
        if df >= 0.0:
            tmax = t0
        # If df < 0.0 we have moved to the right, so update tmin
        else:
            tmin = t0

        f, df, ddf = objective(t, t_data, *args)
        budget = budget - 1
            
        if f < f0:
            t0, f0, df0 = t, f, df
            
        elif t0 == t:
            break
        
    t = min(max(t, min_t), max_t)
    
    f, df, ddf = objective(t, t_data, *args)
    budget = budget - 1
        
    return t, f


def log_expected_improvement(f0, m, v):
    
    # Posterior standard deviation and normalised difference
    s = v ** 0.5
    z = (f0 - m) / s
    
    # Compute log expected improvement differently, depending on size of z
    if z > -20:
        return np.log((f0 - m) * norm.cdf(z) + s * norm.pdf(z))
    
    else:
        return - 0.5 * np.log(2 * np.pi) - 0.5 * z ** 2 - np.log(z ** 2 - 1)
    
    
def _neg_log_ei(t, t_data, ms_, Vs_, iVC_, log_post_):
    
    """
    Computes the negative log expected improvement of a set of
    quintic sline models.
    
    params t : float, position along the line to evaluate EI at
    params t_data : np.array, positions of data
    params ms_ : [np.array], means for each model
    params ms_ : [np.array], variances for each model
    params Vs_ : [np.array], inverse variances times covariances for each model
    params log_post_ : np.array, log-posterior probabilites of each model 
    """

    # Objective value to improve on
    f0 = np.min(ms[:, 0])

    # Posterior predictive of model
    m_, v_ = list(zip(*[post_pred(t, t_data, ms_, Vs_, iVC_) \
                        for ms, Vs, iVC in zip(ms_, Vs_, iVC_)])

    # Log expected improvement at time t
    log_ei = np.array([log_expected_improvement(f0=f0, m=m[0], v=v[0, 0]) \
                       for m, v in zip(m, v)])
                  
    max_log_ei = np.max(log_ei + log_post_)
                  
    log_ei = max_log_ei + np.log(np.sum(np.exp(log_ei - max_log_ei)))
    
    return - log_ei
                  

_dneg_log_ei = grad(_neg_log_ei, argnum=0)
_ddneg_log_ei = hessian(_neg_log_ei, argnum=0)

                  
def neg_log_ei(t, t_data, ms_, Vs_, iVC_, post_probs):

    ei = _neg_log_ei(t, t_data, ms_, Vs_, iVC_, post_probs)
    dei = _dneg_log_ei(t, t_data, ms_, Vs_, iVC_, post_probs)
    ddei = float(_ddneg_log_ei(t, t_data, ms_, Vs_, iVC_, post_probs))

    return ei, dei, ddei


def newton_mixture_on_intervals(budget, t, ms, Vs, iVC, post_probs):
    
    t_opts = []
    f_opts = []
    idx_acq = np.arange(t.shape[0])

    for idx in idx_acq:

        # If interpolating, set tmin and tmax to t's of current interval
        if idx < y.shape[0] - 1:
            tmin = t[idx]
            tmax = t[idx+1]
            
        # If extrapolating, set tmax to last datum plus fraction of range
        else:
            tmin = t[idx]
            tmax = t[idx] + 2e-1 * (t[-1] - t[0])

        # Initialise newton search at midpoint of interval
        t0 = (tmax + tmin) / 2

        # Do newton search
        t_new, f_new = newton(objective=neg_log_ei,
                              budget=budget,
                              t0=t0,
                              tmin=tmin,
                              tmax=tmax,
                              t_data=t,
                              ms_=ms,
                              Vs_=Vs,
                              iVC_=iVC,
                              log_probs_=post_probs)

        t_news.append(t_new)
        f_news.append(f_new)
                  
    return t_news, f_news


def covariances_to_left(ms, Vs, iVC):
    """
    Computes state covariances between the first location of the data
    and all other locations, given the data.
    """
    
    # Number of datapoints
    N = ms.shape[0]
    
    C0 = np.zeros(shape=iVC.shape)
    C0[0, :, :] = Vs[0] @ iVC[0]
    
    M = iVC[0]
    
    for t in range(1, N-1):
        
        M = iVC[t] @ M
        C0[t, :, :] = Vs[t+1] @ M
        
    return C0
        
    
def wolfe_powell(c1, c2, t, ms, Vs, iVC):
    
    # Number of datapoints
    N = ms.shape[0]
    
    mf0 = ms[0, 0]
    mdf0 = ms[0, 1]
    
    C0 = covariances_to_left(ms, Vs, iVC)
    wp_probs = np.zeros(shape=(N-1,))
    
    for i in range(1, N):
        
        # Check WP2. Gradient is noiseless so check is a simple comparison
        if np.abs(ms[i, 1]) > np.abs(c2 * mdf0):
            continue
        
        # If WP2 met, check WP1 and set nonzero WP acceptance probability
        else:
            mu = ms[i, 0] - mf0
            std = (Vs[0, 0, 0] + Vs[i, 0, 0] - 2 * C0[i-1, 0, 0]) ** 0.5
            
            alpha = c1 * t[i] * mdf0
            alpha = (alpha - mu) / std
            
            wp_probs[i-1] = norm.cdf(alpha)
            
    return wp_probs
            
            
            
            
            
    