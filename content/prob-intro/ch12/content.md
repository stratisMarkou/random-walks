# Markov chains

## Markov chain and Markov property

<div class='definition'>

**Definition (Markov chain and markov property)** The sequence $\mathbf{X} = X_0, X_1, ...$ is called a Markov chain if it satisfies the Markov property
    
$$\begin{align}
\mathbb{P}(X_{n + 1} = x_{n + 1} | X_0 = x_0, X_1 = x_1, ..., X_n = x_n) = \mathbb{P}(X_{n + 1} = x_{n + 1} | X_n = x_n)
\end{align}$$
    
for all $n \geq 0$ and all $x_0, x_1, ..., x_{n + 1} \in S$. The Markov chain is called homogeneuous if for all $u, v \in S$, the conditional probability $\mathbb{P}(X_{n + 1} = x_{n + 1} | X_n = x_n)$ does not depend on the value of $n$. In this case, we the *transition matrix* $P$ and *initial distribution* $\lambda$ of the chain are defined as
    
$$\begin{align}
P = (p_{i, j} : i, j \in S), \text{ where } p_{i, j} &= \mathbb{P}(X_1 = j | X_0 = i)\\
\lambda = (\lambda_i : i \in S), \text{ where } \lambda_i &= \mathbb{P}(X_0 = i).
\end{align}$$

</div>
<br>

Because they are probability distributions, $P$ and $\lambda$ satisfy

$$\begin{align}
\lambda \geq 0, & \text{ and } \sum_{i \in S} \lambda_i = 1,\\
p_{i, j} \geq 0, & \text{ and } \sum_{j \in S} p_{i, j} = 1.
\end{align}$$

Any matrix $P$ which satisfies the above property is called a **stochastic matrix**. The book{cite}`grimstir` and these notes deal with homogeneous Markov chains only, although some of the definitions and theorems also apply to inhomogeneous Markov chains.


<div class='theorem'>

**Theorem (Markov chain $\iff$ distribution factorises)** Let $\lambda$ be a distribution and $P$ be a stochastic matrix. The random sequence $\mathbb{X} = (X_n : n \geq 0)$ is a Markov chain with initial distribution $\lambda$ and transition matrix $P$ if and only if
    
$$\begin{align}
\mathbb{P}(X_0 = x_0, X_1 = x_1, ..., X_n = x_n) = \lambda_{x_0} p_{x_0, x_1} ... p_{x_{n - 1}, x_n}
\end{align}$$
    
for all $n \geq 0$ and $x_0, x_1, ..., x_n \in S$.

</div>
<br>



<div class='theorem'>

**Theorem (Extended Markov property)** Let $\mathbf{X} = (X_n : n \geq 0)$ is a Markov chain. For $n \geq 0$, for any event $H$ given in terms of $X_0, X_1, ..., X_{n - 1}$ and any event given in terms of $X_{n + 1}, X_{n + 2}, ...$,
    
$$\begin{align}
\mathbb{P}(F | X_n = x, H) = \mathbb{P}(F | X_n = x), \text{ for } x \in S.
\end{align}$$

</div>
<br>


<div class='theorem'>

**Theorem (Chapman-Kolmogorov equations)** Let $\mathbf{X} = (X_n : n \geq 0)$ be a Markov chain with initial distribution $\lambda$ and transition matrix $P$. Then the *n-step transition probabilities* $p_{x_i, x_j}(n) = \mathbb{P}(X_n = x_j | X_0 = x_i)$ satisfy
    
$$\begin{align}
p_{x_i, x_j}(n + m) = \sum_{x_k \in S} p_{x_i, x_k}(n)p_{x_k, x_j}(m),
\end{align}$$
    
for $x_i, x_j \in S$ and $n, m \geq 0$.

</div>
<br>


<details class="proof">
<summary>Proof: Chapman-Holmogorov equations</summary>

From the definition of $p_{x_i, x_j}(n + m)$ we see
    
$$\begin{align}
p_{x_i, x_j}(n + m) &= \mathbb{P}(X_{n + m} = x_j | X_0 = x_i)\\
&= \sum_{k \in S} \mathbb{P}(X_{n + m} = x_j | X_k = x_k, X_0 = x_0) \mahtbb{P}(X_k = x_k | X_0 = x_i) \\
&= \sum_{k \in S} \mathbb{P}(X_{n + m} = x_j | X_k = x_k) \mahtbb{P}(X_k = x_k | X_0 = x_i) \\
&= \sum_{k \in S} \mathbb{P}(X_{n + m} = x_j | X_k = x_k) \mahtbb{P}(X_k = x_k | X_0 = x_i) \\
&= \sum_{k \in S} p_{x_i, x_k}(n)p_{x_k, x_j}(m),
\end{align}$$
    
where we have used the Markov property to go from the second to the third line.

</details>
<br>



<div class='definition'>

**Definition (Communicating states)** Let $\mathbf{X} = X_0, X_1, ...$ be a Markov chain with state space $S$ and transition matrix $P$. For $i, j \in S$, we say that $i$ leads to $j$, written $i \to j$, if $p_{i, j}(n) > 0$ for some $n \geq 0$. If $i \to j$ and $j \to i$, we write $i \leftrightarrow j$, and say that $i$ and $j$ communicate.

</div>
<br>

<div class='lemma'>

**Lemma (Communication relation)** The relation $\leftrightarrow$ is an equivalence relation.

</div>
<br>


<details class="proof">
<summary>Proof: Communication relation</summary>

A relation is an equivalence relation if it is reflexive, symmetric and transitive. First, for any $i \in S$ we have $i \to i$, so $i \leftrightarrow i$, so communication is reflexive. Second, if $i \leftrightarrow j$ we have $i \to j$ and $j \to i$, from which it follows $j \to i$, so communication is symmetric. Finally, suppose $i \leftrightarrow j$ and $j \leftrightarrow k$. Then, there exist $n, m \geq 0$ such that $p_{i, j}(n) > 0$ and $p_{j, k}(m) > 0$. By the Chapman-Kolmogorov equations
    
$$\begin{align}
p_{i, k}(n + m) &= \sum_{l \in S} p_{i, l}(n) p_{l, k}(m) \\
&= p_{i, j}(n) p_{j, k}(m) > 0,
\end{align}$$
    
from which it follows that $i \to k$. Similarly we have $k \to i$, thus $i \leftrightarrow k$ and $\leftrightarrow$ is transitive.

</details>
<br>


<div class='definition'>

**Definition (Communicating classes, irreducible chains, closed sets)** The equivalence classes of $\leftrightarrow$ are called communicating classes. A Markov chain $\mathbf{X}$ is called irreducible, if there is a single communicating class. A subset $C \subseteq S$ is called closed if $i \in C, i \to j \implies j \in C$. If the singleton set $\{i\}$ is closed, $i$ is called an absorbing state.

</div>
<br>


<div class='definition'>

**Definition (First-passage times and probabilites)** The first-passage time to state $j$ is defined as
    
$$\begin{align}
T_j = \min \{n \geq 1 : X_n = j\},
\end{align}$$
    
and the first-passage probabilites are defined as
    
$$\begin{align}
f_{i, j}(n) = \mathbb{P}(T_j = n | X_0 = i).
\end{align}$$

</div>
<br>


<div class='definition'>

**Definition (First-passage times and probabilites)** A state $i$ is called recurrent if $\mathbb{P}(T_j < \infty | X_0 = i) = 1$, and it is called transient if it is not recurrent.

</div>
<br>


<div class='theorem'>

**Theorem (Recurrence $\iff$ sum of return probabilities diverges)** The state $i$ is recurrent if and only if
    
$$\begin{align}
\sum^{\infty}_{n = 0} p_{i, i}(n) = \infty.
\end{align}$$

</div>
<br>

To prove this result we use the following theorem, which related the generating functions of the return probabilities and the first-passage times.



<details class="proof">
<summary>Proof: Recurrence \(\iff\) sum of return probabilities diverges</summary>

Starting from the relation
    
$$\begin{align}
P_{i, j} = \delta_{i, j} + F_{i, j}(s) P_{j, j}(s),
\end{align}$$
    
we set $j = i$ and rearrange to obtain
    
$$\begin{align}
P_{j, j}(s) = \frac{1}{1 - F_{i, i}(s)}.
\end{align}$$
    
Then letting $s \to 1$, we obtain
    
$$\begin{align}
\sum^{\infty}_{n = 0} p_{i, i}(n) = \lim_{s \to 1} P_{j, j}(s) = \lim_{s \to 1} \frac{1}{1 - F_{i, i}(s)}.
\end{align}$$
    
and considering $\lim_{s \to 1} F_{i, i}(s) = f_{i, i}$, we see that the sum on the left diverges if and only if $f_{i, i} = 1$, i.e. if the state is recurrent.

</details>
<br>



<div class='theorem'>

**Theorem (Gen. func. of return and first-passage probabilities)** Let $P_{i, j}(s)$ and $F_{i, j}(s)$ be the generating functions
    
$$\begin{align}
P_{i, j} &= \sum_{n = 0}^\infty p_{i, j}(n) s^n, \\
F_{i, j} &= \sum_{n = 0}^\infty f_{i, j}(n) s^n.
\end{align}$$
    
Then for any $i, j \in S$, we have

$$\begin{align}
P_{i, j} = \delta_{i, j} + F_{i, j}(s) P_{j, j}(s).
\end{align}$$

</div>
<br>


<details class="proof">
<summary>Proof: Gen. func. of return and first-passage probabilities</summary>
  
First, we can write $p_{i, j}(n)$ as
    
$$\begin{align}
p_{i, j}(n) = \sum_{m = 1}^\infty \mathbb{P}(X_n = j | T_j = m, X_0 = i) \mathbb{P}(T_j = m | X_0 = i).
\end{align}$$
    
Writing $H = \{X_n \neq j \text{ for } 1 \leq n < m\}$ and using the extended Markov property
    
$$\begin{align}
\mathbb{P}(X_n = j | T_j = m, X_0 = i) = \mathbb{P}(X_n = j | X_m = j, H, X_0 = i) = \mathbb{P}(X_n = j | X_m = j).
\end{align}$$
    
Using the fact that the chain is homogeneous
    
$$\begin{align}
p_{i, j}(n) &= \sum_{m = 1}^\infty \mathbb{P}(X_n = j | X_m = j) \mathbb{P}(T_j = m | X_0 = i), \\
&= \sum_{m = 1}^\infty f_{i, j}(m) p_{j, j}(n - m),
\end{align}$$
    
and multiplying both sides by $s^n$ and summing over $n$, we obtain
    
$$\begin{align}
\sum_{n = 1}^\infty p_{i, j}(n) s^n &= \sum_{n = 1}^\infty \sum_{m = 1}^\infty f_{i, j}(m) s^m p_{j, j}(n - m) s^{n - m}, \\
&= \sum_{m = 1}^\infty \sum_{n = m}^\infty f_{i, j}(m) s^m p_{j, j}(n - m) s^{n - m}, \\
&= \left[\sum_{m = 1}^\infty f_{i, j}(m) s^m \right] \left[\sum_{n = m}^\infty p_{j, j}(n - m) s^{n - m}\right],
\end{align}$$
    
where we have used the fact $f_{i, j}(0) = 0$. Lastly, using the fact that $p_{i, j}(0) = \delta_{i, j}$, we arrive at the result
    
$$\begin{align}
P_{i, j}(s) = \delta_{i, j} + F_{i, j}(s) P_{j, j}(s).
\end{align}$$

</details>
<br>


<div class='theorem'>

**Theorem (Communicating class and recurrence/transience)** Let $C$ be a communicating class. Then
    
1. Either every state in $C$ is recurrent or every state is transient.
2. Suppose $C$ contains some recurrent state. Then $C$ is closed.

</div>
<br>


<details class="proof">
<summary>Proof: Communicating class and recurrence/transience</summary>
  
**Part 1:** Suppose $i \in C$ is recurrent. Then from the Chapman-Kolmogorov equations, for any $j \in C$ we have
    
$$\begin{align}
\sum_{n = 1}^\infty p_{j, j}(n) \geq \sum_{l = 1}^\infty p_{j, j}(k + l + m) = p_{j, i}(k) \left[\sum_{l = 1}^\infty p_{i, i}(l)\right] p_{i, j}(m) = \infty,
\end{align}$$
    
so $j$ is also recurrent.
    
**Part 2:** Suppose $i \in C$ is recurrent and that $C$ is not closed. Then there exist $j \in C$ and $k \not \in C$ such that $j \to k$ and $k \not \to j$. From the previous part of this theorem, $j$ is also recurrent. Using these facts we arrive at the contradiction
    
$$\begin{align}
\mathbb{P}(X_n \neq j \text{ for } n \geq 1 | X_0 = j) \geq p_{j, k} > 0,
\end{align}$$
    
where the first inequality follows because $k \not \to j$, so if the chain transitions from $j$ to $k$ in the first step, it cannot return to $j$ in any number of steps. Therefore the assumption that $C$ is not closed, is contradicted.

</details>
<br>

<div class='theorem'>

**Theorem (Communication and recurrence of finite $S$)** Suppose that the state space $S$ is finite
    
1. There exists at least one recurrent state.
2. If the chain is irreducible, all states are recurrent.

</div>
<br>


<details class="proof">
<summary>Proof: Communication and recurrence of finite \(S\)</summary>
  
**Part 1:** Suppose $S$ is finite and that all states are transient. Since all states are transient
    
$$\begin{align}
P_{i, i}(1) < \infty, F_{j, i}(1) \leq 1 \implies P_{j, i}(1) < \infty
\end{align}$$
    
for any $i, j \in S$. Since $P_{j, i}(1) = \sum^\infty_{n = 1} p_{j, i}(n) < \infty$, we must have $p_{j, i}(n) \to 0$ as $n \to \infty$. Since $p_{i, j}(n)$ is a distribution however
    
$$\begin{align}
\sum_{j \in S} p_{i, j}(n) = 1,
\end{align}$$
    
reaching a contradiction.
    
**Part 2:** Suppose that the chain is irreducible, so that all states belong to the same communicating class. From the first part of this theorem, there exists at least one recurrent state and since all states belonging to the same communicating class are either all recurrent or all transient, it follows that all states are recurrent.
   
</details>
<br>

<div class='theorem'>

**Theorem (Polya's theorem)** The symmetric random walk on $\mathbb{Z}^d$ is recurrent if $d = 1, 2, ...$ and transient if $d \geq 3$.

</div>
<br>


<div class='definition'>

**Definition (Hitting time, hitting and absorption probabilities)** The hitting time of a subset $A \subseteq S$ is the earliest time $n$ at which $X_n \in A$.
    
$$\begin{align}
H^A = \inf \{n \geq 0 : X_n \in A\}.
\end{align}$$
    
The hitting probability is defined in terms of the hitting time as
    
$$\begin{align}
h^A_i = \mathbb{P}(H^A < \infty | X_0 = i).
\end{align}$$
    
If $A$ is closed, $h^A_i$ is called an absorption probability.

</div>
<br>


<div class='theorem'>

**Theorem (Hitting probabilities)** The vector of hitting probabilities $h^A = (h^A_i : i \in S)$ is the minimal non-negative solution to
    
$$\begin{align}
h^A_i = \begin{cases}
1 & \text{ for } i \in A, \\
\sum_{j \in S} p_{i, j} h_j^A & \text{ for } i \not \in A.
\end{cases}
\end{align}$$

</div>
<br>


<div class='theorem'>

**Theorem (Expected hitting times)** The vector of expected hitting times $k^A = (k_i^A = \mathbb{E}\left[H_i^A\right] : i \in S)$ is the minimal non-negative solution to
    
$$\begin{align}
k^A_i = \begin{cases}
0 & \text{ for } i \in A, \\
1 + \sum_{j \in S} p_{i, j} k_j^A & \text{ for } i \not \in A.
\end{cases}
\end{align}$$

</div>
<br>


## Stopping times and the strong Markov property


<div class='definition'>

**Definition (Stopping time)** The random variable $T : \Omega \to \{0, 1, 2, ...\} \cup \{\infty\}$ is called a stopping time for the Markov chain $\mathbb{X}$, if the event $\{T = n\}$ is given in terms of $X_0, X_1, ..., X_n$ only, for all $n \geq 0$.

</div>
<br>


<div class='theorem'>

**Theorem (Strong Markov property)** Let $\mathbb{X} = X_0, X_1, ...$ be a Markov chain with transition matrix $P$, and let $T$ be a stopping time. Given $T < \infty$ and $X_T = i$, the sequence $\mathbb{Y} = Y_0, Y_1, ...$, given by $Y_k = X_{T + k}$, is a Markov chain with transition matrix $P$ and initial state $Y_0 = i$. Further, given that $T < \infty$ and $X_T = i$, $\mathbb{Y}$ is independent of $X_0, X_1, ..., X_{T - 1}$.

</div>
<br>

    
## References

```{bibliography} ./references.bib
```