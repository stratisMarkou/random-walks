# Measures

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

This chapter builds up measures.
First, we establish a notion of length on the real line, which we need in order to build up integration.
This notion of length is described by the outer measure.
The outer measure has several good properties which align with our expectations of what an appropriate definition of length on the real line should be.

However, the outer measure lacks an important property, namely additivity: the outer measure of the union of two disjoint sets is not necessarily the sum of the outer measures of the two sets.
This is a problem, because we need additivity in order to prove useful theorems about integration.
We will see that this is not a fundamental limitation of our definition of the outer measure, and show that any function that satisfies the good properties of the outer measure and has domain equal to the power set of $\mathbb{R}$ cannot be additive.

A solution to this issue, which does not give up the good properties of the outer measure, is to relax the requirement that our notion of length is defined on all subsets of $\mathbb{R},$ and instead only require that it is defined on a certain collection of subsets of $\mathbb{R}.$
This leads us to the definitions of $\sigma$-algebras, measurable sets, and measurable functions.
We then introduce measures, and specifically the Lebesgue measure, which we will use later to define integration.

## Outer measure

First, we define and study the outer measure, which is a notion of length on the real line.
We will prove a few good properties that one would hope to hold for a notion of length on the real line.
Then, we will show that the outer measure is not additive.

### Definition of the outer measure

To define the outer measure, we first need a definition of the length of an open interval.

:::{prf:definition} Length of an open interval
:label: mira:def:length-of-open-interval
The length $\ell(I)$ of an open interval $I \subseteq \mathbb{R}$ is defined by

$$\begin{align}
\ell(I) = \begin{cases}
b - a & \text{if } I = (a, b) \text{ for some } a, b \in \mathbb{R} \text{ with } a < b, \\
0 & \text{if } I = \emptyset, \\
\infty & \text{if } I = (-\infty, a) \text{ or } I = (a, \infty) \text{ for some } a \in \mathbb{R}, \\
\infty & \text{if } I = (-\infty, \infty).
\end{cases}
\end{align}$$

:::


Given lengths of open intervals, we can define the outer measure of a set as the least sum of the lengths of open intervals that cover the set.

:::{prf:definition} Outer measure
:label: mira:def:outer-measure
The outer measure $|A|$ of a subset $A \subseteq \mathbb{R}$ is defined by

$$|A| = \inf \left\{ \sum_{j=1}^\infty \ell(I_j) : A \subseteq \bigcup_{j=1}^\infty I_j \right\}.$$

:::



### Good properties

The outer measure has a number of good properties.
First, the outer measure of countable subsets of $\mathbb{R}$ is zero.

:::{prf:theorem} Countable sets have outer measure zero
:label: mira:thm:countable-sets-have-outer-measure-zero
Every countable subset of $\mathbb{R}$ has {prf:ref}`outer measure<mira:def:outer-measure>` $0.$
:::

:::{dropdown} Proof: Countable sets have outer measure zero
Suppose $A = \{ a_1, a_2, \ldots \}$ is a countable subset of $\mathbb{R}.$
Let $\epsilon > 0.$
For $k \in \mathbb{Z}^+,$ let

$$I_k = \left(a_k - \frac{\epsilon}{2^k}, a_k + \frac{\epsilon}{2^k} \right).$$

Then $A \subseteq \bigcup_{k=1}^\infty I_k$ is a sequence of open intervals whose union contains $A.$
Because

$$\sum_{k=1}^\infty \ell(I_k) = 2\epsilon,$$

we have $|A| \leq 2\epsilon.$
Because $\epsilon > 0$ is an arbitrary positive real number, this implies that $|A| = 0.$
:::

Second, the outer measure preserves order, that is the outer measure of a subset of $\mathbb{R}$ is less than or equal to the outer measure of any of its supersets.

:::{prf:theorem} Outer measure preserves order
:label: mira:thm:outer-measure-preserves-order
If $A$ and $B$ are subsets of $\mathbb{R}$ with $A \subseteq B,$ then $|A| \leq |B|.$
:::

:::{dropdown} Proof: Outer measure preserves order
Suppose $A$ and $B$ are subsets of $\mathbb{R}$ with $A \subseteq B,$ and let $I_1, I_2, \ldots$ be a sequence of open intervals whose union contains $B.$
Then the union of this sequence of open intervals also contains $A.$
Therefore

$$|A| \leq \sum_{j=1}^\infty \ell(I_j),$$

and taking the infimum of both sides, over all sequences of open intervals whose union contains $B$ gives $|A| \leq |B|.$

:::


The third good property of the outer measure is translation invariance.
To establish this property, we first need a definition of the translation of a set.

:::{prf:definition} Translation
:label: mira:def:translation
For $A \subseteq \mathbb{R}$ and $t \in \mathbb{R},$ the translation of $t + A$ is defined by

$$A + t = \{ a + t : a \in A \}.$$
:::

:::{prf:theorem} Outer measure is translation invariant
:label: mira:thm:outer-measure-is-translation-invariant
For every subset $A$ of $\mathbb{R}$ and every $t \in \mathbb{R},$ we have $|t + A| = |A|.$
:::

:::{dropdown} Proof: Outer measure is translation invariant
Suppose $A$ is a subset of $\mathbb{R}$ and $t \in \mathbb{R}.$
Let $I_1, I_2, \ldots$ be a sequence of open intervals whose union contains $A.$
Then $t + I_1, t + I_2, \ldots$ is a sequence of open intervals whose union contains $t + A.$
Thus

$$|t + A| \leq \sum_{j=1}^\infty \ell(t + I_j) = \sum_{j=1}^\infty \ell(I_j),$$

and taking the infimum of both sides, over all sequences of open intervals whose union contains $A$ gives $|t + A| \leq |A|.$
Conversely, we can apply the same argument by noting that $A = -t + (t + A)$ to obtain

$$|A| = |-t + (t + A)| \leq |t + A|.$$

Putting these two inequalities together gives $|A| = |t + A|.$
:::


Another useful property of the outer measure is countable subadditivity.
This property will also turn out to be true of more general measures which we will define later.

:::{prf:theorem} Outer measure is countably subadditive
:label: mira:thm:countable-subadditivity-of-outer-measure
Suppose $A_1, A_2, \ldots$ are subsets of $\mathbb{R}.$
Then

$$\left| \bigcup_{k=1}^\infty A_k \right| \leq \sum_{k=1}^\infty |A_k|.$$
:::

:::{dropdown} Proof: Outer measure is countably subadditive
If $|A_k| = \infty$ for some $k \in \mathbb{Z}^+,$ then the inequality holds.
Suppose instead that $|A_k| < \infty$ for all $k \in \mathbb{Z}^+.$
Let $\epsilon > 0.$
By the definition of infimum, for each $k \in \mathbb{Z}^+,$ there exists a sequence $I_{k, 1}, I_{k, 2}, \ldots$ whose union contains $A_k$ and

$$\sum_{j=1}^\infty \ell(I_{k, j}) \leq |A_k| + \frac{\epsilon}{2^k}.$$

Therefore

$$\sum_{k = 1}^\infty \sum_{j=1}^\infty \ell(I_{k, j}) \leq \sum_{k=1}^\infty \left( |A_k| + \frac{\epsilon}{2^k} \right) = \sum_{k=1}^\infty |A_k| + \epsilon.$$

Now, note that the doubly indexed sum above can be rearranged as a single indexed sum, in the order

$$I_{1, 1}, I_{2, 1}, I_{1, 2}, I_{3, 1}, I_{2, 2}, I_{1, 3}, I_{4, 1}, I_{3, 2}, I_{2, 3}, I_{1, 4}, \ldots.$$

From this we conclude that

$$\left| \bigcup_{k=1}^\infty A_k \right| \leq \sum_{k=1}^\infty |A_k| + \epsilon,$$

and since $\epsilon > 0$ is arbitrary, this implies that

$$\left| \bigcup_{k=1}^\infty A_k \right| \leq \sum_{k=1}^\infty |A_k|.$$
:::


### Heine-Borel theorem

Another important property that we want to show for the outer measure is that its value on a closed (rather than open) value on a bounded interval is equal to the difference between the endpoints of the interval, that is $|[a, b]| = b - a$ for $a, b \in \mathbb{R}$ with $a < b.$
To show this, we will use the Heine-Borel theorem, which is a theorem of independent interest beyond measure theory.
The Heine-Borel theorem is a statement about open covers, an idea which we now define.

:::{prf:definition} Open cover, finite subcover
Suppose $A \subseteq \mathbb{R}.$
A collection $\mathcal{C}$ of open intervals is called an open cover of $A$ if $A$ is contained in the union of the intervals in $\mathcal{C}.$
An open cover $\mathcal{C}$ of $A$ is said to have a finite subcover if $A$ is contained in the union of some finite list of sets in $\mathcal{C}.$
:::


The Heine-Borel theorem states that every open cover of a closed bounded subset of $\mathbb{R}$ has a finite subcover.

:::{prf:theorem} Heine-Borel
:label: mira:thm:heine-borel
Every open cover of a closed bounded subset of $\mathbb{R}$ has a finite subcover.
:::

:::{dropdown} Proof: Heine-Borel
This proof goes in two parts.
The first part shows the result for the special case of a closed bounded interval $[a, b].$
The second part then extends this result to any closed bounded subset of $\mathbb{R}.$

__Part 1:__
Suppose $F = [a, b]$ is a closed bounded interval and $\mathcal{C}$ is an open cover of $F.$
Let 

$$D = \{ d \in [a, b]: [a, d] \text{ has a finite subcover of } \mathcal{C} \}.$$

First, $a \in D$ because $[a, a] = \{ a \}$ has a finite subcover of $\mathcal{C},$ since $a \in G$ for some $G \in \mathcal{C}.$
Thus $D$ is nonempty.
Let $s = \sup D,$ and note that $s \in [a, b].$
Since $s \in [a, b],$ there exists an open set $G \in \mathcal{C}$ such that $s \in G.$
Let $\delta > 0$ be such that $(s - \delta, s + \delta) \subseteq G.$
Because $s = \sup D,$ there exist $d \in (s - \delta, s]$ and $n \in \mathbb{Z}^+$ and $G_1, \ldots, G_n \in \mathcal{C}$ such that

$$[a, d] \subseteq \bigcup_{j=1}^n G_j.$$

Now, adding $G$ to this union gives

$$[a, d'] \cup G \subseteq \bigcup_{j=1}^n G_j \cup G,$$

for all $d' \in [s, s + \delta),$ so $d' \in D$ for all $d' \in [s, s + \delta) \cap [a, b],$ which implies that $s = b,$ because otherwise we end up with a contradiction.
Therefore, $F = [a, b]$ has a finite subcover of $\mathcal{C}.$

__Part 2:__
Suppose $F$ is a closed bounded subset of $\mathbb{R}$ and $\mathcal{C}$ is an open cover of $F.$
Because $F$ is bounded, there exist $a, b \in \mathbb{R}$ such that $F \subseteq [a, b].$
The collection of open sets $\mathcal{C} \cup (\mathbb{R} \setminus F)$ is an open cover of $[a, b],$ so by Part 1, there exists a finite subcover $\mathcal{C}'$ of $[a, b]$ from $\mathcal{C} \cup (\mathbb{R} \setminus F),$ say

$$[a, b] \subseteq (\mathbb{R} \setminus F) \cup \bigcup_{j=1}^n G_j,$$

where $G_1, \ldots, G_n \in \mathcal{C}.$
Thus

$$F \subseteq \bigcup_{j=1}^n G_j,$$

which shows that $F$ has a finite subcover from $\mathcal{C}.$
:::

Using the Heine-Borel theorem, we can now show that the outer measure of a closed interval is equal to the difference between the endpoints of the interval.

:::{prf:theorem} Outer measure of a closed interval
:label: mira:thm:outer-measure-of-a-closed-interval

Suppose $a, b \in \mathbb{R}$ with $a < b.$
Then $|[a, b]| = b - a.$
:::

:::{dropdown} Proof: Outer measure of a closed interval

We will show the equality above via two inequalities, namely

$$|[a, b]| \leq b - a   \text{ and }  b - a \leq |[a, b]|.$$ (mira:eq:outer-measure-of-closed-interval)

__First inequality:__
For the first inequality, consider that $[a, b] \subseteq (a - \epsilon, b + \epsilon)$ for all $\epsilon > 0,$ so using the {prf:ref}`order preserving property of the outer measure <mira:thm:outer-measure-preserves-order>`, we have

$$|[a, b]| \leq |(a - \epsilon, b + \epsilon)| = b - a + 2\epsilon,$$

and since $\epsilon > 0$ is arbitrary, this implies that $|[a, b]| \leq b - a.$

__Second inequality:__
For the second inequality, suppose that $I_1, I_2, \ldots$ is a sequence of open intervals whose union contains $[a, b].$
Then $I_1, I_2, \ldots$ is an open cover of $[a, b],$ so by the {prf:ref}`Heine-Borel theorem<mira:thm:heine-borel>`, there exists an $n \in \mathbb{Z}^+$ such that

$$[a, b] \subseteq I_1 \cup \cdots \cup I_n.$$

We will prove by induction that

$$
\sum_{j=1}^n \ell(I_j) \geq b - a,
$$ (mira:eq:outer-measure-of-closed-interval-induction)

which will yield the result after taking the infimum over all sequences of open intervals whose union contains $[a, b].$
To show {eq}`mira:eq:outer-measure-of-closed-interval-induction`, we first note that the base case $n = 1$ holds, because if $[a, b] \subseteq I_1,$ then by the {ref}`order preserving property of the outer measure <mira:thm:outer-measure-preserves-order>`, we have $|[a, b]| \leq \ell(I_1).$
Now, suppose that {eq}`mira:eq:outer-measure-of-closed-interval-induction` holds for some $n \in \mathbb{Z}^+.$
Suppose also that $[a, b] \subseteq I_1 \cup \cdots \cup I_{n+1}.$
Then, $b$ is in at least one of these open intervals which, after relabelling, we can assume is $I_{n+1}.$
Let us write $I_{n+1} = (c, d),$ and note that $b < d.$
Then if $c \leq a,$ we have that $\ell(I_{n+1}) = d - c \geq b - a,$ which shows the inductive step.
If $c > a,$ then $a < c < b < d.$
Since $[a, b]$ is has $I_1, \ldots, I_n, I_{n+1}$ as an open cover, it follows that $[a, c]$ has $I_1, \ldots, I_n,$ as an open cover, that is

$$[a, c] \subseteq I_1 \cup \cdots \cup I_n.$$

Therefore, by the inductive hypothesis, we have

$$\sum_{j=1}^n \ell(I_j) \geq c - a.$$

Adding $\ell(I_{n+1}) = d - c$ to both sides of this inequality gives

$$\sum_{j=1}^{n+1} \ell(I_j) \geq d - a = b - a,$$

which completes the inductive step.

Putting the two inequalities in {eq}`mira:eq:outer-measure-of-closed-interval` together gives the result.
:::


A nice result from the previous theorems is that nontrivial intervals in $\mathbb{R}$ are uncountable.
Interestingly, this proof does not use the [diagonal argument](https://en.wikipedia.org/wiki/Cantor's_diagonal_argument), which is the argument that is usually used to show that the real numbers are uncountable.

:::{prf:theorem} Nontrivial intervals are uncountable
Every inverval in $\mathbb{R}$ that contains at least two distinct elements is uncountable.
:::

:::{dropdown} Proof: Nontrivial intervals are uncountable

Suppose $I$ is an interval that contains $a, b \in \mathbb{R}$ with $a < b.$
Then

$$ |I| \geq |[a, b]| = b - a > 0,$$

where the first inequality follows by the {prf:ref}`order preserving property of the outer measure <mira:thm:outer-measure-preserves-order>`, and the equality follows by the previous theorem on the {prf:ref}`outer measure of a closed interval <mira:thm:outer-measure-of-a-closed-interval>`.
Since {prf:ref}`every countable subset of $\mathbb{R}$ has outer measure zero <mira:thm:countable-sets-have-outer-measure-zero>` and $I$ has nonzero measure, it follows that $I$ is uncountable.

:::



### Nonadditivity of the outer measure
Now we come to the negative result of the outer measure, namely that it is not additive.
Additivity is an important property that we would like our notion of length to have, because it allows us to prove good theorems about integration.

The proof of nonadditivity of the outer measure relies on defining a subset of a closed interval.
Similar sets are used beyond the subadditivity of the outer measure, so we give it a special name.

:::{prf:definition} Rational difference equivalence relation
:label: mira:def:rational-difference-equivalence-relation

Suppose $S \in \mathbb{R}.$
Let $\sim$ be the equivalence relation defined by $x \sim y \iff x - y \in \mathbb{Q},$ for any $\mathbb{R}.$
We call this the rational difference equivalence relation.
:::

:::{dropdown} Detail: Rational difference is an equivalence relation
Let $\sim$ be the binary relation defined by

$$a \sim b \iff a - b \in \mathbb{Q}.$$

Note that $\sim$ is an equivalence relation on $\mathbb{R},$ because it is:

- reflexive: $a - a = 0 \in \mathbb{Q};$
- symmetric: If $a - b \in \mathbb{Q},$ then $b - a = -(a - b) \in \mathbb{Q};$
- transitive: If $a - b \in \mathbb{Q}$ and $b - c \in \mathbb{Q},$ then $a - c = (a - b) + (b - c) \in \mathbb{Q}.$

:::


:::{prf:theorem} Nonadditivity of the outer measure
:label: mira:thm:non-additivity-of-outer-measure

There exist disjoint subsets $A, B$ of $\mathbb{R}$ such that

$$|A \cup B| \neq |A| + |B|.$$
:::


:::{dropdown} Proof: Nonadditivity of the outer measure
__Proof idea:__
We will define a countable collection of disjoint sets.
We will set up these sets so that their union is contained in an closed bounded interval of $\mathbb{R},$ and they all have equal outer measure.
Then, we will show that the outer measure of each of these sets is nonzero, which leads to a contradiction.

__Proof:__
Let $\sim$ be the {prf:ref}`rational difference equivalence relation<mira:def:rational-difference-equivalence-relation>`, and for each $a \in [-1, 1]$ let $\tilde{a}$ be the equivalence class of $a$ under $\sim.$
Then

$$[-1, 1] = \bigcup_{a \in [-1, 1]} \tilde{a}.$$

Now, let $V$ be a representer set, containing exactly one element from each equivalence class of $\tilde$ on $[-1, 1].$
Let also $r_1, r_2, \ldots$ be a sequence which contains all the rational numbers in $[-2, 2]$ exactly once.
Then

$$[-1, 1] \subseteq \bigcup_{k=1}^\infty (r_k + V),$$

because for each $a \in [-1, 1],$ there is a unique element $v \in V$ that is in the same equivalence class as $a,$ namely $v = \tilde{a} \cap V,$ so $a - v \in \mathbb{Q},$ from which it follows that $a - v = r_k$ for some $k \in \mathbb{Z}^+,$ and therefore $a \in r_k + V.$
The set inclusion above together with the {prf:ref}`order preserving property <mira:thm:outer-measure-preserves-order>` of the outer measure, and the {prf:ref}`translation invariance <mira:thm:outer-measure-is-translation-invariant>` of the outer measure imply that

$$2 = |[-1, 1]| \leq \sum_{k=1}^\infty |r_k + V| = \sum_{k=1}^\infty |V|$$

Thus $|V| > 0.$
Now, note that the sets $(r_1 + V), (r_2 + V), \ldots, (r_K + V)$ are disjoint for any $K \in \mathbb{Z}^+.$
Note also that for any $K \in \mathbb{Z}^+,$ we have

$$ \bigcup_{k=1}^K (r_k + V) \subseteq [-3, 3] \implies \left| \bigcup_{k=1}^K (r_k + V) \right| \leq 6.$$

Now, suppose that the outer measure is additive.
Then, applying the additivity property $K - 1$ times gives

$$\left| \bigcup_{k=1}^K (r_k + V) \right| = \sum_{k=1}^K |r_k + V| = K|V| < 6,$$

reaching a contradiction, because $|V| > 0,$ so the above inequality cannot hold for any $K.$
:::

Shortly, we will show that this negative result is not a fundamental limitation of our definition of the outer measure.
Before doing so however, we will give a positive result that is useful in some contexts.
Specifically, we will show that given a sequence of sets that are contained by disjoint open intervals, the outer measure of the union of the sets is equal to the sum of the outer measures of the sets.


:::{prf:theorem} Outer measure is additive if sets are contained by disjoint open intervals
:label: mira:thm:outer-measure-is-additive-if-sets-are-separable

Suppose $S_1, S_2, \ldots$ is a sequence of sets and $A_1, A_2, \ldots$ is a sequence of disjoint open intervals with $S_k \subseteq A_k,$ then

$$\left|\bigcup_{n=1}^\infty S_n\right| = \sum_{n=1}^\infty |S_n|.$$
:::


:::{dropdown} Proof: Outer measure is additive if sets are contained by disjoint open intervals
First, by the {prf:ref}`subadditivity of the outer measure<mira:thm:countable-subadditivity-of-outer-measure>`, we have 

$$\left|\bigcup_{n=1}^\infty S_n\right| \leq \sum_{n=1}^\infty |S_n|.$$

We will now show the inequality in the other direction.
Suppose that $I_1, I_2, \ldots$ is a sequence of open intervals whose union contains $\cup_{n=1}^\infty S_n.$
Since the sets $A_n$ are disjoint, for each $k \in \mathbb{N},$ we have

$$\ell(I_k) \geq \sum_{n=1}^\infty \ell(I_k \cap A_n).$$

Therefore, we have

$$\sum_{k=1}^\infty \ell(I_k) \geq \sum_{k=1}^\infty \sum_{n=1}^\infty \ell(I_k \cap A_n) = \sum_{n=1}^\infty \sum_{k=1}^\infty\ell(I_k \cap A_n) \geq \sum_{n=1}^\infty |S_n|$$

where the last equality follows from the fact that for a fixed $n \in \mathbb{N},$ the sets $I_1 \cap A_n, I_2 \cap A_n, \ldots$ are open intervals whose union contains $S_n.$
Taking the infimum over all sequences of all open intervals whose union contains $\cup_{n=1}^\infty S_n,$ we have

$$\left|\bigcup_{n=1}^\infty S_n\right| \geq \sum_{n=1}^\infty |S_n|,$$ 

completing the result.
:::

This result highlights that if there is a sequence of sets on which the outer measure is not additive, then the sets cannot be separable in the sense described above.


## Measurable spaces and functions

A natural question is whether the {prf:ref}`nonadditivity of the outer measure <mira:thm:non-additivity-of-outer-measure>` is due to a flaw in our definition.
However, this next result shows that any notion of length that satisfies certain intuitive properties cannot be additive.

:::{prf:theorem} Nonexistence of extension of length to all subsets of $\mathbb{R}$
:label: mira:thm:nonexistence-of-extension-of-length-to-all-subsets-of-r
There does not exist a function $\mu$ with the following properties:

(a) $\mu$ is a function from the set of subsets of $\mathbb{R}$ to $[0, \infty],$

(b) $\mu(I) = \ell(I)$ for all open intervals $I \subseteq \mathbb{R},$

(c) For every disjoint sequence $A_1, A_2, \ldots$ of subsets of $\mathbb{R},$ $\mu \left( \cup_{k=1}^\infty A_k \right) = \sum_{k=1}^\infty \mu(A_k),$

(d) $\mu(t + A) = \mu(A)$ for all $A \subseteq \mathbb{R}$ and $t \in \mathbb{R}.$
:::

:::{dropdown} Proof: Nonexistence of extension of length to all subsets of $~\mathbb{R}$

Suppose there exists a function $\mu$ with all the properties listed in the statement of this theorem.
We will show that $\mu$ has all the properties that were used in our proof of the {prf:ref}`nonadditivity of the outer measure <mira:thm:non-additivity-of-outer-measure>`, and we can then repeat the argument used there.

__Showing the relevant properties:__
First, observe that $\mu(\emptyset) = 0,$ because $\emptyset$ is an open interval with length $0.$
Now, $\mu$ has the order preserving property, bevause if $A \subseteq B \subseteq \mathbb{R},$ then $\mu(A) \subseteq \mu(B),$ because considering the sequence $A, B \setminus A, \emptyset, \emptyset, \ldots$ and applying property (c), we arrive at

$$\mu(B) = \mu(A) + \mu(B \setminus A) + 0 + 0 + \ldots = \mu(A) + \mu(B \setminus A) \geq \mu(A).$$

In addition, if $a, b \in \mathbb{R}$ with $a < b,$ then 

$$(a, b) \subseteq [a, b] \subseteq (a - \epsilon, b + \epsilon)$$

for every $\epsilon > 0,$ so

$$\mu((a, b)) \leq \mu([a, b]) \leq \mu((a - \epsilon, b + \epsilon)) = b - a + 2\epsilon,$$

and since $\epsilon > 0$ is arbitrary, this implies that 

$$\mu([a, b]) = b - a.$$ (mira:eq:mu-of-closed-interval)

Finally, if $A_1, A_2, \ldots$ is a sequence of disjoint subsets of $\mathbb{R},$ then

$$A_1, A_2 \setminus A_1, A_3 \setminus (A_1 \cup A_2), \ldots$$

is a sequence of disjoint subsets of $\mathbb{R},$ so by property (c), we have

$$\begin{align}
\mu\left( \bigcup_{k=1}^\infty A_k \right) &= \mu\left( A_1 \cup (A_2 \setminus A_1) \cup (A_3 \setminus (A_1 \cup A_2)) \cup \ldots \right) \\
&= \mu(A_1) + \mu(A_2 \setminus A_1) + \mu(A_3 \setminus (A_1 \cup A_2)) + \cdots \\
&\leq \sum_{k=1}^\infty \mu(A_k).
\end{align}$$ (mira:eq:mu-is-countably-subadditive)

Therefore $\mu$ is countably subadditive.

__Repeating the argument:__
Now, define the set $V$ in the same way that it was defined in the proof of the {prf:ref}`nonadditivity of the outer measure <mira:thm:non-additivity-of-outer-measure>`.
Specifically, let $\sim$ be the equivalence relation such that for $x, y \in [-1, 1]$ we have $x \sim y$ if $x$ and $y$ differ by a rational number.
Let $V$ be the set which contains exactly one representative from each equivalence clss of $\sim.$
Let $r_1, r_2, \ldots$ be a sequence that contains each rational number in $[-2, 2]$ exactly once.
Then, by properties {eq}`mira:eq:mu-of-closed-interval` and {eq}`mira:eq:mu-is-countably-subadditive` of $\mu,$ as well as the translation invariance of $\mu$, property (d), we have

$$2 = \mu([-1, 1]) \leq \mu\left(\bigcup_{k = 1}^\infty r_k + V\right) = \sum_{k=1}^\infty \mu(r_k + V) = \sum_{k=1}^\infty \mu(V)$$

Thus $\mu(V) > 0.$
Now, note that the sets $(r_1 + V), (r_2 + V), \ldots, (r_K + V)$ are disjoint for any $K \in \mathbb{Z}^+.$
Note also that for any $K \in \mathbb{Z}^+,$ we have

$$ \bigcup_{k=1}^K (r_k + V) \subseteq [-3, 3] \implies \mu\left( \bigcup_{k=1}^K (r_k + V) \right) \leq 6.$$

Now, using the additivity and the translation invariance of $\mu$, properties (c) and (d), we have 

$$\mu\left( \bigcup_{k=1}^K (r_k + V) \right) = \sum_{k=1}^K \mu(r_k + V) = K \mu(V) < 6,$$

reaching a contradiction, because $|V| > 0,$ so the above inequality cannot hold for any $K.$
:::


### Sigma algebras

{prf:ref}`mira:thm:nonexistence-of-extension-of-length-to-all-subsets-of-r` shows that there does not exist a notion of length that satisfies all four intuitive properties that we would like length to satisfy.
We therefore need to relax at least one of these properties to proceed.
We cannot relax (b), because we want all open intervals to have the length one would expect.
We also cannot give up (c), because we want length to be additive.
Finally, we cannot give up (d) either, because we want length to be translation invariant.
Therefore, our only option is to relax (a).
This is where $\sigma$-algebras come in: instead of using all subsets of $\mathbb{R}$ as the domain of $\mu,$ we will restrict the domain to be a certain collection of subsets, which circumvents the issue of non-measurable sets.

:::{prf:definition} $\sigma$-algebra
:label: mira:def:sigma-algebra

Suppose $X$ is a set and $S$ is a set of subsets of $X.$
Then $S$ is called a $\sigma$-algebra on $X$ if it satisfies:

- $\emptyset \in S,$
- if $E \in S,$ then $X \setminus E \in S,$
- if $E_1, E_2, \ldots$ is a sequnece of elements of $S,$ then $\bigcup_{k=1}^\infty E_k \in S.$

:::

From this definition, a number of basic properties of $\sigma$ algebras follow immediately.

:::{prf:theorem} Other properties of $\sigma$-algebras
Suppose $S$ is a $\sigma$-algebra on a set $X.$
Then

(a) $X \in S,$

(b) if $D, E \in S,$ then $D \cup E \in S, D \cap E \in S$ and $D \setminus E \in S,$

(c) if $E_1, E_2, \ldots$ is a sequence of elements of $S,$ then $\cap_{k = 1}^\infty E_k \in S.$
:::

:::{dropdown} Proof: Other properties of $~\sigma$-algebras
Because $\emptyset \in S$ and $X = X \setminus \emptyset,$ we have $X \in S.$
Suppose $D, E \in S.$
Then $D \cup E \in S$ because this is the union of the sequence $D, E, \emptyset, \emptyset, \ldots \in S.$
In addition,

$$D \cap E = X \setminus ((X \setminus D) \cup (X \setminus E)) \in S,$$

and also $D \setminus (X \setminus E) = D \cap E \in S.$
Lastly, if $E_1, E_2, \ldots$ is a sequence of elements of $S,$ then

$$\bigcap_{k=1}^\infty E_k = X \setminus \bigcup_{k=1}^\infty (X \setminus E_k) \in S.$$
:::


We will later define measures, which will be functions that take values on $\sigma$-algebras over sets rather than entire powersets.
The fact that $\sigma$-algebras are closed under complements, as well as countable unions and intersections will allow us to prove useful theorems about limits of measures.
For this, we first define measurable spaces and measurable sets.

:::{prf:definition} Measurable space, measurable set
:label: mira:def:measurable-space-measurable-set
A measurable space is an ordered pair $(X, S),$ where $X$ is a set and $S$ is a $\sigma$-algebra on $X.$
An element of $S$ is called a $S$-measurable set, or simply a measurable set if $S$ is clear from the context.
:::

One very useful theorem for proving results about $\sigma$-algebras is that given a set $X$ and a set of subsets of $X,$ say $A,$ the intersection of all $\sigma$-algebras on $X$ that contain $A$ is also a sigma algebra.

:::{prf:theorem} Smallest $\sigma$-algebra containing a collection of subsets
Suppose $X$ is a set and $A$ is a set of subsets of $X.$
Then, the intersection of all $\sigma$-algebras on $X$ that contain $A$ is a $\sigma$-algebra on $X.$
:::

:::{dropdown} Proof: Smallest $~\sigma$-algebra containing a collection of subsets
There is at least one $\sigma$-algebra on $X$ that contains $A,$ because the power set of $X$ is a $\sigma$-algebra on $X$ that contains $A.$
Let $S$ be the intersection of all $\sigma$-algebras on $X$ that contain $A.$

First, $\emptyset \in S,$ because $\emptyset$ is in every $\sigma$-algebra on $X.$

Second, if $E \in S,$ then $E$ is in every $\sigma$-algebra on $X$ that contains $A,$ so $X \setminus E$ is in every $\sigma$-algebra on $X$ that contains $A,$ so $X \setminus E \in S.$

Third, if $E_1, E_2, \ldots$ is a sequence of elements of $S,$ then $E_1, E_2, \ldots$ is a sequence of elements of every $\sigma$-algebra on $X$ that contains $A,$ so $\bigcup_{k=1}^\infty E_k$ is in every $\sigma$-algebra on $X$ that contains $A,$ so $\bigcup_{k=1}^\infty E_k \in S.$
:::

The intersection of all $\sigma$-algebras containing a collection of sets $A$ is sometimes also referred to as the $\sigma$-algebra generated by $A.$
We now come to the definition of an important $\sigma$-algebra, the Borel $\sigma$-algebra over $\mathbb{R}.$
This is the $\sigma$-algebra generated by the open subsets of $\mathbb{R}.$

:::{prf:definition} Borel set
:label: mira:def:borel-set
The smallest $\sigma$-algebra on $\mathbb{R}$ that contains all the open subsets of $\mathbb{R}$ is called the collection of Borel subsets on $\mathbb{R}.$
An element of this $\sigma$-algebra is called a {prf:ref}`Borel set<mira:def:borel-set>`.
:::

Before moving to measurable functions, we will define inverse images of functions.

:::{prf:definition} Inverse image
If $f: X \in Y$ is a function and $A \subseteq Y,$ then the inverse image of $A$ under $f$ is defined by

$$f^{-1}(A) = \{ x \in X : f(x) \in A \}.$$
:::

We now prove certain useful properties that inverse images have
This will allow us to prove some very useful results about measurable functions.

:::{prf:theorem} Algebra of inverse images

Suppose $f: X \to Y$ is a function.
Then

(a) $f^{-1}(Y \setminus A) = X \setminus f^{-1}(A)$ for all $A \subseteq Y,$

(b) $f^{-1}(\cup_{A \in \mathcal{A}} A) = \cup_{A \in \mathcal{A}} f^{-1}(A)$ for all $\mathcal{A} \subseteq \mathcal{P}(Y),$

(c) $f^{-1}(\cap_{A \in \mathcal{A}} A) = \cap_{A \in \mathcal{A}} f^{-1}(A)$ for all $\mathcal{A} \subseteq \mathcal{P}(Y).$

:::

:::{dropdown} Proof: Algebra of inverse images

__Part (a):__
Suppose $A \subseteq Y.$
For $x \in X$ we have

$$\begin{align}
x \in f^{-1}(Y \setminus A) &\iff f(x) \in Y \setminus A \\
&\iff f(x) \notin A \\
&\iff x \notin f^{-1}(A) \\
&\iff x \in X \setminus f^{-1}(A).
\end{align}$$

Thus $f^{-1}(Y \setminus A) = X \setminus f^{-1}(A).$

__Part (b):__
Suppose $\mathcal{A} \subseteq \mathcal{P}(Y).$
Then

$$\begin{align}
x \in f^{-1}\left(\bigcup_{A \in \mathcal{A}} A\right) &\iff f(x) \in \bigcup_{A \in \mathcal{A}} A \\
&\iff f(x) \in A \text{ for some } A \in \mathcal{A} \\
&\iff x \in f^{-1}(A) \text{ for some } A \in \mathcal{A} \\
&\iff x \in \bigcup_{A \in \mathcal{A}} f^{-1}(A).
\end{align}$$

Thus $f^{-1}\left(\bigcup_{A \in \mathcal{A}} A\right) = \bigcup_{A \in \mathcal{A}} f^{-1}(A).$


__Part (c):__
Suppose $\mathcal{A} \subseteq \mathcal{P}(Y).$
Then

$$\begin{align}
x \in f^{-1}\left(\bigcap_{A \in \mathcal{A}} A\right) &\iff f(x) \in \bigcap_{A \in \mathcal{A}} A \\
&\iff f(x) \in A \text{ for all } A \in \mathcal{A} \\
&\iff x \in f^{-1}(A) \text{ for all } A \in \mathcal{A} \\
&\iff x \in \bigcap_{A \in \mathcal{A}} f^{-1}(A).
\end{align}$$

Thus $f^{-1}\left(\bigcap_{A \in \mathcal{A}} A\right) = \bigcap_{A \in \mathcal{A}} f^{-1}(A).$

:::


:::{prf:theorem} Inverse image of a composition

Suppose $f: X \to Y$ and $g: Y \to Z$ are functions.
Then

$$(g \circ f)^{-1}(A) = f^{-1}(g^{-1}(A))$$

for all $A \subseteq Z.$

:::

:::{dropdown} Proof: Inverse image of a composition

Suppose $A \subseteq Z.$
For $x \in X$ we have

$$\begin{align}
x \in (g \circ f)^{-1}(A) &\iff (g \circ f)(x) \in A \\
&\iff g(f(x)) \in A \\
&\iff f(x) \in g^{-1}(A) \\
&\iff x \in f^{-1}(g^{-1}(A)).
\end{align}$$

Thus $(g \circ f)^{-1}(A) = f^{-1}(g^{-1}(A)).$

:::




### Measurable functions
Now we introduce measurable functions.
As the name suggests, measurable functions are functions such that the inverse images of Borel sets under these functions are measurable sets.

:::{prf:definition} Measurable function
:label: mira:def:measurable-function
Suppose $(X, S)$ is a measurable space.
A function $f: X \to \mathbb{R}$ is called $S$-measurable if

$$f^{-1}(B) \in S$$

for all Borel sets $B \subseteq \mathbb{R}.$
:::

One important kind of function is the characteristic function, a function which is equal to one on a given set and zero everywhere else.

:::{prf:defintion} Characteristic function
Suppose $E$ is a subset of a set $X.$
The characteristic function of $E$ is the function $\chi_E: X \to \mathbb{R}$ defined by

$$\chi_E(x) = \begin{cases} 1 & \text{if } x \in E \\ 0 & \text{if } x \notin E. \end{cases}$$
:::

## Conditions for measurable functions
Now we show one very useful result on measurable functions.
Naively showing a function to be measurable would be tricky because we would have to check that the inverse image of any Borel set under the function is measurable.
Since there are lots of Borel sets, this approach would not be possible.
The following result gives a sufficient condition for a function to be measurable, which is far easier to work with.


:::{prf:theorem} Condition for measurable function
:label: mira:thm:condition-measurable
Suppose $(X, S)$ is a measurable space and $f: X \to \mathbb{R}$ is a function such that

$$f^{-1}((a, \infty)) \in S$$

for all $a \in \mathbb{R}.$
Then $f$ is $S$-{prf:ref}`measurable<mira:def:measurable-function>`.
:::

:::{dropdown} Proof: Condition for measurable function

Consider the set

$$T = \{A \subseteq \mathbb{R} : f^{-1}(A) \in S \}.$$

We will show that every {prf:ref}`Borel subset<mira:def:borel-set>` of $\mathbb{R}$ is in $T.$
To do this, we will first show that $T$ is a $\sigma$-algebra on $\mathbb{R}.$
Then, we will show that $T$ contains all the open intervals of $\mathbb{R},$ which will imply that $T$ contains all the Borel subsets of $\mathbb{R}.$

__$T$ is a $\sigma$-algebra on $\mathbb{R}$:__
First, $\emptyset \in T,$ because $f^{-1}(\emptyset) = \emptyset \in S.$
Second, if $A \in T,$ then $f^{-1}(A) \in S,$ so $f^{-1}(X \setminus A) = X \setminus f^{-1}(A) \in S,$ so $X \setminus A \in T.$
Third, if $A_1, A_2, \ldots \in T,$ then $f^{-1}(A_1), f^{-1}(A_2), \ldots \in S,$ so 

$$f^{-1}\left(\bigcup_{k=1}^\infty A_k\right) = \bigcup_{k=1}^\infty f^{-1}(A_k) \in S,$$

so $\cup_{k=1}^\infty A_k \in T.$
Thus $T$ is a $\sigma$-algebra on $\mathbb{R}.$

__Every open interval is in $T$:__
By the hypothesis in the theorem statement, it follows that $f^{-1}((a, \infty)) \in S$ for all $a \in \mathbb{R},$ so $(a, \infty) \in T$ for all $a \in \mathbb{R}.$
Since $T$ is a $\sigma$-algebra on $\mathbb{R},$ it is closed under complementation and intersection so $(-\infty, b] \in T$ for all $b \in \mathbb{R},$ and $(a, b) \in T$ for all $a, b \in \mathbb{R}.$
Therefore $T$ contains all the open intervals of $\mathbb{R},$ so $T$ contains all the Borel subsets of $\mathbb{R}.$
:::


## Properties of measurable functions
In the special case that $X$ is a subset of $\mathbb{R}$ and $S$ is the set of Borel subsets of $\mathbb{R},$ we use the term Borel measurable to refer to $S$-measurable functions.

:::{prf:definition} Borel measurable function
:label: mira:def:borel-measurable-function
Suppose $X \subseteq \mathbb{R}.$
A function $f: X \to \mathbb{R}$ is called Borel measurable if $f^{-1}(B)$ is a {prf:ref}`Borel set<mira:def:borel-set>` for every Borel set $B \subseteq \mathbb{R}.$
:::

Now we prove a number a few results on sufficient conditions for Borel measurable functions.

:::{prf:theorem} Every continuous function is Borel measurable
Every continuous real-valued function defined on a {prf:ref}`Borel subset<mira:def:borel-set>` of $\mathbb{R}$ is a {prf:ref}`Borel measurable function<mira:def:borel-measurable-function>`.
:::

:::{dropdown} Proof: Every continuous function is Borel measurable
Suppose that $X \subseteq \mathbb{R}$ is a {prf:ref}`Borel set<mira:def:borel-set>` and $f: X \to \mathbb{R}$ is a Borel measurable function.
Suppose $a \in \mathbb{R}.$
If $x \in X$ such that $f(x) > a,$ then by the continuity of $f,$ there exists $\delta_x > 0$ such that $f(y) > a$ for all $y \in (x - \delta_x, x + \delta_x).$
Thus, we have

$$\begin{equation}
f^{-1}((a, \infty)) = \left( \bigcup_{x \in f^{-1}((a, \infty))} (x - \delta_x, x + \delta_x) \right) \cap X.
\end{equation}$$

The above union is a union of open sets, which is therefore also open, so its intersection with $X$ is a Bore set.
By our earlier {prf:ref}`condition for measurable functions<mira:thm:condition-measurable>`, $f$ is Borel measurable.
:::


:::{prf:defintion} Increasing function; strictly increasing function
Suppose $X \subseteq \mathbb{R}$ and $f: X \to \mathbb{R}$ is a function.
Then $f$ is called increasing if $f(x) \leq f(y)$ for all $x, y \in X$ with $x < y.$
If $f(x) < f(y)$ for all $x, y \in X$ with $x < y,$ then $f$ is called strictly increasing.
:::


:::{prf:theorem} Every increasing function is Borel measurable
Every increasing function defined on a {prf:ref}`Borel subset<mira:def:borel-set>` of $\mathbb{R}$ is a Borel measurable function.
:::

:::{dropdown} Proof: Every increasing function is Borel measurable
Suppose that $X \subseteq \mathbb{R}$ is a {prf:ref}`Borel set<mira:def:borel-set>` and $f: X \to \mathbb{R}$ is an increasing function.
Suppose $a \in \mathbb{R}.$
Let $b = \inf f^{-1}((a, \infty)).$
Then

$$f^{-1}((a, \infty)) = (b, \infty) \cap X \text{ or } f^{-1}((a, \infty)) = [b, \infty) \cap X$$

holds.
Since $X$ is a Borel set, and both $(b, \infty)$ and $[b, \infty)$ are Borel sets, it follows that $f^{-1}((a, \infty))$ is a {prf:ref}`Borel set<mira:def:borel-set>`.
By our earlier {prf:ref}`condition for measurable functions<mira:thm:condition-measurable>`, $f$ is Borel measurable.
:::

:::{prf:theorem} Composition of measurable functions
Suppose $(X, S)$ is a measurable space and $f: X \to \mathbb{R}$ is a measurable function.
Suppose that $g$ is a real-valued {prf:ref}`Borel measurable function<mira:def:borel-measurable-function>` defined on a subset of $\mathbb{R}$ that includes the range of $f.$
Then $g \circ f: X \to \mathbb{R}$ is a measurable function.
:::

:::{dropdown} Proof: Composition of measurable functions
Suppose $(X, S)$ is a measurable space and $f: X \to \mathbb{R}$ is a measurable function.
Suppose that $g$ is a real-valued Borel measurable function defined on a subset of $\mathbb{R}$ that includes the range of $f.$
Let $B \subseteq \mathbb{R}$ be a {prf:ref}`Borel set<mira:def:borel-set>`.
Because $g$ is a Borel measurable function, and $B$ is a Borel set, $g^{-1}(B)$ is also a Borel set.
Because $f$ is a measurable function, and $g^{-1}(B)$ is a Borel set, $f^{-1}(g^{-1}(B))$ is in $S,$ so $g \circ f$ is Borel measurable.
:::

Measurable functions also satisfy intuitive algebraic properties that are very useful for proving measurability.

:::{prf:theorem} Algebraic operations with measurable functions
Suppose $(X, S)$ is a measurable space and $f, g: X \to \mathbb{R}$ are $S$-{prf:ref}`measurable<mira:def:measurable-function>` functions.
Then

(a) $f + g, f - g, f g$ are $S$-measurable functions,

(b) if $g(x) \neq 0$ for all $x \in X,$ then $f / g$ is a $S$-measurable function.
:::

:::{dropdown} Proof: Algebraic operations with measurable functions
Suppose $(X, S)$ is a measurable space and $f, g: X \to \mathbb{R}$ are $S$-measurable functions.

__Part (a):__
Fix $a \in \mathbb{R}.$
We will first show that

$$(f + g)^{-1}((a, \infty)) = \bigcup_{q \in \mathbb{Q}} \left( f^{-1}((q, \infty)) \cap g^{-1}((a - q, \infty)) \right) \in S.$$

Suppose $x \in (f+g)^{-1}((a, \infty)).$
Then $f(x) + g(x) > a,$ so the open interval $(a - g(x), f(x))$ is non-empty, and thus it contains a rational number $q.$
This implies that $q < f(x)$ and $a - q < g(x),$ so $x \in f^{-1}((q, \infty)) \cap g^{-1}((a - q, \infty)).$
So $x$ is in the right hand side of the equation above.
Conversely, if $x \in \left( f^{-1}((q, \infty)) \cap g^{-1}((a - q, \infty)) \right)$ for some $q \in \mathbb{Q},$ then $f(x) > q$ and $g(x) > a - q,$ so $f(x) + g(x) > a,$ so $x \in (f + g)^{-1}((a, \infty)).$
We conclude that $(f + g)^{-1}((a, \infty))$ is a countable union of intersections of pairs of Borel sets, so it is a Borel set, so $f + g$ is a Borel measurable function.

Noting that if $g$ is a Borel measurable function, then $-g$ is also a Borel measurable function, we have that $f - g = f + (-g)$ is a Borel measurable function.
To show that $fg$ is a Borel measurable function, consider that

$$fg = \frac{(f+g)^2 - f^2 - g^2}{2},$$

and that $(f+g)^2, f^2, g^2$ are all Borel measurable functions because they are compositions of Borel measurable functions with the function $s: \mathbb{R} \to \mathbb{R}$ where $s(x) = x^2,$ which is a Borel measurable function.
Therefore, also considering that halfing is a Borel measurable function, we have that $fg$ is a Borel measurable function.

__Part (b):__
Suppose $g(x) \neq 0$ for all $x \in X.$
Note that the function $r: \mathbb{R} \setminus \{0\} \to \mathbb{R}$ defined by $r(x) = 1/x$ is a Borel measurable function, because it is continuous on its domain.
Then $1/g = r \circ g$ is a composition of Borel measurable functions, so it is a Borel measurable function.
Lastly, $f/g$ is a product of two Borel measurable functions, $f$ and $1 / g,$ so it is a Borel measurable function.
:::

We now prove a very useful result, namely that pointwise limits of measurable functions are measurable.
This is a highly desirable property, and perhaps somewhat surprising that it holds: recall that the pointwise limit of Riemann integrable functions on some interval is not closed under taking pointwise limits.

:::{prf:theorem} Pointwise limit of $S$-measurable functions is $S$-measurable
Suppose $(X, S)$ is a measurable space and $f_1, f_2, \ldots$ are $S$-{prf:ref}`measurable<mira:def:measurable-function>` functions from $X$ to $\mathbb{R}.$
Suppose $\lim_{k \to \infty} f_k(x)$ exists for each $x \in X.$
Define $f: X \to \mathbb{R}$ by

$$f(x) = \lim_{k \to \infty} f_k(x).$$

Then $f$ is a $S$-measurable function.
:::

:::{dropdown} Proof: Pointwise limit of $~S$-measurable functions is $~S$-measurable
Suppose $(X, S)$ is a measurable space and $f_1, f_2, \ldots$ are $S$-measurable functions from $X$ to $\mathbb{R}.$
Suppose $\lim_{k \to \infty} f_k(x)$ exists for each $x \in X.$
Define $f: X \to \mathbb{R}$ by

$$f(x) = \lim_{k \to \infty} f_k(x).$$

Suppose $a \in \mathbb{R}.$
We will show that

$$f^{-1}((a, \infty)) = \bigcup_{j = 1}^\infty \bigcup_{m = 1}^\infty \bigcap_{k = m}^\infty f_k^{-1}\left( \left(a + \frac{1}{j}, \infty \right) \right).$$

Suppose $x \in f^{-1}((a, \infty)).$
Then $f(x) > a,$ so there exists $j \in \mathbb{Z}^+$ such that $f(x) > a + 1/j.$
Then, by the definition of limits, there exists $m \in \mathbb{Z}^+$ such that $f_k(x) > a + 1/j$ for all $k \geq m.$
Thus $x$ is in the right hand side of the equation above.
Conversely, suppose $x$ is in the right hand side of the equation above.
Then there exists $j \in \mathbb{Z}^+$ and $m \in \mathbb{Z}^+$ such that $f_k(x) > a + 1/j$ for all $k \geq m.$
Taking the limit as $k \to \infty,$ we have $f(x) \geq a + 1/j > a,$ so $x \in f^{-1}((a, \infty)).$

We conclude that $f^{-1}((a, \infty))$ is a Borel set and by our earlier {prf:ref}`condition for measurable functions<mira:thm:condition-measurable>`, $f$ is a Borel measurable function.
:::

Sometimes, we may need to consider functions which take values in $[-\infty, \infty].$
We therefore extend the notion of Vorel sets to subsets of $[-\infty, \infty]$ in the following way.

:::{prf:definition} Borel subsets of $[-\infty, \infty]$
A subset of $[-\infty, \infty]$ is called a {prf:ref}`Borel subset<mira:def:borel-set>` if its intersection with $\mathbb{R}$ is a {prf:ref}`Borel set<mira:def:borel-set>`.
:::

With the above definition in place, we can also extend the definition of measurable functions.

:::{prf:definition} Measurable function on $[-\infty, \infty]$
:label: mira:def:measurable-function-infinity
Suppose $(X, S)$ is a measurable space.
A function $f: X \to [-\infty, \infty]$ is $S$-{prf:ref}`measurable<mira:def:measurable-function>` if

$f^{-1}(B) \in S$

for every Borel set $B \subseteq [-\infty, \infty].$
:::

The following result is the counterpart of our earlier {prf:ref}`sufficient condition for measurability<mira:thm:condition-measurable>`, but with infinities included in the range of the function.

:::{prf:theorem} Sufficient condition for measurable function
:label: mira:thm:sufficient-condition-measurable-with-infinity
Suppose $(X, S)$ is a measurable space and $f: X \to [-\infty, \infty]$ is a function such that

$$f^{-1}((a, \infty]) \in S$$

for all $a \in \mathbb{R}.$
Then $f$ is $S$-{prf:ref}`measurable<mira:def:measurable-function>`.
:::

:::{dropdown} Proof: Sufficient condition for measurable function
Suppose $(X, S)$ is a measurable space and $f: X \to [-\infty, \infty]$ is a function such that

$$f^{-1}((a, \infty]) \in S$$

for all $a \in \mathbb{R}.$
Note that

$$f^{-1}(\{\infty\}) = \bigcap_{n=1}^\infty f^{-1}((n, \infty]) \in S,$$

and also similarly $f^{-1}(\{-\infty\}) \in S.$
From these it follows that

$$f^{-1}((a, \infty)) = f^{-1}((a, \infty]) \setminus f^{-1}(\{\infty\}) \in S \text{ for all } a \in \mathbb{R}.$$

Let $B$ be a Borel set in $[-\infty, \infty].$
From our earlier {prf:ref}`condition for measurable functions<mira:thm:condition-measurable>`, it follows that $f^{-1}(B \cap \mathbb{R}) \in S$ for any Borel set $B \subseteq [-\infty, \infty].$
We therefore have

$$\begin{align}
f^{-1}(B) &= f^{-1}((B \cap \mathbb{R}) \cup (B \cap \{\infty\}) \cup (B \cap \{-\infty\})) \\
&= f^{-1}(B \cap \mathbb{R}) \cup f^{-1}(\{\infty\}) \cup f^{-1}(\{-\infty\}) \in S
\end{align}$$

so $f$ is $S$-measurable.
:::

Concluding this section, we show that pointwise infimuma and pointwise supremuma of measurable functions are measurable.
Note that this result would not have made sense before modifying the {prf:ref}`definition of measurability to include infinity<mira:def:measurable-function-infinity>`, because the supremum and infimum can be $\infty$ and $- \infty.$

:::{prf:theorem} Infimum and supremum of a sequence of measurable functions is measurable
Suppose $(X, S)$ is a measurable space and $f_1, f_2, \ldots$ is a sequence of $S$-{prf:ref}`measurable<mira:def:measurable-function>` functions from $X$ to $[-\infty, \infty].$
Define $g, h: X \to [-\infty, \infty]$ by

$$g(x) = \inf\{f_k(x) : k \in \mathbb{Z}^+\} \text{ and } h(x) = \sup\{f_k(x) : k \in \mathbb{Z}^+\}.$$

Then $g$ and $h$ are $S$-{prf:ref}`measurable<mira:def:measurable-function>` functions.
:::

:::{dropdown} Proof: Infimum and supremum of a sequence of measurable functions is measurable
Let $a \in \mathbb{R}.$
The definition of the supremum implies that

$$h^{-1}((a, \infty]) = \bigcup_{k=1}^\infty f_k^{-1}((a, \infty]) \in S,$$

which, together with the earlier {prf:ref}`sufficient condition for measurable function<mira:thm:sufficient-condition-measurable-with-infinity>`, implies that $h$ is $S$-measurable, that is, the supremum of a sequence of measurable functions is measurable.
Now, note that

$$g(x) = -\sup\{-f_k(x) : k \in \mathbb{Z}^+\},$$

so $g$ is the supremum of a sequence of measurable functions, and is therefore measurable.
Therefore, the infimum of a sequence of measurable functions is measurable.
:::



## Measures and their properties

Now we come to the definition of measures.
Our original motivation for the following definition came from trying to extend the notion of the length of an interval to the length of more general sets.
However, the following definition is allows us to generalise a notion of size to other contexts, such as areas or volumes and beyond.

:::{margin}
The word *measure* allows us to use a single word for different notions of size such as length, area or volume.
:::


:::{prf:definition} Measure
:label: mira:def:measure
Suppose $X$ is a set and $S$ is a $\sigma$-algebra on $X.$
A measure on $(X, S)$ is a function $\mu: S \to [0, \infty]$ such that $\mu(\emptyset) = 0$ and $\mu$ is countably additive, that is

$$\mu\left( \bigcup_{k=1}^\infty E_k \right) = \sum_{k=1}^\infty \mu(E_k)$$

for every disjoint sequence $E_1, E_2, \ldots$ of sets in $S.$
:::


Countable additivity of measures is a key property that allows us to prove useful limit theorems.
Note that countable additvity implies finite additivity, that is, if $\mu$ is a measure on $(X, S)$ and $E_1, \ldots, E_n$ are disjoint sets in $S,$ then

$$\mu(E_1 \cup \cdots \cup E_n) = \mu(E_1) + \cdots + \mu(E_n).$$

The following terminology is often very useful.


:::{prf:definition} Measure space
A measure space is an ordered triple $(X, S, \mu),$ where $X$ is a set, $S$ is a $\sigma$-algebra on $X$ and $\mu$ is a measure on $(X, S).$
:::


### Properties of measures

Now we discuss several useful properties of measures.

:::{prf:theorem} Measure preserves order; measure of a set difference
:label: mira:thm:measure-preserves-order
Suppose $(X, S, \mu)$ is a measure space and $D, E \in S$ with $D \subseteq E.$
Then

(a) $\mu(D) \leq \mu(E),$

(b) $\mu(E \setminus D) = \mu(E) - \mu(D)$ provided that $\mu(D) < \infty.$
:::

:::{dropdown} Proof: Measure preserves order; measure of a set difference
Note that $E = D \cup (E \setminus D)$ is a disjoint union, so by {prf:ref}`countable additivity of measures<mira:def:measure>`, we have

$$\mu(E) = \mu(D) + \mu(E \setminus D) \geq \mu(D),$$

which proves part (a).
If $\mu(D) < \infty,$ then part (b) follows by subtracting $\mu(D)$ from both sides of the equation above.
:::


The countable additivity property of measures applies to disjoint countable unions.
The following countable _subadditivity_ property applies to countable unions that may not be disjoint unions.

:::{prf:theorem} Countable subadditivity
Suppose $(X, S, \mu)$ is a measure space and $E_1, E_2, \ldots \in S.$
Then

$$\mu\left( \bigcup_{k=1}^\infty E_k \right) \leq \sum_{k=1}^\infty \mu(E_k).$$

:::

:::{dropdown} Proof: Countable subadditivity
Suppose $E_1, E_2, \ldots \in S.$
Let $D_1 = \emptyset$ and $D_k = E_1 \cup \cdots \cup E_{k-1}$ for $k \geq 2.$
Then $E_1 \setminus D_1, E_2 \setminus D_2, \ldots$ is a sequence of disjoint sets in $S$ whose union equals $\cup_{k=1}^\infty E_k.$
Therefore

$$\begin{align}
\mu\left( \bigcup_{k=1}^\infty E_k \right) &= \mu\left( \bigcup_{k=1}^\infty (E_k \setminus D_k) \right) \\
&= \sum_{k=1}^\infty \mu(E_k \setminus D_k) \\
&\leq \sum_{k=1}^\infty \mu(E_k).
\end{align}$$

where the second equality follows from {prf:ref}`countable additivity of measures<mira:def:measure>` and the inequality follows from the fact that {prf:ref}`measures preserve order<mira:thm:measure-preserves-order>`.
:::


Just as countable additivity implies finite additivity, countable subadditivity implies finite subadditivity.
That is if $\mu$ is a measure on $(X, S)$ and $E_1, \ldots, E_n$ are sets in $S,$ then

$$\mu(E_1 \cup \cdots \cup E_n) \leq \mu(E_1) + \cdots + \mu(E_n).$$

Now we show two very useful results about limits on measures.
Note that the countable additivity property of measures is crucial for the following results.


:::{prf:theorem} Measure of an increasing union
:label: mira:thm:measure-increasing-union
Suppose $(X, S, \mu)$ is a measure space and $E_1, E_2, \ldots \in S$ is an increasing sequence of sets in $S,$ that is $E_1 \subseteq E_2 \subseteq \cdots.$
Then

$$\mu\left( \bigcup_{k=1}^\infty E_k \right) = \lim_{k \to \infty} \mu(E_k).$$
:::

:::{dropdown} Proof: Measure of an increasing union
If $\mu(E_k) = \infty$ for some $k,$ then the equality holds because both sides are equal to $\infty.$
Let us consider the case where $\mu(E_k) < \infty$ for all $k \in \mathbb{Z}^+.$

For convenience, let $E_0 = \emptyset.$
Then, using the fact that $E_1, E_2, \ldots$ is an increasing sequence of sets, we have

$$\bigcup_{k=1}^\infty E_k = \bigcup_{k=1}^\infty (E_k \setminus E_{k-1}),$$

which is a disjoint union.
Therefore, by {prf:ref}`countable additivity of measures<mira:def:measure>`, we have

$$\begin{align}
\mu\left( \bigcup_{j=1}^\infty E_j \right) &= \mu\left( \bigcup_{j=1}^\infty (E_j \setminus E_{j-1}) \right) \\
&= \lim_{k \to \infty} \sum_{j=1}^k \mu(E_j \setminus E_{j-1}) \\
&= \lim_{k \to \infty} \mu(E_k).
\end{align}$$
:::


Just as with the earlier property we showed about limits of increasing sequences of sets, we also have an analogous result about limits of decreasing sequences of sets.

:::{prf:theorem} Measure of a decreasing intersection
Suppose $(X, S, \mu)$ is a measure space and $E_1, E_2, \ldots \in S$ is a decreasing sequence of sets in $S,$ that is $E_1 \supseteq E_2 \supseteq \cdots,$ with $\mu(E_1) < \infty.$
Then

$$\mu\left( \bigcap_{k=1}^\infty E_k \right) = \lim_{k \to \infty} \mu(E_k).$$
:::

:::{dropdown} Proof: Measure of a decreasing intersection
First, we have that

$$E_1 \setminus \bigcap_{k=1}^\infty E_k = \bigcup_{k=1}^\infty (E_1 \setminus E_k),$$

which is an increasing union and, by {prf:ref}`mira:thm:measure-increasing-union`, we have

$$\mu\left( E_1 \setminus \bigcap_{k=1}^\infty E_k \right) = \lim_{k \to \infty} \mu(E_1 \setminus E_k).$$

Using the countable additivity of measures, we have

$$\begin{align}
\mu\left( \bigcap_{k=1}^\infty E_k \right) &= \mu\left( E_1 \right) - \mu\left(E_1 \setminus \bigcap_{k=1}^\infty E_k \right) \\
&= \mu\left( E_1 \right) - \lim_{k \to \infty} \mu(E_1 \setminus E_k) \\
&= \mu\left( E_1 \right) - \lim_{k \to \infty} (\mu(E_1) - \mu(E_k)) \\
&= \lim_{k \to \infty} \mu(E_k).
\end{align}$$

which proves the result.
:::


We conclude this section with another useful result:
the measure of the union of two sets is the sum of the measures of the sets minus the measure of their intersection, which has been counted twice.

:::{prf:theorem} Measure of the union of two sets
Suppose $(X, S, \mu)$ is a measure space and $D, E \in S.$
Then

$$\mu(D \cup E) = \mu(D) + \mu(E) - \mu(D \cap E).$$
:::

:::{dropdown} Proof: Measure of the union of two sets
We have

$$D \cup E = (D \setminus (D \cap E)) \cup (E \setminus (D \cap E)) \cup (D \cap E),$$

which is a disjoint union.
Therefore, by {prf:ref}`countable additivity of measures<mira:def:measure>`, we have

$$\begin{align}
\mu(D \cup E) &= \mu(D \setminus (D \cap E)) + \mu(E \setminus (D \cap E)) + \mu(D \cap E) \\
&= \mu(D) - \mu(D \cap E) + \mu(E) - \mu(D \cap E) + \mu(D \cap E) \\
&= \mu(D) + \mu(E) - \mu(D \cap E).
\end{align}$$
:::


## Lebesgue measure
:::{margin}
Despite the name "outer measure", the outer measure is not in fact a measure - at least not on all subsets of $\mathbb{R},$ because it is not additive.
Restricting its domain to the set of all subsets of $\mathbb{R}$ gives the Lebesgue measure, which is in fact a measure.
:::
Now we move to define the Lebesgue measure which is central in measure theory.
In short the Lebesgue measure is the modified notion of length we have been building up towards.
Specifically, it will be the outer measure restricted (from the set of all subsets of $\mathbb{R}$) to the Borel sets of $\mathbb{R}.$
The main result in this section will be proving that the outer measure, when restricted to the Borel sets of $\mathbb{R},$ is in fact a measure.

### Additivity of outer measure on Borel sets
The main task for showing that the outer measure is a measure, when restricted to Borel sets, is to show that the outer measure is additive on the borel $\sigma$-algebra.
We break up this proof into intermediate results, including some results that are useful in subsequent chapters.
First, we show that the outer measure is additive if one of the sets is open.

:::{prf:theorem} Additivity of outer measure if one of the sets is open
:label: mira:thm:additivity-of-outer-measure-if-one-set-is-open
Suppose $A$ and $G$ are disjoint subsets of $\mathbb{R}$ and $G$ is open.
Then

$$|A \cup G| = |A| + |G|.$$
:::

:::{dropdown} Proof: additivity of outer measure if one of the sets is open
First, we can assume that $|G| < \infty,$ because otherwise both sides of the equation above are equal to $\infty.$

The {prf:ref}`subadditivity of the outer measure<mira:thm:countable-subadditivity-of-outer-measure>` implies that $|A \cup G| \leq |A| + |G|.$
It therefore remains to show the inequality in the opposite direction.

Consider the special case where $G = (a, b),$ for some $a, b \in \mathbb{R}$ with $a < b.$
Further, we can assume that $a, b \neq A,$ because changing a set by at most two points does not change its outer measure.
Let $I_1, I_2, \dots$ be a sequence of open intervals whose union contains $A \cup G.$
For each $n \in \mathbb{Z}^+,$ let

$$J_n = I_n \cap (-\infty, a), K_n = I_n \cap (a, b), L_n = I_n \cap (b, \infty).$$

From this definition, we have that

$$\ell(I_n) = \ell(J_n) + \ell(K_n) + \ell(L_n).$$

Note that $J_1, L_1, J_2, L_2, \dots$ is a sequence of open intervals whose union contains $A,$ and $K_1, K_2, \dots$ is a sequence of open intervals whose union contains $G.$
Thus

$$\begin{align}
\sum_{n = 1}^\infty \ell(I_n) &= \sum_{n = 1}^\infty (\ell(J_n) + \ell(K_n)) + \sum_{n = 1}^\infty \ell(L_n) \\
&\geq |A| + |G|.
\end{align}$$

This inequality implies that $|A \cup G| = |A| + |G|$ in the special case that $G$ is an open interval.
Using induction on $m$ we conclude that if $m \in \mathbb{Z}^+$ and $G$ is a union of $m$ disjoint open intervals that are all disjoint from $A,$ then $|A \cup G| = |A| + |G|.$
Now, suppose that $G$ is an arbitrary open subset of $\mathbb{R}$ that is disjoint from $A.$
Then $G = \cup_{n=1}^\infty I_n$ for some sequence of disjoint open intervals $I_1, I_2, \dots,$ each of which is disjoint from $A.$
For each $m \in \mathbb{Z}^+$ we have

$$\begin{align}
|A \cup G| &\geq \left| A \cup \left(\bigcup_{n=1}^m I_n \right) \right| \\
&\geq |A| + \sum_{n=1}^m \ell(I_n)
\end{align}$$

which in turn implies that

$$\begin{align}
|A \cup G| &\geq |A| + \sum_{n=1}^\infty \ell(I_n) \\
&\geq |A| + |G|
\end{align}$$

completing the proof that $|A \cup G| = |A| + |G|$ for the case of a general open set $G.$
:::

Then we show that the outer measure is additive if one of the sets is closed.

:::{prf:theorem} Additivity of outer measure if one of the sets is closed
Suppose $A$ and $F$ are disjoint subsets of $\mathbb{R}$ and $F$ is closed.
Then

$$|A \cup F| = |A| + |F|.$$
:::

:::{dropdown} Proof: additivity of outer measure if one of the sets is closed
Suppose $I_1, I_2, \dots$ is a sequence of open intervals whose union contains $A \cup F.$
Let $G = \cup_{n = 1}^\infty I_n.$
Then $G$ is an open set which contains $A \cup F.$
Now, note that $G \setminus F = G \cap (\mathbb{R} \setminus F)$ is an intersection of two open sets and is therefore an open set.
Applying our previous result showing that the {prf:ref}`outer measure is additive if one of the sets is open<mira:thm:additivity-of-outer-measure-if-one-set-is-open>` we have that 

$$|G| = |F| + |G \setminus F|.$$

Using the fact that $A \subseteq G \setminus F,$ and the above equation, we have that

$$|G| \geq |F| + |A|.$$

Thaking the infimum over all open covers of $F \cup A,$ we obtain

$$|F \cup A| \geq |F| + |A|,$$

from which we conclude that $|F \cup A| = |F| + |A|.$
:::

Now we turn to a very useful result, which says that any Borel set can be approximated by a closed subset arbitrarily well.

:::{margin}
Note that this result would not hold if we replaced closed sets by open sets.
For example, if $B = [0, 1] \setminus \mathbb{Q},$ then the only open subset of $B$ is the empty set, and thus $B$ cannot be approximated arbitrarily well by open subsets.
:::
:::{prf:theorem} Approximation of Borel sets from below by closed sets
:label: mira:thm:approximation-of-borel-sets-from-below-by-closed-sets
Suppose $B \subseteq \mathbb{R}$ is a {prf:ref}`Borel set<mira:def:borel-set>`.
Then, for every $\epsilon > 0,$ there exists a closed set $F \subseteq B$ such that $|B \setminus F| < \epsilon.$
:::

:::{dropdown} Proof: approximation of Borel sets from below by closed sets
Consider the set

$$\mathcal{L} = \{D \subseteq \mathbb{R}: \text{ for every } \epsilon > 0, \text{ there exists a closed set } F \subseteq D \text{ such that } |D \setminus F| < \epsilon \}.$$

This is the set of all subsets of $\mathbb{R}$ which can be approximated below with closed sets.
Our approach to proving the result will be to show that $\mathcal{L}$ is a $\sigma$-algebra.
Then, noting that $\mathcal{L}$ contains all closed subsets of $\mathbb{R},$ by taking complements we conclude that it must contain all open subsets of $\mathbb{R},$ so it also contains every {prf:ref}`Borel subset<mira:def:borel-set>` of $\mathbb{R},$ which will complete the proof.

To show that $\mathcal{L}$ is a $\sigma$-algebra, we will first show that it is closed under countable intersections.
Suppose $D_1, D_2, \dots \subseteq \mathcal{L}.$
Let $\epsilon > 0.$
For each $k \in \mathbb{Z}^+,$ there exists a closed set $F_k$ such that

$$F_k \subseteq D_k \text{ and } |D_k \setminus F_k| < \frac{\epsilon}{2^k}.$$

Thus $\cap_{k=1}^\infty F_k$ is a closed set and

$$\begin{align}
\left(\bigcap_{n = 1}^\infty D_k\right) \setminus \left(\bigcap_{n = 1}^\infty F_k\right) \subseteq \bigcup_{n = 1}^\infty (D_k \setminus F_k)
\end{align}$$

from which it follows that 

$$\begin{align}
\left|\left(\bigcap^\infty_{n = 1} D_k\right) \setminus \left(\bigcap^\infty_{n = 1} F_k\right) \right| < \epsilon.
\end{align}$$

Thus $\cap_{n=1}^\infty D_k \in \mathcal{L},$ proving that $\mathcal{L}$ is closed under countable intersections.
Now we turn to proving that $\mathcal{L}$ is closed under complementation.
Suppose $D \in \mathcal{L}$ and $\epsilon > 0.$
We will first consider the case $|D| < \infty.$
Let $F \subseteq D$ be a closed set such that $|D \setminus F| < \frac{\epsilon}{2}.$
The definition of outer measure implies that there exists an open set $G$ such that $D \subseteq G$ and $|G| < |D| + \frac{\epsilon}{2}.$
Therefore we have

$$\begin{equation}
(\mathbb{R} \setminus D) \setminus (\mathbb{R} \setminus G) \subseteq G \setminus F.
\end{equation}$$

Now, the set $G \setminus F$ is open, and using the fact that $|F| > |D| - |D \setminus F|,$ we have

$$\begin{equation}
|G \setminus F| = |G| - |F| < \left(|D| + \frac{\epsilon}{2}\right) - \left(|D| - \frac{\epsilon}{2}\right) = \epsilon,
\end{equation}$$

from which we conclude

$$\begin{equation}
\left|(\mathbb{R} \setminus D)\right| \setminus (\mathbb{R} \setminus G) \leq \epsilon.
\end{equation}$$

Therefore $\mathbb{R} \setminus D$ in the case $|D| < \infty.$
Now, for general $D,$ let $\epsilon > 0$ and define the sets $D_k = D \cap [-k, k]$ for $k \in \mathbb{Z}^+.$
The previous case implies that $\mathbb{R} \setminus D_k \in \mathcal{L}.$
Using the fact that $\mathcal{L}$ is closed under intersections and that

$$\begin{equation}
\mathbb{R} \setminus D = \mathbb{R} \setminus \left(\bigcup_{k=1}^\infty D_k\right) = \bigcap_{n = 1}^\infty (\mathbb{R} \setminus D_k), 
\end{equation}$$

we conclude that $\mathbb{R} \setminus D \in \mathcal{L}.$
Thus $\mathcal{L}$ is a $\sigma$-algebra, which concludes the proof.
:::


:::{prf:theorem} Additivity of the outer measure if one of the sets is Borel
:label: mira:thm:additivity-of-outer-measure-if-one-set-is-borel
Suppose $A$ and $B$ are disjoint subsets of $\mathbb{R}$ and $B$ is a Borel set.
Then

$$|A \cup B| = |A| + |B|.$$
:::

:::{dropdown} Proof: Additivity of the outer measure if one of the sets is Borel
Suppose $A$ and $B$ are disjoint subsets of $\mathbb{R}$ and $B$ is a Borel set.

Let $\epsilon > 0.$
By the previous theorem, there exists a closed $F \subseteq B$ such that $|B \setminus F| < \epsilon.$

By another previous theorem, the outer measure is additive whenever one of the sets is closed.

We therefore have

$$\begin{align}
|A \cup B| &\geq |A \cup F| \\
&= |A| + |F| \\
&= |A| + |B| - |B \setminus F| \\
&= |A| + |B| - \epsilon
\end{align}$$

and since $\epsilon > 0$ was arbitrary, we must have $|A \cup B| = |A| + |B|.$
:::


:::{prf:theorem} Existence of a subset of $\mathbb{R}$ that is not a Borel set
:label: mira:thm:existence-of-a-subset-of-R-that-is-not-a-borel-set
There exists a subset $B \subseteq \mathbb{R}$ such that $B$ is not a Borel set.
:::

:::{dropdown} Proof: existence of a subset of $~\mathbb{R}~$ that is not a Borel set
In the proof of {prf:ref}`mira:thm:nonexistence-of-extension-of-length-to-all-subsets-of-r`, we showed that there exist disjoint $A, B \subseteq \mathbb{R}$ such that $|A \cup B| \neq |A| + |B|.$
Now, it must be the case that $|B| < \infty,$ because otherwise both sides of the equation would be equal to $\infty.$
Now, by {prf:ref}`mira:thm:additivity-of-outer-measure-if-one-set-is-borel`, it must be the case that $B$ is not a Borel set, because otherwise we would have $|A \cup B| = |A| + |B|.$
:::


:::{prf:theorem} Outer measure is a measure on Borel sets
:label: mira:thm:outer-measure-is-a-measure-on-borel-sets
The {prf:ref}`outer measure<mira:def:outer-measure>` is a {prf:ref}`measure<mira:def:measure>` on the {prf:ref}`Borel sets<mira:def:borel-set>` of $\mathbb{R}.$
:::

:::{dropdown} Proof: Outer measure is a measure on Borel sets
The outer measure is a non-negative function with $|\emptyset| = 0.$
It remains to show that the outer measure is countably additive on the Borel sets of $\mathbb{R}.$

Suppose $B_1, B_2, \ldots$ is a sequence of disjoint Borel sets.
For each $K \in \mathbb{Z},$ we have

$$\left|\bigcup_{k=1}^\infty B_k\right| &\geq \left| \bigcup_{k=1}^K B_k \right| = \sum_{k=1}^K |B_k|,$$

where the first inequality follows from the {prf:ref}`order-preserving property of measures<mira:thm:measure-preserves-order>` and the second equality follows from {prf:ref}`additivity of outer measure if one of the sets is Borel<mira:thm:additivity-of-outer-measure-if-one-set-is-borel>`.
Taking the limit as $K \to \infty$ we have

$$\left|\bigcup_{k=1}^\infty B_k\right| \geq \sum_{k=1}^\infty |B_k|.$$

Now, using the {prf:ref}`countable subadditivity of outer measure<mira:thm:countable-subadditivity-of-outer-measure>`, we have

$$\left|\bigcup_{k=1}^\infty B_k\right| \leq \sum_{k=1}^\infty |B_k|.$$

Therefore, we conclude that

$$\left|\bigcup_{k=1}^\infty B_k\right| = \sum_{k=1}^\infty |B_k|,$$

which proves that the outer measure is countably additive on the Borel sets of $\mathbb{R}.$
:::


:::{prf:definition} Lebesgue measure
:label: mira:def:lebesgue-measure
The Lebesgue measure is the measure on the Borel $\sigma$-algebra on $\mathbb{R},$ that assigns to each {prf:ref}`Borel set<mira:def:borel-set>` its {prf:ref}`outer measure<mira:def:outer-measure>`.
:::

Note that this definition is sound because the outer measure is a measure on the Borel sets of $\mathbb{R}$, as shown in {prf:ref}`mira:thm:outer-measure-is-a-measure-on-borel-sets`.
It turns out that the Lebesgue measure is actually a measure on a larger class of sets called the Lebesgue measurable sets.

:::{prf:definition} Lebesgue measurable set
:label: mira:def:lebesgue-measurable-set
A set $A \subseteq \mathbb{R}$ is Lebesgue measurable if there exists a Borel set $B$ such that $|A \setminus B| = 0.$
:::

:::{prf:theorem} Equivalent conditions for Lebesgue measurable set
:label: mira:thm:equivalent-conditions-for-lebesgue-measurable-set
Suppose $A \subseteq \mathbb{R}.$
Then the following are equivalent.

1. $A$ is {prf:ref}`Lebesgue measurable<mira:def:lebesgue-measurable-set>`.
2. For each $\epsilon > 0,$ there exists a closed set $F \subseteq A$ such that $|A \setminus F| < \epsilon.$
3. There exist closed sets $F_1, F_2, \ldots$ contained in $A$ such that

$$\left|A \setminus \bigcup_{k=1}^\infty F_k\right| = 0.$$

4. There exists a {prf:ref}`Borel set<mira:def:borel-set>` $B$ such that $|A \setminus B| = 0.$
5. For each $\epsilon > 0,$ there exists an open set $G \supseteq A$ such that $|G \setminus A| < \epsilon.$
6. There exist open sets $G_1, G_2, \ldots$ containing $A$ such that

$$\left|\bigcap_{k=1}^\infty G_k \setminus A\right| = 0.$$

7. There exists a Borel set $B \supseteq A$ such that $|B \setminus A| = 0.$
:::

:::{dropdown} Proof: equivalent conditions for Lebesgue measurable set

__(2) implies (3):__
Suppose (2) holds.
Then, for each $n \in \mathbb{Z}^+,$ there exists a closed set $F_n \subseteq A$ such that $|A \setminus F_n| < \frac{1}{n}.$
Now

$$\begin{align}
A \setminus \bigcup_{k=1}^\infty F_k \subseteq A \setminus F_n
\end{align}$$

for all $n \in \mathbb{Z}^+.$
Therefore $|A \setminus \cup_{k=1}^\infty F_k| \leq |A \setminus F_n| < \frac{1}{n}$ for all $n \in \mathbb{Z}^+.$
Therefore $|A \setminus \cup_{k=1}^\infty F_k| = 0,$ which proves (3).

__(3) implies (4):__
Suppose (3) holds.
Then, there exists a sequence of closed sets $F_1, F_2, \ldots$ such that $F_k \subseteq A$ for all $k \in \mathbb{Z}^+$ and $|A \setminus \cup_{k=1}^\infty F_k| = 0.$
Let $B = \cup_{k=1}^\infty F_k.$
Then $B$ is a Borel set and $|A \setminus B| = 0,$ which proves (4).

__(4) implies (2):__
Suppose (4) holds.
Let $\epsilon > 0.$
Since (4) holds, there exists a Borel set $B$ such that $|A \setminus B| = 0.$
Then, since $B$ is a Borel set, by {prf:ref}`mira:thm:approximation-of-borel-sets-from-below-by-closed-sets`, there exists a closed set $F \subseteq B$ such that $|B \setminus F| < \epsilon.$
Now, since $B$ is a Borel set, so is $B \setminus F.$
Therefore, we have $|A \setminus F| = |A \setminus B| + |B \setminus F| < \epsilon,$ which proves (2).

__(2) implies (5):__
Suppose (2) holds.
Let $\epsilon > 0.$
Define $B = \mathbb{R} \setminus A.$
Then, by (2), there exists a closed set $F \subseteq B$ such that $|B \setminus F| < \epsilon.$
Then $G = \mathbb{R} \setminus F$ is an open set, and it satisfies

$$\begin{equation}
|G \setminus A| = |(\mathbb{R} \setminus F) \setminus A| = |(\mathbb{R} \setminus A) \setminus F| = |B \setminus F| < \epsilon.
\end{equation}$$

Thus $G$ is an open set such that $|G \setminus A| < \epsilon,$ which proves (5).

__(5) implies (6):__
Suppose (5) holds.
Then, for each $n \in \mathbb{Z}^+,$ there exists an open set $G_n$ such that $|G_n \setminus A| < \frac{1}{n}.$
Let $G = \cap_{n=1}^\infty G_n.$
Then $G$ is an open set and $A \subseteq G.$
Therefore, for each $n \in \mathbb{Z}^+,$ we have

$$\begin{align}
|G \setminus A| &\leq |G_n \setminus A| \\
&< \frac{1}{n}.
\end{align}$$

Thus $|G \setminus A| = 0,$ which proves (6).

__(6) implies (7):__
Suppose (6) holds.
Then, there exists a sequence of open sets $G_1, G_2, \ldots$ such that $A \subseteq G_k$ for all $k \in \mathbb{Z}^+$ and $|\cap_{k=1}^\infty G_k \setminus A| = 0.$
Then $B$ is a Borel set and $|B \setminus A| = 0,$ which proves (7).

__(7) implies (2):__
Suppose (7) holds.
Let $\epsilon > 0.$
Since (7) holds, there exists a Borel set $B \subseteq \mathbb{R} \setminus A$ such that $|(\mathbb{R} \setminus A) \setminus B| = 0.$
Then, since $B$ is a Borel set, by {prf:ref}`mira:thm:approximation-of-borel-sets-from-below-by-closed-sets`, there exists a closed set $F \subseteq B$ such that $|B \setminus F| < \epsilon.$
Now, since $B$ is a Borel set, so is $B \setminus F.$
Therefore, we have $|A \setminus F| = |A \setminus B| + |B \setminus F| < \epsilon,$ which proves (2).

__(1) and (4) are equivalent:__
This is the definition of Lebesgue measurable sets {prf:ref}`mira:def:lebesgue-measurable-set`.
:::


:::{prf:theorem} Outer measure is a measure on Lebesgue measurable sets
:label: mira:thm:outer-measure-is-a-measure-on-lebesgue-measurable-sets
* The set $\mathcal{L}$ of Lebesgue measurable sets is a $\sigma$-{prf:ref}`algebra<mira:def:sigma-algebra>` on $\mathbb{R}.$
* The {prf:ref}`outer measure<mira:def:outer-measure>` is a {prf:ref}`measure<mira:def:measure>` on the Lebesgue measurable sets of $\mathbb{R}.$
:::

:::{dropdown} Proof: outer measure is a measure on Lebesgue measurable sets

__Part (a):__
Since (a) and (b) in {prf:ref}`mira:thm:outer-measure-is-a-measure-on-lebesgue-measurable-sets` are equivalent, the set $\mathcal{L}$ of Lebesgue measurable sets is the collection of sets satisfying (b) in {prf:ref}`mira:thm:equivalent-conditions-for-lebesgue-measurable-set`.
As shown in the proof of {prf:ref}`mira:thm:approximation-of-borel-sets-from-below-by-closed-sets`, the set $\mathcal{L}$ is a $\sigma$-algebra.
This proves part (a).

__Part (b):__
We will show that the outer measure is countably additive on the Lebesgue measurable sets of $\mathbb{R}.$
Suppose $A_1, A_2, \ldots$ is a sequence of disjoint Lebesgue measurable sets.
By the {prf:ref}`definition of Lebesgue measurable sets<mira:def:lebesgue-measurable-set>`, there exists a sequence of Borel sets $B_1, B_2, \ldots$ such that $B_k \subseteq A_k$ and $|A_k \setminus B_k| = 0$ for all $k \in \mathbb{Z}^+.$
Then, we have

$$
\left|\bigcup_{k=1}^\infty A_k\right| \geq \left|\bigcup_{k=1}^\infty B_k\right| = \sum_{k=1}^\infty |B_k| = \sum_{k=1}^\infty |A_k| 
$$

where the first equality holds because $B_1, B_2, \ldots$ is a sequence of disjoint Borel sets and the outer measure is countably additive on the Borel sets of $\mathbb{R}$ ({prf:ref}`mira:thm:outer-measure-is-a-measure-on-borel-sets`), and the second equality holds because $|A_k| = |B_k|$ for all $k \in \mathbb{Z}^+.$
Combined with the countable subadditivity of the outer measure, we have

$$\left|\bigcup_{k=1}^\infty A_k\right| = \sum_{k=1}^\infty |A_k|,$$

which shows that the outer measure is countably additive on the Lebesgue measurable sets of $\mathbb{R}.$
:::


We now give another definition of the Lebesgue measure, but this time defined on a different domain.
{prf:ref}`mira:def:lebesgue-measure` defined the Lebesgue measure on the Borel sets of $\mathbb{R},$ whereas {prf:ref}`mira:def:lebesgue-measure-lebesgue-measurable-sets` defines the Lebesgue measure on the Lebesgue measurable sets of $\mathbb{R}.$

:::{prf:definition} Lebesgue measure
:label: mira:def:lebesgue-measure-lebesgue-measurable-sets
The Lebesgue measure is the measure on $(\mathbb{R}, \mathcal{L}),$ where $\mathcal{L}$ is the $\sigma$-algebra of Lebesgue measurable subsets of $\mathbb{R},$ that assigns to each Lebesgue measurable set its outer measure.
:::


## Cantor set and Cantor function

Every countable set has outer measure $0$ ({prf:ref}`mira:thm:countable-sets-have-outer-measure-zero`).
We may ask whether the converse holds:
does each set of outer measure $0$ have to be countable?
The answer is no, and the Cantor set is a counterexample.

:::{prf:definition} Cantor set
:label: mira:def:cantor-set
The Cantor set $C$ is defined as $[0, 1] \setminus \cup_{n=1}^\infty G_n,$ where $G_1 = (\frac{1}{3}, \frac{2}{3})$ and $G_n$ for $n > 1$ is the union of the middle third open intervals in the intervals of $[0, 1] \setminus \cup_{j=1}^{n-1} G_j.$
:::


:::{prf:lemma} Base 3 description of the Cantor set
:label: mira:lem:base-3-description-of-cantor-set
The Cantor set $C$ is the set of all numbers in $[0, 1]$ that have a base 3 representation containing only 0s and 2s.
:::

:::{dropdown} Proof: base 3 description of the Cantor set
Note that the set $G_1$ contains all numbers which have a base 3 representation with a 1 in the first digit, except for the number $1/3 = 0.1_3.$
However, $0.1_3 = 0.0222\ldots_3,$ so this number has a representation containing only 0s and 2s.
Similarly, the set $G_1 \cup G_2$ contains all numbers which have a base 3 representation with a 1 in the first or second digit, except for the numbers $0.1_3, 0.01_3, 0.21_3.$
However, simiarly to our earlier argument, we have $0.1_3 = 0.0222\ldots_3,$ $0.01_3 = 0.002222\ldots_3,$ and $0.21_3 = 0.202222\ldots_3,$ so these numbers also have representations containing only 0s and 2s.
Continuing this process, we see that $\cup_{j=1}^n G_j$ contains all numbers which have a base 3 representation with a 1 in the first, second, or third digit, except for the left endpoints of the sub-intervals of $\cup_{j=1}^n G_j.$
However, these numbers all have representations containing only 0s and 2s.
THerefore the set $[0, 1] \setminus \cup_{n=1}^\infty G_n,$ i.e. the Cantor set, contains all numbers whose decimal representation contains only 0s and 2s.
:::


:::{prf:theorem} Properties of the Cantor set
:label: mira:thm:properties-of-cantor-set
1. The {prf:ref}`Cantor set<mira:def:cantor-set>` is a closed subset of $\mathbb{R}$.
2. The Cantor set has Lebesgue measure $0$.
3. The Cantor set contains no interval with more than one element
:::

:::{dropdown} Proof: properties of the Cantor set
__Part 1:__
The sets $G_n$ defined in {prf:ref}`mira:def:cantor-set` are open sets, so their union $\cup_{n=1}^\infty G_n$ is an open set.
The Cantor set is the intersection of $[0, 1]$ with $\mathbb{R} \setminus \cup_{n=1}^\infty G_n,$ which is a closed set.
Therefore, the Cantor set is a closed subset of $\mathbb{R}.$

__Part 2:__
We proceed by induction.
Weach $G_n$ is the union of $2^{n-1}$ open intervals, each of length $\frac{1}{3^n}.$
Note also that the $G_n$ are all disjoint, and since measures are {prf:ref}`countably additive<mira:def:measure>`, we have

$$\begin{align}
\left|\cup_{n=1}^\infty G_n\right| &= \sum_{n=1}^\infty |G_n| \\
&= \frac{1}{3} + \frac{2}{3^2} + \frac{4}{3^3} + \cdots \\
&= \frac{1}{3} \left(1 + \frac{2}{3} + \frac{4}{9} + \cdots \right) \\
&= \frac{1}{3} \frac{1}{1 - \frac{2}{3}} \\
&= 1.
\end{align}$$

Thus the Cantor set $[0, 1] \setminus \cup_{n=1}^\infty G_n$ has Lebesgue measure $|[0, 1]| - |\cup_{n=1}^\infty G_n| = 1 - 1 = 0.$

__Part 3:__
The Cantor set is a {prf:ref}`Lebesgue set<mira:def:lebesgue-measurable-set>` of measure 0, and a Lebesgue set of measure 0 cannot contain an interval that has more than one element. (Otherwise, the interval would have positive measure and the set would also have positive measure.)
Thus the Cantor set cannot contain an interval with more than one element.
:::


:::{prf:theorem} Cantor function
:label: mira:thm:cantor-function
The Cantor function $\Lambda: [0, 1] \to [0, 1]$ is defined by converting base 3 representations into base 2 representations as follows:

1. If $x \in C,$ then $\Lambda(x)$ is the number obtained from the unique representation of $x$ containing only 0s and 2s, by replacing each 2 by 1 and interpreting the resulting string as a base 2 number.
2. If $x \in [0, 1] \setminus C,$ then $\Lambda(x)$ is computed from a base 3 representation of $x$ by truncating after the first 1, replacing each 2 before the first 1 by 1, and interpreting the resulting tring as a base 2 number.
:::



:::{prf:theorem} Properties of the Cantor function
:label: mira:thm:properties-of-cantor-function
The {prf:ref}`Cantor function<mira:thm:cantor-function>` $\Lambda$ is a continuous, increasing function from $[0, 1]$ onto $[0, 1].$
Furthermore, $\Lambda(C) = [0, 1].$
:::

:::{dropdown} Proof: properties of the Cantor function
__Part 1:__
First we prove that $\Lambda(C) = [0, 1],$ which also implies that $\Lambda$ is onto.
Suppose $y \in [0, 1].$
Then, define $x \in [0, 1]$ to be the number obtained by taking the base 2 representation of $y,$ replacing each $1$ by $2$ and interpreting the result as a base 3 number.
Because $x$ has a base 3 representation containing only 0s and 2s, $x$ is in the Cantor set $C.$
By the definition of the {prf:ref}`Cantor function<mira:thm:cantor-function>`, we have $\Lambda(x) = y.$
Thus $\Lambda(C) = [0, 1].$

__Part 2:__
Now we show that $\Lambda$ is increasing.
Suppose $x_1, x_2 \in [0, 1]$ and $x_1 < x_2.$
Then, in the base 3 representation of $x_1$ and $x_2,$ there exists a $k \in \mathbb{N}$ such that the $k$th digit of $x_1$ is less than the $k$th digit of $x_2.$
Before the $k$th digit, the two numbers have identical digits.
There are a three different cases to consider.
First, if a 1 appears in the base 3 representation of $x_1$ before the $k$th digit (and thus also in the base 3 representation of $x_2$), then the base 3 representation of both $x_1$ and $x_2$ are truncated by $\Lambda$ before the $k$th digit, so $\Lambda(x_1) = \Lambda(x_2).$
Second, if the $k$th digit of $x_1$ is 1, then the base 3 representation of $x_1$ is truncated by the Cantor function at this digit and has trailing 0s.
The base 3 representation of $x_2$ must have a 2 in the $k$th digit, so the $k$th digit of $\Lambda(x_2)$ is 1, and $\Lambda(x_1) \leq \Lambda(x_2).$
Finally, if no 1 appears in the base 3 representation of $x_1$ before the $k$th digit, then $\Lambda(x_1) \leq \Lambda(x_2),$ by inspection of the definition of the Cantor function.


__Part 3:__
Finally, we note that an increasing onto function from $[0, 1]$ to $[0, 1]$ is continuous.
Therefore, $\Lambda$ is continuous.
:::


Now we can use the Cantor function to show that the Cantor set is uncountable.

:::{prf:theorem} Cantor set is uncountable
:label: mira:thm:cantor-set-is-uncountable
The Cantor set $C$ is uncountable.
:::

:::{dropdown} Proof: Cantor set is uncountable
If $C$ were countable, then $\Lambda(C)$ would also be countable.
However, $\Lambda(C) = [0, 1],$ which is uncountable.
Therefore, $C$ must be uncountable.
:::


The Canotr function also shows that even a continuous function can map a set with Lebesgue measure $0$ to a non-measurable set.

:::{prf:theorem} Continuous image of a Lebesgue measurable set can be non-measurable
:label: mira:thm:continuous-image-of-a-lebesgue-measurable-set-can-be-non-measurable
There exists a Lebesgue measurable set $A \subseteq [0, 1]$ such that $|A| = 0$ and $\Lambda(A)$ is not a Lebesgue measurable set.
:::


:::{dropdown} Proof: continuous image of a Lebesgue measurable set can be non-measurable
Let $E$ be a subset of $[0, 1]$ that is not Lebesgue measurable.
Also let $A = C \cap \Lambda^{-1}(E).$
Then $|A| = 0$ because $A \subseteq C$ and $|C| = 0$ ({prf:ref}`mira:thm:outer-measure-preserves-order`).
Thus $A$ is Lebesgue measurable because every subset of $\mathbb{R}$ with outer measure $0$ is Lebesgue measurable.
Because $\Lambda$ maps $C$ onto $[0, 1],$ we have $\Lambda(A) = E.$
:::


## Convergence of measurable functions


:::{prf:definition} Pointwise convergence; uniform convergence
:label: mira:def:pointwise-convergence-uniform-convergence
Suppose $X$ is a set, $f_1, f_2, \ldots$ is a sequence of functions from $X$ to $\mathbb{R},$ and $f: X \to \mathbb{R}$ is a function.

1. The sequence $f_1, f_2, \ldots$ converges pointwise to $f$ if for each $x \in X$ and each $\epsilon > 0,$ there exists $n \in \mathbb{Z}^+$ such that $|f_n(x) - f(x)| < \epsilon$ for all $k \geq n.$
2. The sequence $f_1, f_2, \ldots$ converges uniformly to $f$ if for every $\epsilon > 0,$ there exists $n \in \mathbb{Z}^+$ such that $|f_n(x) - f(x)| < \epsilon$ for all $k \geq n$ and all $x \in X.$
:::



:::{prf:theorem} Uniform limit of continuous functions is continuous
:label: mira:thm:uniform-limit-of-continuous-functions-is-continuous
Suppose $B \subseteq \mathbb{R}$ and $f_1, f_2, \ldots$ is a sequence of continuous functions from $B$ to $\mathbb{R}$ that converges uniformly to a function $f: B \to \mathbb{R}.$
Suppose $b \in B$ and $f_k$ is continuous at $b$ for all $k \in \mathbb{Z}^+.$
Then $f$ is continuous at $b.$
:::

:::{dropdown} Proof: uniform limit of continuous functions is continuous
Let $\epsilon > 0.$
Since $f_n$ converges to $f$ uniformly, there exists $n \in \mathbb{Z}^+$ such that $|f_n(x) - f(x)| < \frac{\epsilon}{3}$ for all $x \in B.$
Because $f_n$ is continuous at $b,$ there exists $\delta$ such that $|f_n(x) - f_n(b)| < \frac{\epsilon}{3}$ for all $x \in B$ such that $|x - b| < \delta.$
Now, suppose that $x \in B$ and $|x - b| < \delta.$
Then we have

$$\begin{align}
|f(x) - f(b)| &\leq |f(x) - f_n(x)| + |f_n(x) - f_n(b)| + |f_n(b) - f(b)| \\
&< \epsilon
\end{align}$$

so $f$ is continuous at $b.$
:::

:::{prf:theorem} Egorov's theorem
:label: mira:thm:egorovs-theorem
Suppose $(X, S, \mu)$ is a measurable space with $\mu < \infty.$
Suppose $f_1, f_2, \dots$ is a sequence of $S$-measurable functions from $X$ to $\mathbb{R}$ that converges pointwise on $X$ to a function $f: X \to \mathbb{R}.$
Then for every $\epsilon > 0,$ there exists a set $E \in S$ such that $\mu(X \setminus E) < \epsilon$ and $f_1, f_2, \dots$ converges uniformly to $f$ on $E.$
:::

<!-- :::{dropdown} Proof: Egorov's theorem
Suppose that $(X, S, \mu)$ is a measurable space with $\mu < \infty$ and that $f_1, f_2, \dots$ is a sequence of $S$-measurable functions from $X$ to $\mathbb{R}$ that converges pointwise on $X$ to a function $f: X \to \mathbb{R}.$
Let $\epsilon > 0.$
Because $f_1, f_2, \dots$ converges to $f$ pointwise, for each $x \in X$ there exists a least $N_{x, \epsilon} \in \mathbb{Z}^+$ such that for all $n \geq N_{x, \epsilon},$ it holds that $|f_n(x) - f(x)| < \epsilon.$
Now define the sets

$$E_k = \{x \in X: N_{x, \epsilon} \leq k\}.$$

We show a number of properties for $E_k.$
First, $E_k$ is $S$-measurable for each $k \in \mathbb{Z}^+,$ which can be shown as follows.
First

$$\begin{align}
x \in E_k \iff |f_m(x) - f(x)| < \epsilon \text{ for all } m \geq k
\end{align}$$

which implies that

$$\begin{align}
E_k = \bigcap_{m = k}^\infty (f_m - f)^{-1}((-\epsilon, \epsilon))
\end{align}$$

which is $S$-measurable since $(f_m - f)^{-1}((-\epsilon, \epsilon))$ is $S$-measurable for each $m \in \mathbb{Z}^+.$
Second, $E_k$ is increasing and $E_k \to X,$ which means that $X \setminus E_k$ is decreasing and $X \setminus E_k \to \emptyset.$
Therefore

$$\begin{equation}
\lim_{k \to \infty} \mu(X \setminus E_k) = \mu(\lim_{k \to \infty} X \setminus E_k) = \mu(\emptyset) = 0.
\end{equation}$$

From this, we conclude that there must exist some $K \in \mathbb{Z}^+$ such that for all $k \geq K$ we have $\mu(X \setminus E_k) < \epsilon.$
::: -->