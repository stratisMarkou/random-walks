# Metric spaces

The first part of the course is about metric spaces.
Metric spaces are sets equiped with a metric, which is a definition of distance.
Metrics generalise the usual notion of distance that the absolute value has on the reals, to more general spaces, and allow us to generalise the notions of convergent sequences and continuity.
However, we will later see that a function can be continuous under many different metrics.
It will turn out that the important underlying structure that determines continuity is the set of open sets corresponding to the metric, and that many different metrics define the same open sets.
This will give rise to the notion of a topology, which abstracts away the idea of a metric altogether and instead defines open sets directly.


## Metric spaces

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
By the {ref}`non-negativity and the triangle inequality of metrics<topology-def-metric-space>` we have that

$$ 0 \leq d(x, x') \leq d(x, x_n) + d(x_n, x') $$

and taking the limit $n \to \infty$ gives $d(x, x') = 0.$
:::

