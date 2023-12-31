# Exercises

This page gives solutions to the exercises from the book Measure, Integration and Real Analysis by Sheldon Axler.
We have been working through the book and exercises with Adrian Goldwaser and Shreyas Padhy, and these solutions are a joint effort.
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

Suppose $X$ is a set and $S$ is the $\sigma$-algebra of all subsets $E$ of $X$ such that $E$ is countatble or $X \setminus E$ is countable.
Give a complete description of the set of all measures $\mu$ on $(X, S).$

:::{dropdown} Solution

Suppose $X$ is a set and $S$ is the $\sigma$-algebra of all subsets $E$ of $X$ such that $E$ is countatble or $X \setminus E$ is countable.
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