# Measurable functions

This page briefly states and proves the Borel-Cantelli lemmas and then focuses on the measurability of functions. A function from one measurable space to another is called measurable if the pre-image of every set in its range sigma-algebra is in its domain sigma-algebra. We state and prove some results on the measurability of functions, including the monotone classes theorem.
    
    
## Borel-Cantelli lemmas

First we introduce the defintion of liminf and limsup in the context of sets.

<div class="definition">
    
**Definition (liminf and limsup)** We define the $\lim \inf$ and $\lim \sup$ of sets as
    
$$\begin{align} \lim \sup A_n &= \bigcup_n \bigcap_{m \geq n} A_m = \{A_n \text{ infinitely often (i.o.)}\} \\
\lim \inf A_n &= \bigcap_n \bigcup_{m \geq n} A_m = \{A_n \text{ eventually}\}\end{align}$$
    
</div>
<br>


The first Borell-Cantelli lemma states that if the sum of the probabilities of a sequence of events is not divergent, then the probability of events from $A_n$ occuring infinitely often is $0$.
    
<div class="lemma">

**Lemma ($1^{st}$ Borel-Cantelli lemma)** If $\sum_n \mathbb{P}(A_n) < \infty$ then $\mathbb{P}(A_n \text{ i.o.}) = 0$.

</div>
<br>
    
    
<details class="proof">
<summary>Proof: \(1^{st}\) Borel-Cantelli lemma</summary>

By definition we have
    
$$\begin{align}
\mathbb{P}(A \text{ i.o.}) &= \mathbb{P}\left(\cap_n \cap_{m \geq n} A_m\right) \\
                           &\geq \mathbb{P}\left(\cap_{m \geq n} A_m\right) \text{ for all } n\\
                           &\geq \sum_{m \geq n}\mathbb{P}\left(A_m\right) \to 0 \text{ as } n \to \infty.
\end{align}$$
    
Hence $\sum_n \mathbb{P}(A_n) < \infty \implies \mathbb{P}(A_n \text{ i.o.}) = 0$.
    
</details>
<br>

The second Borell-Cantelli lemma states that if the sum of the probabilities of a sequence of events is divergent and the events are independent then the probability of events from $A_n$ occuring infinitely often is $1$.
    
<div class="lemma">

**Lemma ($2^{nd}$ Borel-Cantelli lemma)** If $\sum_n \mathbb{P}(A_n) = \infty$ and the $A_n$ are independenent, then $\mathbb{P}(A \text{ i.o.}) = 1$.

</div>
<br>
    
    
<details class="proof">
<summary>Proof: \(2^{nd}\) Borel-Cantelli lemma</summary>

Since the $A_n$ are independenent, we can write
    
$$\begin{align}
\mathbb{P}\left(\bigcap^N_{m \geq n} A_m^C\right) &= \prod_{m = n}^N (1 - a_n) \\
                                                  &\leq \exp\left[-\sum_{m = n}^N a_n\right] && \text{ since } 1 - a \leq e^{-a} \text{ always} \\
                                                  &\to 0 \text{ as } N \to \infty,
\end{align}$$
    
from which it follows that

$$ \mathbb{P}\left(\bigcap_{m \geq n} A_m^C\right) = 0 \text{ for all } n,$$
    
arriving at the result
    
$$ \mathbb{P}(A_n \text{ i.o.}) = 1 - \mathbb{P}\left(\bigcup_n \bigcap_{m \geq n} A_m^C\right) = 1.$$
    
</details>
<br>
    
    
## Measurable functions

We now introduce measurable functions. Ginve measurable spaces $(E, \mathcal{E})$ and $(G, \mathcal{G})$, a function $f : \mathcal{E} \to \mathcal{G}$ is measurable if the pre-image of $f$ of any set in $\mathcal{G}$ is also in $\mathcal{E}$.
    
<div class="definition">
    
**Definition (Measurable functions)** Let $(E, \mathcal{E})$ and $(G, \mathcal{G})$ be measurable spaces. A function $f : \mathcal{E} \to \mathcal{G}$ is called $\mathcal{E}-\mathcal{G}$ measurable if
    
$$ f^{-1}(A) = \{ x \in E : f(x) \in A\} \in \mathcal{E} \text{ for all } A \in \mathcal{G}.$$
    
When $(G, \mathcal{G}) = (\mathbb{R}, \mathcal{B})$, we simply say that $f : E \to \mathbb{R}$ is measurable. If $E$ is a topological space $\mathcal{E} = \mathcal{B}(E)$, we say that $f$ is Borel measurable.
    
</div>
<br>


Pre-images preserve set operations such as complements or unions, so pre-images of $\sigma$-algebras are $\sigma$-algebras.

    
<div class="lemma">

**Lemma (Pre-images of $\sigma$-algebras are $\sigma$-algebras)** If $(E, \mathcal{E})$ and $(G, \mathcal{G})$ are measurable spaces and $f : \mathcal{E} \to \mathcal{G}$ is a measurable function, then
    
$$ \{f^{-1}(A) : A \in \mathcal{G}\} \text{ is a } \sigma \text{ algebra.}$$

</div>
<br>

<details class="proof">
<summary>Proof: Pre-images of \(\sigma\)-algebras are \(\sigma\)-algebras</summary>
    
Consider first the set
    
$$ \mathcal{S} = \{f^{-1}(A) : A \in \mathcal{G}\}.$$
    
Firstly, $\emptyset \in \mathcal{G}$ so $f^{-1}(\emptyset) = \emptyset \in \mathcal{S}$ by assumption. Second, if $A \in \mathcal{G}$ then $A^C \in \mathcal{G}$ so
    
$$f^{-1}(A^C) = f^{-1}(A)^C \in \mathcal{S}.$$
    
Lastly, assuming $A_n \in \mathcal{G}$ we have $A = \bigcup A_n \in \mathcal{G}$. By definition we have $f^{-1}(A)$ and so
    
$$\bigcup_{n = 1} f^{-1}\left(A_n \right) = f^{-1}\left(\bigcup_{n = 1} A_n \right) = f^{-1}(A) \in \mathcal{S}.$$
    
Therefore $S$ satisfies the {ref}`necessary properties<pnm-sigalg-meas>` to be a $\sigma$-algebra.
    
</details>
<br>
    
    
In practice, we can use the following useful result for checking measurability. If $f$ is a measurable function and $\mathcal{G} = \sigma(\mathcal{A})$, where all pre-images of $A \in \mathcal{A}$ are in $\mathcal{E}$, then $f$ is measurable.
    
    
<div class="lemma">

**Lemma (Measurability criterion on a subset of a $\sigma$-algebra)** If $(E, \mathcal{E})$ and $(G, \mathcal{G})$ are measurable spaces and $f : \mathcal{E} \to \mathcal{G}$ and $\mathcal{G} = \sigma(\mathcal{A})$ where $\emptyset \in \mathcal{A}$ and
    
$$f^{-1}(A) \in \mathcal{E} \text{ for all } A \in \mathcal{A},$$
    
then $\{A : f^{-1}(A) \in \mathcal{E}\}$ is a $\sigma$-algebra and it contains $\mathcal{A}$ and $\mathcal{G}$ so $f$ is measurable. In particular, when $(G, \mathcal{G}) = (\mathbb{R}, \mathcal{B})$, then the intervals $\{ (-\infty, y] : y \in \mathbb{R} \}$ generate $\mathcal{B}$ and so if
    
$$ \{x \in E : f(x) \leq y \} \in \mathcal{E} \text{ for all } y \in \mathbb{R}, $$

then $f$ is Borel measurable.

</div>
<br>
    
    
<details class="proof">
<summary>Proof: Measurability criterion on a subset of a \(\sigma\)-algebra</summary>
    
We can show this result using the same argument as the previous lemma.
    
</details>
<br>
    
We now state and prove two lemmas about the measurablity of indicators and about operations which preserve measurability respectively.
    
<div class="lemma">

**Lemma (Indicator function is measurable)** If $A \in \mathcal{E}$, then the indicator function
    
$$\begin{align}
1_{A}(x) = \begin{cases} 1, & \text{ if } x \in A, \\ 0, & \text{ otherwise,}\end{cases}
\end{align}$$
    
is measurable.

</div>
<br>
    
<details class="proof">
<summary>Proof: Indicator function is measurable</summary>

Let $(E, \mathcal{E})$ be a measurable space and consider the measruable space $G, \sigma(G)$ where $G = \{0, 1\}$. Then defining the indicator function
    
$$\begin{align}
1_{A}(x) = \begin{cases} 1, & \text{ if } x \in A, \\ 0, & \text{ otherwise,}\end{cases}
\end{align}$$
    
we see that its pre-image $1_{A}^{-1}$ can only take the values $\emptyset, A, A^C$ or $E$, all of which are in $\mathcal{E}$. Therefore $1_{A}$ is measurable.
    
</details>
<br>
    
    
<div class="lemma">

**Lemma (Operations preserving measurability)** Given a measurable space $(E, \mathcal{E})$ and a sequence of measurable functions $f_n : \mathcal{E} \to \mathcal{B}$, the following are all measurable $f_1 + f_2$, $f_1 \cdot f_2$, $\inf_n f_n$, $\sup_n f_n$, $\lim \inf_n f_n$ and $\lim \sup_n f_n$ and also
    
$$ \{ x \in E : f_n(x) \text{ converges as } n \to \infty \} $$
    
is a measurable subset of $E$.

</div>
<br>

    
Lastly, we mention that given any maps $f_i : \mathcal{E} \to \mathcal{G}$ for $i \in I$, we can make them all $\mathcal{E}-\mathcal{G}$ measurable by setting
    
$$ \mathcal{E} = \sigma\left( f_i^{-1}{A} : A \in \mathcal{G}, i \in I \right),$$
    
which is the $\sigma$-algebra generated by $(f_i : i \in I)$.
    
    
## Monotone classes theorem
    
We conclude with a statement and proof of the monotone classes theorem.
    
<div class="theorem">
    
**Theorem (Monotone classes)** Let $(E, \mathcal{E})$ be a measurable space and let $\mathcal{A}$ be a $\pi$-system generating $\mathcal{E}$. Let $V$ be a vector space of bounded maps $f : E \to \mathbb{R}$ such that
    
1. $1 = 1_{E} \in V$ and $1_A \in V$ for all $A \in \mathcal{A}$,
2. Whenever $f_n$ are bounded maps in $V$ and $f$ is a bounded map such that $0 \leq f_n \uparrow f$ pointwise, then $f \in V$,
    
then $V$ contains all bounded measurable maps.
    
</div>
<br>

<details class="proof">
<summary>Proof: Monotone classes</summary>

Let us define the set $D$ as
    
$$ D = \{A \in \mathcal{E} : 1_A \in V\}. $$
    
Then $D$ contains $E$ because $1 = 1_E \in V$. Also, whenever $A \subseteq B$ we have $1_{B \setminus A} = 1_B - 1_A \in V$ since $V$ is a vector space, so $B \setminus A \in D$. Lastly, whenever $A_n \in D$ such that $A_n \uparrow A$, we have $1_{A_n} \uparrow 1_A$ so $1_A \in V$ and also $A \in D$. Therefore, $D$ satisfies the requirements for being a $d$-system. Since $D$ contains the $\pi$-system $A$, we have by Dynkin's lemma
    
$$ \mathcal{E} \subseteq \sigma(\mathcal{A}) \subseteq \mathcal{D}. $$
    
But since $\mathcal{D} \subseteq \mathcal{E}$ we have $\mathcal{D} = \mathcal{E}$. Therefore, the $\sigma$-algebra $\mathcal{E}$ is generated by the family of sets which correspond to some indicator function in $V$. Now let $f : E \to [0, \infty)$ be any boounded non-negative measurable map. We define the piecewise constant approximation
    
$$ f_N(x) = 2^{-N} \sum^{~N2^N}_{n = 1} n~1_{A_{n, N}},$$
    
where the sets $A_{n, N}$ are defined as
    
$$ A_{n, N} = \left\{x : \frac{n}{2^N} < f(x) \leq \frac{n + 1}{2^N} \right\} \text{ for } n < N, \text{ and } \left\{x : f(x) > n\right\} \text{ for } n = N.$$
    
Τhese sets are contained in $\mathcal{E}$ because $f$ is a measurable map by assumption so that
    
$$\begin{align}
f^{-1}\left(\left(\frac{n}{2^N}, \frac{n + 1}{2^N}\right]\right) &\in \mathcal{E}, \\
~\\
f^{-1}\left(\left(n, \infty \right)\right) &\in \mathcal{E}.
\end{align}$$
    
Since $V$ is a vector space containing $1_{A_{n, N}}$, it contains any linear combination of them so it also contains $f_n$. Now since $f_n(x) \leq f(x)$ we have
    
$$ f_n(x) \leq f(x) \leq f_n(x) + \frac{1}{2^n}, $$
    
so $f_n \uparrow f$ pointwise, so $f \in V$ by the second property that we assumed $V$ to have. To show that $V$ contains an arbitrary bounded, measurable $f : E \to \mathbb{R}$, we can write $f = f^+ + f^-$ and apply the preceeding argument to $f^+ : E \to [0, \infty)$ completing the proof.
    
</details>
<br>
    