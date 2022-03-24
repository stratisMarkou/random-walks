# The real numbers

In this section, we define fields, totally ordered sets, ordered fields, upper and lower bounds, and the upper and lower bound properties.
We then define the real numbers in terms of these eariler definitions.

## Fields

Analysis studies the properties of things like sequences, series, functions, derivatives and integrals defined with respect to the real or the complex numbers.
We therefore need to define the real numbers.
Instead of doing so directly however, we define an object called a *field*, which has all the necessary properties on which to do analysis.
The reals are an example of a field.

<div class="definition">

**Definition (Field)** A field is a set $\mathbb{F}$ with two binary operations $+$ and $\times$ which satisfy the following properties
        
1. **Commutativity:** For any $a, b, c \in \mathbb{F}$, $a + (b + c) = (a + b) + c$ and $a \times (b \times c) = (a \times b) \times c$.
2. **Associativity:** For any $a, b \in \mathbb{F}$, $a + b = b + a$ and $a \times b = b \times a$.
3. **Existence of identities:** There exist $0, 1 \in \mathbb{F}$ such that for any $a \in \mathbb{F}$, $a + 0 = a$ and $a \times 1 = a$.
4. **Existence of inverses:** For any $\mathbb{a} \in \mathbb{F}$, there exists $-a \in \mathbb{F}$ such that $a + (-a) = 0$. If $a \neq 0$, then for any $\mathbb{a} \in \mathbb{F}$, there exists $a^{-1} \in \mathbb{F}$ such that $a \times a^{-1} = 1$.
5. **Distributivity:** For any $a, b, c \in \mathbb{F}$, $a \times (b + c) = (a \times b) + (a \times c)$.
    
We sometimes ommit writing the $\times$ sign in which case, for example, $a \times b$ would be abbreviated as $ab$.
    
</div>
<br>

<details class="proof">
<summary>Note: Properties of addition and multiplication</summary>

It is interesting to note that under the first three conditions, addition and multiplication have the same standing, in the sense that they are both binary operations which satisfy commutativity, associativity and have identity elements.
Now, if we assume that inverses exist for addition and also require the distributivity property, we see that
    
$$\begin{equation}
a \times 0 + a = a \times 0 + a \times 1 = a \times (0 + 1) = a \times 1 = a \implies a \times 0 = 0.
\end{equation}$$
    
Now since $a \times 0 = 0$ for any $a$, we see that multiplication by $0$ is a many-to-one map, which is not invertible.
So that's why we exclude $0$ from the condition for the existence of inverses.
The distributivity property sets addition and multiplication apart.

</details>
<br>

Now we define ordering operations.
A set together with an ordering operation is called an ordered set.
With some additional requirements it becomes a totally ordered set.

<div class="definition">

**Definition (Ordered set, Totally ordered set)** An ordered set $S$ is a set together with a relation $<$ that satisfies
    
1. If $x, y, z \in S$, $x < y$ and $y < z$, then $x < z$.
2. If $x, y \in S$, at most one of $x < y$, $y < x$ or $x = y$ holds.
    
An ordered set $S$ is a called a totally ordered set if for any $x, y \in S$, exactly one of $x < y$, $y < x$ or $x = y$ holds.
We define $x > y \iff x < y$, $x \leq y \iff x < y, \text{ or } x = y$ and $x \geq y \iff x > y, \text{ or } x = y$.
    
</div>
<br>

Note that the equality sign in this definition means that the two elements are the same element.
Therefore, a totally ordered set is a set where if neither $x < y$ nor $y > x$ holds, then $x$ and $y$ must be the same element.
Bringing together the definitions of fields and ordered sets, we obtain ordered fields.


<div class="definition">

**Definition (Ordered field)** An ordered field is a field $\mathbb{F}$ with a relation $<$ that makes $\mathbb{F}$ into an ordered set such that
    
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

Let $x \in \mathbb{F}$ and $x \in \mathbb{F}$.
Exactly one of $x = 0$, $x < 0$ or $x > 0$ holds, and we consdider them separately.
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
    
concluding the proof.
    
    
In the off chance one really wants to show the fact that $(-x)^2 = x^2$, which was used in the last case, here's one way.
Consider 
 
$$\begin{align}
x + (-x) = 0 \implies x^2 + (-x)x = 0
\end{align}$$
    
and also that
    
$$\begin{align}
x + (-x) = 0 \implies (-x)x + (-x)^2 = 0.
\end{align}$$
    
Combining these two identities we obtain $x^2 = (-x)^2$. We can sleep peacefully.

</details>
<br>

(analysis-i-least-upper-bound)=
## Least upper bound property

Another central concept in analysis is that of upper (lower) bounds and that of least upper (greatest lower) bounds.
Among other uses, we will use use these concepts to define the real numbers themselves.

<div class="definition">

**Definition (Upper bound and supremum)** Let $S$ be an ordered field and $A \subseteq S$.
An upper bound for $A$ is an element $x \in S$ such that $a \leq x$ for all $a \in A$, and if such $a$ exists we say $A$ is bounded above.
The upper bound $x$ is a supremum (or least upper bound) if for all $a < x$, there exists $b \in A$ such that $b < a$.
    
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

**Lemma (Archimedean property)** Let $\mathbb{F}$ be an ordered field with the least upper bound property.
Then the set $\{1, 2, 3, ...\}$, the sequence obtained by starting from the $1$ element and applying the operation $+ 1$, is not bounded above.
    
</div>
<br>


<details class="proof">
<summary>Proof: Archimedean property</summary>

If $\{1, 2, 3, ...\}$ has an upper bound, it must also have a least upper bound $x$ by the least upper bound property. Since $x$ is a least upper bound, $x - 1$ is not a least upper bound so there exists $n > x - 1$.
Therefore $n + 1 > x$ and $x$ is not an upper bound, reaching a contradiction.

</details>
<br>