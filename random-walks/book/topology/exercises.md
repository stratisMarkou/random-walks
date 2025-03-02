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
:class: tip
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
:class: tip
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
:class: tip
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


::::{admonition} Exercise 1.4
:class: tip
:label: topology:ex:1.4
Let $C^1([0, 1])$ be the set of continuously differentiable functions on $[0, 1],$ that is differentiable functions whose first derivative is continuous.
For $f \in C^1([0, 1]),$ define

$$||f||_{1, 1} = \int_0^1 |f(x)| \, dx + \int_0^1 |f'(x)| \, dx.$$

Show that $||\cdot||_{1, 1}$ is a norm on $C^1([0, 1]).$
If a sequence $(f_n)$ converges with respect to this norm, show that it also converges with respect to the uniform norm.
Give an example to show that the converse statement does not hold.

:::{dropdown} Solution

__First part:__
First, we show that $||\cdot||_{1, 1}$ is a norm on $C^1([0, 1]),$ by showing that it satisfies the {prf:ref}`properties of a norm <topology:def-norm>`.

__Positive definiteness:__
By the definition of $||\cdot||_{1, 1},$ we have $||f||_{1, 1} \geq 0,$ for all $f \in C^1([0, 1]).$

__Non-degeneracy:__
Let $f \in C^1([0, 1]).$
If $f = 0,$ then $||f||_{1, 1} = 0.$
Conversely, suppose that $||f||_{1, 1} = 0.$
Then it must be the case that $|f(x)|$ is identically zero, because if it were not, then the integral $\int_0^1 |f(x)| \, dx$ would be positive since {prf:ref}`non-negative functions with zero integral are zero almost everywhere <topology:lemma-non-constant-positive-continuous-function-has-positive-integral>`.

__Homogeneity:__
Let $f \in C^1([0, 1])$ and $\lambda \in \mathbb{R}.$
Then

$$\begin{align}
||\lambda f||_{1, 1} &= \int_0^1 |\lambda f(x)| \, dx + \int_0^1 |\lambda f'(x)| \, dx \\
&= |\lambda| \int_0^1 |f(x)| \, dx + |\lambda| \int_0^1 |f'(x)| \, dx \\
&= |\lambda| ||f||_{1, 1}.
\end{align}$$

__Triangle inequality:__
Let $f, g \in C^1([0, 1]).$
Then

$$\begin{align}
||f + g||_{1, 1} &= \int_0^1 |f(x) + g(x)| \, dx + \int_0^1 |f'(x) + g'(x)| \, dx \\
&\leq \int_0^1 |f(x)| + |g(x)| \, dx + \int_0^1 |f'(x)| + |g'(x)| \, dx \\
&= \int_0^1 |f(x)| \, dx + \int_0^1 |f'(x)| \, dx + \int_0^1 |g(x)| \, dx + \int_0^1 |g'(x)| \, dx \\
&= ||f||_{1, 1} + ||g||_{1, 1}.
\end{align}$$

Therefore, $||\cdot||_{1, 1}$ is a norm on $C^1([0, 1]).$

__Second part:__
Here, we want to show that if a sequence $(f_n)$ in $C^1([0, 1])$ converges to some limit $f \in C^1([0, 1])$ with respect to the norm $||\cdot||_{1, 1},$ then it also converges to $f$ with respect to the uniform norm.
Without loss of generality, we can assume that $f = 0,$ because if $f \neq 0,$ then we can consider the sequence $(f_n - f)$ instead.

Let $(f_n)$ be a sequence in $C^1([0, 1])$ that converges with respect to the norm $||\cdot||_{1, 1}.$
Let $\epsilon > 0.$
Then there exists an $N \in \mathbb{N}$ such that for all $n \geq N,$ we have $||f_n - f||_{1, 1} < \epsilon / 2.$
Now, for each $f_n,$ with $n \geq N,$ there must exist at least one $x_n \in [0, 1]$ such that $|f(x_n)| < \epsilon / 2,$ because if not, then the integral $\int_0^1 |f(x_n)| \, dx$ would be at least $\epsilon / 2,$ which would be a contradiction.
Since $[0, 1]$ is a closed interval and each $f_n$ is continuous, each $f_n$ attains its maximum at some $x_n' \in [0, 1].$
Therefore, we have

$$\begin{align}
||f_n||_{\infty} &= |f(x_n')| \\
&\leq |f(x_n)| + |f(x_n') - f(x_n)| \\
&< \epsilon / 2 + |f(x_n') - f(x_n)| \\
&= \epsilon / 2 + \left| \int_{x_n}^{x_n'} f'(x) \, dx \right| \\
&\leq \epsilon / 2 + \int_{x_n}^{x_n'} |f'(x)| \, dx \\
&\leq \epsilon / 2 + ||f_n||_{1, 1} \\
&< \epsilon.
\end{align}$$

for all $n \geq N.$
Therefore $||f_n||_{\infty} < \epsilon$ for all $n \geq N,$ so $(f_n)$ converges to $f$ with respect to the uniform norm.

The converse statement does not hold.
A counterexample is the sequence of functions $(f_n)$ defined by $f_n(x) = \sin(2 \pi n^2 x) / n$ for $x \in [0, 1].$
This sequence converges to the zero function with respect to the uniform norm, because $|f_n|$ is bounded by $1 / n,$ which converges to zero.
However, the sequence does not converge to the zero function with respect to the norm $||\cdot||_{1, 1},$ because

$$\begin{align}
||f_n||_{1, 1} &= \int_0^1 \left| \frac{\sin(2 \pi n^2 x)}{n} \right| \, dx + \int_0^1 \left|2 \pi  n \cos(2 \pi n^2 x) \right| \, dx \\
&> 2 \pi n \int_0^1 \left|\cos(2 \pi n^2 x) \right| \, dx.
\end{align}$$

Now, note that the integral on the right hand side is constant in $n,$ so $||f_n||_{1, 1}$ is unbounded as $n \to \infty.$
Therefore, the sequence $(f_n)$ does not converge to the zero function with respect to the norm $||\cdot||_{1, 1}.$
:::
::::


::::{admonition} Exercise 1.5
:class: tip
Let $d: X \times X \to \mathbb{R}$ be a function which satisfies all the axioms for a {prf:ref}`metric <topology:def-metric-space>` except for the requirement that $d(x, y) = 0 \implies x = y.$
For $x, y \in X,$ define $x \sim y$ if $d(x, y) = 0.$
Show that $\sim$ is an equivalence relation on $X,$ and that $d$ induces a metric on the quotient topology $X / \sim.$

:::{dropdown} Solution
First we show that $\sim$ is an equivalence relation on $X.$
For this, we need to show the three properties of an equivalence relation are satisfied, namely: reflexivity, symmetry, and transitivity.
Reflexivity is satisfied because if $x \in X,$ then by the triangle inequality for the metric $d,$ we have $d(x, x) = 0,$ which implies that $x \sim x.$
Symmetry is satisfied because if $x, y \in X$ and $d(x, y) = 0,$ then $d(y, x) = 0$ by the symmetry of the metric $d.$
Transitivity is satisfied because if $x, y, z \in X$ and $x \sim y$ and $y \sim z,$ then $d(x, y) = d(y, z) = 0,$ so by the triangle inequality for the metric $d,$ we have $d(x, z) = 0,$ so $x \sim z.$

Next, we show that $d$ induces a metric on the quotient topology $X / \sim.$
For this, we need to show that the function $\tilde{d}: (X / \sim) \times (X / \sim) \to \mathbb{R}$ defined by $\tilde{d}([x], [y]) = d(x, y)$ is a metric on $X / \sim.$
Before we start, we show that the function $\tilde{d}$ is well-defined, meaning that no matter which representatives of the equivalence classes we use to compute $\tilde{d},$ the result is the same.
Let $[x] = [x']$ and $[y] = [y'],$ for some $x, x', y, y' \in X.$
Since $x$ and $x'$ are in the same equivalence class, we have $d(x, x') = 0,$ and similarly $d(y, y') = 0.$
Therefore, by the triangle inequality for the metric $d,$ we have

$$d(x, y) \leq d(x, x') + d(x', y') + d(y', y) = d(x', y').$$

Similarly, we can exchange the roles of the $x, y$ and $x', y'$ to show that $d(x', y') \leq d(x, y)$ from which we have that $d(x, y) = d(x', y'),$ which means that $\tilde{d}(x, y) = \tilde{d}(x', y').$
Therefore the value of $\tilde{d}$ does not depend on the choice of representative we make, so $\tilde{d}$ is well-defined.

Now we show that $\tilde{d}$ satisfies the properties of a metric.
Let $x, y, z \in X.$
First, we have that $\tilde{d}([x], [y]) = d(x, y) \geq 0,$ because $d$ is a metric.
Second, we have that

$$\tilde{d}([x], [y]) = 0 \iff d(x, y) = 0 \iff x \sim y \iff [x] = [y].$$

Third, we have that

$$\tilde{d}([x], [y]) = d(x, y) = d(y, x) = \tilde{d}([y], [x]).$$

Lastly, we have

$$\tilde{d}([x], [y]) = d(x, y) \leq d(x, z) + d(z, y) = \tilde{d}([x], [z]) + \tilde{d}([z], [y]).$$
:::
::::


::::{admonition} Exercise 1.6
:class: tip
Find a closed $A_1 \subseteq \mathbb{R}$ (with the standard topology) such that $\overline{\text{Int}(A_1)} \neq A_1$ and an open $A_2 \subseteq \mathbb{R}$ such that $\text{Int}(\overline{A_2}) \neq \text{Int}(A_2).$

:::{dropdown} Solution
Let $A_1 = \{0\},$ which is a closed set.
Then $\text{Int}(A_1) = \emptyset$ so $\overline{\text{Int}(A_1)} = \emptyset \neq \text{Int}(\overline{A_1}).$

Let $A_2 = \mathbb{R} \setminus \{0\},$ which is an open set.
Then $\overline{A_2} = \mathbb{R}$ so $\text{Int}(\overline{A_2}) = \mathbb{R} \neq A_2.$
:::
::::

::::{admonition} Exercise 1.7
:class: tip
Let $f: X \to Y$ be a map between topological spaces.
Show that $f$ is continuous if and only if $f(\overline{A}) \subseteq \overline{f(A)}$ for all $A \subseteq X.$
Deduce that if $f$ is surjective and continuous, the image of a dense set in $X$ is dense in $Y.$

:::{dropdown} Solution
__First part:__
Suppose $f$ is continuous.
Let $A \subseteq X.$
Note that

$$\overline{f(A)} = \bigcap_{C \in \mathcal{C}_{f(A)}} C,$$

that is, the closure of $f(A)$ is the intersection of all closed sets containing $f(A).$
Now consider

$$f^{-1}\left(\overline{f(A)}\right) = f^{-1}\left( \bigcap_{C \in \mathcal{C}_{f(A)}} C \right) \supseteq \bigcap_{C \in \mathcal{C}_{f(A)}} f^{-1}(C) = \bigcap_{C \in \mathcal{C}_{A}} C = f(\overline{A}).$$

where in the second to last inequality we have used the fact that if a set $C$ is closed and contains $f(A),$ then $f^{-1}(C)$ is closed (by the continuity of $f$) and contains $A.$
Applying $f$ to both sides of the above equation, we obtain $f(\overline{A}) \subseteq \overline{f(A)}.$
Conversely suppose that $f(\overline{A}) \subseteq \overline{f(A)}$ for all $A \subseteq X.$ 
Let $B \subseteq Y$ be closed, and let $A = f^{-1}(B).$
Then we have

$$f(\overline{A}) \subseteq \overline{f(A)} \implies f(\overline{f^{-1}(B)}) \subseteq \overline{B} = B.$$

Now $f(\overline{f^{-1}(B)}) = B$ can hold only if $\overline{f^{-1}(B)} = f^{-1}(B),$ because otherwise the set $\overline{f^{-1}(B)} \setminus f^{-1}(B)$ would be nonempty and that would imply that $f(\overline{f^{-1}(B)}) \neq B.$
Finally, $\overline{f^{-1}(B)} = f^{-1}(B)$ implies that $f^{-1}(B)$ is closed, so $f$ is continuous.

__Second part:__
Suppose $f$ is surjective and continuous, and let $A \subseteq X$ be dense.
Since $f$ is surjective, we have $f(X) = Y$ so

$$\overline{f(A)} \supset f(\overline{A}) = f(X) = Y.$$

which implies $\overline{f(A)} = Y,$ so $f(A)$ is dense in $Y.$
:::
::::


::::{admonition} Exercise 1.8
:class: tip
Suppose $X$ is a topological space and $Z \subseteq Y \subseteq X.$
If $Y$ is dense in $X$ and $Z$ is dense in $Y,$ must $Z$ be dense in $X$?

:::{dropdown} Solution
Suppose $C \subseteq X$ is closed and $Z \subseteq C.$
Since $C$ is closed, $C \cap Y$ is closed in the subspace topology on $Y.$
Since $Z$ is dense in $Y,$ and $C \cap Y$ is a closed set that contains $Z,$ we have $C \cap Y = Y.$
Therefore $C \supseteq Y.$
Finally, since $C$ is a closed set that contains $Y$ and $Y$ is dense in $X,$ we have $C = X,$ so $Z$ is dense in $X.$
:::
::::


::::{admonition} Exercise 1.9
:class: tip
Define a topology on $\mathbb{R}$ by declaring the closed subsets to be those which are (1) closed in the usual topology and (2) either bounded or all of $\mathbb{R}.$
Show that this is a topology, that all points of $\mathbb{R}$ are closed with respect to it, but that the topology is not Hausdorff.

:::{dropdown} Solution
__First part:__
Suppose $x \in \mathbb{R}.$
The set $\{x\}$ is closed in the usual topology on $\mathbb{R}$ and is bounded, so it is closed in the new topology.

__Second part:__
Suppose $x_1, x_2 \in \mathbb{R}$ and $x_1 \neq x_2.$
Let $U_1$ and $U_2$ be open sets in the new topology such that $x_1 \in U_1$ and $x_2 \in U_2.$
Now, $U_1$ and $U_2$ cannot be empty because they contain $x_1$ and $x_2,$ so their complements can't be all of $\mathbb{R}$ and must therefore be bounded.
Since $\mathbb{R} \setminus U_1$ and $\mathbb{R} \setminus U_2$ are bounded, their union $(\mathbb{R} \setminus U_1) \cup (\mathbb{R} \setminus U_2)$ is also bounded.
Therefore, the set

$$U_1 \cap U_2 = \mathbb{R} \setminus ((\mathbb{R} \setminus U_1) \cup (\mathbb{R} \setminus U_2))$$

is non-empty, because it is the complement of a bounded set.
Therefore $U_1$ and $U_2$ are not disjoint, so the topology is not Hausdorff.
:::
::::


::::{admonition} Exercise 1.10
:class: tip
The diagonal in $X \times X$ is the set $\Delta = \{(x, x) \in X \times X | x \in X \}.$
If $X$ is a {prf:ref}`Haussdorff space <topology:def-hausdorff-space>`, show that $\Delta$ is a closed subset of $X \times X.$

:::{dropdown} Solution
Let $X$ be a {prf:ref}`Hausdorff space <topology:def-hausdorff-space>`.
We will show that the complement of $\Delta$ is open.

Let $(x_1, x_2) \in X \times X \setminus \Delta.$
Then $x_1 \neq x_2.$
Since $X$ is Hausdorff, there exist open sets $U_x$ and $U_y$ in $X$ such that $x_1 \in U_{x_1},$ $x_2 \in U_{x_2},$ and $U_{x_1} \cap U_{x_2} = \emptyset.$
Then the set $U_{x_1} \times U_{x_2}$ is an open set in $X \times X$ that contains $(x_1, x_2)$ and $U_{x_1} \times U_{x_2} \cap \Delta = \emptyset,$ so $X \times X \setminus \Delta$ is open.
Therefore $\Delta$ is closed.
:::
::::
