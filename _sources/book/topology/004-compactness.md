# Compactness

:::{prf:definition} Compact space
A topological space $X$ is compact if every open cover $\mathcal{V}$ of $X$ has a finite subcover $\mathcal{V}' = \{V_1, \dots, V_n\} \subseteq \mathcal{V}.$
:::

:::{prf:theorem} Closed interval is compact
The closed interval $[0, 1] \subseteq \mathbb{R}$ with the standard topology is compact.
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

:::{prf:lemma} Closed subsets of compact spaces are compact
If $X$ is compact and $C$ is a closed subset of $X,$ then $C$ is also compact.
:::

:::{dropdown} Proof: Closed subsets of compact spaces are compact
Suppose $X$ is compact and $C$ is a closed subset of $X.$
Let $\mathcal{V}$ be an open cover of $C.$
Then since each $V \in \mathcal{V}$ is open in $C,$ there exists open $V'$ in $X$ such that $V' \cap C = V.$
Then, the set $\mathcal{W}$ containing all such $V',$ i.e. all open $V'$ such that $V' \cap C = V$ for some $V \in \mathcal{V},$ together with the open set $X \setminus C,$ is an open cover of $X.$
Since $X$ is compact, it has a finite subcover from $\mathcal{W},$ and since $C \subseteq X,$ this also gives a finite subcover for $C,$ which is therefore compact.
:::


:::{prf:lemma} Compact subspaces of Hausdorff spaces are closed
:label: topology:lemma-compact-subspaces-of-hausdorff-spaces-are-closed
Let $X$ be a Hausdorff space.
If $C \subseteq X$ is compact, then $C$ is closed in $X.$
:::

:::{dropdown} Proof: Compact subspaces of Hausdorff spaces are closed
Let $X$ be a Hausdorff space.
Suppose $C \subseteq X$ is compact.
We will show that $X \setminus C$ is open.

Suppose $x \in X \setminus C.$
We will show there exists an open $U \subseteq X \setminus C$ that contains $x.$
Since $X$ is Hausdorff, for each $y \in C$ there exists an open $W_{xy}$ containing $y$ and an open $U_{xy}$ containing $x$ such that $W_{xy} \cap $U_{xy} = \emptyset.$
Then, the collection $\{W_{xy} \subseteq X: y \in C\}$ is an open cover of $C,$ and since $C$ is compact, it has a finite subcover of the form $\{W_{x_1y}, \dots, W_{x_Ny}\}.$
Then the set $\cap_{n = 1}^N U_{x_ny}$ is open because it is a finite interesection of open sets, and it does not intersect $C,$ so it is contained in $X \setminus C.$
Therefore $X \setminus C$ is open and $C$ is closed.
:::


:::{prf:definition} Bounded metric space
A metric space $(X, d)$ is bounded if there exists $M \in \mathbb{R}$ such that $d(x, y) \leq M$ for all $x, y \in X.$
:::

Note that being bounded is not a topological property.
For example $(0, 1) \simeq \mathbb{R}$ are homeomorphic but $(0, 1)$ is bounded while $\mathbb{R}$ is not.

:::{prf:lemma} Compact metric spaces are bounded
:label: topology:lem-compact-metric-spaces-are-bounded
A compact metric space $(X, d)$ is bounded.
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

:::{prf:theorem} Heine-Borel
A subset $C \subseteq \mathbb{R}$ with the standard topology is compact if and only if it is closed and bounded.
:::

:::{dropdown} Proof: Heine-Borel
Suppose $C \subseteq \mathbb{R}$ with the standard topology.

__Implies:__
Suppose $C$ is closed and bounded.
Since $C$ is bounded, it is contained in a closed set $[-M, M]$ for some $M \in \mathbb{R}.$
Therefore $C$ is a closed subset of a compact space $[-M, M] \simeq [0, 1],$ therefore it is compact.

__Implied by:__
Suppose $C$ is compact.
Since $\mathbb{R}$ is a metric space, it is also Hausdorff, and since $C$ is compact it follows that it is closed.
In addition, since $C$ is a compact metric space, it is also bounded.
:::


:::{prf:lemma} Compact subsets of $\mathbb{R}$ have finite upper bounds
If $A \subseteq \mathbb{R}$ with the standard topology is compact, there exists $\alpha \in A$ such that $\alpha \geq a$ for all $a \in A.$
:::

:::{dropdown} Proof: Compact subsets of $\mathbb{R}$ have finite upper bounds
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
Let $X$ and $Y$ be topological spaces.
If $f: X \to Y$ is continuous and $X$ is compact, then $\text{im}f \subseteq$ is also compact.
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
If $X$ is a compact {prf:ref}`topological space<topology:def-topological-space>` and $f: X \to \mathbb{R}$ is continuous with the standard topology, then $x \in X$ such that $f(x) \geq f(x')$ for all $x' \in X.$
:::

:::{dropdown} Proof: Maximum value theorem
Suppose $X$ is a {prf:ref}`topological space<topology:def-topological-space>` and let $f: X \to \mathbb{R}$ be continuous.
The image of a compact set under a continuous function is compact ({prf:ref}`topology:lem-image-of-compact-space-under-continuous-function-is-compact`), so $\text{im}f$ is compact.
Since $\mathbb{R}$ is a metric space, so $\text{im}f$ is also a metric space and is therefore Hausdorff.
Because $\text{im}f$ is a compact metric space, it must be bounded ({prf:ref}`topology:lem-compact-metric-spaces-are-bounded`).
Therefore $\text{im} f$ contains its supremum, i.e. $f(x) = \sup \text{im} f$ for some $x \in X.$
By definition of the supremum, $f(x) \geq f(x')$ for all $x' \in X.$
:::


:::{prf:lemma} Maximum value theorem for $[0, 1]$
If $f: [0, 1] \to \mathbb{R}$ is continuous with the standard topology on both $[0, 1]$ and $\mathbb{R},$ then there exists $x \in X$ such that $f(x) \geq f(x')$ for all $x' \in X.$
:::

:::{dropdown} Maximum value theorem for $~[0, 1]$
This follows since $[0, 1],$ with the standard topology, is compact ({prf:ref}`topology:maximum-value-theorem`).
:::
