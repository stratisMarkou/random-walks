import autograd.numpy as np
from autograd.scipy.stats import norm
from autograd import grad, hessian

import warnings


def line_search(objective, c1, c2, wp_thresh, t0, y0, t_guess):
    
    # Newton budget
    newton_budget = 6
    
    # Log noise to signal ratio grid for marginalisation
    log_nsr_grid = np.linspace(-20., 0., 6)
    
    # Make initial guess, initialise t and y arrays
    y_guess = objective(t_guess)
    
    t = np.array([t0, t0 + float(t_guess)])
    y = np.concatenate([y0, y_guess], axis=0)
    
    # Loop until a WP acceptable point is found
    while True:
    
        # print(f'Executing linesearch loop, with {t.shape[0]:3d} points')
        
        # Kalman filtering and smoothing for all models
        # results = (mf, Vf, ms, Vs, iVC, theta2, nlml)
        results = [kalman_filter_smoother(t, y, log_nsr) \
                  for log_nsr in log_nsr_grid]
        
        results = list(zip(*results))
        
        # Compute posterior likelihood of each model
        post_probs = np.array([np.exp(-nlml) for nlml in results[-1]])
        post_probs = post_probs / np.sum(post_probs)
        
        # Check for WP acceptable points
        wp_probs = [post_prob * wolfe_powell(c1, c2, t, ms, Vs, iVC) \
                    for post_prob, ms, Vs, iVC in zip(post_probs, *results[2:5])]
        wp_probs = np.sum(wp_probs, axis=0)
        
        # Unpack results
        mf, Vf, ms, Vs, iVC, _, _ = results
        
        # If most probable WP point passes the probability threshold, return it
        idx_most_probable = np.argmax(wp_probs)
        if wp_probs[idx_most_probable] >= wp_thresh:
            return t, y, wp_probs, mf, Vf, ms, Vs, iVC, post_probs
        
        # Optimise EI mixture over each interval separately
        t_news, _ = newton_mixture_on_intervals(budget=newton_budget, 
                                                t=t,
                                                y=y,
                                                ms=ms,
                                                Vs=Vs,
                                                iVC=iVC,
                                                post_probs=post_probs)
            
        # Acquire new points
        y_news = np.concatenate([objective(t_new) for t_new in t_news], axis=0)
        
        t = np.insert(t, np.arange(y_news.shape[0]) + 1, t_news, axis=0)
        y = np.insert(y, np.arange(y_news.shape[0]) + 1, y_news, axis=0)


def kalman_filter_smoother(t, y, log_nsr, verbose=False):
    
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
    mf[0, :], mf[1, :], Vf[0, :, :], Vf[1, :, :] = filter_initialise(dt[0], y, A(dt[0]), C, n2)
    
    if verbose: print(Vf[0, :, :])
    
    # Forward filtering steps
    mf, Vf, S, theta2, nlml = filter_forward(dt, y, mf, Vf, S, C, R, verbose=verbose)
    
    # Backward smoothing steps
    ms, Vs, iVC = smooth_backward(dt, y, mf, Vf, S, ms, Vs, iVC, C, R)
    
    # Compute the first smoothed posterior
    ms, Vs, iVC = smoother_finalise(dt, y, mf, ms, Vs, iVC, n2)
    
    # Adjust variances by overal scale parameter
    Vf = theta2 * Vf
    Vs = theta2 * Vs
    
    if verbose: print(Vf[0, :, :])
        
    return mf, Vf, ms, Vs, iVC, theta2, nlml


def A(dt):
    
    Adt = np.array([[1, dt, dt ** 2 / 2],
                    [0, 1, dt],
                    [0, 0, 1]])
    return Adt


def Q(dt):
    
    Qdt = np.array([[dt ** 5 / 20, dt ** 4 / 8, dt ** 3 / 6],
                    [ dt ** 4 / 8, dt ** 3 / 3, dt ** 2 / 2],
                    [ dt ** 3 / 6, dt ** 2 / 2, dt         ]])
    return Qdt


def iQ(dt):
    
    iQdt = np.array([[ 720 * dt ** -5, -360 * dt ** -4,  60 * dt ** -3],
                     [-360 * dt ** -4,  192 * dt ** -3, -36 * dt ** -2],
                     [  60 * dt ** -3,  -36 * dt ** -2,   9 * dt ** -1]])
    
    return iQdt


def filter_initialise(dt0, y, A0, C, n2):
    
    # Hard coded filtered variances (Vf1 is never used at all)
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


def filter_forward(dt, y, mf, Vf, S, C, R, verbose=False):
    
    T = y.shape[0]
    
    diff = y[1, :] - np.dot(C, np.dot(A(dt[0]), mf[0, :]))
    if verbose: print('diff', diff)
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
        
        R_CSCT = R + C @ S[i] @ C.T
        
        if verbose: print('quad', quad)
        if verbose: print('diff', diff)
        if verbose:
            print('S')
            print(S)
            
        quad = quad + np.dot(diff, np.linalg.solve(R_CSCT, diff)) # np.dot(diff, iR_CMCT(diff, S[i], C, R))
        logdet = logdet + np.linalg.slogdet(R_CSCT)[1]
        
    if verbose: print('quad', quad)
        
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

    iR_CVCT_array = iR_CMCT(array, V, C, R)
    
    K_array = np.dot(V, np.dot(C.T, iR_CVCT_array))
    
    return K_array


def iR_CMCT(array, M, C, R):
    
    R_CMCT = R + np.dot(C, np.dot(M, C.T))
    R_CMCT_inv_array = np.linalg.solve(R_CMCT, array)
    
    return R_CMCT_inv_array

    
#     [  c/(- b^2 + a*c + c*n),      -b/(- b^2 + a*c + c*n)]
#     [ -b/(- b^2 + a*c + c*n), (a + n)/(- b^2 + a*c + c*n)]

#     n2 = R[0, 0]
#     B = np.dot(C, np.dot(M, C.T))
    
#     a = B[0, 0]
#     b = B[0, 1]
#     c = B[1, 1]
    
#     tmp1 = np.array([[c, -b],
#                      [-b, a]])
    
#     tmp2 = np.array([[0, 0],
#                      [0, n2]])
#     tmp = (tmp1 @ array) + (tmp2 @ array)
    
#     tmp = tmp / ((a * c - b ** 2) + c * n2)
    
#     return tmp
    


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
    iQ1 = iQ(dt1)
    iQ2 = iQ(dt2)

    # Compute Sigma, the variance matrix of p(x | x1, x2)
    A2Q1 = np.dot(A2, Q1)
    Q2_plus_A2Q1A2T = Q2 + np.dot(A2Q1, A2.T)
    Sigma = Q1 - np.dot(A2Q1.T, np.linalg.solve(Q2_plus_A2Q1A2T, A2Q1))

    # Compute the mean of p(x | data)
    m = iQ1 @ np.dot(A1, m1) + np.dot(A2.T, iQ2 @ m2)
    m = np.dot(Sigma, m)

    # Compute the variance of p(x | data)
    iQ1A1 = iQ1 @ A1
    iQ2A2 = iQ2 @ A2
    
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
    
    
def newton(objective, budget, t0, tmin, tmax, t_data, ms, Vs, iVC, **kargs):
    
    min_t = tmin + 2e-1 * (tmax - tmin)
    max_t = tmax - 2e-1 * (tmax - tmin)
    
    f0, df0, ddf0 = objective(t0, t_data, ms, Vs, iVC, **kargs)
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

        f, df, ddf = objective(t, t_data, ms, Vs, iVC, **kargs)
        budget = budget - 1
            
        if f < f0:
            t0, f0, df0 = t, f, df
            
        elif t0 == t:
            break
        
    t = min(max(t, min_t), max_t)
    
    f, df, ddf = objective(t, t_data, ms, Vs, iVC, **kargs)
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
    
    
def _neg_log_ei(t, t_data, ms, Vs, iVC, log_post):
    
    """
    Computes the negative log expected improvement of a set of
    quintic sline models.
    
    params t : float, position along the line to evaluate EI at
    params t_data : np.array, positions of data
    params ms : [np.array], means for each model
    params ms : [np.array], variances for each model
    params Vs : [np.array], inverse variances times covariances for each model
    params log_post : np.array, log-posterior probabilites of each model
    """

    # Objective values to improve on
    f0 = [np.min(ms_[:, 0]) for ms_ in ms]

    # Posterior predictive of model
    m, v = list(zip(*[post_pred(t, t_data, ms_, Vs_, iVC_) \
                        for ms_, Vs_, iVC_ in zip(ms, Vs, iVC)]))

    # Log expected improvement at time t
    log_ei = np.array([log_expected_improvement(f0=f0_, m=m_[0], v=v_[0, 0]) \
                       for f0_, m_, v_ in zip(f0, m, v)])
                  
    max_log_ei = np.max(log_ei + log_post)
                  
    log_ei = max_log_ei + np.log(np.sum(np.exp(log_ei - max_log_ei)))
    
    return - log_ei
                  

_dneg_log_ei = grad(_neg_log_ei, argnum=0)
_ddneg_log_ei = hessian(_neg_log_ei, argnum=0)

                  
def neg_log_ei(t, t_data, ms, Vs, iVC, post_probs):

    ei = _neg_log_ei(t, t_data, ms, Vs, iVC, post_probs)
    dei = _dneg_log_ei(t, t_data, ms, Vs, iVC, post_probs)
    ddei = float(_ddneg_log_ei(t, t_data, ms, Vs, iVC, post_probs))

    return ei, dei, ddei


def newton_mixture_on_intervals(budget, t, y, ms, Vs, iVC, post_probs):
    
    T = ms[0].shape[0]
    
    t_news = []
    f_news = []
    idx_acq = np.arange(t.shape[0])

    for idx in idx_acq:
        
        # If point on the interval's left side has positive gradient stop
        if y[idx, 1] > 0:
            break

        # If interpolating, set tmin and tmax to t's of current interval
        if idx < T - 1:
            tmin = t[idx]
            tmax = t[idx+1]
            
        # If extrapolating, set tmax to last datum plus fraction of range
        else:
            tmin = t[idx]
            tmax = t[idx] + (t[-1] - t[0])

        # Initialise newton search at midpoint of interval
        t0 = (tmax + tmin) / 2

        # Do newton search
        t_new, f_new = newton(objective=neg_log_ei,
                              budget=budget,
                              t0=t0,
                              tmin=tmin,
                              tmax=tmax,
                              t_data=t,
                              ms=ms,
                              Vs=Vs,
                              iVC=iVC,
                              post_probs=post_probs)

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
    C0[0, :, :] = Vs[1] @ iVC[0]
    
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
            wp_probs[i-1] = 0.
        
        # If WP2 met, check WP1 and set nonzero WP acceptance probability
        else:
            mu = ms[i, 0] - mf0
            var = Vs[0, 0, 0] + Vs[i, 0, 0] - 2 * C0[i-1, 0, 0]
                
            alpha = c1 * t[i] * mdf0
            alpha = (alpha - mu)
            
            if var <= -1e-6:
                raise Exception("WP standard deviation was <= 1e-6")
                
            elif -1e-6 <= var and var <= 0.:
                
                warnings.warn(f'wolfe_powell var was {var}. '
                              'Treating this as 0, manually.')

                if alpha == 0:
                    wp_probs[i-1] = 0.5

                elif alpha > 0.:
                    wp_probs[i-1] = 1.

                else:
                    wp_probs[i-1] = 0.
                        
            else:
                alpha = alpha / var ** 0.5
                wp_probs[i-1] = norm.cdf(alpha)
            
    return wp_probs