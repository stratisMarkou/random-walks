import numpy as np

def kalman_filter_smoother(log_nsr, t, y):
    """
    
    """
    
    # Set arrays to store means and variances
    N = t.shape[0]
    m = np.zeros(shape=(N, 3))
    V = np.zeros(shape=(N, 3, 3))
    
    # Noise variance to signal (θ) variance ratio
    n2 = np.exp(log_nsr)
    
    # Time intervals between observations
    dt = t[1:] - t[:-1]
    
    # Time dependent state space model matrices
    A = lambda t : np.array([[1, t, t ** 2 / 2],
                             [0, 1, t],
                             [0, 0, 1]])
    
    Q = lambda t : np.array([[t ** 5 / 20, t ** 4 / 8, t ** 3 / 6],
                             [t ** 4 / 8, t ** 3 / 3, t ** 2 / 2],
                             [t ** 3 / 6, t ** 2 / 2, t]])
    
    # Time independent state space model matrices
    C = np.eye(3)[:2, :]
    R = np.array([[n2, 0],
                  [0, 0]])
    
    # Hard code initial filtering step
    V22 = np.array([[n2 * dt[0] ** 5 + 120 * n2 ** 2, 0, - 40 * n2 * dt[0] ** 3],
                    [0, 0, 0],
                    [- 5 * n2 * dt[0] ** 3, 0, dt[0] ** 6 / 8 + 80 * n2 * dt[0]]])
    V22 = V22 / (dt[0] ** 5 + 240 * n2)

    # Kalman matrices for computing the mean
    K1 = np.eye(3)[:, :-1]
    K2 = np.array([[dt[0] ** 6 + 120, 60 * n2 * dt[0] ** 2],
                   [0, dt[0]],
                   [- 5 * dt[0] ** 4, 7 / 2 * dt[0] ** 5 + 60 * n2]])
    K2 = K2 / (dt[0] ** 6 + 240 * n2 * dt[0])
    
    # Computing M = I - K2C and L = M A K1
    M = np.eye(3) - np.dot(K2, C)
    L = np.dot(M, np.dot(A(dt[0]), K1))
    m22 = np.dot(L, y[0, :]) - np.dot(K2, y[1, :])
    
    # Set second step filtered mean and variance
    m[1, :] = m22
    V[1, :, :] = V22
    
    # Filtering steps
    for i in range(2, N):
        
        # Set A and Q matrices for current time
        At = A(dt[i-1])
        Qt = Q(dt[i-1])
        
        S = np.dot(At, np.dot(V[i-1, :], At.T)) + Qt
        y_minus_CAm = y[i, :] - np.dot(C, np.dot(At, m[i-1, :]))
        
        m[i, :] = np.dot(At, m[i-1, :]) + kalman_dot(y_minus_CAm, S, C, R)
        V[i, :] = np.dot(np.eye(3) - kalman_dot(C, S, C, R), S)
        
    return m, V
    
    
def kalman_dot(array, V, C, R):
    
    R_CVCT = R + np.dot(C, np.dot(V, C.T))
    R_CVCT_inv_array = np.linalg.solve(R_CVCT, array)
    
    K_array = np.dot(V, np.dot(C.T, R_CVCT_inv_array))
    
    return K_array