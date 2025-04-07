# Well-orderings and ordinals

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

$\newcommand{\vd}{\vdash}$
$\newcommand{\dvd}{\models}$
$\newcommand{\imp}{\Rightarrow}$


## Well-orderings

:::{prf:definition} Strict total order
:label: lst:def-strict-total-order
Given a set $X,$ a strict total order or linear order is a pair $(X, <),$ where $X$ is a set and $<$ is a relation on $X$ that satisfies

1. $x \not < x$ for all $x \in X.$
2. If $x < y, y < z,$ then $x < z$ for all $x, y, z \in X.$
3. $x < y$ or $x = y$ or $y < x$ for all $x, y \in X.$

We use the shorthand $x > y$ meaning $y < x.$
:::

:::{prf:definition} Non-strict total order
:label: lst:def-non-strict-total-order
A non-strict total order is a pair $(X, \leq),$ where $X$ is a set and $\leq$ is a relation on $X$ that satisfies

1. $x \leq x.$
2. If $x \leq y, y \leq z$ then $x \leq z$ for all $x, y, z \in X.$
3. If $x \leq y, y \leq x$ then $x = y$ for all $x, y \in X.$
4. $x \leq y$ or $y \leq x$ for all $x, y \in X.$

We use the shorthand $x \geq y$ meaning $y \leq x.$
:::

:::{prf:definition} Well-ordering
:label: lst:def-well-ordering
A {prf:ref}`strict total order<lst:def-strict-total-order>` $(X, <)$ is a well-ordering if every non-empty subset has a least element, that is

$$\begin{equation}
(\forall S \subseteq X)(S \neq \emptyset \imp (\exists x \in S)(\forall y \in S) y \geq x)
\end{equation}$$
:::


:::{prf:lemma} Well-ordering equivalent condition
:label: lst:lem-well-ordering-equivalent-condition
A total order is a well-ordering if and only if it has no infinite strictly decreasing sequence.
:::

:::{dropdown} Solution: Well-ordering equivalent condition
Suppose $(X, <)$ is a total order.

__Implies:__
Suppose $(X, <)$ is a total order.
Let $x_1 > x_2 > \dots,$ be an infinite strictly decreasing sequence in $X.$
Then $\{x_n \in X: n \in \mathbb{N}\}$ has no least element, contradicting the definition of a total order.

__Is implied by:__
Suppose $(X, <)$ does not have an infinite strictly decreasing sequence.
Let $S \subseteq X.$
If $S$ is non-empty and has no least element, then for any $x \in S$ we can find $x' \in S$ such that $x > x'.$
We can continue in this way to obtain an infinite strictly decreasing sequence

$$\begin{equation}
x > x' > x'' > \dots,
\end{equation}$$

which is a contradiction.
Therefore if $S$ is non-empty, it must have a least element.
:::

:::{prf:definition} Order isomorphism
We say the {prf:ref}`strict total orders<lst:def-strict-total-order>` $X, Y$ are isomorphic if there exists a bijection $f: X \to Y$ that is order preserving, that is $x < y \imp f(x) < f(y).$
:::

:::{prf:lemma} Principle by induction
:label: lst:lem-principle-by-induction
Let $X$ be a well-ordered set.
Suppose $S \subseteq X$ has the property

$$\begin{equation}
(\forall x)\left(((\forall y) y < x \imp y \in S) \imp x \in S\right).
\end{equation}$$

Then $S = X.$
:::

:::{dropdown} Proof: Principle by induction
Let $X$ be a {prf:ref}`well-ordering<lst:def-well-ordering>`.
Suppose $S \neq X$ is a subset for which the property in the theorem statement holds.
Since $X$ is a well-ordering, if $X \setminus S$ is non-empty, it has a least element, say $x.$
Since $y$ is the least element of $X \setminus S,$ this means that for all $y \in S$ such that $y < x,$ we have $y \in S.$
But since $S$ has the stated property, it follows that $x \in S,$ which is a contradiction.
Therefore $X \setminus S = \emptyset$ and $S = X.$
:::


<!-- $$\begin{equation}
\end{equation}$$

$$\begin{align}
\end{align}$$

:::{prf:definition} 
:label: lst:def-
:::

:::{prf:lemma} 
:label: lst:lem-
:::

:::{prf:theorem} 
:label: lst:thm-
::: -->
