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
Then $|(q, q^{1/n}) - (0, 1)|_\infty = |q| + |q^{1/n} - 1| < \epsilon,$ from which it follows that $(0, 1)$ is a limit point of $A$ that is not contained in $A.$
:::

::::

::::{admonition} Exercise 1.3
Show that the maps $f, g: \mathbb{R}^2 \to \mathbb{R}$ given by $f(x, y) = x + y$ and $g(x, y) = xy$ are continuous with respect to the usual topology on $\mathbb{R}.$
Let $X$ be $\mathbb{R}$ equipped with the topology whose open sets are intervals of the form $(a, \infty).$
Are the maps $f, g: X \times X \to X$ continuous?

:::{dropdown} Solution
First, we show that the maps $f, g: \mathbb{R}^2 \to \mathbb{R}$ are continuous.
For this first part of the question we consider open balls to be taken with respect to the $\ell_1$ norm.
Let $U$ be an open set in $\mathbb{R}$ and $z = (x, y) \in f^{-1}(U).$
Then, note that, for all $(x', y') \in B_{\delta}(z),$ where $\delta = \epsilon / 2,$ we have

$$|f(x', y') - f(x, y)| = |x' - x + y' - y| < |x' - x| + |y' - y| < \epsilon.$$

for all $(x', y') \in B_\delta(z).$
Therefore, $f(B_{\delta}(z)) \subseteq U,$ which implies that $B_{\delta}(z) \subseteq f^{-1}(U),$ so $f$ is continuous.


Similarly, let $U$ be an open set in $\mathbb{R}$ and $z = (x, y) \in g^{-1}(U).$
Then, note that for all $(x', y') \in B_{\delta}(z),$ where $\delta = \sqrt{1 + \epsilon} - 1$ we have

$$\begin{align}
|g(x', y') - g(x, y)| = |x'y' - xy| &= |(x + (x' - x))(y + (y' - y)) - xy| \\
&= |x(y' - y) + y(x' - x) + (x' - x)(y' - y)| \\
&< |x||y' - y| + |y||x' - x| + |x' - x||y' - y| \\
&< 2\delta + \epsilon^2 \\
&= \epsilon \\
\end{align}$$

for all $(x', y') \in B_\delta(z).$
Therefore, $g(B_{\delta}(z)) \subseteq U,$ which implies that $B_{\delta}(z) \subseteq g^{-1}(U),$ so $g$ is continuous.

In the second part of the exercise we replace $\mathbb{R}^2$ with $X \times X,$ where $X = \mathbb{R}$ with the topology whose open sets are intervals of the form $(a, \infty).$

First, we show that $f$ is continuous under the product topology on $X \times X.$
Let $U$ be an open set in $X$ and $z = (x, y) \in f^{-1}(U).$
If $U = \emptyset$ or $U = X,$ then $f^{-1}(U) = \emptyset$ or $f^{-1}(U) = X \times X,$ respectively, which are both open.
Suppose instead that $U \neq \emptyset$ and $U \neq X.$
Then $U = (a, \infty)$ for some $a \in \mathbb{R}.$
Then

$$f^{-1}(U) = \{(x, y) \in X \times X \vert x + y > a\} = \bigcup_{x \in \mathbb{R}} (x, \infty) \times (a - x, \infty),$$

Noting that the sets $(x, \infty) \times (a - x, \infty)$ are open in the product topology on $X \times X,$ we see that $f^{-1}(U)$ is open in $X \times X,$ so $f$ is continuous.

Next we show that $g$ is not continuous under the product topology on $X \times X.$
Let $U = (-\infty, 0),$ which is open in $X.$
Then

$$g^{-1}(U) = (-\infty, 0) \times (0, \infty) \cup (0, \infty) \times (-\infty, 0).$$

We will show that $g^{-1}(U)$ is not open in $X \times X.$
Suppose instead $g^{-1}(U)$ is open in $X \times X.$
Note that $\mathbb{R}$ is open in $X,$ so

$$G = g^{-1}(U) \cap (0, \infty) \times \mathbb{R} = (0, \infty) \times (-\infty, 0)$$

is also open in $X \times X.$
However, this is a contradiction, because for any $z = (x, y) \in G,$ there do not exist sets $V_1 = (a, \infty) \times (b, \infty)$ and $V_2 = (c, \infty) \times (d, \infty)$ such that $x \in V_1$ and $y \in V_2$ and $V_1 \times V_2 \subseteq G,$ because for any $b \in \mathbb{R}$ we have $(b, \infty) \not \subseteq (-\infty, 0).$
This is a contradiction, so $g^{-1}(U)$ is not open in $X \times X,$ and $g$ is not continuous.
:::
::::
