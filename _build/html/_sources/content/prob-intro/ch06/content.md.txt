# Multivariate distributions

Joint distributions and the independence of general random variables are
 defined. Joint continuous distributions are defined, and analogues of the
  results for multivariate discrete random variables are given for the
   continuous case.

## Joint distributions

We are often interested in the values taken by two random variables $X$ and $Y$
, defined on the same probability space $(\Omega, \mathcal{F}, \mathbb{P})$
. The joint distribution function describes the probability of the outcome
 that $X$ and $Y$ assume some values simultaneously.

<div class='definition'>

**Definition (Joint distribution function)** Given random variables $X, Y$
 on $(\Omega, \mathcal{F}, \mathbb{P})$, their joint distribution function is
  the mapping $F_{X, Y} : \mathbb{R}^2 \to [0, 1]$ given by
  
  $$\begin{align}
  F_{X, Y}(x, y) = \mathbb{P}(X \leq x, Y \leq y).
  \end{align}$$

</div>

<br>

This definition can be extended to joint distributions of any number of
 variables, by adding more variables to the set being measured. The joint
  distribution function satisfies:
  
  $$\begin{align}
  \lim_{x, y \to -\infty}F_{X, Y}(x, y) = 0&,\\
  \lim_{x, y \to \infty}F_{X, Y}(x, y) = 1&,\\
  x_1 \leq x_2 \text { and } y_1 \leq y_2 \implies  F_{X, Y}(x_1, y_1) \leq
   F_{X, Y}(x_2, y_2)&.
  \end{align}$$
  
The joint distribution function $F_{X, Y}$ is related to its marginal
 distributions $F_X(x), F_{Y}(y)$ by:
 
 $$\begin{align}
 \lim_{y \to \infty} F_{X, Y}(x, y) = F_X(x),
 \lim_{x \to \infty} F_{X, Y}(x, y) = F_Y(y).
 \end{align}$$
 
We are often interested in how two random variables are related. In the special
 case where they are unrelated, we call them independent.
 
<div class='definition'>

**Definition (Independence of variables)** We say that two random variables
 $X$ and $Y$ are independent if for all $x, y \in \mathbb{R}$, the events $\{X \leq x\}$ and $\{Y \leq y\}$ are independent.

</div>

<br>

Note that previously we had defined independence between events, as well as
 between discrete random variables. This definition extends independence to
  all random variables (discrete, continuous or other).

## Joint density functions

If $X$ and $Y$ are continuous we can go further and define their joint pmf
 from their density function.
 
 
<div class='definition'>

**Definition (Joint probability density function)** The random variables $X
, Y$ on $(\Omega, \mathcal{F}, \mathbb{P})$ is called jointly continuous if
 its joint distribution function can be expressed in the form
 
 $$F_{X, Y}(x, y) = \mathbb{P}(X \leq, Y \leq y) = \int^x_{-\infty} \int^y_
 {-\infty} f(u, v) du dv$$
 
 for $x, y \in \mathbb{R}$ and $f : \mathbb{R}^2 \to [0, \infty)$. If this
  holds, we say that $X, Y$ have joint distribution $f$, denoted $f_{X, Y}$.

</div>

<br>

The joint probability density function is related to the joint mass function by

$$\begin{align}
  f_{X, Y}(x, y) = \begin{cases}
  \frac{d}{dx}\frac{d}{dy} F_{X, Y}(x, y) & \text{ if this exists at } (x, y), \\
  0 & \text{ otherwise.}
  \end{cases}
\end{align}$$

The following theorem says that we can go the other way around, integrating
 the pdf to obtain the probability of an event.
 
<div class='theorem'>

**Theorem (Integral of a pdf)** If $A$ is a regular subset of $\mathbb{R}^2$
 and $X, Y$ are jointly continuous random variables with joint density
  function $f_{X, Y}$, then
 
 $$\begin{align}
 \mathbb{P}\left((X, Y) \in A\right) = \int \int_{(x, y) \in A} f_{X, Y}(x, y
 )dxdy.
 \end{align}$$

</div>

<br>


## Independence and sums

The manipulation of a joint distribution may simplify considerably if the
 variables are independent. As with discrete random variables, two variables
  are independent if and only if the joint distribution of continuous random
   variables factorises.

<div class='theorem'>

**Theorem (Independence $\iff$ pdf factorises)** Two jointly continuous
 random variables $X$ and $Y$ are independent if and only if their joint
  density function may be expressed in the form
  
  $$\begin{align}
  f_{X, Y}(x, y) = g(x)h(y), \text{ for } x, y \in \mathbb{R}.
  \end{align}$$
  
</div>

<br>

Again, much like with discrete random variables, the sum of two independent
 continuous random variables has pmf equal to the convolution of the pmfs of
  the summands.

<div class='theorem'>

**Theorem (Convolution formula)** If the random variables $X$ and $Y$ are
 independent and continuous, with pdfs $f_X$ and $f_Y$, then the density
  function of their sum $Z = X + Y$ is
  
  $$\begin{align}
  f_Z(z) = \int^\infty_{-\infty} f_X(x)f_Y(z - x) dx, \text{ for } z \in
   \mathbb{R}.
  \end{align}$$
  
</div>

<br>

## Changes of variables

Given random variables $X, Y$, we are often interested in the distribution of
 $T(X, Y)$. If the random variables are continuous, and the function $T$ is a
  bijection, then the pmf of $T$ is given by the result below.

<div class='theorem'>

**Theorem (Jacobian formula)** Let $X$ and $Y$ be jointly continuous with
 pdf $f_{X, Y}$ and $B(x, y) = (u(x, y), v(x, y))$ is a bijection from $D
  = \{(x, y) : f_{X, Y}(x, y) > 0\}$ to $S \subseteq \mathbb{R}^2$. Then the
   pair $(U, V) = (u(X, Y), v(X, Y))$ is jointly continuous with joint pdf
  
  $$\begin{align}
  f_{U, V}(u, v) = \begin{cases}
  f_{X, Y}\left(x(u, v), y(u, v)\right) |J(u, v)|, & \text{ if } (u, v) \in S,\\
  0 & \text{ otherwise,}
  \end{cases}
  \end{align}$$
  
  where $J(u, v)$ is the Jacobian of $B$
  
  $$\begin{align}
  J(u, v) = \begin{vmatrix}
  \frac{\partial x}{\partial u}& \frac{\partial x}{\partial v} \\
  \frac{\partial y}{\partial u}& \frac{\partial y}{\partial v}
  \end{vmatrix}.
  \end{align}$$
  
</div>

<br>

This result extends the single-variable analogue for $Y = g(X(\omega))$
, where $g$ is an invertible mapping:

$$f_Y(y) = f_X(g^{-1}(y)) \frac{d}{dy} g^{-1}(y).$$

It can be extended to more random variables by adding further variables to
 the Jacobian.


## Conditional density functions

We are often interested in the distribution of one variable $Y$, conditioned
 on another event $\{X = x\}$, defined analogously to its discrete counterpart.

<div class='definition'>

**Definition (Conditional density function)** The conditional density
 function of $Y$ given $X = x$ is written $f_{Y | X}(\cdot | x)$ and defined by
 
 $$\begin{align}
 f_{Y | X}(y | x) = \frac{f_{X, Y} (x, y)}{f_X(x)}
 \end{align}$$
 
 for $y \in \mathbb{R}$ and $f_X(x) > 0$.

</div>

<br>


## Expectations of continuous random variables

The law of the subconscious statistician for discrete random variables has
 the following counterpart for continuous random variables.

<div class='theorem'>

**Theorem (Law of the subconscious statistician)** For any jointly continuous
 random variables $X, Y$ with pmf $f_{X, Y}$ and well-behaved $g$, we have
 
 $$\begin{align}
 \mathbb{E}\left(g(X, Y)\right) = \int^\infty_{-\infty}\int^{\infty}_{-\infty
 } g(x, y) f_{X, Y}(x, y) dx dy,
 \end{align}$$
 
 whenever this integral converges absolutely.

</div>

<br>

The above result is useful because we need not worry about evaluating the
 distribution of $Z = g(X, Y)$, and can instead evaluate the integral directly.
 
We also have the following result relating the independence of
 random variables to the factorisation of expectations of products of
  functions of the variables. This is again analogous to the similar result
   for discrete distributions.


<div class='theorem'>

**Theorem (Independence $\iff$ expectations of products of functions factorise
)** Jointly continuous random variables $X$ and $Y$ are independent if and
 only if
 
 $$\begin{align}
 \mathbb{E}(g(X)h(Y)) = \mathbb{E}(g(X))\mathbb{E}(h(Y))
 \end{align}$$
 
 for all functions $g, h : \mathbb{R} \to \mathbb{R}$ for which these
  expectations exist.
 
</div>

<br>

The conditional expectation of continuous random variables is defined
 analogously to that for discrete distributions, as shown below.

<div class='definition'>

**Definition (Continuous conditional expectation)** If $X, Y$ are jointly
 continuous random variables with joint density function $f_{X, Y}$, the
  conditional expectation of $Y$ given $X = x$ is defined as
  
  $$\begin{align}
  \mathbb{E}(Y | X = x) = \int^\infty_{-\infty} y f_{Y | X}(y | x) dy = \int
  ^{\infty}_{-\infty} y \frac{f_{X, Y}(x, y)}{f_X(x)} dy,
  \end{align}$$
  
  valid for any $x$ for which $f_X(x) > 0$.
 
</div>

<br>

We also have the following result about conditional expectations, an analogue
 of the equivalent result for discrete functions.

<div class='theorem'>

**Theorem (Law of iterated expectations)** If $X, Y$ are jointly continuous
 random variables, then
 
 $$\begin{align}
 \mathbb{E}(Y) = \int^{\infty}_{-\infty} \mathbb{E}(Y | X = x)f_X(x)dx,
 \end{align}$$
 
 where the integral is over all $x$ for which $f_X(x) > 0$.
 
</div>

<br>
