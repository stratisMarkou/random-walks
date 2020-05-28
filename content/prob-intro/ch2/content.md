# Discrete random variables

Discrete random variables are random variables whose images are countable sets. We define discrete random variables and probability mass functions and present some examples. The (conditional) expectation and variance are important summary statistics of random variables.

## Discrete random variables

We are often interested in the value of a function of elementary events. For example we might be interested in the profit of a gambling game as a function of the elementary outcomes of the game.

<div class='definition'>

**Definition (Discrete random variable)** A discrete random variable $X$ is a function $X : \Omega \to \mathbb{R}$ such that:

1. The image $X(\Omega)$ is a countable subset of $\mathbb{R}$.
2. For every $x \in \mathbb{R}$ we have $\{\omega \in \Omega : X(\omega) = x\} \in \mathcal{F}$.

</div>

<br>

By defining discrete random variables as functions of elementary events, we separate the ideas of experimental outcomes and of functions of these outcomes.

Condition (1) specifies that a discrete random variable can only take countably many values. Condition (2) specifies that every set that is mapped to a certain value $x \in \mathbb{R}$ is contained in the event space $\mathcal{F}$ and is therefore assigned a probability by any probability measure defined on $\mathcal{F}$.

## Probability mass functions

Once we have defined the continuous random variable, we can make statemets about the probability that it will take a certain value, using its **probability mass function**.


<div class='definition'>

**Definition (Probability mass function)** Let $X : \Omega \to \mathbb{R}$ be a discrete random variable. The **probability mass function** (or pmf) is the function $p_X : \mathbb{R} \to [0, 1]$ defined by

$$p_X(x) = \mathbb{P}(X = x)$$

where $\mathbb{P}(X = x)$ is shorthand for $\mathbb{P}(\{\omega \in \Omega : X(\omega) = x\})$.

</div>

<br>

Reviewing the definitions leading up to the pmf, we defined: elementary events, event spaces and probability measures, followed by random variables and the probability mass function. This was a rigorous build-up of what a discrete random variable is, however in many cases we need not consider this construction at all, instead declaring that "$X$ is a random variable with pmf $p_X(\cdot)$" and proceed to give an expression for $p_X(\cdot)$ directly.


<div class='theorem'>

**Theorem (pmf $\implies$ probability space and random variable)** Let $S = \{s_i : i \in I\}$ be a countable set of real numbers and let $\{\pi_i : i \in I\}$ be a collectioin of real numbers satisfying

$$\pi_i \geq 0 \text{ for } i \in I, \text{ and } \sum_{i \in I} \pi_i = 1.$$

There exists a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and a discrete random variable $X$ on $(\Omega, \mathcal{F}, \mathbb{P})$ such that the pmf $p_X(\cdot)$ is given by

$$\begin{align}
p_X(s_i) &= \pi_i && \text{ for } i \in I\\
p_X(s) &= 0 && \text{ if } s \not \in S
\end{align}$$

</div>

<br>

The proof for this theorem is that we can take $\Omega = S$, $\mathcal{F}$ to be the powerset of $\Omega$ and $\mathbb{P}$ defined by

$$\begin{align}
\mathbb{P}(A) = \sum_{i : s_i \in A} \pi_i & \text{ for } A \in \mathcal{F}.
\end{align}$$

Lastly defining $X : \Omega \to \mathbb{R}$ to be any one-to-one function, we arrive at the result because we can verify that:

1. $\mathcal{F}$ is a valid event space.
2. $\mathbb{P}$ is a valid probability measure.
3. $X$ is a valid discrete random variable and has the pmf from the theorem statement.

## Fundamental discrete distributions

Here are some examples of fundamental discrete distributions. Appealing to the theorem above, we can forget about probability spaces and consider only the values taken by the pmf of the random variable in question.

### Bernoulli

Also called the coin toss, the Bernoulli distribution is the simplest discrete distribution. A random variable $X$ is Bernoulli-distributed with paramter $p \in [0, 1]$ if $X$ can take the values 0 or 1:

$$ \begin{align}
\mathbb{P}(X = 0) &= 1 - p, \\
\mathbb{P}(X = 1) &= p.
\end{align}$$

### Binomial

A random variable $X$ is binomially distributed if

$$ \mathbb{P}(X = k) = {n \choose k} p^k (1 - p)^{n - k} ~~\text{for}~~k = 0, 1, 2, ..., n.$$

The sum of $n$ independent and identically distributed coin tosses is Bernoulli distributed.

### Poisson

A random variable $X$ is said to be Poisson-distributed with parameter $\lambda > 0$ if

$$\begin{align}
\mathbb{P}(X = k) = \frac{1}{k!} \lambda^k e^{-\lambda} & \text{ for } k = 0, 1, 2 ...
\end{align}$$

The Poisson distribution is an appropriate model for *point data*. For example, if buses arrive at a local stop such that

1. Each bus arrival occurs at a single point in time.
2. Arrivals are independent of each other.
3. The number $N_{t, t + dt}$ of buses arriving within an infinitesimal time interval $[t, t + dt]$ follows

$$\begin{align}
\mathbb{P}(N_{t, t+ dt} = 0) &= 1 - \lambda dt + o(dt)\\
\mathbb{P}(N_{t, t+ dt} = 1) &= \lambda dt + o(dt),
\end{align}$$

then the number of events occuring within any time interval are Poisson-distributed.

### Geometric

A random variable $X$ has the geometric distribution with parameter $p$ if

$$\begin{align}
\mathbb{P}(X = k) = pq^k & \text{ for } k = 0, 1, 2 ...
\end{align}$$

The geometric distribution naturally models random variables such as "the number of i.i.d. trials up to and including the first occurence of A". For example, the number of i.i.d. coin tosses required until heads is obtained the first time, is geometrically distributed.

### Negative binomial

A random variable $X$ has the negative binomial distribution with parameters $n$ and $p \in [0, 1]$ if

$$\begin{align}
\mathbb{P}(X = k) = {k - 1 \choose n - 1} p^n q^{k - n} & \text{ for } k = n, n + 1, n + 2, ...
\end{align}$$

The number of i.i.d. coin tosses up to and including the $n^{th}$ success is distributed according to the negative binomial distribution. To see this, consider that a sequence of trials up to the $n^{th}$ success contains $n$ successes and $k - n$ failures, so the probability of obtaining that particular sequence is $p^nq^{k - n}$. To count the number of all possible sequences with $k - n$ failures and $n$ successes, consider that the last trial must be a success. That leaves us with $k - 1$ choose $n - 1$ ways to rearrange the remaining successes and failures, arriving at the final expression.


## Expectations

Although random variables are not perfectly determined, we can reason about the values they could attain. The expectation of a random variable captures the value that we expect the variable will have on average - as weighted by the probability measure.

<div class='definition'>

**Definition (Expectation)** The **expectation** of a discrete random variable $X$ is denoted by $\mathbb{E}(X)$ and defined by

$$\begin{align}
\mathbb{E}(X) = \sum_{x : x \in X(\Omega)} x \mathbb{P}(X = x).
\end{align}$$

whenever this sum converges absolutely, i.e. $\sum |x\mathbb{P}(X = x)| < \infty.$

</div>

<br>

The need for the last statement in this definition is that the expectation of a discrete random variable may not always exist. For example, if $X$ has pmf

$$\mathbb{P}(X = x) = \frac{A}{x^{3/2}} \text{ for } x = 1, 2, ...$$

where $A$ is a normalising constant, then the sum in the definition of $\mathbb{E}(X)$ does not converge. When taking expectations of *functions* of discrete random variables, the following result that we often take for granted

<div class='theorem'>

**Theorem (Law of the subconscious statistician)** If $X$ is a discrete random variable and $g : \mathbb{R} \to \mathbb{R}$, then

$$\begin{align}
\mathbb{E}\left(g(x)\right) = \sum_{x \in \text{Im}X} x \mathbb{P}(X = x)
\end{align}$$

whenever this sum converges absolutely.

</div>

<br>

The above can be shown by defining $Y = g(X)$ and considering the expectation of $Y$, showing this is equal to $\mathbb{E}\left(g(X)\right)$. The variance is another central quantity that captures information about a random variable, and in particular about its spread.


<div class='definition'>

**Definition (Variance)** The **variance** of a discrete random variable $X$ is denoted by $\text{Var}(X)$ and defined by

$$\begin{align}
\text{Var}(X) &= \mathbb{E}\left([X - \mathbb{E}(X)]^2\right) \\
&= \mathbb{E}(X^2) - \mathbb{E}(X)^2
\end{align}$$

</div>

<br>

## Conditional expectations

We are often interested in the expectation of a random variable **conditioned on some event**. For example, the event we are conditioning on could be some observed data, based on which we would like to update our beliefs about the random variable, and compute its expectation.

<div class='definition'>

**Definition (Conditional expectation)** If $X$ is a random variable and $\mathbb{P}(B) > 0$, then the expectation of $X$ conditioned on $B$ is written $\mathbb{E}[X | B]$ and defined by

$$\begin{align}
\mathbb{E}[X | B] &= \sum_{x \in \text{Im} X} x\mathbb{P}(X = x | B)
&= \mathbb{E}(X^2) - \mathbb{E}(X)^2
\end{align}$$

whenever this sum converges absolutely.

</div>

<br>

As with conditional probabilities, there is a partition theorem associated with conditional expectations, also known as the law of total expectation.

<div class='theorem'>

**Theorem (Partition theorem for conditional expectations)** If $X$ is a discrete random variable and $\{B_1, B_2, ...\}$ is a partition of $\Omega$ with $\mathbb{P}(B_k) > 0$, we have

$$\begin{align}
\mathbb{E}(X) = \sum_k \mathbb{E}(X | B_k)\mathbb{P}(B_k)
\end{align}$$

whenever this sum converges absolutely.

</div>

<br>

