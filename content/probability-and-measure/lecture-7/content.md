# Image measures and random variables

This page presents image measures, generalised inverses and distribution functions. It states and proves the fact that Radon measures on $\mathcal{B}$ can be written in terms of an appropriate function $g$ and conversly that, given such a $g$ one may construct a Radon measure from it. We also define cumulative distribution functions, stating and proving some of their properties.

(pnm-generalised-inv)=
## Image measures

<div class="definition">
    
**Definition (Image measure)** Given measurable spaces $(E, \mathcal{E})$ and $(G, \mathcal{G})$, a measure $\mu$ on $\mathcal{E}$ and a measurable function $f : \mathcal{E} \to \mathcal{G}$, the image measure $\nu : G \to \mathbb{R}$ of $f$ is defined as
    
$$ \nu = \mu \circ f^{-1}, $$
    
where $f^{-1}$ is the pre-image of $f$.
    
</div>
<br>

<div class="definition">
    
**Definition (Generalised inverse of a function on $\mathbb{R}$)** Let $g : \mathbb{R} \to \mathbb{R}$ be non-constant, right-continuous and non-decreasing and let $I = (g(-\infty), g(\infty))$. The map $f : I \to \mathbb{R}$
    
$$ f(y) = \inf \left\{ x \in \mathbb{R} : y \leq g(x) \right\} $$
    
is called the generalised inverse of $g$.
    
</div>
<br>

    
<div class="lemma">

**Lemma (Properties of the generalised inverse)** If $g$ is a non-constant, right-continuous and non-decreasing function, then its generalised inverse $f$ is left-continuous, non-decreasing and satisfies
    
$$ y \leq g(x) \iff f(y) \leq x. $$

</div>
<br>

<details class="proof">
<summary>Proof: Properties of the generalised inverse</summary>

Let $y \in I$ and define the set
    
$$ J_y = \{x : y \leq g(x)\}, $$
    
which is non-empty since $g(-\infty) < y < g(\infty)$ so we can always find some $x$ such that $y \leq g(x)$. Since $J_y$ is non-empty, its infimum is finite and we write
        
$$ f(y) = \inf J_y. $$

If $x \in J_y$ and $x \leq x'$ then $y \leq g(x) \leq g(x')$ because $g$ is increasing, so $x' \in J_y$. Also for any sequence $x_n \in J_y$ such that $x_n \downarrow x$, we have $y \leq g(x)$ by right continuity. This implies $y \leq g(f(y))$ so $f(y) \in J_y = [f(y), \infty)$ and also
    
$$f(y) \leq x \iff y \leq g(x). $$
    
The $\implies$ part of above follows by applying $g$ to either side of $f(y) \leq x$ and the $\impliedby$ part follows by considering that if $y \leq g(x)$, then $J_y = [f(y), \infty)$ contains $x$.
    
Last, since $y' \leq y \implies J_y \subseteq J_{y'} \implies f(y') \leq f(y)$ hence $f$ is increasing. Lastly if $y_n \uparrow y$, then $J_y = \lim_{n \to \infty} \bigcap_n J_{y_n}$ so
    
$$ f(y_n) = \inf J_{y_n} = \inf \bigcap^n_{k = 1} J_{y_k} \to f(y), $$
    
and $f$ is left-continuous.
    
</details>
<br>


<div class="theorem">
    
**Theorem (Existence of Radon measures on $\mathbb{R}$)** Let $g : \mathbb{R} \to \mathbb{R}$ be a non-constant, right-continuous and non-decreasing function. Then there exists a {ref}`Radon measure<pnm-borel-sig-alg>` $\mu_g$ on $\mathcal{B}$ such that
    
$$ \mu_g((a, b]) = g(b) - g(a),$$
    
for all $a < b$ in $\mathbb{R}$. Conversely, any Radon measure on $\mathbb{R}$ can be represented in this way. We call $\mu_g$ the Lebesgue-Stieltjes measure with distribution function $g$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Existence of Radon measures on \(\mathbb{R}\)</summary>

Let $g : \mathbb{R} \to \mathbb{R}$ be a non-constant, right-continuous and non-decreasing function, $I = (g(-\infty), g(\infty))$ and $f$ be the {ref}`generalised inverse<pnm-generalised-inv>` of $g$.
    
For the first part of the proof, we will show that $f$ is $\mathcal{B}(I)$-$\mathcal{B}$ {ref}`measurable{pnm-measurable-func}`. If $(-\infty, x] \in \mathcal{B}$ then
    
$$\begin{align}
f^{-1}((-\infty, x]) &= \{y \in I : f(y) \leq x\} \\
                     &= \{y \in I : y \leq g(x)\} \\
                     &= (g(-\infty), g(x)] \in \mathcal{B}(I).
\end{align}$$

Furthermore, the sets $(-\infty, x]$ generate $\mathcal{B}$, so any $A \in \mathcal{B}$ can be written in terms of $\emptyset$, complements and countable unions these sets. The pre-image $f^{-1}(A)$ can also be written in terms of $\emptyset$, complements and countable unions of the sets $(g(-\infty), x], x \in I$. Therefore, for any $A \in \mathcal{B}$, the pre-image $f^{-1}(A)$ is in $\mathcal{B}(I)$ and $f$ is measurable. Therefore the image measure
    
$$ \mu_g \equiv \mu \circ f^{-1} $$
    
is defined on $\mathcal{B}(\mathbb{R})$. We also have
    
$$\begin{align}
\mu_g((a, b]) &= \mu\left(\{y : f(y) > a, f(y) \leq b\}\right) \\
              &= g(b) - g(a),
\end{align}$$
    
as stated in the theorem, and $\mu_g$ is a Radon measure. By the {ref}`uniqueness theorem<pnm-uniqueness>`  the unique such measure. Conversely, let $\nu$ be any Radon measure and define
    
$$g(x) = \begin{cases} \nu((0, x]) & \text{ for } x \geq 0 \\
                       - \nu((x, 0]) & \text{ otherwise,} \end{cases}$$
    
which is increasing, right-continuous (by the continuity of measures) and satisfies
    
$$ \nu((a, b]) = g(b) - g(a). $$
    
By the {ref}`uniqueness theorem<pnm-uniqueness>`, $\mu_g = \nu$.
    
</details>
<br>
    
    

<div class="definition">
    
**Definition (Random variable)** Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space and $(E, \mathcal{E})$ a measurable space. We call the measurable map
    
$$X : \Omega \to E$$
    
a random variable in $E$. The image measure $\mu_X = \mathbb{P} \circ X^{-1}$ is called the law or distribution of $X$. When $(E, \mathcal{E}) = (\mathbb{R}, \mathcal{B})$, this distribution is determined by the values it takes on the $\pi$-system $\{(-\infty, x] : x \in \mathbb{R}\}$ and
    
$$\begin{align} F_X(x) &= \mu_X((-\infty, x]) \\
                       &= \mathbb{P}(X \leq x)
\end{align}$$
    
is called the cumulative distribution function.
    
</div>
<br>
    
    
<div class="lemma">

**Corrolary (Properties of cdfs on $\mathbb{R}$)** By the continuity of measures, we have
    
1. $\lim_{z \downarrow x} F(z) = F(x)$.
2. $\lim_{z \to \infty} F(z) = \mathbb{P}(\Omega) = 1$.
3. $\lim_{z \to -\infty} F(z) = \mathbb{P}(\emptyset) = 0$.
    
We say that any $F$ with the above properties is a cdf.

</div>
<br>
    
    
## Independence of random variables
    
<div class="definition">
    
**Definition (Independence of random variables)** A countable family $(X_i : i \in I)$ of random variables is independent if the family of $\sigma$-algebras induced by it $(\sigma(X_i) : i \in I)$ is {ref}`independent<pnm-indep-event-alg>`.
    
</div>
<br>
    
    
<div class="observation">
    
**Remark (Independence $\iff$ factorisation)** A family of independent random variables $(X_i : i \in I)$ in $\mathbb{R}$ is independent if and only if
    
$$ \mathbf{P}(X_1 \leq x_1, ..., X_n \leq x_n) = \mathbb{P}(X_1 \leq x_1) ... \mathbb{P}(X_n \leq x_n), $$
    
for all $x_i \in \mathbb{R}$, for all finite selections $X_1, ..., X_n$ of random variables in the family. 
    
</div>
<br>
    
    
## Construction of random variables
    
Here we construct three common random variables, the Rademacher, Bernoulli and Uniform random variables. More specifically, we will construct countably infinite famililies of independent Bernoulli and Uniform random variables.
    

<div class="definition">
    
**Definition (Rademacher random variable)** The Rademacher random variable $R_n : (0, 1) \to \{0, 1\}$ is the mapping
    
$$ R_n(\omega) = \omega_n, \text{ where } \omega = 0.\omega_1\omega_2 ... \omega_n ... $$
    
is the binary expansion of $\omega$ - made unique by prohibiting infinitely many trailing zeroes.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Family of Rademacher variables is Bernoulli)** The countably infinite family of Rademacher random variables $(R_n : n \in \mathbb{N})$ is independent and identically distributed, with
    
$$ \mathbb{P}(R_n = 0) = \mathbb{P}(R_n = 1) = \frac{1}{2}. $$

</div>
<br>
    
    
<div class="lemma">

**Lemma (Construction of uniformly distributed family)** Given a bijection $m : \mathbb{N}^2 \to \mathbb{N}$, the random variable
    
$$ U_n = \sum_{k = 1}^\infty 2^{-k} U_{nk}, \text{ where } U_{nk} = R_{m(n,k)}$$
    
are indepnendent and uniformly distributed on $(0, 1)$.

</div>
<br>
    
    
<div class="observation">

**Remark (Family of cdfs $\implies$ family of independent r.v.s exists)** Let $(F_n : n \in \mathbb{N})$ be any sequence of probability distribution functions on $\mathbb{R}$. Then, there exist independent random variables $(X_n : n \in \mathbb{N})$ defined on $(\Omega, \mathcal{F}, \mathbb{P}) = ((0, 1), \mathcal{B}(0, 1), \mu_{|(0, 1)})$ such that their probability distributions are $F_{X_n} = F_n$ for all $n \in \mathbb{N}$.

</div>
<br>
    

<details class="proof">
<summary>Proof: Family of cdfs \(\implies\) family of independent r.v.s exists</summary>

Let $Y_n \sim U(0, 1)$ be a family of i.i.d. random variables and set
    
$$ X_n = G_n(Y_n) \text{ where } G_n(y) = \inf \{ x : y \leq F_n(x)\}. $$
    
Then by the {ref}`lemma of generalised inverses<pnm-generalised-inv>`, we have
    
$$\begin{align}
\mathbb{P}(X_n \leq x_n) &= \mathbb{P}(G_n(Y_n) \leq x_n) \\
                         &= \mathbb{P}(Y_n \leq F_n(x_n)) \\
                         &= F_n(x_n),
\end{align}$$
    
arriving at the result.
    
</details>
<br>
    
    
## Convergence of random variables
    
    
<div class="definition">
    
**Definition (Almost everywhere properties)** Let $(E, \mathcal{E}, \mu)$ be a measurable space. Then a property defining $A \in \mathcal{E}$ is said to hold almost everywhere if $\mu(A^C) = 0$. When $(E, \mathcal{E}, \mu) = (\Omega, \mathcal{F}, \mathbb{P})$, we say the property holds almost surely.
    
</div>
<br>
    
    
<div class="definition">
    
**Definition (Convergence almost everywhere/always)** A sequence of measurable $f_n : E \to \mathbb{R}$ is said to converge almost everywhere to $f : E \to \mathbb{R}$ if
    
$$ \mu(x \in E : f_n(x) \not \to f(x)) = 0. $$
    
where we note that $f$ need not be measurable. If $\mu$ is a probability measure, we say the sequence converges almost always.
    
</div>
<br>
    
    
<div class="definition">
    
**Definition (Convergence in mesasure/probability)** If $f_n, f : E \to \mathbb{R}$ are measurable maps, we say $f_n$ converges to $f$ in measure/probability if
    
$$\mu(x \in E : |f_n(x) - f(x)| > \epsilon ) \to 0, $$
    
for any $\epsilon > 0$.
    
</div>
<br>
    
    
<div class="definition">
    
**Definition (Convergence in distribution)** For randomm variables $X_n$ on $\mathbb{R}$, we say that $X_n$ converges to $X$ in distribution if the distribution functions
    
$$ F_{X_n}(x) \to F_X(x), $$
    
wherever $F_X$ is continuous.
    
</div>
<br>
    
The reason we restrict the requirement for convergence only to those points where $F_X$ is continuous is because otherwise this definition would be too restrictive. Consider for example{cite}`grimmettprob` the measurable space $(\mathbb{R}, \mathcal{B}, \mathbb{P})$ and sequences of random variables $X_n, Y_n, Z$ such that
    
$$ \mathbb{P}\left(X_n = -\frac{1}{n}\right) = 1, \mathbb{P}\left(Y_n = \frac{1}{n}\right) = 1, \mathbb{P}\left(Z = 0\right) = 1. $$
    
If convergence in distribution required convergence of CDFs everywhere (not just the points where $F_Z$ is continuous), we would have $F_X \to F_Z$ but $F_Y \not \to F_Z$, because the condition would not be met at the point $z = 0$, where $F_Z$ is discontinuous.
    
    
<div class="theorem">
    
**Theorem (Convergence almost everywhere and in probability)** Let $(f_n : n \in \mathbb{N})$ be a sequence of measurable functions on $(E, \mathcal{E}, \mu)$.
    
1. If $\mu(E) < \infty$, then $f_n \to 0$ almost everywhere $\implies f_n \to 0$ in measure.
2. If $f_n \to 0$ in measure, then $f_{n_k} \to 0$ a.e. along a subsequence $n_k$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Convergence almost everywhere and in probability</summary>

**Part 1** Suppose that $f_n \to 0$ almost everywhere and let $\epsilon > 0, n \in \mathbb{N}$. Then we have
    
$$ \{x : f_k(x) \to 0 \text{ as } k \to \infty\} \subseteq \{x : |f_n(x)| \leq \epsilon\}, $$
    
from which it follows that
    
$$ \mu(f_n \to_{n \to \infty} 0) \leq \mu(|f_n| \leq \epsilon), $$
    
and using the fact that $\mu(|f_n| \leq \epsilon) \to \mu(E)$ as $n \to \infty$ we have that

$$ \mu(f_n \to 0) \to \mu(E) \text{ as } n \to \infty, $$
    
arriving at the result.
    
**Part 2** Suppose that $f_n \to 0$ in measure. We can set $\epsilon = \frac{1}{k}$ and choose a sequence $n_k$ such that
   
$$ \mu\left(|f_{n_k}| \geq \frac{1}{k}\right) = \frac{1}{k^2}. $$
    
Then summing these terms we obtain
    
$$ \sum_{k = 1}^\infty \mu(|f_{n_k}| \geq \frac{1}{k}) < \infty, $$
    
so by the {ref}`first Borell-Cantelli lemma<pnm-bcl>` (which also holds not only for probability spaces, but also for general measurable spaces) we have
    
$$ \mu\left(|f_{n_k}| \geq \frac{1}{k} \text{ i.o.}\right) = 0. $$
    
Therefore, it follows that $\mu(f_{n_k} \to 0) = \mu(E)$ because the set for which this condition does not hold is exactly the set for which $|f_{n_k}| \geq \frac{1}{k}$ occurs infinitely often.
    
</details>
<br>
    
    
<div class="observation">

**Remark (On almost everywhere convergence and in measure)** The requirements for each part in the theorem above are necessary. Consider the following counterexamples
    
**Part 1** If $\mu(E) = \infty$, the following counterexample holds. Let $f_n = \mathbb{1}_(n, \infty)$. This sequence converges to $0$ almost everywhere as $n \to \infty$ but
    
$$ \mu(x : |f_n(x)| \geq \epsilon) = \mu((n, \infty)) = \infty. $$ 
    
**Part 2** It must be the case that $f_{n_k}$ converges to $f$ along the subsequence $n_k$ instead of along all integers, because otherwise the following counterexample holds. Take independent events $A_n$ such that
    
$$\mathbb{P}(A_n) = \frac{1}{n}.$$
    
Then by the {ref}`second Borell-Cantelli lemma<pnm-bcl>`, we have 
    
$$ \mathbb{P}(\mathbb{1}_{A_n} = 1 \text{ i.o.}) = 1, \text{ so } \mathbb{1}_{A_n} \not\to 0 \text{ a.s.}, $$
    
In contrast $\mathbb{P}(\mathbb{1}_{A_n} \geq \epsilon) = \mathbb{P}(A_n) = \frac{1}{n} \to 0$, so $\mathbb{1}_{A_n} \to 0$ in probability as $n \to \infty$.

</div>
<br>
    
    
## Tail events
    
<div class="definition">
    
**Definition (Tail $\sigma$-algebras)** For $X_n$ any sequence of random variables set
    
\begin{align}
\tau_n &= \sigma(X_{n+1}, X_{n+2}, ...), \\
\tau &= \bigcap_n \tau_n,
\begin{align}
    
where $\tau$ is called the tail-$\sigma$-algebra.
    
</div>
<br>
    
    

<div class="theorem">
    
**Theorem (Kolmogorov 0-1 law)** Let $X_n$ be independent random variables. If $A \in \tau$, where $\tau$ is the tail-$\sigma$-algebra defined by these events, then $\mathbb{P}(A) = 1$ or $\mathbb{P}(A) = 0$. If $Y : (\Omega, \tau, \mathbb{P}) \to \mathbb{R}$ is measurable, then $Y$ is almost surely constant.
    
</div>
<br>
    
    
## References

```{bibliography} ./references.bib
```