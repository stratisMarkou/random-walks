# Exercises

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

:::{margin}
If $p$ is a prime number, the $p$-adic metric on $\mathbb{Z}$ is defined as

$$|a - b|_p = p^{-n},$$

where $n$ is the largest integer such that $p^n$ divides $a - b$.
:::
::::{admonition} Exercise 1.1
:label: topology:ex:1.1
Show that the sequence $2015, 20015, 200015, 2000015, \ldots$ converges in the 2-adic metric on $\mathbb{Z}$.

:::{dropdown} Solution
We show that the sequence converges to $15$ in the 2-adic metric.
Let $a_n$ be the $n$th term of the sequence.
Then $a_n - 15 = 2 \times 10^{n + 2}.$
Note that $2 \times 10^{n + 2}$ is divisible by $2^{n + 3}.$
Therefore, $|a_n - 15|_2 = 2^{-(n + 3)} \to 0$ as $n \to \infty.$
:::
::::


::::{admonition} Exercise 1.2
:label: topology:ex:1.2
Determine whether the following subsets $A \subseteq \mathbb{R}^2$ are open, closed or neither, under the standard topology on $\mathbb{R}^2.$

1. $A = \{(x, y) \in \mathbb{R}^2 \vert x < 0\} \cup \{(x, y) \in \mathbb{R}^2 \vert x > 0, y > 1 / x\}.$
2. $A = \{(x, \sin(1 / x)) \in \mathbb{R}^2 \vert x > 0\} \cup \{(0, y) \in \mathbb{R}^2 \vert y \in [-1, 1]\}.$
3. $A = \{(x, y) \in \mathbb{R}^2 \vert x \in \mathbb{Q} \text{ and } x = y^n \text{ for some } n \in \mathbb{N}\}.$

:::{dropdown} Solution
__Set 1:__
The set

$$A = \{(x, y) \in x < 0\} \cup \{(x, y) \in x > 0, y > 1 / x\}$$

is open, because it is the union of two open sets

$$\{(x, y) \in x < 0\} ~\text{ and }~ \{(x, y) \in x > 0, y > 1 / x\}.$$

Note that the set $A$ cannot be closed, because the only sets that are both open and closed are the empty set and the entire space, and $A$ is neither.

__Set 2:__
First, note that the set $S_z = \{(x, \sin(1/x)): x > z\}$ is closed in $\mathbb{R}^2$ for any $z > 0.$
Therefore, its complement is open and the set

$$T_z = S_z' \cap \{(x, y) \in \mathbb{R}^2 \vert x > z\}$$

is also open in $\mathbb{R}^2.$
Then the set

$$U_z = T_z \cap \{(x, y) \in \mathbb{R}^2 \vert |y| > 1\} \cap \{(x, y) \in \mathbb{R}^2 \vert x \notin [0, z]\}$$

is also open because it is the intersection of open sets.
Since $A = \bigcup_{z > 0} U_z,$ the set $A$ is open in $\mathbb{R}^2.$

Again, note that the set $A$ cannot be closed, by the same reasoning that was used to argue for set 1.

__Set 3:__
The set $A$ is not open because for any rational $x \in \mathbb{Q},$ there exists an irrational $x' \in \mathbb{R} \setminus \mathbb{Q}$ that is arbitrarily close to it, so for any $(x, y) \in A,$ there exists an $(x', y)$ that is aribtrarily close to it but is not in $A,$ because $x'$ is irrational.
In addition, the set $A$ is not closed because it does not contain all its {prf:ref}`limit points <topology:def-limit-point>`.
For example, consider the point $(0, 1) \in \mathbb{R}^2.$
This is a limit point of the set $A$: for any $\epsilon > 0,$ there exists a rational $q \in \mathbb{Q}$ such that $0 < |q| < \epsilon / 2$ and a sufficiently large $n \in \mathbb{N}$ such that $|q^{1/n} - 1| < \epsilon / 2.$
Then $|(q, q^{1/n}) - (0, 1)|_\infty = |q| + |q^{1/n} - 1| < \epsilon,$ so $(0, 1)$ is a limit point of $A.$
:::

::::
