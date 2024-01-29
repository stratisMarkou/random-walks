# Why covariance functions?

One question about GPs that I couldn't wrap my head around for a while was: why do we always work with covariance and never precision functions?
After all, one central limitation of GPs is the cost of inverting matrices, which we could perhaps cut down on if we worked with precision instead of covariance functions.

The reason we don't work with precision functions is because it's not possible to define a function which maps pairs of inputs to entries in a precision matrix, such that the precision matrices produced by it are consistent with one another.
In particular, given a set of inputs $x_{1:N}$, we can define a covariance function $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, mapping pairs of inputs $(x_i, x_j)$ to the respective entries of a covariance matrix $\Sigma_{y_{1:N} | x_{1:N}}$, and that the covariance matrices produced by this $k$ are consistent with each other.
However, it is not possible in general to define a precision function $r : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$, mapping pairs of inputs $(x_i, x_j)$ to the repsective entries of a covariance matrix $R_{y_{1:N} | x_{1:N}}$, such that the corresponding precision matrices are consistent with one another.

Consider set of input-output pairs $x_{1:N}, y_{1:N}$.
We will show two ways of computing the marginal distribution of a subset of these variables, $y_{1:M}$ where $M < N$ and show that the covariance function produces consistent covariance matrices, while the precision function is not guaranteed to produce consistent precision matrices.

The first way of obtaining the marginal $p(y_{1:M} | x_{1:M})$ is to simply apply $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ or $r : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ to the subset $x_{1 : M}$ of input variables, to obtain the covariance or precision matrix respectively.

The other way to obtain the marginal distribution is to compute the integral

$$\begin{align}
p(y_{1:M} | x_{1:M}) = \int p(y_{1:N} | x_{1:N}) dy_{M+1:N} = \int \mathcal{N}\left(y_{1:N}; \boldsymbol{\mu}_{y_{1:N} | x_{1:N}}, \Sigma_{y_{1:N} | x_{1:N}} \right) dy_{M+1:N}.
\end{align}$$

Regardless of whether we use $k$ or $r$, the distributions obtained through (a) direct computation or (b) marginalisation, better be the same.
From the marginalisation property of multivariate Gaussians we have

$$\begin{align}
p(y_{1:M} | x_{1:M}) = \mathcal{N}\left(y_{1:M}; \mathbf{a}, A \right),
\end{align}$$

where we have partitioned the mean $\boldsymbol{\mu}_{y_{1:N} | x_{1:N}}$ and covariance $\Sigma_{y_{1:N} | x_{1:N}}$ of the joint distribution as

$$\begin{align}
p(y_{1:N} | x_{1:N}) = \mathcal{N}\left(y_{1:N}; \boldsymbol{\mu}_{y_{1:N} | x_{1:N}}, \Sigma_{y_{1:N} | x_{1:N}} \right) = \mathcal{N}\left(\begin{bmatrix} y_{1:M} \\ y_{M+1:N}
\end{bmatrix}; \begin{bmatrix} \mathbf{a} \\ \mathbf{b}
\end{bmatrix},
\begin{bmatrix}
A\phantom{^\top} & B\\
B^\top & C
\end{bmatrix}\right).
\end{align}$$

A covariance function $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$ taking pairs of inputs $(x_i, x_j)$ as arguments, is consistent in the sense that (a) applying $k$ to all pairs in $x_{1 : N}$ and then marginalising over $x_{M+1:N}$, and (b) applying $k$ to the pairs in $x_{M+1:N}$; will produce the same covariance matrix. This model is self-consistent in this respect.

On the other hand, if the precision function $r$ takes pairs of inputs $(x_i, x_j)$ as its argument, then it cannot be self-consistent. We can see this by considering

$$\begin{align}
R_{y_{1:N} | x_{1:N}} &= \begin{pmatrix}
A\phantom{^\top} & B\\
B^\top & C
\end{pmatrix}^{-1} = \begin{pmatrix}
M & -MBC^{-1}\\
C^{-1}B^\topM & C^{-1} + C^{-1} B^\top MBC^{-1}
\end{pmatrix}, \text{ where } M = (A - B C^{-1}B^\top)^{-1},
\end{align}$$

and oberving that the entry $M_{ij}$ is a function of all the $x_{1:N}$ inputs and not just $x_i$ and $x_j$. Thus, the precision function cannot be self-consistent if it takes pairs of inputs as its argument. In other words, the precision matrix depends on the whole set of inputs we are conditioning on, and any precision function that takes **pairs of inputs** as its arguments will be inconsistent in general - perhaps with some trivial exceptions. We therefore have the following informal observation.


:::{prf:remark} Precision functions and consistency

It is not possible in general to define a precision function $r : \mathbb{R}^{d} \times \mathbb{R}^{d} \to \mathbb{R},$ mapping pairs of $d$-dimensional vectors to real numbers, such that it produces precision matrices which are consistent under marginalisation.

:::

Since GP models are defined by covariance functions with input-pair arguments, this rules out the possibility of defining a GP using a precision function.
We also observe that whereas the covariance of two random variables is a pair-wise quantity (by definition), the precision of two random variables is a set-wise or global quantity, because it depends on all other inputs.

There is a slightly subtler point here that's worth clarifying however.
Consider a positive definite matrix $H.$
Because $H$ is positive definite, it is invertible and its inverse $H^{-1}$ is also positive definite.
Now, what if we just write down the entries of $H^{-1}$ and define $r(x_i, x_j) = H_{ij}$ to be the precision of $x_i$ and $x_j.$ 
Is there something wrong with that?
The answer is no, there is no problem with this, but it's important to note that this precision function gives us the precisions associated with the entire covariance matrix $H^{-1}.$
In other words, it would not give us the precision associated with say a submatrix of $H^{-1},$ say the submatrix $H_{2:N, 2:N}^{-1},$ by the argument we considered above.
However, we could augment the precision function to take a third argument, which is the subset of elements we are interested in querying the GP at, say $\{x_{n_1}, \dots, x_{n_l}\},$ and instead define $r(x_i, x_j, \mathcal{S})$ to be equal to the inverse of $H^{-1}_{[n_1, \dots, n_l]},$ where this subscript notation means the submatrix containing the $n_i$-th rows and columns of $H^{-1}.$
In other words, we can define a precision function for the entire input space, and whenever we want to evaluate it for a subset of the space, we would have to go through the covariance, select the appropriate submatrix, and invert it.
This is consistent with our previous discussion, because this augmented defintion does not depend on just pairs of inputs, but also on the subset of inputs that we are querying the GP at.
Note also, that for this approach to work, we would need to evaluate this master-precision matrix on the entire input space $\mathcal{X},$ such that we are then able to select the appropriate submatrix for any subset of inputs.
This is clearly very expensive for large input spaces, and clearly very challenging if the space $\mathcal{X}$ is infinite.
Nevertheless, there are cases where this approach is useful, such as when defining GPs on graphs, where the $\mathcal{X}$ is the set of nodes in the graph, and the edges of the graph define the structure of the precision matrix.
