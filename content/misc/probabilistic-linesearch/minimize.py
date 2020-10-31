import numpy as np

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
    mf, Vf, S, nlml, s2 = filter_forward(dt, y, mf, Vf, S, C, R)
    
    # Backward smoothing steps
    ms, Vs, CV = smooth_backward(dt, y, mf, Vf, S, ms, Vs, CV, C, R)
    
    # Compute the first smoothed posterior
    ms, Vs, CV = smoother_finalise(dt, y, mf, ms, Vs, CV, n2)
        
    return mf, Vf, ms, Vs, CV


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
    
    quad = 0
    logdet = 0
    
    for i in range(2, T):
        
        # Set A and Q matrices for current time
        At = A(dt[i-1])
        Qt = Q(dt[i-1])
        
        S[i] = np.dot(At, np.dot(Vf[i-1, :], At.T)) + Qt
        diff = y[i, :] - np.dot(C, np.dot(At, mf[i-1, :]))
        
        mf[i, :] = np.dot(At, mf[i-1, :]) + kalman_dot(diff, S[i], C, R)
        Vf[i, :] = S[i] - kalman_dot(np.dot(C, S[i]), S[i], C, R)
        
        R_CSCT = R + np.dot(C, np.dot(S[i], C.T))
        
        quad = quad + 0.5 * np.dot(diff, np.linalg.solve(R_CVCT, diff))
        logdet = logdet + 0.5 * np.linalg.slogdet(R_CSCT)[1]
        
    
        
    return mf, Vf, S, nlml, s2


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