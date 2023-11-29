# Measures


## Outer measure


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



### Good properties of the outer measure

The outer measure has a number of good properties.

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



:::{prf:theorem} Outer measure preserves order

If $A$ and $B$ are subsets of $\mathbb{R}$ with $A \subseteq B,$ then $|A| \leq |B|.$

:::

:::{dropdown} Proof: Outer measure preserves order

Suppose $A$ and $B$ are subsets of $\mathbb{R}$ with $A \subseteq B,$ and let $I_1, I_2, \ldots$ be a sequence of open intervals whose union contains $B.$
Then the union of this sequence of open intervals also contains $A.$
Therefore,

$$|A| \leq \sum_{j=1}^\infty \ell(I_j),$$

and taking the infimum of both sides, over all sequences of open intervals whose union contains $B$ gives $|A| \leq |B|.$

:::



:::{prf:definition} Translation

For $A \subseteq \mathbb{R}$ and $t \in \mathbb{R},$ the translation of $t + A$ is defined by

$$A + t = \{ a + t : a \in A \}.$$

:::




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




:::{prf:defintion} Open cover, finite subcover

Suppose $A \subseteq \mathbb{R}.$

- A collection $\mathcal{C}$ of open intervals is called an open cover of $A$ if $A$ is contained in the union of the intervals in $\mathcal{C}.$
- An open cover $\mathcal{C}$ of $A$ is said to have a finite subcover if $A$ is contained in the union of some finite list of sets in $\mathcal{C}.$

:::



:::{prf:theorem} Heine-Borel

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