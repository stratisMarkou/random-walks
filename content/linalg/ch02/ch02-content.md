# Finite dimensional vector spaces

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

**Span is a subspace:** First, $\{0\} \in \mathbb{F}$ since $0$ is a linear combination of the vectors $v_1, ..., v_n$. Second, $S$ is closed under additions because if $s_1, s_2 \in S$ then $s_1, s_2$ are linear combinations of $v_1, ..., v_n$ and also $s_1 + s_2$ is a linear combination of $S$. Lastly, if $s \in S$ then also $\lambda s \in \mmathbb{F}$ because $s$ is a linear combination of $v_1, ..., v_n$ and the $\lambda$ coefficient can be absorbed in the coefficients of the linear combination. Therefore $S$ satisfies {ref}`the three necessary and sufficient conditions for being a subspace<linalg-subspaces>`.
    
    
**Span is the smallest containing subspace:** This holds because any subspace $U \subseteq V$ which contains the vectors $v_1, ..., v_n$ must also contain all of their linear combinations. Since all the elements in $S$ are linear combinations of the vectors $v_1, ..., v_n$ we have $S \subseteq U$.
    
    
</details>
<br>



<div class="definition">

**Definition (Vector list spans $V$)** We say that a list of vectors $v_1, ..., v_n$ spans $V$ if
    
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

The list $u_1, w_1, ..., w_n$ is linearly dependent, but by the Linear Dependence Lemma we can remove one of the $w$'s from it and it will still span $V$. We can proceed by inserting $u_2$ after $u_1$ in the list, to obtain a new list whose first two entries are $u_1, u_2$ and the rest are $w$'s to get another linearly dependent list. Again by the Linear Dependence Lemma, we can remove one of the $w$'s from the list to obtain a list that still spans $V$. Proceeding iteratively, we can insert all the $u$'s to the list while removing $w$'s - at each step, we can guarantee that a $w$ and not a $u$ will be removed, because the initial $u$-vectors in the list are all linearly independent - until all the $u$'s have been added to the list.

At each step of the above process, the Linear Dependence Lemma implies that there is a $w$ term to remove and thus $m \leq n$.
    
</details>
<br>
    

<div class="lemma">

**Lemma (Finite dimensional subspace)** Any subspace of a finite dimensional vector space is finite dimensional.
    
</div>
<br>


<details class="proof">
<summary>Proof: Finite dimensional subspace</summary>

Let $V$ be a finite dimensional space with subspace $U \subseteq V$. Then there exists a list $v_1, ..., v_n$ which spans $V$.
    
If $U = \{0\}$, then $U$ is finite dimensional. Suppose $U \neq \{0\}$. Then there exists a nonzero $u_1 \in U$. If $u_1$ spans $U$ then $U$ is finite dimensional. If not, there exists $u_2 \in U$ such that $u \not \in \span(u_1)$. If $u_1, u_2$ spans $U$ then again $U$ is finite dimensional. We can proceed in this iterative fashion until a list $u_1, ..., u_m$ is found which spans $U$. If no such list is found, the length of this linearly independent list will eventually exceed the length of the spanning list $v_1, ..., v_n$. But since any linearly independent list cannot have a length greater than a spanning list, this procedure must terminate for some $m \leq n$. Therefore $U$ is finite dimensional.
    
</details>
<br>