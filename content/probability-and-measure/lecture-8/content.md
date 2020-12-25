# The Lebesgue integral

## Simple functions
    
<div class="definition">
    
**Notation (Integral)** For $(E, \mathcal{E}, \mu)$ a measurable space and $f$ a measurable function on $E$, we denote its integral as
    
$$\mu(f) = \int_E f d\mu = \int_E f(x) d\mu(x) = \int f(x) \mu(dx)$$

whenever $f \geq 0$ or whenever $f$ is integrable. Equally, we will define the expectation of random variables $X$ as
    
$$ \mathbb{E}(x) = \int_\Omega X d\mathbb{P} = \int_\Omega X(\omega) d\mathbb{P}(\omega) = \int_\Omega X(\omega) \mathbb{P}(d\omega).$$
    
</div>
<br>
    
    
<div class="definition">
    
**Definition (Simple functions)** We call a function $f : E \to \mathbb{R}$ simple if it is of the form
    
$$ f = \sum^K_{k = 1} a_k \mathbb{1}_{A_k}, $$
    
where $a_k \geq 0$, $A_k \in \mathcal{E}$. For such $f$ we set its integral to be
    
$$ \mu(f) = \sum^K_{k = 1} a_k \mu(A_k), $$
    
where $\mu$ is the Lebesgue measure.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Properties of Lebesgue integrals of simple functions)** We have the following properties of the Lebesgue integral
    
1. $\mu(\alpha f + \beta g) = \alpha \mu(f) + \beta \mu(g)$,
2. $f \leq g \implies \mu(f) \leq \mu(g)$,
3. $f = 0$ almost everywhere $\implies \mu(f) = 0$.
    
where $f, g$ are simple functions and $\alpha, \beta \in \mathbb{R}$.

</div>
<br>
    
## Lebesgue integral
    
<div class="definition">
    
**Definition (Lebesgue integral for general functions)** For a general measurable non-negative $f : E \to [0, \infty]$ we define the Lebesgue integral to be
    
$$ \mu(f) = \sup\{\mu(g) : g \text{ simple } g \leq f\}. $$
    
For a general function $f : E \to [-\infty, \infty]$ we define the Lebesgue inetgral to be
    
$$ \mu(f) = \mu(f^+) - \mu(f^-), $$
   
whenever $\mu(|f|) = \mu(f^+ + f^-) < \infty$, where $f^+ = \max\{f, 0\}$ and $f^- = \max\{-f, 0\}$.
    
</div>
<br>
    

(pnm-monotone-conv)=
## Monotone convergence theorem


The monotone convergence theorem is a key result for the theory of integration. It states that if a sequence of (measurable) functions converges to a limiting (measurable) function pointwise and monotonously from below, then the sequence of Lebesgue measures of these functions converges to the Lebesgue measure of the limiting function, monotonously from below. In other words, for a sequence of monotonously pointwise convergent functions, we may interchange limits and measures.
    
<div class="theorem">
    
**Theorem (Monotone convergence theorem)** Let $f_n, f : E \to [0, \infty]$ be measurable functions, such that $f_n \uparrow f$ pointwise. Then $\mu(f_n) \uparrow \mu(f)$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Monotone convergence theorem</summary>

Let $f_n, f : E \to [0, \infty]$ be measurable functions, such that $f_n \uparrow f$ pointwise. Since $f_n(x) \uparrow f(x)$ for all $x$, we have $\mu(f_n) \leq \mu(f)$ and
    
$$ \mu(f_n) \uparrow M \leq \mu(f) \leq \sup_g \{\mu(g) : \text{ simple } g \leq f\}, $$
    
where $M$ is the supremum of $\mu(f_n)$. It remains to show that this supremum is equal to $\mu(f)$. For this, it suffices to show that $\mu(g) \leq M$ for any simple non-negative $g \leq f$. From this, the result follows by taking a supremum over all simple non-negative $g \leq f$ to obtain $\mu(f) \leq M \implies M = \mu(f)$, completing the result.
    
**Showing $\mu(g) \leq M$:** Let $g$ be a non-negative simple function with $g \leq f$. We can write this $g$ as
    
$$ g = \sum_{k = 1}^K a_k \mathbb{1}_{A_k}, $$
    
where without loss of generality, we can take the $A_k$ sets to be disjoint. We can do this because the $A_k$ are assumed to be within some $\sigma$-algebra, so we can always find a family of disjoint events (and corresponding coefficients) which has the same union as the family of the $A_k$ sets, using operations under which the $\sigma$-algebra is closed. Now, let us define the sequence of functions
    
$$ g_n = \min(2^{-n} \lfloor 2^n f_n \rfloor, g). $$

Note that the $g_n$ are all simple functions satisfying $g_n \uparrow g$ pointwise and also $g_n \leq f_n$. Now let $\epsilon \in (0, 1)$ and define the sets
    
$$ A_k(n, \epsilon) = \{x \in A_k : g_n \geq (1 - \epsilon) a_k \}. $$
    
For fixed $\epsilon$, the set $A_k(n, \epsilon)$ is the subset of $A_k$ within which $g_n$ is at least $(1 - \epsilon) g$. This sequence of sets $A_k(n, \epsilon)$ is monotonously increasing in $n$ and has limit $A_k$, so
    
$$A_k(n, \epsilon) \uparrow A_k \implies \mu(A_k(n, \epsilon)) \uparrow \mu(A_k).$$
    
by the countable additivity of measures. We also have
    
$$ g_n \mathbb{1}_{A_k} \geq (1 - \epsilon) a_k \mathbb{1}_{A_k(n, \epsilon)}. $$
    
Last, we can write
    
$$ M \geq \mu(f_n) \geq \mu(g_n) = \mu\left( \sum_{k = 1}^K g_n \mathbb{1}_{A_k} \right) \geq (1 - \epsilon) \sum_{k = 1}^K a_k \mu\left(\mathbb{1}_{A_k(n, \epsilon)} \right) $$
    
where we have used the countable additivity of measures again. The last term converges monotonously from below to $(1 - \epsilon) \mu(g)$ as $n \to \infty$. Therefore, taking limits of the above expression with $n \to \infty$ we obtain
    
$$ M = \lim_{n \to \infty} \mu(f_n) \geq \lim_{n \to \infty} \mu(g_n) \geq (1 - \epsilon) \mu(g). $$
    
But this holds for arbitrarily small $\epsilon$, so it must be that $M \geq \mu(g)$ arriving at the result.
    
**One bit of explanation:** The reason why we brought the $A_k(n, \epsilon)$ sets into the construction is because we cannot directly assume $\lim_{n \to \infty} \mu(g_n) = \mu(g)$. If we could assume relation, the we could directly apply it to the second-to-last equation above, to arrive at the result. Instead we showed that $\lim_{n \to \infty} \mu(g_n) \geq (1 - \epsilon) \mu(g)$ for arbitrarily small $\epsilon$, and one way to achieve this is by introducing these $A_k(n, \epsilon)$ sets.


</details>
<br>


From this we can prove some intuitive properties of the Lebesgue integral for non-negative functions.


<div class="lemma">
    
**Lemma (Properties of the Lebesgue integral - non-negative)** For all non-negative functions $f, g$ and all constants $\alpha, \beta \geq 0$
    
1. $\mu(\alpha f + \beta g) = \alpha \mu(f) + \beta \mu(g),$
2. $f \leq g \implies \mu(f) \leq \mu(g),$
3. $f = 0$ almost everywhere $\iff$ $\mu(f) = 0$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Properties of the Lebesgue integral - non-negative</summary>
    
For the proof of all three parts of this theorem, define the simple functions
    
$$ f_n = \min(2^{-n}\lfloor 2^n f\rfloor, n) \text{ and } g_n = \min(2^{-n}\lfloor 2^n g\rfloor, n), $$
    
where the minimum with $n$ is taken to handle the case where $f$ or $g$ are unbounded.
    
**Part 1:** For simple $f_n, g_n$ we have
    
$$\mu(\alpha f_n + \beta g_n) = \alpha \mu(f_n) + \beta \mu(g_n). $$
    
Taking the limit $n \to \infty$ of both sides and applying the {ref}`monotone convergence theorem<pnm-monotone-conv>` we arrive at
    
$$\begin{align}
\lim_{n \to \infty} \mu(\alpha f_n + \beta g_n) &= \alpha \lim_{n \to \infty} \mu(f_n) + \beta \lim_{n \to \infty}\mu(g_n) \\
\mu(\alpha f + \beta g) &= \alpha \mu(f) + \beta \mu(g)
\end{align}$$

**Part 2:** If $f \leq g$ we have $f_n \leq g_n$ for every $n \in \mathbb{N}$, so taking limits and using the {ref}`monotone convergence theorem<pnm-monotone-conv>` we obtain
    
$$\begin{align}
\lim_{n \to \infty} \mu(f_n) &\leq \lim_{n \to \infty} \mu(g_n), \\
\mu(f) &\leq \mu(g).
\end{align}$$

**Part 3:** If $f = 0$ almost everywhere, then using $0 \leq f_n \leq f$ and applying the {ref}`monotone convergence theorem<pnm-monotone-conv>`
    
$$\begin{align}
& 0 \leq \lim_{n \to \infty} \mu(f_n) \leq \mu(f), \\
\implies &\lim_{n \to \infty} \mu(f_n) = 0.
\end{align}$$
    
Conversely, if $\mu(f) = 0$ then $f$ must be equal to zero almost everywhere. If this were not the case, then there must exist some $\epsilon > 0$ such that $\mu(\{x : f(x) \geq \epsilon\})$ which together with the fact that $f \geq 0$ implies that $\mu(f) \geq 0.$

</details>
<br>
    
    
We can extend the above results to the case of general integrable functions and real constants. Note that the third result does not extend fully, but becomes an implication.
       
<div class="lemma">
    
**Lemma (Properties of the Lebesgue integral - general case)** For all integrable functions $f, g$ and all constants $\alpha, \beta \in \mathbb{R}$
    
1. $\mu(\alpha f + \beta g) = \alpha \mu(f) + \beta \mu(g),$
2. $f \leq g \implies \mu(f) \leq \mu(g),$
3. $f = 0$ almost everywhere $\implies$ $\mu(f) = 0$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Properties of the Lebesgue integral - general case</summary>
    
Suppose $f, g$ are integrable functions, that is measurable functions with $\mu(|f|), \mu(|g|) < \infty$, and $\alpha, \beta \in \mathbb{R}$
    
**Part 1:** Noting that for any positive measurable function $h$ we have $\mu(-h) = - \mu(h)$, so we can freely move negative signs through the integral and similarly for negative coefficients.
    
$$\begin{align}
\mu(\alpha f + \beta g) &= \mu(\alpha (f^+ - f^-) + \beta (g^+ - g^-)) \\
                        &= \alpha \mu(f^+) - \alpha \mu(f^-) + \beta \mu(g^+) - \beta \mu(g^-) \\
                        &= \alpha \mu(f) + \beta \mu(g).
\end{align}$$
    
**Part 2:** If $f \leq g$ we have $g - f \geq 0$ so $\mu(g - f) \geq 0$ and
    
$$ \mu(f) = \mu(g - (g - f)) = \mu(g) - \mu(g - f) \implies \mu(f) \leq \mu(g). $$

</details>
<br>
    
    
<div class="lemma">
    
**Lemma (Partial converse of third result above)** Let $\mathcal{A}$ be a $\pi$-system containing $E$ which generates $\mathcal{E}$. Then for any integrable function $f$
    
$$ \mu(f \mathbb{1}_A) = 0, \text{ for all } A \in \mathcal{A} \implies f = 0 \text{ a.e.}. $$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Partial converse of third result above</summary>
    
Consider the measure $\nu(A) = \mu(f 1_A)$ defined on $\mathcal{A}$. By the {ref}`uniqueness theorem of measures<pnm-uniqueness>`, $\nu(B) = 0$ for all $B \in \mathcal{E}$ is the unique extension of $\nu$ on $\mathcal{E}$. Therefore $\mu(f 1_B) = 0$ for all $B \in \mathcal{E}$ as well, so $f = 0$ almost everywhere.

</details>
<br>
    
    
<div class="lemma">
    
**Lemma (A variant of the monotone convergence theorem)** Let $g_n$ be non-negative measurable functions. Then
    
$$\begin{align}
\sum_{n = 1}^\infty \mu(g_n) = \mu\left( \sum_{n = 1}^\infty g_n \right).
\end{align}$$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: A variant of the monotone convergence theorem</summary>
    
Let $g_n$ be non-negative measurable functions. Define 
    
$$f_n = \sum_{k = 1}^n g_k,$$
    
a sequence of non-negative functions, which converges pointwise to
    
$$f = \sum_{k = 1}^\infty g_k.$$
    
The result follows by the {ref}`monotone convergence theorem<pnm-monotone-conv>`.
    
</details>
<br>
    
