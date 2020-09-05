# Processes in continuous time

## Poisson process

<div class='definition'>

**Definition (Poisson process)** A Poisson process $N_t$ is a stochastic process with a continuous index set $\mathcal{I} = [0, \infty)$ which
    
1. Takes values in the range $\{0, 1, 2, ... \}$,
2. Is initially zero $N_0 = 0$,
3. Is nondecreasing $s \leq t \implies N_s \leq N_t$,
4. Satisfies the independence relation $0 \leq s < t \implies N_s \perp \!\!\! \perp N_t - N_s$.
5. For some number $\lambda > 0$, called the arrival rate, it satisfies

$$\begin{align} \mathbb{P}(N_{t + h} = n + 1 | N_t = n) &= \lambda h + o(h),\\
\mathbb{P}(N_{t + h} = n | N_t = n) &= 1 - \lambda h + o(h).
\end{align}$$

</div>
<br>



<div class='theorem'>

**Theorem (Marginal distribution of a Poisson process)** Let $N_t$ be a Poisson process. Then for any $t > 0$
    
    
$$\begin{align}
\mathbb{P}(N_t = k) = \frac{1}{k!} (\lambda t)^k e^{-\lambda t} & \text{ for } k = 0, 1, 2, ... .
\end{align}$$

</div>
<br>

Below is the textbook proof for the above theorem.

<details class="proof">
<summary>Proof (a): Marginal distribution of a Poisson process</summary>
    
From the definition of a Poisson process, we have 
    
$$\begin{align}
\mathbb{P}(N_{t + h} = n) &= \sum_{k = 0}^\infty \mathbb{P}(N_{t + h} = n | N_t = k) \mathbb{P}(N_t = k)\\
\\
&= \mathbb{P}(N_{t + h} = n | N_t = n) \mathbb{P}(N_t = n) + \mathbb{P}(N_{t + h} = n | N_t = n - 1) \mathbb{P}(N_t = n - 1) \\
\\
&= \left(1 - \lambda h\right) \mathbb{P}(N_t = n) + \lambda h \mathbb{P}(N_t = n - 1) + o(h).
\end{align}$$
    
Using the notation $p_k(t) = \mathbb{P}(N_t = k)$, we obtain the differential equation
    
$$\begin{align}
p_n'(t) = \lambda p_{n - 1}(t) - \lambda p_n(t),
\end{align}$$
    
for $n \geq 1$, while for $n = 0$ we obtain
    
$$\begin{align}
p_0'(t) = - \lambda p_0(t).
\end{align}$$
    
Considering the generating function of $N_t$
    
$$\begin{align}
G(s, t) = \sum^\infty_{k = 0} p_k(t)s^k,
\end{align}$$
    
and taking sums over both sides of the differential equation, we obtain
    
$$\begin{align}
\sum^\infty_{k = 1} p_k'(t)s^k &= \lambda \sum^\infty_{k = 1} p_{k - 1}(t)s^k - \lambda \sum^\infty_{k = 1} p_k(t)s^k.
\end{align}$$
    
Adding each side of the equation $p_0'(t) = - \lambda p_0(t)$ to each side of the above equations, we obtain
    
$$\begin{align}
\sum^\infty_{k = 0} p_k'(t)s^k &= \lambda \sum^\infty_{k = 1} p_{k - 1}(t)s^k - \lambda \sum^\infty_{k = 0} p_k(t)s^k,
\end{align}$$
    
and arrive at the differential equation
    
$$\begin{align}
\frac{\partial G}{\partial t} = \lambda s G - \lambda G.
\end{align}$$
    
Integrating the differential equation with respect to $t$ we obtain
    
$$\begin{align}
\log G = \lambda t (s - 1) + A(s).
\end{align}$$

The boundary condition
    
$$\begin{align}
G(s, 0) = \sum^\infty_{k = 0} p_k(0) s^k = 1.
\end{align}$$
    
implies $\log G(s, 0) = 0 = A(s)$, so
    
$$\begin{align}
G(s, t) = e^{\lambda t (s - 1)} = \sum_{k = 0}^\infty \left[\frac{1}{k!} (\lambda t)^k e^{-\lambda t} s^k\right] .
\end{align}$$
    
This, together with the {ref}`uniqueness theorem for moments<prob-intro-moments>` implies that
    
$$\begin{align}
p_n(t) = \frac{1}{n!} (\lambda t)^n e^{- \lambda t}.
\end{align}$$

</details>
<br>
    
    
A shorter proof is given below.
    
    
<details class="proof">
<summary>Proof (b): Marginal distribution of a Poisson process</summary>

Consider the family of random variables $Z_1(t), Z_2(t), ...$ where
    
$$\begin{align}
Z_N(t) = \sum^N_{n = 1} B_{N, n},
\end{align}$$
    
where $B_{N, n}$ are i.i.d. Bernoulli distributed random variables with parameter $p = \lambda \frac{t}{N}$. The characteristic function of $B_{N, n}$ is given by
    
$$\begin{align}
\phi_{B_{N, n}}(u) = \mathbb{E}\left[e^{iuB_{N, n}}\right] = 1 - \lambda \frac{t}{N} + \lambda \frac{t}{N} e^{iu} + o\left(\frac{t}{N}\right).
\end{align}$$
    
Now, using the independence of the $B_{N, n}$ variables and {ref}`the properties of the characteristic function<prob-intro-char-funcs>` we obtain
    
$$\begin{align}
\phi_{Z_N}(u) = \left[1 - \lambda \frac{t}{N} + \lambda \frac{t}{N} e^{iu} + o\left(\frac{t}{N}\right) \right]^{\lambda t N}.
\end{align}$$
    
As $N \to \infty$, the sequence of characteristic functions converges to the limit
    
$$\begin{align}
\phi_{Z_N}(u) \to e^{\lambda t (e^{iu} - 1)} = \phi_Z(u)
\end{align}$$

which is the characteristic function of a random variable $Z(t)$ that is Poisson-distributed with parameter $\lambda t$. From this and the {ref}`continuity theorem for characteristic functions<prob-intro-char-cont>`, $Z_N(t)$ converges to $Z(t)$ in distribution. All $Z_N(t)$ satisfy properties (1), (2) and (3) of the definition of the Poisson process. For any $h > 0$, there exists $N$ large enough such that properties (4) and (5) are also satisfied, so in the $N \to \infty$ limit, $Z_N(t) = Z(t)$ satisfies all the properties in the definition of the Poisson process and is therefore a Poisson process.
    
</details>
<br>