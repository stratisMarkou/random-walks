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
:name: topology:ex:1.1
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
:name: topology:ex:1.2
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


::::{admonition} Exercise 1.11
:class: tip
Exhibit a countable basis for the usual topology of $\mathbb{R}.$

:::{dropdown} Solution
The set $B = \{(q_1, q_2): q_1, q_2 \in \mathbb{Q}\}$ is countable.
We will show that it is a basis for the usual topology of $\mathbb{R}.$

Let $U$ be an open set in $\mathbb{R}.$
Then $U$ is the union of countably many open intervals $U_1, U_2, \dots.$
Each of these intervals can be written as $U_n = (a_n, b_n)$ for some $a_n, b_n \in \mathbb{R}$ and $n = 1, 2, \dots.$
We will show that each such interval is a countable union of sets in $B.$

First, for each $a_n,$ there exists a decreasing sequence $\tilde{a}_{n, 1} > \tilde{a}_{n, 2}, \dots \in \mathbb{Q}$ which converges to $a$ from above.
Similarly, for each $b_n,$ there exists an increasing sequence $\tilde{b}_{n, 1} < \tilde{b}_{n, 2}, \dots \in \mathbb{Q}$ which converges to $b$ from below.
Then $U_n = \cup_{m = 1}^\infty (\tilde{a}_{n, m}, \tilde{b}_{n, m}),$ which is a countable union of sets in $B.$
Therefore $U$ can also be written as a countable union of sets in $B,$ and so $B$ is a basis for $\mathbb{R}.$
:::
::::


::::{admonition} Exercise 1.13
:class: tip
Let $A = \{(0, 0, 1), (0, 0, -1)\} \subseteq S^2$ be the poles of the two-dimensional sphere.
Let $B \subseteq T^2$ be the image of $\mathbb{R} \times 0 \subseteq \mathbb{R}^2$ into the two dimensional torus.
Show that $S^2 / A$ is homeomorphic to $T^2 / B.$

:::{dropdown} Solution
For convenience, let us write $X = S^2 / A$ and $Y = T^2 / B.$
We will use polar coordinate notation to describe $S^2$ where $\theta \in [0, \pi]$ is the polar angle and $\phi \in [0, 2 \pi)$ is the azimuthal angle.
Similarly we can also use polar coordinate notation to describe $T^2$ where $\theta \in [0, \pi)$ is the polar angle and $\phi \in [0, 2 \pi)$ is the azimuthal angle.
Let $\pi_X: S^2 \to X$ and $\pi_Y: T^2 \to Y$ be the quotient maps.
Let $f: X \to Y$ be the map defined as:

$$\begin{equation}
f(\pi_X(\{(\theta, \phi)\})) = \begin{cases}
\{(\theta, \phi)\} & \text{if } \pi_X(\{(\theta, \phi)\}) \neq \pi_X(A) \\
\pi_Y(B) & \text{if } \pi_X(\{(\theta, \phi)\}) = \pi_X(A)
\end{cases}
\end{equation}$$

We will now show that $f$ is a homeomorphism between $X$ and $Y.$
First, by inspecting the definition of $f,$ we note that it is bijective.
Now we show that $f$ and $f^{-1}$ are continuous.

__Continuity:__
We show that $f$ is continuous.
Suppose $U$ is an open set in $Y.$
Define the mapping $\iota: S^2 \setminus A \to T^2 \setminus B$ as the identity map in polar coordinates, and note that it is bijective and continuous, so it is a homeomorphism.
Now we consider two possible cases:
either $U$ contains $\pi_Y(B)$ or it does not.

If $U$ does not contain $\pi_Y(B),$ then $\pi_Y^{-1}(U)$ is in the domain of $\iota^{-1},$ and we can write

$$f^{-1}(U) = (\pi_X \circ \iota^{-1} \circ \pi^{-1}_Y)(U).$$

Therefore $f^{-1}(U)$ is open in $X,$ as $(\iota^{-1} \circ \pi^{-1}_Y)(U)$ is open in $S^2.$ 

If $U$ contains $\pi_Y(B),$ then $\pi_Y^{-1}(U)$ is an open set that contains $B.$
Now, the pre-image of $\pi_Y^{-1}(U) \setminus B$ under $\iota$ is an open set in $S^2$ and furthermore, adding $A$ to this set does not change the fact that it is open, i.e. $\iota^{-1}(\pi_Y^{-1}(U) \setminus B) \cup A$ is open in $S^2.$
We can now write

$$f^{-1}(U) = \pi_X(\iota^{-1}(\pi_Y^{-1}(U) \setminus B) \cup A),$$

and since $\iota^{-1}(\pi_Y^{-1}(U) \setminus B) \cup A$ is open in $S^2,$ we have that $f^{-1}(U)$ is open in $X.$
We have therefore shown that $f$ is continuous.

__Continuity of inverse:__
We can similarly show that $f^{-1}$ is continuous.
Let $V$ be an open set in $X.$
Again, we consider two cases:
either $V$ contains $\pi_X(A)$ or it does not.

If $V$ does not contain $\pi_X(A),$ then $\pi_X^{-1}(V)$ is in the domain of $\iota,$ and we can write

$$f(\pi_X^{-1}(V)) = (\pi_Y \circ \iota \circ \pi^{-1}_X)(V).$$

Therefore $f(\pi_X^{-1}(V))$ is open in $Y,$ as $(\iota \circ \pi^{-1}_X)(V)$ is open in $T^2.$

If $V$ contains $\pi_X(A),$ then $\pi_X^{-1}(V)$ is an open set that contains $A.$
Now, the image of $\pi_X^{-1}(V) \setminus A$ under $\iota$ is an open set in $T^2$ and furthermore, adding $B$ to this set does not change the fact that it is open, i.e. $\iota(\pi_X^{-1}(V) \setminus A) \cup B$ is open in $T^2.$
We can now write

$$f(\pi_X^{-1}(V)) = \pi_Y(\iota(\pi_X^{-1}(V) \setminus A) \cup B),$$

and since $\iota(\pi_X^{-1}(V) \setminus A) \cup B$ is open in $T^2,$ we have that $f(\pi_X^{-1}(V))$ is open in $Y.$
We have therefore shown that $f^{-1}$ is continuous.
:::
::::



::::{admonition} Exercise 1.14
:class: tip
Let $||\cdot||: \mathbb{R}^2 \to \mathbb{R}$ be a function which satisifes all the axioms for a norm except possibly the triangle inequality.
Let $B = \{v \in \mathbb{R} : ||v|| \leq 1\}.$
Show that $||\cdot||$ is a norm if and only if $B$ is a convex subset of $\mathbb{R}^2.$
For $r \in (0, \infty),$ let $||v||_r = (|v_1|^r + |v_2|^r)^{1/r}$ for $v = (v_1, v_2) \in \mathbb{R}^2.$
Deduce that $||\cdot||_r$ is a norm if and only if $r \geq 1.$

:::{dropdown} Solution
__First part:__
Suppose $||\cdot||$ is a norm.
Let $v_1, v_2 \in B$ and $t \in [0, 1].$
Then by the triangle inequality

$$\begin{equation}
||tv_1 + (1 - t)v_2|| \leq t||v_1|| + (1 - t)||v_2|| \leq t + (1 - t) = 1,
\end{equation}$$

so $B$ is convex.
Conversely, suppose $B$ is convex.
Let $v_1, v_2 \in \mathbb{R}^2$ and $t \in [0, 1].$
If $v_1 = v_2 = 0,$ then the triangle inequality holds, so suppose that at least one of $v_1$ and $v_2$ is non-zero, and set $m = ||v_1|| + ||v_2|| \neq 0.$
Then we have $v_1 / m, v_2 / m \in B.$
By the convexity of $B$ we have $t(v_1 / m) + (1 - t)(v_2 / m) \in B,$ so

$$\begin{align}
||tv_1 + (1 - t)v_2|| &= m||t(v_1 / m) + (1 - t)(v_2 / m)|| \\
&\leq m ||v_1 / m|| + m ||v_2 / m|| \\
&= ||v_1|| + ||v_2||.
\end{align}$$

Therefore $||\cdot||$ is a norm.

__Second part:__
Let $r \in (0, \infty).$
Without loss of generality, suppose $v_1, v_2 > 0,$ and consider the level set $||v||_r = (v_1^r + v_2^r)^{1/r} = 1.$
Then, whenever $0 < r < 1,$ the level set is not convex, because the line segment connecting $(1, 0)$ and $(0, 1)$ is not contained in the level set.
Therefore $||\cdot||_r$ is not a norm for $r < 1.$
Conversely, suppose $r \geq 1.$
Then the level set $||v||_r = 1$ is convex, so $||\cdot||_r$ is a norm for $r \geq 1.$
:::
::::


::::{admonition} Exercise 1.16
:class: tip
Show that the set of piecewise linear functions is dense in $C[0, 1]$ with the uniform metric.
By considering piecewise linear functions where each linear piece is given by an expression with rational coefficients, deduce that $C[0, 1]$ has a countable dense subset.

:::{dropdown} Solution
__First part:__
Let $f \in C[0, 1]$ equiped with the uniform metric.
Let $\epsilon > 0.$
Then, there exists $\delta > 0$ such that for all $x, y \in [0, 1]$ with $|x - y| < \delta,$ we have $|f(x) - f(y)| < \epsilon.$
Pick $N \in \mathbb{N}$ such that $1/N < \delta.$
Then, the piecewise linear function $g: [0, 1] \to \mathbb{R}$ that interpolates between $((n / N), f(n / N))$ and $((n + 1) / N, f((n + 1) / N))$ for $n = 0, 1, \dots, N - 1$ is within $\epsilon$ of $f$ for any $x \in [0, 1],$ which can be shown as follows.
Suppose $x \in [n / N, (n + 1) / N].$
Then

$$\begin{align}
g(x) &= f\left(\frac{n}{N}\right) \left(x - n\right) + f\left(\frac{n + 1}{N}\right) \left(n + 1 - x\right) \\
&= f\left(\frac{n}{N}\right) \theta + f\left(\frac{n + 1}{N}\right) (1 - \theta),
\end{align}$$

where $\theta = (x - n / N).$
Note that $0 \leq \theta \leq 1.$
We have

$$\begin{align}
|f(x) - g(x)| &= |(f(x) - f(n / N)) \theta - (f(x) - f((n + 1) / N)) (1 - \theta)| \\
&\leq \theta |f(x) - f(n / N)| + (1 - \theta) |f(x) - f((n + 1) / N)| \\
&< \epsilon.
\end{align}$$

Therefore, the set of piecewise linear functions is dense in $C[0, 1]$ with the uniform metric.

__Second part:__
Let $f \in C[0, 1]$ equiped with the uniform metric.
Let $\epsilon > 0.$
We can find a piecewise linear function $g_\epsilon$ that is within $\epsilon / 2$ of $f,$ as measured with the uniform metric, from the first part of the exercise.
Now, we can also find a piecewise linear function $h_\epsilon$ with rational coefficients that is within $\epsilon / 2$ of $g_\epsilon,$ as measured with the uniform metric.
Therefore, $h_\epsilon$ is within $\epsilon$ of $f,$ as measured with the uniform metric.
Since the set of piecewise linear functions with rational coefficients is countable, we have shown that $C[0, 1]$ has a countable dense subset.
:::
::::


::::{admonition} Exercise 2.1
:class: tip
Which of the following subsets of $\mathbb{R}^2$ are (a) connected (b) path connected?

1. $B_1((1, 0)) \cup B_1((-1, 0))$
2. $\bar{B}_1((1, 0)) \cup \bar{B}_1((-1, 0))$
3. $\{(x, y) \in \mathbb{R}^2: y = 0 \text{ or } x / y \in \mathbb{Q}\}$
4. $\{(x, y) \in \mathbb{R}^2: y = 0 \text{ or } x / y \in \mathbb{Q}\} - \{(0, 0)\}$

:::{dropdown} Solution
__Set 1:__
This set is not connected because it is the union of two disjoint open balls in $\mathbb{R}^2.$
It is therefore also not path connected.

__Set 2:__
This set is path connected because:
any two points in $\bar{B}_1((1, 0))$ are connected by a path; any two points in $B_1((-1, 0))$ are connected by a path; a pair of points consisting of a point in $\bar{B}_1((1, 0))$ and a point in $B_1((-1, 0))$ are connected by a path that goes through the point $(0, 0).$
Therefore, the set is path connected, so it is also conneted.

__Set 3:__
This is the set of all straight lines that pass through the origin and have a rational slope, as well as the $y$ axis.
From any point in this set, we can find a path to any other point in the set, by first passing through the origin, and then to the other point.
Therefore, the set is path connected, so it is also connected.

__Set 4:__
This set is not connected, and therefore also not path connected, and this can be shown as follows.
Let us denote this set as $S.$
Let $q \in \mathbb{R} \setminus \mathbb{Q}.$
Consider the sets $A = \{(x, y): y > qx\}$ and $B = \{(x, y): y < qx\}.$
Then, the sets $S \cap A$ and $S \cap B$ are nonempty, disjoint, and open in $S,$ so $S$ is not connected.
:::
::::



::::{admonition} Exercise 2.2
:class: tip
Suppose that $X$ is connected, and that $f: X \to Y$ is a locally constant map, i.e. for every $x \in X,$ there is an open neighbourhood $U$ of $x$ such that $f(x) = f(x')$ for all $x' \in U.$
Show that $f$ is constant.

:::{dropdown} Solution
Let $x \in X$ and $y = f(x).$
Now, consider the sets $A_z = f^{-1}(z),$ and $X \setminus A_z.$
The set $A_y$ is non-empty because $x \in A_y.$
If the set $X \setminus A_y$ is empty, we are done because that means that $f$ is constant and equal to $y,$ so suppose that $X \setminus A_y$ is non-empty.
Note that $A_y$ and $X \setminus A_y$ are disjoint by definition.
We will show that both $A_y$ and $X \setminus A_y$ are open sets.

Let $z \in Y.$
Then, for each $a \in A_z,$ we have that $f$ is locally constant at $a,$ so there exists an open neighbourhood $U_a$ of $a$ such that $f(a') = f(a)$ for all $a' \in U_a.$
In addition, by the definition of $A_z,$ we have that $f(a) = z,$ so $U_a \subseteq A_z$ for all $a \in A_z.$
Thus we can write

$$A_z = \bigcup_{a \in A_z} U_a,$$

where each $U_a$ is open.
Since $A_z$ can be written as a union of open sets, it is open for each $z \in Y.$
Therefore $A_y$ is open.
In addition, since $X \setminus A_y = \cup_{z \in Y: z \neq y} A_z,$ we have that $X \setminus A_y$ is open.
Therefore $A_y$ and $X \setminus A_y$ are non-empty, disjoint, and open, so $X$ is not connected, which is a contradiction.
Therefore $f$ is constant.
:::
::::



::::{admonition} Exercise 2.3
:class: tip
:name: topology:ex-2-3
Show that the product of two connected spaces is connected.

:::{dropdown} Solution 1
Let $X$ and $Y$ be connected spaces.
Suppose that $X \times Y$ is not connected.
Then there exist non-empty disjoint open sets $U$ and $V$ in $X \times Y$ such that $X \times Y = U \cup V.$

Now, for each $x \in X$ the subspace $\{x\} \times Y$ is homeomorphic to $Y,$ so it is connected.
Similarly, for each $y \in Y$ the subspace $X \times \{y\}$ is homeomorphic to $X,$ so it is connected.

For each $x \in X,$ let $S_x = \{x\} \times Y.$
There are two possibilities: (1) there exists some $x \in X$ such that $S_x \cap U \neq \emptyset$ and $S_x \cap V \neq \emptyset,$ or (2) for all $x \in X,$ either $S_x \subseteq U$ or $S_x \subseteq V.$

In the first case, the sets $S_x \cap U$ and $S_x \cap V$ are non-empty, disjoint, and open in $S_x,$ so $S_x$ is not connected, which is a contradiction because $S_x$ is homeomorphic to $Y$ and $Y$ is connected.

In the second case, we must have that $S_x \subseteq U$ for some $x \in X$ and $S_x \subseteq V$ for some $x \in X,$ because otherwise one of the sets $U$ and $V$ would be empty.
From this, we conclude that, for each $y$ the set $T_y = X \times \{y\}$ must intersect both $U$ and $V.$
Then, similarly to the first case, we have that $T_y \cap U$ and $T_y \cap V$ are non-empty, disjoint, and open in $T_y,$ so $T_y$ is not connected, which is a contradiction because $T_y$ is homeomorphic to $X$ and $X$ is connected.
:::
::::


::::{admonition} Exercise 2.4
:class: tip

Show that there is no continuous injective map $f: \mathbb{R}^2 \to \mathbb{R}.$

:::{dropdown} Solution
Suppose there exists a continuous injective map $f: \mathbb{R}^2 \to \mathbb{R}.$
Now consider the subset $\mathbb{R} \setminus \{0\}$ of $\mathbb{R}.$
This is a disconnected set because it can be written as the union of the two disjoint open sets $(-\infty, 0)$ and $(0, \infty).$

Now, because $f$ is injective, the set $f^{-1}(\mathbb{R} \setminus \{0\})$ is equal to $\mathbb{R}^2$ with a single point, the point $f^{-1}(0),$ removed from it.
The set $f^{-1}(\mathbb{R}) \setminus f^{-1}(\{0\})$ is connected because it is path connected.
However, since $f$ is continuous, the sets $f^{-1}((-\infty, 0))$ and $f^{-1}((0, \infty))$ are open, disjoint and their union equals $f^{-1}(\mathbb{R}) \setminus f^{-1}(\{0\}),$ which must therefore be disconnected, arriving at a contradiction.
Therefore, there is no continuous injective map $f: \mathbb{R}^2 \to \mathbb{R}.$
:::
::::



::::{admonition} Exercise 2.5
:class: tip

Show that $\mathbb{R}^2$ with the topology induced by the British railway metric is not homeomorphic to $\mathbb{R}^2$ with the topology induced by the Euclidean metric.

:::{dropdown} Solution
Let $A$ be $\mathbb{R}^2$ with the British railway metric, and let $B$ be $\mathbb{R}^2$ with the Euclidean metric.
Suppose there exists $f: A \to B$ that is a homeomorphism.

Now, note that $A \setminus \{(0, 0)\}$ can be written as the union of half-open rays emanating from the origin, which are open sets in $A.$
We can take the union of all these rays that have $x \geq 0$ to obtain an open set in $A$ and we can take the union of all these rays that have $x < 0$ to obtain another open set in $A.$
These two open sets are disjoint and their union is $A \setminus \{(0, 0)\},$ so $A \setminus \{(0, 0)\}$ is disconnected.

By contrast, noting that $\{f^{-1}((0, 0))\}$ is a singleton subset of $B,$ we have that $B \setminus \{f^{-1}((0, 0))\}$ is connected because it is path connected.
Therefore, $f$ cannot be a homeomorphism, so $A$ is not homeomorphic to $B.$
:::
::::


::::{admonition} Exercise 2.6
:class: tip
:name: topology:ex-2-3
Let $X$ be a topological space.
If $A$ is a connected subspace of $X,$ show that $\overline{A}$ is also connected.
Deduce that any connected component of $X$ is a closed subset of $X.$

:::{dropdown} Solution
Let $X$ be a topological space, and let $A$ be a connected subspace of $X.$
Suppose $\overline{A}$ is not connected, i.e. there exist non-empty and disjoint $B, C \subseteq \overline{A}$ that are open in the subspace topology of $\overline{A}.$
Then, the sets $B' = A \cap B$ and $C' = A \cap C$ are open in the subspace topology of $A,$ and in addition they are disjoint because $B$ and $C$ are disjoint.
This means that at least one of $B'$ or $C'$ must be empty, because otherwise they would disconnect $A.$
Without loss of generality, suppose $C' = \emptyset.$
Now, take $x \in C.$
Since $x \in \overline{A},$ any open set containing $x$ must intersect $A$ which leads to a contradiction, because we just assumed $A \cap C = \emptyset.$
Therefore $\overline{A}$ is connected.

Now, let $x \in X$ and suppose $C(x) \subseteq X$ is the connected component of $x.$
From the result we just showed, since $C(x)$ is connected, $\overline{C(x)}$ is also connected.
Therefore $\overline{C(x)}$ is a connected set containing $x,$ so $\overline{C(x)} \subseteq C(x),$ which implies that $C(x) = \overline{C(x)}.$
We conclude that any connected component of $X$ is a closed subset of $X.$
:::
::::