# Linear maps 


## Vector space of linear maps

Linear maps are one of the central objects of linear algebra. As the name suggests, linear maps are linear functions between vector spaces.

<div class="definition">

**Definition (Linear map)** A linear map is a function $T : V \to W$ with the following properties
    
- **Additivity:** $ T(u + v) = T(u) + T(v)$
- **Homogeneity:** $ T(\lambda u) = \lambda T(u)$
    
for all $u, v \in V$ and $\lambda \in \mathbb{F}$. We write $\mathcal{L}(V, W)$ to denote the set of all linear maps from $V$ to $W$.
    
</div>
<br>

The values that a linear map takes are completely determined by the values it takes on a basis in its domain. Therefore, definining the values that a linear map takes on this basis fully characterises the whole linear map, making it unique.

<div class="lemma">

**Lemma (Uniqueness and existence of linear maps)** Suppose $v_1, ..., v_n$ is a basis of $V$ and $w_1, ..., w_n \in W$. Then there exists a unique linear map such that
    
$$\begin{align}
T v_j = w_j,~~j = 1, ..., n.
\end{align}$$
    
</div>
<br>


<details class="proof">
<summary>Proof: Uniqueness and existence of linear maps</summary>

Let $T : V \to W$ be the map
    
$$\begin{align}
T(c_1 v_1 + ... + c_n v_n) = c_1 w_1 + ... + c_n w_n,
\end{align}$$
    
which is a valid definition since all elements $v \in V$ can be uniquely expressed in the form
        
$$\begin{align}
v = c_1 v_1 + ... + c_n v_n.
\end{align}$$
    
We observe that the map $T$ is linear. Now setting $c_j = 1$ and $c_k = 0$ for all $k \neq j$ we see that the map satisfies
    
$$\begin{align}
T v_j = w_j,~~j = 1, ..., n.
\end{align}$$
    
To show that the map is unique, suppose $S \in \mathcal{L}(V,W)$ and that $Sv_j = w_j,~~j = 1, ..., n$. Then by the linearity and homogeneity of $S$ we have
    
$$\begin{align}
S(c_1 v_1 + ... + c_n v_n) = c_1 w_1 + ... + c_n w_n,
\end{align}$$
    
which means that $S = T$ on all of $\text{span}(v_1, ..., v_n) = V$, so $S$ and $T$ are identical.

</details>
<br>


<div class="definition">

**Definition (Addition and multiplication on $\mathcal{L}(V, W)$)** Suppose $S, T \in \mathcal{L}(V, W)$ and $\lambda \in \mathcal{F}$. We define the sum $S + T$ and product $\lambda T$ as
    
$$\begin{align}
(S + T)(v) &= Sv + Tv,\\
(\lambda T)(v) &= \lambda (Tv),
\end{align}$$
    
for all $v \in V$.
    
</div>
<br>

<div class="lemma">

**Lemma ($\mathcal{L}(V, W)$ is a vector space)** Under the definitions of addition and multiplication for linear operators, the set $\mathcal{L}(V, W)$ of linear operators from $V$ to $W$ is a vector space.
    
</div>
<br>


<details class="proof">
<summary>Proof: \(\mathcal{L}(V, W)\) is a vector space</summary>
    
We note that under the definitions for addition and scalar multiplication given above, $\mathcal{L}(V, W)$ satisfies {ref}`the requirements for being a vector space<linalg-vectorspace>`.

</details>
<br>

Above we defined the scalar multiple of a linear map. We can also define the product of two linear maps to be their composition, provided the range of one is compatible with the domain of the other.

<div class="definition">

**Definition (Product of linear maps)** If $T \in \mathcal{L}(U, V)$ and $S \in \mathcal{L}(V, W)$, then the product $ST \in \mathcal{L}(U, W)$ is defined as
    
$$\begin{align}
(ST)(u) = S(Tu).
\end{align}$$
    
</div>
<br>
    
Products of linear maps satisfy the following useful properties.
    
    
<div class="lemma">

**Lemma (Properties of products of linear maps)** Products of linear maps satisfy the following properties
    
- **Associativity:** Suppose $T_n \in \mathcal{L}(U_{n+1}, U_{n})$ for $n = 1, 2, 3$. Then
    
$$\begin{align}
(T_1 T_2) T_3 = T_1 (T_2 T_3)
\end{align}$$
    
- **Identity:** Suppose $T \in \mathcal{L}(U, V)$ and let $I_U, I_V$ be the identity maps on $U$ and $V$ respectively. Then
    
$$\begin{align}
T I_U = I_V T = T.
\end{align}$$
    
- **Distributive property:** Suppose $T, T_1, T_2 \in \mathcal{L}(U, V)$ and $S, S_1, S_2 \in \mathcal{L}(V, W)$. Then
    
$$\begin{align}
(S_1 + S_2) T = S_1 T + S_2 T, \text{ and } S (T_1 + T_2) = ST_1 ST_2.
\end{align}$$
 
</div>
<br>


<details class="proof">
<summary>Proof: Properties of products of linear maps</summary>
    
**Associativity:** Suppose $T_n \in \mathcal{L}(U_{n+1}, U_{n})$ for $n = 1, 2, 3$, and let $u \in U_3$. Then
    
$$\begin{align}
(T_1 T_2) T_3 u = (T_1 T_2) (T_3 u) = T_1 (T_2 (T_3 u)) = T_1 ((T_2 T_3) u)
\end{align}$$
    
which implies $(T_1 T_2) T_3 = T_1 (T_2 T_3)$.
    
**Identity:** This holds by inspection of the expression $T I_U = I_V T = T$.
    
**Distributive property:** Suppose $T, T_1, T_2 \in \mathcal{L}(U, V)$ and $S, S_1, S_2 \in \mathcal{L}(V, W)$ and let $u \in U$. Then

$$\begin{align}
(S_1 + S_2) (T u) = S_1 (T u) + S_2 (T u) = (S_1 T + S_2 T) u,
\end{align}$$
    
which implies $(S_1 + S_2) T = S_1 T + S_2 T$. Similarly, we have
    
$$\begin{align}
S ((T_1 + T_2) u) = S (T_1 u + T_2 u) = S (T_1 u + T_2 u) = S T_1 u + S T_2 u = (S T_1 + S T_2) u,
\end{align}$$
    
which implies $S (T_1 + T_2) = ST_1 ST_2$.
    
</details>
<br>
    
However, multiplication of linear maps is not commutative (even if the domains and ranges of the two linear maps are compatible), because in general function composition is not commutative. We conclude this section with the following unsurprising lemma on linear maps, which is useful for subsequent proofs.


<div class="lemma">

**Lemma (Linear maps take $0$ to $0$)** If $T \in \mathcal{L}(V, W)$, then $T(0) = 0$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Linear maps take \(0\) to \(0\)</summary>
    
We have
    
$T(0) = T(0 + 0) = T(0) + T(0) \implies T(0) = 0.$

</details>
<br>
