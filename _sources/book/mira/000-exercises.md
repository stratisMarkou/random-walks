# Exercises

This page gives solutions to the exercises from the book Measure, Integration and Real Analysis by Sheldon Axler.
We have been working through the book and exercises with Adrian Goldwasser and Shreyas Padhy, and these solutions are a joint effort.
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

Let $P_N$ be the partition $x_0, \dots x_{3n}$ of $[a, b]$ with $x_n = s$ and $x_{2n} = t,$ defined as

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

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
For $n \in \mathbb{N},$ let $P_n$ denote the partition that divides $[a, b]$ into $2^n$ intervals of equal size.
Prove that

$$\lim_{n \to \infty} L(f, P_n, [a, b]) = L(f, [a, b]) \text{ and } \lim_{n \to \infty} U(f, P_n, [a, b]) = U(f, [a, b]).$$


:::{dropdown} Solution

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function, bounded above by $C$ and below by $-C,$ and define $L = L(f, [a, b]),$ which is finite because $f$ is bounded.
By the definition of supremum, for every $\epsilon > 0$ there exists a partition $R_\epsilon$ of $[a, b]$ such that

$$L(f, [a, b]) - L(f, R_\epsilon, [a, b]) < \epsilon.$$

Let $\delta(R_\epsilon)$ be the size of the smallest subinterval of $R_\epsilon,$ and let $E_{R_\epsilon, k}$ be the partition of $[a, b]$ into $2^{n+k}$ intervals of equal size, such that $\frac{(b-a)}{2^n} \leq \delta(R_\epsilon).$
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
Conversely, if $x \in [0, 1],$ then writing the binary expansion of $x$ as $x = 0.x_1x_2\dots$, we see that

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

Let $X = \mathbb{Q}$ and $S$ be the $\sigma$-algebra of subsets of $\mathbb{Q}$ which are either countable or have countable complements in $\mathbb{Q}.$
Let $\mu$ be the measure on $(\mathbb{Q}, S)$ defined via

$$\mu(x) = \begin{cases}
2^{-n} & \text{if } x = \frac{1}{n} \text{ for } n = 1, 2, \dots, \\
3& \text{if } x = n \text{ for } n = 2, 3, \dots, \\
0 & \text{otherwise}.
\end{cases}$$

Then, for any $E \in S,$ we have $\mu(E) \in \{\infty\} \cup \bigcup_{k = 0}^\infty [3k, 3k + 1].$

:::
::::



::::{admonition} Exercise 2.C.5
:class: tip

Suppose $(X, S, \mu)$ is a measure space such that $\mu(X) < \infty.$
Prove that if $\mathcal{A}$ is a set of disjoint sets in $S$ such that $\mu(A) > 0$ for every $A \in \mathcal{A},$ then $\mathcal{A}$ is countable.

:::{dropdown} Solution

Let $(X, S, \mu)$ be a measure space such that $\mu(X) < \infty.$
Suppose $\mathcal{A}$ is a set of disjoint sets in $S$ such that $\mu(A) > 0$ for every $A \in \mathcal{A}.$

For each $k \in \mathcal{Z},$ let $\mathcal{A}_k = \{A \in \mathcal{A}: 2^k \leq \mu(A) < 2^{k+1}\}.$
Suppose $\mathcal{A}$ is not countable.
Then at least one of the sets $\mathcal{A}_k$ must have an infinite number of elements, which are all disjoint subsets of $X.$

Let $A_1, A_2, \ldots$ be a sequence of elements in $\mathcal{A}_k.$
By countable additivity, we have

$$\mu(X) \geq \mu\left(\bigcup_{A \in \mathcal{A}} A\right) \geq \mu\left(\bigcup_{A \in \mathcal{A}_k} A\right) \geq \mu\left(\bigcup_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty \mu(A_n) \geq \sum_{n=1}^\infty 2^k = \infty,$$

which is a contradiction.
Therefore, $\mathcal{A}$ must be countable.

:::
::::