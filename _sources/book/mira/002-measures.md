# Measures

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
Since $[a, b]$ is has $I_1, \dots, I_n, I_{n+1}$ as an open cover, it follows that $[a, c]$ has $I_1, \dots, I_n,$ as an open cover, that is

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

:::{prf:theorem} Nonadditivity of the outer measure
:label: mira:thm:non-additivity-of-outer-measure

There exist disjoint subsets $A, B$ of $\mathbb{R}$ such that

$$|A \cup B| \neq |A| + |B|.$$

:::


:::{dropdown} Proof: Nonadditivity of the outer measure

__Proof idea:__
We will show this result as follows.
We will define a countable collection of disjoint sets whose union is contained in an closed interval of $\mathbb{R},$ and which have all equal outer measure.
Then, we will show that the outer measure of each of these sets is nonzero, which contradicts the assumption that the outer measure is additive. 

__Proof:__
Let $\sim$ be the binary relation defined by

$$a \sim b \iff a - b \in \mathbb{Q}.$$

Note that $\sim$ is an equivalence relation on $\mathbb{R},$ because it is:

- reflexive: $a - a = 0 \in \mathbb{Q};$
- symmetric: If $a - b \in \mathbb{Q},$ then $b - a = -(a - b) \in \mathbb{Q};$
- transitive: If $a - b \in \mathbb{Q}$ and $b - c \in \mathbb{Q},$ then $a - c = (a - b) + (b - c) \in \mathbb{Q}.$

For $a \in [-1, 1],$ let $\tilde{a}$ be the equivalence class of $a$ under $\sim.$
Then, for any $a \in [-1, 1],$ we have

$$[-1, 1] = \bigcup_{a \in [-1, 1]} \tilde{a}.$$

Now, let $V$ be a set that contains exactly one element from each of the equivalence classes of $\sim$ on $[-1, 1].$
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
As explained earlier, any function that satisfies some of the aforementioned properties of the outer measure and has domain equal to the power set of $\mathbb{R}$ cannot be additive.





## Measurable spaces and functions


:::{prf:theorem} Nonexistence of extension of length to all subsets of $\mathbb{R}$
:label: mira-thm-nonexistence-length

There does not exist a function $\mu$ with the following properties:

(a) $\mu$ is a function fromm the set of subsets of $\mathbb{R}$ to $[0, \infty],$

(b) $\mu(I) = \ell(I)$ for all open intervals $I \subseteq \mathbb{R},$

(c) For every disjoint sequence $A_1, A_2, \ldots$ of subsets of $\mathbb{R},$ $\mu \left( \cup_{k=1}^\infty A_k \right) = \sum_{k=1}^\infty \mu(A_k),$

(d) $\mu(t + A) = \mu(A)$ for all $A \subseteq \mathbb{R}$ and $t \in \mathbb{R}.$

:::

:::{dropdown} Proof: Nonexistence of extension of length to all subsets of $~\mathbb{R}$

Suppose there exists a function $\mu$ with all the properties listed in the statement of this theorem.
We will show that $\mu$ has all the properties that were used in our proof of the {prf:ref}`nonadditivity of the outer measure <mira:thm:non-additivity-of-outer-measure>`, and we can then repeat the argument used there.

__Showing the relevant properties:__
First, observe that $\mu(\emptyset) = 0,$ because $\emptyset$ is an open interval with length $0.$
Now, $\mu$ has the order preserving property, bevause if $A \subseteq B \subseteq \mathbb{R},$ then $\mu(A) \subseteq \mu(B),$ because considering the sequence $A, B \setminus A, \emptyset, \emptyset, \dots$ and applying property (c), we arrive at

$$\mu(B) = \mu(A) + \mu(B \setminus A) + 0 + 0 + \dots = \mu(A) + \mu(B \setminus A) \geq \mu(A).$$

In addition, if $a, b \in \mathbb{R}$ with $a < b,$ then 

$$(a, b) \subseteq [a, b] \subseteq (a - \epsilon, b + \epsilon)$$

for every $\epsilon > 0,$ so

$$\mu((a, b)) \leq \mu([a, b]) \leq \mu((a - \epsilon, b + \epsilon)) = b - a + 2\epsilon,$$

and since $\epsilon > 0$ is arbitrary, this implies that 

$$\mu([a, b]) = b - a.$$ (mira:eq:mu-of-closed-interval)

Finally, if $A_1, A_2, \dots$ is a sequence of disjoint subsets of $\mathbb{R},$ then

$$A_1, A_2 \setminus A_1, A_3 \setminus (A_1 \cup A_2), \ldots$$

is a sequence of disjoint subsets of $\mathbb{R},$ so by property (c), we have

$$\begin{align}
\mu\left( \bigcup_{k=1}^\infty A_k \right) &= \mu\left( A_1 \cup (A_2 \setminus A_1) \cup (A_3 \setminus (A_1 \cup A_2)) \cup \dots \right) \\
&= \mu(A_1) + \mu(A_2 \setminus A_1) + \mu(A_3 \setminus (A_1 \cup A_2)) + \cdots \\
&\leq \sum_{k=1}^\infty \mu(A_k).
\end{align}$$ (mira:eq:mu-is-countably-subadditive)

Therefore $\mu$ is countably subadditive.

__Repeating the argument:__
Now, define the set $V$ in the same way that it was defined in the proof of the {prf:ref}`nonadditivity of the outer measure <mira:thm:non-additivity-of-outer-measure>`.
Specifically, let $\sim$ be the equivalence relation such that for $x, y \in [-1, 1]$ we have $x \sim y$ if $x$ and $y$ differ by a rational number.
Let $V$ be the set which contains exactly one representative from each equivalence clss of $\sim.$
Let $r_1, r_2, \dots$ be a sequence that contains each rational number in $[-2, 2]$ exactly once.
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


### $\sigma$-algebras

:::{prf:definition} $\sigma$-algebra

Suppose $X$ is a set and $S$ is a set of subsets of $X.$
Then $S$ is called a $\sigma$-algebra on $X$ if it satisfies:

- $\emptyset \in S,$
- if $E \in S,$ then $X \setminus E \in S,$
- if $E_1, E_2, \dots$ is a sequnece of elements of $S,$ then $\bigcup_{k=1}^\infty E_k \in S.$

:::



:::{prf:theorem} Other properties of $\sigma$-algebras

Suppose $S$ is a $\sigma$-algebra on a set $X.$
Then

(a) $X \in S,$

(b) if $D, E \in S,$ then $D \cup E \in S, D \cap E \in S$ and $D \setminus E \in S,$

(c) if $E_1, E_2, \dots$ is a sequence of elements of $S,$ then $\cap_{k = 1}^\infty E_k \in S.$

:::


:::{dropdown} Proof: Other properties of $~\sigma$-algebras

Because $\emptyset \in S$ and $X = X \setminus \emptyset,$ we have $X \in S.$
Suppose $D, E \in S.$
Then $D \cup E \in S$ because this is the union of the sequence $D, E, \emptyset, \emptyset, \dots \in S.$
In addition,

$$D \cap E = X \setminus ((X \setminus D) \cup (X \setminus E)) \in S,$$

and also $D \setminus (X \setminus E) = D \cap E \in S.$
Lastly, if $E_1, E_2, \dots$ is a sequence of elements of $S,$ then

$$\bigcap_{k=1}^\infty E_k = X \setminus \bigcup_{k=1}^\infty (X \setminus E_k) \in S.$$

:::



:::{prf:definition} Measurable space, measurable set

A measurable space is an ordered pair $(X, S),$ where $X$ is a set and $S$ is a $\sigma$-algebra on $X.$
An element of $S$ is called a $S$-measurable set, or simply a measurable set if $S$ is clear from the context.

:::



:::{prf:theorem} Smallest $\sigma$-algebra containing a collection of subsets

Suppose $X$ is a set and $A$ is a set of subsets of $X.$
Then, the intersection of all $\sigma$-algebras on $X$ that contain $A$ is a $\sigma$-algebra on $X.$

:::

:::{dropdown} Proof: Smallest $~\sigma$-algebra containing a collection of subsets

There is at least one $\sigma$-algebra on $X$ that contains $A,$ because the power set of $X$ is a $\sigma$-algebra on $X$ that contains $A.$
Let $S$ be the intersection of all $\sigma$-algebras on $X$ that contain $A.$

First, $\emptyset \in S,$ because $\emptyset$ is in every $\sigma$-algebra on $X.$
Second, if $E \in S,$ then $E$ is in every $\sigma$-algebra on $X$ that contains $A,$ so $X \setminus E$ is in every $\sigma$-algebra on $X$ that contains $A,$ so $X \setminus E \in S.$
Third, if $E_1, E_2, \dots$ is a sequence of elements of $S,$ then $E_1, E_2, \dots$ is a sequence of elements of every $\sigma$-algebra on $X$ that contains $A,$ so $\bigcup_{k=1}^\infty E_k$ is in every $\sigma$-algebra on $X$ that contains $A,$ so $\bigcup_{k=1}^\infty E_k \in S.$

:::



:::{prf:definition} Borel set

The smallest $\sigma$-algebra on $\mathbb{R}$ that contains all the open subsets of $\mathbb{R}$ is called the collection of Borel subsets on $\mathbb{R}.$
An element of this $\sigma$-algebra is called a Borel set.

:::


:::{prf:definition} Inverse image

If $f: X \in Y$ is a function and $A \subseteq Y,$ then the inverse image of $A$ under $f$ is defined by

$$f^{-1}(A) = \{ x \in X : f(x) \in A \}.$$

:::


:::{def:theorem} Algebra of inverse images

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



:::{prf:definition} Measurable function

Suppose $(X, S)$ is a measurable space.
A function $f: X \to \mathbb{R}$ is called $S$-measurable if

$$f^{-1}(B) \in S$$

for all Borel sets $B \subseteq \mathbb{R}.$

:::




:::{prf:defintion} Characteristic function

Suppose $E$ is a subset of a set $X.$
The characteristic function of $E$ is the function $\chi_E: X \to \mathbb{R}$ defined by

$$\chi_E(x) = \begin{cases} 1 & \text{if } x \in E \\ 0 & \text{if } x \notin E. \end{cases}$$

:::



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
Third, if $A_1, A_2, \dots \in T,$ then $f^{-1}(A_1), f^{-1}(A_2), \dots \in S,$ so 

$$f^{-1}\left(\bigcup_{k=1}^\infty A_k\right) = \bigcup_{k=1}^\infty f^{-1}(A_k) \in S,$$

so $\cup_{k=1}^\infty A_k \in T.$
Thus $T$ is a $\sigma$-algebra on $\mathbb{R}.$

__Every open interval is in $T$:__
By the hypothesis in the theorem statement, it follows that $f^{-1}((a, \infty)) \in S$ for all $a \in \mathbb{R},$ so $(a, \infty) \in T$ for all $a \in \mathbb{R}.$
Since $T$ is a $\sigma$-algebra on $\mathbb{R},$ it is closed under complementation and intersection so $(-\infty, b] \in T$ for all $b \in \mathbb{R},$ and $(a, b) \in T$ for all $a, b \in \mathbb{R}.$
Therefore $T$ contains all the open intervals of $\mathbb{R},$ so $T$ contains all the Borel subsets of $\mathbb{R}.$

:::



In the special case that $X$ is a subset of the reals and $S$ is the set of Borel subsets of $\mathbb{R},$ we use the term Borel measurable to refer to $S$-measurable functions.

:::{prf:definition} Borel measurable function

Suppose $X \subseteq \mathbb{R}.$
A function $f: X \to \mathbb{R}$ is called Borel measurable if $f^{-1}(B)$ is a Borel set for every Borel set $B \subseteq \mathbb{R}.$

:::




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
