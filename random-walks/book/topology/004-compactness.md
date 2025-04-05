# Compactness


:::{margin}
Here is some [additional intuition](https://math.stackexchange.com/questions/371928/what-should-be-the-intuition-when-working-with-compactness/371949#371949) on compactness.
:::

The final part of the course is about compactness.
Compactness is a slightly less intuitive property than, for example, connectivity.
Roughly speaking, compactness can be viewed as a generalisation of what it means for a subset of $\mathbb{R}^n$ to be closed and bounded, to other topological spaces.


## Compact spaces

The notion of compactness relies on open covers as defined below.

:::{prf:definition} Open cover
Let $\mathcal{U} \subseteq 2^X$ be a {prf:ref}`topology<topology:def-topological-space>` on $X.$
An open cover of $X$ is a subset $\mathcal{V} \subseteq \mathcal{U}$ such that

$$\begin{equation}
\bigcup_{V \in \mathcal{V}} V = X.
\end{equation}$$

We say $\mathcal{V}$ covers $X.$
If $\mathcal{V}' \subseteq \mathcal{V}$ and $\mathcal{V}'$ covers $X,$ then we say $\mathcal{V}'$ is a subcover of $\mathcal{V}.$
:::

Now, a space is defined to be compact if any open cover of the space contains a finite subcover.

:::{prf:definition} Compact space
:label: topology:def-compact-space
A {prf:ref}`topological space<topology:def-topological-space>` $X$ is {prf:ref}`compact<topology:def-compact-space>` if every open cover $\mathcal{V}$ of $X$ has a finite {prf:ref}`subcover<topology:def-topological-space>` $\mathcal{V}' = \{V_1, \dots, V_n\} \subseteq \mathcal{V}.$
:::

We note that compactness is topological property:
if a compact space is homeomorphic to another space, the second space is also compact.
The first result that we show is that the closed unit interval is compact.

:::{prf:theorem} Closed interval is compact
:label: topology:closed-interval-is-compact
The closed interval $[0, 1] \subseteq \mathbb{R}$ with the standard topology is {prf:ref}`compact<topology:def-compact-space>`.
:::

:::{dropdown} Closed interval is compact
Suppose $\mathcal{V}$ is an open cover of $[0, 1].$
Define

$$\begin{equation}
A = \{a \in [0, 1] : [0, a] \text{ has a finite subcover from } \mathcal{V} \}.
\end{equation}$$

We first show that $A$ is non-empty.
Since $\mathcal{V}$ is an open cover of $[0, 1],$ there exists $V \in \mathcal{V}$ that contains $0.$
Therefore $\{0\}$ has a finite sub-cover from $\mathcal{V}$ and $0 \in A.$

Now, let $\alpha = \sup A.$
Suppose $\alpha < 1.$
Since $\mathcal{V}$ covers $[0, 1],$ there exists open $V_\alpha \in \mathcal{V}$ with $\alpha \in V_\alpha.$
Since $V_\alpha$ is open, there exists $\epsilon > 0$ such that $B_\epsilon(\alpha) \subseteq V_\alpha.$
By the definition of $\alpha,$ the set $[0, \max(0, \alpha - \epsilon / 2)]$ has a finite subcover, to which we can add $V_\alpha$ to get a finite subcover of $[0, \min(1, \alpha + \epsilon / 2)].$
This leads to a contradiction, so $\alpha = 1.$

We finally show that $\alpha \in A.$
Repeating this argument, since $\mathcal{V}$ covers $[0, 1],$ there exists open $V_1 \in \mathcal{V}$ that contains $1,$ such that $(1 - \epsilon, 1] \subseteq V_1.$
Since $1 - \epsilon / 2 \in A,$ there exists a finite $\mathcal{V}' \subseteq \mathcal{V}$ which covers $[0, 1 - \epsilon].$
Then $\mathcal{W} = \mathcal{V}' \cup \{V_1\}$ is a finite subcover of $\mathcal{V}.$
:::

Note how this proof relies on the fact that the open interval is closed and bounded.
For example, $\mathbb{R}$ is not compact because the set $\{(n, n+2): n \in \mathbb{N}\}$ is an open cover that does not contain a finite subcover.
Similarly, the open interval $(0, 1)$ is not compact even though it is bounded, since the set $\{(n^{-1}, 1): n \in \mathbb{N}\}$ is an open cover that does not contain a finite subcover.

We now show two useful results.
First, we note that a subset of a compact space is not necessarily a compact space: $(0, 1) \subseteq [0, 1]$ but the former is not compact even though the latter is.
However, a closed subset of a compact space is compact.

:::{prf:lemma} Closed subsets of compact spaces are compact
:label: topology:lem-closed-subsets-of-compact-spaces-are-compact
If $X$ is {prf:ref}`compact<topology:def-compact-space>` and $C$ is a closed subset of $X,$ then $C$ is also compact.
:::

:::{dropdown} Proof: Closed subsets of compact spaces are compact
Suppose $X$ is compact and $C$ is a closed subset of $X.$
Let $\mathcal{V}$ be an open cover of $C.$
Then since each $V \in \mathcal{V}$ is open in $C,$ there exists open $V'$ in $X$ such that $V' \cap C = V.$
Then, the set $\mathcal{W}$ containing all such $V',$ i.e. all open $V'$ such that $V' \cap C = V$ for some $V \in \mathcal{V},$ together with the open set $X \setminus C,$ is an open cover of $X.$
Since $X$ is compact, it has a finite subcover from $\mathcal{W},$ and since $C \subseteq X,$ this also gives a finite subcover for $C,$ which is therefore compact.
:::

Second, a similar result holds for closedness:
a compact subspace of a Hausdorff space is closed.

:::{prf:lemma} Compact subspaces of Hausdorff spaces are closed
:label: topology:lemma-compact-subspaces-of-hausdorff-spaces-are-closed
Let $X$ be a {prf:ref}`Hausdorff space<topology:def-hausdorff-space>`.
If $C \subseteq X$ is {prf:ref}`compact<topology:def-compact-space>`, then $C$ is closed in $X.$
:::

:::{dropdown} Proof: Compact subspaces of Hausdorff spaces are closed
Let $X$ be a Hausdorff space.
Suppose $C \subseteq X$ is compact.
We will show that $X \setminus C$ is open.

Suppose $x \in X \setminus C.$
We will show there exists an open $U \subseteq X \setminus C$ that contains $x.$
Since $X$ is Hausdorff, for each $y \in C$ there exists an open $W_{xy}$ containing $y$ and an open $U_{xy}$ containing $x$ such that $W_{xy} \cap U_{xy} = \emptyset.$
Then, the collection $\{W_{xy} \subseteq X: y \in C\}$ is an open cover of $C,$ and since $C$ is compact, it has a finite subcover of the form $\{W_{x_1y}, \dots, W_{x_Ny}\}.$
Then the set $\cap_{n = 1}^N U_{x_ny}$ is open because it is a finite interesection of open sets, and it does not intersect $C,$ so it is contained in $X \setminus C.$
Therefore $X \setminus C$ is open and $C$ is closed.
:::


It turns out that for $\mathbb{R}^n$ with the standard topology, compactness is equivalent to closedness plus boundedness.
To show this, we first define boundedness for metric spaces.

:::{prf:definition} Bounded metric space
A {prf:ref}`metric space<topology:def-metric-space>` $(X, d)$ is bounded if there exists $M \in \mathbb{R}$ such that $d(x, y) \leq M$ for all $x, y \in X.$
:::

Note that being bounded is not a topological property.
For example $(0, 1) \simeq \mathbb{R}$ are homeomorphic but $(0, 1)$ is bounded while $\mathbb{R}$ is not.
A useful intermediate result is that a closed metric space is bounded.

:::{prf:lemma} Compact metric spaces are bounded
:label: topology:lem-compact-metric-spaces-are-bounded
A {prf:ref}`compact<topology:def-compact-space>` {prf:ref}`metric space<topology:def-metric-space>` $(X, d)$ is bounded.
:::

:::{dropdown} Proof: Compact metric spaces are bounded
Suppose $(X, d)$ is compact.
Pick $x \in X.$
Then $V = \{B_r(x) : r \in \mathbb{R}^+\}$ is an open cover of $X.$
Since $X$ is compact, there exists a finite subcover of the form $\{B_{r_1}(x), \dots, B_{r_n}(x)\}.$
Let $R = \max\{r_1, \dots, r_n\}.$
Then $d(x, y) < R$ for all $y \in X,$ so for all $y, z \in X$ we have

$$\begin{equation}
d(y, z) \leq d(y, x) + d(x, z) < 2R.
\end{equation}$$

Therefore $X$ is boudnded.
:::

We now arrive at one of the main results of this section, the Heine Borel theorem, which states a subsets of $\mathbb{R}$ is compact if and only if it is closed and bounded.

:::{prf:theorem} Heine-Borel
A subset $C \subseteq \mathbb{R}$ with the standard topology is {prf:ref}`compact<topology:def-compact-space>` if and only if it is closed and bounded.
:::

:::{dropdown} Proof: Heine-Borel
Suppose $C \subseteq \mathbb{R}$ with the standard topology.

__Implies:__
Suppose $C$ is closed and bounded.
Since $C$ is bounded, it is contained in a closed set $[-M, M]$ for some $M \in \mathbb{R}.$
Therefore $C$ is a closed subset of a compact space $[-M, M] \simeq [0, 1],$ therefore it is compact.

__Implied by:__
Suppose $C$ is compact.
Since $\mathbb{R}$ is a metric space, it is also Hausdorff, and since $C$ is compact it follows that it is closed ({prf:ref}`topology:lem-closed-subsets-of-compact-spaces-are-compact`).
In addition, since $C$ is a compact metric space, it is also bounded ({ref:prf}`topology:lem-compact-metric-spaces-are-bounded`).
:::

The Heine-Borel theorem formalises the earlier point we made about compactness being a generalisation of closedness plus boundedness, beyond the reals.


:::{prf:lemma} Compact subsets of $\mathbb{R}$ have finite upper bounds
If $A \subseteq \mathbb{R}$ with the standard topology is {prf:ref}`compact<topology:def-compact-space>`, there exists $\alpha \in A$ such that $\alpha \geq a$ for all $a \in A.$
:::

:::{dropdown} Proof: Compact subsets of $~\mathbb{R}~$ have finite upper bounds
Suppose $A \subseteq \mathbb{R}$ with the standard topology is compact.
Since $A$ is compact, it is bounded and closed.
Let $\alpha = \sup A.$
Then $\alpha \geq a$ for all $a \in A,$ and it remains to show that $\alpha \in A.$

Suppose that $\alpha \not \in A.$
Then $x \in \mathbb{R} \setminus A$ and since $A$ is closed, $\mathbb{R} \setminus A$ is open.
By the definition of supremum, for each $\epsilon > 0,$ there exists $a \in A$ such that $|\alpha - a| < \epsilon.$
This is a contradiction, because there must exist a sufficiently small ball centered on $\alpha$ that is contained in $\mathbb{R} \setminus A,$ because the latter is open.
Therefore $\alpha \in A.$
:::


:::{prf:lemma} Image of compact space under continuous function is compact
:label: topology:lem-image-of-compact-space-under-continuous-function-is-compact
Let $X$ and $Y$ be {prf:ref}`topological spaces<topology:def-topological-space>`.
If $f: X \to Y$ is continuous and $X$ is {prf:ref}`compact<topology:def-compact-space>`, then $\text{im}f \subseteq$ is also compact.
:::

:::{dropdown} Proof: Image of compact space under continuous function is compact
Let $X$ and $Y$ be topological spaces.
Suppose $f: X \to Y$ is continuous and $X$ is compact.

Let $\mathcal{V} = \{V_\alpha \subseteq Y: \alpha \in T\}$ be an open cover of $\text{im}f.$
Then the sets $f^{-1}(V_\alpha), \alpha \in T$ are open in $X$ and also form an open cover of it.
Since $X$ is compact, it has a finite subcover of the form $\{f^{-1}(V_{\alpha_1}), \dots, f^{-1}(V_{\alpha_n})\}.$
We conclude that $V_{\alpha_1}, \dots, V_{\alpha_N}$ form a finite subcover of $\text{im}f,$ which is therefore comapct.
:::


:::{prf:definition} Maximum value theorem
:label: topology:maximum-value-theorem
If $X$ is a {prf:ref}`compact<topology:def-compact-space>` {prf:ref}`topological space<topology:def-topological-space>` and $f: X \to \mathbb{R}$ is continuous with the standard topology, then $x \in X$ such that $f(x) \geq f(x')$ for all $x' \in X.$
:::

:::{dropdown} Proof: Maximum value theorem
Suppose $X$ is a {prf:ref}`topological space<topology:def-topological-space>` and let $f: X \to \mathbb{R}$ be continuous.
The image of a compact set under a continuous function is compact ({prf:ref}`topology:lem-image-of-compact-space-under-continuous-function-is-compact`), so $\text{im}f$ is compact.
Since $\mathbb{R}$ is a {prf:ref}`metric space<topology:def-metric-space>`, so $\text{im}f$ is also a metric space and is therefore {prf:ref}`Hausdorff<topology:def-hausdorff-space>`.
Because $\text{im}f$ is a compact metric space, it must be bounded ({prf:ref}`topology:lem-compact-metric-spaces-are-bounded`).
Therefore $\text{im} f$ contains its supremum, i.e. $f(x) = \sup \text{im} f$ for some $x \in X.$
By definition of the supremum, $f(x) \geq f(x')$ for all $x' \in X.$
:::


:::{prf:lemma} Maximum value theorem for $[0, 1]$
If $f: [0, 1] \to \mathbb{R}$ is continuous with the standard topology on both $[0, 1]$ and $\mathbb{R},$ then there exists $x \in X$ such that $f(x) \geq f(x')$ for all $x' \in X.$
:::

:::{dropdown} Maximum value theorem for $~[0, 1]$
This follows from {prf:ref}`topology:maximum-value-theorem`, since the closed interval $[0, 1]$ with the standard topology is {prf:ref}`compact<topology:def-compact-space>`.
:::


## Products and quotients

Now we turn to some properties of products and quotients of compact spaces.
The results in this section are very useful for proving many other properties.

### Product spaces

One particularly useful result is that the product of compact spaces is compact.

:::{prf:theorem} Product of compact spaces is compact
If $X$ and $Y$ are {prf:ref}`compact<topology:def-compact-space>` {prf:ref}`topological spaces<topology:def-topological-space>`, then $X \times Y$ is compact.
:::

:::{dropdown} Proof: Product of compact spaces is compact
Suppose $X$ and $Y$ are compact {prf:ref}`topological spaces<topology:def-topological-space>`.
Let $\mathcal{V}$ be an open cover of $X \times Y.$

First, we consider the special case where each $U \in \mathcal{V}$ has the form $U = V \times W$ where $V \in X$ and $W \in Y.$
Since $\mathcal{V}$ is an open cover of $X \times Y,$ for each $(x, y) \in X \times Y$ there exists $U_{xy} \in \mathcal{V}$ such that $(x, y) \in U_{xy}.$
By our previous assumption we can write this as $U_{xy} = V_{xy} \times W_{xy}$ where $V_{xy} \in X$ and $W_{xy} \in Y.$

Now fix $x \in X.$
The set $\{W_{xw}: y \in Y\}$ is an open cover of $Y$ and since $Y$ is compact, it has a finite subcover $\{W_{xy_1}, \dots, W_{xy_N}\}.$
Now, define $V_x = \cap_{n=1}^N V_{xy_n},$ and note that $V_x$ is a finite intersection of open sets so it is open in $X.$
In addition, $\mathcal{U}_x = \{R_{xy_1}, \dots, U_{xy_N}\}$ is a finite open cover of $V_x \times Y.$
Now, $\{V_x: x \in X\}$ is an open cover of $X$ and since $X$ is compact, it has a finite subcover $\{V_{x_1}, \dots, V_{x_M}\}.$
Therefore $\cup_{m = 1}^M \mathcal{R}_{x_m}$ is a finite subset of $\mathcal{V}$ which covers $X \times Y.$

Now consider the general case where $\mathcal{V}$ is an arbitrary open cover of $X \times Y.$
For each $(x, y) \in X \times Y,$ there exists open $U_{xy} \in \mathcal{V}$ such that $(x, y) \in X \times Y.$
Since $U_{xy}$ is open, there exist open $V_{xy} \subseteq X$ and open $W_{xy} \subseteq Y$ such that $x \in V_{xy}$ and $y \in W_{xy}$ and $V_{xy} \times W_{xy} \subseteq U_{xy}.$
Then, the set $\{V_{xy} \times W_{xy} : (x, y) \in X \times Y\}$ is an open cover of $X \times Y$ of the special case we ahve considered above.
Therefore it has a finite subcover $\{V_{x_1y_1} \times W_{x_1y_1}, \dots, V_{x_Ny_N} \times W_{x_Ny_N}\}.$
Noting that $V_{x_ny_n} \times W_{x_ny_n} \subseteq U_{x_ny_n},$ we see that $\{U_{x_1y_1} \dots U_{x_Ny_N}\}$ has a finite subcover of $X \times Y.$
Therefore $X \times Y$ is compact.
:::


### Quotient spaces

First, we remark that the quotient space of a compact space must be compact, since any open set in the quotient space can be related to an open set in the original space.

:::{prf:lemma} Quotient space of a compact space is compact
:label: topology:lem-quotient-space-of-a-compact-space-is-compact
Suppose $X$ is a compact space and $\sim$ an equivalence relation on $X.$
The quotient space $X / \sim$ is compact.
:::

:::{dropdown} Proof: quotient space of a compact space is compact
Suppose $X$ is a compact space and $\sim$ an equivalence relation on $X.$
Let $\pi: X \to X / \sim$ be the projection map of $\sim.$ 
Let $\mathcal{V}$ be an open cover of $X / \sim.$
Then for each $V \in \mathcal{V},$ $\pi^{-1}(V)$ is open in $X,$ and the set $\mathcal{W} = \{\pi^{-1}(V) \subseteq X: V \in \mathcal{V}\}$ is an open cover of $X.$
Since $X$ is compact $\mathcal{W}$ has a finite subcover $\{W_1, \dots, W_n\}$ so $\{\pi(W_1), \dots, \pi(W_n)\} \subseteq \mathcal{V}$ is a finite open cover of $X / \sim.$
Therefore $X / \sim$ is compact.
:::

We now show two useful results on quotient spaces, specifically we show two sufficient conditions for a map on a compact space to be a homeomorphism.

:::{prf:lemma} Sufficient condition for homeomorphism
:label: topology:lem-sufficient-condition-for-homeomorphism
Suppose $f: X \to Y$ is a continuous bijection.
If $X$ is {prf:ref}`compact<topology:def-compact-space>` and $Y$ is {prf:ref}`Hausdorff<topology:def-hausdorff-space>`, then $f$ is a homeomorphism.
:::

:::{dropdown} Proof: Sufficient condition for homeomorphism
By assumption, $f$ is a continuous bijection so it remains to show that $f^{-1}$ is continuous.
We will show that if $C \subseteq X$ is closed in $X,$ then $(f^{-1})^{-1}(C)$ is closed in $Y.$

Since $f$ is a bijection, $(f^{-1})^{-1}(C) = f(C).$
Since $X$ is compact, $C$ is compact which, together with the fact that $f$ is continuous implies that $f(C) = \text{im}f|_C$ is compact ({prf:ref}`topology:lem-image-of-compact-space-under-continuous-function-is-compact`).
The set $f(C) \subseteq Y$ is therefore a compact subspace of a Hausdorff space, so it is closed ({prf:ref}`topology:lemma-compact-subspaces-of-hausdorff-spaces-are-closed`).
:::

:::{prf:lemma} Condition for homeomorphism for quotient spaces
Suppose $f: X / \sim~\to Y$ is a bijection, $X$ is {prf:ref}`compact<topology:def-compact-space>`, $Y$ is {prf:ref}`Hausdorff<topology:def-hausdorff-space>` and $f \circ \pi$ is continuous.
Then $f$ is a homeomorphism.
:::

:::{dropdown} Proof: Condition for homeomorphism for quotient spaces
Note that the function $\pi: X \to X / \sim$ which maps each element of $X$ to its equivalence class in $X / \sim,$ is continuous.
Since $X$ is compact and $\pi$ is continuous, $\text{im} \pi$ is compact ({prf:ref}`topology:lem-image-of-compact-space-under-continuous-function-is-compact`).
Note that both $\pi$ and $\pi^{-1}$ are continuous.
Since $f \circ \pi$ is continuous, $f = f \circ \pi \circ \pi^{-1}$ is continuous.
Finally, since $f$ is a continuous bijection, $X$ is compact and $Y$ is Hausdorff, $f$ is a homeomorphism ({prf:ref}`topology:lem-sufficient-condition-for-homeomorphism`).
:::


## Sequential compactness

We now introduce another notion of compactness, namely sequential compactness.

:::{prf:definition} Sequential compactness
:label: topology:def-sequentially-compact
A topological space $X$ is sequentially compact if every sequence in $X$ has a convergent subsequence.
:::

Roughly speaking, sequential compacness captures the notion that a sequence cannot spread out arbitrarily in a space without having a subsequence that piles up around some point in the space.
In general, compactness and sequential compactness are different properties, however in a metric space they are equivalent.
To show this, we use the following intermediate lemma.

:::{prf:lemma} Equivalent condition for convergent subsequence in a metric space
:label: topology:lem-equivalent-condition-for-convergent-subsequence-in-a-metric-space
Let $(x_n)$ be a sequence in a {prf:ref}`metric space<topology:def-metric-space>` $(X, d)$ and $x \in X.$
Then $(x_n)$ has a subsequence converging to $x$ if and only if for every $\epsilon > 0$ we have $x_n \in B_\epsilon(x)$ for infinitely many $n \in \mathbb{N}.$
:::

:::{dropdown} Proof: Equivalent condition for convergent sequence in a metric space
Let $(x_n)$ be a sequence in a metric space $(X, d)$ and $x \in X.$

__Implies:__
Suppose $(x_n)$ has a subsequence $(x_{n_k})$ converging to $x.$
Let $\epsilon > 0.$
By the definition of convergence, there exists $N \in \mathbb{N}$ such that for all $m \geq N,$ we have $x_m \in B_\epsilon(x).$
Therefore, for all $n_k \geq m,$ of which there are infinitely many, we have $x_{n_k} \in B_\epsilon(x).$

__Is implied by:__
Suppose that for every $\epsilon > 0$ we have $x_n \in B_\epsilon(x)$ for infinitely many $n \in \mathbb{N}.$
We want to show $(x_n)$ has a subsequence converging to $x.$
By hypothesis, $x_n \in B_{1 / n}(x)$ for infinitely many $n.$
For $k = 1, 2, \dots,$ let $n_k$ be the smallest such $n$ with $n_k > n_{k - 1},$ where we define $n_0 = 0.$
Since $d(x_{n_k}, x) < \frac{1}{n},$ we have that $x_{n_k} \to x.$
:::
::::

We are now ready to show that compactness and sequential compactness are equivalent in metric spaces.

:::{prf:theorem} Compact metric space $\iff$ sequentially compact metric space
:label: topology:thm-compact-metric-space-iff-sequentially-compact-metric-space
A {prf:ref}`metric space<topology:def-metric-space>` $(X, d)$ is a {prf:ref}`compact<topology:def-compact-space>` if and only if it is {prf:ref}`sequentially compact<topology:def-sequentially-compact>`.
:::

:::{dropdown} Proof: Compact metric space $~\iff$ sequentially compact metric space
Let $(X, d)$ be a metric space.

__Implies:__
Suppose $(X, d)$ is compact.
Let $(x_n)$ be a sequence in $X$ and suppose that it does not have a convergent subsequence.
Then, for any $y \in X,$ there is no subsequence converging to $y.$
By {prf:ref}`topology:lem-equivalent-condition-for-convergent-subsequence-in-a-metric-space`, there exists $\epsilon_y > 0$ such that $x_n \in B_\epsilon_y(y)$ only finitely many times.
Let $U_y = B_\epsilon_y(y).$
Now, the set $\mathcal{V} = \{U_y: y \in X\}$ is an open cover of $X.$
Since $X$ is compact, there is a finite subcover $\{U_{y_1}, \dots, U_{y_m}\}.$
Then $x_n \cup_{i = 1}^m U_{y_i} = X$ only for finitely many $n,$ but this is a contradiction because $x_n \in X$ for all $n.$
Therefore $(x_n)$ has a convergent subsequence and $(X, d).$

__[Is implied by:](https://math.stackexchange.com/questions/164472/proving-that-sequentially-compact-spaces-are-compact)__
Suppose $(X, d)$ is sequentially compact.
Let $\mathcal{V}$ be an open cover of $X$ and suppose that there does not exist a finite open cover of $X$ from it.

First, we show that there exists $\delta > 0$ such that any open ball with radius less than $\delta$ is contained within some $V \in \mathcal{V}.$
This intermediate result is also known as [Lebesgue's number lemma](https://en.wikipedia.org/wiki/Lebesgue%27s_number_lemma).
Suppose this is not the case.
Then, for each $n \in \mathcal{N},$ there exists $x_n \in X$ such that $B_{1 / n}(x_n)$ is not contained in any $V \in \mathcal{V}.$
Since $X$ is sequentially compact, the sequence $(x_n)$ has a convergent subsequence $(x_{n_k})$ with a limit $x \in X.$
However, this leads to a contradiction.
First, $x$ cannot be in any $V \in \mathcal{V},$ because if $x$ is in some $V \in \mathcal{V},$ then because $V$ is open there exists $r > 0$ such that $B_r(x) \subseteq V.
Second, this means that all $x_{n_k}$ with $n_k$ sufficiently large such that $d(x_{n_k}, x) < r / 2$ and $n_k > 2 / r$ for all $n_k,$ would then satisfy $B_{1 / n_k}(x_{n_k}) \subseteq B_r(x) \subseteq V.$
This is a contradiction, so the intermediate result holds.

Now let $\delta > 0$ be such that any open ball with radius less than $\delta$ is contained within some $V \in \mathcal{V}.$
Pick $x_1 \in X.$
The ball $B_\delta(x_1)$ is contained in some $V_1 \in \mathcal{V},$ and since $V_1$ does not cover $X$ there exists $x_2 \in X \setminus B_\delta(x_1).$
We proceed recursively to obtain a sequence $(x_n)$ in this manner, which satisfies $x_n \in X \setminus \cup_{i = 1}^{n - 1} B_\delta(x_i).$
The sequence $(x_{n_k})$ has a convergent subsequence, and since it converges it is Cauchy.
However, this is a contradiction because no two elements $x_{n_k}$ can belong to the same open ball of radius $\delta.$
This contradicts the assumption that $\mathcal{V}$ has no finite subcover so $X$ is compact.
:::

## Completeness

We finish with a last section on completeness.
This concerns metric spaces, but relies on results on compactness we have shown in this section.
To define completeness, we first need to define Cauchy sequences.

:::{prf:definition} Cauchy sequence
:label: topology:def-cauchy-sequence
Let $(X, d)$ be a {prf:ref}`metric space<topology:def-metric-space>`.
A sequence $(x_n)$ in $X$ is Cauchy if for every $\epsilon > 0,$ there exists $N \in \mathbb{N}$ such that $d(x_n, x_m) < \epsilon$ for all $n, m \geq N.$
:::

A space is complete if every Cauchy sequence within it converges (to some limit in the space).
Intutively, a Cauchy sequence is one whose the terms are progressively closer to one another.
Completeness therefore means that all such sequences have a limit in the space.

:::{prf:definition} Complete metric space
:label: topology:def-complete-metric-space
A {prf:ref}`metric space<topology:def-metric-space>` $(X, d)$ is complete if every {prf:ref}`Cauchy sequence<topology:def-cauchy-sequence>` in it converges.
:::

For example $(0, 1)$ is a metric space that is not complete because the sequence $(a_n)$ where $a_n = n^{-1}$ is Cauchy but does not converge to a point in $(0, 1).$
By contrast, we will show that $[0, 1]$ is complete, and this is a consequence of the space being compact, as shown by the following result.

:::{prf:lemma} Compact metric spaces are complete
:label: topology:lem-compact-metric-spaces-are-complete
If the {prf:ref}`metric space<topology:def-metric-space>` $(X, d)$ is {prf:ref}`compact<topology:def-compact-space>`, it is also {prf:ref}`complete<topology:def-complete-metric-space>`.
:::

:::{dropdown} Proof: Compact metric spaces are complete
Suppose $(X, d)$ is a compact metric space.
Let $(x_n)$ be a Cauchy sequence in $X.$
From {prf:ref}`topology:thm-compact-metric-space-iff-sequentially-compact-metric-space`, it is sequentially compact.
Since the space is sequentially compact, $(x_n)$ has a convergent subsequence $(x_{n_k}),$ which converges to some $x \in X.$

Let $\epsilon > 0.$
Since $(x_n)$ is Cauchy, there exists $N \in \mathbb{N}$ such that for all $n, m \geq N,$ we have $d(x_n, x_m) < \epsilon / 2.$
Since $(x_{n_k})$ converges to some $x,$ there exists $M \in \mathbb{N}$ such that for all $n_k \geq M,$ we have $d(x_{n_k}, x) < \epsilon / 2.$
Let $l, n_k \geq \max\{N, M\}.$
Then

$$\begin{equation}
d(x_l, x) \leq d(x_l, x_{n_k}) + d(x_{n_k}, x) < \epsilon,
\end{equation}$$

so $x_l$ converges to $x,$ and $X$ is complete.
:::

The interval $[0, 1]$ is a compact set so it is complete ({prf:ref}`topology:lem-compact-metric-spaces-are-complete`.
We conclude with a satisfying result that we can show with the ideas developed in the course:
 $\mathbb{R}^n$ is complete.

:::{prf:lemma} $\mathbb{R}^n$ is complete
$\mathbb{R}^n$ with the standard topology is complete.
:::

:::{dropdown} Proof: $~\mathbb{R}^n~$ is complete
If $(x_n)$ is a Cauchy sequence in $\mathbb{R}^n,$ then $(x_n) \subseteq \overline{B}_r(0)$ for some $r \in \mathbb{R}.$
Since $\overline{B}_r(0)$ is a closed and bounded subset of a metric space, it is compact ({prf:ref}`topology:lem-closed-subsets-of-compact-spaces-are-compact`).
Since $(x_n)$ is a Cauchy sequence in a compact metric space, it converges ({prf:ref}`topology:lem-compact-metric-spaces-are-complete`).
Therefore $\mathbb{R}^n$ is complete.
:::
