# Random walks

## Simple random walk

<div class='definition'>

**Definition (Simple random walk)** A simple random walk $S_n$ is a stochastic process, with index set $\mathcal{I} = \{0, 1, 2, ...\}$ taking values on the integers $(..., -2, -1, 0, 1, 2, ...)$, such that
    
$$\begin{align}
S_{n + 1} = \begin{cases}
S_n + 1 & \text{ with probability } p \\
S_n - 1 & \text{ with probability } 1 - p
\end{cases}
\end{align}$$
    
where $S_0 \in \{..., -2, -1, 0, 1, 2, ... \}$ is the initial position of the walk. If $p = \frac{1}{2}$ we call the walk symmetric, and asymmetric otherwise.

</div>
<br>

<div class='theorem'>

**Theorem (Return probability of a simple random walk)** The probability $u_n = \mathbb{P}(S_n = S_0)$, that a simple random walk returns to its starting point at time $n$ is
    
    
$$\begin{align}
u_n = \begin{cases}
{2m \choose m} p^m (1 - p)^m & \text{ if } n = 2m \text{ is even}, \\
0 & \text{ if } n \text{ is odd}. \\
\end{cases}
\end{align}$$

</div>
<br>

<details class="proof">
<summary>Proof: Return probability of a simple random walk</summary>
    
The only way for the random walk to return to its initial position at time $n$, is if it makes an equal number of forward and backward steps. This is not possible if $n$ is odd, so in this case $u_n = 0$. If $n = 2m$ is even, there are ${2m \choose m}$ ways to choose $m$ foward and $m$ backward steps and the probability of each of these is $p^m(1-p)^m$, hence
    
$$\begin{align}
u_{2m} = {2m \choose m}p^m (1 - p)^m.
\end{align}$$
    
</details>
<br>


## Recurrence and transience


<div class='definition'>

**Definition (Recurrent and transient walks)** If a walk is bound to revisit its starting point, with probability $1$, it is called recurrent, otherwise it is called transient.

</div>
<br>

<div class='theorem'>

**Theorem (Eventual return probability of a simple random walk)** The probability that a simple random walk ever returns to its starting point is
    
$$\begin{align}
\mathbb{P}(S_n = 0 \text{ for some } n = 1, 2, ... | S_0 = 0) = 1 - |p - q|
\end{align}$$
    
where $q = 1 - p$. Hence the walk is recurrent if and only if $p = q = \frac{1}{2}$.

</div>
<br>


<details class="proof">
<summary>Proof: Eventual return probability of a simple random walk</summary>
    
Let $A_n = \{S_n = 0\}$ be the event that the walk revisits its starting point at time $n$ and
    
$$\begin{align}
B_n = \{S_n = 0, S_k \neq 0 \text{ for } 1 \leq k \leq n - 1\}
\end{align}$$
    
be the event that the first return of the walk occurs at time $n$. If $A_n$ occurs, exactly one of $B_1, B_2, ..., B_n$ occurs, so the events $A_n \cap B_k$ are disjoint and
    
$$\begin{align}
\mathbb{P}(A_n) = \sum^N_{k = 1} \mathbb{P}(A_n \cap B_k).
\end{align}$$
    
Further, since the steps of the walk are conditionally independent from each other, we have $\mathbb{P}(A_n | B_k) = \mathbb{P}(A_{n - k})$ and
    
$$\begin{align}
\mathbb{P}(A_n \cap B_k) &= \mathbb{P}(A_n | B_k)\mathbb{P}(B_k) = \mathbb{P}(A_{n - k})\mathbb{P}(B_k),
\end{align}$$
    
which together with the definitions $u_n = \mathbb{P}(A_n)$ and $f_n = \mathbb{P}(B_n)$ can be substituted in the summation formula to obtain
    
$$\begin{align}
u_n = \sum^n_{k = 1} f_k u_{n - k} \text{ for } n = 1, 2, ... .
\end{align}$$
    
Now introducing the generating functions of the two sequences
    
$$\begin{align}
F(s) &= \sum_{n = 0}^\infty f_n s^n, ~~~ U(s) = \sum_{n = 0}^\infty u_n s^n,
\end{align}$$
    
we can write 
    
$$\begin{align}
\sum_{n = 1}^\infty u_n s^n &= \sum^\infty_{n = 1} \sum^n_{k = 1} f_k s^k u_{n - k} s^{n - k} \\
&= \sum^\infty_{k = 1} \sum^\infty_{n = k} f_k s^k u_{n - k} s^{n - k} \\
&= \sum^\infty_{k = 1} f_k s^k \sum^\infty_{m = 0} u_m s^m \\
&= F(s)U(s).
\end{align}$$
    
Since $u_0 = 1$, the above expression yields
    
$$\begin{align}
U(s) - 1 = F(s)U(s).
\end{align}$$
    
Now we compute the expression for $U(s)$
    
$$\begin{align}
U(s) &= \sum^\infty_{n = 0} u_n s^n = \sum^\infty_{m = 0} u_{2m} s^{2m} = \sum^\infty_{m = 0} {2m \choose m} (pqs^2)^m = (1 - 4pqs^2)^{-\frac{1}{2}},
\end{align}$$
    
and from this we obtain an expression for $F(s)$
    
$$\begin{align}
F(s) = 1 - (1 - 4pqs^2)^{\frac{1}{2}},
\end{align}$$
    
arriving at the result
    
$$\begin{align}
\sum^\infty_{n = 0} f_n &= \lim_{s \to 1} F(s) = 1 - (1 - 4pq)^{\frac{1}{2}} = 1 - |p - q|.
\end{align}$$
    
</details>
<br>

## Random walks with absorption

<div class='theorem'>

**Theorem (Gambler's Ruin)** Let $S_n$ be a simple random walk on $\{0, 1, ..., N\}$ with absorbing barriers at $0$ and $N$. If $S_0 = a$, where $0 \leq a \leq N$, then the probability $v(a)$ that the walk is absorbed at $N$ is
    
$$\begin{align}
v(a) = \begin{cases}
\frac{\left(\frac{q}{p}\right)^a - 1}{\left(\frac{q}{p}\right)^N - 1} & \text{ if } p \neq q \\
\frac{a}{N} & \text{ if } p = q = \frac{1}{2},
\end{cases}
\end{align}$$
  
where $q = 1 - p$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Gambler's ruin</summary>
    
Let $A$ be the event that the walk is absorbed at $N$, $X$ be the value of the first step, which can be either $-1$ or $1$, and also let $v(a) = \mathbb{P}(A | S_0 = a)$. Then $v(a)$ follows the recursive relation
    
$$\begin{align}
\mathbb{P}(A) &= \mathbb{P}(A | X = 1)\mathbb{P}(X = 1) + \mathbb{P}(A | X = -1)\mathbb{P}(X = -1)\\
v(a) &= p v(a + 1) + q v(a - 1),
\end{align}$$
    
which is a difference equation that can be solved by substituting the trial solution $v(a) = C \lambda^a$ and solving for $\lambda$ to obtain
    
$$\begin{align}
v(a) = \begin{cases}
\alpha + \beta \left(\frac{q}{p}\right)^a & \text{ if } p \neq q \\
\alpha + \beta a & \text{ if } p = q = \frac{1}{2}.
\end{cases}
\end{align}$$
    
where $\alpha$ and $\beta$ are constants determined by the boundary conditions $v(0) = 0$ and $v(N) = 1$, giving
    
$$\begin{align}
v(a) = \begin{cases}
\frac{\left(\frac{q}{p}\right)^a - 1}{\left(\frac{q}{p}\right)^N - 1} & \text{ if } p \neq q \\
\frac{a}{N} & \text{ if } p = q = \frac{1}{2}.
\end{cases}
\end{align}$$
    
</details>
<br>



<div class='theorem'>

**Theorem (Recurrence/transience of bounded random walk)** Let $S_n$ be a simple random walk on $\{0, 1, ..., N\}$ with absorbing barriers at $0$ and $N$. If $S_0 = a$, where $0 \leq a \leq N$, then the expected number $e(a)$ of steps before the random walk is absorbed at either $0$ or $N$ is given by
    
$$\begin{align}
v(a) = \begin{cases}
\frac{1}{p - q} \left(N \frac{\left(\frac{q}{p}\right)^a - 1}{\left(\frac{q}{p}\right)^N - 1} - a\right) & \text{ if } p \neq q \\
a(N - a) & \text{ if } p = q = \frac{1}{2},
\end{cases}
\end{align}$$
  
where $q = 1 - p$.
    
</div>
<br>



<div class='theorem'>

**Theorem (Absorption probability of left-bounded random walk)** Let $S_n$ be a simple random walk on $\{0, 1, ..., N\}$ with an absorbing barrier at $0$. If $S_0 = a \geq 0$, then the probability that the walk is absorbed at $0$ is given by
    
$$\begin{align}
v(a) = \begin{cases}
\left(\frac{q}{p}\right)^a & \text{ if } p > q \\
1 & \text{ if } p \leq q
\end{cases}
\end{align}$$
  
where $q = 1 - p$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Absorption probability of left-bounded random walk</summary>
    
Let $A$ be the event that the walk is absorbed at $0$, $X$ be the value of the first step, which can be either $-1$ or $1$, and also let $\pi(a) = \mathbb{P}(A | S_0 = a)$. Then $\pi(a)$ follows the recursive relation
    
$$\begin{align}
\mathbb{P}(A) &= \mathbb{P}(A | X = 1)\mathbb{P}(X = 1) + \mathbb{P}(A | X = -1)\mathbb{P}(X = -1)\\
\pi(a) &= \pi(a + 1) p + \pi(a - 1) q,
\end{align}$$
    
which is a difference equation that can be solved by substituting the trial solution $\pi(a) = C \lambda^a$ and solving for $\lambda$ to obtain
    
$$\begin{align}
\pi(a) = \begin{cases}
\alpha + \beta \left(\frac{q}{p}\right)^a & \text{ if } p \neq q \\
\alpha + \beta a & \text{ if } p = q = \frac{1}{2}.
\end{cases}
\end{align}$$
    
In this case however, we only have a single $\pi(0) = 1$ boundary condition, from which we obtain
    
$$\begin{align}
\alpha + \beta &= 1 && \text{ if } p \neq q \\
\alpha &= 1 && \text{ if } p = q = \frac{1}{2}.
\end{align}$$
    
Using the additional constraint $0 \leq \pi(a) \leq 1$, we see that
    
$$\begin{align}
&\alpha = 1, && \beta = 0, && \text{ if } p < q \\
& && \beta = 0, && \text{ if } p = q = \frac{1}{2},
\end{align}$$
    
and $\pi(a) = 1$ if $p \leq q$. For the case $p > q$, the above constraint does not allow us to determine $\alpha$ and $\beta$. To proceed, consider an unconstrained simple random walk starting from $0$, let $C$ be the event that it revisits its starting point, and let $Y$ be its first transition. Also, use the notation $\pi_{p, q}(a)$ for the probability that a left-constrained random walk with right and left transition probabilities $p$  and $q$, is absorbed at $0$. Then $\mathbb{P}(B | Y = -1) = \pi_{q, p}(1)$ and
    
$$\begin{align}
\mathbb{P}(B) &= \mathbb{P}(B | Y = 1)\mathbb{P}(Y = 1) + \mathbb{P}(B | Y = -1)\mathbb{P}(Y = -1)\\
&= p \pi_{p, q}(1) + q \pi_{q, p}(1).
\end{align}$$
    
We have already shown $\pi_{q, p}(1) = 1$ when $q < p$, so that
    
$$\begin{align}
\mathbb{P}(B) = 1 - (p - q) = p \pi_{p, q}(1) + q\\
\implies \pi_{p, q}(1) = \frac{q}{p}.
\end{align}$$
    
This constraint, together with $\alpha + \beta = 1$ gives $\pi(a) = \left(\frac{q}{p}\right)^a$ for the case $p < q$, concluding the proof.
    
</details>
<br>