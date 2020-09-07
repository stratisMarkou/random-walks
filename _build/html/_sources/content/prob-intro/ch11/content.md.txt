# Processes in continuous time

## The Poisson process

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

**Theorem (Marginal distribution of a Poisson process)** Let $N_t$ be a Poisson process with rate $\lambda$. Then for any $t > 0$
    
    
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
    
    
An alternative proof that avoids differential equations is given below.
    
    
<details class="proof">
<summary>Proof (b): Marginal distribution of a Poisson process</summary>

Consider the sequence of random variables $Z_1(t), Z_2(t),~...$ defined by
    
$$\begin{align}
Z_N(t) = \sum^N_{n = 1} B_{N, n},
\end{align}$$
    
where $B_{N, n}$ are i.i.d. Bernoulli-distributed random variables with parameter $p = \lambda \frac{t}{N}$. The first part of this proof shows that the sequence $Z_N(t)$ converges in distribution to $N_t$, and the second shows that the limiting distribution is Poisson with parameter $\lambda t$.
    
    
First, we show that the sequence $Z_N(t)$ converges in distribution to $N_t$. By the definition of $Z(t)$, we have
    
$$\begin{align}
\mathbb{P}(Z_N = k) &=  \sum_{\mathcal{u}_N \in \mathcal{B}_N} \prod_{n = 1}^N \mathbb{P}(B_{N, n} = b_{N, n}) \\
&= \sum_{\mathcal{u}_N \in \mathcal{B}_N} \prod_{n = 1}^N \left(\lambda \frac{t}{N}\right)^{b_{N, n}} \left(1 - \lambda \frac{t}{N}\right)^{1 - b_{N, n}}
\end{align}$$
    
where the sum is over $\mathcal{B}_N$, the set of all binary $N$-tuples $\mathcal{u}_N = (b_{N, 1}, b_{N, 2}, ..., b_{N, N})$ such that $b_{N, n} \in \{0, 1\}$ and $\sum_{n = 1}^N b_{N, n} = k$. Then from the definition of $N_t$
    
$$\begin{align}
\mathbb{P}(N_t = k) &= \sum_{\mathcal{v}_N \in \mathcal{C}_N} \prod_{n = 1}^N \mathbb{P}(N_{t + nh} = c_{N, n} | N_{(n - 1)h} = c_{N, n - 1}) \\
&= \sum_{\mathcal{v}_N \in \mathcal{C}_N} \prod_{n = 1}^N \left(\lambda \frac{t}{N} + o\left(\frac{t}{N}\right)\right)^{c_{N, n} - c_{N, n - 1}} \left(1 - \lambda \frac{t}{N} + o\left(\frac{t}{N}\right)\right)^{1 - (c_{N, n} - c_{N, n - 1})}
\end{align}$$
    
where the sum is over $\mathcal{C}_N$, the set of all binary $N$-tuples $\mathcal{v}_N = (c_{N, 1}, c_{N, 2}, ..., c_{N, N})$ such that $c_{N, 1} \in \{0, 1\}$, $c_{N, N} = k$ and $c_{N, n + 1} - c_{N, n} \in \{0, 1\}$ for $n > 1$. Noting the correspondence between the sets $\mathcal{B}_N$ and $\mathcal{C}_N$ and their elements, and taking the limit $N \to \infty$ we obtain
    
$$\begin{align}
\lim_{N \to \infty} \mathbb{P}(Z_N = k) = \mathbb{P}(N_t = k).
\end{align}$$
    
We now show that $Z(t) = \lim_{N \to \infty} Z_N(t)$ is Poisson-distrbuted. The characteristic function of $B_{N, n}$ is
    
$$\begin{align}
\phi_{B_{N, n}}(u) = \mathbb{E}\left[e^{iuB_{N, n}}\right] = 1 - \lambda \frac{t}{N} + \lambda \frac{t}{N} e^{iu} + o\left(\frac{1}{N}\right).
\end{align}$$
    
Using the independence of the $B_{N, n}$ variables and {ref}`the independence property of the characteristic function<prob-intro-char-funcs>` we obtain
    
$$\begin{align}
\phi_{Z_N}(u) = \left[1 - \lambda \frac{t}{N} + \lambda \frac{t}{N} e^{iu} + o\left(\frac{t}{N}\right) \right]^{\lambda t N}.
\end{align}$$
    
As $N \to \infty$, the sequence of characteristic functions converges to the limit
    
$$\begin{align}
\phi_{Z_N}(u) \to e^{\lambda t (e^{iu} - 1)}
\end{align}$$

which is the characteristic function of a random variable $Z(t)$ that is Poisson-distributed with parameter $\lambda t$, so $N_t$ is also Poisson-distributed with parameter $\lambda t$.
    
</details>
<br>
    
    
## Arrival and Inter-arrival times
    
    
<div class='definition'>

**Definition (Arrival and inter-arrival times of the Poisson process)** Let $N_t$ be a Poisson process with rate $\lambda$. The arrival times $T_0, T_1, ...$ of $N_t$ are defined as $T_0 = 0$ and
    
$$\begin{align}
T_k = \inf \{t : N_t = k\}, \text{ for } k = 1, 2, ... .
\end{align}$$
    
The inter-arrival times $X_1, X_2, ...$ of the process are defined as
    
$$\begin{align}
X_k = T_k - T_{k - 1}, \text{ for } k = 1, 2, ... .
\end{align}$$

</div>
<br>
    
    
<div class='theorem'>

**Theorem (Inter-arrival times of the Poisson process)** Let $N_t$ be a Poisson process with rate $\lambda$. The inter-arrival times $X_1, X_2, ...$ are independent, each having the exponential distribution with parameter $\lambda$.

</div>
<br>
    
Below is an adapted version of the proof in Grimmett and Stirzaker, *Probability and Random Processes*.{cite}`grimstir`
    
<details class="proof">
<summary>Proof: Inter-arrival times of the Poisson process</summary>
    
Let $N_t$ be a Poisson process with parameter $\lambda$ and inter-arrival times $X_1, X_2, ...$. The event $\{X_1 > t\}$ has probability
    
$$\begin{align}
\mathbb{P}(X_1 > t) &= \lim_{h \to \infty} (1 - \lambda h + o(h))^{\frac{t}{h}} \\
&= e^{-\lambda t},
\end{align}$$
    
and $X_1$ is therefore exponentially distributed with parameter $\lambda$. Now considering $X_2$, we have
    
$$\begin{align}
\mathbb{P}(X_2 > t | X_1 = t_1) &= \mathbb{P}(\text{no arrivals in } (t_1, t_1 + t] | X_1 = t_1)\\
&= \mathbb{P}(\text{no arrivals in } (t_1, t_1 + t])\\
&= \lim_{h \to \infty} (1 - \lambda h + o(h))^{\frac{t}{h}} \\
&= e^{-\lambda t},
\end{align}$$
    
where to go from the first to the second line we used the following fact. The event $\{X_1 = t_1\}$ is determined by the number of arrivals occuring during $[0, t_1]$ whereas the event $\{\text{no arrivals in } (t_1, t_1 + t]\}$ is determined by the number of arrivals during $(t_1, t_1 + t]$. By the independence property of the Poisson process, the numbers of arrivals during these two intervals are independent and therefore the two events are also independent. Therefore $X_1$ and $X_2$ are independent and $X_2$ is also exponentially distributed with parameter $\lambda$. Proceeding recursively yields the result.
    
</details>
<br>
    
    
## Lack of memory property
    
    
<div class='definition'>

**Definition (Lack-of-memory property)** A positive random variable $X$ is said to have the lack-of-memory property if
    
$$\begin{align}
\mathbb{P}(X > u + v | X > u) = \mathbb{P}(X > v).
\end{align}$$

</div>
<br>
    
    
<div class='theorem'>

**Theorem (Lack-of-memory $\iff$ exponentially distributed)** The continuous random variable $X$ has the lack of memory property if and only if it is exponentially distributed.

</div>
<br>
    
<details class="proof">
<summary>Proof: Lack-of-memory \(\iff\) exponentially distributed</summary>
    
To see that the exponential distribution has the lack-of-memory property, let $X$ be exponentially distributed with parameter $\lambda$ and consider
    
$$\begin{align}
\mathbb{P}(X > u + v | X > u) &= \frac{\mathbb{P}(X > u + v)}{\mathbb{P}(X > u)} \\
&= \frac{e^{-\lambda (u + v)}}{e^{-\lambda u}} \\
&= e^{-\lambda v} \\
&= \mathbb{P}(X > v).
\end{align}$$
    
To show that a continuous random variable $X$ which has the lack-of-memory property, must be exponentially distributed, consider
    
$$\begin{align}
\mathbb{P}(X > u + v | X > u) = \mathbb{P}(X > v) \implies \mathbb{P}(X > u + v) = \mathbb{P}(X > u)\mathbb{P}(X > v)
\end{align}$$
    
Therefore, the continuous function $G(\cdot) = \mathbb{P}(X > \cdot)$ satisfies

$$\begin{align}
G(u + v) = G(u)G(v), \text{ for } u, v \geq 0.
\end{align}$$
    
It follows that for any non-zero integer $n$

$$\begin{align}
G(n) = G(1)^n,
\end{align}$$
    
and similarly, for any rational $u = \frac{a}{b}$ where $a, b$ are integers, we have
    
$$\begin{align}
G\left(\frac{a}{b}\right)^b &= G\left(a\right) = G\left(1\right)^a,
\end{align}$$
    
from which it follows that $G(u) = G(1)^u$. This relation holds for all rational $u$, and by the continuity of $G$ it also holds for all real numbers. Finally, since $G(u)$ is monotonic decreasing, it must be the case that $0 < G(1) < 1$, so defining $\lambda = - \log G(1)$ we arrive at
    
$$\begin{align}
G(u) = \mathbb{P}(X > u) = e^{-\lambda t}, \text{ for some } \lambda > 0,
\end{align}$$
    
so $X$ must be exponentially distributed with some parameter $\lambda > 0$.

</details>
<br>
    
    
## Simple birth process
    
    
<div class='definition'>

**Definition (Simple birth process)** A simple birth process, $M_t$, is a stochastic process describing the evolution of a population, such that
    
1. The initial population is an integer $I$, $M_0 =  I$,
2. There exists a number $\lambda > 0$ called the birth rate, such that during the interval $(t, t + h]$, each organism of the population has a probability of dividing into two organisms, equal to $\lambda h + o(h)$ and a probability of not dividing equal to $1 - \lambda h + o(h)$,
3. For each organism at time $t$, its future divisions are independent of its past divisions, as well as the divisions of all other organisms present at time $t$.

</div>
<br>
    

<div class='theorem'>

**Theorem (Population distribution of the simple birth process)** Let $M_t$ be a simple birth process with rate $\lambda$, and initial population $M_0 = I$. Then
    
$$\begin{align}
\mathbb{P}(M_t = k) = {k - 1 \choose I - 1} e^{-I\lambda t}(1 - e^{-\lambda t})^{k - I}, \text{ for } k = I, I + 1, ... .
\end{align}$$
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Population distribution of the simple birth process</summary>
    
Let $p_k(t) = \mathbb{P}(M_t = k)$ and consider
    
$$\begin{align}
\mathbb{P}(M_t = k) &= \sum_{i = 0}^\infty \mathbb{P}(M_t = k | M_t = i) \mathbb{P}(M_t = i)\\
&= \left[1 - \lambda k h + o(h)\right]\mathbb{P}(M_t = k | M_t = k) + \left[\lambda (k - 1) h + o(h)\right]\mathbb{P}(M_t = k | M_t = k - 1) + o(h).
\end{align}$$
    
Subtracting $p_k(t)$ from both sides and taking the $h \to 0$ limit, we obtain
    
$$\begin{align}
p_k'(t) = \lambda (k - 1)p_{k - 1}(t) - \lambda k p_k(t) & \text{ for } k = I, I + 1, ... ,
\end{align}$$

with $p_{I - 1}(t) = 0$ and boundary conditions
    
$$\begin{align}
p_k(0) = \begin{cases}
1 & \text{ if } k = I, \\
0 & \text{ if } k \neq I.
\end{cases}
\end{align}$$
    
Therefore for $k = I$
    
$$\begin{align}
p_I'(t) = - \lambda I p_I(t) \implies p_I(t) = e^{-\lambda I t}.
\end{align}$$

</details>
<br>
  

## Birth and death process
    
<div class='definition'>

**Definition (Birth and death process)** A birth and death process, $L_t$, is a stochastic process describing the evolution of a population, such that
    
1. The initial population is an integer $I$, $M_0 =  I$,
2. There exists a number $\lambda > 0$ called the birth rate, such that during the interval $(t, t + h]$, each organism of the population has a probability of dividing once into two organisms, equal to $\lambda h + o(h)$ and a probability of dividing more than once is $o(h)$,
3. There exists a number $\mu > 0$ called the death rate, such that during the interval $(t, t + h]$ each organism has a probability $\mu h + o(h)$ of dying,
3. For each organism at time $t$, its future activity (divisions or death) is independent of its past activity, as well as the activities of all other organisms present at time $t$.

</div>
<br>
    
    
<div class='theorem'>

**Theorem (PGF of birth and death process)** Let $L_t$ be a birth and death process with birth rate $\lambda$ and death rate $\mu > 0$, and initial population $L_0 = I$. Then its pgf is
    
$$\begin{align}
\mathbb{E}(s^{L_t}) = \begin{cases}
\left(\frac{\lambda t (1 - s) + s}{\lambda t (1 - s) + 1}\right)^I & \text{ if } \mu = \lambda \\
\left(\frac{\mu (1 - s) - (\mu - \lambda s)e^{t(\mu - \lambda)}}{\lambda (1 - s) - (\mu - \lambda s)e^{t(\mu - \lambda)}}\right)^I & \text{ if } \mu \neq \lambda.
\end{cases}
\end{align}$$
    
</div>
<br>
    
    
<div class='theorem'>

**Theorem (Extinction of birth and death process)** Let $L_t$ be a birth and death process with birth rate $\lambda$ and death rate $\mu > 0$, and initial population $L_0 = I$. The probability $e(t) = \mathbb{P}(L_t = 0)$ that the probability is extinct by time $t$ tends to
    
$$\begin{align}
e(t) \to \begin{cases}
1 & \text{ if } \lambda \leq \mu, \\
\left(\frac{\mu}{\lambda}\right)^I & \text{ if } \lambda > \mu.
\end{cases}
\end{align}$$
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Extinction of birth and death process</summary>

Let $L_t$ be a birth and death process with birth rate $\lambda$ and death rate $\mu > 0$, and initial population $L_0 = I$. If the pgf at time $t$ is $G(s, t)$, then $G(0, t) = \mathbb{P}(L_t = 0)$ and
    
$$\begin{align}
G(0, t) = \begin{cases}
\left(\frac{\lambda t + s}{\lambda t + 1}\right)^I & \text{ if } \mu = \lambda \\
\left(\frac{\mu - \mu e^{t(\mu - \lambda)}}{\lambda - \mu e^{t(\mu - \lambda)}}\right)^I & \text{ if } \mu \neq \lambda.
\end{cases}
\end{align}$$
    
Letting $t \to \infty$ we arrive at the result.

</details>
<br>
    
    

## First come, first served queue
    
<div class='definition'>

**Definition (First come, first served queue)** A first come, first served queue $Q_t$, is a stochastic process describing the evolution of a system where customers arrive, are queued and served, such that
    
1. The initial number of customers in the queue is an integer $I$, $Q_0 =  I$,
2. Customers arrive in the manner of a Poisson process with rate $\lambda > 0$.
3. The time taken to serve each customer is exponentially distributed with parameter $\mu > 0$, and service times are independent of each other.
4. The inter-arrival times and service times are all independent variables.

</div>
<br>
    
    
    
<div class='theorem'>

**Theorem (Steady state of the first come, first served queue)** Let $Q_t$ be a first come, first served queue with arrival rate $\lambda$ and service rate $\mu > 0$. If $\lambda < \mu$, the queue has a unique steady-state distribution given by
    
$$\begin{align}
\pi_k = \left(1 - \frac{\lambda}{\mu}\right) \left(\frac{\lambda}{\mu}\right)^k, \text{ for } k = 0, 1, 2, ... ,
\end{align}$$
    
independent of $Q_0$. If $\lambda \geq \mu$, there is no steady-state distribution.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Steady state of the first come, first served queue</summary>

Let $Q_t$ be a first come, first served queue with arrival rate $\lambda$ and service rate $\mu > 0$, and write $p_k(t) = \mathbb{P}(Q_t = k)$. Then
    
$$\begin{align}
p_k(t) = \begin{cases}
\lambda p_{k - 1}(t) - (\lambda + \mu) p_k(t) + \mu p_{k + 1}(t) & \text{ if } k \neq 0 \\
- \lambda p_0(t) + \mu p_1(t) & \text{ if } k = 0.
\end{cases}
\end{align}$$
    
Now assume there exists a steady state 
   
$$\begin{align}
\pi_k = \lim_{t \to \infty} p_k(t),
\end{align}$$
    
it will satisfy $p_k'(t) = 0$, so
    
$$\begin{align}
\lambda \pi_{k - 1} - (\lambda + \mu) \pi_k + \mu \pi_{k + 1} &= 0 \\
- \lambda \pi_0 + \mu \pi_1 &= 0.
\end{align}$$
    
Therefore $\pi_1 = \rho \pi_0$ where $\rho = \frac{\lambda}{\mu}$. Continuing recursively
    
$$\begin{align}
\pi_2 &= (1 + \rho) \pi_1 - \rho \pi_0 \\
      &= \rho^2 \pi_0,
\end{align}$$
    
arriving at $\pi_k = \rho^k \pi_0$. If $\rho < 1$ then
    
$$\begin{align}
\sum^\infty_{k = 0} \pi_k = 1 \iff \pi_0 = 1 - \rho,
\end{align}$$
    
arriving at the result
    
$$\begin{align}
\pi_k = \left(1 - \frac{\lambda}{\mu}\right) \left(\frac{\lambda}{\mu}\right)^k.
\end{align}$$
    
On the other hand, if $\rho \geq 1$ $\pi_k$ cannot be a normalised distribution, contradicting our assumption that a steady state exists.

</details>
<br>
    
    
## References

```{bibliography} ./references.bib
```