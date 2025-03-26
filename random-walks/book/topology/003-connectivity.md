# Connectivity

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>


## Definition of connectivity

:::{prf:definition} Connected space
A topological space $X$ is disconnected if $X$ can be written as $A \cup B,$ where $A$ and $B$ are disjoint, non-empty open subsets of $X.$
We say $A$ and $B$ disconnect $X.$
A space is connected if it is not disconnected.
:::

:::{prf:definition} Connected subspace
Given a subset $A$ of a topological space $X,$ we say that $A$ is connected if $A$ is connected as a subspace of $X.$
:::

:::{prf:lemma} Equivalent condition for connectedness
A space $X$ is disconnected if and only if there exists a contunuous surjective $f: X \to \{0, 1\}$ with the discrete topology.
:::

:::{dropdown} Proof (Equivalent condition for connectedness)
Suppose $X$ is disconnected.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $X = A \cup B.$
Define $f: X \to \{0, 1\}$ by

$$f(x) = \begin{cases}
0 & \text{if } x \in A, \\
1 & \text{if } x \in B.
\end{cases}$$

Now, we note that $f$ is surjective because $A$ and $B$ are non-empty.
In addition, $f$ is continuous because $f^{-1}(\{0\}) = A$ and $f^{-1}(\{1\}) = B$ are open.
Thus, $f$ is continuous and surjective.

Conversely, suppose there exists a continuous surjective $f: X \to \{0, 1\}$ with the discrete topology.
Then the disjoint sets $f^{-1}(\{0\})$ and $f^{-1}(\{1\})$ are non-empty (because $f$ is surjective) and open (because $f$ is continuous).
Thus, $X$ is disconnected.
:::


:::{prf:theorem} Closed inverval is connected
The closed interval $[0, 1]$ with the standard topology is connected.
:::

:::{dropdown} Proof (Closed interval is connected)
Suppose $[0, 1]$ is disconnected.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $[0, 1] = A \cup B.$
Without loss of generality, we may assume that $1 \in B.$
Since $A$ is non-empty, $\alpha = \sup A$ exists and $\alpha \in [0, 1].$
There are two possibilities, either $\alpha \in A$ or $\alpha \in B.$

If $\alpha \in A,$ then $\alpha < 1$ and we immediately have a contradiction because, since $A$ is open, there exists an open interval $(\alpha - \varepsilon, \alpha + \varepsilon) \subseteq [0, 1]$ contained in $A$ for some $\varepsilon > 0,$ which means that $\alpha$ cannot be the supremum of $A.$
Therefore, $\alpha \in B.$
However, again, this raises a contradiction because, since $B$ is open, there exists an open interval $(\alpha - \varepsilon, \alpha + \varepsilon) \subseteq [0, 1]$ contained in $B$ for some $\varepsilon > 0,$ which means that $\alpha$ cannot be the supremum of $A.$
Thus, $[0, 1]$ is connected.
:::


:::{prf:lemma} Image of connected space under continuous map is connected
Let $f: X \to Y$ be a continuous map.
If $X$ is connected, then $f(X)$ is connected.
:::

:::{dropdown} Proof (Image of connected space under continuous map is connected)
Suppose $f(X)$ is disconnected.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $f(X) = A \cup B.$
Define $U = f^{-1}(A)$ and $V = f^{-1}(B).$
Then $U$ and $V$ are disjoint, non-empty open sets in $X,$ and $X = U \cup V.$
Therefore $X$ is disconnected, which is a contradiction.
Thus, $f(X)$ is connected.
:::


:::{prf:theorem} Intermediate value theorem
Suppose $f: X \to \mathbb{R}$ is continuous and $X$ is connected.
If $x_0, x_1 \in X$ such that $f(x_0) < 0 < f(x_1),$ then there exists $x \in X$ such that $f(x) = 0.$
:::

:::{dropdown} Proof (Intermediate value theorem)
Suppose there does not exist $x \in X$ such that $f(x) = 0.$
Then $f(X) \cap (-\infty, 0)$ and $f(X) \cap (0, \infty)$ are open, non-empty and disjoint sets whose union is $f(X).$
Therefore, $f(X)$ is disconnected, which is a contradiction.
Thus, there exists $x \in X$ such that $f(x) = 0.$
:::



## Path connectivity

:::{prf:definiton} Path
Let $X$ be a topological space, and $x_0, x_1 \in X.$
Then a path from $x_0$ to $x_1$ is a continuous map $\gamma: [0, 1] \to X$ such that $\gamma(0) = x_0$ and $\gamma(1) = x_1.$
:::

:::{prf:definition} Path connectivity
A topological space $X$ is path connected if for all points $x_0, x_1 \in X,$ there exists a path from $x_0$ to $x_1.$
:::

:::{prf:lemma} Path connected implies connected
If $X$ is path connected, then $X$ is connected.
:::

:::{dropdown} Proof (Path connected implies connected)
Let $X$ be path connected, and let $f: X \to \{0, 1\}$ be continuous.
We want to show that $f$ is constant.

Let $x_0, x_1 \in X.$
By path connectedness, there is a map $\gamma: [0, 1] \to X$ such that $\gamma(0) = x_0$ and $\gamma(1) = x_1.$
Then $f \circ \gamma: [0, 1] \to \{0, 1\}$ is continuous.
Since $[0, 1]$ is connected, $f \circ \gamma$ is constant and $f(\gamma(0)) = f(\gamma(1)),$ which means that $f(x_0) = f(x_1).$
Since $x_0$ and $x_1$ were arbitrary, $f$ is constant.
:::


:::{prf:lemma} Restrictions of homeomorphisms are homeomorphisms
Let $f: X \to Y$ be a homeomorphism, and let $A \subseteq X.$
Then $f|_A: A \to f(A)$ is a homeomorphism.
:::

:::{dropdown} Proof (Restrictions of homeomorphisms are homeomorphisms)
Since $f$ is a homeomorphism, it is a bijection, so $f|_A$ is a bijection.
If $U \subseteq f(A)$ is open, then $U = f(A) \cap U'$ for some open $U' \subseteq Y.$
Then $f^{-1}|_A(U) = f^{-1}(U) \cap A$ is open in $A$ because $f^{-1}$ is continuous.
Therefore $f|_A$ is continuous.

Similarly, we can show that $f|_A^{-1}$ is continuous.
If $V \subseteq A$ is open, then $V = A \cap V'$ for some open $V' \subseteq X.$
Then $(f|_A^{-1})^{-1}(V) = (f^{-1})^{-1}(V) = f(V)$ is open in $f(A)$ because $f$ is continuous.
Therefore $f|_A^{-1}$ is continuous.

Thus, $f|_A$ is a homeomorphism.
:::


## Components

:::{prf:lemma} Path connected equivalence relation
Let $X$ be a topological space.
For $x, x' \in X,$ define $x \sim x'$ if there exists a path from $x$ to $x'.$
Then $\sim$ is an equivalence relation.
:::

:::{dropdown} Proof (Path connected equivalence relation)
Let $x, x', x'' \in X.$

__Reflexivity:__
Then the constant map $\gamma: [0, 1] \to X$ defined by $\gamma(t) = x$ is a path from $x$ to $x,$ so $x \sim x.$

__Symmetry:__
If $\gamma: [0, 1] \to X$ is a path from $x$ to $x',$ then the map $\gamma': [0, 1] \to X$ defined by $\gamma'(t) = \gamma(1 - t)$ is a path from $x'$ to $x,$ so $x \sim x'.$

__Transitivity:__
If $\gamma: [0, 1] \to X$ is a path from $x$ to $x'$ and $\gamma': [0, 1] \to X$ is a path from $x'$ to $x'',$ then the map $\gamma'': [0, 1] \to X$ defined by

$$\gamma''(t) = \begin{cases}
\gamma(2t) & \text{if } 0 \leq t \leq \frac{1}{2}, \\
\gamma'(2t - 1) & \text{if } \frac{1}{2} \leq t \leq 1,
\end{cases}$$

is a path from $x$ to $x'',$ so $x \sim x''.$
:::
