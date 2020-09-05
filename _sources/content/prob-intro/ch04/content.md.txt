# Probability generating functions

Probability generating functions are a useful tool for studying discrete random variables, taking values in $n = 0, 1, 2 ...$. Each pmf has a unique pgf and vice versa. The moments of a random variable can be obtained straightforwardly from its pgf. Pgfs are useful when dealing with sums and random sums of independent random variables.


## Definition

<div class='definition'>

**Definition (Generating function)** Given a sequence $u_0, u_1
, ...$, its generating function is

$$\begin{align}
\sum^\infty_{n = 0} u_n s^n = u_0 + u_1 s + u_2 s^2 + ...
\end{align}$$

for all values of $s$ for which the converges absolutely.

</div>

<br>

The generating function is a general definition, that is not specific to
 probability theory. When the terms of the sequence $u_0, u_1, ...$ are the
  values of a pmf, then the generating function is called a *probability
   generating function*.
   
<div class='definition'>

**Definition (Probability generating function)** Let $X$ be a random variable
 on $(\Omega, \mathcal{F}, \mathbb{P})$, which takes values on the non
 -negative integers and let $p_n = \mathbb{P}(X = n)$. Then the probability
  generating function (or pgf) of $X$ is defined as

$$\begin{align}
G_X(s) = \sum^\infty_{n = 0} p_n s^n = p_0 + p_1 s + p_2 s^2 + ...
\end{align}$$

for all values of $s$ for which the sum converges absolutely.

</div>

<br>

## Uniqueness of PGFs and examples

One very useful result is that if two random variables have the same pgf
, then they have the same pmf - and vice versa.

<div class='theorem'>

**Theorem (Uniqueness of pgfs)** Let $X$ and $Y$ be discrete random variables
 with probability generating functions $G_X$ and $G_Y$. Then 

$$\begin{align}
G_X(s) = G_Y(s) \text{ for all } s \iff \mathbb{P}(X = k) = \mathbb{P}(Y = k
), \text{ for } k = 0, 1, 2, ...
\end{align}$$

</div>

<br>

One direction of this result follows by the definition of the pgf, whereas
 the other can be shown by taking the Taylor expansion of $G_X$ and $G_Y$, and
  observing that all coefficients are equal, which shows that the pmfs of $X$
   and $Y$ are identical.
   
   
### Bernoulli

If $X$ has the Bernoulli distribution with parameter $p$, then

$$\begin{align}
G_X(s) = q + ps, \text{ where } q = 1 - p.
\end{align}$$


### Binomial distribution

If $X$ has the binomial distribution with parameters $p$ and $n$, then

$$\begin{align}
G_X(s) = (q + ps)^n, \text{ where } q = 1 - p.
\end{align}$$

### Poisson distribution

If $X$ has the binomial distribution with parameter $\lambda$, then

$$\begin{align}
G_X(s) = e^{\lambda(s - 1)}.
\end{align}$$


### Geometric distribution

If $X$ has the geometric distribution with parameter $p$, then

$$\begin{align}
G_X(s) = \frac{ps}{1 - qs}, \text{ where } q = 1 - p.
\end{align}$$


### Negative binomial distribution

If $X$ has the negative binomial distribution with parameters $p$ and $n$, then

$$\begin{align}
G_X(s) = \left(\frac{ps}{1 - qs}\right)^n, \text{ where } q = 1 - p.
\end{align}$$


## Moments

We are often interested in the moments, such as the mean, of a random variable
 as these summarise certain aspects of its pmf.

<div class='definition'>

**Definition (Moment)** The $k \geq 1$ moment of a random variable $X$ is the
 quantity $\mathbb{E}(X^k)$.

</div>

<br>

We can easily obtain all moments of a random variable from its pgf, as stated
 by the following result.

<div class='theorem'>

**Theorem (Moments from pgf derivatives)** Let $X$ be a random variable
 with pgf $G_X$. Then
 
 $$\begin{align}
 G_X^{(k)}(1) = \mathbb{E}\left(X(X - 1)...(X - k + 1)\right),
 \end{align}$$

where the $G_X^{(k)}$ notation denotes the $k^{th}$ derivative of $G_X$.

</div>

<br>

The above result is useful in computing higher order moments of random
 variables, by first finding the pgf and taking derivatives.

 
## Sums of independent variables

<div class='theorem'>

**Theorem (Independence $\implies$ $G$ factorises)** If $X$ and $Y$ are
 independent random variables, each taking values on the non-negative
  integers, then
 
 $$\begin{align}
 G_{X + Y}(s) = G_X(s) G_Y(s).
 \end{align}$$

</div>

<br>

By extension, if $X_1, X_2, ..., X_n$ are independent random variables, then
 their sum $X = X_1 + X_2 + ... + X_n$ has pgf $G_X(s) = G_1(s)G_2(s)...G_n(s
 )$. One very useful consequence of the above result is that we can easily
  find the pmf of a sum of random variables by simply taking the product of
   (known) pgfs and matching them against other (known) pgfs. For example, by
    inspecting the example pgfs above, we see that:
   
   - If $X$ and $Y$ are independent and binomially distributed with parameters
    $p$ and $n$ and $p$ and $m$, then $X + Y$ is also binomially distributed
     with parameters $p$ and $n + m$.
   - If $X$ and $Y$ are Poisson distributed with parameters $\lambda$ and $\mu$,
   then $X + Y$ is also Poisson distributed with parameter $\lambda + \mu$.
   - If $X$ and $Y$ are negative binomially distributed with parameters $p$
    and $n$ and $p$ and $m$ respectively, then $X + Y$ is also negative
     binomially distributed with parameters $p$ and $n + m$.
   - If $X_1, X_2, ..., X_n$ are independent and geometrically distributed
   , then $X_1 + X_2 + ... + X_n$ is negative binomially distributed with
    parameters $p$ and $n$.

In some problems of interest, we may have a sum of $N$ i.i.d. random
 variables, where $N$ is itself a random variable. In this case, the
  following result, called the random sum formula, is very useful.
  
<div class='theorem'>

**Theorem (Random sum formula)** Let $N$ and $X_1, X_2, ...$ be random
 variables taking values on the non-negative integers. If $N$ has pgf $G_N$
  and the $X_n$ are independent and identically distributed, with pgf $G_X$
  , then the pgf of the sum
 
 $$\begin{align}
 S = X_1 + X_2 + ... + X_N
 \end{align}$$
 
 has pgf
 
 $$\begin{align}
 G_S(s) = G_N(G_X(s)).
 \end{align}$$

</div>

<br>

Using $G_S$ we can easily determine the moments of a random sum. The random
 sum formula is especially useful when studying branching processes.
