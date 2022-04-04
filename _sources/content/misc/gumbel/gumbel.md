# Gumbel distribution

The Gumbel distribution has enjoyed a fair amount of attention by the machine learning community. It has a number of useful properties, including the [Gumbel trick](https://francisbach.com/the-gumbel-trick/), and has proved very useful in applications such as [A* sampling](https://arxiv.org/abs/1411.0030) and the [Concrete distribution](https://arxiv.org/pdf/1611.00712.pdf). Here we discuss some of the properties of the Gumbel, which are useful for these applications and beyond.

## Gumbels and exponentials

We say that a random variable $\Gamma$ is Gumbel distributed, with parameter $\kappa$, if its CDF is

$$\begin{align}
p(\Gamma \leq \gamma) = e^{-e^{- (\gamma - \kappa)}}.
\end{align}$$

The when $\kappa = 0$, we call the distribution a standard Gumbel. The Gumbel distribution is closely related to the {ref}`exponential distribution<prob-intro-exponential>`. We say that a random variable $\Xi$ is exponentially distributed, with parameter $\lambda$, if its CDF is

$$\begin{align}
p(\Xi \leq \xi) = 1 - e^{-\lambda \xi}.
\end{align}$$

When $\lambda = 1$, we call the distribution a standard exponential. Now, to draw a standard Gumbel $\Gamma$ or a standard exponential $\Xi$ random variable, we can first sample a uniformly distributed variable $U \sim \mathcal{U}[0, 1]$ and apply the corresponding inverse CDFs to $U$

$$\begin{align}
\Gamma &= - \log \left(- \log U\right), \\
\Xi &= - \log U.
\end{align}$$

A standard Gumbel random variable is therefore distributed identically to the negative logarithm of a standard exponential random variable

$$\begin{align}
\Gamma &= - \log \Xi.
\end{align}$$

More generally, a Gumbel with parameter $\kappa$ is identically distributed to an exponential $\Xi$ with parameter $\lambda = \log \kappa$ since

$$\begin{equation}
p(\Gamma \leq \gamma) = e^{-e^{- (\gamma - \kappa)}} = e^{-\lambda e^{- \gamma}} \implies p(\Xi \geq e^{-\gamma}) = e^{-\lambda v} \implies p(\Xi \leq e^{-\gamma} = v) = 1 - e^{-\lambda v}.
\end{equation}$$

## Minimum of exponentials

The exponential distribution has numerous interesting properties. One of these properties is that the minimum of $K$ exponentially distributed random variables $(\Xi_1, \dots, \Xi_K)$ with parameters $(\lambda_1, \dots, \lambda_K)$ respectively, is also exponentially distributed according to

$$\begin{align}
L = \max\left(\Xi_1, \dots, \Xi_K\right) \sim \text{Exp}\left(\lambda_1 + \dots + \lambda_K\right),
\end{align}$$

whilst the index of the minimiser is categorically distributed according to

$$\begin{align}
I = \text{argmin} \left(\Xi_1, \dots, \Xi_K\right) \sim \text{Cat}\left(\pi_1, \cdots, \pi_K\right), \text{ where } \pi_i = \frac{\lambda_i}{\lambda_1 + \dots + \lambda_K}.
\end{align}$$

Further, and somewhat remarkably, the random variables $L$ and $I$ are independent. We can derive this result directly, following Bach. Let us consider the joint distribution

$$\begin{align}
p(I = i, L \geq l) &= p\left(\Xi_i \geq l \text{ and } \Xi_j \geq \Xi_i \text{ for all } j \neq i\right) \\
                   &= \int_l^\infty p(\Xi_i = \xi_i) \prod_{j \neq i} p\left(\Xi_j \geq \xi_i \right) \text{d}\xi_i \\
                   &= \int_l^\infty \lambda_i e^{-\lambda_i \xi_i} \prod_{j \neq i} e^{-\lambda_j \xi_i} \text{d}\xi_i \\
                   &= \underbrace{\frac{\lambda_i}{\lambda_1 + \dots + \lambda_K}}_{p(I = i)}~~\underbrace{\exp\left(-\left[\sum_{k=1}^K \lambda_k\right] l\right)}_{p(L \geq l)}.
\end{align}$$

The distributions of $I$ and $M$ therefore factorise and the variables are independent, whilst their marginal distributions are

$$\begin{align}
p(I = i) &= \frac{\lambda_i}{\lambda_1 + \dots + \lambda_K} \\
p(L \geq l) &= \exp\left[-\left(\sum_{k=1}^K \lambda_k\right) l\right].
\end{align}$$

## The Gumbel trick

The Gumbel trick is the same property, packaged in a different way. In particular

$$\begin{align}
I &= \text{argmin} \left(\Xi_1, \dots, \Xi_K\right) \\
  &= \text{argmin} \left(\log \Xi_1, \dots, \log \Xi_K\right) \\
  &= \text{argmax} \left(-\log \Xi_1, \dots, -\log \Xi_K\right) \\
  &= \text{argmax} \left(\Gamma_1, \dots, \Gamma_K\right)
\end{align}$$

where each $\Gamma_i$ is Gumbel distributed with parameter $\kappa_i = \log \lambda_i$. Using the fact that

$$\begin{align}
\Gamma_i = \kappa_i + Z_i,
\end{align}$$

where $Z_i$ is a standard Gumbel random variable, we arrive at

$$\begin{align}
I = \text{argmax} \left(\kappa_1 + Z_1, \dots, \kappa_K + Z_K\right).
\end{align}$$

Therefore, if we suppose $\pi_{1:K}$ are the probabilities of a categorical

$$\begin{align}
\pi_i \geq 0, \sum_{k=1}^K \pi_k = 1,
\end{align}$$

and we take their logarithms $\kappa_{1:K} = \log \pi_{1:K}$ and define the random variable

$$\begin{align}
I = \text{argmax} \left(\kappa_1 + Z_1, \dots, \kappa_K + Z_K\right).
\end{align}$$

where $Z_i$ is a standard Gumbel, then the $I$ is distribued according to the categorical

$$\begin{align}
p\left(I = i\right) = \pi_i.
\end{align}$$