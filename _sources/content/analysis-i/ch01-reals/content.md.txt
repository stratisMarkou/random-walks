# The real numbers

This section is concerned with defining the real numbers. To do so, we define fields, totally ordered sets and ordered fields, upper (lower) bounds and the upper (lower) properties. The real numbers are defined indirectly, in terms of these objects and properties.

## Fields

Analysis deals with properties of objects like sequences, series, functions, derivatives and integrals defined with respect to the real or the complex numbers. We therefore need to define the real numbers. Instead of doing so directly however, we define an object called a *field*, which has all the necessary properties on which to do analysis, and the reals can be shown to be an example of a field.

<div class="definition">

**Definition (Field)** A field is a set $\mathbb{F}$ with two binary operations $+$ and $\times$ which satisfy the following properties
        
1. For any $a, b, c \in \mathbb{F}$, $a + (b + c) = (a + b) + c$ and $a \times (b \times c) = (a \times b) \times c$.
2. For any $a, b \in \mathbb{F}$, $a + b = b + a$ and $a \times b = b \times a$.
3. There exist $0, 1 \in \mathbb{F}$ such that for any $a \in \mathbb{F}$, $a + 0 = a$ and $a \times 1 = a$.
4. For any $\mathbb{a} \in \mathbb{F}$, there exists $-a \in \mathbb{F}$ such that $a + (-a) = 0$. If $a \neq 0$, then for any $\mathbb{a} \in \mathbb{F}$, there exists $a^{-1} \in \mathbb{F}$ such that $a \times a^{-1} = 1$.
5. For any $a, b, c \in \mathbb{F}$, $a \times (b + c) = (a \times b) + (a \times c)$.
    
</div>
<br>

Another component for defining the reals is that of the ordering operations. A set together with an ordering operation is called an ordered set, and with some additional requirements it becomes a totally ordered set.

<div class="definition">

**Definition (Totally ordered set)** A totally ordered set $S$ is a set together with a relation $<$ that satisfies
    
1. If $x, y, z \in S$, $x < y$ and $y < z$, then $x < z$.
2. If $x, y \in S$, exactly one of $x < y$, $x = y$ or $x > y$ holds.
    
</div>
<br>

An ordered set, has the property that at most one of $x < y$, $x = y$ or $x > y$ holds - but it is not necessary for any of the three comparisons to hold. Bringing together the definition of the field and the ordered set, we arrive at the definition of an ordered field.


<div class="definition">

**Definition (Ordered field)** An ordered field is a set $\mathbb{F}$ with a relation that makes $\mathbb{F}$ into an ordered set such that
    
1. If $x, y, z \in \mathbb{F}$, $x < y$ then $x + z < y + z$.
2. If $x, y, z \in \mathbb{F}$, $x < y$ and $z > 0$ then $xz < yz$.
    
</div>
<br>

Below is our first result, a property satisfied by ordered fields.

<div class="lemma">

**Lemma (Squares are non-negative)** Let $\mathbb{F}$ be an ordered field and $x \in \mathbb{F}$. Then $x^2 \geq 0$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Squares are non-negative</summary>

Let $x \in \mathbb{F}$ and $x \in \mathbb{F}$. Exactly one of $x = 0$, $x < 0$ or $x > 0$ holds, and we consdider them separately.
    
In the first case

$$\begin{align}
x = 0 \implies x^2 = 0 \implies x^2 \geq 0.
\end{align}$$

In the second case
    
$$\begin{align}
x > 0 \implies x^2 > 0.
\end{align}$$

In the third case, 
 
$$\begin{align}
x < 0 \implies x + (-x) < 0 + (-x) \implies 0 < -x, \text{ hence }(-x)^2 = x^2 > 0.
\end{align}$$
    
concluding the proof. In case one really wants to show that $(-x)^2 = x^2$, here's one way. Consider 
 
$$\begin{align}
x + (-x) = 0 \implies x^2 + (-x)x = 0
\end{align}$$
    
and also that
    
$$\begin{align}
x + (-x) = 0 \implies (-x)x + (-x)^2 = 0.
\end{align}$$
    
Combining these two identities we obtain $x^2 = (-x)^2.$ We can sleep peacefully.

</details>
<br>

(analysis-i-least-upper-bound)=
## Least upper bound property

Another central concept in analysis is the upper (lower) bound and the least (greatest) upper (lower) bound. Among other uses, these are used to define the real numbers themselves.

<div class="definition">

**Definition (Upper bound and supremum)** Let $S$ be an oredered field and $A \subseteq S$. An upper bound for $A$ is an element $x \in S$ such that $a \leq x$ for all $a \in A$, and if such $a$ exists we say $A$ is bounded above. The upper bound $x$ is a supremum (or least upper bound) if for all $a < x$, there exists $b \in A$ such that $b < a$.
    
</div>
<br>

The last component for defining the real numbers is the least upper bound property.

<div class="definition">

**Definition (Least upper bound property)** An ordered set $S$ has the least upper bound property if every non-empty subset of $S$ that is bounded from above has a supremum.
    
</div>
<br>

Equivalent definitions for the lower bound, infimum and greatest lower bound property can be made in the obvious way.

<div class="definition">

**Definition (Lower bound, infimum and greatest lower bound property)** The obvious modification, switching the $\leq$ to $\geq$ and the $<$ to $>$ in the definitions for the upper bound, supremum and least upper bound property, gives the definitions for the lower bound, infimum and greatest lower bound property.
    
</div>
<br>

(analysis-i-real-num)=
## The real numbers

We are now at a position to define the real numbers in terms of an ordered field. One can check that such an object exists, and that the decimals satisfy the properties stated in the definition, but we do not do this here.

<div class="definition">

**Definition (Real numbers)** The real numbers is an ordered field with the least upper bound property.
    
</div>
<br>

The second result of the course is the archimedean property, stated and proved below.

<div class="lemma">

**Lemma (Archimedean property)** Let $\mathbb{F}$ be an ordered field with the least upper bound property. Then the set $\{1, 2, 3, ...\}$ - that is the sequence obtained by starting from the $1$ element and applying the operation $+ 1$ -, is not bounded above.
    
</div>
<br>


<details class="proof">
<summary>Proof: Archimedean property</summary>

If $\{1, 2, 3, ...\}$ has an upper bound, it must also have a least upper bound $x$ by the least upper bound property. Since $x$ is a least upper bound, $x - 1$ is not a least upper bound so there exists $n > x - 1$. Therefore $n + 1 > x$ and $x$ is not an upper bound, reaching a contradiction.

</details>
<br>