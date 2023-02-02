# Linear maps 

This section deals with linear maps and their properties. Linear maps are functions which satisfy an additivity and a homogeneity property, and are the central topic of study of Linear Algebra. $ \newcommand{\L}{\mathcal{L}}
\newcommand{\null}{\text{null}~}
\newcommand{\range}{\text{range}~}
\newcommand{\dim}{\text{dim}~}
\newcommand{\span}{\text{span}}
\newcommand{\M}{\mathcal{M}} 
\newcommand{\F}{\mathbb{F}} $

(linalg-vector-space)=
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
    
- **Associativity:** Suppose $T_n \in \mathcal{L}(U_n, U_{n-1})$ for $n = 1, 2, 3$. Then
    
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
    
However, multiplication of linear maps is not commutative (even if the domains and ranges of the two linear maps are compatible), because in general function composition is not commutative. 

    
We also have the following lemma, which is unsurprising but useful for subsequent proofs.


<div class="lemma">

**Lemma (Linear maps take $0$ to $0$)** If $T \in \mathcal{L}(V, W)$, then $T(0) = 0$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Linear maps take \(0\) to \(0\)</summary>
    
We have
    
$$\begin{align}
T(0) = T(0 + 0) = T(0) + T(0) \implies T(0) = 0.
\end{align}$$

</details>
<br>

    
    

## Null spaces and ranges
    

This section introduces null spaces and ranges of linear maps. The null space and range of a linear map are closely related.
    
(linalg-inj-surj)=
### Injective and surjective
 
<div class="definition">

**Definition (Null space)** Suppose $T \in \mathcal{L}(V, W)$. Then the null space of $T$, denoted $\null T$ is
    
$$\begin{align}
\null T = \{v \in V : Tv = 0\}.
\end{align}$$
    
</div>
<br>
    
The null space of a linear map is a subspace of the domain-space of the map.

<div class="lemma">

**Lemma (Null space is a subspace)** Suppose $T \in \mathcal{L}(V, W)$. Then $\null T$ is a subspace of $V$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Null space is a subspace</summary>
    
Suppose $T \in \mathcal{L}(V, W)$. Then $\null T$ is closed under addition and scalar multiplication. It also contains the zero element, so it fulfills the {ref}`criteria for being a subspace<linalg-subspaces>`.

</details>
<br>
    
    

<div class="definition">

**Definition (Injective map)** A function $T : V \to W$ is called injective if
    
$$\begin{align}
Tu = Tv \implies u = v.
\end{align}$$
    
</div>
<br>
    

<div class="lemma">

**Lemma (Injective $\iff$ $\null~T = \{0\}$)** Suppose $T \in \mathcal{L}(V, W)$. Then $T$ is injective if and only if $\null T = \{0\}$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Injective \(\iff\) \(\null~T = \{0\}\)</summary>
    
Suppose $T \in \mathcal{L}(V, W)$. If $T$ is injective, then
    
$$\begin{align}
Tw = 0 \implies Tv + Tw = Tv \forall v \in V,
\end{align}$$
    
and since $T$ is injective we have
    
$$\begin{align}
v + w = v, \implies w = 0,
\end{align}$$
    
so $Tv = Tw \implies v = w$ implies $\null T = \{0\}$. Conversely if $\null T = \{0\}$, then
    
$$\begin{align}
Tv = Tw \implies T(v - w) = 0 \implies v = w,
\end{align}$$
    
so $\null T = \{0\}$ implies $Tv = Tw \implies v = w$.

</details>
<br>
    
    
<div class="definition">

**Definition (Range)** Suppose $T \in \mathcal{L}(V, W)$. Then the null space of $T$, denoted $\range T$ is
    
$$\begin{align}
\range T = \{Tv : v \in V\}.
\end{align}$$
    
</div>
<br>
    

<div class="lemma">

**Lemma (Range is a subspace)** Suppose $T \in \mathcal{L}(V, W)$. Then $\text{range}~T$ is a subspace of $W$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Range is a subspace</summary>
    
Suppose $T \in \mathcal{L}(V, W)$. Then $\range T$ is closed under additions and scalar multiplication. It also contains the zero element, so it fulfills the {ref}`criteria for being a subspace<linalg-subspaces>`.

</details>
<br>
    
    
<div class="definition">

**Definition (Surjective map)** A function $T : V \to W$ is called surjective if
    
$$\begin{align}
\range T = W.
\end{align}$$
    
</div>
<br>
    
(linalg-fund-linear)=
### Theorem of linear maps
    
<div class="theorem">

**Theorem (Fundamental theorem of linear maps)** Suppose $V$ is finite dimensional and $T \in \mathcal{L}(V, W)$. Then $\range T$ is finite dimensional and
    
$$\begin{align}
\dim V = \dim \null T + \dim \range T.
\end{align}$$
    
</div>
<br>


<details class="proof">
<summary>Proof: Fundamental theorem of linear maps</summary>
    
Suppose $V$ is finite dimensional and $T \in \mathcal{L}(V, W)$. Then $\null T$ is a subspace of $V$ and is {ref}`also finite dimensional<linalg-indep>`. Let $u_1, ..., u_m$ be a basis of $\null T$ and $u_1, ..., u_m, v_1, ..., v_n$ be its extension to a basis of $V$. Then if $w \in \range T$ we have
    
$$\begin{align}
Tv = w, \text{ for some } v \in V \implies T(a_1 u_1 + ... + a_m u_m + b_1 v_1 + ... + b_n v_n) = T(b_1 v_1 + ... + b_n v_n).
\end{align}$$
    
Therefore any $w \in \range T$ can be written as a linear combination of the vectors $Tv_1, ..., Tv_n$, implying that $\range T = \span(Tv_1, ..., Tv_n)$. Therefore we have $\dim \null T = m$ and $\dim \range T = n$, as well as $\dim V = n + m$, arriving at
    
$$\begin{align}
\dim V = \dim \null T + \dim \range T.
\end{align}$$

</details>
<br>
    
    
### Dimensions
    

<div class="lemma">

**Lemma (Map to fewer dimensions is not injective)** Suppose $V$ and $W$ are finite-dimensional vector spaces with $\dim V > \dim W$. Then no linear map from $V$ to $W$ is injective.
    
</div>
<br>


<details class="proof">
<summary>Proof: Map to fewer dimensions is not injective</summary> 
    
Suppose $V$ and $W$ are finite-dimensional vector spaces with $\dim V > \dim W$, and let $T \in \mathcal(V, W)$. By the {ref}`fundamental theorem of linear maps<linalg-fund-linear>`, we have
    
$$\begin{align}
\dim V &= \dim \null T + \dim \range T \implies \\
\dim \null T &= \dim V - \dim \range T \\
             &> \dim V - \dim W \\
             &> 0,
\end{align}$$
    
so $\dim \null T > 0$ which {ref}`implies<linalg-inj-surj>` $T$ is not injective.

</details>
<br>
    
    

<div class="lemma">

**Lemma (Map to more dimensions is not surjective)** Suppose $V$ and $W$ are finite-dimensional vector spaces with $\dim V < \dim W$. Then no linear map from $V$ to $W$ is surjective.
    
</div>
<br>


<details class="proof">
<summary>Proof: Map to more dimensions is not surjective</summary>
    
Suppose $V$ and $W$ are finite-dimensional vector spaces with $\dim V < \dim W$, and let $T \in \mathcal(V, W)$. By the {ref}`fundamental theorem of linear maps<linalg-fund-linear>`, we have
    
$$\begin{align}
\dim V &= \dim \null T + \dim \range T \implies \\
\dim \range T &= \dim V - \dim \null T \\
              &< \dim W - \dim \null T \\
              &< \dim W,
\end{align}$$
    
hence we cannot have $\range T = W$ and $T$ is not surjective.

</details>
<br>
    

<div class="lemma">

**Lemma (Homogeneous system of linear of linear equations)** A homogeneous system of linear equations
    
$$\begin{align}
\sum_{k = 1}^K A_{j, k} x_k = 0, j = 1, ..., J,
\end{align}$$
    
with more variables $K$ than equations $J$, has nonzero solutions.
    
</div>
<br>


<details class="proof">
<summary>Proof: Homogeneous system of linear of linear equations</summary>
    
Define the map $T : \F^K \to \F^J$ as
    
$$\begin{align}
(Tx)_j = \sum_{k = 1}^K A_{j, k} x_k,
\end{align}$$
    
for $x \in \F^m$. If $K > J$, then $T$ is a map to a space of fewer dimensions and is thus not injective, which implies its null space contains elements other than the zero element.

</details>
<br>


<div class="lemma">

**Lemma (Inhomogeneous system of linear of linear equations)** An inhomogeneous system of linear equations
    
$$\begin{align}
\sum_{k = 1}^K A_{j, k} x_k = b_j, j = 1, ..., J,
\end{align}$$
    
with more equations $J$ than variables $K$, has no solution for some choice of the constants $b_j$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Inhomogeneous system of linear of linear equations</summary>
    
Define the map $T : \F^K \to \F^J$ as
    
$$\begin{align}
(Tx)_j = \sum_{k = 1}^K A_{j, k} x_k,
\end{align}$$
    
for $x \in \F^m$. If $J > K$, then $T$ is a map to a space of more dimensions and is thus not surjective. This means there exists $w \in \F^J$ such that $w \not \in \range T$ and so $Tv \neq w$ for any $v \in \F^K$

</details>
<br>
    
    
## Matrices
    
<div class="definition">

**Definition (Matrix)** An $m \times n$ matrix $A$ is an array of elements of $\F$ with $n$ rows and $m$ columns
    
$$\begin{align}
A = \begin{pmatrix}
A_{1, 1} & \dots & A_{1, m} \\
\vdots   & \ddots & \vdots   \\
A_{n, 1} & \dots & A_{n, m}
\end{pmatrix},
\end{align}$$
    
where $A_{j, k}$ denotes the entry in row $j$, column $k$ of $A$. We use $\F^{n \times m}$ to denote the set of all $n \times m$ matrices, with entries in $\F$.
    
</div>
<br>
    
    
<div class="definition">

**Definition (Matrix of a linear map)** Suppose $T \in \L(V, W)$ and let $v_1, ..., v_n$ and $w_1, ..., w_n$ be bases of $V$ and $W$ respectively. Then the matrix of $T$with respect to these bases is the $n \times m$ matrix $\M(T)$ whose entries $M_{j, k}$ satisfy

$$\begin{align}
Tv_k = A_{1, k} w_1 + ... + A_{n, k} w_n.
\end{align}$$
    
</div>
<br>
    
    
<div class="definition">

**Definition (Matrix addition)** The sum of two matrices is the matrix obtained by adding the two matrices entry-wise
    
$$\begin{align}
(A + B)_{j, k} = A_{j, k} + B_{j, k}.
\end{align}$$
    
</div>
<br>


<div class="lemma">

**Lemma (Matrix of sum of maps)** If $T, S \mathcal{L}(V, W)$, then

$$\begin{align}
\mathcal{M}(T + S) = \mathcal{M}(T) + \mathcal{M}(S),
\end{align}$$

where both all matrices are with respect to the same bases.

</div>
<br>

    
<details class="proof">
<summary>Proof: Matrix of sum of maps</summary>
    
Suppose $T, S \in \mathcal{L}(V, W)$, let $v_1, ..., v_n$ and $w_1, ..., w_n$ be bases of $V$ and $W$ respectively, and let $\mathcal{M}(\cdot)$ denote the matrix of a linear map with respect to these bases. Let also $A = \M(T), B = \M(S)$. Since $T, S$ are linear, they satisfy
    
$$\begin{align}
(T + S)v_k &= Tv_k + Sv_k \\
           &= (A_{1, k} + B_{1, k}) w_1 + ... + (A_{n, k} + B_{n, k}) w_n
\end{align}$$
    
Therefore writing $C = \M(T + S)$ we have
    
$$\begin{align}
C_{j, k} &= A_{j, k} + B_{j, k}.
\end{align}$$

</details>
<br>
    
    
<div class="definition">

**Definition (Scalar multiplication of a matrix)** The scalar multiple of a matrix $A$ by a scalar $\lambda \in \F$ is the matrix whose entries are the corresponding entries of $A$ multiplied by $\lambda$
    
$$\begin{align}
(\lambda A)_{j, k} = \lambda A_{j, k}.
\end{align}$$
    
</div>
<br>
    

<div class="lemma">

**Lemma (Matrix of a scalar multiple of a map)** Suppose $\lambda \in \F$ and $T \in \L(V, W)$. Then $\M(\lambda T) = \lambda \M(T)$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Matrix of a scalar multiple of a map</summary>
    
Suppose $\lambda \in \F$ and $T \in \L(V, W)$. Let $v_1, ..., v_n$ and $w_1, ..., w_n$ be bases of $V$ and $W$ respectively, and let $\mathcal{M}(\cdot)$ denote the matrix of a linear map with respect to these bases. Then
    
$$\begin{align}
(\lambda T)v_k &= \lambda (Tv_k) \\
               &= (\lambda A_{1, k}) w_1 + ... + (\lambda A_{n, k}) w_n
\end{align}$$
    
and writing $C = \M(\lambda T)$, which we see that
    
$$\begin{align}
C_{j, k} = \lambda A_{j, k}.
\end{align}$$

</details>
<br>
    
    

<div class="lemma">

**Lemma (Dimension of $\F^{n \times m}$)** With matrix addition and scalar multiplication as defined above, $\F^{n \times m}$ defines a vector space with dimension $n \times n$.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Dimension of \(\F^{n \times m}\)</summary>
    
Consider the collection of $nm$ matrices, which have all zero entries except for a single $1$. Let $M_{i, k}$ denote one of these matrices with its $1$ entry at $(j, k)$. These matrices span $\F^{n \times m}$ because any matrix in the space can be written as a linear combination of them. The $M_{i, k}$ matrices are also linearly independent so they are a basis of $\F^{n \times m}$, of length $nm$, so $\dim \F^{n \times m}  = nm$.

</details>
<br>

    
<div class="definition">

**Definition (Matrix multiplication)** Suppose $A$ is an $n \times m$ matrix and $B$ is an $m \times k$ matrix. We define $AB$ to be the matrix
    
$$\begin{align}
(AB)_{j, k} = \sum_{l = 1} A_{j, l}  B_{l, k}.
\end{align}$$
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Matrix of product of linear maps)** If $T \L(U, V)$ and $S \in \L(V, W)$, then $\mathcal{M}(TS) = \mathcal{M}(T)\mathcal{M}(S)$.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Matrix of product of linear maps</summary>
    
Let $T \L(U, V)$ and $S \in \L(V, W)$. Let also $u_1, ..., u_N$ be a basis of $U$, $v_1, ..., v_M$ be a basis of $V$ and $w_1, ..., w_L$ be a basis of $W$, and $\mathcal{M}(T) = A, \mathcal{M}(S) = B$. Then
    
$$\begin{align}
(TS)u_n &= S\left( \sum_{k = 1}^K B_{k, n} v_k \right), \\
        &= \sum_{k = 1}^K B_{k, n} Sv_k, \\
        &= \sum_{k = 1}^K B_{k, n} \sum_{l = 1}^L A_{l, k} w_l, \\
        &= \sum_{l = 1}^L \left( \sum_{k = 1}^K A_{l, k} B_{k, n} \right) w_l,
\end{align}$$
    
and therefore
    
$$\begin{align}
\mathcal{M}(TS)_{l, n} &= \sum_{k = 1}^K A_{l, k} B_{k, n}.
\end{align}$$

</details>
<br>
    
    
<div class="lemma">

**Lemma (Entry of product is row times column)** Suppose $A$ is an $n \times m$ matrix and $B$ is an $m \times k$ matrix. Then
    
$$\begin{align}
(AB)_{j, k} = A_{j, \cdot} B_{\cdot, k}.
\end{align}$$
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Entry of product is row times column</summary>

From the definition of matrix multiplication we have

$$\begin{align}
(AB)_{n, k} &= \sum_{r = 1}^m A_{n, r} B_{r, k}  \\
            &= A_{j, \cdot} B_{\cdot, k}.
\end{align}$$

</details>
<br>
    
    
<div class="lemma">

**Lemma (Column of product is matrix times column)** Suppose $A$ is an $n \times m$ matrix and $B$ is an $m \times k$ matrix. Then
    
$$\begin{align}
(AB)_{\cdot, k} = A B_{\cdot, k}.
\end{align}$$
    
</div>
<br>

<details class="proof">
<summary>Proof: Column of product is matrix times column</summary>
    
From the definition of matrix multiplication we have

$$\begin{align}
(AB)_{\cdot, k} &= \left( \sum_{r = 1}^m A_{n, r} B_{r, k}  \right)_{n = 1}^N  \\
                &= A B_{\cdot, k}.
\end{align}$$

</details>
<br>


(linalg-inv-iso)=
## Invertibility and Isomorphism
    
<div class="definition">

**Definition (Invertible map, inverse)** The map $T \in \L (V, W)$ is invertible if there exists $S \in \L (W, V)$ such that $ST$ and $TS$ equal the identity map, defined on $V$ and $W$. The map $S$ is called the inverse of $T$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Inverse is unique)** Suppose $T \in \L (V, W)$ is an invertible linear map. Then the inverse of $T$ is unique. We write $T^{-1}$ to denote this unique inverse.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Inverse is unique</summary>
    
Suppose $T \in \L (V, W)$ is an invertible linear map, and let $S_1, S_2 \in \L (W, V)$ be inverses of $T$. Then
    
$$\begin{align}
S_1 T = I = S_2 T \implies S_1 T S_1 = S_2 T S_1 \implies S_1 = S_2.
\end{align}$$

</details>
<br>
    
    
<div class="lemma">

**Lemma (Invertible $\iff$ injective, surjective)** A linear map is invertible if and only if it is injective and surjective.
    
</div>
<br>

<details class="proof">
<summary>Proof: Invertible \(\iff\) injective, surjective</summary>
    
Suppose $T \in \L (V, W)$ is a linear map. If $T$ is injective and surjective, then we can define $T^{-1}$ as

$$\begin{align}
T^{-1}w = v, \text{ where } w = Tv.
\end{align}$$
    
This map is well defined because for any $w \in W$ there exists a $v \in V$ such that $w = Tv$, because $T$ is surjective, and further this $w$ is unique, because $T$ is injective. Further $T^{-1}$ is linear because:
    
$$\begin{align}
T^{-1}(w) = v \implies w = Tv, T^{-1}(\lambda w) = v' \text{ where } \lambda w = Tv' \implies v' = \lambda v,
\end{align}$$
    
hence $T^{-1}(\lambda w) = \lambda v$, and also
    
$$\begin{align}
T^{-1}(w_1) = v_1,  T^{-1}(w_2) = v_2 \implies w_1 + w_2 = T(v_1 + v_2), T^{-1}(w_1 + w_2) = v' \text{ where } w_1 + w_2 = Tv' \implies v_1 + v_2 = w_1 + w_2,
\end{align}$$
    
where in the last part we have used the surjectivity and linearity of $T$. Now suppose instead that $T$ is invertible. Then $T$ must be injective, because if it were not, its inverse would not be well defined. It must also be surjective because otherwise $T T^{-1}$ could not equal the identity.

</details>
<br>
    
    
<div class="definition">

**Definition (Isomorphism)** An isomorphim is an invertible linear map. Two vector spaces are called isomorphic if there exists an isomorphism from one to the other.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Isomorphic spaces $\iff$ same dimension)** Two finite dimensional vector spaces are isomorphic if and only if they have the same dimension.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Isomorphic spaces \(\iff\) same dimension</summary>
    
Let $U, V$ be finite dimensional vector and let $u_1, ..., u_n$ and $v_1, ..., v_m$ be bases of $U$ and $V$ respectively. If $n = m$, we can define $T \in \L (U, V)$ as
    
$$\begin{align}
Tu_j = v_j, i = 1, ..., n.
\end{align}$$
    
The map $T$ is injective, because $u_1, ..., u_n$ and $v_1, ..., v_n$ are linearly independent. Also $T$ is surjective because any $v \in V$ can be written as a linear combination of $v_1, ..., v_n$, and this linear combination can in turn be written in the form $T(u_1 + ... + u_n)$.

</details>
<br>
    
    
<div class="lemma">

**Lemma ($\L(V, W)$ and $\mathbb{F}^{n \times m}$ are isomorphic)** Let $v_1, ..., v_n$ and $w_1, ..., w_m$ be bases of $V$ and $W$. Then $\M$ with respect to these bases is an isomorphism from $\L(V, W)$ to $\mathbb{F}^{n \times m}$.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: \(\L(V, W)\) and \(\mathbb{F}^{n \times m}\) are isomorphic</summary>
    
Let $v_1, ..., v_n$ and $w_1, ..., w_m$ be bases of $V$ and $W$. First, $\M$ is injective because its null space is $\{0\}$ since
    
$$\begin{align}
\M(T) = 0 \implies Tv = 0 \text{ for all } v \in V \implies T = 0.
\end{align}$$
    
Second, $\M$ is surjective because for any $A \in \mathbb{F}^{n \times m}$ we can define $T \in \L(V, W)$
    
$$\begin{align}
Tv_k = \sum_{j = 1}^n A_{j, k} w_j,
\end{align}$$
    
for which we have $\M(T) = A$, so $\M$ is surjective. Since $T$ is injective and surjective it is invertible.

</details>
<br>
    

    
    
<div class="lemma">

**Lemma (Dimension of space of linear maps)** Suppose $V$ and $W$ are finite-dimensional. Then

$$\begin{align}
\dim \L(V, W) = \dim V \dim W.
\end{align}$$
    

    
</div>
<br>

    
<details class="proof">
<summary>Proof: Dimension of space of linear maps</summary>
    
Suppose $V$ and $W$ are finite-dimensional, with dimensions $n$ and $m$. We know that $\L(V, W)$ and $\mathbb{F}^{n \times m}$ are isomorphic, and that isomorphic spaces must have the same dimension. Since the dimension of $\mathbb{F}^{n \times m}$ is $nm$, and the dimensions of $\dim V$ and $\dim W$ are $n$ and $m$ respectively, we have

$$\begin{align}
\dim \L(V, W) = \dim V \dim W.
\end{align}$$
    
</details>
<br>
    
<div class="definition">

**Definition (Matrix of a vector)** Suppose $v \in V$ and $v_1, ..., v_n$ is a basis of $V$. The matrix of $v$ with respect to this basis is

$$\begin{align}
\M(v) = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}, \text{ where } v = c_1 v_1 + ... + c_n v_n.
\end{align}$$
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Column of linear map is a basis vector)** If $T \in \L(V, W)$ and $v_1, ..., v_k$ and $w_1, ..., w_k$ are bases of $V$ and $W$ respectively, then $\M(T)_{\cdot, k} = \M(v_k)$.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Column of linear map is a basis vector</summary>
    
This follows immediately from the definitions of $\M(T)$ and $\M(v_k)$.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Linear maps act like matrix multiplication)** Suppose $T \in \L(V, W)$ and $v \in V$, and also that $v_1, ..., v_n$ and $w_1, ..., w_n$ are bases of $V$ and $W$. Then

$$\begin{align}
\M(Tv) = \M(T) \M(v)
\end{align}$$
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Linear maps act like matrix multiplication</summary>
    
Suppose $T \in \L(V, W)$ and $v \in V$, and also that $v_1, ..., v_n$ and $w_1, ..., w_n$ are bases of $V$ and $W$. Then

$$\begin{align}
v = c_1 v_1 + ... + c_n v_n \implies Tv = c_1 Tv_1 + ... + c_n Tv_n,
\end{align}$$
    
and by the linearity of $\M$
    
$$\begin{align}
\M(Tv) = c_1 \M(Tv_1) + ... + c_n \M(Tv_n) = c_1 \M(T)_{\cdot, 1} + ... + c_n \M(T)_{\cdot, n} = \M(T) \M(v).
\end{align}$$
    
</details>
<br>
    
    
<div class="definition">

**Definition (Operator $\L(V)$)** A linear map from a vector space $V$ to itself is called an operator. We use the notation $\L(V)$ for the set of all operators on $V$, $\L(V, V)$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Finite dimensional $T$ invertible $\iff$ $T$ injective $\iff$ $T$ surjective)** Suppose $V$ is a finite dimensional vector space and $T \in \L(V)$. Then the following are equivalent
    
$$\begin{align}
T \text{ is invertible } \iff T \text{ is injective } \iff T \text{ is surjective}.
\end{align}$$
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Finite dimensional \(T\) invertible \(\iff\) \(T\) injective \(\iff\) \(T\) surjective</summary>
    
First, $T$ is invertible if and only if it is injective and surjective. Second, if $T$ is injective its null space must be $\{0\}$ so
    
$$\begin{align}
\dim \range T = \dim V - \dim \null T = \dim V,
\end{align}$$
    
so $T$ is surjective. Lastly, if $T$ is surjective, its range must be $V$ so
    
$$\begin{align}
\dim \null T = \dim V - \dim \range T = 0,
\end{align}$$
    
so $T$ is also injective, and therefore invertible. This suffices to show that all three statements are equivalent.


</details>
<br>

    
<!---
Products of vector spaces 
-->

## Products of vector spaces

<div class="definition">

**Definition (Product of vector spaces)** Suppose $V_1, \dots, V_m$ are vector spaces over $\F$. The product $V_1 \times \dots \times V_m$ is defined by
    
$$\begin{align}
V_1 \times \dots \times V_m = \{(v_1, \dots, v_m) : v_1 \in V_1, \dots, v_m \in V_m\},
\end{align}$$
    
with addition on this space defined as
    
$$\begin{align}
(u_1, \dots, u_m) + (v_1, \dots, v_m) = (u_1 + v_1, \dots, u_m + v_m),
\end{align}$$
    
and scalar multiplication defined as
    
$$\begin{align}
\alpha (u_1, \dots, u_m) = (\alpha u_1, \dots, \alpha u_m).
\end{align}$$
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Product of vector spaces is a vector space)** Suppose $V_1, \dots, V_m$ are vector spaces $\F$. Then $V_1 \times \dots \times V_m$ is a vector space over $\F$.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Product of vector spaces is a vector space </summary>
    
Under the definition given above, a product of vector spaces satisfies the {ref}`properties for being a vector space<linalg-vectorspace>`.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Dimension of product is sum of dimensions)** Suppose $V_1, \dots, V_m$ are finite dimensional vector spaces. Then their product is finite dimensional and
    
$$\begin{align}
\dim(V_1 \times \dots \times V_m) = \dim(V_1) + \dots + \dim(V_m).
\end{align}$$
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Dimension of product is sum of dimensions </summary>
    
Since all the vector spaces are finite dimensional, we can choose a basis for each one. For each of the vector spaces, say $V_i$ consider its basis $v_{j1}, \cdot, v_{jd_j}$ and the vectors in the product space
    
$$\begin{align}
(0, \cdots, 0, v_{j1}, 0, \cdots, 0)&
\vdots &
(0, \cdots, 0, \underbrace{v_{jd_j}}_{j^{th} \text{ slot}}, 0, \cdots, 0) &.
\end{align}$$
    
Considering the set of all such vectors, we see that they are linearly independent and that they span the product space, so they are a basis for it. Counting the length of this list we see that
    
$$\begin{align}
\dim(V_1 \times \dots \times V_m) = \dim V_1 + \dots + \dim V_m.
\end{align}$$

</details>
<br>
    
    
    
<div class="lemma">

**Lemma (Products and direct sums)** Suppoose that $U_1, \dots, U_m$ are subspaces of $V$ and define the linear map $\Gamma : U_1 \times \dots \times U_m \to U_1 + \dots + U_m$ by
    
$$\begin{align}
\Gamma(u_1, \dots, u_m) = u_1 + \dots + u_m.
\end{align}$$
    
Then $U_1 + \dots + U_m$ is a direct sum if and only if $\Gamma$ is injective.
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Products and direct sums </summary>
    
By its definition, the linear map $\Gamma$ is injective if and only if
    
$$\begin{align}
u_1 + \dots + u_m = 0 \implies u_1, \dots, u_m = 0.
\end{align}$$
    
Since $U_1 + \dots + U_m$ is a direct sum if and only if the same condition holds, we arrive at the result.

</details>
<br>
    
    

<div class="lemma">

**Lemma (Direct sum $\iff$ dimensions add up)** Suppoose $U_1, \dots, U_m$ are subspaces of the finite-dimensional space $V$. Then $U_1 + \dots + U_m$ is a direct sum if and only if
    
$$\begin{align}
\dim (U_1 + \dots + U_m) = \dim U_1 + \dots + \dim U_m.
\end{align}$$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Direct sum \(\iff\) dimensions add up </summary>
    
The $\Gamma$ map defined earlier is surjective. By the fundamental theorem of linear maps, $\Gamma$ is injective if and only if
    
$$\begin{align}
\dim (U_1 \times \dots \times U_m) = \dim (U_1 + \dots + U_m).
\end{align}$$
    
By the previous lemma, we see that $U_1 + \dots + U_m$ is a direct sum if and only if
    
$$\begin{align}
\dim (U_1 + \dots + U_m) = \dim U_1 + \dots + \dim U_m.
\end{align}$$

</details>
<br>
    
    
<!---
Quotients of vector spaces 
-->

## Quotients of vector spaces

<div class="definition">

**Definition (Sum of vector and subspace)** Suppose $v \in V$ and $U$ is a subspace of $V$. Then $v + U$ is the subset of $V$ defined as
    
$$\begin{align}
v + U = \{v + u : u \in U\}.
\end{align}$$
    
</div>
<br>

    
<div class="definition">

**Definition (Affine subset)** We call any subset of $V$ that can be written in the form $v + U$, for some $v \in V$ and some subspace $U$ of $V$, an affine subset. We say the affine subset $v + U$ is parallel to $U$.
    
</div>
<br>

    
<div class="definition">

**Definition (Quotient space)** Suppose $U$ is a subspace of $V$. Then the quotient space $V / U$ is tthe set of all affine subsetts of $V$ parallel to $U$. In other words
    
$$\begin{align}
V / U = \{v + U : v \in V\}.
\end{align}$$
    
</div>
<br>
    
The name quotient space is motivated by the fact that if $U, V$ are vector spaces, then 
    
$$\begin{align}
(U \times V) / (\{0\} \times V) \text{ and } U \text{ are isomorphic}.
\end{align}$$
    
So in this sense, the quotient of a space by another has the opposite meaning to the product of two spaces.
    

<div class="lemma">

**Lemma (Affine subsets parallel to $U$ are equal or disjoint)** Suppose $U$ is a subspace of $V$ and $v, w \in V$. Then the following conditions are equivalent
    
1. $v - w \in U,$
2. $v + U = w + U,$
3. $(v + U) \cap (w + U) \neq \emptyset.$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Affine subsets parallel to \(U\) are equal or disjoint </summary>

Suppose the first statement holds. If $u \in U$, then
    
$$\begin{align}
v + u = w + ((v - w) + u) \in w + U,
\end{align}$$
    
so $v + U \subseteq w + U$. Similarly $w + U \subseteq v + U$ and so $v + U = w + U$. Now if the second condition holds, the third condition also holds. Lastly, if the third condition holds, then letting $W = (v + U) \cap (w + U)$ we see that there exist $u_1, u_2$ such that $v + u_1 = w + u_2$ so
    
$$\begin{align}
v + u_1 = w + u_2 \implies v - w = (u_2 - u_1) \in U,
\end{align}$$
    
showing the first condition holds. Thus the three conditions are equivalent.

</details>
<br>
    
    
We can define addition and scalar multiplication on elements of $V / U$ in the following way.
    
    
<div class="definition">

**Definition (Addition and scalar multiplication on $V / U$)** Suppose $U$ is a subspace of $V$. TThen addition and scalar multiplication are defined on $V / U$ by
    
$$\begin{align}
(v + U) + (w + U) &= (v + w) + U, \\
\lambda (v + U) &= (\lambda v) + U,
\end{align}$$
    
where $v, w \in V$ and $\lambda \in \mathbb{F}$.
    
</div>
<br>
    
<details class="proof">
<summary>Detail: Addition and scalar multiplication on \(V / U\)</summary>
    
One detail related to this definition is that an affine subset $v + U$ may have multiple representations, because if $\hat{v} = v + u, u \in U$, then we have $v + U = \hat{v} + U$. We would therefore like to show that addition and scalar multiplication are well defined, in the sense that we get the same result no matter which representation we use.
    
In particular, suppose that $v + U = \hat{v} + U$ and $w + U = \hat{w} + U$ and $\lambda \in \mathbb{F}$. Since $v + U = \hat{v} + U$, we have $v - \hat{v} \in U$, and similarly $w - \hat{w} \in U$. Then
    
$$\begin{align}
(v - \hat{v}) + (w - \hat{w}) \in U \implies (v + w) - (\hat{v} + \hat{w}) \in U \implies (v + w) + U = (\hat{v} + \hat{w}) + V.
\end{align}$$
    
Similarly, we have
    
$$\begin{align}
(v - \hat{v}) \in U \implies \lambda (v - \hat{v}) \in U \implies \lambda v - \lambda \hat{v} \in U \implies (\lambda v) + U = \lambda \hat{v} + U.
\end{align}$$

</details>
<br>
    
    
With these definitions of addition and scalar multiplication, $V / U$ constitutes a vector space.
    
<div class="lemma">

**Lemma (Quotient space is a vector space)** Suppose $U$ is a subspace of $V$. Then $V / U$, with addition and scalar multiplication as defined above is a vector space.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Quotient space is a vector space</summary>
    
By the definition of $V / U$ and the definitions of addition and scalar multiplication on $V / U$, we see that $V / U$ satisfies {ref}`all requirements<linalg-vectorspace>` for being a vector space.

</details>
<br>
    
Now, for convenience, we define the quotient map $\pi$ which, for a given $U$, maps vectors to corresponding affine subsets $v + U$.
    
<div class="definition">

**Definition (Quotient map)** Suppose $U$ is a subspace of $V$. The quotient map $\pi$ is the linear map $\pi : V \to V / U$ defined by
    
$$\begin{align}
\pi(v) = v + U,
\end{align}$$
    
for $v \in V$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Dimension of a quotient space)** Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$. Then
    
$$\begin{align}
\text{dim} V / U = \text{dim} V - \text{dim} U
\end{align}$$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Dimension of a quotient space</summary>
    
Using the fundamental theorem of linear algebra on $\pi$ we have
    
$$\begin{align}
\text{dim} V / U = \text{dim range} \pi + \text{dim null} \pi.
\end{align}$$

</details>
<br>
    
    
    
<div class="definition">

**Definition ($\tilde{T}$ map on $V / (\null {T})$)** Suppose $T \in \mathcal{L}(V, W)$. We define $\tilde{T} : V / (\null T) \to W$ by
    
$$\begin{align}
\tilde{T}(v + \null T) = Tv.
\end{align}$$
    
</div>
<br>
    
    
<details class="proof">
<summary>Detail: \(\tilde{T}\) map on \(V / (\null {T})\)</summary>
    
As with scalar addition and multiplication on $V / U$, here too we might worry about whether or not $\tilde{T}$ is well-defined. In particular, suppose $u, v \in V$. Then

$$\begin{align}
u + (\null T) = v + (\null T) \implies u - v \in \null T \implies \tilde{T} (u + \null{T}) = \tilde{T} (v + \null{T}),
\end{align}$$

which shows that $\tilde{T}$ is well defined.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Null space and range of $\tilde{T}$)** Suppose $T \in \mathcal{L}(V, W)$. Then the following hold
    
- $\tilde{T}$ is a linear map from $V / (\null T)$ to $W$.
- $\tilde{T}$ is injecive.
- $\range \tilde{T} = \range T$.
- $V / (\null T)$ is isomorphic to $\range T$.

</div>
<br>
    
    
<details class="proof">
<summary>Detail: Null space and range of \(\tilde{T}\)</summary>
    
First, $\tilde{T}$ satisfies the requirements for being a linear map, namely additivity and homogeneity, so it is a linear map.
    
Second, to show that $\tilde{T}$ is injective, suppose $\tilde{T} (v + \null T) = 0$ for some $v$. Then $Tv = 0$ which implies $v \in \null T$ so $v + \null T = 0 + \null T$. Therefore $0 + \null T = 0$ where the first zero is in $V$ and the second zero is in $V / (\null T)$. Thus $\tilde{T}$ is injective.
    
Third, to show that $\range \tilde{T} = \range T$, it suffices to consider the definition of $\tilde{T}$.
    
Last, from the previous two results, if we define $\tilde{T}$ to be a map from $V / (\null T)$ to $\range T$, then $\tilde{T}$ is injective, and also surjective, so it is an isomorphism.

</details>
<br>
    

(linalg-duality)=
## Duality
    
    
<div class="definition">

**Definition (Linear functional)** A linear functional on $V$ is a linear map from $V$ to $\mathbb{F}$. In other words, it is an element of $\mathcal{L}(V, \mathbb{F})$.
    
</div>
<br>
    
    
<div class="definition">

**Definition (Dual space)** The dual space of $V$, written $V'$, is the vector space of all linear functionals on $V$, that is $V' = \mathcal{L}(V, \mathbb{F})$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma ($\dim V = \dim V'$)** Suppose $V$ is finite dimensional. Then $V'$ is also finite-dimensional and $\dim V = \dim V'$.

</div>
<br>
    
    
<details class="proof">
<summary>Detail: \(\dim V = \dim V'\)</summary>
    
Suppose $V$ is finite dimensional. Then, {ref}`as shown above<linalg-inv-iso>`, the following holds
    
$$\begin{align}
\dim \mathcal{L}(V, W) = (\dim V) (\dim W) \implies \dim \mathcal{L}(V, \mathbb{F}) = (\dim V) (\dim \mathbb{F}) = \dim V.
\end{align}$$

</details>
<br>    
    
    
<div class="definition">

**Definition (Dual basis)** If $v_1, \dots, v_n$ is a basis of $V$, then the dual basis of $v_1, \dots, v_n$ is the list $\phi_1, \dots, \phi_n$ of elements of $V'$ where
    
$$\begin{align}
\phi_j(v_k) = \begin{cases}
1 & \text{ if } k = j, \\
0 & \text{ if } k \neq j.
\end{cases}
\end{align}$$
    
</div>
<br>
    
    
<details class="proof">
<summary>Detail: Dual basis is well defined</summary>
    
One detail we might want to check is that given a basis $v_1, \dots, v_n$ of $V$, the dual basis $\phi_1, \dots, \phi_n$ of $V'$ exists. We have {ref}`already shown<linalg-vector-space>` that given two vector spaces $V$ with basis $v_1, \dots, v_n$ and $W$ is another vector space with $w_1, \dots, w_n \in W$, there exists a unique linear map such that

$$\begin{align}
Tv_i = w_i, \text{ for } i = 1, \dots, n.
\end{align}$$
    
Then for given $j \in \{1, \dots, n\}$, we can label $T = \phi_j$, let $W = \mathbf{F}$ and set
    
$$\begin{align}
w_k = \begin{cases}
1 & \text{ if } k = j, \\
0 & \text{ if } k \neq j,
\end{cases}
\end{align}$$
    
confirming that $\phi_j$ does exist and is unique.
    
</details>
<br>   
    
    
<div class="lemma">

**Lemma (Dual basis is a basis)** Suppose $v_1, \dots, v_n$ is a basis of $V$. Then the dual basis $\phi_1, \dots, \phi_n$ is a basis of $V'$.

</div>
<br>
    
    
<details class="proof">
<summary>Detail: Dual basis is a basis of the dual space</summary>
    
Suppose $v_1, \dots, v_n$ is a basis of $V$ and $\phi_1, \dots, \phi_n$ be the corresponding dual basis. Suppose there exist $c_1, \dots, c_n$ such that
    
$$\begin{align}
\phi = c_1 \phi_1 + \dots + c_n \phi_n = 0.
\end{align}$$
    
Then we have
    
$$\begin{align}
\phi = c_1 \phi_1(v_i) + \dots + c_n \phi_n(v_i) = 0, \text{ for } i = 1, \dots, n
\end{align}$$
    
which implies that $\phi$ is zero for all elements in $\text{span}(v_1, \dots, v_n) = V$. Therefore $\phi$ is the zero map $\phi = 0 \in \mathcal{L}(V, \mathbb{F})$ which in turn implies that the $\phi_1, \dots, \phi_n$ are all linearly independent. Since the $\phi_1, \dots, \phi_n$ are a linearly independent list of the correct length ($\dim V = \dim V'$), they constitute a basis for $V'$.
    
</details>
<br>
    
    
<div class="definition">

**Definition (Dual map)** If $T \in \mathcal{L}(V, W)$, then its dual map $T' \in \mathcal{L}(W', V')$ is
    
$$\begin{align}
T'(\phi) = \phi \circ T,
\end{align}$$
    
where $\phi \in W'$.
    
</div>
<br>
    
The following figure helps illustrate the various relationships between dual linear maps and vector spaces.
    
<img alt="Dual map" src="../../../_images/duality-commutative.png" class="center-image">
    
While $T$ acts on $v \in V$ to produce $w \in W$, the dual map $T'$ acts on $\phi \in W'$ to produce $\psi = \phi \circ T \in V'$.


<div class="lemma">

**Lemma (Properties of dual maps)** Let $S, T \in \mathcal{L}(V, W)$. Then any dual maps $S', T' \in \mathcal{L}(W', V')$ satisfy
    
- $(S + T)' = S' + T'$.
- $(\lambda S)' = \lambda S'$ for all $\lambda \in \mathbb{F}$.
- $(ST)' = T'S'$.

</div>
<br>
    
    
<details class="proof">
<summary>Proof: Properties of dual maps</summary>
    
Let $S, T \in \mathcal{L}(V, W)$. Then by definition, for each $\phi \in W'$
    
$$\begin{equation}
(S + T)'(\phi) = \phi \circ (S + T) =  \phi \circ S + \phi \circ T = S'(\phi) + T'(\phi).
\end{equation}$$
    
Similarly, for each $\phi \in W'$ and $\lambda \in \mathbb{F}$, we have

$$\begin{equation}
(\lambda S)'(\phi) = \phi \circ (\lambda S) =  \lambda \phi \circ S = \lambda S'(\phi).
\end{equation}$$
    
Lastly, for each $\phi \in W'$, we have

$$\begin{equation}
(ST)'(\phi) = \phi \circ (ST) = \phi \circ S \circ T = S'(\phi) \circ T = T' S'(\phi).
\end{equation}$$
    
</details>
<br>
    
    
<div class="definition">

**Definition (Annihilator)** For $U \subseteq V$, the annihilator of $U$, denoted $U^0$, is defined as
    
$$\begin{equation}
U^0 = \{\phi \in V' : \phi(u) = 0 \text{ for all } u \in U \}.
\end{equation}$$
    
</div>
<br>

    
    
    
<div class="lemma">

**Lemma (Annihilator is a subspace)** Suppose $U \subseteq V$. Then $U^0$ is a subspace of $V'$.

</div>
<br>
    
    
<details class="proof">
<summary>Proof: Annihilator is a subspace</summary>
    
Suppose $U \subseteq V$. Then $U^0$ contains $0 \in V'$ because
        
$$\begin{equation}
0(u) = 0 \implies 0 \in U^0.
\end{equation}$$
    
Further, $U^0$ is closed under multiplications and additions of its elements, because for any $\phi, \psi \in U^0$ and any $\lambda \in \mathbb{F}$ we have
    
$$\begin{align}
(\lambda \phi)(u) &= \lambda \phi(u) = 0 \implies \phi + \psi \in U^0, \\
(\phi + \psi)(u) &= \phi(u) + \psi(u) = 0 + 0 = 0 \implies \phi + \psi \in U^0.
\end{align}$$
    
</details>
<br>
    
    
    
<div class="lemma">

**Lemma (Dimension of the annihilator)** Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$. Then
    
$$\begin{equation}
\dim U + \dim U^0 = \dim V.
\end{equation}$$

</div>
<br>
    

<details class="proof">
<summary>Proof: Dimension of the annihilator</summary>
    
Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$. Then there exists a basis $u_1, \dots, u_m$ for $U$, which can be extended to a basis $u_1, \dots, u_m, \dots, u_n$ of $V$. Now consider the dual basis of $u_1, \dots, u_m, \dots, u_n$, written $\phi_1, \dots, \phi_m, \dots, \phi_n$.
    
Suppose $\phi \in U^0$. Writing $\phi$ as a linear combination of the dual basis
    
$$\begin{equation}
\phi = c_1 \phi_1 + \dots + c_m \phi_m + \dots + c_n \phi_n,
\end{equation}$$
    
we see that for $k = 1, \dots, m$, we have

$$\begin{equation}
\phi(u_k) = c_1 \phi_1(u_k) + \dots + c_m \phi_m(u_k) + \dots + c_n \phi_n(u_k) = c_k = 0,
\end{equation}$$
    
which means that $\phi$ can be written as a linear combination of $\phi_{m+1}, \dots, \phi_n$, which shows that $U^0 \subseteq \span(\phi_1, \dots, \phi_m)$. Conversely, if $\phi$ can be written as a linear combination of $\phi_{m+1}, \dots, \phi_n$, then for $k = 1, \dots, m$, we have
    
$$\begin{equation}
\phi(u_k) = c_m \phi_m(u_k) + \dots + c_n \phi_n(u_k) = 0,
\end{equation}$$
    
which implies that $\phi(u) = 0$ for all $u \in U$.
    
</details>
<br>
    
    
    
<div class="lemma">

**Lemma (Null space of $T'$)** Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. Then
    
- $\null T' = (\range T)^0$.
- $\dim \null T' = \dim \null T + \dim W - \dim V$.

</div>
<br>
    

<details class="proof">
<summary>Proof: Null space of \(T'\)</summary>

Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. If $\phi \in \null T'$, then
    
$$\begin{equation}
T'(\phi) = \phi \circ T = 0.
\end{equation}$$
    
So for all $v \in V$ we have $\phi \circ T v = 0$. This means that if $w \in \range T$, then $\phi(w) = 0$. Therefore if $\phi \in \null T'$ then $\phi \in (\range T)^0$, so $\null T' \subseteq (\range T)^0$. Conversely, if $\phi \in (\range T)^0$, then $\phi(w) = 0$ for all $w \in \range T$, which implies that
    
$$\begin{equation}
(T'(\phi))(v) = \phi \circ T(v) = 0,
\end{equation}$$
    
for all $v \in V$. This means that $\phi \in \null T'$ so $(\range T)^0 \subseteq \null T'$. This concludes the proof that $\null T' = (\range T)^0$.
    
Also, we have
    
$$\begin{align}
\dim \null T' &= \dim (\range T)^0, \\
              &= \dim W - \dim \range T, \\
              &= \dim W - (\dim V - \dim \null T), \\
              &= \dim \null T + \dim W - \dim V.
\end{align}$$

    
</details>
<br>
    
    
    
<div class="lemma">

**Lemma ($T$ is surjective $\iff$ $T'$ is injective)** Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. Then $T$ is surjective if and only if $T'$ is injective.

</div>
<br>
    

<details class="proof">
<summary>Proof: \(T\) is surjective \(\iff\) \(T\) is injective</summary>

Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. From the previous lemma, we have
    
$$\begin{equation}
\dim \null T' = \dim W - \dim \range T.
\end{equation}$$
    
If $T$ is surjective, then $\range T = W \implies \dim \range T = \dim W$, so $\dim \null T' = 0$, so $T'$ is injective. Conversely, if $T'$ is injective, then $\dim \null T' = 0$, so $\dim \range T = \dim W$ and, since $\range T \subseteq W$, this can only occur if $\range T = W$, which means that $T$ is surjective.
    
</details>
<br>
    
    
<div class="lemma">

**Lemma (The range of $T'$)** Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. Then
    
- $\range T' = (\null T)^0$.
- $\dim \range T' = \dim \range T$.

</div>
<br>
    

<details class="proof">
<summary>Proof: The range of \(T'\)</summary>

Let $V$ and $W$ be finite-dimensional and $T \in \mathcal{L}(V, W)$. First, it holds that $\dim \range T' = \dim \range T$ because
    
$$\begin{align}
\dim \range T' &= \dim W' - \dim \null T' \\
               &= \dim W' - \dim (\range T)^0 \\
               &= \dim \range T,
\end{align}$$
    
which shows the second result. Now, suppose $\phi \neq 0 \in \range T'$. Then there exists $\psi \in W'$ such that $\phi = T'(\psi)$. Now if $v \in \null T$, then $\phi(v) = 0$ because if not, then we would have
    
$$\begin{equation}
(T'(\psi))(v) \neq 0 \implies \psi \circ T v \neq 0
\end{equation}$$
    
which is a contradiction because we have assumed $v \in \null T$. Therefore $\phi(v) = 0$ for all $v \in \null T$, so $\phi \in (\null T)^0$, which implies that $\range T' \subseteq (\null T)^0$. Further, we have
    
$$\begin{align}
\dim \range T' &= \dim \range T \\
               &= \dim V - \dim \null T \\
               &= \dim (\null T)^0.
\end{align}$$

Therefore, since $\range T' \subseteq (\null T)^0$ and $\dim \range T' = \dim (\null T)^0$, the two vector spaces must be equal, so $\range T' = (\null T)^0$.
    
</details>
<br>
    
    
    
<div class="lemma">

**Lemma ($T$ is injective $\iff$ $T'$ is surjective)** Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. Then $T$ is injective if and only if $T'$ is surjective.

</div>
<br>
    

<details class="proof">
<summary>Proof: \(T\) is injective \(\iff\) \(T\) is surjective</summary>

Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. From the previous lemma, we have
    
$$\begin{equation}
\dim \range T' = \dim \range T = \dim V - \dim \null T = \dim V' - \dim \null T.
\end{equation}$$
    
If $T$ is injective, then $\dim \null T = 0$ and $\dim \range T' = \dim V'$ so $T'$ is surjective. Conversely, if $T'$ is surjective, then $\dim \range T' = \dim V' = \dim V$ so $\dim \null T = 0$ which is equivalent to $T$ being injective.
    
</details>
<br>


<div class="definition">

**Definition (Transpose)** The transpose of an $n$ by $m$ matrix $A$, denoted $A^\top$, is the $m$ by $n$ matrix obtained by interchanging the rows and columns of $A$, that is
    
$$\begin{equation}
(A^\top)_{j, i} = A_{i, j}, \text{ for } i = 1, \dots, n \text{ and } j = 1, \dots, m.
\end{equation}$$
    
</div>
<br>
    
    
    
<div class="lemma">

**Lemma (Transpose of product of matrices)** Let $A$ be an $n$ by $m$ matrix and $B$ be a $m$ by $k$ matrix. Then
    
$$\begin{equation}
(AB)^\top = B^\top A^\top.
\end{equation}$$

</div>
<br>

<details class="proof">
<summary>Proof: Transpose of product of matrices</summary>

Let $A$ be an $n$ by $m$ matrix and $B$ be a $m$ by $k$ matrix. Then
    
$$\begin{equation}
(AB)_{ij} = \sum_{k = 1}^m A_{ik} B_{kj} \implies ((AB)^\top)_{ij} = \sum_{k = 1}^m A_{jk} B_{ki} = \sum_{k = 1}^m (A^\top)_{kj} (B^\top)_{ik} = (B^\top A^\top)_{ij}.
\end{equation}$$
    
</details>
<br>
    
