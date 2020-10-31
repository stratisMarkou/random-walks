# Dynkin's lemma and uniqueness

<div class="definition">

**Definition ($\pi$ system)** A family of sets $\mathcal{A}$ is called a $\pi$ system if $\emptyset \in \mathcal{A}$ and
and for any $A, B \in \mathcal{A}$ we have $A \cup B \in \mathcal{A}$.

</div>
<br>

<div class="definition">

**Definition ($d$ system)** A family of sets $\mathcal{A}$ is called a $d$ system if
    
1. $E \in \mathcal{A}$.
2. For any $A, B \in \mathcal{A}$ such that $A \subseteq B$ we have $B \setminus A \in \mathcal{A}$.
3. For any sequence $A_n \in \mathcal{A}$ such that $A_n \uparrow A$, we have $\bigcup_n A_n \in \mathcal{A}$.

</div>
<br>

<div class="lemma">

**Lemma (Dynkin's lemma)** Let $\mathcal{A}$ be a $\pi$ system. Then any $d$-system that contains $\mathcal{A}$ also contains $\sigma(\mathcal{A})$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Dynkin's lemma</summary>



</details>
<br>

<div class="theorem">

**Theorem (Uniqueness of extension)** Let $\mu_1, \mu_2$ be measures on $(E, \mathcal{E})$, such that $\mu_1(E) = \mu_2(E) < \infty$. Suppose that $\mu_1 = \mu_2$ on $\mathcal{A}$ where $\mathcal{A}$ is a $\pi$ system that generates $\mathcal{E}$, $\mathcal{E} \subseteq \sigma(\mathcal{A})$. Then $\mu_1 = \mu_2$ on $\mathcal{E}$.
    
</div>
<br>

Since rings are $\pi$ systems, this theorem guarantees that the extensions found by Caratheodory's theorem are unique.

<details class="proof">
<summary>Proof: Uniqueness of extension</summary>

We define $\mathcal{D}$ as the family of subsets of $E$ on which $\mu_1$ and $\mu_2$ agree.
    
$$\begin{align}
\mathcal{D} = \{A \in \mathcal{E} : \mu_1(A) = \mu_2(A)\}.
\end{align}$$
    
By definition $\mathcal{A} \subseteq \mathcal{D}$. We will show $\mathcal{E} \subseteq \sigma(\mathcal{A}) \subseteq \mathcal{D}$, by showing that $\mathcal{D}$ is a $d$ system that contains the $\pi$ system $\mathcal{A}$ and appealing to Dynkin's lemma to obtain $\sigma(\mathcal{A}) \subseteq \mathcal{D}$.
    
First we have $E \in \mathcal{D}$ by assumption. Second, if $A, B \in \mathcal{D}$, then
    
$$\begin{align}
\mu_i(A) + \mu_i(B \ A) &= \mu_i(B) \text{ for } i = 1, 2,
\end{align}$$
    
and also $\mu_1(A) = \mu_2(A), \mu_1(B) = \mu_2(B)$. Therefore
    
$$\begin{align}
\mu_1(B \ A) &= \mu_2(B \ A) \implies B \ A \in \mathcal{D}.
\end{align}$$
    
Third, assuming $A_n \in \mathcal{A}$, $A_n \uparrow A$ and $A_n$ is disjoint (wlog) we have
    
$$\begin{align}
\mu_1(A) = \mu_1\left(\bigcup_{n = 1}^\infty A_n\right) = \lim_{N \to \infty} \sum_{n = 1}^N \mu_1\left(A_n\right) = \lim_{N \to \infty} \sum_{n = 1}^N \mu_2\left(A_n\right) = \mu_2\left(\bigcup_{n = 1}^\infty A_n\right) = \mu_2(A),
\end{align}$$
    
so $A \in \mathcal{D}$. Therefore $\mathcal{D}$ is a $d$ system which contains
    
</details>
<br>



<div class="observation">

**Remark (Uniquness and finiteness)** 
    
</div>
<br>