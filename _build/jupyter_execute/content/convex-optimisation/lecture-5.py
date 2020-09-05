# Optimality and problem definitions

## Optimisation problem

**Standard form:** of an optimisation problem is

\begin{align}
\text{minimise }~&f_0(x)\\
\text{subject to }~&f_m(x) \leq 0, \text{ for } m = 1, 2, ..., M\\
&h_n(x) = 0, \text{ for } n = 1, 2, ..., N
\end{align}

- $x \in \mathbb{R}^n$ is the optimisation variable
- $f_0 : \mathbb{R}^n \to \mathbb{R}$ is the optimisation objective
- $f_m : \mathbb{R}^n \to \mathbb{R}$ are the inequality constraints
- $f_n : \mathbb{R}^n \to \mathbb{R}$ are the equality constraints

**Optimal value:** of a problem defined as

$$p^* = \text{inf}\{f(x_0~|~f_m(x) \leq 0, m = 1,..., M, h_n(x) = 0, n = 1, ..., N\}$$

where the infimum of an empty set is $\infty$ by convention (cost is infinite if no $x$ satisfies the constraints).

## Optimality and locally optimal points

**Feasible point:** a point $x$ is feasible if $x \in \textbf{dom}~f_0$ and it satisfies the constraints.

**Optimal point:** a point is optimal if it is feasible and $f_0(x) = p^*$, where $p^*$ is the optimal value of the problem. If no $x$ satisfies $f_0(x) = p^*$, then we say the problem does not achieve its optimal value - for example, unconstrained minimsation of $f_0(x) = -\log x, x \in \mathbb{R}_{++}$, does not achieve its optimal value.

**Locally optimal point:** a point is locally optimal if there exists an $R > 0$ such that $x$ is optimal for the problem

\begin{align}
&\text{minimise } && f_0(z) \\
&\text{subject to } && f_n(z) \leq 0, n = 1, ..., N\\
& &&h_m(z) = 0, m = 1, ..., M\\
& &&||z - x||_2 \leq R.
\end{align}

In other words, within a small enough finite neighbourhood of $x$, $x$ is the best feasible point.

## Implicit constraints and feasibility problems

**Implicit constraint:** In addition to its explicit constraints (equalities and inequalities), every optimisation problem has the implicit constraint that

\begin{align}
x \in \mathcal{D} = \bigcap_{n = 1}^N \textbf{dom}~f_n \cap \bigcap_{m = 1}^M \textbf{dom}~h_m,
\end{align}

where $\mathcal{D}$ is called the **domain of the problem**. A problem is **unconstrained** if it has no explicit constraints $N = M = 0$.

**Feasibility problem:** A feasibility problem amounts to finding a feasible point and can be written as

\begin{align}
&\text{minimise }~&&0\\
&\text{subject to }~&&f_m(x) \leq 0, \text{ for } m = 1, 2, ..., M\\
& &&h_n(x) = 0, \text{ for } n = 1, 2, ..., N.
\end{align}

Under this definition, any feasible point is optimal - which is enough when we search for a feasible point.

## Convex optimisation problem

**Standard form of convex optimisation problem:** The standard form of a convex optimisation problem is

\begin{align}
\text{minimise }~&f_0(x)\\
\text{subject to }~&f_m(x) \leq 0, \text{ for } m = 1, 2, ..., M\\
&a_n^\top x = b_n, \text{ for } n = 1, 2, ..., N
\end{align}

where $f_0, f_1, ..., f_N$ are convex and the equality constraints are affine. It is important to note that the constraints of a convex optimisation problem can be transformed so that the feasible set is unchanged, but the $f_1, ..., f_N$ are no longer convex, or that the equalities are not affine. **In this case, the problem is no longer convex, even if it is equivalent to its original form.**

**Quasiconvex problem:** A problem is **quasiconvex** if it takes the same form as above, except $f_0$ is quasiconvex.

## Local optima, global optima and optimality criteria

Any local optimum of a convex problem is also the global optimum. If the objective is also differentiable, there are useful criteria that every optimum must satisfy.

**Optimality criterion for differentiable $f_0$:** A point $x$ is optimal if and only if it is feasible and

$$\nabla f_0(x)^\top (y - x) \geq 0, \text{ for all feasible } y.$$

If $\nabla f_0(x)$ is nonzero, it defines a supporting hyperplane to the feasible set at $x$. This criterion takes more specific points depending on the constraints - since these determine the feasible set. Some examples are

**Unconstrained problem:** If a problem is unconstrained, then $x$ is optimal if and only if

$$x \in \textbf{dom}~f_0,~~\nabla f_0(x) = 0.$$

**Equality constrained problem:** If the problem has an affine constraint only

\begin{align}
\text{minimise }~&f_0(x)\\
&A x = b,
\end{align}

then $x$ is optimal if and only if there exists $\nu$ such that

$$x \in \textbf{dom } f_0,~~Ax = b,~~ \nabla f_0(x) + A^\top \nu = 0.$$

**Minimisation over nonnegative orthant:** If the problem is constrained to the nonnegative orthant

$$\textbf{minimise } f_0(x), \text{ subject to } x \succcurlyeq 0,$$

then $x$ is optimal if and only if

$$x \in \textbf{dom}~f_0,~x \succcurlyeq 0, \text{ and } \begin{cases}
    \nabla f_0(x)_i \geq 0 & \text{if } x_i = 0\\
    \nabla f_0(x)_i = 0              & \text{if } x_i > 0
\end{cases}$$


## Equivalent convex problems

**Equivalent problems (informal):** Two problems are equivalent if the solution of one is readily obtained from the solution of the other with small computational overhead, and vice versa. Example ways which yield equivalent convex problems are:

- **Eliminating equality constraints:** The standard convex problem \begin{align}
\text{minimise }~&f_0(x)\\
\text{subject to }~&f_m(x) \leq 0, &&\text{ for } m = 1, 2, ..., M\\
&a_n^\top x = b_n, &&\text{ for } n = 1, 2, ..., N
\end{align} for example, can be recast into \begin{align}
\text{minimise }~&f_0(Fz + x_0)\\
\text{subject to }~&f_m(Fz + x_0) \leq 0, \text{ for } m = 1, 2, ..., M
\end{align} where $F$ and $x_0$ are such that $Ax = b \iff x = Fz + x_0$. For example, $F$ could be chosen to be a basis for the null space of $A$ and $x_0$ a solution to $Ax = b$.

<br>

- **Introducing equality constraints:** We can go the opposite way and introduce equality constraints instead of eliminating them. For example, we can rewrite\begin{align}
\text{minimise }~&f_0(A_0 x + b_0)\\
\text{subject to }~&f_m(A_m x + b_m) \leq 0, \text{ for } m = 1, 2, ..., M
\end{align} into the equivalent problem \begin{align}
\text{minimise }~&f_0(y_0)\\
\text{subject to }~&f_m(y_m) \leq 0, &&\text{ for } m = 1, 2, ..., M\\
&y_m = A_m x + b_m, &&\text{ for } m = 0, 1, 2, ..., M
\end{align}

<br>

- **Introducing slack variables for linear inequalities:** We can also modify problems to convert inequalities into equalities by introducing slack variables and some additional inequalities. For example, we can rewrite\begin{align}
\text{minimise }~&f_0(x)\\
\text{subject to }~&a_m^\top x \leq b_m, &&\text{ for } m = 1, 2, ..., M
\end{align} into the equivalent problem \begin{align}
\text{minimise }~&f_0(x)\\
\text{subject to }~&a_m^\top x + s_m = b_m, &&\text{ for } m = 1, 2, ..., M\\
& s_m \geq 0, &&\text{ for } m = 1, 2, ..., M
\end{align}

<br>

- **Linearise objective by using the epigraph:** The standard form convex problem can also be written as\begin{align}
\text{minimise }~&t\\
\text{subject to }~& f_0(x) - t \leq 0, &&\\
&f_m(x) \leq 0, &&\text{ for } m = 1, 2, ..., M\\
&a_n^\top x = b_n, &&\text{ for } n = 1, 2, ..., N,
\end{align} making the objective linear. Note that this is still a convex problem because $f_0(x) - t$ is jointly convex in $(x, t)$.

<br>

- **Minimising over a subset of variables:** If some variables of our original problem are unconstrained \begin{align}
\text{minimise }~&f_0(x_1, x_2)\\
\text{subject to }~&f_m(x_1) \leq 0, &&\text{ for } m = 1, 2, ..., M
\end{align} we can minimise over them to obtain the reduced problem \begin{align}
\text{minimise }~&\tilde{f_0}(x_1)\\
\text{subject to }~&f_m(x_1) \leq 0, &&\text{ for } m = 1, 2, ..., M
\end{align} where $\tilde{f_0} = \inf_{x_2} f_0(x_1, x_2)$.

## Quasiconvex optimisation

**Quasiconvex function:** A function $f$ is quasiconvex if it has a convex domain and it satisfies

$$f\big(\theta x + (1 - \theta)y\big) \leq \max\{f(x),f(y)\},~\forall x, y \in \textbf{dom }f, \theta \in [0, 1].$$

**Quasiconvex problem:** A quasiconvex problem takes a similar form as a convex problem\begin{align}
\text{minimise }~&f_0(x)\\
\text{subject to }~&f_m(x) \leq 0, &&\text{ for } m = 1, 2, ..., M\\
&a_n^\top x = b_n, &&\text{ for } n = 1, 2, ..., N
\end{align} except $f_0$ is a quasi-convex function.

**Solving quasiconvex problems:** One method for solving quasiconvex problems is centered on two observations. The first is that the sublevel sets of quasiconvex functions are convex. The second is that for any quasiconvex function $f_0(x)$, there exists a family of functions $\phi_t(x)$ which is convex in $x$ for fixed $t$, and whose $0$-sublevel set is the $t$-sublevel set of $f_0(x)$ $$f_0(x) \leq t \iff \phi_t(x) \leq 0.$$ With this observation, we can solve the quasiconvex problem to arbitrary precision by iteratively solving the (convex) feasibility problem \begin{align}
\text{minimise }~&0\\
\text{subject to }~& \phi_t(x) \leq 0, &&\\
&f_m(x) \leq 0, &&\text{ for } m = 1, 2, ..., M\\
&a_n^\top x = b_n, &&\text{ for } n = 1, 2, ..., N
\end{align} for given $t$. This is a valid convex problem because $\phi_t(x)$ is convex in $x$ for fixed $t$. We can then then use bisection search to find the smallest value of $t$ for which the feasibility problem has a solution. This smallest value of $t$ is the optimal value of the original quasiconvex problem.


## Linear Programmes (LP)

**Linear program:** A linear programme is a convex optimisation of the form \begin{align} &\text{minimise}&& c^\top x + d\\
&\text{subject to}&& Gx \leq h \\
& && Ax = b.
\end{align}

**Examples of linear programmes:**

- The diet problem 
- Piecewise linear functions
- Chebyshev center of a polyhedron

