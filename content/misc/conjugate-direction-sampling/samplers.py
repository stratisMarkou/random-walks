import tensorflow as tf
import tensorflow_probability as tfp
tfd = tfp.distributions

from tensorflow_probability.python.mcmc.internal import slice_sampler_utils as ssu



class CGSSKernel(tfp.mcmc.TransitionKernel):
    
    def __init__(self, log_prob, reset_every):
        
        super().__init__()
        
        self.log_prob = log_prob
        self.epsilon = 1e-3
        self.reset_every = reset_every
        
    
    def is_calibrated(self):
        return True
    
    
    def one_step(self, current_state, previous_kernel_results, seed=None):
        
        x = current_state
        D = previous_kernel_results[0]
        
        d = self.new_conjugate_direction(x, D)
        d = d / tf.reduce_sum(d ** 2, axis=0, keepdims=True) ** 0.5
        cond_log_prob = self.cond_log_prob(x, d)
        
        result = ssu.slice_sampler_one_dim(cond_log_prob,
                                           x_initial=tf.zeros(shape=()),
                                           max_doublings=5,
                                           step_size=1.0*tf.ones(shape=()))
            
        stepsize, _, _, _, _ = result
        x = x + stepsize * d
        
        D = tf.concat([D, d], axis=-1)
        
        if D.shape[1] >= self.reset_every:
            D = D[:, -self.reset_every:]
        
        return x, [D]
    
    def bootstrap_results(self, initial_state):
        return [tf.zeros(shape=(initial_state.shape[0], 0))]
    
    
    def new_conjugate_direction(self, x, D):
        
        _, dl = self.log_prob(x)
        
        if True: D.shape[1] == 0:
#             return dl
            rand = tf.random.uniform(shape=(D.shape[0], 1))
            rand = rand / tf.reduce_sum(rand ** 2)
            return rand
        
        else:
            # Get hessian-gradient products at x, compute conjugate direction
            AD = self.grad_hessian_products(x, D)
            d = self.conjugate_by_gram_schmidt(dl, D, AD)
        
            return d
    
    
    def conjugate_by_gram_schmidt(self, d, D, AD):
        
        DTAD = tf.matmul(D, AD, transpose_a=True)
        DTAd = tf.matmul(AD, d, transpose_a=True)
        a = - tf.linalg.solve(DTAD, DTAd)
        
        d = d + tf.matmul(D, a)
        
        return d
    
        
    def grad_hessian_products(self, x, D):
        
        K = D.shape[-1]
        
        X = tf.tile(x, multiples=[1, K])
        
        _, dl_pos = self.log_prob(X + self.epsilon * D)
        _, dl_neg = self.log_prob(X - self.epsilon * D)
        
        AD = (dl_pos - dl_neg) / (2 * self.epsilon)
        
        return AD
    
    def cond_log_prob(self, x, d):
        return lambda a : self.log_prob(x + a * d)[0]