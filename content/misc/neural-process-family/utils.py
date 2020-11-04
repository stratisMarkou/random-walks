import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf


# =============================================================================
# Exponentiated Quadratic covariance helper
# =============================================================================

def eq_covariance(x1, x2, scale, cov_coeff, noise_coeff):
    
    # Matrices of input differences
    diff = x1[..., :, None, :] - x2[..., None, :, :]
    
    # Quadratic form of EQ, and EQ covariance
    quad = - 0.5 * tf.reduce_sum((diff / scale) ** 2, axis=-1)
    cov = cov_coeff ** 2 * np.exp(quad)
    
    cov = cov + noise_coeff ** 2 * tf.eye(cov.shape[-1],
                                          batch_shape=cov.shape[:-2])
    
    return cov


# =============================================================================
# Helper for sampling data from a GP prior
# =============================================================================


def sample_1d_datasets_from_gp(x_min,
                               x_max,
                               num_datasets,
                               num_datapoints,
                               scale,
                               cov_coeff,
                               noise_coeff):
    
    # Draw inputs uniformly at random within [x_min, x_max]
    x_shape = (num_datasets, num_datapoints)
    x = tf.random.uniform(shape=x_shape, minval=x_min, maxval=x_max)
    
    # Covariance of outputs
    cov = eq_covariance(x[..., None],
                        x[..., None],
                        scale,
                        cov_coeff,
                        noise_coeff)
    
    print(cov.shape)
    # Cholesky factor of covariance
    cov_chol = tf.linalg.cholesky(cov)
    
    # Normal Gaussian noise to multiply by cholesky
    epsilon = tf.random.normal(shape=x.shape)
    
    # Generate data
    y = np.einsum('bij, bj -> bi', cov_chol, epsilon)
    
    return x, y
    