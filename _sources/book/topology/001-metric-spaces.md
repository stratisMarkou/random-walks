# Metric spaces

The first part of the course is about metric spaces.
Metric spaces are sets equiped with a metric, which is a definition of distance.
Metrics generalise the usual notion of distance that the absolute value has on the reals, to more general spaces, and allow us to generalise the notions of convergent sequences and continuity.
However, we will later see that a function can be continuous under many different metrics.
It will turn out that the important underlying structure that determines continuity is the set of open sets corresponding to the metric, and that many different metrics define the same open sets.
This will give rise to the notion of a topology, which abstracts away the idea of a metric altogether and instead defines open sets directly.


## Metric spaces

We begin with the definition of metric spaces, which are sets equiped with a notion of distance, the metric.

:::{prf:definition} Metric space
:label: topology-def-metric-space
A metric space is a pair $(X, d_X)$ of a set $X,$ called the space, and a function $d_X: X \times X \to \mathbb{R},$ called the metric, which satisfy

1. $d(x, y) \geq 0$ for all $x, y \in X,$
2. $d(x, x) = 0$ if and only if $x \in X,$
3. $d(x, y) = d(y, x)$ for all $x, y \in X,$
4. $d(x, z) \leq d(x, y) + d(y, z)$ for all for all $x, y, z \in X.$
:::


:::{prf:example} Examples of metric spaces
__Euclidean metric:__
Let $X = \mathbb{R}^N.$
The Euclidean metric $d_X$ on $X$ is defined as 

$$ d_X(a, b) = \sqrt{\sum_{n = 1}^N (a_n - b_n)^2}, \text{ where } a, b \in X. $$

__Discrete metric:__
Let $X$ be any set.
The discrete metric $d_X$ on $X$ is defined as 

$$ d_X(a, b) = \begin{cases} 0 & \text{ if } x = y \\ 1 & \text{ if } x \neq y \\  \end{cases}, \text{ where } a, b \in X. $$
:::


:::{prf:definition} Metric subspace
Let a metric space $(X, d_X),$ and $Y \subseteq X.$
We call $(Y, d_Y)$ a metric subspace of $X$ where $d_Y: Y \to \mathbb{R}$ is defined such that $d_Y(a, b) = d_X(a, b)$ for all $a, b \in Y.$
:::

With the definition of metric spaces in place, we are ready to define convergent sequences.
This is a generalisation of convergence from the familiar definition in the context of the real numbers to more general metric spaces.


:::{prf:definition} Convergent sequence
Let $(x_n)$ be a sequence in a metric space $(X, d_X).$
We say that $(x_n)$ converges to $x \in X,$ written $x_n \to x$ if for every $\epsilon > 0,$ there exists $N \in \mathbb{N}$ such that $d_X(x_n, x) < \epsilon$ for all $n > N.$
:::

Similar to analogous results in analysis, we can show that in a metric space, limits are unique.


:::{prf:lemma} Limits in metric spaces are unique
:label: topology-lemma-limits-in-metric-spaces-are-unique
Suppose $(X, d_X)$ is a metric space and $(x_n)$ is a sequence in $X$ such that $x_n \to x$ and $x_n \to x'$ for some $x, x' \in X.$
Then $x = x'.$
:::

:::{dropdown} Proof: Limits in metric spaces are unique
Let $(X, d_X)$ be a metric space and $(x_n)$ be a sequence in $X$ such that $x_n \to x$ and $x_n \to x'$ for some $x, x' \in X.$
By the {ref}`non-negativity, symmetry and the triangle inequality of metrics<topology-def-metric-space>` we have that

$$0 \leq d(x, x') \leq d(x, x_n) + d(x_n, x') = d(x_n, x) + d(x_n, x')$$

and taking the limit $n \to \infty$ gives $d(x, x') = 0.$
:::

With convergent sequences in place, we can define continuous functions.
This definition appears slightly different than the $\epsilon-\delta$ defnition in analysis, but we will shortly see the two are equivalent.


:::{prf:definition} Continuous function
:label: topology-def-continuous-function
Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces.
A function $f: X \to Y$ is continuous if $f(x_n) \to f(x)$ in $Y$ whenever $x_n \to x$ in $X.$
:::


## Norms

We now introduce the idea of a norm, which is a definition of the length of a point in a vector space.


:::{prf:definition} Norm
:label: topology-def-norm
Let $V$ be a vector space.
A norm is a function $||\cdot||: V \to \mathbb{R}$ which satisfies the following properties.

1. $||v|| \geq 0$ for all $v \in V,$
2. $||v|| = 0$ if and only if $v = 0,$
3. $||\lambda v|| = |\lambda|||v||$ for all $\lambda \in \mathbb{R}$ and $v \in V,$
4. $||v + w|| \leq ||v|| + ||w||$ for all $v, w \in V.$
:::


A norm can be used to define a metric on a vector space.


:::{prf:lemma} Norms induce metrics
:label: topology-lemma-norms-induce-metrics
Let $V$ be a vector space with a norm $||\cdot||.$
The function $d_V: V \times V \to \mathbb{R}$ defined as $d_V(v, w) = ||v - w||$ is a metric on $V.$
:::

:::{dropdown} Proof: Norms induce metrics
Let $V$ be a vector space with a norm $||\cdot||$ and define $d_V: V \times V \to \mathbb{R}.$
Using the {ref}`properties of norms<topology-def-norm>`, for any $v, w, u \in V,$ we have

1. $d_V(v, w) = ||v - w|| \geq 0,$ by property 1 of norms,
2. $d_V(v, v) = ||v|| = 0 \iff v = 0,$ by property 2 norms,
3. $d_V(v, w) = ||v - w|| = ||w - v|| = d_V(w, v),$ by property 3 of norms,
4. $d_V(v, u) = ||v - u|| \leq ||v - w|| + ||w - u|| = d_V(v, w) + d_V(w, u),$ by property 4 of norms.
:::

:::{prf:example} Examples of norms
The following are examples of norms on $C[0, 1],$ the vector space of continuous functions with domain $[0, 1].$

$$\begin{align}
||\cdot||_1 &= \int_0^1 |\cdot(x)| dx, \\
||\cdot||_2 &= \int_0^1 |\cdot(x)|^2 dx, \\
||\cdot||_\infty &= \max_{x \in [0, 1]} |\cdot(x)| dx.
\end{align}$$
:::
