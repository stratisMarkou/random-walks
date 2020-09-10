# Moment generating functions

Moments are an important tool in the study of random variables. Moment generating functions are a useful tool related to the moments of random variables. Under certain conditions, there is a one-to-one mapping between random variables and moment generating functions. One example use of mgfs is the computation of a sum of independent random variables.  Mgfs do not always exist, an issue that is circumvented by characteristic functions which exist for a much broader class of random variables. Two useful inequalities, the Markov and the Jensen inequalities are presented and proved. 

(prob-intro-moments)=
## Moments

The moments of a random variable contain useful information about it. In fact, under the following technical conditions, the moments uniquely determine the distribution of the random variable.

<div class='theorem'>

**Theorem (Uniqueness theorem for moments)** Suppose that all moments $\mathbb{E}(X^k), k = 1, 2, ...$
of the random variable $X$ exist, and that the series
 
 $$\begin{align}
 \sum^\infty_{k = 0}\frac{t^k}{k!} \mathbb{E}(X^k),
 \end{align}$$
 
 is absolutely convergent for some $t > 0$. Then the moments uniquely
  determine the distribution of $X$.

</div>
<br>

## Covariance and correlation

We are often interested in the extent to which two random variables co-vary, a
 property that is quantified by the their covariance, as defined below.

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

Clearly, if we multiply $X$ and $Y$ by $a$ and $b$ respectively, their
 covariance will change by a factor of $ab$. We may be interested
  in a scale-invariant metric of the covariance between two random variables
  , captured by the correlation coefficient.

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

The correlation coefficient of two random variables has absolute value less
 than or equal to $1$, as stated by the following result which is worth
  bearing in mind.

<div class="theorem">

**Theorem (Correlation between $-1$ and $1$)** If $X$ and $Y$ are random
 variables, then
 
 $$\begin{align}
 -1 \leq \rho(X, Y) \leq 1,
 \end{align}$$
 
 whenever this correlation exists.

</div>
<br>

The above result can be shown quickly from an application of the Cauchy
-Schwartz inequality stated and proved below.

<details class="proof">
<summary>Proof: \(-1 \leq \rho(X, Y) \leq 1\) </summary>

Given random variables $X$ and $Y$, define $U = X - \bar{X}$ and $V = Y- \bar{Y}$. By applying the Cauchy-Schwartz inequality on $U$ and $V$, we obtain

$$\begin{align}
\frac{\mathbb{E}(UV)^2}{\mathbb{E}(U^2)\mathbb{E}(V^2)} \leq 1.
\end{align}$$

Taking a square root and substituting for $U$ and $V$ we arrive at the result 

$$\begin{align}
-1 \leq \rho(X, Y) \leq 1.
\end{align}$$
 

</details>
<br>

<div class="theorem">

**Theorem (Cauchy-Schwartz inequality)** If $U$ and $V$ are random variables, then

$$\begin{align}
\mathbb{E}(UV)^2 \leq \mathbb{E}(U^2)\mathbb{E}(V^2),
\end{align}$$

whenever these expectations exist.

</div>
<br>

<details class="proof">
<summary>Proof: Cauchy-Schwartz inequality</summary>

Let $s \in \mathbb{R}$ be a real number and $W = sU + V$ be a random variable. Then $W^2 \geq 0$ and we have 

\begin{align}\mathbb{E}(X^2) = a s^2 + b s + c \geq 0,\end{align}
    
where $a = \mathbb{E}(U^2)$, $b = 2\mathbb{E}(UV)$ and $\mathbb{E}(V^2)$. Since $\mathbb{E}(W^2) \geq 0$ holds for all values of $s$, then the quadratic above can equal zero at most once - because otherwise it would achieve negative values. Therefore we have 

\begin{align}b^2 - 4ac = 4\mathbb{E}(UV)^2 - 4\mathbb{E(U^2)\mathbb{E}(V^2) \leq 0,\end{align}
    
from which we arrive at the result
    
\begin{align}\mathbb{E}(UV)^2 &\leq \mathbb{E}(U^2)\mathbb{E}(V^2).\end{align}

</details>
<br>

## Moment generating functions

Since the moments of a random variable uniquely determine its distribution.

<div class="definition">

**Definition (Moment generating function)** The moment generating function of
 a random variable $X$, denoted $M_X$ is defined by
 
 $$\begin{align}
 M_X(t) = \mathbb{E}(e^{tX}),
 \end{align}$$
 
 for all $t \in \mathbb{R}$ for which the expectation exists.

</div>
<br>


  
We have the following relation between moments of a random variable and
 derivatives of its mgf.

<div class="theorem">

**Theorem (Moments equal to derivatives of mgf)** If $M_X$ exists in a
 neighbourhood of $0$, then $k = 1, 2, ...$,
 
 $$\begin{align}
 \mathbb{E}(X^k) = M_X^{(k)}(0),
 \end{align}$$
 
 the $k^{th}$ derivative of $M_X$ at $t = 0$.
 
</div>
<br>

Further, we also have the following useful relation for the mgf of a sum of
 random variables.

<div class="theorem">

**Theorem (Independence $\implies$ mgf of sum factorises)** If $X$ and $Y$ are
 independent random variables, then $X + Y$ has moment generating function
 
 $$
 M_{X + Y}(t) = M_X(t) M_Y(t).
 $$

</div>
<br>

Intuitively, since the moments of a random variable uniquely determine its
 distribution, then also a generating function $M_X(t)$ uniquely determines the
  distribution of the corresponding random variable $X$. On an intuitive
   level this can be seen by noting that $M_X(t)$ can be rewritten as

$$\begin{align}
\mathbb{E}(e^{tX}) &= \mathbb{E}\left[ \sum_{n = 1}^N \frac{1}{n!} (tX)^n, \right]\\
                   &=  \sum_{n = 1}^N \frac{t^n}{n!} \mathbb{E}\left[X^n\right],
\end{align}$$

so the moments can be determined from the mgf, and the distribution of $X$
 can then be determined from the moments. The following result formalises this
  intuition.

<div class="theorem">

**Theorem (Uniqueness of mgfs)** If the moment generating function $M_X(t) = \mathbb{E}(e^{tX}) < \infty$ for all $t \in [-\delta, \delta]$ for some $\delta > 0$, there is a unique distribution with mgf $M_X$. Under this
 condition, we have that $\mathbb{E}(X^k) < \infty$ for $k = 1, 2, ...$ and
 
 $$\begin{align}
 M_X(t) = \sum^\infty_{k = 0} \frac{t^k}{k!} \mathbb{E}(X^k) \text{ for } |t
 | < \delta.
 \end{align}$$

</div>
<br>

## Examples of MGFS

Here are examples of moment generating functions of some common continuous random variables.

### Uniform

If $X$ is uniformly distributed in $[a, b]$, then its mgf is
\begin{align}
M_X(t) = \frac{e^{tb} - e^{ta}}{t}.
\end{align}

### Exponential

If $X$ is exponentially distributed with parameter $\lambda$, then its mgf is
\begin{align}
M_X(t) = \frac{\lambda}{\lambda - t}.
\end{align}

### Normal

If $X$ is normally distributed with parameters $\mu$, $\sigma^2 > 0$, then
 its mgf is
 
 $$\begin{align}
 M_X(t) = \exp\left(\mu t + \frac{\sigma^2t}{2}\right).
 \end{align}$$

### Cauchy

If $X$ is Cauchy distributed, then it does not have an mgf because the integral

$$\begin{align}
\int^\infty_{-\infty} \frac{e^{tx}}{1 + x^2} dx,
\end{align}$$

diverges for any $t \neq 0$. Many other variables do not have mgfs for the
 same reason, a difficulty that is circumvented by characteristic functions
  defined below.

### Gamma

If $X$ is gamma distributed with parameters $w > 0$ and $\lambda > 0$, then
 its mgf is
\begin{align}
M_X(t) = \left(\frac{\lambda}{\lambda - t}\right)^w.
\end{align}

(prob-intro-markov-jensen)=
## Markov and Jensen inequalities

The Markov inequality is a useful result that bounds the probability that a
 non-negative random variable is larger than some positive threshold.

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

For any non-negative random variable $X(\omega)$ and positive $t > 0$, we have
\begin{align}X(\omega) \geq t \mathbb{1}_{X \geq t},\end{align}
where $\mathbb{1}_{X \geq t} = 1$ if $X(\omega) \geq t$ and $\mathbb{1}_{X\geq t} = 0$
otherwise. Rearranging and taking expectations, we obtain 
\begin{align}\mathbb{P}(X \geq t) = \frac{\mathbb{E}(X)}{t}.\end{align}

</details>
<br>

One consequence of the Markov inequality is the Chebyshev inequality

$$\begin{align}
\mathbb{P}(|X - \bar{X}| \geq \alpha) \leq \frac{\sigma^2}{\alpha^2}
\end{align}$$

where $\sigma^2$ is the variance of $X$. The Markov inequality is useful in
 proofs involving bounds of probabilities that a variable will fall within a
  certain range.
  
Another useful result is Jensen's inequality, which is handy when working with
 convex or concave functions.

<div class="definition">

**Definition (Convex function)** A function $g : (a, b) \to \mathbb{R}$ is
 convex if
 
 $$\begin{align}
 g\left(tu + (1 - t)v\right) \leq t g(u) + (1 - t) g(v),
 \end{align}$$
 
 for every $t \in [0, 1]$ and $u, v \in (a, b)$.

</div>
<br>

The definition of a concave function is as above, except the inequality sign
 is flipped. Jensen's inequality then takes the following form.

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

It can be proved quickly by applying the supporting tangent
 theorem (see below) and taking an expectation over $X$.

<details class="proof">
<summary>Proof: Jensen's inequality</summary>

From the supporting tangent theorem we have
\begin{align}g(X) \geq g(w) + \alpha (X - w),\end{align}
and by setting the constant $w = \mathbb{E}(X)$ and taking an expectation
 over $X$, the $X - w$ term cancels and we obtain Jensen's inequality
 \begin{align}\mathbb{E}[g(X)] \geq g(\mathbb{E}(X)).\end{align}

</details>
<br>

The supporting tangent theorem says that for any point $w$ in the domain of a
 convex function $g$, we can always find a line passing through $(w, g(w))$
 , which lower-bounds the function.

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

</details>
<br>

(prob-intro-char-funcs)=
## Characteristic functions

Unlike the moment generating function which might not exist for some random variables, the characteristic function of a random variable, defined below, exists for a broader set of variables.

<div class="definition">

**Definition (Characteristic function)** The characteristic function of a
 random variable $X$ is written $\phi_X$ and defined as
 
 $$\begin{align}
 \phi_X(t) = \mathbb{E}(e^{itX}), \text{ for } t \in \mathbb{R}.
 \end{align}$$
 
</div>
<br>

The characteristic function has the following two useful properties.

<div class="theorem">

**Theorem (Two properties of characteristic functions)** Let $X$ and $Y$ be
 independent random variables with characteristic functions $\phi_X$ and $\phi_Y$. Then 
 
1. If $a, b \in \mathbb{R}$ and $Z = aX + b$, then $\phi_Z(t) = e^{itb} \phi_X(at)$.
2. The characteristic function of $X + Y$ is $\phi_{X + Y}(t) = \phi_X(t)\phi_Y(t)$.

</div>
<br>

<details class="proof">
<summary>Proof: Properties of the characteristic function</summary>

To show the first property, consider

  $$\begin{align}
  \phi_Z(t) &= \mathbb{E}\left(e^{itZ}\right)\\
  &= \mathbb{E}\left(e^{it(aX + b)}\right)\\
  &= e^{itb} \mathbb{E}\left(e^{itaX}\right)\\
  &= e^{itb} \phi_X(at).
  \end{align}$$
    
For the second property, consider
    
  $$\begin{align}
  \phi_{X + Y}(t) &= \mathbb{E}\left(e^{it(X + Y)}\right)\\
  &= \mathbb{E}\left(e^{itX} e^{itY}\right)\\
  &= \mathbb{E}\left(e^{itX}\right)\mathbb{E}\left(e^{itY}\right)\\
  &= \phi_X(t) \phi_Y(t),
  \end{align}$$
    
where we have used the fact that $X$ and $Y$ are independent to get from the second to the third line.

</details>
<br>

As with the mgf, the characteristic function of a random variable is unique, in the sense that two radoom variables have the same distributions if and only if they have the same characteristic functions.

<div class="theorem">

**Theorem (Uniqueness of characteristic functions)** Let $X$ and $Y$ have
 characteristic functions $\phi_X$ and $\phi_Y$. Then $X$ and $Y$ have the
  same distributions if and only if $\phi_X(t) = \phi_Y(t)$ for all $\mathbb{R}$.

</div>
<br>

We can obtain the pdf of a random variable by applying the following inverse transformation.

<div class="theorem">

**Theorem (Inversion theorem)** Let $X$ have characteristic function $\phi_X$
 and density function $f$. Then
 
 $$\begin{align}
 f(x) = \frac{1}{2\pi}\int^\infty_{-\infty} e^{-itx} \phi(t) dt,
 \end{align}$$
 
 at every point $x$ where $f$ is differentiable.

</div>
<br>

Note the similarity between the Fourier transform and the transform of the characteristic function.
