import autograd.numpy as np
from autograd.scipy.stats import norm

def kalman_filter_smoother(t, y, log_nsr):
    
    # Set arrays to store means and variances, compute time differences
    T = t.shape[0]
    mf = np.zeros(shape=(T, 3))
    Vf = np.zeros(shape=(T, 3, 3))
    ms = np.zeros(shape=(T, 3))
    Vs = np.zeros(shape=(T, 3, 3))
    S = np.zeros(shape=(T, 3, 3))
    CV = np.zeros(shape=(T - 1, 3, 3))
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
    ms, Vs, CV = smooth_backward(dt, y, mf, Vf, S, ms, Vs, CV, C, R)
    
    # Compute the first smoothed posterior
    ms, Vs, CV = smoother_finalise(dt, y, mf, ms, Vs, CV, n2)
    
    # Adjust variances by overal scale parameter
    Vf = theta2 * Vf
    Vs = theta2 * Vs
        
    return mf, Vf, ms, Vs, CV, theta2, nlml


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


def smooth_backward(dt, y, mf, Vf, S, ms, Vs, CV, C, R):
    
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
        CV[i] = np.dot(Vs[i+1], J.T)
        
    return ms, Vs, CV


def smoother_finalise(dt, y, mf, ms, Vs, CV, n2):
        
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
    
    CV[0] = np.dot(Vs[1], J.T)
    
    return ms, Vs, CV
    
    
def kalman_dot(array, V, C, R):
    
    R_CVCT = R + np.dot(C, np.dot(V, C.T))
    R_CVCT_inv_array = np.linalg.solve(R_CVCT, array)
    
    K_array = np.dot(V, np.dot(C.T, R_CVCT_inv_array))
    
    return K_array


def post_pred(t, t_data, ms, Vs, CV):
    
    # Index of first datapoint to the right of time t (datapoint 2)
    i = np.searchsorted(t_data, t)
    
    # Time difference from datapoint to left of t
    dt1 = t - t_data[i-1]
    
    # Check if interpolating or extrapolating
    if i < t_data.shape[0]:
        
        # Time difference to datapoint to right of t
        dt2 = t_data[i] - t
        
        # If interpolating, use interpolating posterior
        return int_post_pred(dt1, ms[i-1], Vs[i-1], dt2, ms[i], Vs[i], CV[i-1])
    
    else:
        # Otherwise, use extrapolating posterior
        return ext_post_pred(dt1, ms[-1], Vs[-1])
    

def int_post_pred(dt1, m1, V1, dt2, m2, V2, CV):
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

    V = np.dot(iQ2A2.T, np.dot(V2, iQ2A2))
    V = V + np.dot(iQ1A1, np.dot(V1, iQ1A1.T))
    V = V + np.dot(iQ2A2.T, np.dot(CV, iQ1A1.T))
    V = V + np.dot(iQ1A1, np.dot(CV.T, iQ2A2))
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


def log_expected_improvement(f0, m, v):
    
    # Posterior standard deviation and normalised difference
    s = v ** 0.5
    z = (f0 - m) / s
    
    # Compute log expected improvement differently, depending on size of z
    if z > -20:
        return np.log((f0 - m) * norm.cdf(z) + s * norm.pdf(z))
    
    else:
        return - 0.5 * np.log(2 * np.pi) - 0.5 * z ** 2 - np.log(z ** 2 - 1)
    
    
    
def newton(objective, budget, t0, tmin, tmax, t_data, ms, Vs, CV):
    
    min_t = tmin + 1e-1 * (tmax - tmin)
    max_t = tmax - 1e-1 * (tmax - tmin)
    
    f0, df0, ddf0 = objective(t0, t_data, ms, Vs, CV)
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

        f, df, ddf = objective(t, t_data, ms, Vs, CV)
        budget = budget - 1
            
        if f < f0:
            t0, f0, df0 = t, f, df
            
        elif t0 == t:
            break
        
    t = min(max(t, min_t), max_t)
    
    f, df, ddf = objective(t, t_data, ms, Vs, CV)
    budget = budget - 1
        
    return t, f



def wolfe_powell(ms, Vs)