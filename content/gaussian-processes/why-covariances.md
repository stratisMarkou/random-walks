# Why covariance functions?

One question about GPs that I couldn't wrap my head around was why do we work with covariance instead of precision functions. After all, one central limitation of GPs is the cost of inverting matrices, which we could perhaps cut down on if we worked with precision instead of covariance functions.

The reason we don't work with precision functions is because it's not possible to define a function which maps pairs of inputs to entries in a precision matrix, such that the precision matrices produced by it are consistent with one another. In particular, given a set of inputs $\mathbf{x}_{1:N} = \{\mathbf{x}_n \in \mathbb{R}^d\}_{n = 1}^N$, we can define a covariance function $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, mapping **pairs of inputs** $(\mathbf{x}_i, \mathbf{x}_j)$ to the respective entries of a covariance matrix $\boldsymbol{\Sigma}_{y_{1:N} | \mathbf{x}_{1:N}}$, and that the covariance matrices produced by this $k$ are consistent with each other. However, it is not possible in general to define a precision function $r : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, mapping **pairs of inputs** $(\mathbf{x}_i, \mathbf{x}_j)$ to the repsective entries of a covariance matrix $\boldsymbol{\Lambda}_{y_{1:N} | \mathbf{x}_{1:N}}$, such that the corresponding precision matrices are consistent with one another.

Consider set of input-output variables $\mathbf{x}_{1:N}, y_{1:N}$. We will show two ways of computing the marginal distribution of a subset of these variables, $y_{1:M}$ where $M < N$ and show that the covariance function produces consistent covariance matrices, while the precision function is not guaranteed to produce consistent precision matrices. One way to obtain the marginal distribution is to compute the integral

$$\begin{align}
p(y_{1:M} | \mathbf{x}_{1:M}) = \int p(y_{1:N} | \mathbf{x}_{1:N}) dy_{M+1:N} = \int \mathcal{N}\left(\mathbf{y}_{1:N}; \boldsymbol{\mu}_{y_{1:N} | \mathbf{x}_{1:N}}, \boldsymbol{\Sigma}_{y_{1:N} | \mathbf{x}_{1:N}} \right) dy_{M+1:N}.
\end{align}$$

Another way of obtaining the marginal $p(y_{1:M} | \mathbf{x}_{1:M})$ is to simply apply $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ or $r : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ to the subset $\mathbf{x}_{1 : M}$ of input variables, to obtain the covariance or precision matrix respectively. Regardless of whether we use $k$ or $r$, the distributions obtained through (a) marginalisation or (b) direct computation, better be the same. From the marginalisation property of multivariate Gaussians we have

$$\begin{align}
p(y_{1:M} | \mathbf{x}_{1:M}) = \mathcal{N}\left(\mathbf{y}_{1:M}; \mathbf{a}, \mathbf{A} \right),
\end{align}$$

where we have partitioned the mean $\boldsymbol{\mu}_{y_{1:N} | \mathbf{x}_{1:N}}$ and covariance $\boldsymbol{\Sigma}_{y_{1:N} | \mathbf{x}_{1:N}}$ of the joint distribution as

$$\begin{align}
p(y_{1:N} | \mathbf{x}_{1:N}) = \mathcal{N}\left(\mathbf{y}_{1:N}; \boldsymbol{\mu}_{y_{1:N} | \mathbf{x}_{1:N}}, \boldsymbol{\Sigma}_{y_{1:N} | \mathbf{x}_{1:N}} \right)= \mathcal{N}\left(\begin{bmatrix} \mathbf{y}_{1:M} \\ \mathbf{y}_{M+1:N}
\end{bmatrix}; \begin{bmatrix} \mathbf{a} \\ \mathbf{b}
\end{bmatrix},
\begin{bmatrix}
\mathbf{A}\phantom{^\top} & \mathbf{B}\\
\mathbf{B}^\top & \mathbf{C}
\end{bmatrix}\right).
\end{align}$$

A covariance function $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ taking **pairs of inputs** $(\mathbf{x}_i, \mathbf{x}_j)$ as arguments, is consistent in the sense that (a) applying $k$ to all pairs in $\mathbf{x}_{1 : N}$ and then marginalising over $\mathbf{x}_{M+1:N}$, and (b) applying $k$ to the pairs in $\mathbf{x}_{M+1:N}$; will produce the same covariance matrix. This model is self-consistent in this respect.

On the other hand, if the precision function $r$ takes pairs of inputs $(\mathbf{x}_i, \mathbf{x}_j)$ as its argument, then it cannot be self-consistent. We can see this by considering

$$\begin{align}
\boldsymbol{\Lambda}_{y_{1:N} | \mathbf{x}_{1:N}} &= \begin{pmatrix}
\mathbf{A}\phantom{^\top} & \mathbf{B}\\
\mathbf{B}^\top & \mathbf{C}
\end{pmatrix}^{-1} = \begin{pmatrix}
\mathbf{M} & -\mathbf{M}\mathbf{B}\mathbf{C}^{-1}\\
\mathbf{C}^{-1}\mathbf{B}^\top\mathbf{M} & \mathbf{C}^{-1} + \mathbf{C}^{-1} \mathbf{B}^\top \mathbf{M}\mathbf{B}\mathbf{C}^{-1}
\end{pmatrix}, \text{ where } \mathbf{M} = (\mathbf{A} - \mathbf{B} \mathbf{C}^{-1}\mathbf{B}^\top)^{-1},
\end{align}$$

and oberving that the entry $M_{ij}$ is a function of all the $\{\mathbf{x}_n\}_{1:N}$ inputs and not just $\mathbf{x}_i$ and $\mathbf{x}_j$. Thus, the precision function cannot be self-consistent if it takes pairs of inputs as its argument. In other words, the precision matrix depends on the whole set of inputs we are conditioning on, and any precision function that takes **pairs of inputs** as its arguments will be inconsistent in general - perhaps with some trivial exceptions. We therefore have the following informal observation.


<div class='observation'>

**Observation (Precision functions and consistency)** It is not possible in general to define a function $r : \mathbb{R}^{d} \times \mathbb{R}^{d} \to \mathbb{R}$, mapping pairs of $d$-dimensional vectors to real numbers, such that it produces precision matrices which are consistent under marginalisation.

</div>

<br>

Since GP models are defined by covariance functions with input-pair arguments, this rules out the possibility of defining a GP using a precision function. We also observe that whereas the covariance of two random variables is a pair-wise quantity (by definition), the precision of two random variables is a set-wise or global quantity.
