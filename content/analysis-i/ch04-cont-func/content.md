# Continuous functions

<div class="definition">

**Definition (Continuous function)** A function $f$ is continuous at $x_0$ if for any $\epsilon > 0$, there exists $\delta > 0$ such that
    
$$ |x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon. $$
    
</div>
<br>

<div class="lemma">

**Lemma (Sufficient and necessary condition for continuity)** The following two statements are equivalent
    
1. $f$ is continuous.
2. If $a_n \to a$ is a sequence in $\mathbb{R}$, then $f(a_n) \to f(a)$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Continuity \(\iff\) convergence of map of convergent sequence</summary>

**Proving (1) implies (2):** Suppose $f$ is continuous and $a_n \to a$ is a sequence in $\mathbb{R}$, and let $\epsilon > 0$. Since $f$ is continuous, we can find $\delta > 0$ such that
    
$$ |x - a| < \delta \implies |f(x) - f(a)| < \epsilon. $$
    
Since $a_n \to a$, we can find $N$ large enough such that
    
$$ n > N \implies |a_n - a| < \delta \implies |f(a_n) - f(a)| < \epsilon, $$
    
arriving at the result.
    
**Proving (2) implies (1):** Suppose $f$ is a function such that for any convergent sequence, $a_n \to a$, in $\mathbb{R}$ we have
    
$$ f(a_n) \to f(a). $$
    
We will argue the other way, assuming $f$ is not continuous and arriving at a contradiction. Suppose that $f$ is not continuous. Then there exist $x_0, \epsilon$ such that for any $\delta$, there exists some $x_\delta$ such that
    
$$ |x_\delta - x_0| < \delta \text{ and } |f(x_\delta) - f(x_0)| \geq \epsilon. $$
    
Now consider a sequence of such $\delta$'s, setting $\delta_n = \frac{1}{n}$. For each $\delta_n$ there exists a corresponding $x_{\delta_n}$ that satisfies the above relation. But then the sequence $x_{\delta_n}$ satisfies
    
$$ x_{\delta_n} \to x_0 \text{ and } |f(x_{\delta_n}) - f(x_0)| \geq \epsilon, $$
    
which directly contradicts our assumption that $f(a_n) \to f(a)$ for any convergent sequence $a_n$. Therefore $f$ must be continuous.

    
</details>
<br>


<div class="lemma">

**Lemma (Operations that preserve continuity)** Let $A \subseteq \mathbb{R}$ and $f, g : A \to \mathbb{R}$ be continuous functions. Then
    
1. $f + g$ is continuous.
2. $fg$ is continuous.
3. If $g \neq 0$, then $f/g$ is continuous.
    
</div>
<br>

<details class="proof">
<summary>Proof: Operations that preserve continuity</summary>
    
For all following parts, suppose that $f$ and $g$ are continuous functions.
    
**Proving (1):** For any $x_0, \epsilon$ we can find $\delta$ such that
    
$$ |x - x_0| < \delta \implies |f(x) - f(x_0)| < \frac{\epsilon}{2} \text{ and } |g(x) - g(x_0)| < \frac{\epsilon}{2}. $$
    
By the triangle inequality we have
    
$$ |f(x) + g(x) - f(x_0) - g(x_0)| \leq |f(x) - f(x_0)| + |g(x) - g(x_0)| < \epsilon, $$
    
arriving at the result.
    
**Proving (2)** For given $x_0, \lambda$ we can find $\delta > 0$ such that
    
$$ |x - x_0| < \delta \implies |f(x) - f(x_0)| < \lambda \text{ and } |g(x) - g(x_0)| < \lambda. $$
    
Therefore we can write
    
$$ \begin{align}
|f(x)g(x) - f(x_0)g(x_0)| &= |(f(x) - f(x_0)) (g(x) - g(x_0)) + \\
                          &~~~~~~~ + f(x_0)(g(x) - g(x_0)) + (f(x) - f(x_0))g(x_0)| \\
                          &\leq \lambda^2 + \lambda |f(x_0)| + \lambda |g(x_0)|.
\end{align}$$
    
Let $\epsilon > 0$. Since $\lambda > 0$ can be made arbitrarily small, the right-hand side above can also be made arbitrarily small, by chosing an appropriately small $\delta > 0$. For such a $\delta$ then
    
$$ \begin{align}
|x - x_0| < \delta \implies |f(x)g(x) - f(x_0)g(x_0)| \leq \epsilon,
\end{align}$$
    
arriving at the result.
    
**Proving (3)** Suppose $g$ is a continuous, non-zero function. Since $g$ is continuous, for any $x_0$ and $\lambda > 0$ we can find $\delta$ such that
    
$$ |x - x_0| < \delta \implies |g(x) - g(x_0)| < \lambda g(x_0)^2. $$
    
Then we have
    
$$\begin{align}
\left|\frac{1}{g(x)} - \frac{1}{g(x_0)}\right| = \left|\frac{g(x) - g(x_0)}{g(x)g(x_0)} \right| = \frac{|g(x) - g(x_0)|}{|g(x)g(x_0)|} < \lambda \frac{|g(x_0)|}{|g(x)|} \leq \lambda \frac{|g(x_0)|}{|g(x_0)| - \lambda}.
\end{align}$$
    
In particular, we can choose $\delta > 0$ such that the right-side of the above is smaller than any $\epsilon > 0$ arriving at
    
$$\begin{align}
\left|\frac{1}{g(x)} - \frac{1}{g(x_0)}\right| < \epsilon.
\end{align}$$
    
A similar argument holds when $g(x_0) < 0$ Therefore, if $g$ is a continuous non-zero function, its reciprocal is also a continuous non-zero function. By statement (2) proved earlier, $\frac{f}{g}$ is also a continuous function.
    
    
</details>
<br>


<div class="lemma">

**Lemma (Composition preserves continuity)** Let $A, B \subseteq \mathbb{R}$ and $f : B \to \mathbb{R}, g : A \to B$ be continuous functions. Then $f \circ g$ is also continuous.
    
</div>
<br>

<details class="proof">
<summary>Proof: Composition preserves continuity</summary>
    
Since $f$ and $g$ are continuous, for any $x_0, \epsilon$ we can find $\delta, \lambda > 0$ such that
    
$$\begin{align}
|x - x_0| < \delta &\implies |g(x) - g(x_0)| < \lambda \\
|u - g(x_0)| < \lambda &\implies |f(u) - f(g(x_0))| < \epsilon.
\end{align}$$
    
Combining these two expressions we arrive at the result
    
$$\begin{align}
|x - x_0| < \delta &\implies |f(u) - f(g(x_0))| < \epsilon.
\end{align}$$

    
</details>
<br>


<div class="theorem">

**Theorem (Maximum value theorem)** Let $[a, b]$ be a closed interval in $\mathbb{R}$ amd $f : [a, b] \to \mathbb{R}$ be continuous. Then $f$ is bounded and attains its bounds.
    
</div>
<br>

<details class="proof">
<summary>Proof: Maximum value theorem</summary>

    
</details>
<br>


<div class="theorem">

**Theorem (Intermediate value theorem)** Let $[a, b]$ be a closed interval in $\mathbb{R}$ amd $f : [a, b] \to \mathbb{R}$ be continuous. Suppose that $f(a) < 0 < f(b)$. Then there exists $x \in (a, b)$ such that $f(x) = 0$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Intermediate value theorem</summary>

    
</details>
<br>



<div class="lemma">

**Lemma (Sufficient condition for inverse)** Let $f : [a, b] \to [c, d]$ be a continuous strictly increasing function with $f(a) = c, f(b) = d$. Then $f$ is invertible and its inverse is continuous.
    
</div>
<br>

<details class="proof">
<summary>Proof: Sufficient condition for inverse</summary>
    

    
</details>
<br>


<div class="lemma">

**Lemma (Continuous induction)** Let $a < b$ and let $A \subseteq [a, b]$ have the following properties
    
1. $a \in A$
2. If $x \in A$ and $x \neq b$ then there exists $y \in A$ such that $x < y$.
3. If there exists $\epsilon > 0$ there exists $y \in A$ such that $y \in (x - \epsilon, x]$, then $x \in A$.

Then $b \in A$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Continuous induction</summary>

Since $A$ is a bounded set, its supremum $s$ is in $[a, b]$. Since $s$ is the supremum of $A$, for any $\epsilon > 0$ the set $(s - \epsilon, s]$ contains an element of $A$, so $s$ is contained in $A$ by property (3) of $A$. Now suppose $s \neq b$. In this case, from property (2) there exists another element $x \in A$ such that $s < x$. Therefore $s$ is not the supremum of $A$ reaching a contradiction. Therefore we must have $s = b$.

    
</details>
<br>