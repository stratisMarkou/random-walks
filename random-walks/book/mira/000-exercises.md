# Exercises

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

This page gives solutions to the exercises from the book Measure, Integration and Real Analysis by Sheldon Axler.
We have been working through the book and exercises with Adrian Goldwaser, Bruno Mlodozeniec and Shreyas Padhy, and these solutions are a joint effort.
Please [email me](mailto:stratismar@gmail.com) if you find any errors in these solutions or have any other comments.

## Chapter 1.A

::::{admonition} Exercise 1.A.1
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function such that

$$L(f, P, [a, b]) = U(f, P, [a, b])$$

for some partition $P$ of $[a, b].$ Prove that $f$ is a constant function on $[a, b].$

:::{dropdown} Solution

Let $f$ be a function and $P$ be a partition $x_0, \ldots, x_N$ of $[a, b]$ such that

$$L(f, P, [a, b]) = U(f, P, [a, b]).$$

Note that for each $n = 1, \ldots, N,$ we have

$$(x_n - x_{n-1}) \inf_{x \in [x_{n-1}, x_n]} f = (x_n - x_{n-1}) \sup_{x \in [x_{n-1}, x_n]} f$$

The infimum and supremum of a funtion on any domain are equal if and only if $f$ is constant on this domain.
Therefore, $f$ is constant on each interval $[x_{n-1}, x_n],$ so it must be constant on $[a, b].$

:::

::::


::::{admonition} Exercise 1.A.2
:class: tip

Suppose $a \leq s < t \leq b.$
Define $f: [a, b] \to \mathbb{R}$ by

$$f(x) = \begin{cases}
1 & \text{if } s < x < t, \\
0 & \text{otherwise}.
\end{cases}$$

Prove that $f$ is Riemann integrable on $[a, b]$ and that $\int_a^b f = t - s.$

:::{dropdown} Solution

Let $P_N$ be the partition $x_0, \ldots x_{3n}$ of $[a, b]$ with $x_n = s$ and $x_{2n} = t,$ defined as

$$x_i - x_{i-1} = \begin{cases}
\frac{s - a}{n} \text{ if } 1 \leq i \leq n, \\
\frac{t - s}{n} \text{ if } n < i \leq 2n, \\
\frac{b - t}{n} \text{ if } 2n < i \leq 3n.
\end{cases}$$

This partition satisifies

$$\begin{align}
L(f, P_N, [a, b]) &= \sum_{i=1}^n \frac{s - a}{n} \inf_{x \in [x_{i-1}, x_i]} f + \sum_{i=n+1}^{2n} \frac{t - s}{n} \inf_{x \in [x_{i-1}, x_i]} f + \sum_{i=2n+1}^{3n} \frac{b - t}{n} \inf_{x \in [x_{i-1}, x_i]} f \\
&= \frac{t - s}{n} (n - 2),
\end{align}$$

where the $(n - 2)$ term comes from the fact that $f(x_n) = f(s) = 0$ and $f(x_{2n}) = f(t) = 0.$
Similarly for the upper Riemann sum, we have

$$\begin{align}
U(f, P_N, [a, b]) &= \sum_{i=1}^n \frac{s - a}{n} \sup_{x \in [x_{i-1}, x_i]} f + \sum_{i=n+1}^{2n} \frac{t - s}{n} \sup_{x \in [x_{i-1}, x_i]} f + \sum_{i=2n+1}^{3n} \frac{b - t}{n} \sup_{x \in [x_{i-1}, x_i]} f \\
&= (t - s).
\end{align}$$

Therefore

$$\inf_{n \in \mathbb{N}} \left[U(f, P_N, [a, b]) - L(f, P_N, [a, b])\right] = 0,$$

which implies that 

$$\inf_{n \in \mathbb{N}} \left[U(f, P_N, [a, b]) - L(f, P_N, [a, b])\right] \geq \inf_{n \in \mathbb{N}} U(f, P_N, [a, b]) - \sup_{n \in \mathbb{N}} L(f, P_N, [a, b])= 0.$$

Therefore $f$ is Riemann integrable on $[a, b]$ and that $\int_a^b f = t - s.$

:::

::::

::::{admonition} Exercise 1.A.3
:name: mira-ex-1a3
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
Prove that $f$ is Riemann integrable on $[a, b]$ if and only if for every $\epsilon > 0,$ there exists a partition $P$ of $[a, b]$ such that

$$U(f, P, [a, b]) - L(f, P, [a, b]) < \epsilon.$$

:::{dropdown} Solution

Let $f: [a, b] \to \mathbb{R}$ be a bounded function.

__Part 1:__ Suppose $f$ is Riemann integrable on $[a, b].$
Then by the definition of the Riemann integral, we have

$$\inf_P U(f, P, [a, b]) - \sup_P L(f, P, [a, b]) = 0$$

from which it follows that

$$\begin{align}
\inf_P U(f, P, [a, b]) - \sup_P L(f, P, [a, b]) = 0 && (\text{rearranging}) \\
\inf_{P, P'}\left[U(f, P, [a, b]) - L(f, P', [a, b])\right] =0 && (\text{rewriting inf using sup}) \\
\inf_{P, P'}\left[U(f, P \cup P', [a, b]) - L(f, P \cup P', [a, b])\right] =0 && (\text{refining partitions}) \\
\inf_{R}\left[U(f, R, [a, b]) - L(f, R, [a, b])\right] =0 && (\text{rewriting } R = P \cup P')
\end{align}$$

Therefore, for any $\epsilon > 0,$ there exists a partition $R$ of $[a, b]$ such that 

$$U(f, R, [a, b]) - L(f, R, [a, b]) < \epsilon.$$

__Part 2:__
Similarly, we can go in the other direction.
Suppose that for every $\epsilon > 0,$ there exists a partition $P$ of $[a, b]$ such that

$$U(f, P, [a, b]) - L(f, P, [a, b]) < \epsilon.$$

Then, taking the infimum over all partitions $P$ of $[a, b],$ we have

$$\begin{align}
\epsilon &\geq \inf_P \left[U(f, P, [a, b]) - L(f, P, [a, b])\right] \\
&\geq \inf_P U(f, P, [a, b]) + \inf_P (- L(f, P, [a, b])) \\
&= \inf_P U(f, P, [a, b]) - \sup_P L(f, P, [a, b]) \\
&= U(f, [a, b]) - L(f, [a, b]) \\
&\geq 0
\end{align}$$

Therefore, $U(f, [a, b]) = L(f, [a, b]),$ which means that $f$ is Riemann integrable on $[a, b].$

:::
::::



::::{admonition} Exercise 1.A.4
:class: tip
:name: mira-ex-1a4

Suppose $f, g: [a, b] \to \mathbb{R}$ are Riemann integrable.
Prove that $f + g$ is Riemann integrable on $[a, b]$ and that

$$\int_a^b (f + g) = \int_a^b f + \int_a^b g.$$

:::{dropdown} Solution

Let $f, g: [a, b] \to \mathbb{R}$ be Riemann integrable.
Note that for any $a \leq c \leq d \leq b,$ we have

$$\begin{align}
\inf_{[c, d]} f + g &\geq \inf_{[c, d]} f + \inf_{[c, d]} g, \\
\sup_{[c, d]} f + g &\leq \sup_{[c, d]} f + \sup_{[c, d]} g.
\end{align}$$

Therefore, for any partition $P$ of $[a, b],$ we have

$$\begin{align}
L(f, P, [a, b]) + L(g, P, [a, b]) &\leq L(f + g, P, [a, b]), \\
U(f, P, [a, b]) + U(g, P, [a, b]) &\geq U(f + g, P, [a, b]).
\end{align}$$

This implies that

$$\begin{align}
&U(f + g, P, [a, b]) - L(f + g, P, [a, b]) \leq \\
\leq &U(f, P, [a, b]) - L(f, P, [a, b]) + U(g, P, [a, b]) - L(g, P, [a, b]).
\end{align}$$

Let $\epsilon > 0.$
Now, from {ref}`exercise 1.A.3 <mira-ex-1a3>`, since $f$ and $g$ are Riemann integrable, there exist partitions $P_f$ and $P_g$ such that

$$\begin{align}
U(f, P_f, [a, b]) - L(f, P_f, [a, b]) &< \frac{\epsilon}{2}, \\
U(g, P_g, [a, b]) - L(g, P_g, [a, b]) &< \frac{\epsilon}{2}.
\end{align}$$

Defining the partition $P$ of $[a, b],$ to be the partition containing all the points in $P_f$ and $P_g,$ we have

$$\begin{align}
U&(f + g, P, [a, b]) - L(f + g, P, [a, b]) \\
\leq U&(f, P_f, [a, b]) - L(f, P_f, [a, b]) + U(g, P_g, [a, b]) - L(g, P_g, [a, b]) \\
&< \epsilon.
\end{align}$$

where in the inequality we have used {prf:ref}`the property of refined partitions <mira-thm-refining-partitions>`.

:::
::::



::::{admonition} Exercise 1.A.5
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Prove that the function $-f$ is Riemann integrable on $[a, b]$ and

$$\int_a^b (-f) = - \int_a^b f.$$

:::{dropdown} Solution

If $f$ is Riemann integrable, from {ref}`exercise 1.A.3<mira-ex-1a3>`, for any $\epsilon > 0,$ there exists a partition $P$ of $[a, b]$ such that

$$U(f, P, [a, b]) - L(f, P, [a, b]) < \epsilon.$$

Since $\inf_{[c, d]} -f = - \sup_{[c, d]} f,$ we have $U(-f, P, [a, b]) = - L(f, P, [a, b])$ so

$$U(-f, P, [a, b]) - L(-f, P, [a, b]) = U(f, P, [a, b]) - L(f, P, [a, b]) < \epsilon$$

Therefore, again from {ref}`exercise 1.A.3<mira-ex-1a3>`, it follows that $-f$ is also Riemann integrable on $[a, b],$ and

$$\int_a^b (-f) = - \int_a^b f.$$

:::
::::



::::{admonition} Exercise 1.A.6
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Suppose $g: [a, b] \to \mathbb{R}$ is a function such that $g(x) = f(x)$ for all but finitely many $x \in [a, b].$
Prove that $g$ is Riemann integrable on $[a, b]$ and

$$\int_a^b g = \int_a^b f.$$

:::{dropdown} Solution

Let $f: [a, b] \to \mathbb{R}$ be Riemann integrable and $g: [a, b] \to \mathbb{R}$ be a function such that $g(x) = f(x)$ for all but finitely many $x \in [a, b].$

Since $f$ and $g$ are equal for all but finitely many points, the function $h = f - g$ is zero for all but finitely many $x \in [a, b].$
Let $P_n$ be the uniform partition of $[a, b],$ namely $x_0, x_1, \ldots, x_n$ where

$$x_i - x_{i-1} = \frac{b - a}{n},$$

and let $C = \sup_{[a, b]} |h|.$
Then, for any $n \in \mathbb{N},$ we have

$$\begin{align}
U(h, P_n, [a, b]) - L(h, P_n, [a, b]) &\leq 2k \frac{b - a}{n} C, 
L(h, P_n, [a, b]) &\geq -2k \frac{b - a}{n} C,
\end{align}$$

where $k$ is the number of points in $[a, b]$ where $h$ is non-zero.
Therefore

$$\begin{align}
U(g, P_n, [a, b]) - L(g, P_n, [a, b]) \leq 4k \frac{b - a}{n} C,
\end{align}$$

and since $n$ can be made arbitrarily large it follows, by {ref}`exercise 1.A.3<mira-ex-1a3>`, that $h$ is Riemann integrable on $[a, b].$
Therefore, $g = f - h$ is also Riemann integrable on $[a, b],$ because it is a sum of two Riemann integrable functions, which we know from {ref}`exercise 1.A.4<mira-ex-1a4>` is Riemann integrable, and satisfies

$$\int_a^b g = \int_a^b f - \int_a^b h = \int_a^b f.$$

:::
::::



::::{admonition} Exercise 1.A.7
:class: tip
:name: mira-ex-1a7

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
For $n \in \mathbb{N},$ let $P_n$ denote the partition that divides $[a, b]$ into $2^n$ intervals of equal size.
Prove that

$$\lim_{n \to \infty} L(f, P_n, [a, b]) = L(f, [a, b]) \text{ and } \lim_{n \to \infty} U(f, P_n, [a, b]) = U(f, [a, b]).$$


:::{dropdown} Solution

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function, bounded above by $C$ and below by $-C,$ and define $L = L(f, [a, b]),$ which is finite because $f$ is bounded.
By the definition of supremum, for every $\epsilon > 0$ there exists a partition $R_\epsilon$ of $[a, b]$ such that

$$L(f, [a, b]) - L(f, R_\epsilon, [a, b]) < \epsilon.$$

Let $\delta(R_\epsilon)$ be the size of the smallest subinterval of $R_\epsilon,$ and let $E_{R_\epsilon, k}$ be the partition of $[a, b]$ into $2^{n+k}$ intervals of equal size, where $n \in \mathbb{Z}^+$ is the smallest positive integer such that $\frac{(b-a)}{2^n} \leq \delta(R_\epsilon).$
Now, note that

$$\begin{align}
\left|L(f, R_\epsilon, [a, b]) - L(f, E_{R_\epsilon, k}, [a, b])\right| &\leq \frac{|R_\epsilon|}{2^{n+k}} 2C,
\end{align}$$

where $|R_\epsilon|$ is the number of points in the partition $R_\epsilon.$
Let $k_\epsilon$ be the smallest integer such that

$$\frac{|R_\epsilon|}{2^{n+k_\epsilon}} 2C < \epsilon.$$

Then, for any $k \geq k_\epsilon,$ we have

$$\begin{align}
\left|L(f, [a, b]) - L(f, E_{R_\epsilon, k}, [a, b])\right| = 2\epsilon.
\end{align}$$

Therefore the sequence $L(f, E_{R_{1/n}, k_{1/n}}, [a, b])$ tends to $L(f, [a, b])$ as $n \to \infty.$
Note that this sequence is a subsequence of the increasing and bounded above sequence $L(f, P_n, [a, b]),$ so it must also converge to $L(f, [a, b]).$
Repeating this argument for the upper Riemann sums, we obtain an analogous result for the upper Riemann sum.
Thefore, we have

$$\lim_{n \to \infty} L(f, P_n, [a, b]) = L(f, [a, b]) \text{ and } \lim_{n \to \infty} U(f, P_n, [a, b]) = U(f, [a, b]).$$

:::
::::



::::{admonition} Exercise 1.A.8
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is Rieman integrable.
Prove that

$$\int_a^b f = \lim_{n \to \infty} \frac{b - a}{n} \sum_{j=1}^n f\left(a + \frac{j(b - a)}{n}\right).$$

:::{dropdown} Solution

This exercise follows the a similar argument to {ref}`exercise 1.A.7<mira-ex-1a7>`.
Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Since $f$ is Riemann integrable, it is bounded, so there exists $C > 0$ such that $|f(x)| \leq C$ for all $x \in [a, b].$
By the definition of supremum, for any $\epsilon > 0,$ there exists a partition $R_\epsilon$ of $[a, b]$ such that

$$L(f, [a, b]) - L(f, R_\epsilon, [a, b]) < \epsilon.$$

Let $\delta(R_\epsilon)$ be the size of the smallest subinterval of $R_\epsilon,$ let $n_\epsilon \in \mathbb{Z}^+$ be the smallest integer such that $(b - a)/n_\epsilon \leq \delta(R_\epsilon),$ and let $E_{R_\epsilon, k}$ be the partition of $[a, b]$ into $n_\epsilon + k$ intervals of equal size.
Then, we have that

$$|L(f, R_\epsilon, [a, b]) - L(f, E_{R_\epsilon, k}, [a, b])| \leq \frac{|R_\epsilon|}{n_\epsilon + k} 2C,$$

where $|R_\epsilon|$ is the number of points in the partition $R_\epsilon.$
Let $k_\epsilon$ be the smallest integer such that

$$\frac{|R_\epsilon|}{n_\epsilon + k_\epsilon} 2C < \epsilon.$$

Then, for any $k \geq k_\epsilon,$ we have

$$\begin{align}
\left|L(f, [a, b]) - L(f, E_{R_\epsilon, k}, [a, b])\right| < \epsilon.
\end{align}$$

Therefore, any partition $P_n$ of $[a, b]$ into $n > n_\epsilon + k_\epsilon$ intervals of equal size satisfies 

$$\left|L(f, [a, b]) - L(f, P_n, [a, b])\right| < \epsilon,$$

and $L(f, P_n, [a, b])$ converges to $L(f, [a, b])$ as $n \to \infty.$
Now, note that for any such partition $P_n$ of $[a, b],$ we have

$$\begin{align}
L(f, [a, b]) \geq \frac{b - a}{n} \sum_{j=1}^n f\left(a + \frac{j(b - a)}{n}\right) \geq \frac{b - a}{n} \sum_{j=1}^n \inf_{x \in [x_{j-1}, x_j]} f(x) = L(f, P_n, [a, b]),
\end{align}$$

where $x_j = a + j(b - a)/n,$ so taking the limit as $n \to \infty,$ we obtain

$$\lim_{n \to \infty} \frac{b - a}{n} \sum_{j=1}^n f\left(a + \frac{j(b - a)}{n}\right) = L(f, [a, b]) = \int_a^b f.$$

:::
::::



::::{admonition} Exercise 1.A.9
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is Rieman integrable.
Prove that if $c, d \in [a, b]$ and $a \leq c < d \leq b,$ then $f$ is Riemann integrable on $[c, d].$

:::{dropdown} Solution

Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable, and let $c, d \in [a, b]$ such that $a \leq c < d \leq b.$
Since $f$ is Riemann integrable, by {ref}`exercise 1.A.3<mira-ex-1a3>`, for any $\epsilon > 0,$ there exists a partition $P_\epsilon$ of $[a, b]$ such that

$$U(f, P_\epsilon, [a, b]) - L(f, P_\epsilon, [a, b]) < \epsilon.$$

Now, let $P_\epsilon'$ be the partition of $[a, b]$ obtained by adding the points $c$ and $d$ to $P_\epsilon.$
Then, by the {prf:ref}`property of refined partitions <mira-thm-refining-partitions>`, we have

$$U(f, P_\epsilon', [a, b]) - L(f, P_\epsilon', [a, b]) \leq U(f, P_\epsilon, [a, b]) - L(f, P_\epsilon, [a, b]) < \epsilon,$$

and letting $P_\epsilon''$ be the partition of $[c, d]$ containing all points of $P_\epsilon'$ in $[c, d],$ we have

$$U(f, P_\epsilon'', [c, d]) - L(f, P_\epsilon'', [c, d]) \leq U(f, P_\epsilon', [a, b]) - L(f, P_\epsilon', [a, b]) < \epsilon.$$

Therefore, for each $\epsilon,$ there exists a partition $P_\epsilon''$ of $[c, d]$ such that

$$U(f, P_\epsilon'', [c, d]) - L(f, P_\epsilon'', [c, d]) < \epsilon,$$

and using {ref}`exercise 1.A.3<mira-ex-1a3>` again, we conclude that $f$ is Riemann integrable on $[c, d].$

:::
::::




::::{admonition} Exercise 1.A.10
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $c \in (a, b).$
Prove that $f$ is Riemann integrable on $[a, b]$ if and only if $f$ is Riemann integrable on $[a, c]$ and $f$ is Riemann integrable on $[c, b].$
Furthermore, prove that if these conditions hold, then

$$\int_a^b f = \int_a^c f + \int_c^b f.$$

:::{dropdown} Solution

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $c \in (a, b).$

__Part 1:__
If $f$ is Rieman integrable on $[a, b],$ then by {ref}`exercise 1.A.3<mira-ex-1a3>`, for any $\epsilon > 0,$ there exists a partition $P_\epsilon$ of $[a, b]$ such that

$$U(f, P_\epsilon, [a, b]) - L(f, P_\epsilon, [a, b]) < \epsilon.$$

Let $P_\epsilon'$ be the partition of $[a, b]$ obtained by adding the point $c$ to $P_\epsilon.$
Then, by the {prf:ref}`property of refined partitions <mira-thm-refining-partitions>`, we have

$$U(f, P_\epsilon', [a, b]) - L(f, P_\epsilon', [a, b]) \leq U(f, P_\epsilon, [a, b]) - L(f, P_\epsilon, [a, b]) < \epsilon,$$

and defining $P|_{[x_1, x_2]}$ to be the partition of $[x_1, x_2]$ containing all points of $P$ in $[x_1, x_2],$ we have

$$\begin{align}
U(f, P_\epsilon'|_{[a, c]}, [a, c]) + U(f, P_\epsilon'|_{[c, b]}, [c, b]) &= U(f, P_\epsilon', [a, b]) \\
L(f, P_\epsilon'|_{[a, c]}, [a, c]) + L(f, P_\epsilon'|_{[c, b]}, [c, b]) &= L(f, P_\epsilon', [a, b])
\end{align}$$

from which, we arrive at

$$\begin{align}
U(f, P_\epsilon'|_{[a, c]}, [a, c]) - L(f, P_\epsilon'|_{[a, c]}, [a, c]) &\leq U(f, P_\epsilon', [a, b]) - L(f, P_\epsilon', [a, b]) < \epsilon, \\
U(f, P_\epsilon'|_{[c, b]}, [c, b]) - L(f, P_\epsilon'|_{[c, b]}, [c, b]) &\leq U(f, P_\epsilon', [a, b]) - L(f, P_\epsilon', [a, b]) < \epsilon.
\end{align}$$

So $f$ is Riemann integrable on $[a, c]$ and $f$ is Riemann integrable on $[c, b],$ with

$$\int_a^b f = \int_a^c f + \int_c^b f.$$

__Part 2:__
Going the other direction, if $f$ is Riemann integrable on $[a, c]$ and $f$ is Riemann integrable on $[c, b],$ then there exist partitions $P_1$ and $P_2$ of $[a, c]$ and $[c, b]$ respectively such that

$$\begin{align}
U(f, P_1, [a, c]) - L(f, P_1, [a, c]) &< \epsilon, \\
U(f, P_2, [c, b]) - L(f, P_2, [c, b]) &< \epsilon.
\end{align}$$

Letting $P$ be the partition of $[a, b]$ containing all points of $P_1$ and $P_2,$ we have

$$\begin{align}
U(f, P, [a, b]) = U(f, P_1, [a, c]) + U(f, P_2, [c, b]) \\
L(f, P, [a, b]) = L(f, P_1, [a, c]) + L(f, P_2, [c, b])
\end{align}$$

and combining these with the inequalities above, we obtain

$$U(f, P, [a, b]) - L(f, P, [a, b]) < 2\epsilon.$$

Since $\epsilon$ can be made arbitrarily small, it follows that $f$ is Riemann integrable on $[a, b].$

:::
::::



::::{admonition} Exercise 1.A.11
:class: tip

Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Define $F: [a, b] \to \mathbb{R}$ by

$$F(t) = \begin{cases}
0 & \text{ if } t = a \\
\int_a^t & \text{ if } t \in (a, b].
\end{cases}$$

Prove that $F$ is continuous on $[a, b].$

:::{dropdown} Solution
Let $t_0 \in [a, b]$ and $\epsilon > 0.$
Since $f$ is Riemann integrable, it {prf:ref}`is boundedd<mira-bounds-on-riemann-integral>` by some $C \in \mathbb{R}.$
For any $\delta > 0$ and $x \in [a, b],$ if $|t - t_0| < \delta,$ then

$$|F(t) - F(t_0)| = \left|\int^t_{t_0} f\right| < \delta C.$$

Therefore, by picking $\delta < \epsilon / C$ we have $|F(t) - F(t_0)| < \epsilon,$ showing that $F$ is continuous.
:::
::::


::::{admonition} Exercise 1.A.12
:class: tip
Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Prove taht $|f|$ is Riemann integrable and that

$$\left|\int_a^b f\right| \leq \int_a^b |f|.$$

:::{dropdown} Solution
Let $\epsilon > 0.$
Since $f$ is Riemann integrable, there exists a partition $P_\epsilon = (x_0, x_1, \dots, x_n)$ of $[a, b]$ such that

$$U(f, P_\epsilon, [a, b]) - L(f, P_\epsilon, [a, b]) < \epsilon.$$

Now since

$$\begin{align}
\sup_{y \in [x_{k-1}, x_k]} |f(y)| - \inf_{z \in [x_{k-1}, x_k]} |f(z)| &\leq \sup_{y \in [x_{k-1}, x_k]} f(y) - \inf_{z \in [x_{k-1}, x_k]} f(z)
\end{align}$$

we have that

$$U(|f|, P_\epsilon, [a, b]) - L(|f|, P_\epsilon, [a, b]) \leq U(f, P_\epsilon, [a, b]) - L(f, P_\epsilon, [a, b]) < \epsilon$$

so $|f|$ is Riemann integrable.
Since $U(|f|, P_\epsilon, [a, b]) \geq U(f, P_\epsilon, [a, b]),$ we have that

$$\left|\int_a^b f\right| \leq \int_a^b |f|.$$
:::
::::



::::{admonition} Exercise 1.A.13
:class: tip
Suppose $f: [a, b] \to \mathbb{R}$ is an increasing function, meaning that $c, d \in [a, b]$ with $c < d$ implies $f(c) \leq f(d).$
Prove that $f$ is Riemann integrable on $[a, b].$

:::{dropdown} Solution
Let $P_n$ be the partition of $[a, b]$ into $2^n$ intervals of equal length.
Fix $n \in \mathbb{Z}^+$ and let $x_0, x_1, \dots, x_{2^n}$ be the points in $P_n$ and $y_0, y_1, \dots, y_{2^{n+1}}$ be the points in $P_{n+1}.$
Consider some fixed $0 \leq j \leq n.$
We have

$$\begin{align}
~&\left(\sup_{[x_j, x_{j+1}]}f - \inf_{[x_j, x_{j+1}]}f \right) (x_{j+1} - x_j) = \\
=~&\left(\sup_{[x_j, x_{j+1}]}f - \inf_{[x_j, x_{j+1}]}f \right) (y_{2j+1} - y_{2j}) + \left(\sup_{[x_j, x_{j+1}]}f - \inf_{[x_j, x_{j+1}]}f \right) (y_{2j+2} - y_{2j+1}) \\
\geq~&\left(\sup_{[y_{2j}, x_{2j+1}]}f - \inf_{[y_{2j}, y_{2j+1}]}f \right) (y_{2j+1} - y_{2j}) + \left(\sup_{[y_{2j + 1}, y_{2j+2}]}f - \inf_{[y_{2j+1}, y_{2j+2}]}f \right) (y_{2j+2} - y_{2j+1}) \\
=~&\left(\sup_{[y_{2j+1}, y_{2j+2}]}f - \inf_{[y_{2j}, y_{2j+1}]}f\right) \cdot 2^{-n-1} \\
=~&\left(\sup_{[x_j, x_{j+1}]}f - \inf_{[x_j, x_{j+1}]}f \right) \cdot 2^{-n-1}
\end{align}$$

In other words, each time we increment $n,$ the difference between the upper and lower Riemann sums decreases by a factor of $2.$
Therefore, by induction, we have

$$U(f, P_n, [a, b]) - L(f, P_n, [a, b]) = 2^{-(n-1)} \cdot \left(U(f, P_1, [a, b]) - L(f, P_1, [a, b]) \right).$$

so $f$ is Riemann integrable over $[a, b].$
:::
::::


::::{admonition} Exercise 1.A.14
:class: tip
Suppose $f_1, f_2, \dots$ is a sequence of Riemann integrable functions on $[a, b]$ such that $f_1, f_2, \dots$ converges uniformly to a function $f: [a, b] \to \mathbb{R}.$
Prove that $f$ is Riemann integrable and

$$\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.$$

:::{dropdown} Solution
Let $\epsilon > 0.$
Since $f_n \to f$ uniformly, there exists $N \in \mathbb{N}$ such that for all $n \geq N,$ we have

$$|f_n(x) - f(x)| < \epsilon.$$

Since $f_n$ is Riemann integrable for all $n \in \mathbb{Z}^+$ and $f_n \to f,$ it follows that $f$ is bounded.
Then, for all $n \geq N$ and any partition $P$ of $[a, b],$ we have

$$U(f, [a, b]) \leq U(f, P, [a, b]) \leq U(f_n, P, [a, b]) + \epsilon (b - a).$$

Taking the infimum over $P$ we obtain

$$U(f, [a, b]) \leq U(f_n, [a, b]) + \epsilon (b - a).$$

We can also form a similar inequality for the lower Riemann sum, that is

$$L(f, [a, b]) \geq L(f_n, [a, b]) - \epsilon (b - a).$$

Putting these together we obtain

$$L(f_n, [a, b]) - \epsilon (b - a) \leq L(f, [a, b]) \leq U(f, [a, b]) \leq U(f_n, [a, b]) + \epsilon (b - a),$$

for all $n \geq N.$
Since $\epsilon > 0$ can be chosen to be arbitrarily small, we conclude that $f$ is Riemann integrable and that

$$\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.$$
:::
::::


## Chapter 1.B

::::{admonition} Exercise 1.B.1
:class: tip
Define $f: [0, 1] \to \mathbb{R}$ as follows

$$f(a) = \begin{cases}
0 & \text{ if } a \not \in \mathbb{Q} \\
\frac{1}{n} & \text{ if } a \in \mathbb{Q} \text{ and } n \in \mathbb{Z}^+ \text{ smallest } n \text{ s.t. } a = \frac{m}{n} \text{ for some } m \in \mathbb{Z}^+. \\
\end{cases}$$

Show that $f$ is Riemann integrable and compute $\int_0^1 f.$

:::{dropdown} Solution
Let $A_n$ be the set of all rationals $a$ in $[0, 1]$ such that $n$ is the smallest positive integer such that $a = m/n$ for some integer $m.$
Then $A_n$ is finite for all $n.$
Let

$$f_n(a) = \begin{cases}
0 & \text{ if } a \not \in \mathbb{Q} \text{ or } a \not \in \bigcup^n_{k = 1} A_k \\
\frac{1}{k} & \text{ if } a \in \bigcup^n_{k = 1} A_k \text{ and } k \in \mathbb{Z}^+ \text{ is the smallest } k \text{ s.t. } a = \frac{m}{k} \text{ for some } m \in \mathbb{Z}^+. \\
\end{cases}$$

Then, $\int_a^b f_n = 0.$
Also $f_n \to f$ uniformly and $\int_a^b f_n = 0,$ so

$$\int_a^b f = \lim_{n \to \infty} \int_a^b f_n = 0.$$
:::
::::


::::{admonition} Exercise 1.B.2
:class: tip
Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
Prove that $f$ is Riemann integrable if and only if

$$L(-f, [a, b]) = - L(f, [a, b])$$

:::{dropdown} Solution
Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
If $f$ is Riemann integrable, then

$$\begin{align}
L(-f, [a, b]) &= \sup_P L(-f, P, [a, b]) \\
&= \sup_P -U(f, P, [a, b]) \\
&= - \inf_P U(f, P, [a, b]) \\
&= - U(f, [a, b]) \\
&= - L(f, [a, b]).
\end{align}$$

Conversely, if 

$$L(-f, [a, b]) = - L(f, [a, b]),$$

then we have

$$\begin{align}
L(-f, [a, b]) &= - L(f, [a, b]) \\
&= - \sup_P L(f, P, [a, b]) \\
&= \inf_P -L(f, P, [a, b]) \\
&= \inf_P U(-f, P, [a, b]) \\
&= U(-f, P, [a, b]),
\end{align}$$

so $-f$ is Riemann integrable, which means $f$ must also be Riemann integrable.
:::
::::


::::{admonition} Excercise 1.B.3
:class: tip
Suppose $f, g: [a, b] \to \mathbb{R}$ are bounded functions.
Prove that

$$L(f, [a, b]) + L(g, [a, b]) \leq L(f + g, [a, b]),$$

and

$$U(f + g, [a, b]) \leq U(f, [a, b]) + U(g, [a, b]).$$

:::{dropdown} Solution
Let $P_1$ and $P_2$ be partitions of $[a, b].$
Then, letting $P$ be a partition of $[a, b]$ which includes all points included in $P_1$ and $P_2,$ we have

$$L(f, P_1, [a, b]) + L(g, P_2, [a, b]) \leq L(f + g, P, [a, b]).$$

Taking the supremum of both sides with respect to $P_1$ and $P_2,$ we obtain

$$L(f, [a, b]) + L(g, [a, b]) \leq L(f + g, [a, b]).$$

Repeating the same argument for the upper Riemann sum completes the proof.
:::
::::


::::{admonition} Exercise 1.B.4
:class: tip
Given en example of bounded functions $f, g: [0, 1] \to \mathbb{R}$ such that

$$L(f, [a, b]) + L(g, [a, b]) < L(f + g, [a, b]),$$

and

$$U(f + g, [a, b]) < U(f, [a, b]) + U(g, [a, b]).$$

:::{dropdown} Solution
Consider the functions $f(x) = \mathbb{1}_{x \in \mathbb{Q}}$ and $g(x) = \mathbb{1}_{x \not \in \mathbb{Q}}.$
First, we have that $f + g = 1$ so $U(f, [0, 1]) = L(f, [0, 1]) = 1.$
On the other hand, any subinterval of $[0, 1]$ of nonzero length contains at least one rational and at least one irrational number.
Therefore for any partition $P$ of $[0, 1],$ we have

$$L(f, P, [0, 1]) = L(g, P, [0, 1]) = 0 ~~\text{ and }~~ U(f, P, [0, 1]) = U(g, P, [0, 1]) = 1.$$

Therefore, these functions satisfy the requirements of the problem statement.
:::
::::



::::{admonition} Exercise 1.B.5
:class: tip
Give an example of a sequence of continuous real-valued functions $f_1, f_2, \dots$ on $[0, 1]$ and a continuous real-valued function $f$ on $[0, 1]$ such that

$$f(x) = \lim_{k \to \infty} f_k(x)$$

for each $x \in [0, 1]$ but

$$\int_0^1 f \neq \lim_{k \to \infty} \int_0^1 f_k.$$

:::{dropdown} Solution
Consider the functions $f_1, f_2, \dots$ defined as

$$f_k(x) = \begin{cases}
k - k^2 x & \text{ if } 0 < x \leq k \\ 
0 & \text{ otherwise.}
\end{cases}$$

Note that $\lim_{k \to \infty} f_k = 0,$ and also for all $k \in \mathbb{Z}^+,$ we have $\int_0^1 f_k = 1.$
Thus

$$\int_0^1 f \neq \lim_{k \to \infty} \int_0^1 f_k.$$
:::
::::


## Chapter 2.A

::::{admonition} Exercise 2.A.1
:class: tip
Prove that if $A$ and $B$ are subsets of $\mathbb{R}$ and $|B| = 0,$ then $|A \cup B| = |A|.$

:::{dropdown} Solution
Suppose that $|B| = 0.$
If $|A| = \infty,$ then $|A \cup B| = \infty = |A|.$
Instead, suppose that $|A| < \infty.$
Let $\epsilon > 0.$
Then, there exist sequences of open intervals $I_1, I_2, \dots$ and $J_1, J_2, \dots$ such that

$$A \subseteq \bigcup_{n = 1}^\infty I_n ~\text{ and }~ \sum_{n = 1}^\infty \ell(I_n) \leq |A| + \frac{\epsilon}{2}$$

and similarly

$$B \subseteq \bigcup_{n = 1}^\infty J_n ~\text{ and }~ \sum_{n = 1}^\infty \ell(J_n) \leq \frac{\epsilon}{2}.$$

Define the sequence $K_1, K_2, \dots$ to be the sequence of intervals $I_1, J_1, I_2, J_2, \dots.$
Then

$$A \cup B \subseteq \bigcup_{n = 1}^\infty K_n ~\text{ and }~ \sum_{n = 1}^\infty \ell(K_n) \leq |A| + \epsilon,$$

and since $\epsilon > 0$ was arbitrary, we have $|A \cup B| \leq |A|.$
By the {prf:ref}`order preserving property of the outer measure<mira:thm:outer-measure-preserves-order>` we have $|A \cup B| \geq |B|$ and thus $|A \cup B| = |A|.$
:::
::::


::::{admonition} Exercises 2.A.2
:class: tip
Suppose $A \subseteq \mathbb{R}$ and $t \in \mathbb{R}.$
Let $tA = \{ta: a \in A\}.$
Prove that $|tA| = |t||A|.$

\[Assume that $0 \cdot \infty$ is defined to be 0.\]

:::{dropdown} Solution
If $t = 0,$ then $tA = \{0\}$ so $|tA| = 0.$
Also, irrespective of the value of $|A|,$ we have $|t||A| = 0,$ so $|tA| = |t||A|.$
Instead suppose that $t \neq 0.$
Also, suppose that $|A|< \infty.$
Then, there exists a sequence of open intervals $I_1, I_2, \dots$ such that $\cup_{n=1}^\infty I_n \subseteq A$ and also $\sum_{n=1}^\infty |A| + \epsilon.$
Now, note that

$$\bigcup_{n=1}^\infty tI_n = t \bigcup^\infty_{n=1} I_n \subseteq tA,$$

and also 

$$\sum_{n=1}^\infty \ell(tI_n) = |t| \sum_{n=1}^\infty \ell(I_n) \leq |t| |A| + |t| \epsilon.$$

And since $\epsilon > 0$ was arbitrary, we have $|tA| \leq |t||A|.$
To get the unequality the other way, consider that

$$|A| = |t^{-1} (tA)| \leq |t^{-1}| |tA| \implies |t||A| \leq |tA|,$$

where we have used the assumption $t \neq 0.$
Therefore $|tA| = |t||A|$ whenever $|A| < \infty.$

Finally, consider the case $|A| = \infty$ and $t \neq 0.$
Then, we have that $|t||A| = \infty.$
Also, we must have $|tA| = \infty,$ because if we did not, then we could use the previous result with a factor of $t^{-1}$ to show that $|A| < \infty,$ which would lead to a contradiction.
This completes all parts of the proof.
:::
::::



::::{admonition} Exercise 2.A.3
:class: tip
Prove that if $A, B \subseteq{R}$ and $|A| < \infty,$ then $|B \setminus A| \geq |B| - |A|.$

:::{dropdown} Solution
Suppose that $A, B \subseteq{R}$ and $|A| < \infty.$
By the {prf:ref}`subadditivity of the outer measure<mira:thm:outer-measure-preserves-order>` and the {prf:ref}`order preserving property of the outer measure<mira:thm:outer-measure-preserves-order>`.

$$|B \setminus A| + |A| \geq |A \cup B| \geq |B| \implies |B \setminus A| \geq |B| - |A|.$$
:::
::::



::::{admonition} Exercise 2.A.4
:class: tip
Suppose that $F$ is a subset of $\mathbb{R}$ with the property that every open sucover of $F$ has a finite subcover.
Prove that $F$ is closed and bounded.

:::{dropdown} Solution
Suppose that $F$ is a subset of $\mathbb{R}$ with the property that every open sucover of $F$ has a finite subcover.
First, we show $F$ is bounded.
The collection of sets $(n-1, n+1)$ for $n \in \mathbb{Z}^+$ is an open cover of $\mathbb{R}$ and therefore it is an open cover of $F.$
By assumption, this set has a finite subcover on $F,$ say $I_{n_1}, \dots, I_{n_k},$ whose union has a finite infimum and a finite supremum.
Therefore $F$ is a bounded set.
Let $a = \inf F$ and $b = \sup F.$

We will show that $F$ is a closed set by showing that it contains all its limit points, by way of contradiction.
Suppose $x_n \in F$ is a sequence of points in $F$ which converges to a limit $x.$
Suppose $x \not \in F.$
Then, define the following two base-case open intervals

$$\begin{align}
I_1 = \left(a - 1, \frac{a + x}{2}\right) = (c_1, d_1) \\
I_2 = \left(\frac{b + x}{2}, b + 1\right) = (c_2, d_2) \\
\end{align}$$

as well as the intervals

$$\begin{align}
I_{2n+1} = \left(\frac{c_{2n-1} + d_{2n-1}}{2}, \frac{d_{2n-1} + x}{2}\right) \\
I_{2n+2} = \left(\frac{c_{2n} + x}{2}, \frac{d_{2n} + d_{2n}}{2}\right).
\end{align}$$

This sequence is an open cover of $F,$ so it has a finite subcover.
But that means that there exists $k \in \mathbb{Z}^+$ such that

$$\inf\{|x - y| \in \mathbb{R}: y \in \cup^\infty_{n = 1} I_n\} \geq \delta.$$

But since $x_n \in x$ and $x_n \in F$ for all $n \in \mathbb{Z}^+,$ this leads to a contradiction.
:::
::::



::::{admonition} Exercise 2.A.5
:class: tip
Suppose $\mathcal{A}$ is a set of closed subsets of $\mathbb{R}$ such that $\cap_{F \in \mathcal{A}} F = \emptyset.$
Prove that if $\mathcal{A}$ contains at least one bounded set, then there exist $n \in \mathbb{Z}^+$ and $F_1, \dots, F_n \in \mathcal{A}$ such that $F_1 \cap \dots \cap F_n = \emptyset.$

:::{dropdown} Solution
Suppose $\mathcal{A}$ is a set of closed subsets of $\mathbb{R}$ such that $\cap_{F \in \mathcal{A}} F = \emptyset.$
Further, suppose that $\mathcal{A}$ contains at least one closed bounded set $F_0.$
Since $\cap_{F \in \mathcal{A}} F = \emptyset,$ we have

$$\left(\bigcap_{F \in \mathcal{A}} F\right)' = \bigcup_{F \in \mathcal{A}} F' = \mathbb{R},$$

so we have

$$F_0 \subseteq \bigcup_{F \in \mathcal{A}: F \neq F_0} F'.$$

The union above is an open cover of $F_0,$ so it has a finite subcover on $F_0,$ say $F_1', \dots, F_n'.$
Since $F_0 \subseteq F_1' \cup \dots \cup F_n'$ we have

$$F_0 \cap (F_1' \cup \dots \cup F_n')' = F_0 \cap F_1 \cap \dots \cap F_n = \emptyset.$$
:::
::::


::::{admonition} Exercise 2.A.6
:class: tip
Prove that if $a, b \in \mathbb{R}$ and $a < b,$ then

$$|(a, b)| = |[a, b)| = |(a, b]| = b - a.$$

:::{dropdown} Solution
Using the fact that $|[a, b]| = b - a,$ together with the {prf:ref}`order preserving property of the outer measure<mira:thm:outer-measure-preserves-order>` we have that

$$b - a = |[a, b]| \geq |[a, b)| \geq |(a, b)| = b - a$$

so $|[a, b)| = b - a.$
Similarly, $|(a, b]| = b - a,$ concluding the proof.
:::
::::


::::{admonition} Exercise 2.A.7
:class: tip
Suppose $a, b, c, d$ are real numbers with $a < b$ and $c < d.$
Prove that

$$|(a, b) \cup (c, d)| = (b - a) + (d - c)$$

if and only if $(a, b) \cap (c, d) = \emptyset.$

:::{dropdown} Solution
Suppose $a, b, c, d$ are real numbers with $a < b$ and $c < d.$
By the {prf:ref}`countable subadditivity of the outer measure<mira:thm:countable-subadditivity-of-outer-measure>`

$$|(a, b) \cup (c, d)| \leq (b - a) + (d - c)$$

always holds.
It remains to show that the opposite inequality holds if and only if $(a, b) \cap (c, d) = \emptyset.$
First, suppose $(a, b) \cap (c, d) \neq \emptyset,$ and assume without loss of generality that $d > b.$
Then, we have that $c < b,$ so

$$|(a, b) \cup (c, d)| = d - \min(a, c) = d - (c + \min(a - c, 0)) = (d - c) - \min(a - c, 0) < (d - c) + (b - a).$$

Therefore $|(a, b) \cup (c, d)| \geq (b - a) + (d - c)$ holds only if the two intervals are disjoint.
Going the other way, suppose that the two intervals are disjoint, again assuming that $d > b$ without loss of generality.
Let $I_1, I_2, \dots$ be a sequence of open intervals whose union contains $(a, b) \cup (c, d).$
Then, the union of the open intervals $I_1 \cap (a, b), I_2 \cap (a, b), \dots$ contains $(a, b)$ and similarly, the union of the open intervals $I_1 \cap (c, d), I_2 \cap (c, d), \dots$ contains $(c, d).$
Finally, using the fact that $(a, b)$ and $(c, d)$ are disjoint, we have

$$\sum_{n = 1}^\infty \ell(I_n) \geq \sum_{n = 1}^\infty \ell(I_n \cap (a, b)) + \ell(I_n \cap (c, d))$$

which implies that

$$|(a, b) \cup (c, d)| \geq |(a, b)| + |(c, d)|.$$

Putting these results together arrive at the required conclusion.

:::
::::


::::{admonition} Excercise 2.A.8
:class: tip
Prove that if $A \subseteq \mathbb{R}$ and $t > 0,$ then $|A| = |A \cap (-t, t)| + |A \cap (\mathbb{R} \setminus (-t, t))|.$

:::{dropdown} Solution
First, by the {prf:ref}`countable subadditivity of the outer measure<mira:thm:countable-subadditivity-of-outer-measure>` we have

$$|A| \leq |A \cap (-t, t)| + |A \cap (\mathbb{R} \setminus (-t, t))|$$

for all $t > 0.$
To prove the inequality the other way, suppose $I_1, I_2, \dots$ is a sequence of open intervals whose union contains $A.$
Then, we have

$$\begin{align}
\sum_{n = 1}^\infty \ell(I_n) &= \sum_{n = 1}^\infty \ell(I_n \cap (-t, t)) + \ell(I_n \cap (-\infty, t)) + \ell(I_n \cap (\mathbb{R} \setminus (t, \infty))) \\
&\geq |A \cap (-t, t)| + |A \cap (\mathbb{R} \setminus (-t, t))|
\end{align}$$

where we have used the fact that the sequence of sets

$$I_1 \cap (-\infty, t], I_1 \cap [t, \infty), I_2 \cap (-\infty, t], \dots$$

has a union that contains $A \cap (\mathbb{R} \setminus (-t, t)),$ and the outer measures of these sets are equal to

$$\ell(I_1 \cap (-\infty, t)), \ell(I_1 \cap (t, \infty)), \ell(I_2 \cap (-\infty, t)), \dots,$$

completing the proof.
:::
::::


::::{admonition} Exercise 2.A.9
:class: tip
Prove that $|A| = \lim_{t \to \infty} |A \cap (-t, t)|$ for all $A \subseteq \mathbb{R}.$

:::{dropdown} Solution
First, by the {prf:ref}`countable subadditivity of the outer measure<mira:thm:countable-subadditivity-of-outer-measure>` we have

$$\begin{align}
|A| &= \left|\bigcup_{n = 1}^\infty (A \cap (n-1, n)) \cup (A \cap (-n, -n + 1)) \cup \{-n-1, n-1\} \right| \\
&\leq \sum_{n = 1}^\infty \left|(A \cap (n-1, n)) \cup (A \cap (-n, -n+1)) \cup \{-n-1, n-1\} \right| \\
&= \lim_{N \to \infty} \sum_{n = 1}^N \left|(A \cap (n-1, n)) \cup (A \cap (-n, -n+1)) \cup \{-n-1, n-1\} \right| \\
&= \lim_{N \to \infty} \left|A \cap (-N, N)\right|.
\end{align}$$

Note that since $\left|A \cap (-t, t)\right|$ is non-decreasing in $t \in \mathbb{Z}^+,$ the limit above is unchanged even if $N \not \in \mathbb{Z}^+.$
In addition, we have $|A| \geq |A \cap (-t, t)|$ for all $t \in \mathbb{R},$ and putting these two inequalities together, we conclude that

$$|A| = \lim_{t \to \infty} |A \cap (-t, t)|.$$
:::
::::


::::{admonition} Exercise 2.A.10
:class: tip
Prove that $|[0, 1] \setminus \mathbb{Q}| = 1.$

:::{dropdown} Solution
First, by the {prf:ref}`countable subadditivity of the outer measure<mira:thm:countable-subadditivity-of-outer-measure>` we have

$$\begin{equation}
|[0, 1] \setminus \mathbb{Q}| \geq |[0, 1]| - |\mathbb{Q}| = |[0, 1]| = 1,
\end{equation}$$

where we have used the fact that {prf:ref}`countable sets have measure zero<mira:thm:countable-sets-have-measure-zero>`.
Using the fact that the {prf:ref}`outer measure preserves order<mira:thm:outer-measure-preserves-order>` we have $|[0, 1] \setminus \mathbb{Q}| \leq |[0, 1]| = 1,$ concluding the proof.
:::
::::


## Chapter 2.C

::::{admonition} Exercise 2.C.1
:class: tip

Explain why there does not exist a measure space $(X, S, \mu)$ with the property that 

$$\{\mu(E) : E \in S\} = [0, 1).$$

:::{dropdown} Solution

Let $(X, S, \mu)$ be a measure space.
If $\mu(X) \geq 1,$ then $\{\mu(E) : E \in S\} \neq [0, 1),$ because $X \in S.$
Instead, suppose $\mu(X) < 1.$
Then, there exists $\epsilon > 0$ such that $\mu(X) < 1 - \epsilon,$ and since $\mu(E) \leq \mu(X)$ for any $E \in S,$ we have $\mu(E) < 1 - \epsilon$ for any $E \in S.$
Therefore, $\{\mu(E) : E \in S\} \subseteq [0, 1 - \epsilon) \neq [0, 1).$

:::
::::



::::{admonition} Exercise 2.C.2
:class: tip

Suppose $\mu$ is a measure on $(\mathbb{Z}^+, 2^{\mathbb{Z}^+}).$
Prove that there is a sequence $w_1, w_2, \ldots$ in $[0, \infty]$ such that

$$\mu(E) = \sum_{n \in E} w_n$$

for every $E \subseteq \mathbb{Z}^+.$

:::{dropdown} Solution

Let $\mu$ be a measure on $(\mathbb{Z}^+, 2^{\mathbb{Z}^+}).$
Define $w_n = \mu(\{n\})$ for each $n \in \mathbb{Z}^+.$
For any $E \subseteq \mathbb{Z}^+,$ we have

$$\mu(E) = \mu\left(\bigcup_{n \in E} \{n\} \right) = \sum_{n \in E} \mu(\{n\}) = \sum_{n \in E} w_n.$$

Therefore, the sequence $w_1, w_2, \ldots$ satisfies the required property.

:::
::::



::::{admonition} Exercise 2.C.3
:class: tip

Give an example of a meeasure $\mu$ on $(\mathbb{Z}^+, 2^{\mathbb{Z}^+})$ such that

$$\{\mu(E): E \subseteq \mathbb{Z}^+\} = [0, 1].$$

:::{dropdown} Solution

Let $\mu$ be the measure on $(\mathbb{Z}^+, 2^{\mathbb{Z}^+})$ defined via $\mu(\{n\}) = 2^{-n}$ for each $n \in \mathbb{Z}^+.$
This definition determines the measure on all subsets of $\mathbb{Z}^+$ because

$$\mu(E) = \mu\left(\bigcup_{n \in E} \{n\} \right) = \sum_{n \in E} \mu(\{n\}) = \sum_{n \in E} 2^{-n}.$$

Then, for any $E \subseteq \mathbb{Z}^+,$ we have $\mu(E) \in [0, 1].$
Conversely, if $x \in [0, 1],$ then writing the binary expansion of $x$ as $x = 0.x_1x_2\ldots$, we see that

$$x = \sum_{n=1}^\infty 2^{-n} \mathbf{1}(x_n = 1) = \sum_{n \in E} 2^{-n},$$

where $E = \{n \in \mathbb{Z}^+: x_n = 1\}.$
Therefore, $x \in \{\mu(E): E \subseteq \mathbb{Z}^+\}.$
We therefore conclude that $\{\mu(E): E \subseteq \mathbb{Z}^+\} = [0, 1].$

:::
::::




::::{admonition} Exercise 2.C.4
:class: tip

Give an example of a measure space $(X, S, \mu)$ such that

$$\{\mu(E): E \in S\} = \{\infty\} \cup \bigcup_{k = 0}^\infty [3k, 3k + 1].$$

:::{dropdown} Solution

Let $X = \mathbb{Z}$ and $S = 2^{\mathbb{Z}}.$
Let $\mu$ be the measure on $(X, S)$ defined via

$$\mu(\{n\}) = \begin{cases}
2^{n} & \text{if } n < 0, \\
3& \text{if } n \geq 0. \\
\end{cases}$$

Then, for any $E \in S,$ we have

$$\mu(E) \in \{\infty\} \cup \bigcup_{k = 0}^\infty [3k, 3k + 1].$$

:::
::::



::::{admonition} Exercise 2.C.5
:class: tip

Suppose $(X, S, \mu)$ is a measure space such that $\mu(X) < \infty.$
Prove that if $\mathcal{A}$ is a set of disjoint sets in $S$ such that $\mu(A) > 0$ for every $A \in \mathcal{A},$ then $\mathcal{A}$ is countable.

:::{dropdown} Solution

Let $(X, S, \mu)$ be a measure space such that $\mu(X) < \infty.$
Suppose $\mathcal{A}$ is a set of disjoint sets in $S$ such that $\mu(A) > 0$ for every $A \in \mathcal{A}.$
For each $k \in \mathbb{Z},$ let 

$$\mathcal{A}_k = \{A \in \mathcal{A}: 2^k \leq \mu(A) < 2^{k+1}\}.$$

Suppose $\mathcal{A}$ is not countable.
Then at least one of the sets $\mathcal{A}_k$ must have an infinite number of elements, which are all disjoint subsets of $X.$
Let $A_1, A_2, \ldots$ be a sequence of elements in $\mathcal{A}_k.$
By countable additivity, we have

$$\mu(X) \geq \mu\left(\bigcup_{A \in \mathcal{A}} A\right) \geq \mu\left(\bigcup_{A \in \mathcal{A}_k} A\right) \geq \mu\left(\bigcup_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty \mu(A_n) \geq \sum_{n=1}^\infty 2^k = \infty,$$

which is a contradiction.
Therefore, $\mathcal{A}$ must be countable.

:::
::::



::::{admonition} Exercise 2.C.6
:class: tip

Find all $c \in [3, \infty)$ such that there exists a measure space $(X, S, \mu)$ with

$$\{\mu(E): E \in S\} = [0, 1] \cup [3, c].$$

:::{dropdown} Solution

Suppose $(X, S, \mu)$ is a measure space such that $\text{im}(\mu) = \{\mu(E): E \in S\} = [0, 1] \cup [3, c].$
Then, it must be the case that $\mu(X) = c.$
Now, since $A$ is the range of $\mu,$ it holds that for each $x \in \text{im}(\mu),$ there exists $E \in S$ such that $\mu(E) = x.$
Now, using the fact that

$$\mu(X \setminus E) = \mu(X) - \mu(E) = c - x,$$

we see that $c - x \in \text{im}(\mu).$
Therefore, for any $x \in A,$ we have $c - x \in A,$ and the only $c \in [3, \infty)$ that satisfies this property is $c = 3.$

:::
::::




::::{admonition} Exercise 2.C.7
:class: tip

Given an example of a measure space $(X, S, \mu)$ such that

$$\{\mu(E): E \in S\} = \{\infty\} \cup [3, \infty].$$

:::{dropdown} Solution

Let $X = \mathbb{Z}$ and $S = 2^{\mathbb{Z}}.$
Let $\mu$ be the measure on $(X, S)$ defined via

$$\mu(\{n\}) = \begin{cases}
2^{n} & \text{if } n < 0, \\
n& \text{if } n \geq 0. \\
\end{cases}$$

Then, we have that

$$\{\mu(E): E \in S\} = \{\infty\} \cup [3, \infty].$$

:::
::::



::::{admonition} Exercise 2.C.8
:class: tip

Give an example of a set $X,$ a $\sigma$-algebra $S$ on $X,$ a set $\mathcal{A}$ of subsets of $X,$ such that $S$ is the smallest $\sigma$-algebra on $X$ containing $\mathcal{A},$ and two measures $\mu$ and $\nu$ on $(X, S)$ such that $\mu(A) = \nu(A)$ for every $A \in \mathcal{A},$ and $\mu(X) = \nu(X),$ but $\mu \neq \nu.$

:::{dropdown} Solution

Let $X = \{1, 2, 3, 4\},$ and let

$$\mathcal{A} = \{\{1, 2\}, \{2, 3\}, \{3, 4\}, \{4, 1\}\}.$$

Note that $S$ must contain all singleton sets, namely $\{1\}, \{2\}, \{3\}, \{4\}.$
This is because, for example, $\{1\} = \{1, 2\} \cap \{4, 1\},$ and so on for the other singleton sets.
Therefore $S$ must contain all subsets of $X.$

Now, let $\mu$ be the measure on $(X, S)$ defined via

$$\mu(\{1\}) = \mu(\{2\}) = \mu(\{3\}) = \mu(\{4\}) = 1,$$

and let $\nu$ be the measure on $(X, S)$ defined via

$$\nu(\{1\}) = \nu(\{3\}) = \frac{1}{2} \text{ and } \nu(\{2\}) = \nu(\{4\}) = \frac{3}{2}.$$

Then, $\mu$ and $\nu$ agree on all elements of $\mathcal{A},$ and $\mu(X) = \nu(X) = 4,$ but $\mu \neq \nu.$

:::
::::




::::{admonition} Exercise 2.C.9
:class: tip

Suppose $\mu$ and $\nu$ are measures on a measurable space $(X, S).$
Prove that $\mu + \nu$ is a measure on $(X, S).$

:::{dropdown} Solution

Let $\mu$ and $\nu$ be measures on a measurable space $(X, S).$
We need to show that $\mu + \nu$ is a measure on $(X, S).$
First, note that $\mu + \nu$ is a function whose domain is $S$ and whose range is a subset of $[0, \infty].$
Second, note that $(\mu + \nu)(\emptyset) = \mu(\emptyset) + \nu(\emptyset) = 0.$
Third, suppose $A_1, A_2, \ldots$ is a sequence of disjoint sets in $S.$
Then, we have

$$\begin{align}
(\mu + \nu)\left(\bigcup_{n=1}^\infty A_n\right) &= \mu\left(\bigcup_{n=1}^\infty A_n\right) + \nu\left(\bigcup_{n=1}^\infty A_n\right) \\
&= \sum_{n=1}^\infty \mu(A_n) + \sum_{n=1}^\infty \nu(A_n) \\
&= \sum_{n=1}^\infty \left[\mu(A_n) + \nu(A_n)\right] \\
&= \sum_{n=1}^\infty (\mu + \nu)(A_n).
\end{align}$$

Therefore, $\mu + \nu$ is a measure on $(X, S).$

:::
::::




::::{admonition} Exercise 2.C.10
:class: tip

Give an example of a measure space $(X, S, \mu)$ and a decreasing sequence $E_1 \subseteq E_2 \subseteq \cdots$ of sets in $S$ such that

$$\mu\left(\bigcap_{n=1}^\infty E_n\right) \neq \lim_{n \to \infty} \mu(E_n).$$

:::{dropdown} Solution

Let $X = \mathbb{N}$ and $S = 2^{\mathbb{N}}.$
Let $\mu$ be the measure on $(X, S)$ defined via $\mu(\{n\}) = \frac{1}{n},$ and let $E_n = \{n, n+1, \ldots\}.$
Then, we have

$$\mu\left(\bigcap_{n=1}^\infty E_n\right) = \mu(\emptyset) = 0,$$

but also

$$\lim_{n \to \infty} \mu(E_n) = \lim_{n \to \infty} \sum_{k = n}^{\infty} \frac{1}{k} = \infty.$$

:::
::::



::::{admonition} Exercise 2.C.11
:class: tip
Suppose $(X, S, \mu)$ is a measure space and $C, D, E \in S$ are such that

$$\mu(C \cap D) < \infty, \mu(C \cap E) < \infty, \mu(D \cap E) < \infty.$$

Find and prove a formula for $\mu(C \cup D \cup E)$ in terms of $\mu(C),$ $\mu(D),$ $\mu(E),$ $\mu(C \cap D),$ $\mu(C \cap E),$ $\mu(D \cap E),$ and $\mu(C \cap D \cap E).$

:::{dropdown} Solution
Suppose $(X, S, \mu)$ is a measure space and $C, D, E \in S$ are such that

$$\mu(C \cap D) < \infty, \mu(C \cap E) < \infty, \mu(D \cap E) < \infty.$$

Then, we have

$$\begin{align}
\mu(C \cup D \cup E) &= \mu((C \cup D) \cup E) \\
&= \mu(C \cup D) + \mu(E) - \mu((C \cup D) \cap E) \\
&= \mu(C) + \mu(D) - \mu(C \cap D) + \mu(E) - \mu((C \cap E) \cup (D \cap E)) \\
&= \mu(C) + \mu(D) + \mu(E) - \mu(C \cap D) - \mu(C \cap E) - \mu(D \cap E) + \\
&~~~~+ \mu(C \cap D \cap E).
\end{align}$$
:::
::::



::::{admonition} Exercise 2.C.12
:class: tip
Suppose $X$ is a set and $S$ is the $\sigma$-algebra of all subsets $E$ of $X$ such that $E$ is countable or $X \setminus E$ is countable.
Give a complete description of the set of all measures $\mu$ on $(X, S).$

:::{dropdown} Solution
Suppose $X$ is a set and $S$ is the $\sigma$-algebra of all subsets $E$ of $X$ such that $E$ is countable or $X \setminus E$ is countable.
Then, a measure $\mu$ on $(X, S)$ is completely determined by the value of $\mu(\{x\})$ for each $x \in X,$ along with $\mu(X).$
:::
::::



## Chapter 2.D

::::{admonition} Exercise 2.D.1
:class: tip

Show that the set consisting of those numbers in $(0, 1)$ that have a decimal expansion containing one hundred consecutive 4s is a Borel subset of $\mathbb{R}.$
What is the Lebesgue measure of this set?

:::{dropdown} Solution

__Showing the set is Borel:__
Let $A$ be the set consisting of those numbers in $(0, 1)$ that have a decimal expansion containing one hundred consecutive 4s.
We can write $A$ as the union

$$\begin{align}
A = \bigcup_{n=1}^\infty \bigcup_{x_1 \ldots x_n \in D} \left(\sum_{k=1}^n x_k \cdot 10^{-k}\right) + 10^{-n} \cdot \left[\sum_{m=1}^{100} 4 \cdot 10^{-m}, 10^{-100} + \sum_{m=1}^{100} 4 \cdot 10^{-m} \right)
\end{align}$$

where $D$ is the set of integers from 0 to 9, together with the set

$$\begin{align}
\left[\sum_{m=1}^{100} 4 \cdot 10^{-m}, 10^{-100} + \sum_{m=1}^{100} 4 \cdot 10^{-m} \right).
\end{align}$$

This is a countable union of closed-open intervals and is therefore a Borel set.


__Computing the measure:__
Let $C(n, k)$ the number of rational numbers in $(0, 1)$ whose decimal expansion has $n$ digits, such that these $n$ digits do not contain one hundred consecutive 4s and also such that the $k$ last digits in the expansion are all 4s.
Then, $C(1, 0) = 9$ and $C(1, 1) = 1.$
By its definition, we can set up a recursive relation for $C(n, k)$ as follows.

For each rational number whose expansion has $n-1$ digits, such that these $n-1$ digits do not contain one hundred consecutive 4s, there are ten possible digits we can append to the end of the expansion to obtain a rational number whose expansion has $n$ digits.
If we append a digit that is not 4, then the resulting rational number with $n$ digits will not contain one hundred consecutive 4s and also, the last digit will not be 4.
Therefore, $C(n, 0) = 9 \sum_{k' = 0}^{99} C(n-1, k').$
If we append a digit that is 4, then the resulting rational number with $n$ digits will contain fewer than one hundred consecutive 4s if and only if there are fewer than $99$ consecutive 4s in the last digits of the expansion.
Also, we would be increasing the number of consecutive 4s in the last digits of the expansion by 1.
Therefore, $C(n, k) = C(n-1, k-1)$ if and only if $1 \leq k < 99.$
We can collect this information into the following recursion

$$\begin{align}
C(n, k) = \begin{cases}
9 \sum_{k' = 0}^{99} C(n-1, k') &\text{if } k = 0 \\
C(n-1, k-1) &\text{if } 1 \leq k < 99
\end{cases}
\end{align}$$

Letting $C_n = (C_{n, 0}, C_{n, 1}, \ldots, C_{n, 99})$ we can write this as

$$C_n = \begin{bmatrix}
9 & 9 & 9 & \dots & 9 & 9 \\
1 & 0 & 0 & \dots & 0 & 0 \\
0 & 1 & 0 & \dots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & 0 & 0 \\
0 & 0 & 0 & \dots & 1 & 0 \\
\end{bmatrix}C_{n-1}.$$

Let $A_n$ be the set of real numbers in $(0, 1)$ whose decimal expansion does not contain one hundred consecutive 4s up to and including the $n^{th}$ digit.
Then

$$|A_n| = \frac{1}{10^n} \sum_{k = 0}^{99} C(n, k),$$

because $A_n$ consists of $C(n, k)$ intervals of size $10^{-n},$ each corresponding to each of the $C(n, k)$ ways to choose the first $n$ digits of a rational number in $(0, 1)$ whose decimal expansion does not contain one hundred consecutive 4s and also such that the last $k$ digits are all 4s, followed by an arbitrary sequnce of digits.
Now, using the recursion derived earlier, the above equality can be expressed as

$$\begin{align}
|A_n| = \left|\begin{bmatrix}
0.9 & 0.9 & 0.9 & \dots & 0.9 & 0.9 \\
0.1 & 0 & 0 & \dots & 0 & 0 \\
0 & 0.1 & 0 & \dots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & 0 & 0 \\
0 & 0 & 0 & \dots & 0.1 & 0 \\
\end{bmatrix}^{n-1} \begin{bmatrix}
0.9 \\
0.1 \\
0 \\
\vdots \\
0 
\end{bmatrix}\right|
\end{align}$$

where $| \cdot |$ denotes the summation of the elements of a vector.
Noting that $A_n$ is a decreasing sequence of sets and that $\cap_{n = 1}^\infty = A,$ we have

$$|A| = \lim_{n \to \infty} |A_n| = \lim_{n \to \infty} \left|\begin{bmatrix}
0.9 & 0.9 & 0.9 & \dots & 0.9 & 0.9 \\
0.1 & 0 & 0 & \dots & 0 & 0 \\
0 & 0.1 & 0 & \dots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & 0 & 0 \\
0 & 0 & 0 & \dots & 0.1 & 0 \\
\end{bmatrix}^{n-1} \begin{bmatrix}
0.9 \\
0.1 \\
0 \\
\vdots \\
0 
\end{bmatrix}\right|$$

Finally, moving the limit inside the $| \cdot |,$ we have 

$$|A| = \left|\lim_{n \to \infty} \begin{bmatrix}
0.9 & 0.9 & 0.9 & \dots & 0.9 & 0.9 \\
0.1 & 0 & 0 & \dots & 0 & 0 \\
0 & 0.1 & 0 & \dots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & 0 & 0 \\
0 & 0 & 0 & \dots & 0.1 & 0 \\
\end{bmatrix}^{n-1} \begin{bmatrix}
0.9 \\
0.1 \\
0 \\
\vdots \\
0 
\end{bmatrix}\right|$$

Now, note that the limit of the matrix power above is the zero matrix, so $|A| = 0.$
Therefore, the set of numbers in $(0, 1)$ whose decimal expansion does not contain one hundred consecutive 4s has Lebesgue measure 0.
We conclude that the set of numbers in $(0, 1)$ whose decimal expansion contains one hundred consecutive 4s has Lebesgue measure 1.

:::
::::



::::{admonition} Exercise 2.D.2
:class: tip

Prove that there exists a bounded set $A \subseteq \mathbb{R}$ such that $|F| \leq |A| - 1$ for every closed set $F \subseteq A.$

:::{dropdown} Solution

Let $E \subseteq [0, 1]$ be a set that is not Borel.
Then, there exists $\epsilon > 0$ such that for any closed $F \subseteq E$ we have $|E \setminus F| \geq \epsilon.$
The set $E \cdot \lceil 1/\epsilon \rceil$ is not Borel, and also

$$|E \cdot \lceil 1/\epsilon \rceil \setminus F| \geq 1 \text{ for all closed } F \subseteq E \cdot \lceil 1/\epsilon \rceil.$$

Defining $A = E \cdot \lceil 1/\epsilon \rceil,$ and letting $F$ be any closed subset of $A,$ we have

$$|A \setminus F| = |A| - |F| \geq 1 \text{ for every closed set } F \subseteq A,$$

which shows the result.

:::
::::




::::{admonition} Exercise 2.D.3
:class: tip

Prove that there exists a set $A \subseteq \mathbb{R}$ such that $|G \setminus A| = \infty$ for every open set $G$ that contains $A.$

:::{dropdown} Solution


Let $\sim$ be the {prf:ref}`rational difference equivalence relation <mira:def:rational-difference-equivalence-relation>` on $\mathbb{R},$ and let $V$ be a set containing exactly one element from each equivalence class of $\sim$ on $[-1, 1].$
In the proof of the {prf:ref}`nonadditivity of the outer measure<mira:thm:non-additivity-of-outer-measure>` we showed that $|V| > 0,$ and that $V$ is not Borel.
Since $V \subseteq \mathbb{R}$ is not Borel, there must exist some $\epsilon > 0$ such that for any open set $G \subseteq \mathbb{R}$ we have $|G \setminus V| \geq \epsilon.$
Now, note that the set

$$A = \bigcup_{n \in \mathbb{Z}} 2n + V$$

is not Borel.
Then for any open set $G \subseteq \mathbb{R},$ we have

$$\begin{align}
|G \setminus A| &= \left|\bigcup_{n \in \mathbb{Z}} (G \cap [2n-1, 2n+1]) \setminus (2n + V)\right| \\
&= \sum_{n \in \mathbb{Z}} |(G \cap (2n-1, 2n+1)) \setminus (2n + V)| \\
&= \infty,
\end{align}$$

where in the last line we have used the preliminary result, and in the last line we have used the fact that the sets $(G \cap [2n-1, 2n+1]) \setminus (2n + V)$ are contained in disjoint open intervals $(2n-1, 2n+1),$ so {prf:ref}`the outer measure of their union is the sum of their outer measures <mira:thm:outer-measure-is-additive-if-sets-are-separable>`.

:::
::::




::::{admonition} Exercise 2.D.4
:class: tip

The phrase nontrivial interval is used to denote an interval of $\mathbb{R}$ that contains more than one element.
Recall that an interval might be open, closed, or neither.

(a) Prove that the union of each collection of nontrivial intervals of $\mathbb{R}$ is the union of a countable subset of that collection.

(b) Prove that the union of each collection of nontrivial intervals of $\mathbb{R}$ is a Borel set.

(c) Prove that there exists a collection of closed intervals of $\mathbb{R}$ whose union is not a Borel set.


:::{dropdown} Solution

__Part a:__
Given a nontrivial interval $I,$ let $I'$ denote the interval minus its supremum and infimum, that is

$$I' = I \setminus \{\inf I, \sup I\}.$$

Then, note that the set $\cup_{I \in C} I'$ is a union of open sets and is therefore open, so it can be written as the union of a countable collection of disjoint open intervals, say $U_1, U_2, \ldots.$
The sets $\cup_{I \in C} I$ and $\cup_{n=1}^\infty U_n$ differ by at most the infimum and supremum of each interval $U_n,$ of which there are countably many.
Each of the endpoints of each of the $U_n$ that is contained in $\cup_{I \in C} I$ must be contained in at least one $I \in C.$
Therefore, $\cup_{I \in C} I$ can be written as a countable union of the sets $U_n$ and the corresponding sets $I \in C$ containing their endpoints.
Now, we will show that each $U_n$ can be written as a countable union of nontrivial intervals in $C.$

Consider the case where $U_n$ is bounded, and let $\inf U_n = a$ and $\sup U_n = b.$
Then, for each $k \in \mathbb{Z},$ we have $[a + 1/k, b - 1/k] \subseteq U_n.$
Note that $\{I' : I \in C\}$ is an open cover of $U_n,$ so it is also an open cover of $[a + 1/k, b - 1/k].$
By the {prf:ref}`Heine-Borel theorem <mira:thm:heine-borel>`, there exists a finite open subcover of $[a + 1/k, b - 1/k]$ from $\{I' : I \in C\},$ so there exists a finite set of nontrivial intervals in $C$ whose union contains $[a + 1/k, b - 1/k].$
The union of all such sets over $k = 1, 2, \ldots$ is a countable union of nontrivial intervals in $C$ whose union contains $U_n.$

Consider the case where $U_n$ is bounded below but not above, and let $\inf U_n = a.$
Then, for each $k \in \mathbb{Z},$ we have $[a + 1/k, a + k] \subseteq U_n.$
Similarly to the reasoning above, $[a + 1/k, a + k]$ can be covered by a finite number of nontrivial intervals in $C,$ and the union of all such sets over $k = 1, 2, \ldots$ is a countable union of nontrivial intervals in $C$ whose union contains $U_n.$
The same reasoning applies to the case where $U_n$ is bounded above but not below, using instead the intervals $[b - k, b - 1/k]$ for $k = 1, 2, \ldots,$ where $b = \sup U_n.$
Lastly, to deal with the case where $U_n$ is unbounded, we apply the same argument considering instead intervals of the form $[-k, k]$ for $k = 1, 2, \ldots.$

We therefore conclude that $\cup_{I \in C} I$ can be written as a countable union of open intervals $U_n$ and a countable union of nontrivial intervals in $C$ containing any endpoints of the $U_n$ that are missing from $\cup_{I \in C} I.$
In addition, each $U_n$ can be written as a countable union of nontrivial intervals in $C.$
Therefore the entire union consists of nontrivial intervals in $C,$ and is countable.


__Part b:__
Since all nontrivial intervals are intervals, they are Borel.
Since, as we showed in part (a), the union of a collection of nontrivial intervals is a countable union of subsets of that collection, which are themselves Borel, so the union is also Borel.

__Part c:__
Let $\sim$ be the {prf:ref}`rational difference equivalence relation <mira:def:rational-difference-equivalence-relation>` on $\mathbb{R},$ and let $V$ be a set containing exactly one element from each equivalence class of $\sim$ on $[-1, 1].$
This set is a union of closed intervals, specifically it is the union of singleton closed intervals.
As shown in the proof of the {prf:ref}`nonadditivity of the outer measure<mira:thm:non-additivity-of-outer-measure>`, $V$ is not a Borel set.

:::
::::




::::{admonition} Exercise 2.D.5
:class: tip

Prove that if $A \subseteq \mathbb{R}$ is a Lebesgue measurable, then there exists an increasing sequence $F_1 \subseteq F_2 \subseteq \cdots$ of closed sets contained in $A$ such that

$$\left| A \setminus \bigcup_{n=1}^\infty F_n \right| = 0.$$

:::{dropdown} Solution

Suppose $A \subseteq \mathbb{R}$ is Lebesgue measurable.
Then, for each $n\in \mathbb{N},$ there exists a closed set $C_n \subseteq A$ such that $|A \setminus C_n| < 1/n.$
Let $F_n = \bigcup_{k=1}^n C_k,$ and note that $F_1 \subseteq F_2 \subseteq \cdots$ is an increasing sequence of closed sets contained in $A,$ and also that

$$|A \setminus F_n| < |A \setminus C_n| < \frac{1}{n}.$$

Therefore, for each $n \in \mathbb{N},$ we have

$$\left|A \setminus \bigcup_{n=1}^\infty F_n\right| \leq \left|A \setminus F_n\right| < \frac{1}{n},$$

and taking $n \to \infty,$ we obtain

$$\left|A \setminus \bigcup_{n=1}^\infty F_n\right| = 0.$$

:::
::::



::::{admonition} Exercise 2.D.6
:class: tip

Suppose $A \subseteq \mathbb{R}$ and $|A| < \infty.$
Prove that $A$ is Lebesgue measurable if and only if for every $\epsilon > 0$ there exists a set $G$ that is the union of finitely many disjoint open intervals such that $|A \setminus G| + |G \setminus A| < \epsilon.$

:::{dropdown} Solution

Suppose $A \subseteq \mathbb{R}$ and $|A| < \infty.$
We prove the result in two parts.

__Part 1:__
Suppose $A$ is Lebesgue measurable.
Let $\epsilon > 0.$
Then, there exists an open set $B$ such that

$$A \subseteq B \text{ and } |B \setminus A| < \epsilon/2.$$ (mira:eq:2d6:1)

Since $B$ is an open set, it is equal to a countable union of disjoint open intervals, say $B = \cup_{n=1}^\infty I_n.$
Note that $|B| \leq |A| + |B \setminus A| < \infty,$ so 

$$|B| = \left|\bigcup_{n=1}^\infty I_n\right| = \sum_{n=1}^\infty |I_n| < \infty.$$ (mira:eq:2d6:2)

Therefore, the sequence $|I_1|, |I_2|, \ldots$ is bounded and attains its supremum.
By relabelling, we can order the $I_n$ in order of decreasing outer measure.
From {eq}`mira:eq:2d6:2`, we know that the series of $|I_n|$ converges, so there exists $N \in \mathbb{N}$ such that

$$\sum_{n=1}^\infty |I_n| - \sum_{n=1}^N |I_n| < \epsilon/2,$$

which, together with the fact that $\sum_{n=1}^N I_N \subseteq B,$ implies

$$\left| B \setminus \bigcup_{n=1}^N I_n \right| = \left| \bigcup_{n=N+1}^\infty I_n\right| = \sum_{n=N+1}^\infty |I_n| < \epsilon/2.$$

Therefore, letting $G = \sum_{n=1}^N I_n,$ we have

$$\begin{align}
\left|A \setminus G\right| &= \left|A \cap G'\right| \\
&= \left|(A \cap B \cap G') \cup (A \cap B' \cap G')\right| \\
&\leq \frac{\epsilon}{2} + \left|A \cap B'\right| \\
&= \frac{\epsilon}{2}
\end{align}$$

where in the last line we have used the fact that $|A \cap B'| = 0$ because $A \subseteq B.$
Therefore, putting the inequalities in {eq}`mira:eq:2d6:1` and {eq}`mira:eq:2d6:2` together, we have

$$|G \setminus A| + |A \setminus G| < \epsilon.$$


__Part 2:__
Conversely, suppose that for every $\epsilon > 0$ there exists a set $B$ that is the union of finitely many disjoint open intervals such that

$$|B \setminus A| + |A \setminus B| < \epsilon.$$

Fix $\epsilon > 0,$ and let $B$ be a set that satisfies the above conditions, and 

$$|B \setminus A| + |A \setminus B| < \epsilon / 2.$$ (mira:eq:2d6:3)

Then, by {eq}`mira:eq:2d6:3` and the definition of the outer measure, there exists a sequence of open intervals $I_1, I_2, \ldots,$ such that $\cup_{n=1}^\infty I_n \subseteq A \setminus B$ and

$$\sum_{n=1}^\infty |I_n| < \epsilon / 2.$$ (mira:eq:2d6:4)

Now, let $I = \cup_{n=1}^\infty I_n.$
Then, the set $B \cup I$ is open and

$$\begin{align}|(G \cup I) \setminus A| &= |(G \cap A') \cup (I \cap A')| \\
&\leq |G \cap A'| + |I \cap A'| \\
&\leq |G \setminus A| + |I| \\
&< \epsilon
\end{align}$$

where in the last line we have used {eq}`mira:eq:2d6:3` and {eq}`mira:eq:2d6:4`.
Therefore the set $G = B \cup I$ is an open set that contains $A$ and satisfies $|G \setminus A| < \epsilon.$
It follows that $A$ is Lebesgue measurable.

:::
::::




::::{admonition} Exercise 2.D.7
:class: tip

Prove that if $A \subseteq \mathbb{R}$ is a Lebesgue measurable set, then there exists a decreasing sequence $G_1 \supseteq G_2 \supseteq \cdots$ of open sets containing $A$ such that

$$\left| \bigcap_{n=1}^\infty G_n \setminus A \right| = 0.$$


:::{dropdown} Solution

Suppose $A \subseteq \mathbb{R}$ is a Lebesgue measurable set.
Then for each $n \in \mathbb{N},$ there exists an open set $U_n$ such that $|U_n \setminus A| < 1/n.$
Let $G_n = \cap_{k=1}^n U_k.$
Then, $G_1 \supseteq G_2 \supseteq \cdots$ is a decreasing sequence of open sets containing $A,$ and also

$$\left| \left( \bigcup_{k=1}^\infty U_k \right) \setminus A \right| \leq \left| G_n \setminus A \right| < \frac{1}{n}$$

for all $n \in \mathbb{N}.$

:::
::::




::::{admonition} Exercise 2.D.8
:class: tip

Prove that the collection of Lebesgue measurable subsets of $\mathbb{R}$ is translation invariant.
More precisely, prove that if $A \subseteq \mathbb{R}$ is Lebesgue measurable and $t \in \mathbb{R},$ then $t + A$ is Lebesgue measurable.

:::{dropdown} Solution

Suppose $A$ is Lebesgue measurable and $t \in \mathbb{R}.$
Since $A$ is Lebesgue measurable, there exists a Borel set $B$ such that $B \subseteq A$ and $|A \setminus B| = 0.$
Since addition is a continuous function, the pre-image of any Borel set under the function $f: \mathbb{R} \to \mathbb{R}$ defined as $f(x) = x - t$ is a Borel set.
Therefore $f^{-1}(B) = t + B$ is a Borel set.
Because addition leaves the outer measure invariant, we have

$$|(t + A) \setminus (t + B)| = |t + (A \setminus B)| = |A \setminus B| = 0,$$

so $t + A$ is Lebesgue measurable.

:::
::::




::::{admonition} Exercise 2.D.9
:class: tip

Prove that the collection of Lebesgue measurable subsets of $\mathbb{R}$ is dilation invariant.
More precisely, prove that if $A \subseteq \mathbb{R}$ is Lebesgue measurable and $t \in \mathbb{R},$ then $tA$ is Lebesgue measurable.

:::{dropdown} Solution

Suppose $A$ is Lebesgue measurable and $t \in \mathbb{R}.$
If $t = 0,$ then $tA = \{0\},$ which is Lebesgue measurable.
Suppose $t \neq 0.$
Since $A$ is Lebesgue measurable, there exists a Borel set $B$ such that $A \subseteq B$ and $|B \setminus A| = 0.$
Since multiplication by a constant is a continuous function, the pre-image of any Borel set under the function $f: \mathbb{R} \to \mathbb{R}$ defined as $f(x) = t^{-1}x$ is a Borel set.
Therefore $f^{-1}(B) = tB$ is a Borel set.
Since multiplication by a constant is equivalent to scaling the outer measure by the absolute value of the constant, we have

$$|tA \setminus tB| = |t(A \setminus B)| = |t| |A \setminus B| = 0,$$

so $tA$ is Lebesgue measurable.

:::
::::




::::{admonition} Exercise 2.D.10
:class: tip


Prove that if $A$ and $B$ are disjoint subsets of $\mathbb{R}$ and $B$ is Lebesgue measurable, then $|A \cup B| = |A| + |B|.$

:::{dropdown} Solution

Suppose $A$ and $B$ are disjoint subsets of $\mathbb{R}$ and $B$ is Lebesgue measurable.
Then, there exists a Borel set $C \subseteq B$ such that $|B \setminus C| = 0.$
Then

$$|A \cup B| = |A \cup C \cup (B \setminus C)| = |A \cup C| = |A| + |C| = |A| + |B|.$$

:::
::::




::::{admonition} Exercise 2.D.11
:class: tip

Prove that if $A \subseteq \mathbb{R}$ and $|A| > 0,$ then there exists a subset of $A$ that is not Lebesgue measurable.

:::{dropdown} Solution

If $A \subseteq \mathbb{R}$ is not Lebesgue measurable, then we are done.
Suppose $A$ is Lebesgue measurable.
Then, each of the sets $A \cap (n, n+1), n \in \mathcal{N}$ is Lebesgue measurable.
In addition

$$0 < |A| = |\bigcup_{n \in \mathbb{Z}} (n, n+1) \cap A| \leq \sum_{n \in \mathbb{Z}} |(n, n+1) \cap A|,$$

so $|(n, n+1) \cap A| > 0$ for some $n \in \mathbb{Z}.$
Now, let $\sim$ be the {prf:ref}`rational difference equivalence relation <mira:def:rational-difference-equivalence-relation>` on $\mathbb{R},$ and let $V$ be a set containing exactly one element from each equivalence class of $\sim$ on $(n, n+1) \cap A.$
If $V$ is not Lebesgue measurable then we are done, so suppose it is not Borel.
Let $r_1, r_2, \dots$ be a sequence that contains each rational in $[-1, 1]$ exactly once.
By the definition of $\sim,$ we have $(r_i + V) \cap (r_j + V) = \emptyset$ for $i \neq j.$
Then, note that

$$|A \cap (n, n+1)| \leq \left| \bigcup_{i=1}^\infty (r_i + V) \right| \leq \sum_{i=1}^\infty |(r_i + [n, n+1])| = 3.$$

Since $V$ is Lebesgue measurable, so is $r_i + V$ for each $i \in \mathbb{N}.$
Thus by the {prf:ref}`countable subadditivity of the outer measure <mira:thm:countable-subadditivity-of-outer-measure>`, we have

$$ 3 \geq \left| \bigcup_{i=1}^\infty (r_i + V) \right| = \sum_{i=1}^n |r_i + V| \geq \sum_{i=1}^n |V| = n |V|$$

for all $n \in \mathbb{N},$ which can only hold if $|V| = 0.$
But this implies $|\cup_{i=1}^\infty (r_i + V)| = 0,$ which in turn implies $|A \cap (n, n+1)| = 0,$ which is a contradiction.
Therefore, $V \subseteq A$ is not Lebesgue measurable.

:::
::::



## Chapter 4.A

::::{admonition} Exercise 4.A.1
:class: tip
:label: mira-ex-4a1
Suppose $(X, \mathcal{S}, \mu)$ is a measure space and $h: X \to \mathbb{R}$ is an $\mathcal{S}$-measurable function.
Prove that

$$\mu\left(x \in X: |h(x)| \geq c \right) \leq \frac{1}{c^p} \int |h|^p d\mu$$

for all positive numbers $c$ and $p.$

:::{dropdown} Solution
Note that for all positive numbers $c$ and $p,$ we have $|h(x)| > c$ if and only if $|h(x)|^p > c^p.$
Therefore, applying Markov's inequality, we have

$$\mu\left(x \in X: |h(x)| \geq c \right) = \mu\left(x \in X: |h(x)|^p \geq c^p \right) \leq \frac{1}{c^p} \int |h|^p d\mu.$$
:::
::::



::::{admonition} Exercise 4.A.2 (Chebyshev's inequality)
:class: tip
:label: mira-ex-4a2
Suppose $(X, \mathcal{S}, \mu)$ is a measure space with $\mu(X) = 1$ and $h \in \mathcal{L}^1(\mu).$
Prove that

$$\mu\left(x \in X: \left|h(x) - \int h d\mu\right| \geq c \right) \leq \frac{1}{c^2} \int \left|h - \int h d\mu\right|^2 d\mu$$

for all $c > 0.$

:::{dropdown} Solution
Note that for all $c > 0,$ we have $\left|h(x) - \int h d\mu\right| \geq c$ if and only if $\left|h(x) - \int h d\mu\right|^2 \geq c^2.$
Therefore, applying the result of {prf:ref}`Exercise 4.A.1 <mira-ex-4a1>`, we have

$$\begin{align}
\mu\left(x \in X: \left|h(x) - \int h d\mu\right| \geq c \right) &\leq \frac{1}{c^2} \int \left|h - \int h d\mu\right|^2 d\mu 
&= \frac{1}{c^2} \int \left(h - \int h d\mu\right)^2 d\mu.
&= \frac{1}{c^2} \left(\int h^2 d\mu - \left(\int h d\mu\right)^2\right).
\end{align}$$
:::
::::



::::{admonition} Exercise 4.A.3
:class: tip
Suppose $(X, \mathcal{S}, \mu)$ is a measure space.
Suppose $h \in \mathcal{L}^{1}(\mu)$ and $||h||_1 > 0.$
Prove that there exists at most one number $c \in (0, \infty)$ such that

$$\mu\left(x \in X: |h(x)| \geq c \right) = \frac{||h||_1}{c}.$$

:::{dropdown} Solution
We have

$$\mu(\{x \in X: |h(x)| \geq c\}) \leq \frac{1}{c} \int_{\{x \in X: |h(x)| \geq c\}} |h| d\mu \leq ||h||_1.$$

Therefore, if the condition in the exercise holds, then we must have

$$\mu(\{x \in X: |h(x)| \geq c\}) = \frac{1}{c} \int_{\{x \in X: |h(x)| \geq c\}} |h| d\mu.$$

Define $A_c = \{x \in X: |h(x)| \geq c\}.$
Then, we have

$$c \mu(A_c) = \int_{A_c} |h| d\mu,$$

which implies that $h$ is equal to $c$ on $A_c$ $\mu$-almost everywhere.
Note that, by the equation above, if $A_c$ has zero measure, then $|h|$ is zero $\mu$-almost everywhere on $X$ so the condition $||h||_1 > 0$ is not satisfied.
Therefore, $A_c$ must have positive measure.
Now, suppose there exists another number $c' > c$ such that

$$\mu\left(x \in X: |h(x)| \geq c' \right) = \frac{||h||_1}{c'}.$$

Then, $A_{c'} \subseteq A_c,$ and $0 < |A_{c'}| < |A_c|.$
Further, by the same argument as above, we have $h = c'$ on $A_{c'}$ $\mu$-almost everywhere.
However, this is a contradiction, because $h = c$ on $A_c$ $\mu$-almost everywhere.
Therefore, there cannot exist a second number $c' > c$ such that the condition in the exercise holds.
:::
::::



::::{admonition} Exercise 4.A.4
:class: tip
Show  that the constant $3$ in the Vitali Covering Lemma cannot be replaced by a smaller positive constant.

:::{dropdown} Solution
Note that the constant $3$ in the Vitali covering lemma (VCL) cannot be replaced by a number less than or equal to $1.$
Suppose that it can be replaced by some constant $C$ with $1 < C < 3.$
Consider the list containing the two intervals $(-2-\epsilon, \epsilon)$ and $(-\epsilon, 2+\epsilon)$ for some $\epsilon > 0.$
Now, VCL requires that we select a subset of disjoint intervals from this list, so we can select at most one of them.
In order for this interval to contain the union of both intervals, we must have

$$\epsilon \geq \frac{3 - C}{C - 1}.$$

Therefore, the conclusion of VCL would be violated for any $\epsilon < (3 - C)(C - 1).$
We conclude that the constant $3$ in VCL cannot be replaced by a smaller positive constant.
:::
::::



::::{admonition} Exercise 4.A.9
:class: tip
Suppoose $h: \mathbb{R} \to \mathbb{R}$ is Lebesgue measurable.
Prove that

$$\{b \in \mathbb{R}: h^*(b) > c\}$$

is an open subset of $\mathbb{R}$ for every $c \in \mathbb{R}.$

:::{dropdown} Solution
Suppose $h: \mathbb{R} \to \mathbb{R}$ is Lebesgue measurable.
Let $c > 0$ and define

$$A_c = \{b \in \mathbb{R}: h^*(b) > c\}.$$

Let $m: \mathbb{R} \times (0, \infty) \to \infty$ be the function

$$m(b, t) = \frac{1}{2t} \int_{b - t}^{b + t} |h| d\mu.$$

Let $a \in A_c.$
By the definition of supremum, there exist $\epsilon > 0, t_\epsilon > 0$ such that

$$m(a, t_\epsilon) > c + \epsilon.$$

Because of the property thatt integrals on small sets are small, there exists $\delta > 0$ such that

$$\int_B |h|d\mu < \epsilon$$

for every set $B \subseteq \mathcal{S}$ such that $\mu(B) < \delta.$
Now, consider a ball of radius $\delta / 2$ centered at $a.$
Then, for any $a' \in B_{\delta/2}(a),$ we have

$$\begin{align}
\left|m(a', t_\epsilon) - m(a, t_\epsilon)\right| &< \left|\int_{a' - t_\epsilon}^{a' + t_\epsilon} |h| d\mu - \int_{a - t_\epsilon}^{a + t_\epsilon} |h| d\mu\right| \\
&\leq \left|\int_B |h| d\mu\right| \\
&< \epsilon.
\end{align}$$

where $B = [a' - t_\epsilon, a' + t_\epsilon] \Delta [a - t_\epsilon, a + t_\epsilon],$ where $\Delta$ denotes the symmetric difference of two sets.
Thus $\mu(B) < \delta,$ so $m(a', t_\epsilon) > c$ for all $a' \in B_{\delta/2}(a).$
Therefore

$$h^*(a') > m(a', t_\epsilon) > c$$

which implies that $a' \in A_c$ and $B_{\delta/2}(a) \subseteq A_c.$
This means that $A_c$ is open.
:::
::::




::::{admonition} Exercise 4.A.10
:class: tip
:label: mira-ex-4a10
Prove or give a counterexample: if $h: \mathbb{R} \to [0, \infty)$ is an increasing function, then $h^*$ is also an increasing function.

:::{dropdown} Solution
Suppose $h: \mathbb{R} \to [0, \infty)$ is an increasing function, and let $a, b \in \mathbb{R}$ with $a < b.$
For $x \in \mathbb{x}$ define $h_x$ as $h_x(c) = h(c)$ for all $c \in \mathbb{R}.$
Then, since $h$ is increasing, $h_x > h$ for all $x \in \mathbb{R},$ so

$$\int_{a - t}^{a + t} |h| \leq \int_{a - t}^{a + t} |h_x|$$

for all $x \in \mathbb{R}$ and $t > 0.$
Therefore

$$\int_{a - t}^{a + t} |h| \leq \int_{a - t}^{a + t} |h_(b - a)| = \int_{b - t}^{b + t} |h|,$$

and taking the supremum over $t > 0$ we arrive at the result.
:::
::::




::::{admonition} Exercise 4.A.11
:class: tip
Give an example of a Borel meeasurable function $h: \mathbb{R} \to [0, \infty)$ such that $h^*(b) < \infty$ for all $b \in \mathbb{R}$ but $\sup\{h^*(b): b\in \mathbb{R}\} = \infty.$

:::{dropdown} Solution
We will give an example and a high-level justification for why it works without proving this.
Consider the function $h: \mathbb{R} \to [0, \infty)$ defined as

$$h(x) = \sum_{n=1}^\infty n \chi_{[2^n, 2^n + 1]}.$$

This is a countable sum of Borel measurable functions and is therefore Borel measurable.
Note also that $h^*(2^n + 1/2) \to \infty$ as $n \to \infty,$ so $\sup\{h^*(b): b\in \mathbb{R}\} = \infty.$
Finally, we note that since the gap between individual characteristic functions increases exponentially quickly, while the height of each characteristic function increases linearly, it follows that for any $b \in \mathbb{R},$ the quantity $\int_{b - t}^{b + t} |h|$ is bounded in $t$ and therefore $h^*(b) < \infty.$
:::
::::



## Chapter 5.A

::::{admonition} Exercise 5.A.1
:class: tip
Suppose $(X, S)$ and $(Y, T)$ are measurable spaces.
Prove that if $A$ is a nonempty subset of $X$ and $B$ is a nonempty subset of $Y$ such that $A \times B \in S \otimes T,$ then $A \in S$ and $B \in T.$

:::{dropdown} Solution
Suppose $(X, S)$ and $(Y, T)$ are measurable spaces, and that if $A$ is a nonempty subset of $X$ and $B$ is a nonempty subset of $Y$ such that $A \times B \in S \otimes T.$
Since $A$ and $B$ are nonempty, there exist $a \in A$ and $b \in B.$
Since cross sections of measurable sets are measurable, we have $A = [A \times B]_a \in T$ and $B = [A \times B]^b \in S.$
:::
::::

::::{admonition} Exercise 5.A.10
:class: tip
Suppose $(X, S, \mu)$ and $(Y, T, \nu)$ are $\sigma$-finite measure spaces.
Prove that if $\omega$ is a measure of $S \otimes T$ such that $\omega(A \times B) = \mu(A)\nu(B)$ for all $A \in S$ and all $B \in T,$ then $\omega = \mu \times \nu.$

:::{dropdown} Solution
Let $\mathcal{A}$ be the set of all finite unions of rectangles $A \times B$ where $A \in S$ and $B \in T,$ and note that $\mathcal{A}$ is an algebra.
Since a finite union of rectangles can be expressed as a disjoint finite union of rectangles, from now on we will assume that the elements of $\mathcal{A}$ are disjoint finite unions of rectangles.
Now, define the set

$$\mathcal{M} = \left\{E \in S \otimes T: \omega(E) = (\mu \times \nu)(E)\right\}.$$

Note that $\omega$ agrees with $\mu \times \nu$ on all rectangles.
Therefore, they also agree on all disjoint unions of rectangles.
So $\omega$ and $\mu \times \nu$ agree on every element of $\mathcal{A},$ so $\mathcal{A} \subseteq \mathcal{M}.$
Now, we will show that $\mathcal{M}$ is a monotone class.
First, suppose that $E_1 \subseteq E_2 \subseteq \dots$ is a sequence of sets in $\mathcal{M}.$
Then, we have

$$\lim_{n \to \infty} \omega(E_n) = \lim_{n \to \infty} (\mu \times \nu)(E_n) \implies \omega(E) = (\mu \times \nu)(E_n).$$

Second, suppose that $E_1 \supseteq E_2 \supseteq \dots.$ 
Since $(X, S, \mu)$ and $(Y, T, \nu)$ are $\sigma$-finite measure spaces, there exist disjoint sequences of sets $X_1, X_2 \dots$ and $Y_1 \subseteq Y_2 \dots,$ such that

$$\bigcup_{n = 1}^\infty X_n = X ~~\text{ and }~~ \bigcup_{n = 1}^\infty Y_n = Y$$

and also $\mu(X_n), \mu(Y_n) < \infty$ for all $k \in \mathbb{Z}^+.$
Now define $R_1, R_2, \dots$ to be the sequence of rectangles

$$X_1 \times Y_1, X_1 \times Y_2, X_2 \times Y_1, \dots.$$

This sequence is disjoint and its union equals $S \times T.$
Also, $\omega(R_k) = (\mu \times \nu)(R_k) < \infty$ for all $k \in \mathbb{R}.$
Therefore, defining $E = \cap_{n = 1}^\infty E_n,$ we have

$$\begin{align}
\omega(E) &= \sum_{j = 1}^\infty \omega(R_j \cap E) \\
          &= \sum_{j = 1}^\infty \omega(\lim_{n \to \infty} R_j \cap E_n) \\
          &= \sum_{j = 1}^\infty \lim_{n \to \infty} \omega(R_j \cap E_n) \\
          &= \lim_{n \to \infty} \sum_{j = 1}^\infty \omega(R_j \cap E_n) \\
          &= \lim_{n \to \infty} \omega(E_n),
\end{align}$$

where in the third line we have used the bounded convergence theorem.
By a similar argument, we have

$$(\mu \times \nu)(E) = \lim_{n \to \infty} (\mu \times \nu)(E_n).$$

Putting these results together, we have $\omega(E) = (\mu \times \nu)(E),$ so $\mathcal{M}$ is a monotone class.
Since $\mathcal{M}$ is a monotone class that contains $\mathcal{A},$ it contains $S \otimes T$ so $\mathcal{M} = S \otimes T,$ and the two measures $\omega$ and $\mu \times \nu$ agree on all of $S \otimes T.$
:::
::::


## Chapter 6.A

::::{admonition} Exercise 6.A.1
:class: tip
Verify that each of the following examples of sets $V$ and functions $d: V \times V \to \mathbb{R}$ are indeed metric spaces.

1. Suppose $V$ is a nonempty set.
Define $d$ as

$$\begin{equation}
d(f, g) = \begin{cases}
1 &\text{ if } f = g \\
0 &\text{ if } f \neq g
\end{cases}
\end{equation}$$

2. Let $V = \mathbb{R}.$
Define $d$ as

$$\begin{equation}
d(x, y) = |x - y|.
\end{equation}$$

3. Let $V = \mathbb{R}.$
For $n \in \mathbb{Z}^+,$ define $d$ as

$$\begin{equation}
d((x_1, \dots, x_n), (y_1, \dots, y_n)) = \max\{\|x_1 - y_1|, \dots, |x_n - y_n|\}.
\end{equation}$$

4. Let $V = C([0, 1]),$ the set of continuous real-valued functions on $[0, 1].$
Define $d$ as

$$\begin{equation}
d(f, g) = \sup\{|f(t) - g(t)|: t \in [0, 1]|\}.
\end{equation}$$

5. Let $V$ be the set of sequences $(a_1, a_2, \dots)$ with $a_k \in \mathbb{R}$ and $\sum_{n=1}^\infty |a_k| < \infty.$
Define $d$ as

$$\begin{equation}
d((a_1, a_2, \dots), (b_1, b_2, \dots)) = \sum_{n=1}^\infty |a_k - b_k|.
\end{equation}$$


:::{dropdown} Solution
For all the definitions above, $d(f, g) \geq 0$ and equality with zero holds only if $f, g.$
Further, $d(f, g) = d(g, f).$
It remains to show the triangle inequality

$$\begin{equation}
d(f, h) \leq d(f, g) + d(g, h) \text{ for all } f, g, h \in V
\end{equation}$$

holds for each example.

__Example 1:__
Suppose $f, g, h \in \mathbb{V}.$
If $f = h,$ then the triangle inequality holds since

$$\begin{equation}
d(f, h) = 0 \leq d(f, g) + d(g, h),
\end{equation}$$

holds.
If $f \neq h,$ then at least one of $f \neq g$ and $g \neq h$ must hold, so the triangle inequality holds because

$$\begin{equation}
d(f, h) = 1 \leq d(f, g) + d(g, h).
\end{equation}$$

__Example 2:__
Suppose $f, g, h \in \mathbb{R}.$
Then the triangle inequality holds because

$$\begin{equation}
d(f, h) = |f - h| = |(f - g) + (g - h)| \leq |f - g| + |g - h| \leq d(f, g) + d(g, h).
\end{equation}$$

__Example 3:__
Suppose $n \in \mathbb{Z}^+$ and $(x_1, \dots, x_n), (y_1, \dots, y_n), (z_1, \dots, z_n) \in \mathbb{R}^n.$
Then the triangle inequality holds because

$$\begin{align}
&~~~~d((x_1, \dots, x_n), (z_1, \dots, z_n)) = \\
&= \max\{|x_1 - z_1|, \dots, |x_n - z_n|\} \\
&= \max\{|(x_1 - y_1) + (y_1 - z_1)|, \dots, |(x_n - y_n) + (y_n - z_n)|\} \\
&\leq \max\{|x_1 - y_1| + |y_1 - z_1|, \dots, |x_n - y_n| + |y_n - z_n|\} \\
&\leq \max\{|x_1 - y_1|, \dots, |x_n - y_n|\} + \max\{|y_1 - z_1|, \dots, |y_n - z_n|\} \\
&\leq d((x_1, \dots, x_n), (y_1, \dots, y_n)) + d((y_1, \dots, y_n), (z_1, \dots, z_n)).
\end{align}$$

__Example 4:__
Suppose $f, g, h \in C([0, 1]).$
Then, the triangle inequality holds because

$$\begin{align}
d(f, h) &= \sup\{|f(t) - h(t)|: t \in [0, 1]|\} \\
&= \sup\{|(f(t) - g(t)) + (g(t) - h(t))|: t \in [0, 1]|\} \\
&\leq \sup\{|f(t) - g(t)| + |g(t) - h(t)|: t \in [0, 1]|\} \\
&\leq \sup\{|f(t) - g(t)|: t \in [0, 1]|\} + \sup\{|g(t) - h(t)|: t \in [0, 1]|\} \\
&= d(f, g) + d(g, h).
\end{align}$$

__Example 5:__
Suppose $(f_1, f_2, \dots), (g_1, g_2, \dots), (h_1, h_2, \dots) \in V,$ where $V$ is the set of sequences $(a_1, a_2, \dots)$ of real numbers such that $\sum_{n=1}^\infty |a_k| < \infty.$
Then, the triangle inequality holds because

$$\begin{align}
&~~~~d((f_1, f_2, \dots), (h_1, h_2, \dots)) = \\
&= \sum_{n=1}^\infty |f_k - h_k| \\
&= \sum_{n=1}^\infty |(f_k - g_k) + (g_k - h_k)| \\
&\leq \sum_{n=1}^\infty |f_k - g_k| + |g_k - h_k| \\
&= d((f_1, f_2, \dots), (g_1, g_2, \dots)) + d((g_1, g_2, \dots), (h_1, h_2, \dots)).
\end{align}$$

:::
::::


::::{admonition} Exercise 6.A.2
:class: tip
Prove that every finite subset of a metric space is closed.

:::{dropdown} Solution
Suppose $(V, d)$ is a metric space and let $A$ be a finite subset of $V.$
Let $x \in A'.$
Since $A$ is finite, the set $\{d(x, y) \in \mathbb{R}^+: y \in A\}$ has a minimum element, and this minimum element is non-zero, say equal to some positive $m \in \mathbb{R}$
Therefore, any open ball centered on $x$ with radius less than or equal to $m$ is contained in $A'.$
Since $x$ was arbitrary, $A'$ is open, so $A$ is closed.
:::
::::

::::{admonition} Exercise 6.A.3
:class: tip
Prove that every closed ball in a metric space is closed.

:::{dropdown} Solution
Suppose $(V, d)$ is a metric space.
Let $r \in \mathbb{R}^+$ and $f \in V.$
Let $g \in \overline{B}(f, r)'.$
Then, $d(f, g) > r$ so the open ball $B(g, d(f, g) - r)$ does not intersect the closed ball $\overline{B}(f, r).$
[Otherwise there would exist a common element $h \in B(g, d(f, g) - r) \cap \overline{B}(f, r)$ which leads to a contradiction via the triangle inequality since $d(f, g) \leq d(f, h) + d(h, g) < r.$]
Since the two balls do not intersect, $B(g, r - d(f, g)) \subseteq \overline{B}(f, r)',$ which means that $\overline{B}(f, r)'$ is an open set, so $\overline{B}(f, r)$ is a closed set.
:::
::::

::::{admonition} Exercise 6.A.4
:class: tip

Suppose $V$ is a metric space.

1. Prove that the union of each collection of open subsets of $V$ is an open subset of $V.$
2. Prove that the intersection of each finite collection of open subsets of $V$ is an open subset of $V.$

:::{dropdown} Solution
In the following parts, $V$ is a metric space and $\mathcal{A}$ is a collection of subsets of $V.$

__Part 1:__
Let $S = \cup_{A \in \mathcal{A}} A.$
If $s \in S,$ there exists some $A \in \mathcal{A}$ such that $s \in A.$
Since every $A \in \mathcal{A}$ is open, there exists an open ball centered on $s$ that is contained in $A.$
This open ball is also contained in $S,$ so $S$ is open.

__Part 2:__
Now suppose that, in addition, $\mathcal{A} = \{A_1, \dots A_N\}$ is finite.
If $s \in S,$ then $s \in A_n$ for $n = 1, \dots, N.$
Since each $A$ is open, for each $A_n \in \mathcal{A},$ there exists an open ball centered on $s$ with radius $r_n,$ which is contained in $A_n.$
Now, letting $r = \min\{r_1, \dots, r_N\}$ we see that the open ball centered on $s$ with radius $r$ is contained in each $A_n$ and therefore it is also contained in their intersection, i.e. it is contained in $S.$
Therefore there exists an open ball centered on $s \in S,$ which implies that $S$ is open.
:::
::::


::::{admonition} Exercise 6.A.5
:class: tip

Suppose $V$ is a metric space.

1. Prove that the intersection of each collection of closed subsets of $V$ is an open subset of $V.$
2. Prove that the union of each finite collection of open subsets of $V$ is an open subset of $V.$

:::{dropdown} Solution
The complement of an intersection of a collection of sets is equal to the union of the complements of the sets in the collection.
Similarly, the complement of a union of a collection of sets is equal to the intersection of the complements of the sets in the collection.
Therefore, applying the result of the previous exercise we arrive at the two required results.
:::
::::


::::{admonition} Exercise 6.A.6
:class: tip

1. Prove that if $V$ is a metric space, $f \in V,$ and $r > 0,$ then $\overline{B(f, r)} \subseteq \overline{B}(f, r).$
2. Give an example of a metric space $V,$ $f \in V,$ and $r > 0$ such that $\overline{B(f, r)} \neq \overline{B}(f, r).$

:::{dropdown} Solution

__Part 1:__
First, note that $B(f, r) \subseteq \overline{B}(f, r).$
Second $\overline{B}(f, r)$ is a closed set, and the closure of a set is the intersection of all closed sets that contain it, so $\overline{B(f, r)}$ is contained in any closed set that contains $B(f, r),$ so $\overline{B(f, r)} \subseteq \overline{B}(f, r).$

__Part 2:__
Let $V = \mathbb{Z}$ with the metric $d: \mathbb{Z} \times \mathbb{Z} \to \mathbb{R}^+$ defined as $d(f, g) = |f - g|.$
Also let $f = 0$ and $r = 1.$
Then $B(f, r) = \{0\}$ and so $\overline{B(f, r)} = \{0\}.$
However, $\overline{B}(f, r) = \{-1, 0, 1\}$ so $\overline{B(f, r)} \neq \overline{B}(f, r)$ as required.
:::
::::

::::{admonition} Exercise 6.A.7
:class: tip
Show that each sequence in a metric space has at most one limit.

:::{dropdown} Solution
Let $(V, d)$ be a metric space.
Suppose $f_1, f_2, \dots \in V$ is a sequence in $V.$
If $a, b \in V$ are limits of $f_1, f_2, \dots,$ then

$$\begin{equation}
\lim_{n \to \infty} d(f_n, a) = 0 \text{ and } \lim_{n \to \infty} d(f_n, b) = 0.
\end{equation}$$

From the triangle inequality, $d(a, b) \leq d(a, f_n) + d(f_n, b),$ and taking limits of both sides, we conclude that $d(a, b) = 0,$ which implies that $a = b.$
Therefore the sequence can have at most one limit in $V.$
:::
::::


::::{admonition} Exercise 6.A.8
:class: tip
Prove that each open subset of a metric space $V$ is the union of some sequence of closed subsets of $V.$

:::{dropdown} Solution
Let $V$ be a metric space, let $U$ be an open subset of $V$ and define

$$\begin{equation}
U_r = \{f \in V: d(f, g) \geq r \text{ for all } g \in U'\}.
\end{equation}$$

Therefore $U_r$ is the set of elements in $U$ that are at least a distance $r$ away from $V.$
Note also that $U_r \subseteq U.$
Now, note that for fixed $g \in U',$ the set $\{f \in V: d(f, g) \geq r\}$ is closed, because it is the complement of the open set $\{f \in V: d(f, g) < r\}.$
The intersection of a collection of closed sets is closed, so $U_r$ is closed.

Now, note that for each $n \in \mathbb{Z}^+,$ we have $U_{\frac{1}{n}} \subseteq U,$ from which it follows that $\bigcup_{n = 1}^\infty U_{\frac{1}{n}} \subseteq U.$
Conversely, if $x \in U,$ since $U$ is open there exists a ball of radius $\frac{1}{n}$ for some $n \in \mathbb{Z}^+$ contained in $U,$ so $x \in U_{\frac{1}{n}},$ from which it follows that $U \subseteq \bigcup_{n = 1}^\infty U_{\frac{1}{n}}.$
Therefore $U$ is the union of a sequence of closed sets in $V,$ as required.

:::
::::


::::{admonition} Exercise 6.A.10
:class: tip
Prove or give a counterexample:
If $V$ is a metric space and $U, W$ are subserts of $V,$ then $\overline{U} \cup \overline{W} = \overline{U \cup W}.$

:::{dropdown} Solution
If $v \in \overline{U},$ then there exists a sequence of elements in $U$ whose limit is $v.$
Therefore there exists a sequence of elements in $U \cup W$ whose limit is $v,$ so $v \in \overline{U \cup W}.$
Similarly, if $v \in \overline{W},$ it follows that $v \in \overline{U \cup W}.$
We conclude that $\overline{U} \cup \overline{W} \subseteq \overline{U \cup W}.$

If $v \in \overline{U \cup W},$ then $v$ must be the limit of a sequence of elements in $U \cup W.$
This sequence must have a infinite subsequence of elements in at least one of $U$ or $W$ with $v$ as its limit, so $v \in \overline{U} \cup \overline{W}.$
We conclude that $\overline{U \cup W} \subseteq \overline{U} \cup \overline{W},$ which completes the proof.
:::
::::


::::{admonition} Exercise 6.A.11
:class: tip
Prove or give a counterexample:
If $V$ is a metric space and $U, W$ are subsets of $V,$ then $\overline{U} \cap \overline{W} = \overline{U \cap W}.$

:::{dropdown} Solution
The equation does not hold.
As a counterexample, consider $\mathbb{R}$ with the metric

$$d(f, g) = |f - g|,$$

and let $U = (-1, 0), W = (0, 1).$
Then we have $\overline{U} = [-1, 0]$ and $\overline{W} = [0, 1].$
Therefore, we have $\overline{U} \cap \overline{W} = \{0\},$ but $U \cap W = \emptyset$ so $\overline{U \cap W} = \emptyset.$
:::
::::


::::{admonition} Exercise 6.A.12
:class: tip
Suppose $(U, d_U), (V, d_V)$ and $(W, d_W)$ are metric spaces.
Suppose also that $T: U \to V$ and $S: V \to W$ are continuous functions.

1. Using the definition of continuity, show that $S \circ T: U \to W$ is continuous.
2. Using the equivalence of continuity with the property that the limit of a function is equal to the function of its limit, show that $S \circ T: U \to W$ is continuous.
3. Using the equivalence of continuity with the property that the inverse image of an open set under a function is open, show that $S \circ T: U \to W$ is continuous.

:::{dropdown} Solution
__Part 1:__
Let $v \in V$ and $\epsilon > 0.$
Since $S$ is continuous, there exists $\delta_S > 0$ such that $d_W(S(v), S(v')) < \epsilon$ for all $v' \in V$ such that $d_V(v, v') < \delta_S.$
Let $u \in U.$
Since $T$ is continuous, there exists $\delta_T > 0$ such that $d_V(T(u), T(u')) < \delta_S$ for all $u' \in U$ such that $d_U(u, u') < \delta_T.$
Letting $v = T(u)$ and putting together these facts, we see that $d_W(S \circ T(u), S \circ T(u')) < \epsilon$ for all $u' \in U$ such that $d_U(u, u') < \delta_T,$ which shows that $S \circ T$ is continuous.

__Part 2:__
Suppose $u_1, u_2, \dots$ is a sequence in $U$ with limit $u \in U.$
Since $S$ and $T$ are both continuous

$$\begin{align}
S \circ T(u) &= S(T(u)) \\
&= S\left(T\left(\lim_{k \to \infty} u_k\right)\right) \\
&= S\left(\lim_{k \to \infty} T(u_k)\right) \\
&= \lim_{k \to \infty} S\left(T(u_k)\right) \\
&= \lim_{k \to \infty} S \circ T (u_k)
\end{align}$$

Therefore $S \circ T$ is continuous.

__Part 3:__
Suppose $G$ is an open subset in $W.$
Since $S$ is continuous, $S^{-1}(G)$ is open in $V$ and since $T$ is continuous, $T^{-1}(S^{-1}(G)) = (S \circ T)^{-1}(G)$ is open in $U,$ so $S \circ T$ is continuous.
:::
::::

::::{admonition} Exercise 6.A.14
:class: tip
Suppose a Cauchy sequence in a metric space has a convergent subsequence.
Prove that the Cauchy sequence converges.

:::{dropdown} Solution
Let $(V, d)$ be a metric space and $v_1, v_2, \dots$ be a Cauchy sequence in $V.$
Suppose that $v_{k_1}, v_{k_2}, \dots$ is a subsequence which converges to $v \in V.$
Let $\epsilon > 0.$
Since the sequence $v_1, v_2, \dots$ is Cauchy, there exists $K$ such that for all $k, k' \geq K$ we have $d(v_k, v_{k'}) < \frac{\epsilon}{2}.$
In addition, by our earlier assumption, there exists $N$ such that for all $n \geq N$ we have $d(v_{k_n}, v) < \frac{\epsilon}{2}.$
Then, letting $L$ be the maximum of $K$ and $k_N$ we see that for any $l \geq L$ it holds that $d(v_l, v) \leq d(v_l, v_k) + d(v_k, v) < \epsilon,$ concluding the proof.
:::
::::


::::{admonition} Exercise 6.A.16
:class: tip
Suppose $(U, d)$ is a metric space.
Let $W$ denote the set of all Cauchy sequences of elements of $U.$

1. For $(f_1, f_2, \dots)$ and $(g_1, g_2, \dots)$ in $W,$ define $(f_1, f_2, \dots) \equiv (g_1, g_2, \dots)$ to mean that $\lim_{k \to \infty} d(f_k, g_k) = 0.$
Show that $\equiv$ is an equivalence relation on $W.$

2. Let $V$ denote the set of equivalence classses of elements of $W$ under the equivalence relation above.
For $(f_1, f_2, \dots) \in W,$ let $(f_1, f_2, \dots)\hat{~}$ denote the equivalence class of $(f_1, f_2, \dots).$
Show that the following definition of $d_V: V \times V \to [0, \infty)$ makes sense and that $d_V$ is a metric on $V$

$$\begin{equation}
d_V((f_1, f_2, \dots)\hat{~}, (g_1, g_2, \dots)\hat{~}) = \lim_{k \to \infty} d(f_k, g_k).
\end{equation}$$

3. Show that $(V, d_V)$ is a complete metric space.

4. Show that the map from $U$ to $V$ that takes $f \in U$ to $(f, f, f, \dots)\hat{~}$ preserves distances, meaning that for all $f, g \in U,$ we have

$$d(f, g) = d_V((f, f, f, \dots)\hat{~}, (g, g, g, \dots)\hat{~})$$

5. Explain why (4) shows that every metric space is a subset of some complete metric space.


:::{dropdown} Solution
__Part 1:__
First, we have that $d(f_k, f_k) = 0$ so $(f_1, f_2, \dots) \equiv (f_1, f_2, \dots).$
Second, if $(f_1, f_2, \dots) \equiv (g_1, g_2, \dots),$ we have

$$\lim_{k \to \infty} d(f_k, g_k) = 0 \implies \lim_{k \to \infty} d(g_k, f_k) = 0,$$

so it follows that $(g_1, g_2, \dots) \equiv (f_1, f_2, \dots).$
Third, if $(f_1, f_2, \dots) \equiv (g_1, g_2, \dots),$ and $(g_1, g_2, \dots) \equiv (h_1, h_2, \dots),$ we have that

$$\lim_{k \to \infty} d(f_k, h_k) \leq \lim_{k \to \infty} (d(f_k, g_k) + d(g_k, h_k)) = 0,$$

which means that $(f_1, f_2, \dots) \equiv (h_1, h_2, \dots).$
Therefore $\equiv$ is an equivalence relation.

__Part 2:__
First, for $d_V$ to be well-defined, it should not matter which representative elements of $(f_1, f_2, \dots)\hat{~}$ and $(g_1, g_2, \dots)\hat{~}$ we pick in the right hand side of the equation that defines $d_V.$
In particular, suppose $(\tilde{f}_1, \tilde{f}_2, \dots) \in (f_1, f_2, \dots)\hat{~}.$
Then

$$\begin{equation}
\lim_{k \to \infty} d(\tilde{f}_k, g_k) \leq \lim_{k \to \infty} (d(f_k, g_k) + d(f_k, \tilde{f}_k)) = \lim_{k \to \infty} d(f_k, g_k),
\end{equation}$$

so it does not matter which representative element of $(f_1, f_2, \dots)\hat{~}$ we pick when defining $d_V.$
The same holds for $(g_1, g_2, \dots)\hat{~},$ so $d_V$ is well-defined.

Second, we show that $d_V$ is a metric.
By the definition of $d_V,$ we have that

$$d_V((f_1, f_2, \dots)\hat{~}, (g_1, g_2, \dots)\hat{~}) \geq 0,$$

with equality holding if and only if $\lim_{k \to \infty} d(f_k, g_k) = 0,$ which in turn holds if and only if $(f_1, f_2, \dots) \equiv (g_1, g_2, \dots),$ which is equivalent to $(f_1, f_2, \dots)\hat{~} = (g_1, g_2, \dots)\hat{~}.$
In addition, we have that

$$\begin{equation}
d_V((f_1, f_2, \dots)\hat{~}, (g_1, g_2, \dots)\hat{~}) = d_V((g_1, g_2, \dots)\hat{~}, (f_1, f_2, \dots)\hat{~})
\end{equation}$$

because $d(f_k, g_k) = d(g_k, f_k).$
Lastly, if $(h_1, h_2, \dots) \in W,$ we have that

$$\begin{align}
&~~~~d_V((f_1, f_2, \dots)\hat{~}, (h_1, h_2, \dots)\hat{~}) =\\
&= \lim_{k \to \infty} d(f_k, h_k) \\
&\leq\lim_{k \to \infty} (d(f_k, g_k) + d(g_k, h_k)) \\
&= d_V((f_1, f_2, \dots)\hat{~}, (g_1, g_2, \dots)\hat{~}) + d_V((g_1, g_2, \dots)\hat{~}, (h_1, h_2, \dots)\hat{~}),
\end{align}$$

so $d_V$ satisfies the triangle inequality, completing the proof that it is a metric.

__Part 3:__
Suppose that $(v_1, v_2, \dots)$ is a Cauchy sequence in $V.$
We will show that there exists an element $w \in V$ and $K \in \mathbb{Z}^+$ such that for all $k \geq K$ we have $\lim_{i \to \infty} d((v_k)_i, w_i) = 0.$
Since each sequence $v_k$ is itself Cauchy, there exists $N_k \in \mathbb{Z}^+$ such that $N_k \geq k$ and for all $i, j \geq N_k,$ we have $d(v_i, v_j) < \frac{1}{k}.$
Define the terms of the sequence $w$ to be $w_k = (v_k)_{N_k}.$
We now show that $w$ is in fact the limit of $(v_1, v_2, \dots).$

Let $\epsilon > 0.$
Since $(v_1, v_2, \dots)$ is Cauchy, there exists $N_{\epsilon}^{(1)} \in \mathbb{Z}^+$ such that for all $i, j \geq N_{\epsilon}^{(1)},$ we have 

$$\lim_{k \to \infty} d((v_i)_k, (v_j)_k) < \frac{\epsilon}{3}.$$

In addition, for fixed $k \in \mathbb{Z}^+$ since each sequence $v_k$ is Cauchy, there exists $N_{k, \epsilon}^{(2)} \in \mathbb{Z}^+$ such that for all $i, j \geq N_{k, \epsilon}^{(2)},$ we have

$$\lim_{k \to \infty} d((v_k)_i, (v_k)_j) < \frac{\epsilon}{3}.$$

Now, we have that

$$\begin{align}
d((v_k)_i, w_i) &\leq d((v_k)_i, (v_k)_j) + d((v_k)_j, w_i) \\
&= d((v_k)_i, (v_k)_j) + d((v_k)_j, (v_i)_{N_i}) \\
&\leq d((v_k)_i, (v_k)_j) + d((v_k)_j, (v_i)_j) + d((v_i)_j, (v_i)_{N_i})
\end{align}$$

where in the first line we have applied the triangle inequality, in the second line we have substituted the definition $w_i = (v_i)_{N_i}$ and in the third line we have again used the triangle inequality again.
Now, letting $i, k \geq N_{\epsilon}^{(1)}$ means that the limit of the second term in the inequality, as $j \to \infty$, is smaller than $\epsilon / 3.$
In addition, letting $i, j \geq \max(N_{\epsilon}^{(1)}, N_{k, \epsilon}^{(2)})$ means that the first term in the inequality is smaller than $\epsilon / 3.$
Lastly, by the definition of $N_i,$ letting $j \geq \max(N_{\epsilon}^{(1)}, N_{k, \epsilon}^{(2)}, N_i)$ means that the last term in the inequality is smaller than $\frac{1}{i}.$
We therefore obtain

$$\begin{align}
d((v_k)_i, w_i) &\leq \lim_{j \to \infty} d((v_k)_i, (v_k)_j) + \lim_{j \to \infty} d((v_k)_j, (v_i)_j) + \lim_{j \to \infty} d((v_i)_j, (v_i)_{N_i}) \\
&< \frac{2\epsilon}{3} + \frac{1}{i}
\end{align}$$

so for all $i > \frac{3}{\epsilon}$ we have $d((v_k)_i, w_i) < \epsilon.$
This means that $d_V(v_k\hat{~}, w\hat{~}) < \epsilon$ for all $k \geq N_{\epsilon}^{(1)}$ which means that $w\hat{~}$ is the limit of the sequence $(v_1\hat{~}, v_2\hat{~}, \dots),$ so $V$ is a complete metric space.

__Part 4:__
By part (2), defining $f_k = f$ and $g_k = g$ for all $k \in \mathbb{Z}^+,$ we have that

$$d_V((f, f, f, \dots)\hat{~}, (g, g, g, \dots)\hat{~}) = \lim_{k \to \infty} d(f_k, g_k) = d(f, g),$$

as required.

__Part 5:__
We can add elements to the set $U$ to ensure that the resulting set is complete.
Specifically, we add to $U$ the set

$S = \left\{w \in W | w \neq (f, f, f, \dots)\hat{~} \text{ for any } f \in U \right\},$

to obtain the larger set $\hat{U} = U \cup S.$
Now, for $u \in \hat{U},$ we define $\hat{u}$ to be equal to $(u, u, \dots)\hat{~}$ if $u \in U$ and equal to $u$ otherwise.
Then, define the function $d_\hat{U}: \hat{U} \times \hat{U} \to \mathbb{R}$ as

$$d_\hat{U}(u, v) = d_V(\hat{u}, \hat{v}).$$

This function is a metric over $\hat{U}.$
Further, if $(u_1, u_2, \dots)$ is a Cauchy sequence of elements of $U,$ then $(\hat{u_1}, \hat{u_2}, \dots)$ is a Cauchy sequence of equivalence classes in $V.$
Since $V$ is complete, the sequence $(\hat{u_1}, \hat{u_2}, \dots)$ has a limit, denoted $\hat{u},$ in $V.$
Therefore the sequence $(u_1, u_2, \dots)$ converges to $\hat{u}$ in the metric space $(\hat{U}, d_{hat{U}}).$
:::
::::
