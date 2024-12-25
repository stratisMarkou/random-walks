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
A sequence $x_n \to x$ if for every open neighbourhood $U$ of $x,$ there exists $N \in \mathbb{N}$ such that $x_n \in U$ for all $n > N.$
:::


We now turn to uniqueness of limits.
In general, in a topological space limits need not be unique.
For example, given a set $X$ with the coarse topology $\mathcal{U} = \{\emptyset, X\},$ every sequence converges to every point.
However, further assumptions on the topology can result into unique limits.

:::{prf:definition} Hausdorff space
:label: topology:def-hausdorff-space
A topological space $(X, \mathcal{U})$ is Hausdorff if for every pair of distinct points $x_1, x_2 \in X,$ there exist open neighbourhoods $U_1, U_2$ of $x_1, x_2$ respectively such that $U_1 \cap U_2 = \emptyset.$
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