# Moments and moment generating functions

## Moments

<div class='theorem'>

**Theorem (Uniqueness theorem for moments)** Suppose that all moments $
\mathbb{E}(X^k), k = 1, 2, ...$ of the random variable $X$ exist, and that
 the series
 
 $$\begin{align}
 \sum^\infty_{k = 0}\frac{t^k}{k!} \mathbb{E}(X^k),
 \end{align}$$
 
 is absolutely convergent for some $t > 0$. Then the moments uniquely
  determine the distribution of $X$.

</div>
<br>

## Variance and covariance

<div class='definition'>

**Definition (Covariance)** If $X$ and $Y$ are random variables, then their
 covariance is denoted $\text{cov}(X, Y)$ and defined as
 
 $$\begin{align}
 \text{cov}(X, Y) = \mathbb{E}\left(X - \mathbb{E}(X)\right)\mathbb{E}\left(Y
  - \mathbb{E}(Y)\right),
 \end{align}$$
 
 whenever these expectations exist.

</div>
<br>

<div class='definition'>

**Definition (Correlation coefficient)** If $X$ and $Y$ are random variables
, then their correlation coefficient is denoted $\rho(X, Y)$ and defined as
 
 $$\begin{align}
 \rho(X, Y) = \frac{\text{cov}(X, Y)}{\sqrt{\text{var}(X)\text{var}(Y)}},
 \end{align}$$
 
 whenever the covariance and variances exist and $\text{Var}(X)\text{Var}(Y
 ) \neq
  0$.

</div>
<br>

<div class="theorem">

**Theorem (Correlation between $-1$ and $1$)** If $X$ and $Y$ are random
 variables, then
 
 $$\begin{align}
 -1 \leq \rho(X, Y) \leq 1,
 \end{align}$$
 
 whenever this correlation exists.

</div>
<br>

<div class="theorem">

**Theorem (Cauchy-Schwartz inequality)** If $U$ and $V$ are random variables
, then

$$\begin{align}
\mathbb{E}(UV)^2 \leq \mathbb{E}(U^2)\mathbb{E}(V^2),
\end{align}$$

whenever these expectations exist.

</div>
<br>

<details class="proof">
<summary>Proof: Cauchy-Schwartz inequality</summary>

<div>

Let $s \in \mathbb{R}$ be a real number and $W = U + sV$ be a random variable
. Then $W^2 \geq 0$ and we have
\begin{align}\mathbb{E}(X^2) = a s^2 + b s + c \geq 0,\end{align}
where $a = \mathbb{E}(U^2)$, $b = 2\mathbb{E}(UV)$ and $\mathbb{E}(V^2)$
. Since $\mathbb{E}(W^2) \geq 0$ holds for all values of $s$, then the
 quadratic above can equal zero at most once - because otherwise it would
  achieve negative values. Therefore we have
\begin{align}b^2 - 4ac = 4\mathbb{E}(UV)^2 - 4\mathbb{E}(U^2)\mathbb{E}(V^2
) \leq 0,\end{align}
from which we arrive at the result 
\begin{align}\mathbb{E}(UV)^2 &\leq \mathbb{E}(U^2)\mathbb{E}(V^2).\end{align}

</div>

</details>
<br>

## Moment generating functions

<div class="definition">

**Definition (Moment generating function)** The moment generating function of
 a random variable $X$, denoted $M_X$ is defined by
 
 $$\begin{align}
 M_X(t) = \mathbb{E}(e^{tX}),
 \end{align}$$
 
 for all $t \in \mathbb{R}$ for which the expectation exists.

</div>
<br>

<div class="theorem">

**Theorem (Moments equal to derivatives of mgf)** If $M_X$ exists in a
 neighbourhood of $0$, then $k = 1, 2, ...$,
 
 $$\begin{align}
 \mathbb{E}(X^k) = M_X^{(k)}(0),
 \end{align}$$
 
 the $k^{th}$ derivative of $M_X$ at $t = 0$.
 
</div>
<br>

<div class="theorem">

**Theorem (Independence $\implies$ mgf of sum factorises)** If $X$ and $Y$ are
 independent random variables, then $X + Y$ has moment generating function
 
 $$
 M_{X + Y}(t) = M_X(t) M_Y(t).
 $$

</div>
<br>

<div class="theorem">

**Theorem (Uniqueness of mgfs)** If the moment generating function $M_X(t
) = \mathbb{E}(e^{tX}) < \infty$ for all $t \in [-\delta, \delta]$ for some $
\delta > 0$, there is a unique distribution with mgf $M_X$. Under this
 condition, we have that $\mathbb{E}(X^k) < \infty$ for $k = 1, 2, ...$ and
 
 $$\begin{align}
 M_X(t) = \sum^\infty_{k = 0} \frac{t^k}{k!} \mathbb{E}(X^k) \text{ for } |t
 | < \delta.
 \end{align}$$

</div>
<br>


## Markov and Jensen inequalities

<div class="theorem">

**Theorem (Markov inequality)** For any non-negative random variable $X
 : \Omega \to \mathbb{R}$,
 
 $$\begin{align}
 \mathbb{P}(X \geq t) \leq \frac{\mathbb{E}(X)}{t} \text{ for } t > 0.
 \end{align}$$

</div>
<br>

<details class="proof">
<summary>Proof: Markov inequality</summary>
<div>

For any non-negative random variable $X(\omega)$ and positive $t > 0$, we have
\begin{align}X(\omega) \geq t \mathbb{1}_{X \geq t},\end{align}
where $\mathbb{1}_{X \geq t} = 1$ if $X(\omega) \geq t$ and $\mathbb{1}_{X\geq t} = 0$
otherwise. Rearranging and taking expectations, we obtain 
\begin{align}\mathbb{P}(X \geq t) = \frac{\mathbb{E}(X)}{t}.\end{align}

</div>
</details>
<br>

<div class="definition">

**Definition (Convex function)** A function $g : (a, b) \to \mathbb{R}$ is
 convex if
 
 $$\begin{align}
 g\left(tu + (1 - t)v\right) \leq t g(u) + (1 - t) g(v),
 \end{align}$$
 
 for every $t \in [0, 1]$ and $u, v \in (a, b)$.

</div>
<br>

<div class="theorem">

**Theorem (Jensen's inequality)** Let $X$ be a random variable taking values
 in the, possibly infinite, domain $(a, b)$ such that $\mathbb{E}(X)$ exists
  and $g : (a, b) \to \mathbb{R}$ be a convex function such that $\mathbb{E
  }|g(X)| < \infty$. Then
  
  $$\begin{align}
  \mathbb{E}[g(X)] \geq g[\mathbb{E}(X)].
  \end{align}$$

</div>
<br>

Jensen's inequality can be proved quickly by applying the supporting tangent
 theorem (see below) and taking an expectation over $X$.

<details class="proof">
<summary>Proof: Jensen's inequality</summary>

<div>

From the supporting tangent theorem we have
\begin{align}g(X) \geq g(w) + \alpha (X - w),\end{align}
and by setting the constant $w = \mathbb{E}(X)$ and taking an expectation
 over $X$, the $X - w$ term cancels and we obtain Jensen's inequality
 \begin{align}\mathbb{E}[g(X)] \geq g(\mathbb{E}(X)).\end{align}

</div>

</details>
<br>

<div class="theorem">

**Theorem (Supporting tangent theorem)** Let $g : (a, b) \to \mathbb{R}$ be
 convex, and let $w \in (u, v)$. There exists $\alpha \in \mathbb{R}$ such that
 
 $$\begin{align}
 g(x) \geq g(w) + \alpha (x - w), \text{ for } x \in (a, b).
 \end{align}$$
 
</div>
<br>

<details class="proof">
<summary>Proof: Supporting tangent theorem</summary>

<div>

Since $g$ is convex, we have
\begin{align}\frac{g(w) - g(u)}{w - u} \leq \frac{g(v) - g(w)}{v - w},\end{align}
otherwise $g$ could not be convex, because $g(w)$ would be strictly less
 than the linear interpolation between $g(u)$ and $g(v)$ at $w$. The above
  inequality holds for all $u < w < v$, we can maximise the left hand side
   over $u$ and the right hand side over $v$ and obtain $L_w \leq R_w$, where
    \begin{align}L_w = \sup\left\\{\frac{g(w) - g(u)}{w - u} : u < w\right\\}, R_w
     = \inf\left\\{\frac{g(v) - g(w)}{v - w} : v < w\right\\}.\end{align}
    we can then take $\alpha \in [L_w, R_w]$ and see that
    \begin{align}\frac{g(w) - g(u)}{w - u} \leq \alpha \leq \frac{g(v) - g(w)}{v- w}.\end{align}
    By rearranging the two sides of the above equation we obtain
    \begin{align}g(x) \geq g(w) + \alpha (x - w),\end{align}
    for the cases where $x = u < w$ and $x = v > w$ respectively. The
     inequality holds trivially for $x = w$.
 


</div>

</details>
<br>

## Characteristic functions

<div class="definition">

**Definition (Characteristic function)** The characteristic function of a
 random variable $X$ is written $\phi_X$ and defined as
 
 $$\begin{align}
 \phi_X(t) = \mathbb{E}(e^{itX}), \text{ for } t \in \mathbb{R}.
 \end{align}$$
 
</div>
<br>

<div class="theorem">

**Theorem (Two properties of characteristic functions)** Let $X$ and $Y$ be
 independent random variables with characteristic functions $\phi_X$ and $\phi_Y$. Then 
 
1. If $a, b \in \mathbb{R}$ and $Z = aX + b$, then $\phi_Z(t) = e^{itb} \phi_X(at)$.
2. The characteristic function of $X, Y$ is $\phi_{X + Y}(t) = \phi_X(t)\phi_Y(t)$.

</div>
<br>

<div class="theorem">

**Theorem (Uniqueness of characteristic functions)** Let $X$ and $Y$ have
 characteristic functions $\phi_X$ and $\phi_Y$. Then $X$ and $Y$ have the
  same distributions if and only if $\phi_X(t) = \phi_Y(t)$ for all $\mathbb{R}$.

</div>
<br>

<div class="theorem">

**Theorem (Inversion theorem)** Let $X$ have characteristic function $\phi_X$
 and density function $f$. Then
 
 $$\begin{align}
 f(x) = \frac{1}{2\pi}\int^\infty_{-\infty} e^{-itx} \phi(t) dt,
 \end{align}$$
 
 at every point $x$ where $f$ is differentiable.

</div>
<br>