# Introduction

If you are reading this, you probably need no convincing that optimisation is an extremely important topic and that many important applications can be viewed as optimisation problems. Unfortunately, most optimisation problems are very difficult to solve, in the sense that it takes a lot of computation to solve them exactly.

Convex optimisation refers to a family of optimisation problems - problems with a convex cost and convex constraints - which can nontheless be solved exactly, efficiently and reliably. Many problems which are of interest in applications are convex problems, or can be transformed into convex problems and therefore be solved quickly. Further, strong theoretical statements can be made about convex problems. Below are two examples of such problems which are widely applicable: least squares and linear programming.


## Least squares

Least squares is an unconstrained optimisation problem of the form:

$$\begin{align}
&\text{minimise}&&~~f_0(x) = ||Ax - b||_2^2,
\end{align}$$

where $x \in \mathbb{R}^n$, $b \in \mathbb{R}^m$ and $A \in \mathbb{R}^{m\times n}$. For least squares, there exists a closed-form solution

$$\begin{align}
x^* = (A^\top A)^{-1} A^\top b,
\end{align}$$

and the problem can be solved in $\mathcal{O}(mn^2)$ time. In general, optimisation problems (including the covnex ones presented in the course) do not have closed form solutions like least squares do. However, the fact that a problem does not have a closed-form solution does not imply the exact solution cannot be computed, or that the problem is expensive to solve. Neither does it mean that the problem is more expensive to solve than other similar problems with closed-form solutions. Linear programming, is such a convex problem which does not have a closed form solution, but can be solved just as fast as least squares.

## Linear programming

A linear programme is an optimisation problem of the form:

$$\begin{align}
&\text{minimise}&&~~c^\top x\\
&\text{subject to}&&~~a_i^\top x \leq b_i, \text{ for } i = 1, 2, ..., m.
\end{align}$$

where $x, c \in \mathbb{R}^n$, $a_i \in \mathbb{R}^n$ for $i = 1, 2, ..., m$. Such linear programming problems can be solved in $\mathcal{O}(mn^2)$ time. 

## Convex optimisation

Least squares and linear programmes both fall in a wider family of optimisation problems, which this couurse is all about. An optimisation problem is convex if it can be written as

$$\begin{align}
& \text{minimise }&&~~f_0(x)\\
& \text{subject to }&&~~f_n(x) \leq b_n, \text{ for } i = 1, 2, ..., n\\
& &&~~a_m^\top x = c_m, \text{ for } m = 1, 2, ..., m\\
\end{align}$$

where $f_i$ are all convex functions. A function $f$ is convex if and only if

$$\begin{align}
f\big(\theta x + (1 - \theta) y\big) \leq \theta f(x) + (1 - \theta) f(y),~~~\text{ for all } x, y \in \mathbb{R}^n, \text{ and any } \theta \in [0, 1].
\end{align}$$