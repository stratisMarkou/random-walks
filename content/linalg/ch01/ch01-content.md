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

**Definition (List)** A list of length $n \in \mathcal{N}^0$ is an ordered collection of $n$ elements, written as
    
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

**Definition (Additive inverse in $\mathcal{F}^n$)** For $x \in \mathcal{F}^n$, the additive inverse of $x$, denoted $-x$ is the vector $-x \in \mathcal{F}^n$ such that
    
$$ x + (-x) = 0. $$
    
</div>
<br>

