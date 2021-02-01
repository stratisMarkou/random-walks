# Differentiation

## Limits of functions

<div class="definition">

**Definition (Limit of functions)** Let $A \subseteq \mathbb{R}$ and let $f : A \to \mathbb{R}$. We write

$$ \lim_{x \to a} f(x) = \ell $$
    
if for all $\epsilon > 0$, there exists $\delta > 0$ such that for all $x \in A$, such that $0 < |x - a| < \delta$ we have
    
$$|f(x) - \ell| < \epsilon.$$
    
</div>
<br>

<div class="lemma">

**Lemma (Rules for limits of functions)** If $f(x) \to l$ and $g(x) \to m$ as $x \to a$, then $f(x) + g(x) \to l + m$, $f(x)g(x) \to lm$ and also $\frac{f(x)}{g(x)} \to \frac{l}{m}$ if $g$ and $m$ are non-zero.
    
</div>
<br>


<details class="proof">
<summary>Proof: Rules for limits of functions</summary>
    
In all following parts we assume $f(x) \to l$ and $g(x) \to m$ as $x \to a$.

**Proof for sums:** In general, it holds that
    
$$|(f(x) + g(x)) - (l + m)| \leq |f(x) - l| + |g(x) - m|.$$
    
Since $f, g$ have limits $l, m$, there exists for any $\epsilon > 0$ some $\delta > 0$ such that both terms of the right-hand side are less than $\frac{\epsilon}{2}$ for all $0 < |x - a| < \delta$. This means that for any $\epsilon > 0$
    
$$|(f(x) + g(x)) - (l + m)| \leq |f(x) - l| + |g(x) - m| < \epsilon, $$
    
arriving at  the result
    
**Proof for products:** In general, it holds that
    
$$|f(x)g(x) - lm| = |(f(x) - l)(g(x) - m) + (lg(x) - lm) + (mf(x) - lm)|.$$
    
Since $f, g$ have limits $l, m$, we can find $\lambda > 0$ such that
    
$$ 0 < |x - a| < \delta \implies |f(x) - l| < \lambda \text{ and } |g(x) - m| < \lambda. $$
    
Therefore we can write
    
$$|f(x)g(x) - lm| < \lambda^2 + l\lambda + m\lambda,$$
    
and since $\lambda$ can be made arbitrarily small, the right hand side above can be made arbitrarily small, smaller than any required $\epsilon > 0$. Thus we conclude
    
$$ 0 < |x - a| < \delta \implies |f(x)g(x) - lm| < \epsilon, $$
    
arriving at the result.
    
**Proof for quotients:** For this part we also assume $m$ is non-zero and $g(x)$ is also non-zero (for any argument $x$). Since $g$ has limit $l$, then for any $\lambda > 0$ we can find $\delta > 0$ such that
    
$$ 0 < |x - a| < \delta \implies |g(x) - l| < \lambda l^2. $$
    
We also have the inequality
    
$$\begin{align}
\left|\frac{1}{g(x)} - \frac{1}{l}\right| = \left|\frac{g(x) - l}{g(x)l} \right| = \frac{|g(x) - l|}{|g(x)l|} < \lambda \frac{|l|}{|g(x)|} \leq \lambda \frac{|l|}{|l| - \lambda},
\end{align}$$
    
and the right-hand side of this inequality can be made arbitrarily small by choosing a sufficiently small $\lambda$. Therefore
    
$$ \frac{1}{g(x)} \to \frac{1}{l} \text{ as } x \to a. $$
    
Using the previous result on products, with the functions $f$ and $\frac{1}{g}$, we arrive at the result.
    
</details>
<br>

(analysis-i-derivative)=
## The derivative

<div class="definition">

**Definition (Differentiable function)** We say that $f$ is differentiable at $x_0$ with a derivative $f'$ if
    
$$ \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = f', $$
    
or equivalently if
    
$$ \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = f'. $$
    
</div>
<br>

<div class="definition">

**Definition (Small oh notation)** We write $o(h)$ for a function that satisfies
    
$$ \frac{o(h)}{h} \to 0 \text{ as } h \to 0. $$
    
</div>
<br>

<div class="lemma">

**Lemma (Equivalent definition of the derivative)** An equivalent definition for the derivative $f'$ of a function $f$ is
    
$$ f(x_0 + h) = f(x_0) + h f'(x_0) + o(h). $$
    
In particular, this equality holds if and only if $f$ is differentiable at $x_0$ with derivative $f'(x_0)$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Equivalent definition of the derivative</summary>
    
Suppose that $f$ is a function that is differentiable at $x_0$ with a derivative $f'$. Then
    
$$\frac{f(x_0 + h) - f(x_0)}{h} \to f'(x_0) $$
    
as $h \to 0$. Rearranging we obtain
    
$$ f(x_0 + h) \to f(x_0) + hf'(x_0). $$
    
Writing $g(h) = f(x_0 + h) - (f(x_0) + hf'(x_0))$ we have
    
$$ f(x_0 + h) \to f(x_0) + hf'(x_0) + g(h), $$
    
and since $\frac{g(h)}{h} \to 0$ as $h \to 0$, it follows that $g(h) = o(h)$, arriving at the result.
    
Going the other way, suppose 
    
$$ f(x_0 + h) = f(x_0) + h f'(x_0) + o(h). $$
    
Rearranging and taking a limit we arrive at
    
$$ f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0) - o(h)}{h} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}. $$
    
</details>
<br>

<div class="definition">

**Definition (Multiple derivatives)** We say that $f$ is $(n+1)$-times differentiable if it is $n$-times differentiable and its $n^{th}$ derivative $f^{(n)}$ is differentiable.
    
</div>
<br>

<div class="lemma">

**Lemma (Sum and product rule)** Let $f, g$ be differentiable at $x$. Then $f+g$ and $fg$ are differentiable at $x$ with
    
$$\begin{align}
(f + g)'(x) = f'(x) + g'(x), \\
(fg)'(x) = f'(x)g(x) + f(x)g'(x).
\end{align}$$
    
</div>
<br>

<details class="proof">
<summary>Proof: Sum and product rule</summary>
    
In both following parts assume the functions $f, g$ are differentiable at $x$.
    
**Proof of sum rule:** The result follows from
    
$$\begin{align}
\lim_{\epsilon \to 0} \frac{(f(x + \epsilon) + g(x + \epsilon)) - (f(x) + g(x))}{\epsilon} &= \lim_{\epsilon \to 0} \left[\frac{f(x + \epsilon) - f(x)}{\epsilon} + \frac{g(x + \epsilon) - g(x)}{\epsilon} \right] \\
&= f'(x) + g'(x).
\end{align}$$

**Proof of product rule:** Similarly, the result follows from
    
$$\begin{align}
\lim_{\epsilon \to 0} &\frac{f(x + \epsilon)g(x + \epsilon) - f(x)g(x)}{\epsilon} = \\
&= \lim_{\epsilon \to 0} \frac{f(x + \epsilon)g(x + \epsilon) - f(x)g(x + \epsilon) + f(x)g(x + \epsilon) - f(x)g(x)}{\epsilon} \\
&= \lim_{\epsilon \to 0} g(x + \epsilon) \frac{f(x + \epsilon) - f(x)}{\epsilon} + f(x)\frac{g(x + \epsilon) - g(x)}{\epsilon} \\
&= f'(x)g(x) + f(x)g'(x).
\end{align}$$
    
</details>
<br>


<div class="lemma">

**Lemma (Chain rule)** If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then $f \circ g$ is differentaible at $x$ with derivative $f'(g(x))g'(x)$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Chain rule</summary>
    
Suppose $f, g$ are functions such that $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$. Using the {ref}`equivalent definition of the derivative<analysis-i-derivative>` we have
    
$$\begin{align}
\lim_{\epsilon \to 0} \frac{f(g(x + \epsilon)) - f(g(x))}{\epsilon} &= \lim_{\epsilon \to 0} \frac{f(g(x) + \epsilon g'(x) + o(\epsilon)) - f(g(x))}{\epsilon} \\
&= \lim_{\epsilon \to 0} \frac{f(g(x) + \epsilon g'(x) + o(\epsilon)) - f(g(x))}{\epsilon} \\
&= \lim_{\epsilon \to 0} \frac{f(g(x)) + f'(g(x) + \epsilon g'(x) + o(\epsilon)) + o(\epsilon) - f(g(x))}{\epsilon} \\
&= f'(g(x)).
\end{align}$$
    
</details>
<br>

<div class="lemma">

**Lemma (Quotient rule)** Let $f, g$ be differentiable at $x$ and $g(x) \neq 0$. Then $\frac{f}{g}$ is differentiable at $x$ with derivative
    
$$ \left(\frac{f}{g}\right)^{-1} = \frac{f'(x)g(x) - f(x)g'(x)}{g^2(x)}. $$
    
</div>
<br>

<details class="proof">
<summary>Proof: Quotient rule</summary>
    
Suppose $f, g$ are functions such that $g$ is differentiable at $x$ and that $g(x) \neq 0$. Noting that $\frac{1}{x}$ is differentiable everywhere except $x = 0$, we can define $h(x) = g(x)^{-1}$ apply the chain rule to obtain
    
$$\begin{align}
h'(x) = - \frac{g'(x)}{g(x)^2},
\end{align}$$
    
and then apply the product role to obtain
    
$$ \left(\frac{f}{g}\right)^{-1} = \frac{f'(x)g(x) - f(x)g'(x)}{g^2(x)}. $$
    
</details>
<br>

<div class="lemma">

**Lemma (Differentiability $\implies$ continuity)** If $f$ is differentiable at $x_0$, then it is also continuous at $x_0$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Differentiability \(\implies\) continuity</summary>
    
Suppose that $f$ is differentiable at $x_0$. We have
    
$$ \frac{f(x_0 + h) - f(x_0)}{h} = \frac{hf'(x_0) + o(h)}{h} = f'(x_0) + \frac{o(h)}{h}. $$
    
Since $\frac{o(h)}{h} \to 0$ as $h \to 0$, the left hand side also goes to $0$ as $h \to 0$. Taking absolute values and multiplying both sides by the function $|h|$ and taking the limit $h \to 0$ we see that
    
$$ |f(x_0 + h) - f(x_0)| \to 0 $$
    
as $h \to 0$. Therefore, by the definition of limits of functions, for any $\epsilon > 0$ we can find a $\delta > 0$ such that 
    
$$ 0 < |h| < \delta \implies |f(x_0 + h) - f(x_0)| < \epsilon, $$
    
arriving at the result.
    
</details>
<br>


## Theorems involving derivatives

### Derivative of an inverse


<div class="theorem">

**Theorem (Inverse functions and their derivatives)** Let $f : [a, b] \to [c, d]$ be differentiable on $(a, b)$, continuous on $[a, b]$ and strictly increasing. Suppose that $f(a) = c, f(b) = d$. Then $f$ has an inverse $g$ and for each $y \in (c, d)$, $g$ is differentiable at $y$ with derivative $\frac{1}{f'(g(y))}$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Inverse functions and their derivatives</summary>

The inverse of $f$ exists by a {ref}`sufficient condition<analysis-i-inv>` on inverses that we proved earlier.  Let $y \in (c, d)$ and $x = g(y)$. Then letting $g(y + \epsilon) = x + \delta$ we obtain
    
$$ \frac{g(y + \epsilon) - g(y)}{\epsilon} = \frac{x + \delta - x}{f(x + \delta) - f(x)}. $$
    
Since $g$ {ref}`is continuous<analysis-i-inv>`, it follows that $g(y + \epsilon) \to g(y)$ as $\epsilon \to 0$, so $\delta \to 0$ in the same limit as well. Therefore
    
$$ \lim_{\epsilon \to 0} \frac{g(y + \epsilon) - g(y)}{\epsilon} = \lim_{\delta \to 0} \frac{x + \delta - x}{f(x + \delta) - f(x)} = \frac{1}{f'(y)} = \frac{1}{f'(g(x))}, $$
    
arriving at the result.
    
</details>
<br>


    
(analysis-i-rolle)=
### Rolle's theorem


<div class="theorem">

**Theorem (Rolle's theorem)** Let $f$ be continuous on a closed interval $[a, b]$ and differentiable on $(a, b)$. Suppose that $f(a) = f(b)$. Then, there exists $x \in (a, b)$ such that $f'(x) = 0$.

</div>
<br>

<details class="proof">
<summary>Proof: Rolle's theorem</summary>
    
If $f$ is constant, then the result follows immediately. Assume $f$ is not constant. Since $f$ is continuous in $[a, b]$, it attains a maximal (or minimal) value in the interval $(a, b)$ which is strictly larger (or smaller) than $f(a) = f(b)$ - this must hold because otherwise $f$ is constant. Assume, wlog, that $f$ attains a maximum value at $x \in (a, b)$. Since $f(x)$ is a maximal value, we must have
    
$$\begin{align}
\leq f(x + \epsilon) - f(x) \leq 0 \geq f(x) - f(x - \epsilon)
\end{align}$$
    
and since the limits of both sides as $\epsilon \to 0$ must both be equal to $f'(x)$, we arrive at $f'(x) = 0$.
    
</details>
<br>

<div class="theorem">

**Theorem (Higher-order Rolle's)** Let $f$ be continuous on $[a, b]$ and $n$-times differentiable on an open interval containing $[a, b]$, such that
    
$$ f(a) = f^{(1)}(a) = f^{(2)}(a) = ... = f^{(n-1)}(a) = f(b) = 0. $$
    
Then, there exists $x \in (a, b)$ such that $f^{(n)}(x) = 0$.

</div>
<br>
    
<details class="proof">
<summary>Proof: Higher-order Rolle's theorem</summary>
    
Let $f$ be defined as in the theorem. We can apply Rolle's theorem to $f$ to show that there exists $b_1 \in (a, b)$ such that $f^{(1)}(b_1)$. We can proceed recursively, applying Rolle's theorem at each step to see that there exists $b_{k+1} \in (a, b_k)$ such that $f^{(k+1)}(b_{k+1})$. Continuing to order $n$ we arrive at the result.
    
</details>
<br>
    
    

<div class="lemma">

**Corollary (Rolle's for two functions)** Suppose that $f$ and $g$ are both differentiable on an open interval containing $[a, b]$ and that $f^{(k)}(a) = g^{(k)}(a)$ for $k = 0, 1, ..., n - 1,$ and also $f(b) = g(b)$. Then there exists $x \in (a, b)$ such that $f^{(n)}(b) = g^{(n)}(b)$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Rolle's for two functions</summary>
    
We can define $h(x) = f(x) - g(x)$ and apply Higher-order Rolle's to find $x \in (a, b)$ such that
    
$$h^{(n)}(x) = 0 \implies f^{(n)}(x) = g^{(n)}(x), $$
    
arriving at the result.
    
</details>
<br>


### Mean value theorem

<div class="theorem">

**Theorem (Mean value theorem)** Let $f$ be continuous on a closed interval $[a, b]$ and differentiable onn $(a, b)$. Suppose that $f(a) = f(b)$. Then, there exists $x \in [a, b]$ such that
    
$$ f'(x) = \frac{f(b) - f(a)}{b - a}. $$

</div>
<br>
    
<details class="proof">
<summary>Proof: Mean value theorem</summary>
    
We can prove quickly prove the mean value theorem using {ref}`Rolle's theorem<analysis-i-rolle>`. Define the linear function
    
$$ g(x) = \frac{f(b) - f(a)}{b - a} x, $$
    
and observe that the function $h(x) = f(x) - g(x)$ satisfies $h(a) = h(b)$. Therefore by {ref}`Rolle's theorem<analysis-i-rolle>` there exists $x \in (a, b)$ such that

$$ h'(x) = f'(x) - g'(x) = 0 \implies f'(x) =  \frac{f(b) - f(a)}{b - a}, $$
    
arriving at the result.
    
</details>
<br>

### Local inverse theorem

<div class="theorem">

**Theorem (Local inverse theorem)** Let $f$ be a function with continuous derivative on $(a, b)$. Let $x \in (a, b)$ and suppose that $f'(x) \neq 0$. Then there exists an open interval containing $x$ on which $f$ is invertible. Moreover, if $g$ is the inverse, then
    
$$g'(f(z)) = \frac{1}{f'(z)}$$
    
for every $x$ in the open interval.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Local inverse theorem</summary>

Suppose wlog that $f'(x) \neq 0$. Consider the interval $[x - \delta, x + \delta]$. Since $f'$ is continuous, it must be the case that
    
$$ \delta_{\max} \equiv \max_{\delta} \{\delta : z \in [x - \delta, x + \delta] \implies f'(z) > 0\} > 0. $$
    
If this were not the case, we would always be able to find a $z$ arbitrarily close to $x$ such that $f'(z) \leq 0$ which would contradict the assumption that $f'$ is continuous. Therefore, $f' > 0$ in the interval
    
$$A = [x - \delta_{\max}, x + \delta_{\max}].$$
    
The result follows by applying the theorem on inverse functions proved earlier, to $f$ constrained in the interval $A$, and considering that
    
$$ g(f(z)) = z \implies g'(f(z)) f'(z) = 1, $$
    
by an application of the chain rule.
    
</details>
<br>

### Taylor's theorem

<div class="theorem">

**Theorem (Taylor's theorem)** Let $f$ be an $n$-times differentiable function. Then for any $x_0$ and $h > 0$ we can find $x \in (x_0, x_0 + h)$ such that

$$ f(x_0 + h) = f(x_0) + hf'(x_0) + ... + \frac{h^{n-1}}{(n - 1)!} f^{(n-1)}(x_0) + \frac{h^n}{n!} f^{(n)}(x). $$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Taylor's theorem</summary>

Consider the polynomial
    
$$ Q(x_0 + h) = \sum_{n = 0}^{N-1} \frac{(x_0 + h)^n}{n!} f^{(n)}(x_0), $$
    
observing that $Q^{(k)}(x_0) = f^{(k)}(x_0)$ for $k = 0, 1, ..., N-1$. Now add another $N$-order term to $Q$, to obtain another polynomial $P$ such that $P(x_0 + h) = f(x_0 + h)$, namely
    
$$ P(x) = Q(x) + \frac{(x - x_0)^N}{h^N} (f(x_0 + h) - Q(x_0 + h)). $$
    
The polynomial $P$ therefore satisfies $P^{(k)}(x_0) = f^{(k)}(x_0)$ for $k = 0, 1, ..., n - 1,$ and also $P(x_0 + h) = f(x_0 + h)$. From the earlier {ref}`lemma on Rolle's for two functions<analysis-i-rolle>` there exists $x \in (x_0, x_0 + h)$ such that $P(h) = f(x_0 + h)$, arriving at the result.
    
</details>
<br>


## Complex derivatives

<div class="definition">

**Definition (Complex derivative)** Let $f : \mathbb{C} \to \mathbb{C}$. Then $f$ is differentiable at $x$ with derivative $f'(z)$ if

$$ \lim_{h \to 0} \frac{f(x_0 + h) - f(z)}{h} \text{ exists and equals } f'(z), $$

or equivalently

$$ f(x_0 + h) = f(x_0) + hf'(x_0) + o(h). $$
    
</div>
<br>