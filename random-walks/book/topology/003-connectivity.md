# Connectivity

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>


This section introduces connectivity (or connectedness).
Connectivity is a topological property that describes whether a space, or subspace, consists of "one piece."
There are different variants of connectivity.
We introduce these variants here and discuss some of their properties.

## Definition of connectivity
The first definition of connectivity amounts to whether a space can be split into a disjoint union of two (non-empty) open sets.

:::{prf:definition} Connected space
:label: topology:def-connected
A {prf:ref}`topological space<topology:def-topological-space>` $X$ is disconnected if $X$ can be written as $A \cup B,$ where $A$ and $B$ are disjoint, non-empty open subsets of $X.$
We say $A$ and $B$ disconnect $X.$
A space is connected if it is not disconnected.
:::

:::{dropdown} Some additional intuition on connected spaces
We give some additional intuition on the conditions for connectivity.

__Disjoint sets:__
We require that the sets are disjoint because if not, then our notion of connectivity would not make sense:
if we did not require the sets are disjoint, then pairs of sets like $(-\infty, 1)$ and $(-1, \infty)$ would disconnect $\mathbb{R},$ which would not align with our expectation of what disconnected means.

__Non-empty sets:__
We also require that both sets are non-empty because we can always express a space as the disjoint union of itself and the empty set, both of which are empty.
Allowing this would trivialise the definition.

__Open sets:__
Finally, we require that the sets are both open.
If we did not require this, then $(-\infty, 0)$ and $[0, \infty)$ would disconnect $\mathbb{R}.$
Intuitively, this final requirement ensures that neither of the two sets contains a shared boundary:
if one set contained elements that are part of the boundary of the other, then this would not align with our expectation of what disconnected means.

__An additional observation:__
We also note the following point about disconnected sets:
if $A, B \subseteq X$ disconnect $X,$ then both $A, B$ are open and closed in $X.$
To see this, note that $A \cap B = \emptyset$ and $A \cup B = X.$
Therefore, $X \setminus A = B$ so the complement of $A$ in $X$ is open, which means $A$ is closed in $X.$
A similar argument shows $B$ is closed in $X$ as well.
In this sense, we can consider $A$ and $B$ as disconnected or separate.
for example, any sequence that converges in $A$ (or $B$) does not have its limit in $B$ (or $A$).
We can also go the other way and observe that for any connected space $X,$ the only subspace of it that is both open and closed is the space $X$ itself:
if $X$ contains a non-empty subset $A$ that is both open and closed, then $B = X \subset A$ is an open subset of $X$ that is disjoint from $A,$ and if $B$ were non-empty then $A$ and $B$ would disconnect $X,$ so $B = \emptyset$ and $A = X.$
With this final bit of intuition, whenever a space can be disconnected into $A$ and $B,$ we can regard $A$ and $B$ as separate sets in $X,$ whose union does not alter topological properties such as convergence of sequences when we consider the two sets together.
:::

:::{prf:definition} Connected subspace
Given a subset $A$ of a {prf:ref}`topological space<topology:def-topological-space>` $X,$ we say that $A$ is connected if $A$ is {prf:ref}`connected<topology:def-connected>` as a subspace of $X.$
:::

:::{prf:lemma} Equivalent condition for connectedness
A space $X$ is {prf:ref}`disconnected<topology:def-connected>` if and only if there exists a contunuous surjective $f: X \to \{0, 1\}$ with the discrete topology.
:::

:::{dropdown} Proof: Equivalent condition for connectedness
Suppose $X$ is {prf:ref}`disconnected<topology:def-connected>`.
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
The closed interval $[0, 1]$ with the standard topology is {prf:ref}`connected<topology:def-connected>`.
:::

:::{dropdown} Proof: Closed interval is connected
Suppose $[0, 1]$ is {prf:ref}`disconnected<topology:def-connected>`.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $[0, 1] = A \cup B.$
Without loss of generality, we may assume that $1 \in B.$
Since $A$ is non-empty, $\alpha = \sup A$ exists and $\alpha \in [0, 1].$
There are two possibilities, either $\alpha \in T$ or $\alpha \in B.$

If $\alpha \in T,$ then $\alpha < 1$ and we immediately have a contradiction because, since $A$ is open, there exists an open interval $(\alpha - \varepsilon, \alpha + \varepsilon) \subseteq [0, 1]$ contained in $A$ for some $\varepsilon > 0,$ which means that $\alpha$ cannot be the supremum of $A.$
Therefore, $\alpha \in B.$
However, again, this raises a contradiction because, since $B$ is open, there exists an open interval $(\alpha - \varepsilon, \alpha + \varepsilon) \subseteq [0, 1]$ contained in $B$ for some $\varepsilon > 0,$ which means that $\alpha$ cannot be the supremum of $A.$
Thus, $[0, 1]$ is {prf:ref}`connected<topology:def-connected>`.
:::


:::{prf:lemma} Image of connected space under continuous map is connected
Let $f: X \to Y$ be a continuous map.
If $X$ is {prf:ref}`connected<topology:def-connected>`, then $f(X)$ is too.
:::

:::{dropdown} Proof: Image of connected space under continuous map is connected
Suppose $f(X)$ is {prf:ref}`disconnected<topology:def-connected>`.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $f(X) = A \cup B.$
Define $U = f^{-1}(A)$ and $V = f^{-1}(B).$
Then $U$ and $V$ are disjoint, non-empty open sets in $X,$ and $X = U \cup V.$
Therefore $X$ is disconnected, which is a contradiction.
Thus, $f(X)$ is {prf:ref}`connected<topology:def-connected>`.
:::


:::{prf:theorem} Intermediate value theorem
Suppose $f: X \to \mathbb{R}$ is continuous and $X$ is connected.
If $x_0, x_1 \in X$ such that $f(x_0) < 0 < f(x_1),$ then there exists $x \in X$ such that $f(x) = 0.$
:::

:::{dropdown} Proof: Intermediate value theorem
Suppose there does not exist $x \in X$ such that $f(x) = 0.$
Then $f(X) \cap (-\infty, 0)$ and $f(X) \cap (0, \infty)$ are open, non-empty and disjoint sets whose union is $f(X).$
Therefore, $f(X)$ is {prf:ref}`disconnected<topology:def-connected>`, which is a contradiction.
Thus, there exists $x \in X$ such that $f(x) = 0.$
:::



## Path connectivity

:::{prf:definiton} Path
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>`, and $x_0, x_1 \in X.$
Then a path from $x_0$ to $x_1$ is a continuous map $\gamma: [0, 1] \to X$ such that $\gamma(0) = x_0$ and $\gamma(1) = x_1.$
:::

:::{prf:definition} Path connectivity
:label: topology:def-path-connected
A {prf:ref}`topological space<topology:def-topological-space>` $X$ is {prf:ref}`path connected<topology:def-path-connected>` if for all points $x_0, x_1 \in X,$ there exists a path from $x_0$ to $x_1.$
:::

:::{prf:lemma} Path connected implies connected
If $X$ is {prf:ref}`path connected<topology:def-path-connected>`, then $X$ is {prf:ref}`connected<topology:def-connected>`.
:::

:::{dropdown} Proof: Path connected implies connected
Let $X$ be {prf:ref}`path connected<topology:def-path-connected>`, and let $f: X \to \{0, 1\}$ be continuous.
We want to show that $f$ is constant.

Let $x_0, x_1 \in X.$
By path connectedness, there is a map $\gamma: [0, 1] \to X$ such that $\gamma(0) = x_0$ and $\gamma(1) = x_1.$
Then $f \circ \gamma: [0, 1] \to \{0, 1\}$ is continuous.
Since $[0, 1]$ is {prf:ref}`connected<topology:def-connected>`, $f \circ \gamma$ is constant and $f(\gamma(0)) = f(\gamma(1)),$ which means that $f(x_0) = f(x_1).$
Since $x_0$ and $x_1$ were arbitrary, $f$ is constant.
:::


:::{prf:lemma} Restrictions of homeomorphisms are homeomorphisms
Let $f: X \to Y$ be a homeomorphism, and let $A \subseteq X.$
Then $f|_A: A \to f(A)$ is a homeomorphism.
:::

:::{dropdown} Proof: Restrictions of homeomorphisms are homeomorphisms
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

We now introduce path components and connected components.
These are equivalence classes of points which are path connected or connected, repspectively.

### Path components

:::{prf:lemma} Path connected equivalence relation
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>`.
For $x, x' \in X,$ define $x \sim x'$ if there exists a path from $x$ to $x'.$
Then $\sim$ is an equivalence relation.
:::

:::{dropdown} Proof: Path connected equivalence relation
Let $x, x', x'' \in X.$
We show that $\sim$ satisfies the properties of an equivalence relation.

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


:::{prf:definition} Path component
Equivalence classes of the path connectivity equivalence relation are called path components.
:::


### Connected components

:::{prf:lemma} Union of intersecting connected sets is connected
:label: topology:lem-union-of-increasing-connected-sets-is-connected
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>`.
Suppose $Y_\alpha \subseteq X$ is {prf:ref}`connected<topology:def-connected>` for all $\alpha \in T,$ and $\cap_{\alpha \in T} Y_\alpha \neq \emptyset.$
Then $\cup_{\alpha \in T} Y_\alpha$ is {prf:ref}`connected<topology:def-connected>`.
:::

:::{dropdown} Proof: Union of intersecting connected sets is connected
Suppose $Y = \cup{\alpha \in T} Y_\alpha$ is {prf:ref}`disconnected<topology:def-connected>`.
Then there exist disjoint, non-empty open sets $A$ and $B$ that are subsets of $Y$ such that $A \cup B = Y.$
Since $A$ and $B$ are open in $Y,$ there exist open $A', B' \subseteq X$ such that $A = A' \cap Y$ and $B = B' \cap Y.$
Define

$$\begin{equation}
A_\alpha = A \cap Y_\alpha = A' \cap Y_\alpha,~~ B_\alpha = B \cap Y_\alpha = B' \cap Y_\alpha.
\end{equation}$$

Note that $A_\alpha$ and $B_\alpha$ are open in $Y_\alpha.$
Note also that $A_\alpha \cup B_\alpha = Y_\alpha$ and $A_\alpha \cap B_\alpha = \emptyset.$
Since $Y_\alpha$ is {prf:ref}`connected<topology:def-connected>`, we must have either $A_\alpha = \emptyset$ or $B_\alpha = \emptyset$ because otherwise $A_\alpha$ and $B_\alpha$ would disconnect $Y_\alpha.$

Now, by assumption, $\cap_{\alpha \in T} Y_\alpha$ is non-empty, so pick $y \in \cap_{\alpha \in T}.$
Then $y \in A$ or $y \in B,$ and without loss of generality we can pick $y \in A.$
Since $y \in A,$ we have $y \in A_\alpha$ for all $\alpha \in T.$
This implies that $B_\alpha = \emptyset$ for all $\alpha \in T,$ and in turn $B = \emptyset.$
This is a contradiction because we assumed $A$ and $B$ disconnect $Y$ and therefore cannot be empty.
Therefore $Y$ is {prf:ref}`connected<topology:def-connected>`.
:::


With this result in place, we are ready to define connected components.

:::{prf:definition} Connected component
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>` and $x \in X.$
Define

$$\begin{equation}
\mathcal{C}(x) = \{A \subseteq X : x \in A \text{ and } A \text{ is connected.}\}
\end{equation}$$

Then $C(x) = \cup_{A \in \mathcal{C}(x)} A$ is the connected component of $x.$
:::

In other words, the connected component of $x \in X$ is the largest {prf:ref}`connected<topology:def-connected>` subset of $X$ containing $x,$ which can be shown as follows.

:::{prf:remark} Connected component of $x \in X$ is the largest connected subspace containing $x$
First, note that $\{x\} \in \mathcal{C}(x),$ so $x \in \mathcal{C}(x).$
Second, note that $C(x)$ is {prf:ref}`connected<topology:def-connected>` because $x \in \cap_{A \in \mathcal{C}(x)} A$ so the set $\cap_{A \in \mathcal{C}(x)} A$ is connected, and by our previous {prf:ref}`lemma<topology:lem-union-of-increasing-connected-sets-is-connected>`, $C(x)$ must also be connected.
Therefore $C(x)$ is a connected subset of $X$ that contains $x.$
Finally, by the defintion of $C(x),$ we see that if another connected subspace $C'$ contains $x,$ then it must be a subset of $C(x).$
:::


Similarly to path components, connected components also define an equivalence relation and equivalence classes.


:::{prf:lemma} Elements in a connected component have the same connected component
:label: topology:lem-elements-in-a-connected-component-have-the-same-connected-component
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>` and $x, y \in X.$
If $y \in C(x),$ then $C(x) = C(y).$
:::

:::{dropdown} Proof: All elements in a connected component have the same connected component
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>` and $x, y \in X.$
If $y \in C(x),$ then $C(x)$ is a {prf:ref}`connected<topology:def-connected>` subspace containing $y$ and must therefore be a subset of $C(y)$ so $C(x) \subseteq C(y).$
Because of this, we have $x \in C(y)$ as well, and by the same argument it follows that $C(y) \subseteq C(x).$
We conclude that $C(x) = C(y).$
:::

A corollary of the above is that:
the binary relation that says two elements are equivalent if they share the same connected components is an equivalence relation.

:::{prf:lemma} Connected equivalence relation
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>`.
For $x, x' \in X,$ define $x \sim x'$ if $C(x) = C(x').$
Then $\sim$ is an equivalence relation.
:::

:::{dropdown} Proof: Connect equivalence relation
Let $X$ be a {prf:ref}`topological space<topology:def-topological-space>`.
For $x, x' \in X,$ define $x \sim x'$ if $C(x) = C(x').$
We will prove that this binary relation satisfies the three requirements of equivalence relations.
In the following, let $x, x', x'' \in X.$

__Reflexivity:__
Trivially, $C(x) = C(x)$ so $x \sim x'.$

__Symmetry:__
Suppose $x \sim x'.$
This means that $C(x) = C(x'),$ so $x' \sim x$ holds as well.

__Transitivity:__
Suppose $x \sim x'$ and $x' \sim x''.$
These conditions mean that $C(x) = C(x')$ and $C(x') = C(x'')$ so $C(x) = C(x'')$ and $x \sim x''.
:::

:::{prf:lemma} Open connected subspaces of $\mathbb{R}^n$ are path connected
If $U \subseteq \mathbb{R}^n$ with the standard topology is open and {prf:ref}`connected<topology:def-connected>`, then it is {prf:ref}`path connected<topology:def-path-connected>`.
:::

:::{dropdown} Proof: open connected subspaces of $~\mathbb{R}^n$ are path connected
Suppose $U \subseteq \mathbb{R}^n$ with the standard topology is open and {prf:ref}`connected<topology:def-connected>`.
Let $A$ be a path component of $U.$
We will show that $A = U,$ by showing that $U \setminus A$ must be empty.
In turn, we will argue this by showing that both $A$ and $U \setminus A$ must be open, and since they are disjoint and $A$ is non-empty, then $U \setminus A$ must be empty:
otherwise $A$ and $U \setminus A$ would disconnect $U.$

__Showing $A$ is open:__
Let $a \in A.$
Since $U$ is open, there exists $\epsilon > 0$ such that $B_\epsilon(a) \subseteq U.$
Since $B_\epsilon(a) \simeq \text{Int}(D^n)$ is {prf:ref}`path connected<topology:def-path-connected>`, and $A$ is a path component containing $a,$ we have that $B_\epsilon(a) \subseteq A.$
Therefore $A$ is an open subset of $U.$

__Showing $U \setminus A$ is open:__
Now suppose that $b \in U \setminus A.$
Then since $U$ is open, there exists $\epsilon > 0$ such that $B_\epsilon(b) \subseteq U.$
Now, we must have $B_\epsilon(b) \cap A = \emptyset$ because if $B_\epsilon(b)$ and $A$ intersect, and since $B_\epsilon(b)  \simeq \text{Int}(D^n)$ is path connected, it would follow that $B_\epsilon(b)$ and $A$ are path connected, so $b \in A$ which is a contradiction.
Therefore $B_\epsilon(b) \cap A = \emptyset,$ which means $B_\epsilon(b) \subseteq U \setminus A,$ which implies that $U \setminus A$ is open.

We conclude that since $A$ and $U \setminus A$ are disjoint open subsets of $U,$ and $U$ is connected, we must have $U \setminus A = \emptyset.$
So $U = A$ and $U$ is path connected.
:::
