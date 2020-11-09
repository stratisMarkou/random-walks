import numpy as np


def slice_sample(x0, unnorm_log_prob, expand_method, expand_params, with_shrinkage):
    
    f0 = unnorm_log_prob(x0)
    y = np.log(np.exp(f0) * np.random.rand())
    
    L = None
    R = None
    
    if expand_method == 'step_out':
        w, m = expand_params
        L, R, _ = step_out_expansion(x0, y, unnorm_log_prob, w, m)
        
    elif expand_method == 'double':
        w, p = expand_params
        L, R, _ = double_expansion(x0, y, unnorm_log_prob, w, p)
        
    x = sample_acceptable_set(x0=x0,
                              y=y,
                              L=L,
                              R=R,
                              unnorm_log_prob=unnorm_log_prob,
                              expand_method=expand_method,
                              expand_params=expand_params,
                              with_shrinkage=with_shrinkage)
    
    return x, y


def step_out_expansion(x0, y, unnorm_log_prob, w, m):
    
    U = np.random.rand()
    L = x0 - w * U
    R = L + w
    
    Lhist = [L]
    Rhist = [R]
    
    J = np.floor(m * np.random.rand())
    K = m - 1 - J
    
    fL = unnorm_log_prob(L)
    fR = unnorm_log_prob(R)
    
    while J > 0 and y <= fL:
        
        L = L - w
        J = J - 1
        fL = unnorm_log_prob(L)
        
        Lhist.append(L)
        
    while K > 0 and y <= fR:
        
        R = R + w
        K = K - 1
        fR = unnorm_log_prob(R)
        
        Rhist.append(R)
        
    return L, R, (Lhist, Rhist)


def double_expansion(x0, y, unnorm_log_prob, w, p):
    
    U = np.random.unform()
    L = x0 - w * U
    R = L + w
    K = p
    
    Lhist = [L]
    Rhist = [R]
    
    fL = unnorm_log_prob(L)
    fR = unnorm_log_prob(R)
    
    while K > 0 and (fL > y or fR > y):
        
        V = np.random.uniform()
        
        if V > 0.5:
            L = L - (R - L)
            fL = unnorm_log_prob(L)
            
        else:
            R = R + (R - L)
            fR = unnorm_log_prob(R)
        
        Lhist.append(L)
        Rhist.append(R)
        
        K = K - 1
            
    return L, R, (Lhist, Rhist)


def sample_acceptable_set(x0, y, L, R, unnorm_log_prob, expand_method, expand_params, with_shrinkage):
    
    L0, R0 = L, R
    
    while True:
        
        x = L + (R - L) * np.random.rand()
        
        accept = is_acceptable(x, y, L0, R0, unnorm_log_prob, expand_method, expand_params)
        
        if accept:
            return x
        
        elif with_shrinkage and x <= x0:
            L = x
            
        elif with_shrinkage and x > x0:
            R = x
            
            
def is_acceptable(x, y, L, R, unnorm_log_prob, expand_method, expand_params):
    
    # Function value at candidate point
    f = unnorm_log_prob(x)
    
    # For stepping out, check x is in the slice (y < f)
    if expand_method == 'step_out':
        
        if y <= f:
            return True
        
        else:
            return False
    
    # For doubling, check the doubling sequence can be recreated the other way
    elif expand_method == 'double':
        
        w, p = expand_params
        
        fx = unnorm_log_prob(x)
        
        while R - L > 1.5 * w:
            
            M = (R + L) / 2
            
            fL = unnorm_log_prob(L)
            fM = unnorm_log_prob(M)
            fR = unnorm_log_prob(R)
            
            if x >= M and (y < fM or y < fR): L = M
                
            elif x < M and (y < fL or y < fM): R = M
            
            else: return False
            
        # If the point is not rejcected in the loop, it is acceptable
        return True
            