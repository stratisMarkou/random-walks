# Linear maps 

This section deals with linear maps and their properties. Linear maps are functions which satisfy an additivity and a homogeneity property, and are the central topic of study of Linear Algebra. $ \newcommand{\L}{\mathcal{L}}
\newcommand{\null}{\text{null}~}
\newcommand{\range}{\text{range}~}
\newcommand{\dim}{\text{dim}~}
\newcommand{\span}{\text{span}}
\newcommand{\M}{\mathcal{M}} 
\newcommand{\F}{\mathbb{F}} $

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

    
    

## Null spaces and ranges
    

This section introduces null spaces and ranges of linear maps. The null space and range of a linear map are closely related and central to the study of linear maps and vector spaces.
    
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

**Lemma (Injective $\iff$ $\text{null}~T = \{0\}$)** Suppose $T \in \mathcal{L}(V, W)$. Then $T$ is injective if and only if $\null T = \{0\}$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Injective \(\iff\) \(\text{null}~T = \{0\}\)</summary>
    
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

**Lemma (Matrix of product of linear maps)** If $T \L(U, V)$ and $S \in \L(V, W)$, then $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$.
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Entry of product is row times column)** Suppose $A$ is an $n \times m$ matrix and $B$ is an $m \times k$ matrix. Then
    
$$\begin{align}
(AB)_{j, k} = A_{j, \cdot} B_{\cdot, k}.
\end{align}$$
    
</div>
<br>
    
    
<div class="lemma">

**Lemma (Column of product is matrix times column)** Suppose $A$ is an $n \times m$ matrix and $B$ is an $m \times k$ matrix. Then
    
$$\begin{align}
(AB)_{\cdot, k} = A B_{\cdot, k}.
\end{align}$$
    
</div>
<br>

    
<div class="definition">

**Definition ()** 
    
</div>
<br>
    

    
    
    
    
    

    
    
<div class="definition">

**Definition ()** 
    
</div>
<br>
    
    
<div class="lemma">

**Lemma ()** 
    
</div>
<br>

    
<details class="proof">
<summary>Proof: </summary>

</details>
<br>


$$\begin{align}
\end{align}$$