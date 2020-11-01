import numpy as np


def sample(p, x0, num_steps, reset_every):
    
    D = x0.shape[0]
    
    directions = np.zeros(shape=(D, D))
    
    # Outer loop
    for n in range(N):
        
        # Number of steps per loop
        for d in range(D):
            
            # Compute the direction to sample in
            direction = orthogonal_direction_by_gram_schmidt(p, directions[:d])
            
            # Sample in this direction
            p_ = lambda x : p(x)[0]
            ## Sampler like a-star or slice sampling goes here
            
            # Update direction memory
    
    