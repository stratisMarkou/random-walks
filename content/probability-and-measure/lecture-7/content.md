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
    
Then by the lemma of generalised inverses, we have
    
$$\begin{align}
\mathbb{P}(X_n \leq x_n) &= \mathbb{P}(G_n(Y_n) \leq x_n) \\
                         &= \mathbb{P}(Y_n \leq F_n(x_n)) \\
                         &= F_n(x_n),
\end{align}$$
    
arriving at the result.
    
</details>
<br>