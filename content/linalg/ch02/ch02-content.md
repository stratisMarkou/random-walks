# Finite dimensional vector spaces

(linalg-lincomb-and-span)=
## Linear combinations and span

<div class="definition">

**Definition (Linear combination)** Given a list of vectors $v_1, ..., v_n \in V$, we call
    
$$ v = a_1v_1 + ... + a_n v_n, a_i \in \mathbb{F}, $$
    
a linear cobination of these vectors.
    
</div>
<br>


<div class="definition">

**Definition (Span)** The set of all linear combinations of a list of vectors, is called the span of the list and is denoted
    
$$\text{span}(v_1, ..., v_n) = \{a_1v_1 + ... + a_n v_n, a_i \in \mathbb{F}\}.$$
    
We define the span of the empty list $()$ to be the set $\{0\}$.
    
</div>
<br>


<div class="lemma">

**Lemma (Span is the smallest containing subspace)** The span of a list of vectors in $V$ the smallest subspace of $V$ that contains the vectors.
    
</div>
<br>


<details class="proof">
<summary>Proof: Span is the smallest containing subspace</summary>
    
In the following, let $v_1, ..., v_n \in V$ and $S = \text{span}(v_1, ..., v_n)$.

**Span is a subspace:** First, $\{0\} \in \mathbb{F}$ since $0$ is a linear combination of the vectors $v_1, ..., v_n$. Second, $S$ is closed under additions because if $s_1, s_2 \in S$ then $s_1, s_2$ are linear combinations of $v_1, ..., v_n$ and also $s_1 + s_2$ is a linear combination of $S$. Lastly, if $s \in S$ then also $\lambda s \in \mathbb{F}$ because $s$ is a linear combination of $v_1, ..., v_n$ and the $\lambda$ coefficient can be absorbed in the coefficients of the linear combination. Therefore $S$ satisfies {ref}`the three necessary and sufficient conditions for being a subspace<linalg-subspaces>`.
    
    
**Span is the smallest containing subspace:** This holds because any subspace $U \subseteq V$ which contains the vectors $v_1, ..., v_n$ must also contain all of their linear combinations. Since all the elements in $S$ are linear combinations of the vectors $v_1, ..., v_n$ we have $S \subseteq U$.
    
    
</details>
<br>

(linalg-span)=
## Span

<div class="definition">

**Definition (List spans $V$)** We say that a list of vectors $v_1, ..., v_n$ spans $V$ if
    
$$\text{span}(v_1, ..., v_n) = V.$$
    
</div>
<br>



<div class="definition">

**Definition (Finite/Infinite dimensional vector space)** A vector space is called finite dimensional if it is spanned by some list of vectors in it. If a vector space is not finite dimensional, we call it infinite dimensional.
    
</div>
<br>


<div class="definition">

**Definition (Polynomial, degree)** A function $p : \mathbb{F} \to \mathbb{F}$ is called a polynomial with coefficients in $\mathbb{F}$ if there exist $a_0, ..., a_m \in \mathbb{F}$ such that
    
$$ p(z) = a_0 + a_1 z + a_2 z^2 + ... + a_m z_m, \text{ for all } z \in \mathbb{F}. $$
    
We say that $p$ has degree $k$ where $k$ is the largest integer for which $a_k \neq 0$. We use $\mathcal{P}(\mathbb{F})$ to denote the set of all polynomials with coeffcients in $\mathbb{F}$. We use $\mathcal{P}_m(\mathbb{F})$ to denote the set of all polynomials of degree $m$ with coefficients in $\mathbb{F}$. We define the degree of the polynomial that is identically $0$ to be $- \infty$.
    
</div>
<br>

(linalg-indep)=
## Linear independence

<div class="definition">

**Definition (Linearly independent/dependent)** We call a list of vectors $v_1, ..., v_m$ linearly independent if
    
$$ a_1 v_1 + ... + a_m v_m = 0 \implies a_1 = ... = a_m = 0. $$
    
The empty list $()$ is defined to be linearly independent. We call a list of vectors in $V$ linearly dependent if it is not linearly independent.
    
</div>
<br>



<div class="lemma">

**Lemma (Linear Dependence Lemma)** If $v_1, ..., v_m \in V$ is linearly dependent, there exists $j \in \{1, 2, ..., m\}$ such that
    
- $v_j \in \text{span}(v_1, ..., v_{j-1})$.
    
- if the $j^{th}$ term is removed from the list, the span of the resulting list remains the same.
    
</div>
<br>

<details class="proof">
<summary>Proof: Linear Dependence Lemma</summary>
    
In the following parts, let $v_1, ..., v_m$ be a linearly dependent list of vectors in $V$.
    
**Part 1:** Since $v_1, ..., v_m$ is linearly dependent, there exists a linear combination
    
$$ a_1 v_1 + ... + a_m v_m = 0, $$
    
such that at least one $a_i \neq 0$. Let $v_j$ be this vector. Then
    
$$ v_j = -\sum_{i \neq j} \frac{a_i}{a_j}v_i, $$
    
so $v_j \in \text{span}(v_1, ..., v_{j-1})$.
    
**Part 2:** From the previous argument, we can express $v_j$ as a linear combination of the other vectors in the list. Therefore, any linear combination of the vectors of the full list can be re-written as a linear combination of the vectors in the list with $v_j$ removed, by adjusting the remaining coefficients appropriately:
    
$$\begin{align}
v = a_1 v_1 + ... + a_m v_m = \sum_{i \neq j} \left(a_i - \frac{a_i}{a_j} \right) v_i.
\end{align}$$
    
</details>
<br>



<div class="definition">

**Definition (Length of linearly independent and spanning lists)** In a finite dimensional space, the length of any linearly independent list cannot be larger than the length of any spanning list.
    
</div>
<br>


<details class="proof">
<summary>Proof: Length of linearly independent and spanning lists</summary>

Suppose that $V$ is a finite dimensional vector space and that $u_1, ..., u_m$ is a linearly independent list while $w_1, ..., w_n$ is a spanning list. We can proceed in the following recursive process.

The list $u_1, w_1, ..., w_n$ is linearly dependent, but by the Linear Dependence Lemma we can remove one of the $w$ vectors from this list, and the resulting list will still span $V$. We can proceed by inserting $u_2$ after $u_1$ in the list, to obtain a new list whose first two entries are $u_1, u_2$ and the rest are $w$'s to get another linearly dependent list. Again by the Linear Dependence Lemma, we can remove one of the $w$'s from the list to obtain a list that still spans $V$. Proceeding iteratively, we can insert all the $u$'s to the list while removing $w$'s, until all the $u$'s have been added to the list.

At each step of the above process, the linear independence of the $u_1, \dots, u_n$ together with the Linear Dependence Lemma imply that there is a $w$ term to remove and thus $m \leq n$.
    
</details>
<br>
    

<div class="lemma">

**Lemma (Finite dimensional subspace)** Any subspace of a finite dimensional vector space is finite dimensional.
    
</div>
<br>


<details class="proof">
<summary>Proof: Finite dimensional subspace</summary>

Let $V$ be a finite dimensional space with subspace $U \subseteq V$. Then there exists a list $v_1, ..., v_n$ which spans $V$.
    
If $U = \{0\}$, then $U$ is finite dimensional. Suppose $U \neq \{0\}$. Then there exists a nonzero $u_1 \in U$. If $u_1$ spans $U$ then $U$ is finite dimensional. If not, there exists $u_2 \in U$ such that $u \not \in \text{span}(u_1)$. If $u_1, u_2$ spans $U$ then again $U$ is finite dimensional. We can proceed in this iterative fashion until a list $u_1, ..., u_m$ is found which spans $U$. If no such list is found, the length of this linearly independent list will eventually exceed the length of the spanning list $v_1, ..., v_n$. But since any linearly independent list cannot have a length greater than a spanning list, this procedure must terminate for some $m \leq n$. Therefore $U$ is finite dimensional.
    
</details>
<br>
    
    
    
## Bases

<div class="definition">

**Definition (Basis)** We call a list of vectors in $V$ a basis of $V$ if it is linearly independent and it spans $V$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Criterion for basis)** A list $v_1, ..., v_n \in V$ is a basis of $V$ if and only if every $v \in V$ can be written as
    
$$ v = a_1 v_1 + ... + a_n v_n, a_i \in \mathcal{F}, $$
    
in a unique way.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Criterion for basis</summary>

Suppose $v_1, ..., v_n \in V$ is a basis of $V$. Then it spans $V$ so every $v \in V$ can be written in the form
    
$$\begin{align}
v = a_1 v_1 + ... + a_n v_n, a_i \in \mathcal{F}.
\end{align}$$
    
Furthermore, this expression is unique because $v_1, ..., v_n$ is linearly independent so if 
    
$$\begin{align}
v = a_1 v_1 + ... + a_n v_n = b_1 v_1 + ... + b_n v_n.
\end{align}$$
    
for some $b_i \in \mathcal{F}$, then
    
$$\begin{align}
(b_1 - a_1) v_1 + ... + (b_n - a_n) v_n = 0 \implies a_i = b_i,
\end{align}$$
    
where we have used {ref}`the definition of linear independence<linalg-indep>`. Going the other way, if every $v$ can be writen in a unique way as
    
$$\begin{align}
v = a_1 v_1 + ... + a_n v_n, a_i \in \mathcal{F},
\end{align}$$
    
then $v_1, ..., v_n$ spans $V$ and also $0$ can be written in a unique way as the linear combination of the vectors $v_1, ..., v_n$. The list is a linearly independent spanning list in $V$ and is therefore a basis of $V$.
    
</details>
<br>
    
    
<div class="lemma">

**Lemma (Spanning list contains basis)** If $\text{span}(v_1, ..., v_n) = V$, then $(v_1, ..., v_n)$ can be reduced to a basis of $v$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Spanning list contains basis</summary>

Suppose $v_1, ..., v_n \in V$ and $\text{span}(v_1, ..., v_n) = V$. We can apply the {ref}`Linear Dependence Lemma<linalg-indep>` a number of times, removing a vector from the list at each step. At each such step, the resulting list still spans $V$. The process must eventually terminate - if it did not there would be no vectors left in $V$ so the list would no longer span $V$. When the process terminates, the list must be linearly independent - if it was not, then the {ref}`Linear Dependence Lemma<linalg-indep>` could be applied once again to remove another vector from the list. Therefore, the resulting list is a linearly independent spanning list and hence also a basis.
    
</details>
<br>
    
  
 
<div class="lemma">

**Lemma (Finite dimensional vector spaces have bases)** If $V$ is a finite dimensional vector space, then there exists a basis of $V$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Finite dimensional vector spaces have bases</summary>

By {ref}`definition<linalg-span>`, a finite dimensional vector space $V$ has a spanning list. By the previous lemma, the spanning list can be reduced to a basis.
    
</details>
<br>
    
    
  
<div class="lemma">

**Lemma (Linearly independent list extends to a basis)** Every linearly independent list $v_1, ..., v_m$ in a finite dimensional vector space $V$ can be extended to a basis of $V$ by adding vectors $v_{m + 1}, ..., v_n$ to it, such that the resulting list $v_1, ..., v_n$ is a basis of $V$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Linearly independent list extends to a basis</summary>

Let $v_1, ..., v_m$ be a linearly independent list of vectors in $V$, a finite dimensional vector space. Since $V$ is a finite dimensional space, it has a spanning list $w_1, ..., w_n$ {ref}`by definition<linalg-span>`. By appending these vectors to the original list, we obtain a new list
    
$$\begin{align}
v_1, ..., v_m, w_1, ..., w_n
\end{align}$$   
    
which spans $V$. We may then apply the {ref}`Linear Dependence Lemma<linalg-indep>` a number of times, removing a vector from the list at each step. The procedure must terminate - if it did not there would be no vectors left in $V$ so the list would no longer span $V$. The resulting list must be linearly independent - if it was not, then the lemma could be applied once again to remove another vector from the list. In addition, the list will span $V$ so the end result is a linearly dependent spanning list in $V$, which is a basis.
    
Note also that none of the vectors $v_1, ..., v_m$ will be removed from the list because these are already linearly independent. Therefore the resulting list will contain all of the $v_1, ..., v_m$ vectors, because these are already linearly independent. So the final list is an extended version of the original.
    
</details>
<br>
    
    
    
<div class="lemma">

**Lemma ($U$ is a subspace $\implies U \oplus W = V$)** Let $V$ be a finite dimensional vector space with subspace $U$. Then there exists a subspace $V$ of $W$ such that $U \oplus W = V$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: \(U\) if a subspace \(\implies U \oplus W = V\)</summary>

Since $U$ is a subspace of the finite space $V$, it has a basis $u_1, ..., u_m$. This basis can be extended to a basis of $V$, by appending the vectors $w_1, ..., w_n$ to it. Therefore the resulting list
    
$$\begin{align}
u_1, ..., u_m, w_1, ..., w_n
\end{align}$$
    
spans $V$. Let $\text{span}(w_1, ..., w_n) = W$. Then $W$ is a subspace and $U + W = V$. To see that $U + W = U \oplus W$ is a direct sum, {ref}`it suffices to show<linalg-direct-sum>` that $U \cap W = \{0\}$. This holds because the list $u_1, ..., u_m, w_1, ..., w_n$ is linearly independent so if $U$ and $W$ shared an element $x$, then $x$ would be in the spans of both $u_1, ..., u_m$ and $w_1, ..., w_n$. Therefore, it would be possible to write $0$ as a non-zero linear combination of the vectors of the two lists, contradicting the fact that they are linearly independent. Therefore $U + W = U \oplus W$, concluding the proof.
    
</details>
<br>
    
    
## Dimension
    
<div class="lemma">

**Lemma (Bases have the same length)** Any two bases of a finite dimensional vector space $V$ have the same length.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Bases have the same length</summary>

Let $\ell_1, \ell_2$ be two bases of the finite dimensional vector space $V$. Both $\ell_1, \ell_2$ are spanning lists. Since a linearly independent list cannot have length greater than the dimension of a spanning list, we have
    
$$\begin{align}
\text{dim span} {\ell_1} \leq \text{dim span} {\ell_2},
\end{align}$$
    
but also, reversing the roles of $\ell_1, \ell_2$ we also have
    
$$\begin{align}
\text{dim span} {\ell_2} \leq \text{dim span} {\ell_1},
\end{align}$$
    
implying $\text{dim span} {\ell_1} = \text{dim span} {\ell_2}$.
    
</details>
<br>
    
    
<div class="definition">

**Definition (Dimension)** Let $V$ be a {ref}`finite-dimensional vector space<linalg-indep>`. The dimension of $V$, written $\text{dim}~V$, is the length of any basis of $V$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Dimension of a subspace)** If $V$ is a finite dimensional vector space and $U$ is a subspace of $V$, then $\text{dim}~ U \leq \text{dim}~ V$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Dimension of a subspace</summary>

Let $V$ be a finite dimensional vector space and $U$ be a subspace of $V$. Since $U$ is a finite dimensional vector space, it has a basis. This basis can be extended to a basis of $V$. The extended basis is a list with at least as many vectors as the original basis. Therefore $\text{dim}~ U \leq \text{dim}~ V$.
    
</details>
<br>
    
    
<div class="lemma">

**Lemma (Linearly independent list of the right length is a basis)** If $V$ is a finite dimensional space, then every linearly independent list of length $\text{dim}~V$ is a basis of $V$.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Linearly independent list of the right length is a basis</summary>
    
Suppose $V$ is a finite dimensional space and let $v_1, ..., v_n \in V$ be a linearly independent list with $n = \text{dim}~V$. This list can be extended to a basis of $V$. But since all bases have the same length, the extension construction cannot add any new vectors to the list. Therefore $v_1, ..., v_n$ is a basis of $V$, and all linearly independent lists of length $\text{dim}~V$ are bases.
    
</details>
<br>
  
    
<div class="lemma">

**Lemma (Spanning list of the right length is a basis)** Suppose $V$ is a finite-dimensional vector space and $v_1, ..., v_n$ is a list of length with dimension $n = \text{dim}~V$. Then if $v_1, ..., v_n$ spans $V$ it is a basis of $V$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Spanning list of the right length is a basis</summary>
    
Suppose $V$ is a finite-dimensional vector space and $v_1, ..., v_n \in V$ is a list of length with dimension $n = \text{dim}~V$. Suppose also that $v_1, ..., v_n$ spans $V$. We will show that $v_1, ..., v_n$ is linearly independent.
    
If $v_1, ..., v_n$ were linearly dependent, then by the {ref}`linear dependence lemma<linalg-indep>` we could remove a non-zero number of vectors from it, while leaving its span unchanged. By removing vectors until the list becomes linearly independent, we would obtain a linearly independent list which spans $V$ and is therefore a basis. But this basis would have length striclty smaller than $n$, which is a contradiction because every basis of $V$ must have length $n$. So $v_1, ..., v_n$ was linearly independent to begin with, and therefore also a basis.
    
</details>
<br>
  
    
<div class="lemma">

**Lemma (Dimension of a sum)** Suppose $U_1, U_2$ are subspaces of a finite-dimensional vector space. Then
    
$$\begin{align}
\text{dim} (U_1 + U_2) = \text{dim}~U_1 + \text{dim}~U_2 - \text{dim} (U_1 \cap U_2).
\end{align}$$
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Dimension of a sum</summary>
    
Suppose $U_1, U_2$ are subspaces of a finite-dimensional vector space. Then $U_1 \cap U_2$ is a finite-dimensional vector space, so there exists a basis $u_1, ..., u_n$ for it. This basis can be extended to a basis $u_1, ..., u_n, v_1, ..., v_k$ for $U_1$ and a basis $u_1, ..., u_n, w_1, ..., w_m$ for $U_2$. Now we will show that
    
$$\begin{align}
\text{dim} (U_1 + U_2) = n + k + m.
\end{align}$$
    
First, the list $u_1, ..., u_n, v_1, ..., v_k, w_1, ..., w_m$ spans $U_1 + U_2$. Second, it is linearly independent by the following argument. Suppose
    
$$\begin{align}
a_1 u_1 + ... + a_n u_n + b_1 v_1 + ... + b_n v_n + c_1 w_1 + ... + c_n w_n = 0.
\end{align}$$

Then it holds that
    
$$\begin{align}
c_1 w_1 + ... + c_n w_n = - a_1 u_1 - ... - a_n u_n - b_1 v_1 - ... - b_n v_n,
\end{align}$$
    
which implies $(c_1 w_1 + ... + c_n w_n) \in U_1$. But since $w_i \in U_2$, we also have $(c_1 w_1 + ... + c_n w_n) \in U_1 \cap U_2$ so
    
$$\begin{align}
c_1 w_1 + ... + c_n w_n = d_1 u_1 + ... + d_n u_n,
\end{align}$$
    
for some $d_1, ..., d_n$. But since the $u$'s and $w$'s are linearly independent, this can only hold if the $c$'s and $d$'s are all zero. Therefore 
    
$$\begin{align}
a_1 u_1 + ... + a_n u_n + b_1 v_1 + ... + b_n v_n = 0,
\end{align}$$
    
which again by linear independence can hold only if the $a$'s and $b$'s are all zero, arriving at the result.
    
</details>
<br>
    