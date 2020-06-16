# Distribution and density functions

## Distribution functions

Extending the definition of a discrete random variable allows us to deal
 with probability spaces with uncountably many outcomes.

<div class='definition'>

**Definition (Random variable)** A discrete random variable $X$ is a
 function $X : \Omega \to \mathbb{R}$ such that for every $x \in \mathbb{R}$
  we have $\{\omega \in \Omega : X(\omega) = x\} \in \mathcal{F}$.

</div>

<br>

Whereas discrete random variables are described by a pmf, general random
 variables are described by distribution functions.

<div class='definition'>

**Definition (Distribution function)** If $X$ is a random variable on $(\Omega, \mathcal{F}, \mathbb{P})$, then its distribution function of $X$ is
 the function $F_X : \mathbb{R} \to [0, 1]$ defined as
 
 $$\begin{align}
 F_X(x) = \mathbb{P}(X \leq x).
 \end{align}$$

</div>

<br>

The following useful properties are true of distribution functions:

1. $F_X(x) \leq F_X(y)$ if $x \leq y$, since $\{X \leq x\} \subseteq \{Y \leq
 y\}$.
2. $\lim_{x \to -\infty} F_X(x) = 0$ and $\lim_{x \to \infty} F_X(x) = 1$, by
 the continuity of $\mathbb{P}$ and considering $\mathbb{P}(\emptyset) = 0$
  and $\mathbb{P}(\Omega) = 1$.
3. $F_X$ is continuous from the right, by the continuity of $\mathbb{P}$.
4. $\mathbb{P}(a < X \leq b) = \mathbb{P}(X \leq b) - \mathbb{P}(X \leq a)$.


## Continuous random variable definition and examples

Just like discrete random variables are special case of random variables
, continuous random variables are another special case of interest.

<div class='definition'>

**Definition (Continuous random variable)** A random variable $X$ is
 continuous if and only if its distribution function $F_X$ can be written in
  the form
  
  $$\begin{align}
  F_X(x) = \mathbb{P}(X \leq x) = \int^x_{-\infty} f_X(z) dz,
  \end{align}$$
  
  for some non-negative function $f_X$, called the **probability density
   function (pdf)** of $X$.

</div>

<br>

Pdfs are a rough counterpart [^pdfandpmf] of pmfs for continuous random
 variables. Given a continuous random variable $X$ and its distribution
  function $F_X$ we can write its pmf as:
  
  $$\begin{align}
  f_X(x) = \begin{cases}
  \frac{d}{dx} F_X(x) & \text{ if this exists at } x,\\
  0 & \text{ otherwise.}
  \end{cases}
  \end{align}$$
  
Further, the pmf $f_X$ satisfies the following properties.
  
<div class='theorem'>

**Theorem (Probability density function properties)** IF $X$ is a continuous
 random variable with density function $f_X$, then
 
 $$\begin{align}
 \mathbb{P}(X = x) = 0 & \text{ for } x \in \mathbb{R},\\
 \mathbb{P}(a \leq X \leq b) = \int^b_a f_X(z) dz & \text{ for } a, b \in
  \mathbb{R} \text{ with } a \leq b
 \end{align}$$

</div>

<br>

### Uniform

$X$ is uniformly distributed in the interval $[a, b]$ if its density function is

$$\begin{align}
f_X(x) = \begin{cases}
\frac{1}{b - a} & \text{ if } x \in [a, b]\\
0 & \text{otherwise}.
\end{cases}
\end{align}$$

### Exponential

$X$ is exponentially distributed with parameter $\lambda$ if its density
 function is
 
$$\begin{align}
f_X(x) = \begin{cases}
\lambda e^{-\lambda x} & \text{ if } x > 0,\\
0 & \text{ if } x \leq 0.
\end{cases}
\end{align}$$

### Normal

$X$ is normally distributed with parameters $\mu$ and $\sigma^2$, if its
 density function is
 
 $$\begin{align}
 f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(- \frac{1}{2\sigma^2}(x
  - \mu)^2)\right) & \text{ for } x \in \mathbb{R}.
 \end{align}$$
 
### Cauchy

$X$ is Cauchy distributed if its density function is

$$\begin{align}
f_X(x) = \frac{1}{\pi(1 + x^2)} & \text{ for } x \in \mathbb{R}.
\end{align}$$

### Gamma

$X$ is gamma distributed with parameters $w > 0$ and $\lambda > 0$ if its
 density function is

$$\begin{align}
f_X(x) = \begin{cases}
\frac{1}{\Gamma(w)}\lambda^w x^{w-1}e^{-\lambda x} & \text{ if } x > 0,\\
0 & \text{ if } x \leq 0.
\end{cases}
\end{align}$$

where $\Gamma(w)$ is the gamma function defined as

$$\begin{align}
\Gamma(w) = \int_0^\infty x^{w-1} e^{-x} dx.
\end{align}$$

 Note that the exponential distribution is a special case of the gamma
  distribution, when $w = 1$. More generally, if $X_1, X_2, ..., X_w$ are
   exponentially distributed with parameter $\lambda$, their sum $X = X_1
    + X_2 + ... + X_w$ is gamma distributed with parameters $w$ and $\lambda$
    . This can be proved most easily using moment generating functions, but
     can also be shown using continuous convolutions. Alternatively, $f_X$
      can be obtained up to a normalisation constant, by considering that it
       is equal to the product of $f_{X_1}, f_{X_2}, ..., f_{X_w}$ and a
        volume term  which scales as $x^{w-1}$.
        
### Beta

$X$ is beta distributed with parameters $a, b > 0$ if it has density function

$$\begin{align}
\frac{1}{B(s, t)} x^{s - 1} (1 - x)^{t - 1} & \text{ for } 0 \leq x \leq 1,
\end{align}$$

where $B(s, t)$ is the beta function defined as

$$\begin{align}
B(s, t) = \int^1_0 x^{s - 1} (1 - x)^{t - 1} dx = \frac{\Gamma(s)\Gamma(t
)}{\Gamma(s + t)}.
\end{align}$$

The last equality above can be shown by computing the convolution of two
 gamma distributions with parameters $(s, \lambda)$ and $(t, \lambda)$, to
  obtain a third gamma distribution with parameters $(s + t, \lambda)$ and
   then comparing the normalisation constants of the convolution expression
   , and the standard form of the gamma distribution.
   
### Chi-squared

$X$ is chi-squared distributed with $n$ degrees of freedom if it has density
 function
 
$$\begin{align}
f_X(x) = \begin{cases}
\frac{1}{2\Gamma\left(\frac{n}{2}\right)} \left(\frac{x}{2}\right)^{\frac{n}{2
} - 1} e ^{-\frac{x}{2}} & \text{ if } x > 0,\\
0 & \text{ if } x \leq 0.
\end{cases}
\end{align}$$

The chi-squared distribution is a special version of the gamma distribution
, where $w = n / 2$ and $\lambda = 1/2$, which is of interest on its own. For
 example, if $Z$ is normally distributed with parameters $(\mu, \sigma^2)$
 , then $X = (Z - \mu)^2 / \sigma^2$ is chi-squared distributed with $n = 1$
  degrees of freedom.
  
## Functions of random variables

We are often interested in functions of random variables, and the
 distributions of values these take. Strictly speaking, if $X$ is a random
  variable on $(\Omega, \mathcal{F}, \mathbb{P})$ and $g : \mathbb{R} \to
   \mathbb{R}$ is any function, then $Y(\omega) = g[X(\omega)]$ is not a
    variable in general, because $\{\omega \in \Omega : Y(\omega) = y\}$ may
     not in general be in $\mathcal{F}$. Grimmett and Welsh acknowledge but
      defer this detail.
 
[^pdfandpmf]: More accurately, the analogy is precise between $f_X(x)\delta x$
 and $p_X(x)$, where $f_X$ and $p_X$ are a pdf and a pmf respectively.
