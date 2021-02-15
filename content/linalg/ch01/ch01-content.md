# Vector spaces

## Complex numbers

It's assumed that the reader is already familiar with the real numbers $\mathbb{R}$, but not necessarily with the complex numbers $\mathbb{C}$, defined below.

<div class="definition">

**Definition (Complex numbers)** A complex number is an oredered list $(a, b)$ where $a, b \in \mathbb{R}$, written as $a + bi$. The set of complex numbers is denoted by $\mathbb{C}$. Addition and multiplication on $\mathbb{C}$ are denoted as
    
$$\begin{align}
(a + bi) + (c + di) &= (a + c) + (b + d)i, \\
(a + bi)(c + di) &= (ac - bd) + (bc + ad)i. \\
\end{align}$$
    
</div>
<br>

We often abbreviate $a + 0i$ as $a$ and $0 + bi$ as $bi$. In what follows, we will often write $\mathbb{F}$ to denote either $\mathbb{R}$ or $\mathbb{C}$. Multiplication and addition in the complex numbers satisfy the familiar properties that multiplication and addition of in the real numbers do.

<div class="lemma">

**Lemma (Properties of complex arithmetic)** Addition and multiplication of complex numbers satisfy:
    
- **Commutativity:** $a + b = b + a$ and $ab = ba$ for all $a, b \in \mathbb{C}$.
- **Associativity:** $(a + b) + c = a + (b + c)$ and $(ab)c = a(bc)$ for all $a, b, c \in \mathbb{C}$.
- **Identities:** $a + 0 = a$ and $a \cdot 1 = a$ for all $a\in \mathbb{C}$.
- **Additive inverses:** For every $a \in \mathbb{C}$, there exists unique $b \in \mathbb{C}$ such that $a + b = 0$
- **Multiplicative inverses:** For every nonzero $a \in \mathbb{C}$, there exists unique $b \in \mathbb{C}$ such that $\frac{a}{b} = 1$.
- **Distributive property:** $(a + b)c = ac + bc$ for all $a, b, c \in \mathbb{C}$.
    
</div>
<br>



<div class="definition">

**Definition (Subtraction and division)** Let $a, b \in \mathbb{C}$. We then
    
- Write $-a$ for the additive inverse of $a$ and define subtractionn on $\mathbb{C}$ by
    
$$ b - a = b + (-a). $$
    
- Write $\frac{1}{a}$ for the mmultiplicative inverse of $a$ whenever $a \neq 0$ and define division on $\mathbb{C}$ by
    
$$ \frac{b}{a} = b \left(\frac{1}{a}\right). $$
    
</div>
<br>



<div class="definition">

**Definition (Powers)** For $a \in \mathbb{F}$ and $m \in \mathbb{N}^+$ we use $a^m$ to define the product
    
$$\begin{align}
a^m = \underbrace{a ... a}_{m \text{ times}},
\end{align}$$

and call this the $m^{th}$ power of $a$.
    
</div>
<br>



<div class="definition">

**Definition (List, length)** A list of length $n \in \mathbb{N}^0$ is an ordered collection of $n$ elements, written as
    
$$ (x_1, ..., x_n) $$
    
Two lists are equal if and only if they have the same length and the same elements in the same order. We sometimes ommit the parentheses and we write $()$ for the empty list of length $0$.
    
</div>
<br>


<div class="definition">

**Definition ($\mathbb{F}^n$)** We write $\mathbb{F}^n$ for the set of all lists of length $n$ of elements of $\mathbb{F}$. For $(x_1, ..., x_n) \in \mathbb{F}^n$ and $i \in \{1, ..., n\}$, we say that $x_i$ is the $i^{th}$ coordinate of $(x_1, ..., x_n)$.
    
</div>
<br>


<div class="definition">

**Definition (Addition in $\mathbb{F}^n$)** Addition in $\mathbb{F}^n$ is defined by adding corresponding coordinates
    
$$(x_1, ..., x_n) + (y_1, ..., y_n) = (x_1 + y_1, ..., x_n + y_n).$$
    
</div>
<br>

<div class="lemma">

**Lemma (Commutativity of addition in $\mathbb{F}^n$)** Addition in $\mathbb{F}^n$ is commutative
    
$$ x, y \in \mathbb{F}^n \implies x + y = y + x. $$
    
</div>
<br>


<div class="definition">

**Definition (Zero list)** We use $0$ to denote a list whose coordinates are all $0$. Distinguishing this symbol from the real number $0$ and determining the length of the list can be based on context.
    
</div>
<br>

<div class="definition">

**Definition (Additive inverse in $\mathbb{F}^n$)** For $x \in \mathbb{F}^n$, the additive inverse of $x$, denoted $-x$ is the vector $-x \in \mathbb{F}^n$ such that
    
$$ x + (-x) = 0. $$
    
</div>
<br>

<div class="definition">

**Definition (Scalar multiplication in $\mathbb{F}^n$)** For $\lambda \in \mathbb{F}$ and $x \in \mathbb{F}^n$, we define the multiple of $\lambda$ and $x$ to be the coordinate-wise product of $x$ with $\lambda$, that is
    
$$ \lambda x = (\lambda x_1, ..., \lambda x_n). $$
    
</div>
<br>

<div class="definition">

**Definition (Addition and scalar multiplication on sets)** We define addition and scalar multiplication on sets as
    
- **Addition:** a function which assigns an element $u + v \in V$ to each pair $u, v \in V$.
- **Scalar multiplication:** a function which assignsan element $\lambda v \in V$ to each $\lambda \in \mathbb{F}$ and $v \in V$.
    
</div>
<br>

## Vector spaces

<div class="definition">

**Definition (Vector space)** A vector space is a set $V$ together with an addition and scalar multiplication defined on $V$, such that the following properties hold:
    
- **Commutativity:** $u + v = v + u$ for all $u, v \in V$.
- **Associativity:** $(u + v) + w = u + (v + w)$ and $(ab)v = a(bv)$ for all $u, v, w \in V$ and $a, b \in \mathbb{F}$.
- **Additive identity:** there exists an element $0 \in V$ such that $v + 0 = v$ for all $v \in V$.
- **Additive inverse:** for every $v \in V$ there exists an element $w \in V$ such that $v + w = 0$.
- **Multiplicative identity:** $1 \cdot v = v$ for all $v \in V$.
- **Distributive proeprties:** $a (u + v) = au + av$ and $(a + b) v = av + bv$ for all $a, b \in \mathbb{F}$ and all $u, v \in V$.
    
Elements of a vector space are called *vectors* or *points*.
    
</div>
<br>



<div class="definition">

**Definition (Real and complex vector spaces)** A vector space over $\mathbb{R}$, meaning its scalars are in $\mathbb{R}$, is called a real vector space. A vector space over $\mathbb{C}$, meaning its scalars are in $\mathbb{C}$, is called a complex vector space.
    
</div>
<br>


In these notes we follow Axler and use the symbol $V$ to denote a vector space over $\mathbb{F}$ where $\mathbb{F} = \mathbb{R}$ or $\mathbb{F} = \mathbb{C}$.


<div class="definition">

**Definition (Notation $\mathbb{F}^S$)** If $S$ is a set, $\mathbb{F}^S$ denotes the set of functions from $S$ to $\mathbb{F}$.
    
- For $f, g \in \mathbb{F}^S$, the sum $f + g$ is defined as $(f + g)(x) = f(x) + g(x)$.
- For $\lambda \in \mathbb{F}$ and $f \in \mathbb{F}^S$, the product $\lambda f$ is defined as $(\lambda f)(x) = \lambda f(x)$.
    
</div>
<br>


<div class="lemma">

**Lemma (Unique additive identity/inverses)** A vector space has a unique additive identity. Every element in a vector space has a unique additive inverse.
    
</div>
<br>

<details class="proof">
<summary>Proof: Unique additive identity/inverses</summary>

Let $V$ be a vector space and $a, b \in V$ be additive identities in $V$. Then for any $v \in V$
    
$$\begin{align}
v + a = v = v + b
\end{align}$$
    
and adding the additive inverse of $v$ to both sides we obtain
    
$$\begin{align}
v + a + (-v) &= v + b + (-v) \\
a &= b
\end{align}$$
 
therefore the additive identity is unique. Now suppose that $w, z \in V$ are both additive inverses of $v$. Then we have
    
$$\begin{align}
v + w = 0 = v + z
\end{align}$$
    
and adding $w$ to both sides we obtain
    
$$\begin{align}
v + w + w &= v + z + w \\
w &= z
\end{align}$$
    
showing that additive inverses are unique.
    
</details>
<br>


<div class="lemma">

**Lemma (Multiplication by $0$)** For any $a \in \mathbb{F}, v \in V$, we have $0v = 0$ and $a0 = 0$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Multiplication by \(0\)</summary>

Let $a \in \mathbb{F}, v \in V$. Then by the definition of scalar multiplication in vector spaces we have
    
$$\begin{align}
0v &= (0 + 0)v = 0v + 0v \\
\implies 0v &= 0,
\end{align}$$
    
and by the definition of $0 \in V$ we have
    
$$\begin{align}
a0 &= a(0 + 0) = a0 + a0 \\
\implies a0 &= 0.
\end{align}$$
    
</details>
<br>


<div class="lemma">

**Lemma (Multiplication by $-1$)** We have $(-1)v = -v$ for every $v \in V$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Multiplication by \(-1\)</summary>

If $v \in V$, we then have
    
$$\begin{align}
(1 - 1)v = v + (-1) v = 0 \implies -v = (-1) v,
\end{align}$$
    
since additive inverses are unique.
    
</details>
<br>

(linalg-subspaces)=
### Subspaces

<div class="definition">

**Definition (Subspace)** A subset $U$ of $V$is a subspace of $V$ if $U$ is also a vector space with the same addition and scalar multiplication as $V$.
    
</div>
<br>


<div class="lemma">

**Lemma (Conditions for subspace)** A subset $U$ of $V$ is a subspace of $V$ if and only if $U$ satisfies
    
- **Additive identity:** $0 \in U$.
- **Closure under addition:** $u, w \in U$ implies $u + w \in U$.
- **Closure under multiplication:** $a \in \mathbb{F}$ and $u \in U$ implies $au \in U$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Conditions for subspace</summary>

If $U$ is a subspace, then it satisfies all three properties by the definition of a vector space.
    
If $U$ satisfies all three of the above properties, we can confirm that it also satisfies the properties for being a vector space, one by one:
    
- **Commutativity, associativity, multiplicative identity, distributive properties:** these are satisfied on $U$, because addition in $U$ is defined in the same way as in $V$ and $V$ is a vector space.
- **Additive identity:** the additive identity is in $U$ by the assumptions of the lemma.
- **Additive inverse:** for any element $v \in V$, its additive inverse $-v = (-1)v$ is in $V$ by the assumption of closure under multiplication.
    
</details>
<br>

<div class="definition">

**Definition (Sum of subsets)** Let $U_1, ..., U_n$ be subsets of $V$. We define the sum $U_1 + ... + U_n$ as the set
    
$$ U_1 + ... + U_n = \{u_1 + ... + u_m : u_1 \in U_1, ..., u_m \in U_m\}.$$
    
</div>
<br>


<div class="lemma">

**Lemma (Sum of sets is the smallest containing set)** Let $U_1, ..., U_n$ be subspaces of $V$. Then their sum $U_1 + ... + U_n$ is the smallest subspace of $V$ that contains them.
    
</div>
<br>


<details class="proof">
<summary>Proof: Sum of sets is the smallest containing set</summary>

Let $S$ be the smallest subspace of $V$ that contains $U_1, ..., U_n$. Since $S$ is a subspace, it {ref}`is closed under addition<linalg-subspaces>` so $S$ must contain all elements of the form
    
$$\begin{align}
u_1 + ... + u_n : u_1 \in U_1, ..., u_n \in U_n,
\end{align}$$
    
and must therefore contain $U_1 + ... + U_n$. Therefore $U_1 + ... + U_n \subseteq S$.
    
To show that $U_1 + ... + U_n$ is a subspace, we observe that it contains the additive identity, it is closed under addition and it is also closed under scalar multiplication. Therefore $U_1 + ... + U_n$ is a subspace concluding the proof that the sum of $U_1, ..., U_n$ is the smallest subspace containing them.
    
</details>
<br>
    
    
(linalg-direct-sum)=
### Direct sums


<div class="definition">

**Definition (Direct sum)** Let $U_1, ..., U_n$ be subspaces of $V$. The sum $U_1 + ... + U_n$ is called a direct sum if each element in the set can be written in only one way as a sum $u_1 + ... + u_n$. If $U_1 + ... + U_n$ is a direct sum, we use the notation $U_1 \oplus ... \oplus U_n$ to make this explicit.
    
</div>
<br>
    
 
<div class="lemma">

**Lemma (Direct sum $\iff$ unique writing of $0$)** Suppose $U_1, ..., U_n$ are subspaces of $V$. Then $U_1 + ... + U_n$ is a direct sum if and only if there is a unique way to write $0$ as the sum $u_1 + ... + u_n$ where $u_i \in U_i$, in which each $u_i = 0$.
    
</div>
<br>


<details class="proof">
<summary>Proof: Direct sum \(\iff\) unique writing of \(0\)</summary>

Suppose $U_1 + ... + U_n = U_1 \oplus ... \oplus U_n$ is a direct sum. By the {ref}`definition of the direct sum<linalg-direct-sum>`, there exists a single unique way to write $0$ as a sum of the form $u_1 + ... + u_n$ where $u_i \in U_i$.
    
Going the other way, suppose now there exists a unique way to write $0$ as the sum $u_1 + ... + u_n$ where $u_i \in U_i$, by setting $u_i = 0$. Now consider an element $v \in U_1 + ... + U_n$ and consider two ways of writing it
    
$$\begin{align}
u_1 + ... + u_n = w_1 + ... + w_n,
\end{align}$$
    
where $u_i, w_i \in U_i$. Then also $u_i - w_i \in U_i$, so rearranging we obtain
    
$$\begin{align}
(u_1 - w_1) + ... + (u_n - w_n) = 0,
\end{align}$$
  
and since by assumption there is one unique way to write $0$ as a sum of this form, we have
    
$$\begin{align}
u_i - v_i = 0 \implies u_i = v_i,
\end{align}$$
    
so the two ways of writing $v$ are identical.
    
</details>
<br>
    
 
<div class="lemma">

**Lemma (Direct sum $\iff$ intersection equals $\{0\}$)** Suppose $U$ and $W$ are subspaces of $V$. Then $U + W$ is a direct sum if and only if $U \cap W = \{0\}$.
    
</div>
<br>


<details class="proof">
<summary>Proof: (Direct sum \(\iff\) intersection equals \(\{0\}\)</summary>

Suppose $U + W = U \oplus W$ is a direct sum. Suppose $v \in U$ and $v \in W$. Then $v \in U \oplus W$ and there exist at least two ways of writing $v$ as the sum of the form
    
$$\begin{align}
u_1 + w_1 = u_2 + w_2,
\end{align}$$
    
where $u_1, u_2 \in U$ and $w_1, w_2 \in W$, which are by setting $u_1 = v, w_1 = 0$ or $u_2 = 0, w_2 = v$. This contradicts the assumption that $U + W$ is a direct sum.
    
Going the other way, suppose now that $U \cap W = \{0\}$. Then there exists a unique way to write $0$ as a sum of the form 
    
$$\begin{align}
u_1 + w_1 = u_2 + w_2 = 0,
\end{align}$$
    
where $u_1, u_2 \in U$ and $w_1, w_2 \in W$. Then rearranging we would obtain
    
$$\begin{align}
(u_1 - u_2) + (w_1 - w_2) = 0,
\end{align}$$
    
but since $U, W$ have no common elements, the only way to satisfy this equation is if $u_1 - u_2 = 0$ and also $w_1 - w_2 = 0$, which shows that the two ways of writing $0$ are identical. This shows that $U + W$ is a {ref}`direct sum<linalg-direct-sum>`.
    
</details>
<br>