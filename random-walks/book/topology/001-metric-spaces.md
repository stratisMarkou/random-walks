# Metric spaces

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

The first part of the course is about metric spaces.
Metric spaces are sets equiped with a metric, which is a definition of distance.
Metrics generalise the usual notion of distance that the absolute value has on the reals, to more general spaces, and allow us to generalise the notions of convergent sequences and continuity.
However, we will later see that a function can be continuous under many different metrics.
It will turn out that the important underlying structure that determines continuity is the set of open sets corresponding to the metric, and that many different metrics define the same open sets.
This will give rise to the notion of a topology, which abstracts away the idea of a metric altogether and instead defines open sets directly.


## Metric spaces

We begin with the definition of metric spaces.
A metric space is a set that is equiped with a notion of distance between elements, the metric.

:::{prf:definition} Metric space
:label: topology:def:metric-space
A metric space is a pair $(X, d_X)$ of a set $X,$ called the space, and a function $d_X: X \times X \to \mathbb{R},$ called the metric, which for all $x, y, z \in X$ satisfies

1. $d(x, y) \geq 0,$
2. $d(x, y) = 0$ if and only if $x = y,$
3. $d(x, y) = d(y, x),$
4. $d(x, z) \leq d(x, y) + d(y, z).$
:::


Two common examples of metrics, which we will use later on, are the familiar Euclidean metric and the discrete metric.

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
Let a {prf:ref}`metric space<topology:def:metric-space>` $(X, d_X),$ and $Y \subseteq X.$
We call $(Y, d_Y)$ a metric subspace of $X$ where $d_Y: Y \to \mathbb{R}$ is defined such that $d_Y(a, b) = d_X(a, b)$ for all $a, b \in Y.$
:::

With the definition of metric spaces in place, we are ready to define convergent sequences.
This is a generalisation of convergence from the familiar definition in the context of the real numbers to more general metric spaces.


:::{prf:definition} Convergent sequence
Let $(x_n)$ be a sequence in a {prf:ref}`metric space<topology:def:metric-space>` $(X, d_X).$
We say that $(x_n)$ converges to $x \in X,$ written $x_n \to x$ if for every $\epsilon > 0,$ there exists $N \in \mathbb{N}$ such that $d_X(x_n, x) < \epsilon$ for all $n > N.$
:::

Similar to analogous results in analysis, we can show that in a metric space, limits are unique.


:::{prf:lemma} Limits in metric spaces are unique
:label: topology:lemma-limits-in-metric-spaces-are-unique
Suppose $(X, d_X)$ is a {prf:ref}`metric space<topology:def:metric-space>` and $(x_n)$ is a sequence in $X$ such that $x_n \to x$ and $x_n \to x'$ for some $x, x' \in X.$
Then $x = x'.$
:::

:::{dropdown} Proof: Limits in metric spaces are unique
Let $(X, d_X)$ be a metric space and $(x_n)$ be a sequence in $X$ such that $x_n \to x$ and $x_n \to x'$ for some $x, x' \in X.$
By the {ref}`non-negativity, symmetry and the triangle inequality of metrics<topology:def:metric-space>` we have that

$$0 \leq d(x, x') \leq d(x, x_n) + d(x_n, x') = d(x_n, x) + d(x_n, x')$$

and taking the limit $n \to \infty$ gives $d(x, x') = 0.$
:::

With convergent sequences in place, we can define continuous functions.
This definition appears slightly different than the $\epsilon-\delta$ defnition in analysis, but we will shortly see the two are equivalent.


:::{prf:definition} Continuous function
:label: topology:def:continuous-function
Let $(X, d_X)$ and $(Y, d_Y)$ be {prf:ref}`metric space<topology:def:metric-space>`.
A function $f: X \to Y$ is continuous if $f(x_n) \to f(x)$ in $Y$ whenever $x_n \to x$ in $X.$
:::


## Norms

We now introduce the idea of a norm, which is a definition of the length of a point in a vector space.


:::{prf:definition} Norm
:label: topology:def:norm
Let $V$ be a vector space.
A norm is a function $||\cdot||: V \to \mathbb{R}$ which satisfies the following properties.

1. $||v|| \geq 0$ for all $v \in V,$
2. $||v|| = 0$ if and only if $v = 0,$
3. $||\lambda v|| = |\lambda|||v||$ for all $\lambda \in \mathbb{R}$ and $v \in V,$
4. $||v + w|| \leq ||v|| + ||w||$ for all $v, w \in V.$
:::


A norm can be used to define a metric on a vector space.

:::{prf:lemma} Norms induce metrics
:label: topology:lemma-norms-induce-metrics
Let $V$ be a vector space with a norm $||\cdot||.$
The function $d_V: V \times V \to \mathbb{R}$ defined as $d_V(v, w) = ||v - w||$ is a metric on $V.$
:::

:::{dropdown} Proof: Norms induce metrics
Let $V$ be a vector space with a norm $||\cdot||$ and define $d_V: V \times V \to \mathbb{R}.$
Using the {ref}`properties of norms<topology:def:norm>`, for any $v, w, u \in V,$ we have

1. $d_V(v, w) = ||v - w|| \geq 0,$ by property 1 of norms,
2. $d_V(v, v) = ||v|| = 0 \iff v = 0,$ by property 2 norms,
3. $d_V(v, w) = ||v - w|| = ||w - v|| = d_V(w, v),$ by property 3 of norms,
4. $d_V(v, u) = ||v - u|| \leq ||v - w|| + ||w - u|| = d_V(v, w) + d_V(w, u),$ by property 4 of norms.
:::

:::{prf:example} Examples of norms
:label: topology:examples-of-norms
The following are examples of norms on $C[0, 1],$ the vector space of continuous functions with domain $[0, 1].$

$$\begin{align}
||\cdot||_1 &= \int_0^1 |\cdot(x)| dx, \\
||\cdot||_2 &= \int_0^1 |\cdot(x)|^2 dx, \\
||\cdot||_\infty &= \max_{x \in [0, 1]} |\cdot(x)| dx.
\end{align}$$
:::

::::{dropdown} Proof: Examples above are norms
Most of the properties of norms in {prf:ref}`topology:def:norm` follow from the definition of the examples but property 2, the identity of indiscernibles for norms, is a little more involved.
For this, we need an intermediate result that we prove here.

:::{prf:lemma} Non-constant positive continuous function has positive integral
:label: topology:lemma-non-constant-positive-continuous-function-has-positive-integral
Let $f \in C[0, 1]$ satisfy $f(x) \geq 0$ for all $x \in [0, 1].$
If $f$ is not constantly $0,$ then $\int_0^1 f(x)dx > 0.$
:::

:::{dropdown} Proof: Non-constant positive continuous function has positive integral
Suppose $f \in C[0, 1]$ satisfies $f(x) \geq 0$ for all $x \in [0, 1],$ and $f$ is not constantly $0.$
Then, there exists $x_0 \in [0, 1]$ such that $f(x_0) > a$ for some $a > 0.$
Since $f$ is continuous, there exists $\delta > 0$ such that $f(x) > a / 2$ for all $x \in (x_0 - \delta, x_0 + \delta).$
Then, defining $g \in C[0, 1]$ as

$$g(x) = \begin{cases}
a / 2 & \text{ if } x \in (x_0 - \delta, x_0 + \delta), \\
0 & \text{ otherwise}, \\
\end{cases}$$

we note that $f \geq g,$ and taking integrals we obtain

$$\int_0^1 f(x)dx \geq \int_0^1 g(x)dx \geq \int_{\max(0,~x_0 - \delta)}^{\min(1,~x_0 + \delta)} \frac{a}{2} dx \geq \frac{a\delta}{2} > 0,$$

which completes the proof.
:::

Now we can show that each of the examples is indeed a norm.
In the following, assume that $f, g \in C[0, 1]$

__Example 1:__
First, $||f||_1 \geq 0$ so the first property is satisfied.
Second, by {prf:ref}`topology:lemma-non-constant-positive-continuous-function-has-positive-integral` we have that $||f||_1 = 0$ only if $f = 0,$ so the second property is satisfied.
Third, note that $||\lambda f||_1 = |\lambda|||f||_1.$
Fourth, we have that

$$\begin{align}
||f + g||_1 &= \int_0^1 |f(x) + g(x)| dx \\
&\leq \int_0^1 (|f(x)| + |g(x)|) dx \\
&= \int_0^1 |f(x)|dx + \int_0^1|g(x)| dx \\
&= ||f||_1 + ||g||_1 dx
\end{align}$$

where going from the first to the second line holds by the triangle inequality of absolute values.


__Example 2:__
The first three parts of the argument for example 1 hold also for example 2.
For the fourth part, we have that

$$\begin{align}
||f + g||_2^2 &= \int_0^1 (f(x) + g(x))^2 dx \\
&= \int_0^1 f(x)^2 + 2f(x)g(x) + g(x)^2 dx \\
&= \int_0^1 f(x)^2 dx + 2\int_0^1 f(x)g(x)dx + \int_0^1 g(x)^2 dx \\
&\leq ||f||_2^2 + 2||f||_2||g||_2 + ||g||_2^2 dx \\
&= (||f||_2 + ||g||_2)^2 dx \\
\end{align}$$

where going from the third to the fourth line we have used the Cauchy-Schwarz inequality (which we have not proved yet, but will be given later).


__Example 3:__
Again, the first three parts of the argument for example 1 also hold for example 3.
For the fourth part, we have

$$\begin{align}
||f + g||_\infty &= \max_{x \in [0, 1]} |f(x) + g(x)| \\
&\leq \max_{x \in [0, 1]} |f(x)| + |g(x)| \\
&\leq \max_{x \in [0, 1]} |f(x)| + \max_{x \in [0, 1]} |g(x)| \\ 
&\leq ||f||_\infty + ||g||_\infty,
\end{align}$$

where from the first to the second line we have used the triangle inequality of the absolute value, and from the second to the third we have used the fact that the maximum of a sum of two functions is no greater than the sum of their maxima.

This concludes the proof showing that all four examples are norms.
::::


## Inner products

Now we turn to inner products.
Inner products generalise the notion of angles between vectors to general vector spaces.

:::{prf:definition} Inner product
:label: topology:inner-product-space
Let $V$ be a vector space.
An inner product on $V$ is a function $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{R}$ which satisfies:

1. $\langle v, v \rangle \geq 0$ for all $v \in V,$
2. $\langle v, v \rangle = 0$ if and only if $v = 0,$
3. $\langle v, w \rangle = \langle w, v \rangle$ for all $v, w \in V,$
4. $\langle v_1 + \lambda v_2, w \rangle = \langle v_1, w \rangle + \lambda \langle v_2, w \rangle $ for all $v_1, v_2, w \in V$ and $\lambda \in \mathbb{R}.$
:::

The properties of an inner product look very similar to those of a norm.
In fact an inner product can be used to define a norm on a vector space.
To show this, we must first however show an intermediate result for inner products.

:::{prf:lemma} Cauchy-Schwarz inequality
:label: topology:cauchy-schwarz
If $\langle \cdot, \cdot \rangle$ is an {prf:ref}`inner product<topology:inner-product-space>` on a vector space $V,$ then for all $v, w \in V,$ we have

$$\langle v, w \rangle^2 \leq \langle v, v \rangle \langle w, w \rangle.$$
:::

:::{dropdown} Proof: Cauchy-Schwarz inequality
Let $v, w \in V$ and $\lambda \in \mathbb{R}.$
Then, by the {prf:ref}`properties of inner products<topology:inner-product-space>`, we have

$$\langle v + \lambda w, v + \lambda w \rangle \geq 0.$$

Expanding the left-hand side, we obtain

$$\langle v, v \rangle + 2\lambda \langle v, w \rangle + \lambda^2 \langle w, w \rangle \geq 0,$$

and since the quadratic in $\lambda$ is non-negative, the discriminant must be non-positive, giving

$$4\langle v, w \rangle^2 - 4\langle v, v \rangle \langle w, w \rangle \leq 0,$$

which rearranges to the Cauchy-Schwarz inequality.
:::


We can now show that an inner product induces a norm.

:::{prf:lemma} Inner products induce norms
:label: topology:lemma-inner-products-induce-norms
Let $V$ be a vector space with an {prf:ref}`inner product<topology:inner-product-space>` $\langle \cdot, \cdot \rangle.$
The function $||\cdot||: V \to \mathbb{R}$ defined as

$$||v|| = \sqrt{\langle v, v \rangle}$$

is a norm on $V.$
:::

:::{dropdown} Proof: Inner products induce norms
Let $V$ be a vector space with an inner product $\langle \cdot, \cdot \rangle$ and define $||\cdot||: V \to \mathbb{R}.$
Using the {ref}`properties of inner products<topology:inner-product-space>`, for any $v, w \in V,$ we have

1. $||v|| = \sqrt{\langle v, v \rangle} \geq 0,$ by property 1 of inner products,
2. $||v|| = 0 \iff \langle v, v \rangle = 0 \iff v = 0,$ by property 2 of inner products,
3. $||\lambda v|| = \sqrt{\langle \lambda v, \lambda v \rangle} = \sqrt{\lambda^2 \langle v, v \rangle} = |\lambda|||v||,$ by property 3 of inner products,
4. $||v + w||^2 = \langle v, v \rangle + \langle v, w \rangle + \langle w, v \rangle + \langle w, w \rangle = ||v||^2 + 2\langle v, w \rangle + ||w||^2 \leq ||v||^2 + 2||v|| ||w|| + ||w||^2 = (||v|| + ||w||)^2,$ by {prf:ref}`Cauchy-Schwarz inequality<topology:cauchy-schwarz>`.

Therefore $||\cdot||$ is a norm on $V.$
:::


## Open and closed sets

We now turn to open and closed sets in metric spaces.
These will turn out to be the key objects that determine continuity of functions in metric spaces.
We first define open and closed balls.

:::{prf:definition} Open and closed balls
:label: topology:def:open-and-closed-balls
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>`.
For any $x \in X$ and $r > 0,$ we define the open ball to be the set

$$B_r(x) = \{ x' \in X : d_X(x, x') < r \},$$

and the closed ball to be the set

$$\overline{B}_r(x) = \{ x' \in X : d_X(x, x') \leq r \}.$$
:::


With open and closed balls defined, we can now define open and closed sets.

:::{prf:definition} Open and closed subsets
:label: topology:def:open-and-closed-subsets
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>`.
A subset $U \subseteq X$ is open if for every $x \in U,$ there exists $r > 0$ such that $B_r(x) \subseteq U.$
A subset $C \subseteq X$ is closed if its complement $X \setminus C$ is open.
:::


We can now show that the terms _open ball_ and _closed ball_ are in fact justified, by showing that open balls are open subsets and closed balls are closed subsets.

:::{prf:lemma} Open (closed) balls are open (closed)
:label: topology:lemma-open-and-closed-balls-are-open-and-closed
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>`.
Then, for any $x \in X$ and $r > 0,$ the {prf:ref}`open ball<topology:def:open-and-closed-balls>` $B_r(x)$ is an open subset of $X$ and the {prf:ref}`closed ball<topology:def:open-and-closed-balls>` $\overline{B}_r(x)$ is a closed subset of $X.$
:::

:::{dropdown} Proof: Open (closed) balls are open (closed)
Let $(X, d_X)$ be a metric space and $x \in X$ and $r > 0.$
Then, for any $x' \in B_r(x),$ we have $d_X(x, x') < r,$ so we can choose $\epsilon = r - d_X(x, x') > 0.$
By the {prf:ref}`triangle inequality<topology:def:metric-space>`, we have that $B_\epsilon(x') \subseteq B_r(x),$ so $B_r(x)$ is open.

Similarly, suppose $x' \in X \setminus \overline{B}_r(x).$
Then, $d_X(x, x') > r,$ so we can choose $\epsilon = d_X(x, x') - r > 0,$ and by the triangle inequality we have that $B_\epsilon(x') \subseteq X \setminus \overline{B}_r(x),$ so $X \setminus \overline{B}_r(x)$ is open and $\overline{B}_r(x)$ is closed.
:::


Sometimes it's handy to have the following shorthand when talking about open sets.

:::{prf:definition} Open neighbourhood
:label: topology:def:open-neighbourhood
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>`.
If $x \in X,$ an open neighbourhood of $x$ is an open set $U \subseteq X$ such that $x \in U.$
:::


We can re-express convergence of sequences in terms of this shorthand.

:::{prf:lemma} Convergence implies sequence eventually in open neighbourhood
:label: topology:lemma-convergence-implies-sequence-eventually-in-open-neighbourhood
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>` and $(x_n)$ be a sequence in $X$ that converges to $x \in X.$
Then, for every {prf:ref}`open neighbourhood<topology:def:open-neighbourhood>` $U$ of $x,$ there exists $N \in \mathbb{N}$ such that $x_n \in U$ for all $n > N.$
:::

:::{dropdown} Proof: Convergence implies sequence eventually in open neighbourhood
Let $(X, d_X)$ be a metric space and $(x_n)$ be a sequence in $X$ that converges to $x \in X.$
Let $U$ be an open neighbourhood of $x.$
Since $U$ is open, there exists $r > 0$ such that $B_r(x) \subseteq U.$
Since $x_n \to x,$ there exists $N \in \mathbb{N}$ such that $d_X(x_n, x) < r$ for all $n > N,$ so $x_n \in B_r(x) \subseteq U$ for all $n > N.$
:::


Now we define limit points of sets.
Intuitively, a limit point of a set is a point that is the limit of some sequence in the set.
Note that a limit point of a set need not itself be in the set.

:::{prf:definition} Limit point
:label: topology:def:limit-point
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>` and $A \subseteq X.$
A point $x \in X$ is a limit point of $A$ if there exists a sequence $(x_n)$ in $A$ such that $x_n \to x.$
:::


Limit points allow an equivalent definition of closed sets, as stated in the following lemma.

:::{prf:lemma} Closed set $\iff$ set contains all its limit points
:label: topology:lemma-closed-set-iff-set-contains-all-its-limit-points
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>` and $A \subseteq X.$
The set $A$ is {prf:ref}`closed<topology:def:open-and-closed-subsets>` if and only if $A$ contains all its {prf:ref}`limit points<topology:def:limit-point>`.
:::

:::{dropdown} Proof: Closed set $\iff$ set contains all its limit points
Let $(X, d_X)$ be a metric space and $C \subseteq X.$

($\Rightarrow$) Suppose $C$ is closed.
Let $x$ be a limit point of $C,$ and suppose that $x \notin C.$
Then, $x \in X \setminus C,$ which is open by the definition of a closed set.
Since $x$ is a limit point of $C,$ there exists a sequence $(x_n)$ in $C$ such that $x_n \to x.$
But since $X \setminus C$ is an open neighbourhood of $x,$ there exists $N \in \mathbb{N}$ such that $x_n \in X \setminus C$ for all $n > N,$ which contradicts the assumption that $x \notin C.$

($\Leftarrow$) Suppose $C$ contains all its limit points.
We want to show that $X \setminus C$ is open.
For this, suppose $x \in X \setminus C.$
We will show that there exists $n \in \mathbb{N}$ such that $B_{1 / n}(x) \subseteq X \setminus C.$
Suppose that this is not the case.
Then, for each $n \in \mathbb{N},$ we have $B_{1 / n}(x) \cap C \neq \emptyset,$ so we can choose $x_n \in B_{1 / n}(x) \cap C.$
Then, $x_n \to x,$ so $x$ is a limit point of $C$ and since $C$ contains all its limit points, it must also contain $x,$ which contradicts the assumption that $x \in X \setminus C.$
:::


Now we turn to the important result of the first part of the course.
This result shows that the thing that determines whether a function is continuous is not the metric itself, but rather the collection of sets that are open under the metric.
In particular, even if two metrics are different, if they define the same open sets, then the same functions will be continuous under both of them.

:::{prf:theorem} Characterisation of continuity
:label: topology:theorem-characterisation-of-continuity
Let $(X, d_X)$ and $(Y, d_Y)$ be {prf:ref}`metric spaces<topology:def:metric-space>` and $f: X \to Y$ be a function.
Then, the following are equivalent:

1. $f$ is {prf:ref}`continuous<topology:def:continuous-function>`,
2. $f(x_n) \to f(x)$ in $Y$ whenever $x_n \to x$ in $X,$
3. For every {prf:ref}`open set<topology:def:open-and-closed-subsets>` $U \subseteq Y,$ the preimage $f^{-1}(U)$ is open in $X,$
4. For every {prf:ref}`closed set<topology:def:open-and-closed-subsets>` $C \subseteq Y,$ the preimage $f^{-1}(C)$ is closed in $X,$
5. For every $x \in X$ and $\epsilon > 0,$ there exists $\delta > 0$ such that $f(B_\delta(x)) \subseteq B_\epsilon(f(x)).$
:::

:::{dropdown} Proof: Characterisation of continuity
We break the proof down into a series of implications.

($1 \iff 2$) This is the definition of {prf:ref}`continuity<topology:def:continuous-function>`.

($2 \Rightarrow 3$) Suppose $f(x_n) \to f(x)$ in $Y$ whenever $x_n \to x$ in $X.$
Suppose $U \subseteq Y$ is open but $f^{-1}(U)$ is not.
Then, there exists $x \in f^{-1}(U)$ such that for every $n \in \mathbb{N}$ there exists $x_n \in B_{1 / n}(x)$ such that $x_n \notin f^{-1}(U).$
This implies that $f(x_n) \notin U$ for any $n \in \mathbb{N}.$
However, $x_n \to x$ in $X,$ so $f(x_n) \to f(x)$ in $Y.$
This is a contradiction because since $U$ is open, any sequence that converges to a point in $U$ must {prf:ref}`eventually be<topology:lemma-convergence-implies-sequence-eventually-in-open-neighbourhood>` in $U$.

($3 \Rightarrow 4$) Suppose that for every open set $U \subseteq Y,$ the preimage $f^{-1}(U)$ is open in $X.$
Then, for every closed set $C \subseteq Y,$ the set $Y \setminus C$ is open so the set $f^{-1}(Y \setminus C)$ is open, so the preimage $f^{-1}(C) = X \setminus f^{-1}(Y \setminus C)$ is closed in $X.$

($4 \Rightarrow 5$) Suppose that for every closed set $C \subseteq Y,$ the preimage $f^{-1}(C)$ is closed in $X.$
Let $x \in X$ and $\epsilon > 0.$
Since $Y \setminus B_\epsilon(f(x))$ is closed, $f^{-1}(Y \setminus B_\epsilon(f(x))) = X \setminus f^{-1}(B_\epsilon(f(x)))$ is closed.
Therefore, the set $f^{-1}(B_\epsilon(f(x)))$ is open, so there exists $\delta > 0$ such that $B_\delta(x) \subseteq f^{-1}(B_\epsilon(f(x))),$ which implies that $f(B_\delta(x)) \subseteq B_\epsilon(f(x)).$

($5 \Rightarrow 2$) Suppose that for every $x \in X$ and $\epsilon > 0,$ there exists $\delta > 0$ such that $f(B_\delta(x)) \subseteq B_\epsilon(f(x)).$
Suppose $(x_n)$ is a sequence in $X$ such that $x_n \to x.$
Let $\epsilon > 0.$
Then, there exists $\delta > 0$ such that $f(B_\delta(x)) \subseteq B_\epsilon(f(x)).$
Since $x_n \to x,$ there exists $N \in \mathbb{N}$ such that $x_n \in B_\delta(x)$ for all $n > N,$ so $f(x_n) \in f(B_\delta(x)) \subseteq B_\epsilon(f(x))$ for all $n > N,$ which implies that $f(x_n) \to f(x).$
:::


We conclude with three properties of open sets that we will use to define toplogies in the next section.

:::{prf:lemma} Properties of open sets
:label: topology:lemma-properties-of-open-sets
Let $(X, d_X)$ be a {prf:ref}`metric space<topology:def:metric-space>`.
Then

1. The empty set $\emptyset$ and $X$ are open,
2. If $\{U_i\}_{i \in I}$ is a collection of open sets, then $\bigcup{i \in I} U_i$ is open,
3. If $U_1, \ldots, U_N$ are open sets, then $\bigcap{n = 1}^N U_n$ is open.
:::

:::{dropdown} Proof: Properties of open sets
__Property 1:__
The empty set is open vacuously.
The whole space $X$ is open because for every $x \in X,$ we have $B_r(x) \subseteq X,$ for any $r > 0.$

__Property 2:__
Let $\{U_i\}_{i \in I}$ be a collection of open sets.
Suppose $x \in \cup_{i \in I} U_i.$
Then, there exists $i \in I$ such that $x \in U_i,$ so there exists $r > 0$ such that $B_r(x) \subseteq U_i \subseteq \bigcup_{i \in I} U_i,$ so $\bigcup_{i \in I} U_i$ is open.

__Property 3:__
Let $U_1, \ldots, U_N$ be open sets.
Suppose $x \in \cap_{n = 1}^N U_n.$
Then, $x \in U_n$ for all $n = 1, \ldots, N,$ so there exists $r_n > 0$ such that $B_{r_n}(x) \subseteq U_n$ for all $n = 1, \ldots, N.$
Taking $r = \min\{r_1, \ldots, r_N\},$ we have that $B_r(x) \subseteq U_n$ for all $n = 1, \ldots, N,$ so $\cap_{n = 1}^N U_n$ is open.
:::
