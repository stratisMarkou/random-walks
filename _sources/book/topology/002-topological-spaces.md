# Topological Spaces

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

In the previous chapter we saw that in a metric space, continuity of functions is only indirectly determined by the metric itself.
Instead, the structure that determines continuity {prf:ref}`is the collection open sets under the metric<topology:theorem-characterisation-of-continuity>`.
This motivates the definition of a topological space, which abstracts the notion of open sets from metric spaces.

## Topologies
First, we define topological spaces.
These are sets equipped with a topology, a collection of subsets which we _define_ to be open.
Unlike in metric spaces, where we first defined open balls and then used them to define open sets, here we define open sets directly, and require they satisfy certain properties.

:::{prf:definition} Topological space
:label: topology:def-topological-space
A topological space is a set $X,$ called the space, together with a collection $\mathcal{U} \subseteq \mathcal{P}(X)$ of subsets of $X,$ called the topology on $X,$ such that

1. $\emptyset, X \in \mathcal{U},$
2. If ${U_i}_{i \in I} \subseteq \mathcal{U},$ then $\bigcup_{i \in I} U_i \in \mathcal{U},$
3. If $U_1, \dots, U_n \in \mathcal{U},$ then $\bigcap_{i=1}^n U_i \in \mathcal{U}.$

The elements of $X$ are called points, and the elements of $\mathcal{U}$ are called open sets.
:::


When working with specific spaces, they will often be already be equipped with a metric.
We refer to the topology associated with a given metric as the induced topology.

:::{prf:definition} Induced topology
:label: topology:def-induced-topology
Let $(X, d)$ be a {prf:ref}`metric space<topology:def-metric-space>`.
Then, the topology induced by $d$ is the set of all open sets in $X$ with respect to the metric $d.$
:::


We now also re-define continuity in terms of open sets.

:::{prf:definition} Continuous function
:label: topology:def-continuous-function-topology
Let $f: X \to Y$ be a function between topological spaces.
Then, $f$ is continuous if for every open set $U \subseteq Y,$ the pre-image $f^{-1}(U)$ is an open set in $X.$
:::


:::{prf:lemma} Composition preserves continuity
:label: topology:lemma-composition-preserves-continuity
If $f: X \to Y$ and $g: Y \to Z$ are {prf:ref}`continuous functions<topology:def-continuous-function-topology>` between {prf:ref}`topological spaces<topology:def-topological-space>`, then the composition $g \circ f: X \to Z$ is continuous.
:::


In topology, we are interested in studying the properties of spaces that are preserved under continuous deformations.
Therefore, from a topology perspective, two spaces are considered essentially the same up to a continuous bijection.
This is captured by the notion of homeomorphism.

:::{prf:definition} Homeomorphism
:label: topology:def-homeomorphism
A function $f: X \to Y$ between {prf:ref}`topological spaces<topology:def-topological-space>` is a {prf:ref}`homeomorphism<topology:def-homeomorphism>` if it is bijective, {prf:ref}`continuous<topology:def-continuous-function-topology>`, and its inverse $f^{-1}$ is also continuous.
Equivalently, $f$ is a homeomorphism if $f$ is a bijection and $U \subseteq X$ is {prf:ref}`open<topology:def-topological-space>` if and only if $f(U) \subseteq Y$ is open.
We say two spaces are homeomorphic if there exists a homeomorphism between them.
:::

:::{prf:lemma} Homeomorphism is an equivalence relation
:label: topology:lemma-homeomorphism-equivalence-relation
{prf:ref}`Homeomorphism<topology:def-homeomorphism>` is an equivalence relation between topological spaces.
:::

:::{dropdown} Proof: Homeomorphism is an equivalence relation
__Reflexivity:__
The identity map $I_X: X \to X$ is a homeomorphism, because it is bijective, continuous, and its inverse is itself.
Therefore $X \equiv X.$

__Symmetry:__
If $f: X \to Y$ is a homeomorphism, then $f^{-1}: Y \to X$ is also a homeomorphism.
Therefore $X \equiv Y$ implies $Y \equiv X.$

__Transitivity:__
If $f: X \to Y$ and $g: Y \to Z$ are homeomorphisms, then $g \circ f: X \to Z$ is a homeomorphism.
Therefore $X \equiv Y$ and $Y \equiv Z$ implies $X \equiv Z.$
:::

In general, the approach for showing that two spaces are homeomorphic is to find a homeomorphism between them.
However, showing that two spaces are _not_ homeomorphic is more difficult.
In particular, there is no simple recipe for showing that two spaces are not homeomorphic.
Instead, we resort to certain topological properties that are preserved under homeomorphisms.
Whenever two spaces have different such properties, we can conclude that they are not homeomorphic.
Two such properties are connectedness and compactness.
In the remainder of this chapter we give definitions and results building up to these properties.


## Sequences

We now turn to re-defining concepts from metric spaces in terms of topological spaces, starting with sequences.
First we re-define the following shorthand for open sets.

:::{prf:definition} Open neighbourhood
:label: topology:def-open-neighbourhood-topology
An open neighbourhood of a point $x \in X$ in a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U})$ is an open set $U \in \mathcal{U}$ such that $x \in U.$
:::


In topological spaces, convergent sequences are defined directly in terms of open neighbourhoods, rather than using open balls.

:::{prf:definition} Convergent sequence
:label: topology:def-convergent-sequence-topology
A sequence $x_n \to x$ if for every {prf:ref}`open neighbourhood<topology:def-open-neighbourhood-topology>` $U$ of $x,$ there exists $N \in \mathbb{N}$ such that $x_n \in U$ for all $n > N.$
:::


We now turn to uniqueness of limits.
In general, in a topological space limits need not be unique.
For example, given a set $X$ with the coarse topology $\mathcal{U} = \{\emptyset, X\},$ every sequence converges to every point.
However, further assumptions on the topology can result into unique limits.

:::{prf:definition} Hausdorff space
:label: topology:def-hausdorff-space
A {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U})$ is Hausdorff if for every pair of distinct points $x_1, x_2 \in X,$ there exist {prf:ref}`open neighbourhoods<topology:def-open-neighbourhood-topology>` $U_1, U_2$ of $x_1, x_2$ respectively such that $U_1 \cap U_2 = \emptyset.$
:::

:::{margin}
Earlier, we proved that {prf:ref}`limits in metric spaces are unique<topology:lemma-limits-in-metric-spaces-are-unique>`.
The property we used in that proof was that, in a {prf:ref}`metric space <topology:def-metric-space>`, open balls centered around distinct points are disjoint if their radii are small enough.
This was the Hausdorff property in disguise.
Metric spaces are always {prf:ref}`Hausdorff<topology:def-hausdorff-space>`, and therefore have unique limits.
:::

:::{prf:lemma} Limits are unique in Hausdorff spaces
:label: topology:lemma-limits-unique-hausdorff
If $X$ is {prf:ref}`Hausdorff<topology:def-hausdorff-space>` and $(x_n)$ is a sequence in $X$ such that $x_n \to x$ and $x_n \to x',$ then $x = x'.$
:::

:::{dropdown} Proof: Limits are unique in Hausdorff spaces
Let $(x_n)$ be a sequence in $X$ such that $x_n \to x$ and $x_n \to x'.$
Suppose $x \neq x'.$
Since $X$ is Hausdorff, there exist open neighbourhoods $U, U'$ of $x, x'$ respectively such that $U \cap U' = \emptyset.$
Since $x_n \to x,$ there exists $N \in \mathbb{N}$ such that $x_n \in U$ for all $n > N.$
Similarly, since $x_n \to x',$ there exists $N' \in \mathbb{N}$ such that $x_n \in U'$ for all $n > N'.$
Then, for all $n > \max(N, N'),$ we have $x_n \in U \cap U' = \emptyset,$ which is a contradiction.
Therefore, $x = x'.$
:::


We now revisit closed sets and limit points, this time in topological spaces.

:::{prf:definition} Closed set
:label: topology:def-closed-set-topology
A set $C \subseteq X$ in a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U})$ is closed if its complement $X \setminus C$ is open.
:::


We now prove some properties of closed sets.

:::{prf:lemma} Properties of closed sets
:label: topology:lemma-properties-of-closed-sets
Let $(X, \mathcal{U})$ be a {prf:ref}`topological space<topology:def-topological-space>`.
Then,

1. $\emptyset$ and $X$ are {prf:ref}`closed<topology:def-closed-set-topology>`,
2. If $C_1, \dots, C_n$ are closed, then $\bigcup_{i=1}^n C_i$ is closed,
3. If $\{C_i\}_{i \in I}$ are closed, then $\bigcap_{i \in I} C_i$ is closed.
:::

:::{dropdown} Proof: Properties of closed sets
__Property 1:__
Since $\emptyset$ is open, its complement $X$ is closed.
Similarly, since $X$ is open, its complement $\emptyset$ is closed.

__Property 2:__
If $C_1, \dots, C_n$ are closed, then their complements $X \setminus C_1, \dots, X \setminus C_n$ are open.
Therefore, $\bigcup_{i = 1}^n (X \setminus C_i) = X \setminus \bigcap_{i = 1}^n C_i$ is open, so $\bigcap_{i = 1}^n C_i$ is closed.

__Property 3:__
If ${C_i}_{i \in I}$ are closed, then their complements ${X \setminus C_i}_{i \in I}$ are open.
Therefore, $\bigcap_{i \in I} (X \setminus C_i) = X \setminus \bigcup_{i \in I} C_i$ is open, so $\bigcup_{i \in I} C_i$ is closed.
:::

Note the similarity of the properties above to the defining properties of {prf:ref}`open sets<topology:def-topological-space>`.
In fact, we could have defined topologies in terms of closed sets rather than open sets.


:::{prf:lemma} Singleton set in Hausdorff space is closed
:label: topology:lemma-singleton-set-closed-hausdorff
If $X$ is {prf:ref}`Hausdorff<topology:def-hausdorff-space>` and $x \in X,$ then $\{x\}$ is closed.
:::

:::{dropdown} Proof: Singleton set in Hausdorff space is closed
__Proof 1:__
Let $X$ be Hausdorff and $x \in X.$
We want to show that $\{x\}$ is closed, which we can do by showing that $\{x\}$ is an intersection of closed sets.
Let $x' \in X \setminus \{x\}.$
Since $X$ is Hausdorff, there exist open neighbourhoods $U_x, U_{x'}$ of $x, x'$ respectively such that $U_x \cap U_{x'} = \emptyset.$
Then, $X \setminus U_{x'}$ is closed, and $\{x\} = X \setminus U_{x'}.$
Finally, we have $\{x\} = \bigcap_{x' \in X \setminus \{x\}} (X \setminus U_{x'}),$ so $\{x\}$ is closed.


__Proof 2:__
Let $X$ be Hausdorff and $x \in X.$
We want to show that $X \setminus \{x\}$ is open.
Let $x' \in X \setminus \{x\}.$
Then $x \neq x'.$
Since $X$ is Hausdorff and $x \neq x',$ there exist open neighbourhoods $U, U'$ of $x, x'$ respectively such that $U \cap U' = \emptyset.$
Then, $U' \subseteq X \setminus \{x\},$ so $X \setminus \{x\}$ is open.
:::


:::{prf:definition} Closure
:label: topology:def-closure
Let $A \subseteq X$ be a subset of a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U})$.
Define

$$\mathcal{C}_A = \{C \subseteq X \mid A \subseteq C \text{ and } C \text{ is closed}\}.$$

Then, the closure of $A,$ written $\overline{A},$ is defned as

$$\overline{A} = \bigcap_{C \in \mathcal{C}_A} C.$$
:::


:::{prf:lemma} Closure of a set is the smallest closed set containing it
:label: topology:lemma-closure-closed-set
Given a set $A \subseteq X$ in a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U}),$ its closure $\overline{A}$ is the smallest closed set containing $A.$
:::

:::{dropdown} Proof: Closure of a set is the smallest closed set containing it
Let $A \subseteq X$ be a subset of a topological space $(X, \mathcal{U}).$
We want to show that $\overline{A}$ is the smallest closed set containing $A.$
First, $\overline{A}$ is an intersection of closed sets containing $A,$ so it contains $A$ and {prf:ref}`it is closed<topology:lemma-properties-of-closed-sets>`.
Let $C$ be a closed set containing $A.$
Then $C \in \mathcal{C}_A,$ so $\overline{A} \subseteq C.$
We conclude, $\overline{A}$ is the smallest closed set containing $A.$
:::


:::{margin}
The standard definition of limit point given here requires that the open neighbourhood includes a point different from the limit point itself.
This is the standard definition of limit points, see e.g. {cite}`munkrestopology`.
Dexter Chua's [notes](https://dec41.user.srcf.net/notes/IB_E/metric_and_topological_spaces.pdf#page=19.72) for the Cambridge course on Metric and Topological Spaces, which I have been following, use a different definition of limit points, namely: a point in $X$ is a limit point of $A,$ if there exists a sequence $(x_n)$ in $A$ such that $x_n \to x.$
Under this definition, all elements of $A$ are limit points of $A,$ which does not match the standard defintion.
I have chosen to follow the standard definition, ammending the results provided in the notes as needed.
:::
:::{prf:definition} Limit point
:label: topology:def-limit-point
Let $A \subseteq X$ be a subset of a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U}).$
Then $x \in X$ is a limit point of $A$ if every open neighbourhood of $x$ contains a point of $A$ different from $x.$
:::


:::{prf:lemma} Set is closed if and only if it contains its limit points
:label: topology:lemma-closed-set-iff-it-contains-its-limit-points
Given a set $A \subseteq X$ in a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U}),$ the set $A$ is {prf:ref}`closed<topology:def-closed-set-topology>` if and only if $A$ contains all its {prf:ref}`limit points<topology:def-limit-point>`.
:::

:::{dropdown} Proof: Set is closed if and only if it contains its limit points
First, suppose $A$ is closed.
We will show it contains all its limit points.
Let $x$ be a limit point of $A.$
Suppose $x \notin A.$
Since $A$ is closed, $X \setminus A$ is open, so there exists an open neighbourhood $U$ of $x$ such that $U \cap A = \emptyset.$
However, since $x$ is a limit point of $A,$ every open neighbourhood of $x$ contains a point of $A$ different from $x,$ which contradicts $U \cap A = \emptyset.$

Next, suppose $A$ contains all its limit points.
We will show it is closed.
Suppose $x \in X \setminus A.$
This means $x$ is not a limit point of $A,$ so there exists an open neighbourhood $U$ of $x$ such that $U \cap A$ contains no points other than, possibly, $x.$
Therefore, $U \subseteq X \setminus A,$ so $X \setminus A$ is open, and $A$ is closed.
:::


:::{prf:definition} Dense subset
:label: topology:def-dense-subset
A subset $A \subseteq X$ of a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U})$ is dense in $X$ if $\overline{A} = X.$
:::


:::{prf:definition} Interior
:label: topology:def-interior
Let $A \subseteq X$ be a subset of a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U}).$
Define

$$\mathcal{O}_A = \{U \subseteq X \mid U \subseteq A \text{ and } U \text{ is open}\}.$$

Then, the interior of $A,$ written $\text{Int}(A),$ is defined as

$$\text{Int}(A) = \bigcup_{U \in \mathcal{O}_A} U.$$
:::


:::{prf:lemma} Interior of a set is the largest open set contained in it
:label: topology:lemma-interior-open-set
Given a set $A \subseteq X$ in a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U}),$ its {prf:ref}`interior<topology:def-interior>` $\text{Int}(A)$ is the largest open set contained in $A.$
:::

:::{dropdown} Proof: Interior of a set is the largest open set contained in it
Let $A \subseteq X$ be a subset of a topological space $(X, \mathcal{U}).$
Then, since $\text{Int}(A)$ is a union of open sets contained in $A,$ it is open and contained in $A.$
Suppose $U$ is an open set contained in $A.$
Then $U \in \mathcal{O}_A,$ so $U \subseteq \text{Int}(A).$
Therefore, $\text{Int}(A)$ is the largest open set contained in $A.$
:::


:::{prf:lemma} Complement of interior is closure of complement
:label: topology:def-complement-interior-closure-complement
Given a set $A \subseteq X$ in a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U}),$ we have

$$X \setminus \text{Int}(A) = \overline{X \setminus A}.$$
:::

:::{dropdown} Proof: Complement of interior is closure of complement
Let $A \subseteq X$ be a subset of a topological space $(X, \mathcal{U}).$
We have that

$$X \setminus \text{Int}(A) = X \setminus \bigcup_{U \in \mathcal{O}_A} U = \bigcap_{U \in \mathcal{O}_A} (X \setminus U) = \bigcap_{C \in \mathcal{C}_{X \setminus A}} C = \overline{X \setminus A}.$$
:::


### New topologies from old

Now we look into how existing topological spaces can be used to define new ones.
First, we define the subspace topology.

:::{prf:definition} Subspace topology
:label: topology:def-subspace-topology
Let $(X, \mathcal{U})$ be a {prf:ref}`topological space<topology:def-topological-space>`, and let $Y \subseteq X$ be a subset.
Then, the subspace topology on $Y$ is the collection of subsets of $Y$ given by: $V$ is an open set in $Y$ if there exists an open set $U \in \mathcal{U}$ such that $V = U \cap Y.$
:::


:::{prf:lemma} Subspace topology is a topology
:label: topology:lemma-subspace-topology
The subspace topology on a subset $Y \subseteq X$ of a {prf:ref}`topological space<topology:def-topological-space>` $(X, \mathcal{U})$ is a {prf:ref}`topology<topology:def-topological-space>`.
:::

:::{dropdown} Proof: Subspace topology is a topology
Let $(X, \mathcal{U})$ be a topological space, and let $Y \subseteq X$ be a subset.
We want to show that the subspace topology on $Y$ is a topology.
Let $\mathcal{U}_Y$ be the subspace topology on $Y.$
We show each of the {prf:ref}`properties of a topology<topology:def-topological-space>` are satisfied by the subspace topology.

First, $\emptyset = \emptyset \cap Y$ and $Y = X \cap Y,$ so $\emptyset, Y \in \mathcal{U}_Y.$
Second, suppose $V_\alpha \in \mathcal{U}_Y$ for all $\alpha \in A.$
Then, there exist open sets $U_\alpha \in \mathcal{U}$ such that $V_\alpha = U_\alpha \cap Y.$
Then

$$\bigcup_{\alpha \in I} V_\alpha = \bigcup_{\alpha \in I} (U_\alpha \cap Y) = (\bigcup_{\alpha \in I} U_\alpha) \cap Y \in \mathcal{U}_Y.$$

Finally, suppose $V_1, \dots, V_n \in \mathcal{U}_Y.$
Then, there exist open sets $U_1, \dots, U_n \in \mathcal{U}$ such that $V_i = U_i \cap Y.$
Then

$$\bigcap_{i=1}^n V_i = \bigcap_{i=1}^n (U_i \cap Y) = (\bigcap_{i=1}^n U_i) \cap Y \in \mathcal{U}_Y.$$

Putting these three parts together, we conclude that the subspace topology on $Y$ is a topology.
:::


:::{bibliography}
:filter: docname in docnames

:::