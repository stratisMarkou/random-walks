# Convex functions

## Definition and examples

**Convex function:** A function whose domain is convex, and which also satisfies

$$f\big(\theta x + (1 - \theta) y\big) \leq \theta f(x) + (1 - \theta) f(y),$$

for every $x, y \in \textbf{dom}(f)$ and $\theta \in [0, 1]$.

**Strictly convex function:** As above, except the inequality is strict

$$f\big(\theta x + (1 - \theta) y\big) < \theta f(x) + (1 - \theta) f(y).$$

**Concave and strictly concave funtions:** Same as the definitions above except the inequality sign goes the other way - the domain still needs to be a convex set. The negative of a concave function is convex and vice versa.

**Examples of convex functions in $\mathbb{R}$:**
- affine: $ax + b$, for any $a, b \in \mathbb{R}$.
- exponential: $e^{\alpha x}$ for any $\alpha \in \mathbb{R}$.
- powers: $x^\alpha$ on $\mathbb{R}_{++}$ for $\alpha \geq 1$ or $\alpha \leq 0$.
- powers of absolute value: $|x|^p$ for $p \geq 1$.

**Examples of concave functions in $\mathbb{R}$:**
- affine: $ax + b$, for any $a, b \in \mathbb{R}$.
- logarithm: $\log x$ for $x \in \mathbb{R}_{++}$.
- powers: $x^\alpha$ on $\mathbb{R}_{++}$ for $0 \leq \alpha \leq 1$.

**Examples of convex functions in $\mathbb{R}^n$:**
- affine: $a^\top x + b$, for any $a \in \mathbb{R}^n, b \in \mathbb{R}$.
- $p$-norm: $||x||_p = \left[ \sum_{i = 1}^n |x_i|^p\right]^{1/p}$ for $p \geq 0$.

**Examples of convex functions in $\mathbb{R}^{n \times m}$:**
- affine: $\text{Tr}(A^\top X) = \left[\sum_{i = 1}^n \sum_{j = 1}^m A_{ij} X_{ij}\right] + b$
- spectral norm: $f(X) = ||X||_2 = \sigma_{\text{max}}(X) = \lambda^{1/2}_{\text{max}}(X^\top X)$, where $\lambda_{\text{max}}(\cdot)$ is the maximum eigenvalue of a matrix.

## Restriction to a line

**Restriction to a line:** A function $f$ from $\mathbb{R}^n$ to $\mathbb{R}$ is convex if and only if the restriction $g$ of $f$ on any line, is also convex

$$g(t) = f(x + tv),~~~\textbf{dom}~g = \{t~|~x + tv \in \textbf{dom}~f\},$$

for any $x \in \textbf{dom}~f, v \in \mathbb{R}^n$.

**Example use of restriction:** Using the above result we can prove the convexity of quite complicated functions. Take for example the function $\log \det : \mathbf{S}_{++}^n \to \mathbb{R}$ and restrict it to a line along matrix $V$. For $\textbf{dom}~g = \{t~|~X + tV \in \textbf{dom}~f\}$ to be non-empty, $V$ will have to be symmetric but does not have to be positive-definite. The restricted function $g$ is

\begin{align}
g(t) = \log \det (X + tV) &= \log \det X + \log \det (I + tX^{-1/2}VX^{-1/2})\\
&= \log \det X + \sum_{i = 1}^n  \log (1 + t \lambda_i)
\end{align}

where $\lambda_i$ is the $i^\text{th}$ eigenvalue of $X^{-1/2}VX^{-1/2}$ and $X^{-1/2}$ exists because $X$ is positive-definite. The components $\log (1 + t \lambda_i)$ are all concave regardless of the value of $\lambda_i$, so $g$ is concave along any line in $\mathbf{S}_{++}^n$ and thus $\log \det$ is also concave.

## Extended value extension

**Extended-value extension:** The extended-value extension $\tilde{f}$ of $f$ is

$$ \tilde{f}(x) = f(x) \text{ if } x\in \textbf{dom}~f, \text{ otherwise } \infty.$$

This definition helps to extend the domain of convex functions to a larger set, for example extending $f(x) = x^2, \textbf{dom}~f = \mathbb{R}_{+}$ from the positive reals $\mathbb{R}_{+}$ to the whole real line $\mathbb{R}$ and still have $\tilde{f}$ be covex.

## Condtions for convexity on differentiable functions

**First-order differentiability (informal):** A function $f$ is differentiable if its domain is open and the gradient

$$\nabla f(x) = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, ..., \frac{\partial f}{\partial x_n} \right)$$

exists at each $x \in \textbf{dom}~f$. From this follows a first-order condition for covexity.

**First-order condition:** A differentiable function $f$ with a convex domain is convex if and only if

$$f(x) \geq f(x_0) + \nabla f(x_0)^\top (x - x_0), \text{ for all } x_0, x \in \textbf{dom}~f.$$

**Second-order differentiability (informal):** A function $f$ is twice differentiable if its domain is open and the hessian $\nabla^2 f(x) \in \mathbf{S}^n$ $$\nabla^2 f(x)_{ij} = \frac{\partial^2f(x)}{\partial x_i \partial x_j},~i, j = 1, ..., n,$$ exists at each $x \in \textbf{dom}~f$. From this follows a second-order condition for convexity.

**Second-order condition:** A twice differentiable function $f$ with convex domain is 

\begin{align}
\text{convex if and only if }\nabla^2 f &\succcurlyeq 0 \text{ for all } x \in \textbf{dom} f\\
\text{strictly convex if }\nabla^2 f &\succ 0 \text{ for all } x \in \textbf{dom} f.
\end{align}

Note $f$ can be stricly convex and still have $\nabla^2 f = 0$ for some $x$ - take for example $f(x) = x^4$.

## More examples of convex functions

**Quadratic function:** $f(x) = \frac{1}{2} x^\top P x + q^\top x + r$ for $P \succ 0$.

**Least squares objective:** $f(x) = ||Ax - b||_2^2$ for any $A, b$.

**Quadratic-over-linear:** $f(x, y) = \frac{x^2}{y}$ for $y > 0$.

**log-sum-exp or soft-max:** $f(x) = \log \sum_{n = 1}^N e^{x_k}$.

**Geometric mean:** $f(x) = \left(\prod_{i = 1}^n x_i\right)^{1/n}$ $x > 0$.


## Epigraphs and sublevel sets

**Sublevel set:** The $\boldsymbol{\alpha}$-sublevel set of $f$ is

$$C_\alpha = \{x \in \textbf{dom}~f~|~f(x) \leq \alpha \},$$

the set of $x$ for which $f(x)$ is no larger than $\alpha$. Sublevel sets of convex functions are convex.

**Epigraph:** The epigraph of $f : \mathbb{R}^n \to \mathbb{R}$ is

$$\textbf{epi}~f = \{(x, t) \in \mathbb{R}^{n + 1} | x \in \textbf{dom}~f, f(x \leq t)\},$$

the set of points which are on or above $f$ in $\mathbb{R}^{n + 1}$.

## Jensen's inequality

**Convex function:** The definition of a convex function

$$f\big(\theta x + (1 - \theta)y\big) \leq \theta f(x) + (1 - \theta)f(y),$$

is a special case of Jensen's inequality.

**Jensen's inequality:** If $f$ is convex and $\mathbb{E}$ is the expectation over a random variable $x$

$$f\big(\mathbb{E}[x]\big) \leq \mathbb{E}\big[f(x)\big].$$

## Establishing convexity

1. Directly verify definition, for example by restricting to an arbitrary line and showing the restricted function is convex.
2. Show Hessian is positive semi-definite.
3. Show function can be obtained through a number of operations which preserve convexity.

### Operations that preserve convexity of sets

- **Nonnegative multiple:** $\alpha f$ is convex if $f$ is convex and $\alpha \geq 0$.
- **Sum:** If $f_1$ and $f_2$ are convex, $f_1 + f_2$ is also convex. This extends to infinite sums and integrals.
- **Composition with affine function:** $f(Ax + b)$ is convex if $f$ is convex.
- **Pointwise maximum:** If $f_1, f_2, ..., f_n$ are all convex, then $$f(x) = \max \{f_1(x), f_2(x), ..., f_n(x)\},$$ is convex.
- **Pointwise supremum:** If $f(x, y)$ is convex in $x$ for each $y \in \mathcal{Y}$, then $$\DeclareMathOperator*{\sup}{sup} g(x) = \sup_{y \in \mathcal{Y}}f(x, y)$$ is also convex.
- **Composition with scalar function:** Given functions $g : \mathbb{R}^n \to \mathbb{R}$ and $h : \mathbb{R} \to \mathbb{R}$ their composition $$f(x) = h(g(x)),$$ is convex if (1) $g$ is convex, $h$ is convex and $\tilde{h}$ is nondecreasing; if (2) $g$ is concave, $h$ is convex and $\tilde{h}$ is nonincreasing.
- **Vector composition:** Composition with scalar functions can be extended to composition of vector functions. Suppose Given functions $g : \mathbb{R}^n \to \mathbb{R}^k$ and $h : \mathbb{R}^k \to \mathbb{R}$, then$$f(x) = h\big(g(x)\big) = h\big(g_1(x), g_2(x), ..., g_k(x)\big),$$ is convex if (1) $g_i$ are all convex, $h$ is convex and $\tilde{h}$ non-decreasing in each argument; (2) $g_i$ are all concave, $h$ is convex and $\tilde{h}$ non-increasing in each argument.

