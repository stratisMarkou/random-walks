# Branching processes

## Stochastic and brancing processes

This chapter deals with branching processes, which is a particular type of stochastic process. We make a brief digression to define stochastic processes{cite}`spweiss` for completeness.

<div class='definition'>

**Definition (Stochastic process)** A stochastic process is a family of random variables $\{X(t), t\in \mathcal{I}\}$ on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$, where $\mathcal{I}$ is a set called the index set.

</div>
<br>

Stochastic processes can take discrete or continuous values and can have a discrete or continuous index set $\mathcal{I}$. The branching process describes how a population evolves at discrete time intervals, and therefore takes discrete values and has a discrete index set $\mathcal{I}$.

<div class='definition'>

**Definition (Branching process)** A branching process is a collection of random variables $X_0, X_1, X_2, ...$, representing a population of *nomads* which evolves as follows:
    
1. At $t = 0$ there is one nomad, $X_0 = 1$.
2. At every time-step, each nomad dies after giving birth to a *family* of new nomads of random size $C$.
3. The family sizes descending from each nomad are i.i.d. and are distributed according to the pmf $\mathbb{P}(C = k) = p_k, k = 0, 1, 2 ...$, called the *family-size distribution*.

</div>
<br>

## Probability generating functions

We are interested in the distribution of the nomad population at future times. The recursive nature of the process gives a neat expression in terms of the generating function of the family-size distribution.

<div class='theorem'>

**Theorem (Probability generating functions of a branching process)** Let $X_t$ be a branching process with family-size distribution $\mathbb{P}(C = k) = p_k$, whose probability generating function is $G$. Then the probability generating functions $G_0, G_1, ...$ of $X_0, X_1, ...$ are
    
$$\begin{align}
G_0(s) = s, G_{t+1}(s) = G_t(G(s)), \text{ for } t = 1, 2, ... .
\end{align}$$

</div>
<br>


<details class="proof">
<summary>Proof: Proability generating functions of a branching process</summary>
    
Let $C_{t, n}$ be the family size born from the $n^{th}$ nomad at time $t$. At $t = 0$, the population is $X_0 = 1$ so that $G_0(s) = s$. For $t > 0$ we have

$$\begin{align}
G_{t + 1} &= \mathbb{E}_{X_{t + 1}}\left[s^{X_{t + 1}}\right]\\
&= \mathbb{E}_{X_t}\left[\mathbb{E}_{C_{t, 1}, C_{t, 2}, ... C_{t, X_t}}\left[s^{X_{t + 1}} | X_t \right]\right]\\
&= \mathbb{E}_{X_t}\left[G(s)^{X_t}\right]\\
&= G_t(G(s)),
\end{align}$$
    
where the subscripts in the expectations give the variables over which the expectation is taken. From the first to the second line we used the law of iterated expectations; from the second to the third we used the fact that the $C_{t, 1}, C_{t, 2}..., C_{t, X_t}$ variables are i.i.d. so the pgf of their sum is equal to the product of their pgfs.
    
</details>
<br>

## Mean population

<div class='theorem'>

**Theorem (Mean population of a branching process)** The mean value of a branching process $X_t$ is
    
$$\begin{align}
\mathbb{E}(X_t) = \mu^t,
\end{align}$$

where $\mu = \mathbb{E}(C)$ is the mean family size. From this, it follows that as $t \to \infty$

$$\begin{align}
\mathbb{E}(X_t) \to \begin{cases}
0 & \text{ if } \mu < 1\\
1 & \text{ if } \mu = 1\\
\infty & \text{ if } \mu > 1
\end{cases}
\end{align}$$

</div>
<br>

This result is not surprising since each nomad will give birth to $\mu$ other nomads on average. It can be proved quickly using probability generating functions.

<details class="proof">
<summary>Proof: Mean population of a branching process</summary>
    
We have 
    
$$\begin{align}
\mathbb{E}(X_t) &= \frac{d}{ds} G_t(s) \bigg \vert_{s = 1}\\
&= G_{t - 1}'(G(1))G'(1)\\
&= G_{t - 1}'(1)\mu
\end{align}$$
    
and considering that $G_{t - 1}'(1) = \mathbb{E}(X_{t-1})$, the result follows by induction.
    
</details>
<br>

## Ultimate extinction

We are also interested in the behaviour of the process as $t \to \infty$. If the population ever reaches $X_t = 0$, it will have become extinct.

<div class='definition'>

**Definition (Extinction probability)** Given a branching process $X_t$, the extinction probability $e$ is
    
$$\begin{align}
e = \mathbb{P}(X_t = 0 \text{ for some } t \geq 0).
\end{align}$$
    
Alternatively, defining $E_t = \{X_t = 0\}$ as the event that the process is extinct by time $t$ and $e_t = \mathbb{P}(E_t)$ we have
    
$$\begin{align}
\{X_t = 0 \text{ for some } t \geq 0\} = \bigcup^\infty_{t = 0} E_t,
\end{align}$$

and since $E_t \subseteq E_{t+1}$ we have $e = \lim_{t \to \infty} e_t$ by the continuity of probability measures. Thus $e$ can equivalently be defined as the limit of $e_t$ as $t \to \infty$.

</div>
<br>

We are interested in the probability of ultimate extinction, that is the probability that $X_t = 0$ for some $t$. Again, generating functions give a neat answer for this quantity too.

<div class='theorem'>

**Theorem (Extinction probability theorem)** Let $X_t$ be a branching process, whose family sizes $C$ have common probability generating function $G$. The probability of extinction $e$ is the smallest non-negative root of the equation
    
$$\begin{align}
x = G(x).
\end{align}$$

</div>
<br>

<details class="proof">
<summary>Proof: Extinction proability theorem</summary>
    
We have $e_t = \mathbb{P}(X_t = 0) = G_t(0)$ and $G_{t + 1}(s) = G(G_t(s))$ so that
    
$$\begin{align}
e_{t + 1} &= G_{t + 1}(0)\\
&= G(G_t(0)) \\
&= G(e_t) \\
\end{align}$$
    
Taking the limit $t \to \infty$ with initial condition $e_0 = 0$, we obtain
    
$$\begin{align}
e &= \lim_{t \to \infty} e_t\\
\implies G(e) &= G\left(\lim_{t \to \infty} e_t\right)\\
&= \lim_{t \to \infty} G(e_t)\\
&= \lim_{t \to \infty} e_{t+1}\\
& \\
&= e\\
\implies e &= G(e)
\end{align}$$
    
where we have used the fact that $G$ is continuous on $[0, 1]$. To show that $e$ is the smallest non-negative root, suppose $\eta \geq 0$ is another non-negative root. Since $G$ is non-decreasing on $[0, 1]$, we have
    
$$\begin{align}
e_1 &= G(0) \leq G(\eta) = \eta\\
e_2 &= G(e_1) \leq G(\eta) = \eta\\
&~~\vdots\\
e &\leq \eta
\end{align}$$
    
</details>
<br>

The following theorem gives a necessary and sufficient condition for ultimate extinction to be certain.

<div class='theorem'>

**Theorem (Extinction survival theorem)** Let $X_t$ be a branching process whose family size distribution satisfies $\mathbb{P}(C = 1) \neq 1$. The probability of ultimate extinction satisfies $e = 1$ if and only if the mean family size satisfies $\mu \leq 1$.

</div>
<br>

<details class="proof">
<summary>Proof: Extinction survival theorem</summary>
    
In the trivial case where $\mathbb{P}(C = 1) = 1$ we have $X_t = 1$ for all $t$ and $e = 0$. Now considering the facts that on the interval $[0, 1]$, the function $G$ is
    
1. continuous, since it is a power series with a radius of convergence of at least $1$,
2. non-decreasing, since $G'(x) \geq 0$,
2. convex, since $G''(x) \geq 0$,
4. $G(1) = 1$,
    
we see that the graph of $y = G(x)$ will intersect the graph of $y = x$ at $x = 1$, and that the two graphs will have a smaller non-negative point of intersection if and only if $G'(1) > 1$. The condition $e = 1$ holds if and only if the smallest non-negative point of intesection is $1$, which is equivalent to the condition $G'(1) = \mu \leq 1$, arriving at the result.
    
</details>
<br>

From the definition of the probability of extinction, it follows that if $\mu \leq 0$, then $X_t \to 0$ in probability. Further, if the inequality is strict, $\mu < 1$, then $X_t \to 0$ in mean square - this does not hold for $\mu = 1$.


<details class="proof">
<summary>Proof: Convergence of a branching process in probability and in mean-square</summary>
    
To show that $X_t \to 0$ in probability, suppose $\mu \leq 1$, let $\epsilon > 0$ and consider
    
$$\begin{align}
\mathbb{P}(X_t > \epsilon) &= 1 - \mathbb{P}(X_t \leq \epsilon)\\
&= 1 - \big(\mathbb{P}(X_t = 0) + \mathbb{P}(0 < X_t \leq \epsilon)\big).
\end{align}$$

From the extinction survival theorem, $\mathbb{P}(X_t = 0) \to 1$ as $t \to \infty$ so

$$\begin{align}
\mathbb{P}(X_t > \epsilon) &=  1 - \big(\mathbb{P}(X_t = 0) + \mathbb{P}(0 < X_t \leq \epsilon)\big) \leq 1 - \mathbb{P}(X_t = 0) \to 0, \text{ as } t \to \infty,
\end{align}$$
    
and $X_t \to 0$ in probability. We now treat the mean-square case. Consider
    
$$\begin{align}
\mathbb{E}(X_t^2) &= \text{Var}(X_t) + \mathbb{E}(X_t)^2.
\end{align}$$
    
Using the law of total variance
    
$$\begin{align}
\text{Var}(X_t) &= \text{Var}_{X_{t - 1}}(\mathbb{E}_{X_t}(X_t | X_{t - 1})) + \mathbb{E}_{X_{t - 1}}(\text{Var}_{X_t}(X_t | X_{t - 1}))\\
&= \text{Var}_{X_{t - 1}}(\mu X_{t-1}) + \mathbb{E}_{X_{t - 1}}(X_{t - 1} \sigma^2)\\
&= \mu^2 \sigma_{t - 1}^2 + \mu^t \sigma^2
\end{align}$$
    
Proceeding recursively, we obtain
    
$$\begin{align}
\sigma_1^2 &= \sigma^2 \\
\sigma_2^2 &= \mu \sigma^2 + \mu^2 \sigma^2\\
&~\vdots \\
\sigma_t^2 &= \mu^{t-1} \sigma^2 + \mu^t \sigma^2 + ... + \mu^{2t - 1} \sigma^2,
\end{align}$$
    
which is a geometric sum. In the special case of $\mu = 1$, we see that $\sigma_t^2 = t \sigma^2$. If $\mu \neq 1$, we can use the geometric sum to obtain
    
$$\begin{align}
\sigma_t^2 &= \sigma^2 \mu^{t - 1} \frac{1 - \mu^t}{1 - \mu}.
\end{align}$$
    
Substituting these results into the expression for $\mathbb{E}(X_t^2)$ we obtain
    
$$\begin{align}
\mathbb{E}(X_t^2) = \begin{cases}
1 + t\sigma^2 & \text{ if } \mu = 1\\
\mu^{2t} + \sigma^2 \mu^{t - 1} \frac{1 - \mu^t}{1 - \mu} & \text{ if } \mu \neq 1.
\end{cases}
\end{align}$$
    
Therefore $\mathbb{E}(X_t^2) \to 0$, implying that $X_t \to 0$ in mean-square if and only if $\mu < 1$.
  
</details>
<br>


## References

```{bibliography} ./references.bib
```
