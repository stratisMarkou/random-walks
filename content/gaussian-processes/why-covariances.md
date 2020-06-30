# Why covariance functions?

One question about GPs that I couldn't wrap my head around until recently was why do we work with covariance instead of precision functions. After all, one central limitation of GPs is the cost of inverting matrices, which we could perhaps cut down on if we worked with precision functions directly. The reason we work with covariance instead of precision functions, is because it's not possible to define a function that maps pairs of inputs to entries in a precision matrix, such that the precision matrices produced by it are consistent with one another.

Consider two machine learners, Alice and Bob. Alice prefers to define her GP priors using a covariance function $k$. Bob on the other hand prefers to define his GPs using a precision function $r.$ Alice and Bob wish to choose $k$ and $r$ so that if they pass some data $\mathbf{x}_{1:N} = \{\mathbf{x}_n\}^N_{n=1}, \mathbf{x}_n \in \mathbb{R}^d$ to them, they get $\boldsymbol{\Sigma}_{y_{1:N} | \mathbf{x}_{1:N}}$ and $\boldsymbol{\Lambda}_{y_{1:N} | \mathbf{x}_{1:N}}$, the covariance and precision matrices of the GP prior over the corresponding outputs $y_{1:N}$, respectively.

We will see that Alice can define a covariance function $k : \mathbb{R}^{2d} \to \mathbb{R}$, mapping **pairs of inputs** $(\mathbf{x}_i, \mathbf{x}_j)$ to the respective entries in the covariance matrix, and that the covariance matrices produced by this $k$ are consistent with each other. However, it will not in general be possible for Bob to define a precision function $r : \mathbb{R}^{2d} \to \mathbb{R}$, mapping **pairs of inputs** $(\mathbf{x}_i, \mathbf{x}_j)$ to precisions, such that the corresponding precision matrices are consistent with one another.

In particular, suppose that Alice and Bob choose a subset of input-output pairs $\mathbf{x}_{1:M}, y_{1:M}, M < N$ and want to determine their marginal distribution

$$\begin{align}
p(y_{1:M} | \mathbf{x}_{1:M}) = \int p(y_{1:N} | \mathbf{x}_{1:N}) dy_{M+1:N} = \int \mathcal{N}\left(\mathbf{y}_{1:N}; \boldsymbol{\mu}_{y_{1:N} | \mathbf{x}_{1:N}}, \boldsymbol{\Sigma}_{y_{1:N} | \mathbf{x}_{1:N}} \right) dy_{M+1:N}.
\end{align}$$

From the marginalisation property of multivariate Gaussians, we have

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

Alice can use a covariance function which takes **pairs of inputs** $(\mathbf{x}_i, \mathbf{x}_j)$, because $A_{ij}$ depends only on $\mathbf{x}_i$ and $\mathbf{x}_j$. The matrices obtained by (a) applying $k$ to all input pairs in $\{\mathbf{x}_n\}^N_{n=1}$ and then marginalising over $\mathbf{x}_{M+1:N}$ and by (b) applying $k$ to the pairs in $\{\mathbf{x}_n\}^M_{n=1}$, are equal and therefore the GP model is consistent in this respect.

On the other hand, if Bob wants his model to marginalise consistently, then his precision function $r$ cannot take just pairs of inputs $(\mathbf{x}_i, \mathbf{x}_j)$ as its argument. We can see this by considering

$$\begin{align}
\boldsymbol{\Lambda}_{y_{1:N} | \mathbf{x}_{1:N}} &= \begin{pmatrix}
\mathbf{A}\phantom{^\top} & \mathbf{B}\\
\mathbf{B}^\top & \mathbf{C}
\end{pmatrix}^{-1} = \begin{pmatrix}
\mathbf{M} & -\mathbf{M}\mathbf{B}\mathbf{C}^{-1}\\
\mathbf{C}^{-1}\mathbf{B}^\top\mathbf{M} & \mathbf{C}^{-1} + \mathbf{C}^{-1} \mathbf{B}^\top \mathbf{M}\mathbf{B}\mathbf{C}^{-1}
\end{pmatrix}, \text{ where } \mathbf{M} = (\mathbf{A} - \mathbf{B} \mathbf{C}^{-1}\mathbf{B}^\top)^{-1},
\end{align}$$

and oberving that $\mathbf{A} \neq \mathbf{M}$. Therefore $r\left(\mathbf{x
}_i, \mathbf{x}_j\right) = \mathbf{M}_{ij}$ cannot hold in general because $\mathbf{M}$ is a function of all the $\{\mathbf{x}_n\}^N_{n=1}$ inputs
, whereas we only passed $\mathbf{x}_i, \mathbf{x}_j \in \{\mathbf{x}_n\}^M_{n=1}$ to $r$. In other words, the precision matrix depends on the whole set of inputs we are conditioning on, and any precision function that takes **pairs of inputs** as arguments will be inconsistent - perhaps with some trivial exceptions. We therefore have the following informal observation.


<div class='observation'>

**Observation (Precision functions and consistency)** It is not possible in general to define a function $r : \mathbb{R}^{2d} \to \mathbb{R}$, mapping pairs of $d$-dimensional vectors to real numbers, such that it produces precision matrices which are consistent under marginalisation.

</div>

<br>

Since GP models are defined by covariance functions with input-pair arguments, this rules out the possibility of defining a GP using a precision function. We also observe that whereas the covariance of two random variables is a pair-wise quantity (by definition), the precision of two random variables is a set-wise or global quantity.
