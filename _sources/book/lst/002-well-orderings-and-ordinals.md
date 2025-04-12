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
:label: lst:def:strict-total-order
Given a set $X,$ a strict total order or linear order is a pair $(X, <),$ where $X$ is a set and $<$ is a relation on $X$ that satisfies

1. $x \not < x$ for all $x \in X.$
2. If $x < y, y < z,$ then $x < z$ for all $x, y, z \in X.$
3. $x < y$ or $x = y$ or $y < x$ for all $x, y \in X.$

We use the shorthand $x > y$ meaning $y < x.$
:::

:::{prf:definition} Non-strict total order
:label: lst:def:non-strict-total-order
A non-strict total order is a pair $(X, \leq),$ where $X$ is a set and $\leq$ is a relation on $X$ that satisfies

1. $x \leq x.$
2. If $x \leq y, y \leq z$ then $x \leq z$ for all $x, y, z \in X.$
3. If $x \leq y, y \leq x$ then $x = y$ for all $x, y \in X.$
4. $x \leq y$ or $y \leq x$ for all $x, y \in X.$

We use the shorthand $x \geq y$ meaning $y \leq x.$
:::

:::{prf:definition} Well-ordering
:label: lst:def:well-ordering
A {prf:ref}`strict total order<lst:def:strict-total-order>` $(X, <)$ is a well-ordering if every non-empty subset has a least element, that is

$$\begin{equation}
(\forall S \subseteq X)(S \neq \emptyset \imp (\exists x \in S)(\forall y \in S) y \geq x)
\end{equation}$$
:::


:::{prf:lemma} Well-ordering equivalent condition
:label: lst:lem:well-ordering-equivalent-condition
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
We say the {prf:ref}`strict total orders<lst:def:strict-total-order>` $X, Y$ are isomorphic if there exists a bijection $f: X \to Y$ that is order preserving, that is $x < y \imp f(x) < f(y).$
:::

:::{prf:lemma} Principle by induction
:label: lst:lem:principle-by-induction
Let $X$ be a well-ordered set.
Suppose $S \subseteq X$ has the property

$$\begin{equation}
(\forall x)\left(((\forall y) y < x \imp y \in S) \imp x \in S\right).
\end{equation}$$

Then $S = X.$
:::

:::{dropdown} Proof: Principle by induction
Let $X$ be a {prf:ref}`well-ordering<lst:def:well-ordering>`.
Suppose $S \neq X$ is a subset for which the property in the theorem statement holds.
Since $X$ is a well-ordering, if $X \setminus S$ is non-empty, it has a least element, say $x.$
Since $y$ is the least element of $X \setminus S,$ this means that for all $y \in S$ such that $y < x,$ we have $y \in S.$
But since $S$ has the stated property, it follows that $x \in S,$ which is a contradiction.
Therefore $X \setminus S = \emptyset$ and $S = X.$
:::

:::{prf:lemma} Uniqueness of well-ordering isomorphisms
:label: lst:lem:uniqueness-of-well-ordering-isomorphisms
Let $X$ and $Y$ be isomorphic well-orderings.
Then, there is a unique isomorphism between $X$ and $Y.$
:::

:::{dropdown} Proof: Uniqueness of well-ordering isomorphisms
Let $X, Y$ be well-orderings and $f$ and $g$ be two isomorphisms from $X$ to $Y.$
Note that since $f, g$ preserve order, they must map the least element of $X$ to the least element of $Y,$ so $f(\min X) = g(\min Y).$
By the {prf:ref}`principle by induction<lst:lem:principle-by-induction>` it suffices to show that if $f(y) = g(y)$ for all $y < x,$ then $f(x) = g(x).$

Let $S = \{f(x) \in Y: y < x\}.$
We know that $Y \setminus S$ is non-empty because $f(x) \not \in S.$
Therefore $Y \setminus S$ must have a least element, say $a = \min(Y \setminus S).$
Now it must be that $a = f(x)$ because otherwise, by the minimality of $a$ we would have $a < f(x),$ which means that $f^{-1}(a) < x,$ since $f$ is order preserving.
Then $f^{-1}(a) \in S$ and $a = f(f^{-1}(a)) \in Y,$ which is a contradiction.

The induction hypothesis is that $f(y) = g(y)$ for all $y < x.$
Therefore $\{g(y): y < x\} = S$ as well.
By the same argument as above $g(x) = \min(Y \setminus S) = f(x).$
Which concludes the proof.
:::


:::{prf:definition} Initial segment
:label: lst:def:initial-segment
A subset $Y$ of a totally ordered $X$ is an initial segment if

$$\begin{equation}
x \in Y, y < x \imp y \in Y.
\end{equation}$$
:::


:::{prf:lemma} Initial segment equivalent condition
:label: lst:lem:initial-segment-equivalent-condition
Every initial segment $Y$ of a {prf:ref}`well-ordering<lst:def:well-ordering>` $X$ is of the form

$$\begin{equation}
I_x = \{y \in X: y < x\}.
\end{equation}$$
:::

:::{dropdown} Proof: Initial segment equivalent condition
Let $X$ is a {prf:ref}`well-ordering<lst:def:well-ordering>`, and let $Y$ to be an initial segment in $X.$

Take $x = \min(X \setminus Y).$
Then for any $y \in I_x,$ we have $y < x.$
So $y \in Y$ by definition of $x.$
So $I_x \subseteq Y.$

Going the other direction, if $y \in Y,$ then $y \neq x.$
Also by the definition of $x,$ we cannot have $y > x,$ so $y < x.$
Therefore $y \in I_x$ and $Y \subseteq I_x.$

We conclude that $Y = I_x.$ 
:::


In the following results, we think of each function $f: X \to Y$ as a subset of $X \times Y,$ i.e. an element of $\mathbb{P}(X \times Y).$

:::{prf:definition} Restriction of a function
:label: lst:def:restriction-of-a-function
For $f: A \to B$ and $C \subseteq A,$ the restriction of $f$ to $C$ is

$$\begin{equation}
f|_C =\{(x, f(x)): x \in C\}.
\end{equation}$$
:::


:::{prf:theorem} Definition by recursion
:label: lst:thm:definition-by-recursion
Let $X$ be a well-ordered set and $Y$ be any set.
Then for any function $G: \mathbb{P}(X \times Y) \to Y,$ there exists a function $f: X \to Y$ such that

$$\begin{equation}
f(x) = G(f|_x)
\end{equation}$$

for all $x \in X.$
:::

::::{dropdown} Proof: Definition by recursion

We prove this result via a trick notion of an _attempt_.

:::{prf:definition} Attempt
:label: lst:def:attempt
Let $I$ is an initial segment of $X.$
We say $h: I \to Y$ is an attempt if

$$h(x) = G(h|_{I_x})$$

for all $x \in I.$
:::


Any two attempts that are defined at some $x$ must be equal at $x.$

:::{prf:lemma} Attempts agree
:label: lst:lem:attempts-agree
If {prf:ref}`attempts<lst:def:attempt>` $h$ and $h'$ are defined at $x,$ then $h(x) = h'(x).$
:::

:::{dropdown} Proof: Attempts agree
Note that $h$ and $h'$ must agree on the least element of $X.$
Therefore by induction it suffices to show that if $h(y) = h'(y)$ for all $y < x,$ then $h(x) = h'(x).$
Suppose $h(y) = h'(y)$ for all $y < x.$
Then $h|_{I_x} = h'|_{I_x}.$
By the definition of attempt, we then have

$$h(x) = G(h|_{I_x}) = G(h'_{I_x}) = h'(x).$$
:::

Now we show that for any $x \in X$ there must exist an attempt $h$ that is defined at $x.$


:::{prf:lemma} An attempt exists for each $x$
:label: lst:lem:an-attempt-exists-for-each-x
For any $x \in X,$ there must exist an attempt $h$ that is defined at $x.$
:::

:::{dropdown} Proof: An attempt exists for each $~x$
We proceed by induction, and assume that for each $y < x,$ there exists an attempt $h_y$ defined at $y.$
Then we combine all these functions together and take $h' = \cup_{y < x} h_y.$
This is a well-defined function since {prf:ref}`attempts agree<lst:lem:attempts-agree>`, and it is defined for all $y < x.$
Now, add $(x, G(h'|_{I_x}))$ to $h',$ to obtain an attempt $h$ that is defined at $x.$
We therefore have an attempt that is defined at $x.$
:::

Given this result, define $f: X \to Y$ by $f(x) = y$ if there exists an attempt $h,$ defined at $x$ with $h(x) = y.$
Finally, we note that by its definition using attempts, this $f$ is unique, concluding the proof.
::::


:::{prf:lemma} Subset collapse
:label: lst:lem:subset-collapse
Let $X$ be a well-ordering and let $Y \subseteq X.$
Then $Y$ is isomorphic to an initial segment of $X.$
Moreover, this initial segment is unique.
:::

:::{dropdown} Proof: Subset collapse
Let $X$ be a well-ordering and let $Y \subseteq X.$
We will construct $f: Y \to X$ to be an order preserving bijection with an initial segment of $X.$
Specifically, we will map each $x \in Y.$ to the smallest element of $X$ that we have not yet mapped to.
Let

$$\begin{equation}
f(x) = \min (X \setminus \{f(y): y < x\}).
\end{equation}$$

The minimum is well-defined because $\{f(y): y < x\} \neq X.$
This is because $f(z) < x$ for all $z < x$ by induction, so $x \not \in \{f(y): y < x\}.$
Therefore, by {prf:ref}`lst:thm:definition-by-recursion`, the result holds.
:::


:::{prf:definition} Isomorphic notation
:label: lst:def:isomorphic-notation
We write $X \leq Y$ if $X$ is isomorphic to an {prf:ref}`initial segment<lst:def:initial-segment>` of $Y.$
We write $X < Y$ if $X \leq Y$ but $X$ is not isomorphic to $Y,$ and similarly for $X > Y.$
:::


:::{prf:theorem} Well-orderings are ordered
:label: lst:thm:well-orderings-are-ordered
Let $X, Y$ be well-orderings.
Then either $X \leq Y$ or $Y \leq X.$
:::

:::{dropdown} Well-orderings are ordered
We attempt to define an isomorphism $f: X \to Y$ by

$$\begin{equation}
f(x) = \min (Y \setminus \{f(y): y < x\}).
\end{equation}$$

Now, depending on whether $Y \setminus \{f(y): y < x\} = \emptyset$ for some $x \in X,$ this function is either well-defined or not.
If it is well-defined, then it is an isomorphism from $X$ to an initial segment of $Y.$
If it is not well-defined, there exists an $x \in X$ such that $\{f(y): y < x\} = Y.$
In this case, $f$ is a bijection between $I_x = \{y: y < x\}$ and $Y.$
So $f$ is an isomorphism between $Y$ and an initial segment of $X.$
:::


:::{prf:theorem} Sufficient condition for isomorphic well-orderings
:label: lst:thm:sufficient-condition-for-well-orderings
Let $X, Y$ be well-orderings.
If $X \leq Y$ and $Y \leq X,$ then $X$ and $Y$ are isomorphic.
:::

:::{dropdown} Solution: Sufficient condition for isomorphic well-orderings
Let $X, Y$ be well-orderings with $X \leq Y$ and $Y \leq X.$

Since $X \leq Y,$ there is an order preserving function $f: X \to Y$ that is a bijection between $X$ and an initial segment of $Y.$
Similarly, since $Y \leq X,$ there is an order preserving function $g: Y \to X$ that is a bijection between $Y$ and an initial segment of $X.$

Now $g \circ f: X \to X$ is a bijection between $X$ and an initial segment of $X.$
It is not possible to have a bijection between a set and a proper subset of the set, it must be that $g \circ f$ is a bijection between $X$ and itself.
Similarly, $f \circ g$ must be a bijection between $Y$ and itself.

Therefore, both $f$ and $g$ must be bijections, and $X$ and $Y$ are isomorphic.
:::



## New well orderings

:::{prf:definition} Successor
:label: lst:def:successor
Given a well-ordering $X$ and some $x \not \in X,$ we define a well-ordering on $X \cup \{x\}$ such that $y < x$ for all $y \in X,$ and call this the successor of $X,$ written $X^+.$
:::


:::{prf:definition} Extension
:label: lst:def:extension
Given well-orderings $(X, <_X)$ and $(Y, <_Y),$ we say that $Y$ is an extension of $X$ if $X$ is a proper {prf:ref}`initial segment<lst:def:initial-segment>` of $Y$ and $<_X$ and $<_Y$ agree when defined.
:::


:::{prf:definition} Nested family
:label: lst:def:nested-family
We say well-orderings $\{X_i: i \in I\}$ form a nested set if for all $i, j \in I$ with $i \neq j,$ either $X_i$ extends $X_j$ or $X_j$ extends $X_i.$
:::


:::{prf:lemma} Nested family has union well-ordering
:label: lst:lem:nested-family-has-union-well-ordering
Let $\{X_i: i \in I\}$ be a {prf:ref}`nested set<lst:def:nested-family>` of well-orderings.
Then, there exists a well-ordering $X$ with $X_i \leq X$ for all $i \in I.$
:::


:::{dropdown} Proof: Nested family has union well-ordering
Let $\{X_i: i \in I\}$ be a nested set of well-orderings.
Define $X = \cup_{i \in I} X_i,$ with the relation $<$ defined on $X$ as $\cup_{i \in I} <_i,$ where $<_i$ is the ordering of $X_i.$
This is a {prf:ref}`total ordering<lst:def:strict-total-order>`.
Since $\{X_i: i \in I\}$ is a nested family, each $X_i$ is an initial segment of $X.$

To show this is a well-ordering, let $S \subseteq X$ be a non-empty subset of $X.$
Then $S \cap X_i$ must be non-empty for some $i \in I.$
Since $X_i$ is a well-ordering, $S \cap X_i$ has a minimum element, say $x.$
Then, for any $y \in S,$ we must have $x \leq y.$
Otherwise, if $y \in S$ and $y < x,$ we would have $y \in X_i$ because $X_i$ is an initial segment of $X.$
Therefore, $S$ has a least element and $X$ is a well-ordering.
:::


## Ordinals

:::{prf:definition} Ordinal
:label: lst:def:ordinal
An ordinal is a well-ordering, with any two regarded as the same if they are isomorphic.
:::


:::{prf:definition} Order type
:label: lst:def:order-type
If a well-ordering $X$ has a corresponding ordinal $\alpha,$ we say $X$ has order type $\alpha$ and write $\text{otp}(X) = \alpha.$
:::

:::{prf:definition} Order type notation
:label: lst:def:order-type-notation
For each $k \in \mathbb{N},$ we write $k$ for the order type of the (unique) well-ordering of size $k.$
We write $\omega$ for teh order type of $\mathbb{N}.$
:::

:::{prf:definition} Ordinal inequality signs
:label: lst:def:ordinal-inequality-signs
For ordinals $\alpha, \beta,$ we write $\alpha \leq \beta$ if $X \leq Y$ for some $X$ of type $\alpha$ and $Y$ of type $\beta.$
We define strict inequality sings for ordinals in a similar way.
:::


:::{prf:definition} Initial segment of set of ordinals
:label: lst:def:initial-segment-of-set-of-ordinals
We write $I_\alpha = \{\beta: \beta < a\}.$
:::

:::{prf:lemma} Ordinals smaller than an ordinal form a well-ordering
:label: lst:lem:ordinals-smaller-than-an-ordinal-form-a-well-ordering
Let $\alpha$ be an ordinal.
Then the ordinals $< \alpha$ form a well-ordering of order type $\alpha.$
:::

:::{dropdown} Proof: Ordinals smaller than an ordinal form a well-ordering
Let $\alpha$ be an ordinal.
Let $X$ have order type $\alpha.$
By {prf:ref}`lst:def:isomorphic-notation`, the well orderings $< X$ are exactly those well-orderings which are isomorphic to some proper initial segment of $X.$
These are the sets $I_x$ for some $x \in X.$
We can therefore form a bijection between $X$ and the well-orderings $< X$ via the function that maps $x \in X$ to $I_x.$
This function is one-to-one and order preserving.
Therefore $\alpha$ is isomorphic to $X$ which is isomorphic to the collection of ordinals of size $< \alpha.$
:::


:::{prf:theorem} Non-empty set of ordinals has least element
:label: lst:thm:non-empty-set-of-ordinals-has-least-element
Let $S$ be a non-empty set of ordinals.
Then $S$ has a least element.
:::

:::{dropwdown} Proof: Non-empty set of ordinals has least element
Suppose $S$ is a non-empty set of ordinals.
Pick $\alpha \in S.$
If $\alpha$ is the least element of $S$ then we are done, so suppose it is not.
Then $I_\alpha \cap S$ is a non-empty set.
Since $I_\alpha$ is well-ordered, the set $I_\alpha \cap S$ has a least element, and this is also the least element of $S.$
:::


:::{prf:theorem} Burali-Forti
:label: lst:thm:burali-forti
The ordinals do not form a set.
:::

:::{dropdown} Proof: Burali-Forti
Suppose the {prf:ref}`ordinals<lst:def:ordinal>` form a set $X.$
Then they also form a {prf:ref}`well-ordering<lst:def:ordinal>`.
Let the {prf:ref}`order type<lst:def:order-type>` of $X$ be $\alpha.$
Then $X$ is {prf:def}`isomorphic<lst:def:isomorphic-notation>` to $I_\alpha,$ which is a proper {prf:ref}`initial segment<lst:def:initial-segment-of-set-of-ordinals>` of $X.$
This is a contradiction.
:::

<!-- $$\begin{equation}
\end{equation}$$

$$\begin{align}
\end{align}$$

:::{prf:definition} 
:label: lst:def:
:::

:::{prf:lemma} 
:label: lst:lem:
:::

:::{prf:theorem} 
:label: lst:thm:
:::

:::{dropdown} 
::: -->