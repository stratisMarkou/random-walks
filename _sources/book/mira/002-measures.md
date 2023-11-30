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

:::{prf:definition} Translation

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

$$[-1, 1] \subseteq \bigcup_{k=1}^\infty (r_k + V),$

because for each $a \in [-1, 1],$ there is a unique element $v \in V$ that is in the same equivalence class as $a,$ namely $v = \tilde{a} \cap V,$ so $a - v \in \mathbb{Q},$ from which it follows that $a - v = r_k$ for some $k \in \mathbb{Z}^+,$ and therefore $a \in r_k + V.$
The set inclusion above together with the {prf:ref}`order preserving property <mira:thm:outer-measure-preserves-order>` of the outer measure, and the {prf:ref}`translation invariance <mira:thm:outer-measure-is-translation-invariant>` of the outer measure imply that

$$|[-1, 1]| = 2 \leq \sum_{k=1}^\infty |r_k + V| = \sum_{k=1}^\infty |V|$$

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
