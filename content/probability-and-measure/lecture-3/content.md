# Dynkin's lemma and uniqueness

## Dynkin's lemma

<div class="definition">

**Definition ($\pi$ system)** A family of sets $\mathcal{A}$ is called a $\pi$ system if $\emptyset \in \mathcal{A}$ and
and for any $A, B \in \mathcal{A}$ we have $A \cap B \in \mathcal{A}$.

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

**Lemma ($\pi$ and $d$ system $\iff$ $\sigma$-algebra)** If a family of sets is both a $\pi$-system and a $d$-system, it is a $\sigma$-algebra.
    
</div>
<br>

<details class="proof">
<summary>Proof: \(\pi\) and \(d\) system \(\iff\) \(\sigma\)-algebra</summary>

Let $\mathcal{A}$ be a family of sets that is both a $\pi$ system and a $d$-system. By definition $\emptyset, E \in \mathcal{A}$ and also if $A \in \mathcal{A}$ we have $E \setminus A = A^C \in \mathcal{A}$. We also have that if $A, B \in \mathcal{A}$ then $A \cup B = (A^C \setminus B)^C = (A^C \cap B^C)^C = A \cup B \in \mathcal{A}$.
    
It remains to show that $\mathcal{A}$ is closed under countable unions. Let $A_n \in \mathcal{A}$. Then
    
$$\begin{align}
B_n = \bigcup_{k = 1}^n A_n \in \mathcal{A}.
\end{align}$$
    
Now $B_n \uparrow \bigcup_{k = 1}^\infty A_n$ so $\bigcup_{k = 1}^\infty A_n \in \mathcal{A}$ because $\mathcal{A}$ is a $d$-system. The converse statement holds because a $\sigma$-algebra satisfies each of the properties required for it to be a $\pi$ and a $d$ system by definition.

</details>
<br>


<div class="lemma">

**Lemma (Dynkin's lemma)** Let $\mathcal{A}$ be a $\pi$ system. Then any $d$-system that contains $\mathcal{A}$ also contains $\sigma(\mathcal{A})$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Dynkin's lemma</summary>

We define $\mathcal{D}$ as the intersection of all $d$-systems containing $\mathcal{A}$. We will show that $\mathcal{D}$ is a $d$ system and a $\pi$ system from which it follows, with a use of the previous lemma, that $\mathcal{D}$ is a $\sigma$-algebra containing $\mathcal{A}$, and therefore $\sigma(\mathcal{A}) \subseteq \mathcal{A}$.
    
First, $\mathcal{D}$ contains $E$ since it is an intersection of $d$ systems, each of which contains $E$. Second, if $A, B \in \mathcal{D}$ with $B \subseteq A$, then $A, B$ are contained by every $d$ system that contains $\mathcal{A}$, and so is $B \setminus A$, from which it follows that $A \setminus B \in \mathcal{D}$. Lastly, by the same argument if $A_n \in \mathcal{D}$, then $A = \bigcup_{n = 1}^\infty A_n \in \mathcal{D}$. So $\mathcal{D}$ is a $d$ system.
    
To show that $\mathcal{D}$ is a $\pi$ system consider the set
    
$$ \mathcal{D}' = \{B \in \mathcal{D} : A \cap B \in \mathcal{D} \text{ for all } A \in \mathcal{A}\}. $$
    
We see that $\mathcal{A} \subseteq \mathcal{D}'$ because $\mathcal{A}$ is a $\pi$ system. Further $\mathcal{D}'$ is a $d$ system because
    
1. $E \cap A = A^C \in \mathcal{D}$.
2. If $B_1, B_2 \in \mathcal{D}'$, such that $B_1 \subseteq B_2$, then \begin{align} (B_2 \setminus B_1) \cap A = (B_2 \cap A) \setminus B_1 \in \mathcal{A} \end{align} and since $A, B_1, B_2 \in \mathcal{D}$ and $\mathcal{D}$ is a $d$ system, we also have $(B_2 \setminus B_1) \cap A \in \mathcal{D}$ for all $A \in \mathcal{A}$ and thus $B_2 \setminus B_1 \in \mathcal{D}$.
3. If $B_n \uparrow B$ and $A \in \mathcal{A}$, then $B_n \cap A \in \mathcal{D}$ and \begin{align} B_n \cap A \uparrow B \cap A \in \mathcal{D} \end{align} since $\mathcal{D}$ is a $d$ system. Hence $B \in \mathcal{D}'$.
    
Therefore $\mathcal{D}'$ is a $d$ system containing $\mathcal{A}$ hence $\mathcal{D} \subseteq \mathcal{D}'$. Conversely $\mathcal{D}' \subseteq \mathcal{D}$ by the definition of $\mathcal{D}'$ hence $\mathcal{D} = \mathcal{D}'$. Now define the set
    
$$ \mathcal{D}'' = \{B \in \mathcal{D} : A \cap B \in \mathcal{D} \text{ for all } A \in \mathcal{D}\}. $$
    
By construction, this is a $\pi$ system that contains $\mathcal{A}$. By repeating the previous steps we have $\mathcal{D} = \mathcal{D}''$ and since $\mathcal{D}$ (and thus also $\mathcal{D}''$) is a $\pi$ system and a $d$ system it is also a $\sigma$-algebra that contains $\mathcal{A}$ as well as $\sigma(\mathcal{A})$.

</details>
<br>

## Uniqueness of measures

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
\mu_i(A) + \mu_i(B \setminus A) &= \mu_i(B) \text{ for } i = 1, 2,
\end{align}$$
    
and also $\mu_1(A) = \mu_2(A), \mu_1(B) = \mu_2(B)$. Therefore
    
$$\begin{align}
\mu_1(B \setminus A) &= \mu_2(B \setminus A) \implies B \setminus A \in \mathcal{D}.
\end{align}$$
    
Third, let us assume $A_n \in \mathcal{A}$, $A_n \uparrow A$ and $A_n$. We define $B_n$ to be the disjoint sequence of sets $B_n = A_n \setminus \cup_{m < n} A_n$ and observe that $B_n \in \mathcal{D}$ because $A \setminus B \in \mathcal{A}$ whevener $A, B \in \mathcal{A}$. Therefore we have
    
$$\begin{align}
\mu_1(A) &= \mu_1\left(\bigcup_{n = 1}^\infty B_n\right) = \lim_{N \to \infty} \sum_{n = 1}^N \mu_1\left(B_n\right) = \lim_{n \to \infty} \mu_1\left(A_n\right) = \\
&= \lim_{n \to \infty} \mu_2 \left(A_n\right) = \lim_{n \to \infty} \sum_{n = 1}^N \mu_2\left(B_n\right) = \mu_2\left(\bigcup_{n = 1}^\infty B_n\right) = \mu_2(A),
\end{align}$$
    
so $A \in \mathcal{D}$. Therefore $\mathcal{D}$ is a $d$ system which contains the $\pi$ system $\mathcal{A}$, and by Dynkin's lemma it also contains $\sigma(\mathcal{A})$.
    
</details>
<br>



<div class="observation">

**Remark (Uniquness and finiteness)** A measure on $(E, \mathcal{E})$ is finite if $\mu(E) < \infty$. The uniqueness theorem applies to $\sigma$-finite measures $\mu$.
    
</div>
<br>