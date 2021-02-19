import tensorflow as tf
import tensorflow.keras as tfk

import numpy as np
from scipy.integrate import ode as ODE
import matplotlib.pyplot as plt

import sys
from utils import sample_data_from_ou_gp


class NeuralNetwork(tf.Module):

    def __init__(self,
                 input_dim,
                 output_dim,
                 hidden_dims,
                 nonlinearity,
                 dtype,
                 name='neural_network',
                 **kwargs):

        super().__init__(name=name, **kwargs)

        self.dtype = dtype

        shapes = [input_dim] + hidden_dims + [output_dim]
        shapes = [(s1, s2) for s1, s2 in zip(shapes[:-1], shapes[1:])]

        self.W = []
        self.b = []
        self.num_linear = len(hidden_dims) + 1

        with self.name_scope:
            for shape in shapes:
                W = tf.Variable(0 * tf.random.normal(shape=shape, dtype=dtype) /
                                shape[0] ** 0.5)
                b = tf.Variable(0 * tf.random.normal(shape=shape[1:],
                                                 dtype=dtype))

                self.W.append(W)
                self.b.append(b)

        self.nonlinearity = getattr(tf.nn, nonlinearity)

    def __call__(self, tensor):

        for i, (W, b) in enumerate(zip(self.W, self.b)):

            tensor = tf.einsum('...i, ij -> ...j', tensor, W) + b

            if i < self.num_linear - 1:
                tensor = self.nonlinearity(tensor)

        return tensor


    @tf.function
    def dbAdtheta(self, tensor):

        with tf.GradientTape() as tape:

            tensor = self.__call__(tensor) # (D * (D + 1))

        # Leading dimension of tensor (equal to D * (D + 1))
        K = tensor.shape[0]

        grads = tape.jacobian(tensor, self.trainable_variables)
        grads = [tf.reshape(grad, (K, -1)) for grad in grads]
        grads = tf.concat(grads, axis=-1)

        return grads


    def unflatten_parameters(self, flattened):

        N = 0
        unflattened = []

        for variable in self.trainable_variables:

            n = tf.reduce_prod(variable.shape)
            unflattened_ = tf.reshape(flattened[N:N+n], variable.shape)

            unflattened.append(unflattened_)

            N = N + n

        return unflattened


def OU_Esde(gamma, sigma):

    def _OU_Esde(m, S, A, b):

        term1 = (m[0] ** 2 + S[0, 0]) * (A[0, 0] - gamma) ** 2 / (2 * sigma ** 2)
        term2 = - b[0] * m[0] * (A[0, 0] - gamma) / (2 * sigma ** 2)
        term3 = b[0] ** 2 / (2 * sigma ** 2)

        return term1 + term2 + term3

    return _OU_Esde


def moment_dynamics(network, t, z, Sigma, D):

    # Convert input arrays to tensors of the right dtype
    t = tf.convert_to_tensor(t, dtype=network.dtype)
    t = tf.reshape(t, (-1,))
    z = tf.convert_to_tensor(z, dtype=network.dtype)
    Sigma = tf.convert_to_tensor(Sigma, dtype=network.dtype)

    # Unpack current state into mean and covariance
    m = z[:D]
    S = tf.reshape(z[D:], (D, D))

    # Pass t through network and unpack b and A
    bA = network(t)
    b = bA[:D]
    A = tf.reshape(bA[D:], (D, D))

    # ODEs for mean and variance
    dm = - tf.tensordot(A, m, [[1], [0]]) + b
    dS = - tf.matmul(A, S) - tf.matmul(S, A, transpose_b=True) + Sigma

    # Repack mean and variance back into dz
    dS = tf.reshape(dS, (-1,))
    dz = tf.concat([dm, dS], axis=0)

    # Convert back to numpy array
    dz = dz.numpy()

    return dz


def unpack_moment_and_multiplier_dynamics(z, D):

    reshape = np.reshape if type(z) == np.ndarray else tf.reshape

    # Split z into moment part and multiplier part
    zm = z[:(D + D ** 2)]
    zl = z[(D + D ** 2):2*(D + D ** 2)]

    # Unpack state into m, S, Psi, lamda
    m = zm[:D]
    S = reshape(zm[D:], (D, D))
    lamda = zl[:D]
    Psi = reshape(zl[D:], (D, D))

    return m, S, lamda, Psi


def moment_and_multiplier_dynamics(network, Esde, t, z, Sigma, D):

    # Convert input arrays to tensors of the right dtype
    t = tf.convert_to_tensor(t, dtype=network.dtype)
    t = tf.reshape(t, (-1,))
    z = tf.convert_to_tensor(z, dtype=network.dtype)
    Sigma = tf.convert_to_tensor(Sigma, dtype=network.dtype)

    # Unpack dynamics vector
    m, S, lamda, Psi = unpack_moment_and_multiplier_dynamics(z, D)

    # Pass t through network and unpack b and A
    bA = network(t)
    b = bA[:D]
    A = tf.reshape(bA[D:], (D, D))

    # Take gradients of Esde wrt moments
    with tf.GradientTape() as tape:
        tape.watch([m, S, b, A])

        E = Esde(m, S, A, b)

    # Take gradients and reshape
    dE = tape.gradient(E, [m, S, b, A])
    dEdm = dE[0]
    dEdS = tf.reshape(dE[1], (D, D))
    dEdb = dE[2]
    dEdA = tf.reshape(dE[3], (D, D))

    # Gradients of b and A w.r.t. parameters
    dbAdtheta = network.dbAdtheta(t)
    dbdtheta = dbAdtheta[:1, :]
    dAdtheta = dbAdtheta[1:, :]
    dAdtheta = tf.reshape(dAdtheta, (D, D, -1))

    # ODEs for m and S
    dm = - tf.tensordot(A, m, [[1], [0]]) + b
    dS = - tf.matmul(A, S) - tf.matmul(S, A, transpose_b=True) + Sigma

    # ODEs for lambda and Psi
    dlamda = - dEdm + tf.tensordot(A, lamda, axes=[[0], [0]])
    dPsi = - dEdS + 2 * tf.matmul(Psi, A)

    # ODEs for parameter gradients
    dLdtheta = tf.reduce_sum(dEdA[:, :, None] * dAdtheta, axis=[0, 1])
    dLdtheta = dLdtheta + tf.reduce_sum(dEdb[:, None] * dbdtheta, axis=[0])
    dLdtheta = dLdtheta - tf.einsum('ij, jkp, ki -> p', Psi, dAdtheta, S)
    dLdtheta = dLdtheta - tf.einsum('ij, jk, ikp -> p', Psi, S, dAdtheta)
    dLdtheta = dLdtheta - np.einsum('i, ijp, j -> p', lamda, dAdtheta, m)
    dLdtheta = dLdtheta + np.einsum('i, ip -> p', lamda, dbdtheta)

    # Repack m, S, lamda and Psi
    dS = tf.reshape(dS, (-1,))
    dPsi = tf.reshape(dPsi, (-1,))
    dz = tf.concat([dm, dS, dlamda, dPsi, dLdtheta], axis=0)

    # Convert back to numpy array
    dz = dz.numpy()

    return dz


def forward_solve(network, Sigma, m0, S0, t0, t1, dt, atol):

    # State space dimension
    D = m0.shape[0]

    # Convert initial mean and covariance to numpy and pack into z state
    S0 = tf.reshape(S0, (-1,))
    z0 = tf.concat([m0, S0], axis=0)
    z0 = z0.numpy()

    # The moment dynamics function to use in the ODE integrator
    f = lambda t, z: moment_dynamics(network, t, z, Sigma, D)

    # Initialise ODE integrator
    ode = ODE(f=f).set_integrator('vode', atol=atol)
    ode = ode.set_initial_value(z0, t0)

    t = [t0]
    mS = [z0]

    # Integrate forwards
    while ode.successful:
        z = ode.integrate(ode.t + dt)
        t.append(ode.t + dt)
        mS.append(z)
        if ode.t > t1:
            return t, np.array(mS)


def backward_solve(network,
                   t_data,
                   y_data,
                   Sigma,
                   Esde,
                   r,
                   m1,
                   S1,
                   t0,
                   t1,
                   dt,
                   atol):

    # dtype to use
    dtype = m1.dtype

    # State space dimension
    D = m1.shape[0]

    # Convert data tensors to numpy arrays
    t_data = t_data.numpy()
    y_data = y_data.numpy()

    # Convert initial mean and covariance to numpy and pack into z state
    S1 = tf.reshape(S1, (-1,))
    lamda1 = tf.zeros(shape=(D,), dtype=dtype)
    Psi1 = tf.zeros(shape=(D ** 2,), dtype=dtype)
    num_variables = tf.reduce_sum([tf.reduce_prod(v.shape) for v in \
                                   network.trainable_variables])
    theta_zeros = tf.zeros((num_variables,), dtype=dtype)

    z1 = tf.concat([m1, S1, lamda1, Psi1, theta_zeros], axis=0)
    z1 = z1.numpy()

    # The moment dynamics function to use in the ODE integrator
    f = lambda t, z: moment_and_multiplier_dynamics(network=network,
                                                    Esde=Esde,
                                                    t=t,
                                                    z=z,
                                                    Sigma=Sigma,
                                                    D=D)

    t_limits = [(t_data[i], t_data[i+1]) for i in range(len(t_data)-1)]
    t_limits = [(t0, t_data[0])] + t_limits + [(t_data[-1], t1)]
    t_limits.reverse()

    t = [t1]
    zs = [z1]
    z = z1

    for i, (t_left, t_right) in enumerate(t_limits):

        # Initialise ODE integrator
        ode = ODE(f=f).set_integrator('vode', atol=atol)
        ode = ode.set_initial_value(z, t_right)

        # Integrate forwards
        while ode.successful:

            t_ = max(ode.t - dt, t_left)
            z = ode.integrate(t_)

            t.append(t_)
            zs.append(z)

            if ode.t <= t_left + 1e-6:

                if i == len(t_limits)-1:
                    return t, np.array(zs)

                else:
                    z = apply_multiplier_jump(z, y_data[i], r, D)
                    break


def apply_multiplier_jump(z, y, r, D):

    # Unpack moments and multipliers
    m, S, lamda, Psi = unpack_moment_and_multiplier_dynamics(z, D)

    # Dimension of state space
    D = m.shape[0]

    # Compute gradients w.r.t. m and S
    dEdm = (m - y) / r ** 2
    dEdS = np.eye(y.shape[0]) / r ** 2

    # Apply jump conditions
    lamda = lamda + dEdm
    Psi = Psi + dEdS
    Psi = np.reshape(Psi, (-1,))

    # Replace updated values of multipliers
    z[D+D**2:(2*D+D**2)] = lamda
    z[(2*D+D**2):2*(D+D**2)] = Psi

    return z



tf.random.set_seed(0)
#
## ==============================================================================
## Test forward dynamics
## ==============================================================================
#
#input_dim = 1
#output_dim = 2
#hidden_dims = [128, 128, 128]
#nonlinearity = 'relu'
#dtype = tf.float64
#
#network = NeuralNetwork(input_dim=input_dim,
#                        output_dim=output_dim,
#                        hidden_dims=hidden_dims,
#                        nonlinearity=nonlinearity,
#                        dtype=dtype)
#
#Sigma = tf.convert_to_tensor([1.], dtype=dtype)
#m0 = tf.convert_to_tensor([0.], dtype=dtype)
#S0 = tf.convert_to_tensor([5e-1], dtype=dtype)
#t0 = 0.
#t1 = 1.
#dt = 1e-3
#atol = 1e-6
#
#t, mS = forward_solve(network=network,
#                                Sigma=Sigma,
#                                m0=m0,
#                                S0=S0,
#                                t0=t0,
#                                t1=t1,
#                                dt=dt,
#                                atol=atol)
#
#t = np.array(t)[:-1]
#mS = np.array(mS)[:-1]
#
#plt.plot(t, mS[:, 0], color='k', zorder=2)
#plt.fill_between(t,
#                 mS[:, 0] - mS[:, 1] ** 0.5,
#                 mS[:, 0] + mS[:, 1] ** 0.5,
#                 color='gray',
#                 alpha=0.5,
#                 zorder=1)
#plt.ylim([-2, 2])
#plt.show()
#
#
## ==============================================================================
## Test augmented dynamics
## ==============================================================================
#
#D = 1
#
#gamma = 1.
#sigma = 1.
#
#Esde = OU_Esde(gamma=gamma,
#               sigma=sigma)
#
#t0 = 0.
#t1 = t[-1]
#dt = 1e-3
#atol = 1e-6
#z = np.zeros(shape=(2 * D * (D + 1),))
#Sigma = tf.eye(D, dtype=dtype)
#
#m1 = mS[-1, :1]
#S1 = mS[-1, 1:, None]
#
#t_, mS_ = backward_solve(network=network,
#                         Sigma=Sigma,
#                         Esde=Esde,
#                         m1=m1,
#                         S1=S1,
#                         t0=t0,
#                         t1=t1,
#                         dt=dt,
#                         atol=atol)
#
#
#t_ = np.array(t_)
#mS_ = np.array(mS_)[:, :D*(D+1)]
#
#
#plt.plot(t_, mS_[:, 0], color='k', zorder=2)
#plt.fill_between(t_,
#                 mS_[:, 0] - mS_[:, 1] ** 0.5,
#                 mS_[:, 0] + mS_[:, 1] ** 0.5,
#                 color='gray',
#                 alpha=0.5,
#                 zorder=1)
#plt.ylim([-2, 2])
#
#plt.show()
#


# ==============================================================================
# Test gradient descent training
# ==============================================================================

# Network parameters
input_dim = 1
output_dim = 2
hidden_dims = [128, 128]
nonlinearity = 'relu'
dtype = tf.float64

# SDE parameters
Sigma = tf.convert_to_tensor([1.], dtype=dtype)
m0 = tf.convert_to_tensor([0.5], dtype=dtype)
S0 = tf.convert_to_tensor([1.], dtype=dtype)
t0 = 0.
t1 = 10.
D = m0.shape[0]

gamma = 1.
sigma = 1.
r = 1e-2

Esde = OU_Esde(gamma=gamma,
               sigma=sigma)


# Training parameters
num_steps = int(1e3)
learning_rate = 1e-6
dt = 1e-3
atol = 1e-4

# Define network
network = NeuralNetwork(input_dim=input_dim,
                        output_dim=output_dim,
                        hidden_dims=hidden_dims,
                        nonlinearity=nonlinearity,
                        dtype=dtype)

num_variables = tf.reduce_sum([tf.reduce_prod(v.shape) for v in \
                               network.trainable_variables])

# Draw data from OU covariance
t_data = tf.linspace(3., 7., 2)
y_data = sample_data_from_ou_gp(t_data, sigma=sigma, gamma=gamma)[:, None]

optimiser = tfk.optimizers.SGD(learning_rate=learning_rate)

for i in range(num_steps):

    t1  = 10.

    t, mS = forward_solve(network=network,
                          Sigma=Sigma,
                          m0=m0,
                          S0=S0,
                          t0=t0,
                          t1=t1,
                          dt=dt,
                          atol=atol)

    t1 = t[-1]
    m1 = mS[-1, :1]
    S1 = mS[-1, 1:, None]

    t_, z = backward_solve(network=network,
                          Sigma=Sigma,
                          Esde=Esde,
                          t_data=t_data,
                          y_data=y_data,
                          r=r,
                          m1=m1,
                          S1=S1,
                          t0=t0,
                          t1=t1,
                          dt=dt,
                          atol=atol)

    dtheta = z[-1, -num_variables:]
    dtheta = network.unflatten_parameters(dtheta)
    dtheta = [-dtheta_ for dtheta_ in dtheta]

    t_ = np.array(t_)
    lamda = z[:, 2]
    Psi = z[:, 3]

    optimiser.apply_gradients(zip(dtheta, network.trainable_variables))


    if i % 1 == 0:

        t = tf.convert_to_tensor(t, dtype=dtype)
        bA_ = []

        for t__ in t:
            bA_.append(network(t__[None]))

        bA_ = tf.convert_to_tensor(bA_)
        b = bA_[:, 0]
        A = bA_[:, 1]

        plt.plot(t, mS[:, 0], color='k', zorder=2)
        plt.fill_between(t,
                         mS[:, 0] - mS[:, 1] ** 0.5,
                         mS[:, 0] + mS[:, 1] ** 0.5,
                         color='gray',
                         alpha=0.5,
                         zorder=1)
        plt.scatter(t_data.numpy(), y_data.numpy()[:, 0])
        plt.ylim([-2, 2])
        plt.show()

        plt.plot(t_, lamda)
        plt.show()

        plt.plot(t_, Psi)
        plt.show()
