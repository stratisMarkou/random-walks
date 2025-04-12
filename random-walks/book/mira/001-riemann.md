# Riemann integration

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

The first part of the book introduces the Riemann integral.
The Riemann integral is good enough for many use cases, but it also has important limitations.
We first review the definition of the Riemann integral and its properties.
Then we discuss the limitations of th Riemann integral and show important ways in which it falls short.
This will lead to the idea of the outer measure as a more appropriate definition of length, however we will see that this too fails to capture important properties that we would like it to have.
This leads on to the Lebesgue measure, the Lebesgue integral and more generally Lebesgue integration.

## Riemann integral

We begin with a few definitions needed to write down the definition of the Riemann integral.
Given a function $f: [a, b] \to \mathbb{R},$ we will define its Riemann integral as the limit of an approximation of the area under the curve of $f$ by rectangles which partition $[a, b].$
A partition of $[a, b]$ is defined as follows.

:::{prf:definition} Partition

Suppose $a, b \in \mathbb{R}$ with $a < b$.
A partition of $[a, b]$ is a list of the form $x_0, x_1, \ldots, x_n$ where

$$a = x_0 < x_1 < \ldots < x_n = b.$$
:::

We also need some notation for the infimum and supremum of a function in order to form our approximation.

:::{prf:definition} Infimum and supremum

If $f$ is a real valued function and $A$ is a subset of its domain, then

$$\inf_{x \in A} f(x) = \inf \{ f(x) : x \in A \}, \sup_{x \in A} f(x) = \sup \{ f(x) : x \in A \}.$$
:::

With these definitions in place we can define upper and lower Riemann sums.
A lower (upper) Riemann sum is an approximation of the area under the curve of $f$ by rectangles below (above) the curve.

:::{prf:definition} Upper and lower Riemann sums

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $P$ is a partition $x_0, x_1, \ldots, x_n$ of $[a, b]$.
Then the lower Riemann sum $L(f, P, [a, b])$ and the upper Riemann sum $U(f, P, [a, b])$ are defined as

$$\begin{align}
L(f, P, [a, b]) &= \sum_{i=1}^n (x_i - x_{i-1}) \inf_{x \in [x_{i-1}, x_i]} f, \\
U(f, P, [a, b]) &= \sum_{i=1}^n (x_i - x_{i-1}) \sup_{x \in [x_{i-1}, x_i]} f.
\end{align}$$
:::

A very useful intermediate result is that refining a partition of $[a, b],$ i.e. adding more points to the partition, can only increase the lower Riemann sum and reduce the upper Riemann sum.


:::{prf:theorem} Inequalities with Riemann sums
:label: mira-thm:refining-partitions

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $P, P'$ are partitions of $[a, b],$ such that all the points in $P$ are also contained in $P'.$
Then

$$L(f, P, [a, b]) \leq L(f, P', [a, b]) \leq U(f, P', [a, b]) \leq U(f, P, [a, b]).$$

:::

:::{dropdown} Proof: Inequalities with Riemann sums

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $P$ is the partition $x_0, \dots, x_n$ of $[a, b]$ and $P'$ is the partition $x_0', \dots, x_N'$ of $[a, b].$
Suppose that all the points in $P$ are also contained in $P'.$
Then for any $j = 1, \ldots, n,$ there exists a $k \in \{0, \ldots, N - 1\}$ and a positive integer $m$ such that $x_{j-1} = x_k'$ and $x_{j+1} = x_{k+m}'.$
Then, we have

$$\begin{align}
(x_j - x_{j-1}) \inf_{x \in [x_{j-1}, x_j]} f &= \sum_{i=1}^m (x_{k+i} - x_{k+i-1}) \inf_{x \in [x_{j-1}, x_j]} f \\
&\leq \sum_{i=1}^m (x_{k+i} - x_{k+i-1}) \inf_{x \in [x_{k+i-1}, x_{k+i}]} f,
\end{align}$$

which implies that $L(f, P, [a, b]) \leq L(f, P', [a, b]).$
A similar argument shows that $U(f, P', [a, b]) \leq U(f, P, [a, b]).$
The middle inequality follows from the fact that the infimum of a set is less than or equal to its supremum.
Putting these inequalities together gives the result

$$L(f, P, [a, b]) \leq L(f, P', [a, b]) \leq U(f, P', [a, b]) \leq U(f, P, [a, b]).$$

:::



Another useful inequality which is derived directly from the previous one, is that any lower Riemann sum of a function is less than or equal to any of its upper Riemann sums.

:::{prf:theorem} Lower Riemann sum $\leq$ upper Riemann sum

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $P, P'$ are partitions of $[a, b].$
Then

$$L(f, P, [a, b]) \leq U(f, P', [a, b]).$$

:::

:::{dropdown} Proof: Lower Riemann sum $\leq$ upper Riemann sum

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function and $P, P'$ are partitions of $[a, b].$
Then

$$\begin{align}
L(f, P, [a, b]) &\leq L(f, P \cup P', [a, b]) \\
&\leq U(f, P \cup P', [a, b]) \\
&\leq U(f, P', [a, b]),
\end{align}$$

where the first inequality follows from the {ref}`refinement property of partitions <mira-thm:refining-partitions>`, the second inequality follows from the fact that the infimum of a set is less than or equal to its supremum, and the third inequality follows again from the refinement property.

:::




With these definitions and results in place, we are ready to define lower and upper Riemann integrals.
The lower and upper Riemann integral can be thought of as a bound to the best approximation to the area under the curve of $f$ by rectangles below and above the curve, respectively.

:::{prf:definition} Riemann integral

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
Then the lower Riemann integral $L(f, [a, b])$ and the upper Riemann integral $U(f, [a, b])$ of $f$ are defined as

$$\begin{align}
L(f, [a, b]) &= \sup_P L(f, P, [a, b]), \\
U(f, [a, b]) &= \inf_P U(f, P, [a, b]),
\end{align}$$

where the supremum and infimum are taken over all partitions $P$ of $[a, b].$

:::



From the definition of the lower and upper Riemann integral, and our previous results, it follows that the lower Riemann integral is less than or equal to the upper Riemann integral.

:::{prf:theorem} Lower Riemann integral $\leq$ upper Riemann integral

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
Then

$$L(f, [a, b]) \leq U(f, [a, b]).$$

:::

:::{dropdown} Proof: Lower Riemann integral $~\leq~$ upper Riemann integral

Suppose $f: [a, b] \to \mathbb{R}$ is a bounded function.
Then, for any partition $P$ of $[a, b],$ we have

$$L(f, [a, b]) = \sup_P L(f, P, [a, b]) \leq U(f, P, [a, b])$$

and taking the infimum over all partitions $P$ of $[a, b]$ gives

$$L(f, [a, b]) \leq \sup_P L(f, P, [a, b]) \leq \inf_P U(f, P, [a, b]) = U(f, [a, b]).$$

:::


With these definitions and results in place, we are ready to define the Riemann integral.




:::{prf:definition} Riemann integral

- A bounded function on a closed bounded interval is called Riemann integrable if its lower and upper Riemann integrals are equal.

- If $f: [a, b] \to \mathbb{R}$ is Rieman integrable, then its Riemann integral $\int_a^b f$ is defined by

$$\int_a^b f = L(f, [a, b]) = U(f, [a, b]).$$

:::



We conclude this section with two useful results about the Riemann integral.



:::{prf:theorem} Continuous functions are Riemann integrable

Every continuous function on a closed bounded interval is Riemann integrable.

:::


:::{dropdown} Proof: Continuous functions are Riemann integrable

Suppose $f: [a, b] \to \mathbb{R}$ is a continuous function.
It follows that $f$ is bounded and uniformly continuous on $[a, b].$
Let $\epsilon > 0.$
Because $f$ is uniformly continuous on $[a, b],$ there exists a $\delta > 0$ such that

$$|f(s) - f(t)| < \epsilon \text{ for all } s, t \in [a, b] \text{ with } |s - t| < \delta.$$

Let $n \in \mathbb{N}$ be such that $\frac{b - a}{n} < \delta.$
Let $P$ be the equally spaced partition $a = x_0 < x_1 < \ldots < x_n = b$ of $[a, b]$ with

$$x_j - x_{j-1} = \frac{b - a}{n}$$

for $j = 1, \ldots, n.$
Then, we have

$$\begin{align}
U(f, [a, b]) - L(f, [a, b]) &\leq U(f, P, [a, b]) - L(f, P, [a, b]) \\
&= \frac{b - a}{n} \sum_{j=1}^n \left( \sup_{x \in [x_{j-1}, x_j]} f - \inf_{x \in [x_{j-1}, x_j]} f \right) \\
&= (b - a) \epsilon,
\end{align}$$

where the first inequality follows from the definition of the upper and lower Riemann integral, the second equality follows from our definition of the uniform partition $P,$ and the last equality follows from the uniform continuity of $f.$
Since this holds for any $\epsilon > 0,$ we have $U(f, [a, b]) = L(f, [a, b])$ and so $f$ is Riemann integrable.

:::



The last result in this section concerns a frequently used estimate for the Riemann integral of a function.

:::{prf:theorem} Bounds on the Riemann integral
:label: mira-bounds-on-riemann-integral

Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Then

$$(b - a) \inf_{x \in [a, b]} f \leq \int_a^b f \leq (b - a) \sup_{x \in [a, b]} f.$$

:::

:::{dropdown} Proof: Bounds on the Riemann integral

Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable.
Let $P$ be the partition $a = x_0 \leq x_1 = b$ of $[a, b].$
Then, we have

$$(b - a) \inf_{x \in [a, b]} f = L(f, P, [a, b]) \leq \int_a^b f.$$

Similarly, we have

$$\int_a^b f \leq U(f, P, [a, b]) = (b - a) \sup_{x \in [a, b]} f.$$

:::




## Deficiencies of the Riemann integral

While the Riemann integral is sufficient for a range of use cases, it has a number of deficiencies.
These include the following three issues:

- Riemann integration does not handle functions with many discontinuities.
While functions with a finite number of discontinuities are Riemann integrable, functions with an infinite number of discontinuities need not be.
- Riemann integration does not handle bounded functions.
While the Riemann integral can be extended to handle some unbounded functions by taking limits of the integral endpoints, this does not work well for certain functions.
- Riemann integration does not work well with limits.
In particular, the limit of a sequence of Riemann integrable functions need not be Riemann integrable, and even if it is, the integral of the limit need not be the limit of the integrals.

The next four examples illustrate these issues.
The first is an example of a bounded function which is not Riemann integrable.

::::{prf:example} A function that is not Riemann integrable
:label: mira-eg-not-riemann-integrable

The function $f: [0, 1] \to \mathbb{R}$ defined by

$$f(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q}, \\ 0 & \text{if } x \in \mathbb{R} \setminus \mathbb{Q}, \end{cases}$$

is not Riemann integrable.

:::{dropdown} Proof: A function that is not Riemann integrable

Suppose $P$ is a partition $x_0, \ldots, x_n$ of $[0, 1].$
Then, we have

$$U(f, P, [0, 1]) = \sum_{i=1}^n (x_i - x_{i-1}) \sup_{x \in [x_{i-1}, x_i]} f = \sum_{i=1}^n (x_i - x_{i-1}) = 1.$$

On the other hand, we have

$$L(f, P, [0, 1]) = \sum_{i=1}^n (x_i - x_{i-1}) \inf_{x \in [x_{i-1}, x_i]} f = \sum_{i=1}^n 0 = 0.$$

Since this holds for any partition $P$ of $[0, 1],$ we have $U(f, [0, 1]) = 1$ and $L(f, [0, 1]) = 0.$
Therefore, $f$ is not Riemann integrable.

:::

::::




As we saw, the function $f$ in the previous example is bounded, but not Riemann integrable.
Further, the Riemann integral does not work for functions which are unbounded, as shown by the next example.

::::{prf:example} Riemann integration does not work with unbounded functions

The function $f: [0, 1] \to \mathbb{R}$ defined by

$$f(x) = \begin{cases} \frac{1}{\sqrt{x}} & \text{if } x \in (0, 1], \\ 0 & \text{if } x = 0, \end{cases}$$

would give $U(f, [0, 1]) = \infty$ for every partition $P$ of $[0, 1].$
A standard way to handle unbounded functions with the Riemann integral is to take limits of the integral endpoints.
For example, for this particular function, we could define

$$\int_0^1 f \stackrel{\text{def}}{=} \lim_{a \downarrow 0} \int_a^1 f,$$

where the limit $a \downarrow 0$ means that $a$ approaches $0$ from above.
Then, we would have

$$\int_0^1 f = \lim_{a \downarrow 0} \int_a^1 f = \lim_{a \downarrow 0} \left( 2 - 2\sqrt{a}\right) = 2.$$

::::


However, as the next example shows, the above approach does not always work.


::::{prf:example} Riemann integration does not work with limits

Let $r_1, r_2, \ldots$ be a sequence which includes all the rational numbers in $(0, 1)$ exactly once and that includes no other numbers.
Define the functions $f_n: [0, 1] \to \mathbb{R}$ as

$$f_n(x) = \begin{cases} \frac{1}{\sqrt{x - r_n}} & \text{if } x \in \left(r_k, 1\right], \\ 0 & \text{if } x \in [0, r_n], \end{cases}$$

and let $f: [0, 1] \to \mathbb{R}$ be the function defined by

$$f(x) = \sum_{n=1}^\infty \frac{f_n(x)}{2^n}.$$

While each of the functions above has area less than $2,$ looking at the expression that defines $f,$ we would expect the area under the curve of $f$ to be less than $2.$
However, $f$ is not Riemann integrable, and further, it is not handled by the approach we outlined in the previous example.
That is because every nonempty open subinterval of $[0, 1]$ contains at least one rational number, so $f$ is unbounded on every such subinterval.

::::



Lastly, Riemann integration does not work well with pointwise limits of functions, as shown by the next example.


::::{prf:example} Riemann integration does not work with pointwise limits

Let $r_1, r_2, \ldots$ be a sequence which includes all the rational numbers in $(0, 1)$ exactly once and that includes no other numbers.
Define the functions $f_n: [0, 1] \to \mathbb{R}$ as

$$f_n(x) = \begin{cases} 1 & \text{if } x \in \{r_1, \dots, r_n\}, \\ 0 & \text{otherwise}, \end{cases}$$

and define $f: [0, 1] \to \mathbb{R}$ as

$$f(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q}, \\ 0 & \text{otherwise}. \end{cases}$$

Each $f_n$ is Riemann integrable and $f_n(x) \to f(x)$ for all $x \in [0, 1],$ but $f$ is not Riemann integrable -- this was shown in {prf:ref}`the first example <mira-eg-not-riemann-integrable>` in this section.

::::




In general, because analysis is concerned with results about limits, we would like to be able to exchange the order of limits and integrals.
While, as shown above, we cannot do this with the Riemann integral in general, it is possible if the limit function exists and is Riemann integrable.

:::{prf:theorem} Interchanging Riemann integral and limit

Suppose $a, b, M \in \mathbb{R}$ with $a < b.$
Suppose $f_1, f_2, \dots$ is a sequence of Riemann integrable functions on $[a, b]$ such that

$$|f_n(x)| \leq M,$$

for all $k \in \mathbb{N}$ and $x \in [a, b].$
Suppose $\lim_{n \to \infty} f_n(x)$ exists for each $x \in [a, b].$
Define $f: [a, b] \to \mathbb{R}$ as

$$f(x) = \lim_{n \to \infty} f_n(x).$$

If $f$ is Riemann integrable on $[a, b],$ then

$$\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.$$
:::

We do not provide a proof for this result here.
However, we note that this result suffers from the issue that the limit function $f$ is required to be Riemann integrable.
Ideally, given a good definition of integrals, we would like this to follow directly from the other assumptions in this theorem.
The measure theoretic definition of the integral, which is developed in the next sections, yields an exchange theorem which does not suffer from this issue.
