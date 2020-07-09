# Numerical simulation of SDEs

This is a reproduction of certain scripts found in Higham, *An algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations.*{cite}`higham` This paper is an accessible introduction to SDEs, centered around ten MATLAB scripts. Here, I have reproduced eight of them in Python and added some notes, skipping over the sections on linear stability.

Stochastic differential equations (SDEs) describe the evolution of stochastic processes which take values in a continuous space, and are indexed by a continuous time variable. Whereas ordinary differential equations (ODEs) describe a variables which change according to a deterministic rule, SDEs describe variables whose change is governed partly by a deterministic component and partly by a stochastic component. SDEs are therefore an appropriate model for systems whose dynamics involve some true randomness, or some fine grained complexity which we cannot afford to or do not wish to model.

import numpy as np
import matplotlib.pyplot as plt

from IPython.display import HTML, set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')
css_style = open('../../../_static/custom_style.css', 'r').read()
HTML(f'<style>{css_style}</style>')

## The Wiener Process

The Wiener process is a stochastic process that is not only of interest in itself, but is also used as the stochastic component in SDEs.

<div class="definition">
    
**Definition (Wiener process)** A *standard Wiener process* over [0, T] is a random variable $W(t)$ that depends continuously on $t \in [0, T]$ and satisfies:

1. W(0) = 0, with probability 1.
2. For $0 \leq t_1 < t_2 \leq T$ the random variable $W(t_2) - W(t_1)$ has distribution $\mathcal{N}(0, t_2 - t_1)$.
3. For $0 \leq t_1 < t_2 < t_3 < t_4 \leq T$, the random variables $W(t_2) - W(t_1)$ and $W(t_4) - W(t_3)$ are independent.
    
</div>

<br>

We can imagine the Wiener process as the path followed by a particle that experiences infinitely many, infinitesimal kicks. The size of these kicks, $W(t_2) - W(t_1)$, diminishes as the interval between them, $t_2 - t_1$, diminishes. The kicks are also independent from each other, so the future path of the particle is independent of its past path given its present position.

## Sampling from a Wiener process

How can we draw a sample $W_t$ from a Wiener process? Since a sample from the Wiener process takes a random value for every $t \in [0, \infty)$, the best we can do on a computer is to sample the process at a finite subset of time instances. We specify the times $t_1, t_2, ..., t_N$ at which to sample $W_t$, and then use the definition of the Wiener process to see that we should sample as follows:

$$\begin{align}
W_{t_{n+1}} = W_{t_{n}} + \Delta W_{t_{n}}, \text{ where } \Delta W_{t_{n}} \sim \mathcal{N}(0, t_{n+1} - t_n),
\end{align}$$

where $W_{t_0} = W_{0} = 0$. We can therefore sample all the $\Delta W_{t_n}$ independently, and take their cumulative sum to compute $W_{t_n}$.

# Set random seed
np.random.seed(0)

# Time to simulate for and level of discretisation
T = 1
N = 500
dt = T / N

# Times to sample at
t = np.linspace(0, T, N)[:, None]

# Sample dW's and compute cumulative sum
dW = dt ** 0.5 * np.random.normal(size=(N - 1, 1))
W = np.concatenate([[0], np.cumsum(dW)])

plt.figure(figsize=(6, 4))
plt.plot(t, W, color='k')

plt.xticks(np.linspace(0, T, 6))
plt.yticks(np.linspace(-2, 2, 5))
plt.xlim([0, 1])
plt.ylim([-2, 2])

plt.title('Discretised sample from Weiner process')
plt.xlabel('Time (t)')
plt.ylabel('Position (x)')
plt.show()

So even though we can't represent the entirety of the path, we can sample it to arbitrary precision.

## Function of a Wiener process

If we are interested in a stochastic process which is a function of a Wiener process, say

$$\begin{align}
X_t = \exp\left(t + \frac{1}{2}W_t\right)
\end{align}$$

we can sample $W_t$ first, then pass it through the function to get the corresponding values of $X_t$. We'll draw `S = 1000` samples of $X_t$, compute their mean, standard deviation and show three of these samples.

# Set random seed 
np.random.seed(0)

# Time to simulate for, discretisation level and number of paths
T = 1
N = 500
S = 1000
dt = T / N

# Times to sample at
t = np.linspace(0, T, N)

# Sample dW's and compute cumulative sum
dW = dt ** 0.5 * np.random.normal(size=(N - 1, S))
W = np.concatenate([np.zeros(shape=(1, S)), np.cumsum(dW, axis=0)], axis=0)

# Compute values 
X = np.exp(t[:, None] + 0.5 * W)
X_mean = np.mean(X, axis=1)
X_stdev = np.var(X, axis=1) ** 0.5

plt.figure(figsize=(6, 4))
plt.plot(t, X[:, 0], color='r', label='Sample 1')
plt.plot(t, X[:, 1], color='g', label='Sample 2')
plt.plot(t, X[:, 2], color='b', label='Sample 3')

plt.plot(t, X_mean, color='k', label='Mean')
plt.fill_between(t,
                 X_mean - 2 * X_stdev,
                 X_mean + 2 * X_stdev,
                 color='gray',
                 alpha=0.3,
                 label='Std. dev.')

plt.xticks(np.linspace(0, T, 6))
plt.yticks(np.linspace(0, 6, 4))
plt.xlim([0, 1])
plt.ylim([0, 6])

plt.title(r'Samples from $\exp\left(t + \frac{1}{2} W_t\right)$')
plt.xlabel('Time (t)')
plt.ylabel('Value (x)')
plt.legend()
plt.show()

## Evaluating a stochastic integral

The next thing that we're interested in is evaluating a stochastic integral. Stochastic integrals turn out to be a whole different chapter from the usual deterministic integrals.

# Set random seed
np.random.seed(3)

# Time to simulate for and discretisation level
T = 1
N = int(1e6)
dt = T / N

# Sample dW's and compute cumulative sum
dW = dt ** 0.5 * np.random.normal(size=(N,))
W = np.concatenate([[0], np.cumsum(dW)])

# Evaluate the Ito integral
ito_approx = np.sum(W[:-1] * dW)
ito_exact = 0.5 * W[-2] ** 2 - 0.5 * T

# The Wiener process must be evaluated at the midpoints to evaluate the Stratonovich integral
W_midpoint = (W[:-1] + W[1:]) / 2
W_midpoint = W_midpoint + np.random.normal(0, (dt / 4) ** 0.5, size=(N,))

# Evaluate the Stratonovich integral
strat_approx = np.sum(W_midpoint * dW)
strat_exact = 0.5 * W[-2] ** 2

print(f'Ito integral approximation (exact): {ito_approx:.3f} ({ito_exact:.3f})')
print(f'Stratonovich approximation (exact): {strat_approx:.3f} ({strat_exact:.3f})')

## Euler-Maruyama method

The Euler-Maruyama method is the analoge of the Euler method for deterministic integrals, applied to the stochastic case.

<div class="definition">
    
**Definition (Euler-Maruyama method)** Given a scalar SDE with drift and diffusion functions $f$ and $g$
    \begin{align}dX(t) = f(X(t))dt + g(X(t)) dW(t),\end{align}
    the Euler-Maruyama method approximates $X$ by
    \begin{align} X_{j + 1} = X_j + f(X_j) \Delta t + g(X_j) \Delta W_j,\end{align}
    where $\Delta t > 0$ is the time step, $X_j = X(\tau_j), W_j = W(\tau_j)$ and $\tau_j = j\Delta t$.
    
</div>
<br>

The `euler_maruyama` function takes the *drift* and *diffusion* functions $f$, $g$ and applies the EM algorithm (not to be confused with Expectation Maximisation), from the specified initial conditions. Note that we can sample the `dW` in advance.

def euler_maruyama(seed, X0, T, N, f, g):
    
    # Set random seed
    np.random.seed(seed)
    
    # Set discretisation, initial value and times at which to evaluate
    dt = T / N
    X = [X0]
    t = np.linspace(0, T, N + 1)
    
    # Sample Wiener process dW's
    dW = dt ** 0.5 * np.random.normal(size=(N,))
    
    for i in range(N):
        
        # Apply Euler-Maruyama at each point in time
        dX = f(X[-1], t[i]) * dt + g(X[-1], t[i]) * dW[i]
        
        # Store the new X
        X.append(X[-1] + dX)
    
    # Compute W to return it at the end
    W = np.concatenate([[0], np.cumsum(dW)])
    
    return t, X, W

Below is the definition of `f` and `g` that we will be integrating, namely

$$\begin{align}
f(x, t) &= \lambda x,\\
g(x, t) &= \mu x,
\end{align}$$

known as the Black-Scholes model. This is implemented as a closure, i.e. `f_g_black_scholes` takes in the appropriate `lambda` and `mu` and returns the corresponding `f` and `g`.

def f_g_black_scholes(lamda, mu):
    
    def f(X, t):
        return lamda * X
    
    def g(X, t, grad=False):
        return mu if grad else mu * X
    
    return f, g

Higham chose these drift and diffusion terms because the associated SDE has a closed form solution, with which we can compare our numerical solution. The analytic solution to the Black-Scholes model is

$$\begin{align}
X_t = X_0 \exp \left[\Big(\lambda - \frac{1}{2} \mu^2\Big)~t + \mu W_t\right],
\end{align}$$

which we implement in `exact_black_scholes` below. Unlike deterministic differential equations, where the solution is a unique function, the solution of an SDE depends on the random noise sample $W_t$. In particular, an analytic solution to an SDE is still a stochastic process, where the dependence on $t$ and $W_t$ is written in closed form. It's important to note that a different $W_t$ sample will lead to a different $X_t$ solution, so the EM solution and the exact solution must share the same $W_t$.

def exact_black_scholes(X0, t, W, lamda, mu):
    return X0 * np.exp((lamda - 0.5 * mu ** 2) * t + mu * W)

We are can now run the EM method and compare it aginst the exact solution below.

# Black-Scholes parameters
lamda = 2
mu = 1

# Seed and integration parameters
seed = 0
X0 = 1
T = 1
N = int(1e2)

# Get drift and diffusion functions of the Black-Scholes model
f, g = f_g_black_scholes(lamda=lamda, mu=mu)

# Solve approximately via the EM method
t, X, W = euler_maruyama(seed=seed, X0=X0, T=T, N=N, f=f, g=g)

# Get the exact solution for the same W sample
X_exact = exact_black_scholes(X0=X0, t=t, W=W, lamda=lamda, mu=mu)

plt.figure(figsize=(6, 4))
plt.plot(t, X_exact, color='k', zorder=1, label='Exact solution')
plt.scatter(t, X, s=20, marker='x', color='red', zorder=2, label='Euler-Maruyama')

plt.xlim([0, T])
plt.xticks(np.linspace(0, 1, 6))
plt.yticks(np.linspace(0, 8, 5))
plt.title('Euler-Maruyama and exact solutions of Black-Scholes model')
plt.xlabel('t')
plt.ylabel('$X_t$')
plt.legend()
plt.show()

We can change the accuracy of the solution by changing $N$ appropriately - more of this in the convergence section. As a fun aside, what if we try out a different drift term? One nice choice is

$$\begin{align}
f(x, t) &= \omega~\text{cos}(\omega t),\\
g(x, t) &= \mu x.
\end{align}$$

In the case $\mu = 0$, the solution is the deterministic function $X_t = \text{sin}(\omega t)$. When $\mu \neq 0$, the solution will be perturbed by the gaussian noise, hopefully in an interesting way.

def f_g_sine(omega, mu):
    
    def f(X, t):
        return omega * np.cos(omega * t)
    
    def g(X, t):
        return mu * X
    
    return f, g

# SDE parameters
omega = 2. * np.pi
mu = 0.3

# Seed and integration parameters
seed = 0
X0 = 1
T = 2
N = int(1e3)

# Get drift and diffusion functions of our sine model
f, g = f_g_sine(omega=omega, mu=mu)

# Solve approximately via the EM method
t, X, W = euler_maruyama(seed=seed, X0=X0, T=T, N=N, f=f, g=g)

plt.scatter(t, X, s=1, marker='x', color='red', zorder=2, label='Euler-Maruyama')

plt.xlim([0, T])
plt.xticks(np.linspace(0, T, 6))
plt.yticks(np.linspace(-3, 3, 5))
plt.title('Euler-Maruyama solution of sine model')
plt.xlabel('t')
plt.ylabel('$X_t$')
plt.legend()
plt.show()

## Strong and weak convergence

<div class="definition">
    
**Definition (Strong convergence)** A method for approximating a stochastic process $X(t)$ is said to have strong order of convergence $\gamma$ if there exists a constant such that
    \begin{align}\mathbb{E}|X_n - X(\tau_n)| \leq C\Delta t^\gamma\end{align}
    for any fixed $\tau_n = n\Delta t \in [0, T]$ and $\Delta t$ sufficiently small.

</div>
<br>

A weaker condition for convergence is the amount by which the expected values of the stochastic process depart from each other. 

<div class="definition">
    
**Definition (Weak convergence)** A method for approximating a stochastic process $X(t)$ is said to have weak order of convergence $\gamma$ if there exists a constant such that
    \begin{align}|\mathbb{E}[X_n] - \mathbb{E}[X(\tau_n)]| \leq C\Delta t^\gamma\end{align}
    for any fixed $\tau_n = n\Delta t \in [0, T]$ and $\Delta t$ sufficiently small.

</div>
<br>

The paper states without proof that, under conditions on $f$ and $g$, Euler-Maruyama has strong order of convergence $\frac{1}{2}$ and weak order of convergence $1$. We do not provide a proof for any of the above statements, but instead evaluate the rate of convergence empirically, as in the paper.

def parallel_euler_maruyama(seed, num_paths, X0, T, N, f, g):
    
    np.random.seed(seed)
    
    dt = T / N
    
    X = X0 * np.ones(shape=(num_paths, N + 1))
    
    t = np.linspace(0, T, N + 1)
    
    dW = dt ** 0.5 * np.random.normal(size=(num_paths, N))
    
    for i in range(N):
        
        X[:, i+1] = X[:, i] + f(X[:, i], t[i]) * dt + g(X[:, i], t[i]) * dW[:, i]
        
    W = np.concatenate([np.zeros(shape=(num_paths, 1)), np.cumsum(dW, axis=1)], axis=1)
    
    return t, X, W

lamda = 2
mu = 1

seed = 0
X0 = 1
T = 1
Ns = (10 ** np.linspace(2, 4, 4)).astype(dtype=np.int)
num_paths = int(1e4)

f, g = f_g_black_scholes(lamda=lamda, mu=mu)

dts = []
X_abs_diffs = []

for N in Ns:
    
    t, X, W = parallel_euler_maruyama(seed=seed, num_paths=num_paths, X0=X0, T=T, N=N, f=f, g=g)
    X_exact = exact_black_scholes(X0=X0, t=t[None, :], W=W, lamda=lamda, mu=mu)
    
    dts.append(T / N)
    
    X_abs_diff = np.abs(X[:, -1] - X_exact[:, -1])
    X_abs_diffs.append(X_abs_diff)
    
X_abs_diffs = np.stack(X_abs_diffs, axis=0)
em_strong_errors = np.mean(X_abs_diffs, axis=1)

plt.plot(dts, em_strong_errors, color='k')
plt.loglog()
plt.yticks([1e-2, 1e-1, 1e0])
plt.xlabel(r'$\Delta t$', fontsize=20)
plt.ylabel(r'$\mathbb{E}|X_n - X(\tau_n)|$', fontsize=20)
plt.title('Euler-Maruyama strong convergence', fontsize=20)
plt.show()

lamda = 2
mu = 1

seed = 0
X0 = 1
T = 1
Ns = (10 ** np.linspace(2, 4, 4)).astype(dtype=np.int)
num_paths = int(1e4)

f, g = f_g_black_scholes(lamda=lamda, mu=mu)

dts = []
X_approx = []
X_exacts = []

for N in Ns:
    
    t, X, W = parallel_euler_maruyama(seed=seed, num_paths=num_paths, X0=X0, T=T, N=N, f=f, g=g)
    X_exact = exact_black_scholes(X0=X0, t=t[None, :], W=W, lamda=lamda, mu=mu)
    
    dts.append(T / N)
    X_approx.append(X[:, -1])
    X_exacts.append(X_exact[:, -1])
    
X_approx = np.stack(X_approx, axis=0)
X_exacts = np.stack(X_exacts, axis=0)

X_approx_means = np.mean(X_approx, axis=-1)
X_exacts_means = np.mean(X_exacts, axis=-1)

em_weak_errors = np.abs(X_approx_means - X_exacts_means)

plt.plot(dts, em_weak_errors, color='k')
plt.loglog()
plt.yticks([1e-3, 1e-2, 1e-1, 1e0])
plt.xlabel(r'$\Delta t$', fontsize=20)
plt.ylabel(r'$|\mathbb{E}X_n - \mathbb{E}X(\tau_n)|$', fontsize=20)
plt.title('Euler-Maruyama weak convergence', fontsize=20)
plt.show()

## Milstein's higher order method

<div class="definition">
    
**Definition (Milstein's method)** Given a scalar SDE with drift and diffusion functions $f$ and $g$
    \begin{align}dX(t) = f(X(t))dt + g(X(t)) dW(t),\end{align}
    the Milstein method approximates $X$ by
    \begin{align} X_{j + 1} = X_j + f(X_j) \Delta t + g(X_j) \Delta W_j + \frac{1}{2}g(X_j)g'(X_j) (\Delta W_j^2 - \Delta t),\end{align}
    where $\Delta t > 0$ is the time step, $X_j = X(\tau_j), W_j = W(\tau_j)$ and $\tau_j = j\Delta t$.
    
</div>
<br>

def parallel_milstein(seed, num_paths, X0, T, N, f, g):
    
    np.random.seed(seed)
    
    dt = T / N
    
    X = X0 * np.ones(shape=(num_paths, N + 1))
    
    t = np.linspace(0, T, N + 1)
    
    dW = dt ** 0.5 * np.random.normal(size=(num_paths, N))
    
    for i in range(N):
        
        # Compute the EM term and the higher order correction term
        dX = f(X[:, i], t[i]) * dt + g(X[:, i], t[i]) * dW[:, i]
        dX = dX + 0.5 * g(X[:, i], t[i]) * g(X[:, i], t[i], grad=True) * (dW[:, i] ** 2 - dt)
        
        X[:, i+1] = X[:, i] + dX
        
    W = np.concatenate([np.zeros(shape=(num_paths, 1)), np.cumsum(dW, axis=1)], axis=1)
    
    return t, X, W

lamda = 2
mu = 1

seed = 0
X0 = 1
T = 1
N = int(1e2)
num_paths = 1

f, g = f_g_black_scholes(lamda=lamda, mu=mu)

t, X, W = parallel_milstein(seed=seed, num_paths=num_paths, X0=X0, T=T, N=N, f=f, g=g)
X_exact = exact_black_scholes(X0=X0, t=t[None, :], W=W, lamda=lamda, mu=mu)

plt.plot(t, X_exact[0, :], color='k', zorder=1, label='Exact solution')
plt.scatter(t, X[0, :], s=20, marker='x', color='red', zorder=2, label='Euler-Maruyama (subsampled)')
plt.legend()
plt.xlim([0, T])
plt.xticks(np.linspace(0, 1, 6))
plt.yticks(np.linspace(0, 8, 5))
plt.title('Milstein solution', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.ylabel('X', fontsize=20)
plt.show()

lamda = 2
mu = 1

seed = 0
X0 = 1
T = 1
Ns = (10 ** np.linspace(2, 4, 4)).astype(dtype=np.int)
num_paths = int(1e4)

f, g = f_g_black_scholes(lamda=lamda, mu=mu)

dts = []
X_abs_diffs = []

for N in Ns:
    
    t, X, W = parallel_milstein(seed=seed, num_paths=num_paths, X0=X0, T=T, N=N, f=f, g=g)
    X_exact = exact_black_scholes(X0=X0, t=t[None, :], W=W, lamda=lamda, mu=mu)
    
    dts.append(T / N)
    
    X_abs_diff = np.abs(X[:, -1] - X_exact[:, -1])
    X_abs_diffs.append(X_abs_diff)
    
X_abs_diffs = np.stack(X_abs_diffs, axis=0)
mil_strong_errors = np.mean(X_abs_diffs, axis=1)

plt.plot(dts, em_strong_errors, color='k')
plt.loglog()
plt.yticks([1e-2, 1e-1, 1e0])
plt.xlabel(r'$\Delta t$', fontsize=20)
plt.ylabel(r'$\mathbb{E}|X_n - X(\tau_n)|$', fontsize=20)
plt.title('Milstein strong convergence', fontsize=20)
plt.show()

lamda = 2
mu = 1

seed = 0
X0 = 1
T = 1
Ns = (10 ** np.linspace(2, 4, 4)).astype(dtype=np.int)
num_paths = int(1e4)

f, g = f_g_black_scholes(lamda=lamda, mu=mu)

dts = []
X_approx = []
X_exacts = []

for N in Ns:
    
    t, X, W = parallel_milstein(seed=seed, num_paths=num_paths, X0=X0, T=T, N=N, f=f, g=g)
    X_exact = exact_black_scholes(X0=X0, t=t[None, :], W=W, lamda=lamda, mu=mu)
    
    dts.append(T / N)
    X_approx.append(X[:, -1])
    X_exacts.append(X_exact[:, -1])
    
X_approx = np.stack(X_approx, axis=0)
X_exacts = np.stack(X_exacts, axis=0)

X_approx_means = np.mean(X_approx, axis=-1)
X_exacts_means = np.mean(X_exacts, axis=-1)

mil_weak_errors = np.abs(X_approx_means - X_exacts_means)

plt.plot(dts, mil_weak_errors, color='k')
plt.loglog()
plt.yticks([1e-3, 1e-2, 1e-1, 1e0])
plt.xlabel(r'$\Delta t$', fontsize=20)
plt.ylabel(r'$|\mathbb{E}X_n - \mathbb{E}X(\tau_n)|$', fontsize=20)
plt.title('Milstein weak convergence', fontsize=20)
plt.show()

## Stochastic chain rule

Suppose we want to evaluate a function $V(\cdot)$ at various $X(t)$, i.e. $V(X(t))$. If $X(t)$ were a deterministic quantity, such as the solution to an ODE, we could solve for $X(t)$ and plug it into $V$. Alternatively, we could express the evolution of $V$ itself as a differential equation using the chain rule:

\begin{align}
dV &= \frac{dV}{dX}dX = \frac{dV}{dX} f(t) dt, \text{ where } dX = f(t) dt,\\
\end{align}

This way, we could solve the following ODE directly for $V$

\begin{align}
\frac{dV}{dt} &= \frac{dV}{dX} f(t).
\end{align}

For an autonomous SDE however the chain rule takes a different form, which under the Ito definition is as follows.

<div class="theorem">
    
**Definition (Ito's result for one dimension)** Let $X_t$ be an Ito process given by

\begin{align}
    dX_t = U_t dt + H_t dW_t.
\end{align}
    
where $U_t, H_t$ are square-integrable processes, and let $V(X, t)$ be a twice continuously differentiable function. Then $Y_t = V(X_t, t)$ is again an Ito process and
    
\begin{align}
    dY_t = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial X} dX_t + \frac{1}{2}\frac{\partial^2 V}{\partial X^2} V_t^2 dt. 
\end{align}
    
If $V$ does not depend on $t$, we have
    
\begin{align}
    dY_t = \left(\frac{\partial V}{\partial X} U_t + \frac{1}{2}\frac{\partial^2 V}{\partial X^2} H_t^2 \right) dt + \frac{\partial V}{\partial X}H_t dW_t. 
\end{align}
    
</div>
<br>

For a more formal definition and proof of Ito's result see {cite}`oksendal` (Theorem 4.1.8 and pages 44-48). Below is a short sketch proof, which highlights why the additional term appears in this example.

<details class="proof">
<summary>Informal argument: Ito's result for one dimension</summary>

<div>
    
Writing the infinitesimal difference in $Y_t$ as a Taylor expansion we get
\begin{align}
    dY_t = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial X} dX_t + \frac{1}{2} \left[\frac{\partial^2 V}{\partial^2 X} dX_t^2 + 2 \frac{\partial^2 V}{\partial X \partial t} dt dX_t + \frac{\partial^2 V}{\partial t^2} dt^2 \right] + o(dt^2),
\end{align}
where the $o(dt^n)$ notation means that the ratio of the term being ommited, to the infinitesimal $dt^n$ goes to 0 as $dt \to 0$. Now since $dX_t = U_t dt + H_t dW_t$ and $dW_t$ is of order $dt^{1/2}$, the last two terms in the square brackets are $o(dt^{3/2})$ and we can neglect them. The reference provides a formal argument for neglecting these terms, showing that their contribution to the Ito integral has zero mean and a variance that tends to 0 as $dt \to 0$ - these contributions converge to $0$ in the sense of mean square convergence.
    
However, the first term is of order $dt$ and does not vanish. In particular
\begin{align}
    dX_t^2 = U_t^2 dt^2 + 2 U_tH_t dW_t dt + H_t^2 dW_t^2.
\end{align}
In the above expression, we can neglect the first two terms which are of order $dt^{3/2}$ and larger. Again, here the formal argument is that their associated contributions to the Ito integral converge to 0 in mean square. This yields the expression
\begin{align}
    dY_t = \frac{\partial V}{\partial X} U_t dt + \frac{1}{2}\frac{\partial^2 V}{\partial X^2} H_t^2 dW_t^2 + \frac{\partial V}{\partial X}H_t dW_t. 
\end{align}
Now consider the contribution to the Ito integral of the last term, i.e. the sum
\begin{align}
    \sum_{n = 1}^N \frac{\partial^2 V}{\partial X^2}\Bigg \vert_{X_{t_n}} H_{t_n}^2 dW_{t_n}^2 = \sum_{n = 1}^N a_n dW_{t_n}^2,
\end{align}
where $t_n = n~dt$ and $N = T / dt$. This sum has expectation $\sum_{n = 1}^N a_n dt$ and it can be shown that its variance goes to 0 as $dt \to 0$, so the contribution converges to $\sum_{n = 1}^N a_n dt$ in mean square and we can write
\begin{align}
    dY_t = \left(\frac{\partial V}{\partial X} U_t + \frac{1}{2}\frac{\partial^2 V}{\partial X^2} H_t^2 \right) dt + \frac{\partial V}{\partial X}H_t dW_t. 
\end{align}

    
 
</div>

</details>
<br>

With this corrected rule, we can directly

## References

```{bibliography} ./num-sde-ref.bib
```

