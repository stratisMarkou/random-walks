# Introduction to Convex Optimisation

If you are reading this, you probably need no convincing that optimisation is an extremely important topic and that a great deal of applications can be viewed as optimisation problems. Unfortunately, most optimisation problems are very difficult to solve, in the sense that they are computationally expensive to solve exactly (e.g. global optimisation or Travelling Salesman). An even greater number of problems do not have a nice closed-form solution which we can write down (e.g. Linear Programmes) - in fact there are very few problems which do.

However, the fact that a problem does not have a closed-form solution, does not imply the exact solution cannot be computed, or that the problem is a expensive to solve. Neither does it mean that the problem is more expensive to solve than other similar problems with closed-form solutions.

Convex optimisation refers to a family of optimisation problems - problems with a convex cost and convex constraints - which in general do not have nice closed-form solutions, but can nontheless be solved exactly.

## Least squares

Least squares is an unconstrained optimisation problem of the form:

\begin{align}
&\text{minimise}&&~~f_0(x) = ||Ax - b||_2^2
\end{align}

where $x \in \mathbb{R}^n$, $b \in \mathbb{R}^m$ and $A \in \mathbb{R}^{m\times n}$.

## Linear programming

A linear programme is an optimisation problem of the form:

\begin{align}
&\text{minimise}&&~~c^\top x\\
&\text{subject to}&&~~a_i^\top x \leq b_i, \text{ for } i = 1, 2, ..., n
\end{align}

## Convex optimisation

Least squares and linear programmes both fall in a wider family of optimisation problems, which this couurse is all about. An optimisation problem is convex if it can be written as:

\begin{align}
& \text{minimise }&&~~f_0(x)\\
& \text{subject to }&&~~f_n(x) \leq b_n, \text{ for } i = 1, 2, ..., N\\
& &&~~a_m^\top x = c_m, \text{ for } m = 1, 2, ..., M\\
\end{align}

where $f_i$ are all convex functions. A function $f$ is convex if and only if:

\begin{align}
f\big(\theta x + (1 - \theta) y\big) \leq \theta f(x) + (1 - \theta) f(y), \theta \in [0, 1].
\end{align}

