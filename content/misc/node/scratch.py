import numpy as np
from scipy.integrate import ode as ODE
from matplotlib import pyplot as plt


import tensorflow as tf
import tensorflow.keras as tfk
import tensorflow_probability as tfp

tfd = tfp.distributions


class NODE(tf.Module):
    
    def __init__(self, hidden_size, state_size, dtype, name='node'):
        
        super().__init__()
        
        self.dtype = dtype
        
        self.state_size = state_size
        
        self.W1 = tf.random.normal(shape=(state_size, hidden_size),
                                   mean=0.,
                                   stddev=state_size**-0.5,
                                   dtype=dtype)
        self.W1 = tf.Variable(self.W1)
        
        self.b1 = tf.random.normal(shape=(1, hidden_size),
                                   mean=0.,
                                   stddev=1.,
                                   dtype=dtype)
        self.b1 = tf.Variable(self.b1)
        
        self.W2 = tf.random.normal(shape=(hidden_size, state_size),
                                   mean=0,
                                   stddev=hidden_size**-0.5,
                                   dtype=dtype)
        self.W2 = tf.Variable(self.W2)
        
        self.b2 = tf.random.normal(shape=(1, state_size),
                                   mean=0.,
                                   stddev=1.,
                                   dtype=dtype)
        self.b2 = tf.Variable(self.b2)
        
    
    def f(self, t, z):
        
        z = tf.convert_to_tensor(z, dtype=self.dtype)
        z = tf.reshape(z, (-1, self.state_size))
        
        f = tf.einsum('ni, ij -> nj', z, self.W1)
        f = f + self.b1
        
        f = tf.cast(tf.tanh(f), dtype=self.dtype)
        
        f = tf.einsum('ni, ij -> nj', f, self.W2)
        f = f + self.b2
        
        return f
    
    
    def backward_dynamics(self, t, za):
        """
        params za : tf.tensor, concatenated state and adjoint (B * (2 * Z + P),)
        
        returns tensor of shape (B * (2 * Z + P),)
        """
        
        num_params = tf.reduce_sum([tf.reduce_prod(tensor.shape) for tensor in self.trainable_variables])
        last_dim = 2 * self.state_size + num_params
        
        za = tf.convert_to_tensor(za, dtype=self.dtype)
        za = tf.reshape(za, (-1, last_dim))
        
        z = za[:, :self.state_size] # (B, Z)
        a = za[:, self.state_size:2*self.state_size] # (B, Z)
        
        with tf.GradientTape(persistent=True) as tape:

            tape.watch(z)
            tape.watch(self.trainable_variables)

            f = self.f(t, z)

        dfdz = tape.batch_jacobian(f, z) # (B, Z, Z) dfdz_ij = (df_i)/dz_j
        dfdz_a = - tf.einsum('nij, ni -> nj', dfdz, a)
        
        dfdtheta = tape.jacobian(f, self.trainable_variables) # list of (B, Z, Pi)
        dfdtheta = [tf.reshape(tensor, (tensor.shape[0], tensor.shape[1], -1)) for tensor in dfdtheta]
        dfdtheta_a = [- tf.einsum('nij, ni -> nj', tensor, a) for tensor in dfdtheta]
        
        augmented_dynamics = tf.concat([f, dfdz_a] + dfdtheta_a, axis=1)
        
        return augmented_dynamics
        
        
    def flatten_tensors(self, tensors):

        flattened = tf.zeros(shape=(0,))
        
        shapes = []
        sizes = []
        
        for tensor in tensors:
            
            tensor = tf.reshape(tensor, (-1,))
            flattened = tf.concat([flattened, tensor], axis=0)
            
            shapes.append(tensor.shape)
            sizes.append(tf.reduce_prod(tensor.shape))
        
        return flattened, shapes, sizes
    
    
    def loglik(self, zpred, zdata):
        """
        params zpred : tf.tensor, predicted state (B, Z)
        params zdata : tf.tensor, data state (B, Z)
        
        where (batch_size, state_size) is (B, Z).
        """

        assert zpred.shape == zdata.shape

        dist = tfd.MultivariateNormalDiag(loc=zpred,
                                          scale_identity_multiplier=1e-1)

        # Loglik of each state dimension, for each datapoint (B, Z)
        loglik = dist.log_prob(zdata)
        
        # Average log likelihood over batch
        loglik = tf.reduce_sum(loglik)

        return loglik
    
    
    def backward_initial_conditions(self, t, z, zdata):
        
        with tf.GradientTape(persistent=True) as tape:
            
            tape.watch(z)
            
            L = - self.loglik(z, zdata)
            
        dLdz = tape.gradient(L, z)
        
        zeros = [tf.zeros(shape=(z.shape[0], tf.reduce_prod(tensor.shape)), dtype=self.dtype) \
                 for tensor in self.trainable_variables]
        
        init_cond = tf.concat([z, dLdz] + zeros, axis=1)
        
        return init_cond
    
dtype = tf.float32
state_size = 2

z0 = 20 * (np.random.uniform(size=(state_size,)) - 0.5)

# Set integration parameters
t0 = 0.
t1 = 10.
num_traj = 100
num_steps = 50
dt = t1 / num_steps

# Hidden size for transition dynamics
hidden_size = 3

# Set state size to 2 for 2D plots
state_size = 2

# New transition dynamics with random weights
node = NODE(hidden_size=hidden_size, state_size=state_size, dtype=dtype)

# Set forward ODE integrator
ode = ODE(f=lambda t, z : tf.reshape(node.f(t, z), (-1,))).set_integrator('vode')
ode = ode.set_initial_value(z0, t0)

# Integrate numerically within time interval
while ode.successful() and ode.t < t1:
    z = ode.integrate(ode.t + dt)
    
print(z.shape)
z1 = z
    
# Set backward ODE integrator
ode = ODE(f=lambda t, z : tf.reshape(node.f(t, z), (-1,))).set_integrator('vode')
ode = ode.set_initial_value(z1, t1)

# Integrate numerically within time interval
while ode.successful() and ode.t > t0:
    z0_ = ode.integrate(ode.t - dt)
    
print(z0, z0_)

# np.save('z0.npy', z0)
# np.save('z1.npy', z1)
# np.save('z0_.npy', z0_)

# z0 = np.load('z0.npy')
# z1 = np.load('z1.npy')
# z0_ = np.load('z0_.npy')
    
za1 = node.backward_initial_conditions(t1,
                                       tf.convert_to_tensor(np.reshape(z1, (-1, 2)), dtype=dtype),
                                       tf.convert_to_tensor(np.reshape(z1, (-1, 2)), dtype=dtype))

za1 = np.array(za1)

print(za1.shape)
print(node.backward_dynamics(1., za1).shape)
    
# Set backward ODE integrator
f = lambda t, za : np.array(tf.reshape(node.backward_dynamics(t, za), (-1,)))
ode = ODE(f=f).set_integrator('vode')
ode = ode.set_initial_value(za1[0, :], t1)

print(5 * '\n')

# Integrate numerically within time interval
while ode.successful() and ode.t > t0:
    print(ode.t)
    za = ode.integrate(ode.t - dt)
    
print(ode.successful())
print(5 * '\n')
print(z0, z1, z0_, za[:2])
print(za)