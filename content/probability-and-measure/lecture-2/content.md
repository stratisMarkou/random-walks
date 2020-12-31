# Caratheodory's theorem

This page, and the whole of the second lecture, are concerned with Caratheodory's extension theorem. We state it below and break down its proof in several steps.

(pnm-caratheodory)=
## Statement

<div class="theorem">

**Theorem (Caratheodory's extension theorem)** Let $\mathcal{A} \subseteq \mathcal{P}(E)$ be a ring of subsets of $E$ and let $\mu : \mathcal{A} \to [0, \infty]$ be a countably additive set function. Then $\mu$ can be extended to a measure on $\sigma(\mathcal{A})$.

</div>
<br>

The plan for proving it is as follows. We first define a function $\mu^* : E \to [0, \infty]$ given by

$$ \mu^*(B) = \inf\left\{\sum_n \mu(A_n) : A_n \in \mathcal{A}, B \subseteq \bigcup_n A_n\right\},$$

whenever such $(A_n)$ exists and $\mu^*(B) = \infty$ otherwise. We will call this function the outer measure, although we haven't yet proved it is a measure. Since $\mu^*(\emptyset) = 0$, $\mu^*$ is a {ref}`set function<pnm-l1-setfunc>`. Also observe that $\mu^*$ is {ref}`increasing<pnm-l1-setfunc>` because

$$ A \subseteq B \implies \mu^*(A) \leq \mu^*(B).$$

We will call $A \subseteq E$ $\mu^*$-measurable if, for all $B \subseteq E$, we have 

$$ \mu^*(B) = \mu^*(B \cap A) + \mu^*(B \setminus A).$$

Finally we introduce the family of sets $\mathcal{M}$ as

$$ \mathcal{M} = \{A \subseteq E : A \text{ is } \mu^*\text{-measurable}\}.$$

We will show that $\mu$ and $\mu^*$ agree on $\mathcal{A}$ and that $\mathcal{M}$ is a $\sigma$-algebra containing $\mathcal{A}$. Therefore $\mu$ can be extended to a measure $\mu^*$ on the $\sigma$-algebra $\mathcal{M}$, and consequently on $\sigma(\mathcal{A})$, such that $\mu = \mu^*$ on $\mathcal{A}$.

(pnm-l2-countsub)=
## Outer measure is sub-additive

The first result that we prove is that $\mu^*$ is countably sub-additive for sequences of sets in $E$. This is used for showing subsequent results as well.

<div class="lemma">

**Lemma ($\mu^*$ is countably sub-additive)** Whenever $B_n \in E$ such that $\bigcup_{n = 1}^\infty B_n \in E$ we have
    
$$ \mu^*\left( \bigcup_{n = 1}^\infty B_n \right) \leq \sum_{n = 1}^\infty \mu^*\left(B_n \right).$$

</div>
<br>

<details class="proof">
<summary>Proof: \(\mu^*\) is countably sub-additive</summary>

We assume that $\mu^*(B_n) < \infty$, otherwise the inequality is vacuously satisfied. Then for all $n \in \mathbb{R}$ and $\epsilon > 0$, there exist $A_{nm} \in \mathcal{A}$ such that $B_n \subseteq \cup^\infty_{m = 1} A_{nm}$ and
    
$$ \mu^*(B_n) + \frac{\epsilon}{2^n} \geq \sum_{m = 1} \mu(A_{nm}),$$
    
by the definition of $\mu^*$. Since $B = \cup_n B_n \subseteq \cup_n \cup_m A_{nm}$ and $\mu^*$ is increasing, we have
    
$$\begin{align}
\mu^*(B) &\leq \mu^*\left( \bigcup_{n = 1}^\infty \bigcup_{m = 1}^\infty A_{nm} \right) \leq \sum_{n = 1}^\infty \sum_{m = 1}^\infty \mu(A_{nm})\\
         &\leq \sum_{n = 1}^\infty \mu^*(B_n) + \epsilon,
\end{align}$$
    
where we have used the countable sub-additivity of $\mu$. Because this holds for arbitrary $\epsilon > 0$, we have
    
$$\begin{align}
\mu^*(B) \leq \sum_{n = 1}^\infty \mu^*(B_n),
\end{align}$$
    
so $\mu^*$ is countably sub-additive.

</details>
<br>


## Measure extension

Now we show that $\mu^*$ extends $\mu$ in the sense that whenver $A \in \mathcal{A}$, we have $\mu^*(A) = \mu(A)$.

<div class="lemma">

**Lemma ($\mu^*$ extends $\mu$)** Whenever $A \in \mathcal{A}$ we have $\mu^*(A) = \mu(A)$.

</div>
<br>

<details class="proof">
<summary>Proof: \(\mu^*\) extends \(\mu\)</summary>

Whenever $A \in \mathcal{A}$ and for any disjoint sequence $A_n \in \mathcal{A}$ such that $A \subseteq \cup_n A_n$ we have
    
$$ \mu(A) \leq \mu\left( \bigcup_{n = 1}^\infty (A \cap A_n) \right) \leq \sum_{n = 1}^\infty \mu(A_n),$$
    
where in the last inequality we used the countable additivity of $\mu$. By taking the infimum of both sides, over all possible sequences $A_n$ such that $A \subseteq \cup_n A_n$, we have
    
$$ \mu(A) \leq \mu^*(A).$$
    
We also have
    
$$ \mu^*(A) \leq \mu(A),$$
    
because we can set $A_1 = A, A_{n > 1} = \emptyset$ and observe that $\sum_n \mu(A_n)$ is at least as large as the infimum in the definition of $\mu^*$.

</details>
<br>


## Family M contains family A

We now show that $\mathcal{A} \subseteq \mathcal{M}$, which implies $\sigma(\mathcal{A}) \subseteq \sigma(\mathcal{M})$. Therefore a measure on $\sigma(\mathcal{M})$ would also be a well-defined measure on $\sigma(\mathcal{A})$.

<div class="lemma">

**Lemma ($\mathcal{A} \subseteq \mathcal{M}$)** Under the definitions above, $\mathcal{A} \subseteq \mathcal{M}$. Consequently $\sigma(\mathcal{A}) \subseteq \sigma(\mathcal{M})$.

</div>
<br>

<details class="proof">
<summary>Proof: \(\mathcal{A} \subseteq \mathcal{M}\)</summary>

To prove $\mathcal{A} \subseteq \mathcal{M}$ we need to show that
    
$$ A \in \mathcal{A} \text{ and } B \subseteq E \implies \mu^*(B) = \mu^*(A \cap B) + \mu^*(B \setminus A). $$
    
Because $\mu^*$ is {ref}`countably sub-additive<pnm-l2-countsub>` we have
    
$$ \mu^*(B) \leq \mu^*(B \cap A) + \mu^*(B \setminus A), $$
    
To prove the opposite inequality assume $\mu^*(B) < \infty$ (otherwise the inequality is vacuously satisfied). Then for any $\epsilon > 0$, there exist $A_n \in \mathcal{A}$ such that $B \subseteq \cup_n A_n$ and
    
$$ \sum_{n = 1} \mu(A_{n}) \leq \mu^*(B) + \epsilon.$$
    
Because $B \subseteq \cup_n A_n$ and $\mu^*$ is increasing and {ref}`countably sub-additive<pnm-l2-countsub>` we have
    
$$\begin{align}
\mu^*(B \cap A) + \mu^*(B \setminus A) &\leq \mu^*\left(\bigcup_n A_n \cap A\right) + \mu^*\left(\bigcup_n A_n \setminus A\right) \\
                                       &\leq \sum_{n = 1}^\infty \mu\left(A_n \cap A\right) + \sum_{n = 1}^\infty \mu\left(A_n \setminus A\right) \\
                                       &= \sum_{n = 1}^\infty \mu\left(A_n\right) \\
                                       &\leq \mu^*(B) + \epsilon.
\end{align}$$
    
where we have used the fact that $\mu^* = \mu$ on $\mathcal{A}$ and that $\mu$ is countably sub-additive from the first to the second line. Since this holds for arbitrary $\epsilon > 0$ we have
    
$$\begin{align}
\mu^*(B \cap A) + \mu^*(B \setminus A) \leq \mu^*(B) + \epsilon,
\end{align}$$
    
concluding that 
    
$$ A \in \mathcal{A} \text{ and } B \subseteq E \implies \mu^*(B) = \mu^*(A \cap B) + \mu^*(B \setminus A). $$
    
Therefore $A \in \mathcal{A} \implies A \in \mathcal{M}$ and $\mathcal{A} \subseteq \mathcal{M}$.

</details>
<br>
    
(pnm-l2-msigma)=
## Family M is a sigma-algebra
    
We now show that $\mathcal{M}$ is itself a $\sigma$-algebra, which implies that $\sigma(\mathcal{A}) \subseteq \mathcal{M}$, so any measure on $\mathcal{M}$ is also a well defined measure on $\sigma(\mathcal{A})$.
    
<div class="lemma">

**Lemma ($\mathcal{M}$ is a $\sigma$-algebra)** Under the definitions above, the family $\mathcal{M}$ is a $\sigma$-algebra.

</div>
<br>

<details class="proof">
<summary>Proof: \(\mathcal{M}\) is a \(\sigma\)-algebra</summary>

First, we have $\emptyset \in \mathcal{M}$ and also $A \in \mathcal{M} \implies A^C \in \mathcal{M}$. Now we show that $\mathcal{M}$ is closed under countable unions. Let $B \subset E$, assume $A_n \in \mathcal{M}$ is a disjoint sequence and set $A = \cup_n A_n$. Then
    
$$\begin{align}
\mu^*(B) &= \mu^*(B \cap A_1) + \mu^*(B \cap A^C_1) \\
         &= \mu^*(B \cap A_1) + \mu^*(B \cap A^C_1 \cap A_2) + \mu^*(B \cap A^C_1 \cap A^C_2)\\
         &~\vdots \\
         &= \sum_{n = 1}^N \mu^*(B \cap A_n) + \mu^*\left(B \cap \bigcap_{n = 1}^N A^C_n \right) \\
         &\geq \sum_{n = 1}^N \mu^*(B \cap A_n) + \mu^*\left(B \cap \bigcap_{n = 1}^\infty A^C_n \right),
\end{align}$$
    
where we have used the facts that the $A_n$ are measurable and that $\mu^*$ is an increasing function. Since the above holds for any $N$ we have
    
$$\begin{align}
\mu^*(B) &\geq \sum_{n = 1}^\infty \mu^*(B \cap A_n) + \mu^*\left(B \cap \bigcap_{n = 1}^\infty A^C_n \right) \\
         &\geq \mu^*(B \cap A) + \mu^*\left(B \cap A^C \right) \\
         &= \mu^*(B \cap A) + \mu^*\left(B \cap A^C \right).
\end{align}$$
    
Since $\mu$ is {ref}`countably sub-additive<pnm-l1-countsub>` we also have
    
$$\begin{align}
\mu^*(B) \leq \mu^*(B \cap A) + \mu^*\left(B \cap A^C \right),
\end{align}$$

which together with the previous inequality implies that
    
$$\begin{align}
\mu^*(B) = \mu^*(B \cap A) + \mu^*\left(B \cap A^C \right).
\end{align}$$
    
Hence $A = \bigcup_{n = 1}^\infty A_n \in \mathcal{M}$ and $\mathcal{M}$ is closed under countable unions. Therefore $\mathcal{M}$ is a $\sigma$-algebra.
    
</details>
<br>
    
    
## Outer measure is a measure
    
We complete the proof by showing that the restriction of $\mu^*$ to the domain $\mathcal{M}$ is a measure on $\mathcal{M}$. Hence it is also a valid measure on $\sigma(\mathcal{A}) \supseteq \mathcal{A}$.
    
<div class="lemma">

**Lemma ($\mu_{\mathcal{M}}^*$ is a measure)** Let $\mu_{\mathcal{M}}^*$ be the restriction of $\mu^*$ to the domain $\mathcal{M}$. Then $\mu_{\mathcal{M}}^*$ is a measure on $\mathcal{M}$.

</div>
<br>
    
<details class="proof">
<summary>Proof: \(\mathcal{M}\) is a \(\sigma\)-algebra</summary>

In the proof of the {ref}`previous lemma<pnm-l2-msigma>` we showed that if $B \subset E$ and $A_n \in \mathcal{M}$ is a disjoint sequence, then
    
$$\begin{align}
\mu^*(B) \geq \sum_{n = 1}^\infty \mu^*(B \cap A_n) + \mu^*\left(B \cap A^C \right),
\end{align}$$
    
By setting $B = A = \cup_n A_n$ we arrive at
    
$$\begin{align}
\mu^*(A) \geq \sum_{n = 1}^\infty \mu^*(A_n),
\end{align}$$
    
while from the sub-additivity of $\mu^*$ we have that
    
$$\begin{align}
\mu^*(A) \leq \sum_{n = 1}^\infty \mu^*(A_n).
\end{align}$$
    
Therefore the function $\mu^*$ is countably additive
    
$$\begin{align}
\mu^*(A) = \sum_{n = 1}^\infty \mu^*(A_n),
\end{align}$$
    
and therefore a measure on $\mathcal{M}$.
    
</details>
<br>
    
This completes the proof of Caratheodory's extension theorem. As said before, this theorem is useful because when proving results on measures, we can restrct ourselves to working with rings instead of $\sigma$-algebras. Once a measure has been found for the ring, we can appeal to this theorem to show that the measure can be extended to the $\sigma$-algebra generated by the ring. The benefit is that rings are simpler structures than $\sigma$-algebras and therefore easier to work with.