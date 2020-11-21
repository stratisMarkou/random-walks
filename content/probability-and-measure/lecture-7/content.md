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
    
which is non-empty since $g(-\infty) < y < g(\infty)$ so we can always find some $x$ suuch that $y \leq g(x)$. Since $J_y$ is non-empty, its infimum is finite and we write
        
$$ f(y) = \inf J_y. $$

If $x \in J_y$ and $x' \geq x$ then $y \leq g(x) \leq g(x')$ because $g$ is increasing, so $x' \in J_y$. Also for any sequence $x_n \in J_y$ such that $x_n \downarrow x$, we have $y \leq g(x)$ by right continuity so $J_y = [f(y), \infty)$. Therefore
    
$$f(y) \leq x \iff y \leq g(x).$$
    
In addition, $y' \leq y \implies J_y \subseteq J_{y'} \implies f(y') \leq f(y)$ hence $f$ is increasing. Lastly if $y_n \uparrow y$, then $J_y = \lim_{n \to \infty} \bigcap_n J_{y_n}$ so
    
$$ f(y_n) = \inf J_{y_n} = \inf \bigcap^n_k J_{y_k} \to f(y). $$
    
</details>
<br>


<div class="theorem">
    
**Definition (Existence of Radon measures on $\mathbb{R}$)** Let $g : \mathbb{R} \to \mathbb{R}$ be a non-constant, right-continuous and non-decreasing function. Then there exists a {ref}`Radon measure<pnm-borel-sig-alg>` $\mu_g$ on $\mathcal{B}$ such that
    
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