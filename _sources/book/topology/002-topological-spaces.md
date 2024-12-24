# Topological Spaces

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

In the previous chapter we saw that in a metric space, continuity of functions is only indirectly determined by the metric itself.
Instead, the structure that determines continuity {prf:ref}`is the set of open sets<topology:theorem-characterisation-of-continuity>`.
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
Let $(X, d)$ be a metric space.
Then, the topology induced by $d$ is the set of all open sets in $X$ with respect to the metric $d.$
:::


We now also re-define continuity in terms of open sets.

:::{prf:definition} Continuous function
:label: topology:def-continuous-function-topology
Let $f: X \to Y$ be a function between topological spaces.
Then, $f$ is continuous if for every open set $U \subseteq Y,$ the pre-image $f^{-1}(U)$ is an open set in $X.$
:::

