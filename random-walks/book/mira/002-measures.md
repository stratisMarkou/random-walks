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

The lenght $\ell(I)$ of an open interval $I \subseteq \mathbb{R}$ is defined by

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

The outer measure $|A|$ of a subset $A \subseteq \mathbb{R}$ is defined by

$$|A| = \inf \left\{ \sum_{j=1}^\infty \ell(I_j) : A \subseteq \bigcup_{j=1}^\infty I_j \right\}.$$

:::



### Good properties

The outer measure has a number of good properties.
First, the outer measure of countable subsets of $\mathbb{R}$ is zero.

:::{prf:theorem} Countable sets have outer measure zero
:label: mira:thm:countable-sets-have-measure-zero

Every countable subset of $\mathbb{R}$ has outer measure $0.$

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
Therefore,

$$|A| \leq \sum_{j=1}^\infty \ell(I_j),$$

and taking the infimum of both sides, over all sequences of open intervals whose union contains $B$ gives $|A| \leq |B|.$

:::


The third good property of the outer measure is translation invariance.
To establish this property, we first need a definition of the translation of a set.

:::{prf:definition} Translation invariance
:label: mira:thm:outer-measure-is-translation-invariant

For $A \subseteq \mathbb{R}$ and $t \in \mathbb{R},$ the translation of $t + A$ is defined by

$$A + t = \{ a + t : a \in A \}.$$

:::



With this definition in place, we can now state the translation invariance property of the outer measure.
Specifically, the outer measure of a set is the same as the outer measure of its translation.

:::{prf:theorem} Outer measure is translation invariant

For every subset $A$ of $\mathbb{R}$ and every $t \in \mathbb{R},$ we have $|t + A| = |A|.$

:::

:::{dropdown} Proof: Outer measure is translation invariant

Suppose $A$ is a subset of $\mathbb{R}$ and $t \in \mathbb{R}.$
Let $I_1, I_2, \ldots$ be a sequence of open intervals whose union contains $A.$
Then $t + I_1, t + I_2, \ldots$ is a sequence of open intervals whose union contains $t + A.$
Thus,

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
Then $I_1, I_2, \ldots$ is an open cover of $[a, b],$ so by the {prf:ref}`Heine-Borel theorem <mira:thm:heine-borel>`, there exists an $n \in \mathbb{Z}^+$ such that

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
We will show this result as follows.
We will define a countable collection of disjoint sets.
We will set up these sets so that their union is contained in an closed bounded interval of $\mathbb{R},$ and they all have equal outer measure.
Then, we will show that the outer measure of each of these sets is nonzero, which leads to a contradiction.

__Proof:__
Let $\sim$ be the equivalence class of $a$ under the {prf:ref}`rational difference equivalence relation<mira:def:rational-difference-equivalence-relation>`, and for each $a \in [-1, 1]$ let $\mathtilde{a}$ be the equivalence class of $a$ under $\sim.$
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
:label: mira:thm:nonexistence-length

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

$$2 = \mu([-1, 1]) = \mu\left(\bigcup_{k = 1}^\infty r_k + V\right) = \sum_{k=1}^\infty \mu(r_k + V) = \sum_{k=1}^\infty \mu(V)$$

Thus $\mu(V) > 0.$
Now, note that the sets $(r_1 + V), (r_2 + V), \ldots, (r_K + V)$ are disjoint for any $K \in \mathbb{Z}^+.$
Note also that for any $K \in \mathbb{Z}^+,$ we have

$$ \bigcup_{k=1}^K (r_k + V) \subseteq [-3, 3] \implies \mu\left( \bigcup_{k=1}^K (r_k + V) \right) \leq 6.$$

Now, using the additivity and the translation invariance of $\mu$, properties (c) and (d), we have 

$$\mu\left( \bigcup_{k=1}^K (r_k + V) \right) = \sum_{k=1}^K \mu(r_k + V) = K \mu(V) < 6,$$

reaching a contradiction, because $|V| > 0,$ so the above inequality cannot hold for any $K.$

:::


### Sigma algebras

{prf:ref}`mira:thm:nonexistence-length` shows that there does not exist a notion of length that satisfies all four intuitive properties that we would like length to satisfy.
We therefore need to relax at least one of these properties to proceed.
We cannot relax (b), because we want all open intervals to have the length one would expect.
We also cannot give up (c), because we want length to be additive.
Finally, we cannot give up (d) either, because we want length to be translation invariant.
Therefore, our only option is to relax (a).
This is where $\sigma$-algebras come in: instead of using all subsets of $\mathbb{R}$ as the domain of $\mu,$ we will restrict the domain to be a certain collection of subsets, which circumvents the issue of non-measurable sets.

:::{prf:definition} $\sigma$-algebra
:label: mira:def:sigma-algebra

Suppose $X$ is a set and $\mathcal{S}$ is a set of subsets of $X.$
Then $\mathcal{S}$ is called a $\sigma$-algebra on $X$ if it satisfies:

- $\emptyset \in \mathcal{S},$
- if $E \in \mathcal{S},$ then $X \setminus E \in \mathcal{S},$
- if $E_1, E_2, \ldots$ is a sequnece of elements of $\mathcal{S},$ then $\bigcup_{k=1}^\infty E_k \in S.$

:::

From this definition, a number of basic properties of $\sigma$ algebras follow immediately.

:::{prf:theorem} Other properties of $\sigma$-algebras
Suppose $\mathcal{S}$ is a $\sigma$-algebra on a set $X.$
Then

(a) $X \in \mathcal{S},$

(b) if $D, E \in \mathcal{S},$ then $D \cup E \in \mathcal{S}, D \cap E \in \mathcal{S}$ and $D \setminus E \in \mathcal{S},$

(c) if $E_1, E_2, \ldots$ is a sequence of elements of $\mathcal{S},$ then $\cap_{k = 1}^\infty E_k \in \mathcal{S}.$
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
The smallest $\sigma$-algebra on $\mathbb{R}$ that contains all the open subsets of $\mathbb{R}$ is called the collection of Borel subsets on $\mathbb{R}.$
An element of this $\sigma$-algebra is called a Borel set.
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
:label: mira-thm-condition-measurable
Suppose $(X, S)$ is a measurable space and $f: X \to \mathbb{R}$ is a function such that

$$f^{-1}((a, \infty)) \in S$$

for all $a \in \mathbb{R}.$
Then $f$ is $S$-measurable.
:::

:::{dropdown} Proof: Condition for measurable function

Consider the set

$$T = \{A \subseteq \mathbb{R} : f^{-1}(A) \in S \}.$$

We will show that every Borel subset of $\mathbb{R}$ is in $T.$
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
Suppose $X \subseteq \mathbb{R}.$
A function $f: X \to \mathbb{R}$ is called Borel measurable if $f^{-1}(B)$ is a Borel set for every Borel set $B \subseteq \mathbb{R}.$
:::

Now we prove a number a few results on sufficient conditions for Borel measurable functions.

:::{prf:theorem} Every continuous function is Borel measurable
Every continuous real-valued function defined on a Borel subset of $\mathbb{R}$ is a Borel measurable function.
:::

:::{dropdown} Proof: Every continuous function is Borel measurable
Suppose that $X \subseteq \mathbb{R}$ is a Borel set and $f: X \to \mathbb{R}$ is a Borel measurable function.
Suppose $a \in \mathbb{R}.$
If $x \in X$ such that $f(x) > a,$ then by the continuity of $f,$ there exists $\delta_x > 0$ such that $f(y) > a$ for all $y \in (x - \delta_x, x + \delta_x).$
Thus, we have

$$\begin{equation}
f^{-1}((a, \infty)) = \left( \bigcup_{x \in f^{-1}((a, \infty))} (x - \delta_x, x + \delta_x) \right) \cap X.
\end{equation}$$

The above union is a union of open sets, which is therefore also open, so its intersection with $X$ is a Bore set.
By our earlier {prf:ref}`condition for measurable functions<mira-thm-condition-measurable>`, $f$ is Borel measurable.
:::


:::{prf:defintion} Increasing function; strictly increasing function
Suppose $X \subseteq \mathbb{R}$ and $f: X \to \mathbb{R}$ is a function.
Then $f$ is called increasing if $f(x) \leq f(y)$ for all $x, y \in X$ with $x < y.$
If $f(x) < f(y)$ for all $x, y \in X$ with $x < y,$ then $f$ is called strictly increasing.
:::


:::{prf:theorem} Every increasing function is Borel measurable
Every increasing function defined on a Borel subset of $\mathbb{R}$ is a Borel measurable function.
:::

:::{dropdown} Proof: Every increasing function is Borel measurable
Suppose that $X \subseteq \mathbb{R}$ is a Borel set and $f: X \to \mathbb{R}$ is an increasing function.
Suppose $a \in \mathbb{R}.$
Let $b = \inf f^{-1}((a, \infty)).$
Then

$$f^{-1}((a, \infty)) = (b, \infty) \cap X \text{ or } f^{-1}((a, \infty)) = [b, \infty) \cap X$$

holds.
Since $X$ is a Borel set, and both $(b, \infty)$ and $[b, \infty)$ are Borel sets, it follows that $f^{-1}((a, \infty))$ is a Borel set.
By our earlier {prf:ref}`condition for measurable functions<mira-thm-condition-measurable>`, $f$ is Borel measurable.
:::

:::{prf:theorem} Composition of measurable functions

Suppose $(X, S)$ is a measurable space and $f: X \to \mathbb{R}$ is a measurable function.
Suppose that $g$ is a real-valued Borel measurable function defined on a subset of $\mathbb{R}$ that includes the range of $f.$
Then $g \circ f: X \to \mathbb{R}$ is a measurable function.

:::

:::{dropdown} Proof: Composition of measurable functions
Suppose $(X, S)$ is a measurable space and $f: X \to \mathbb{R}$ is a measurable function.
Suppose that $g$ is a real-valued Borel measurable function defined on a subset of $\mathbb{R}$ that includes the range of $f.$
Let $B \subseteq \mathbb{R}$ be a Borel set.
Because $g$ is a Borel measurable function, and $B$ is a Borel set, $g^{-1}(B)$ is also a Borel set.
Because $f$ is a measurable function, and $g^{-1}(B)$ is a Borel set, $f^{-1}(g^{-1}(B))$ is in $S,$ so $g \circ f$ is Borel measurable.
:::

Measurable functions also satisfy intuitive algebraic properties that are very useful for proving measurability.

:::{prf:theorem} Algebraic operations with measurable functions
Suppose $(X, S)$ is a measurable space and $f, g: X \to \mathbb{R}$ are $S$-measurable functions.
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
Suppose $(X, S)$ is a measurable space and $f_1, f_2, \ldots$ are $S$-measurable functions from $X$ to $\mathbb{R}.$
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

We conclude that $f^{-1}((a, \infty))$ is a Borel set and by our earlier {prf:ref}`condition for measurable functions<mira-thm-condition-measurable>`, $f$ is a Borel measurable function.
:::

Sometimes, we may need to consider functions which take values in $[-\infty, \infty].$
We therefore extend the notion of Vorel sets to subsets of $[-\infty, \infty]$ in the following way.

:::{prf:definition} Borel subsets of $[-\infty, \infty]$
A subset of $[-\infty, \infty]$ is called a Borel subset if its intersection with $\mathbb{R}$ is a Borel set.
:::

With the above definition in place, we can also extend the definition of measurable functions.

:::{prf:definition} Measurable function on $[-\infty, \infty]$
:label: mira:def:measurable-function-infinity
Suppose $(X, \mathcal{S})$ is a measurable space.
A function $f: X \to [-\infty, \infty]$ is $\mathcal{S}$-measurable if

$f^{-1}(B) \in \mathcal{S}$

for every Borel set $B \subseteq [-\infty, \infty].$
:::

The following result is the counterpart of our earlier {prf:ref}`sufficient condition for measurability<mira-thm-condition-measurable>`, but with infinities included in the range of the function.

:::{prf:theorem} Sufficient condition for measurable function
:label: mira-thm-sufficient-condition-measurable-with-infinity
Suppose $(X, \mathcal{S})$ is a measurable space and $f: X \to [-\infty, \infty]$ is a function such that

$$f^{-1}((a, \infty]) \in \mathcal{S}$$

for all $a \in \mathbb{R}.$
Then $f$ is $\mathcal{S}$-measurable.
:::

:::{dropdown} Proof: Sufficient condition for measurable function
Suppose $(X, \mathcal{S})$ is a measurable space and $f: X \to [-\infty, \infty]$ is a function such that

$$f^{-1}((a, \infty]) \in \mathcal{S}$$

for all $a \in \mathbb{R}.$
Note that

$$f^{-1}(\{\infty\}) = \bigcap_{n=1}^\infty f^{-1}((n, \infty]) \in \mathcal{S},$$

and also similarly $f^{-1}(\{-\infty\}) \in \mathcal{S}.$
From these it follows that

$$f^{-1}((a, \infty)) = f^{-1}((a, \infty]) \setminus f^{-1}(\{\infty\}) \in \mathcal{S} \text{ for all } a \in \mathbb{R}.$$

Let $B$ be a Borel set in $[-\infty, \infty].$
From our earlier {prf:ref}`condition for measurable functions<mira-thm-condition-measurable>`, it follows that $f^{-1}(B \cap \mathbb{R}) \in \mathcal{S}$ for any Borel set $B \subseteq [-\infty, \infty].$
We therefore have

$$\begin{align}
f^{-1}(B) &= f^{-1}((B \cap \mathbb{R}) \cup (B \cap \{\infty\}) \cup (B \cap \{-\infty\})) \\
&= f^{-1}(B \cap \mathbb{R}) \cup f^{-1}(\{\infty\}) \cup f^{-1}(\{-\infty\}) \in \mathcal{S}
\end{align}$$

so $f$ is $\mathcal{S}$-measurable.
:::

Concluding this section, we show that pointwise infimuma and pointwise supremuma of measurable functions are measurable.
Note that this result would not have made sense before modifying the {prf:ref}`definition of measurability to include infinity<mira:def:measurable-function-infinity>`, because the supremum and infimum can be $\infty$ and $- \infty.$

:::{prf:theorem} Infimum and supremum of a sequence of measurable functions is measurable
Suppose $(X, \mathcal{S})$ is a measurable space and $f_1, f_2, \ldots$ is a sequence of $\mathcal{S}$-measurable functions from $X$ to $[-\infty, \infty].$
Define $g, h: X \to [-\infty, \infty]$ by

$$g(x) = \inf\{f_k(x) : k \in \mathbb{Z}^+\} \text{ and } h(x) = \sup\{f_k(x) : k \in \mathbb{Z}^+\}.$$

Then $g$ and $h$ are $\mathcal{S}$-measurable functions.
:::

:::{dropdown} Proof: Infimum and supremum of a sequence of measurable functions is measurable
Let $a \in \mathbb{R}.$
The definition of the supremum implies that

$$h^{-1}((a, \infty]) = \bigcup_{k=1}^\infty f_k^{-1}((a, \infty]) \in \mathcal{S},$$

which, together with the earlier {prf:ref}`sufficient condition for measurable function<mira-thm-sufficient-condition-measurable-with-infinity>`, implies that $h$ is $\mathcal{S}$-measurable, that is, the supremum of a sequence of measurable functions is measurable.
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
Suppose $X$ is a set and $\mathcal{S}$ is a $\sigma$-algebra on $X.$
A measure on $(X, \mathcal{S})$ is a function $\mu: \mathcal{S} \to [0, \infty]$ such that $\mu(\emptyset) = 0$ and $\mu$ is countably additive, that is

$$\mu\left( \bigcup_{k=1}^\infty E_k \right) = \sum_{k=1}^\infty \mu(E_k)$$

for every disjoint sequence $E_1, E_2, \ldots$ of sets in $\mathcal{S}.$
:::


Countable additivity of measures is a key property that allows us to prove useful limit theorems.
Note that countable additvity implies finite additivity, that is, if $\mu$ is a measure on $(X, \mathcal{S})$ and $E_1, \ldots, E_n$ are disjoint sets in $\mathcal{S},$ then

$$\mu(E_1 \cup \cdots \cup E_n) = \mu(E_1) + \cdots + \mu(E_n).$$

The following terminology is often very useful.


:::{prf:definition} Measure space
A measure space is an ordered triple $(X, \mathcal{S}, \mu),$ where $X$ is a set, $\mathcal{S}$ is a $\sigma$-algebra on $X$ and $\mu$ is a measure on $(X, \mathcal{S}).$
:::


### Properties of measures

Now we discuss several useful properties of measures.

:::{prf:theorem} Measure preserves order; measure of a set difference
:label: mira-thm-measure-preserves-order
Suppose $(X, \mathcal{S}, \mu)$ is a measure space and $D, E \in \mathcal{S}$ with $D \subseteq E.$
Then

(a) $\mu(D) \leq \mu(E),$

(b) $\mu(E \setminus D) = \mu(E) - \mu(D)$ provided that $\mu(D) < \infty.$
:::

:::{dropdown} Proof: Measure preserves order; measure of a set difference
Note that $E = D \cup (E \setminus D)$ is a disjoint union, so by {prf:ref}`countable additivity of measures<mira-def-measure>`, we have

$$\mu(E) = \mu(D) + \mu(E \setminus D) \geq \mu(D),$$

which proves part (a).
If $\mu(D) < \infty,$ then part (b) follows by subtracting $\mu(D)$ from both sides of the equation above.
:::


The countable additivity property of measures applies to disjoint countable unions.
The following countable _subadditivity_ property applies to countable unions that may not be disjoint unions.

:::{prf:theorem} Countable subadditivity
Suppose $(X, \mathcal{S}, \mu)$ is a measure space and $E_1, E_2, \ldots \in \mathcal{S}.$
Then

$$\mu\left( \bigcup_{k=1}^\infty E_k \right) \leq \sum_{k=1}^\infty \mu(E_k).$$

:::

:::{dropdown} Proof: Countable subadditivity
Suppose $E_1, E_2, \ldots \in \mathcal{S}.$
Let $D_1 = \emptyset$ and $D_k = E_1 \cup \cdots \cup E_{k-1}$ for $k \geq 2.$
Then $E_1 \setminus D_1, E_2 \setminus D_2, \ldots$ is a sequence of disjoint sets in $\mathcal{S}$ whose union equals $\cup_{k=1}^\infty E_k.$
Therefore

$$\begin{align}
\mu\left( \bigcup_{k=1}^\infty E_k \right) &= \mu\left( \bigcup_{k=1}^\infty (E_k \setminus D_k) \right) \\
&= \sum_{k=1}^\infty \mu(E_k \setminus D_k) \\
&\leq \sum_{k=1}^\infty \mu(E_k).
\end{align}$$

where the second equality follows from {prf:ref}`countable additivity of measures<mira-def-measure>` and the inequality follows from the fact that {prf:ref}`measures preserve order<mira-thm-measure-preserves-order>`.
:::


Just as countable additivity implies finite additivity, countable subadditivity implies finite subadditivity.
That is if $\mu$ is a measure on $(X, \mathcal{S})$ and $E_1, \ldots, E_n$ are sets in $\mathcal{S},$ then

$$\mu(E_1 \cup \cdots \cup E_n) \leq \mu(E_1) + \cdots + \mu(E_n).$$

Now we show two very useful results about limits on measures.
Note that the countable additivity property of measures is crucial for the following results.


:::{prf:theorem} Measure of an increasing union
:label: mira-thm-measure-increasing-union
Suppose $(X, \mathcal{S}, \mu)$ is a measure space and $E_1, E_2, \ldots \in \mathcal{S}$ is an increasing sequence of sets in $\mathcal{S},$ that is $E_1 \subseteq E_2 \subseteq \cdots.$
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
Therefore, by {prf:ref}`countable additivity of measures<mira-def-measure>`, we have

$$\begin{align}
\mu\left( \bigcup_{j=1}^\infty E_j \right) &= \mu\left( \bigcup_{j=1}^\infty (E_j \setminus E_{j-1}) \right) \
&= \lim_{k \to \infty} \sum_{j=1}^k \mu(E_j \setminus E_{j-1}) \\
&= \lim_{k \to \infty} \mu(E_k).
\end{align}$$


Just as with the earlier property we showed about limits of increasing sequences of sets, we also have an analogous result about limits of decreasing sequences of sets.

:::{prf:theorem} Measure of a decreasing intersection
Suppose $(X, \mathcal{S}, \mu)$ is a measure space and $E_1, E_2, \ldots \in \mathcal{S}$ is a decreasing sequence of sets in $\mathcal{S},$ that is $E_1 \supseteq E_2 \supseteq \cdots,$ with $\mu(E_1) < \infty.$
Then

$$\mu\left( \bigcap_{k=1}^\infty E_k \right) = \bigcup_{k=1}^\infty \mu(E_k).$$
:::

:::{dropdown} Proof: Measure of a decreasing intersection
First, we have that

$$E_1 \setminus \bigcap_{k=1}^\infty E_k = \bigcup_{k=1}^\infty (E_1 \setminus E_k),$$

which is an increasing union, and by our earlier result on {prf:ref}`measures of increasing unions<mira-thm-measure-increasing-union>`, we have

$$\mu\left( E_1 \setminus \bigcap_{k=1}^\infty E_k \right) = \lim_{k \to \infty} \mu(E_1 \setminus E_k).$$

Using the countable additivity of measures, we have

$$\mu(E_1) - \mu\left( \bigcap_{k=1}^\infty E_k \right) = \mu(E_1) - \lim_{k \to \infty} \mu(E_k)$$

which proves the result.
:::


We conclude this section with another useful intuitive result, namely that the measure of the union of two sets is the sum of the measures of the sets minus the measure of their intersection, which has been counted twice.

:::{prf:theorem} Measure of the union of two sets
Suppose $(X, \mathcal{S}, \mu)$ is a measure space and $D, E \in \mathcal{S}.$
Then

$$\mu(D \cup E) = \mu(D) + \mu(E) - \mu(D \cap E).$$
:::

:::{dropdown} Proof: Measure of the union of two sets
We have

$$D \cup E = (D \setminus (D \cap E)) \cup (E \setminus (D \cap E)) \cup (D \cap E),$$

which is a disjoint union.
Therefore, by {prf:ref}`countable additivity of measures<mira-def-measure>`, we have

$$\begin{align}
\mu(D \cup E) &= \mu(D \setminus (D \cap E)) + \mu(E \setminus (D \cap E)) + \mu(D \cap E) \\
&= \mu(D) - \mu(D \cap E) + \mu(E) - \mu(D \cap E) + \mu(D \cap E) \\
&= \mu(D) + \mu(E) - \mu(D \cap E).
\end{align}$$
:::
