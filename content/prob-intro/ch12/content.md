# Markov chains

## Markov chain and Markov property

<div class='definition'>

**Definition (Markov chain and markov property)** The sequence $\mathbf{X} = X_0, X_1, ...$ is called a Markov chain if it satisfies the Markov property
    
$$\begin{align}
\mathbb{P}(X_{n + 1} = x_{n + 1} | X_0 = x_0, X_1 = x_1, ..., X_n = x_n) = \mathbb{P}(X_{n + 1} = x_{n + 1} | X_n = x_n)
\end{align}$$
    
for all $n \geq 0$ and all $x_0, x_1, ..., x_{n + 1} \in S$. The Markov chain is called homogeneuous if for all $u, v \in S$, the conditional probability $\mathbb{P}(X_{n + 1} = v | X_n = u)$ does not depend on the value of $n$. In this case, we the *transition matrix* $P$ and *initial distribution* $\lambda$ of the chain are defined as
    
$$\begin{align}
P = (p_{i, j} : i, j \in S), \text{ where } p_{i, j} = \mathbb{P}(X_1 = j | X_0 = i)\\
\lambda = (\lambda_i : i \in S), \text{ where } \lambda_i = \mathbb{P}(X_0 = i).
\end{align}$$

</div>
<br>

Because they are probability distributions, $P$ and $\lambda$ satisfy

$$\begin{align}
\lambda \geq 0, & \text{ and } \sum_{i \in S} \lambda_i = 1,\\
p_{i, j} \geq 0, & \text{ and } \sum_{j \in S} p_{i, j} = 1.
\end{align}$$

Any matrix $P$ which satisfies the above property is called a **stochastic matrix**.


<div class='theorem'>

**Theorem (Markov chain $\iff$ distribution factorises)** Let $\lambda$ be a distribution and $P$ be a stochastic matrix. The random sequence $\mathbb{X} = (X_n : n \geq 0)$ is a Markov chain with initial distribution $\lambda$ and transition matrix $P$ if and only if
    
$$\begin{align}
\mathbb{P}(X_0 = x_0, X_1 = x_1, ..., X_n = x_n) = \lambda_{x_0} p_{x_0, x_1} ... p_{x_{n - 1}, x_n}
\end{align}$$
    
for all $n \geq 0$ and $x_0, x_1, ..., x_n \in S$.

</div>
<br>



<div class='theorem'>

**Theorem (Extended Markov property)** Let $\mathbb{X} = (X_n : n \geq 0)$ is a Markov chain. For $n \geq 0$, for any event $H$ given in terms of $X_0, X_1, ..., X_{n - 1}$ and any event given in terms of $X_{n + 1}, X_{n + 2}, ...$,
    
$$\begin{align}
\mathbb{P}(F | X_n = x, H) = \mathbb{P}(F | X_n = x), \text{ for } x \in S.
\end{align}$$

</div>
<br>


<div class='theorem'>

**Theorem (Chapman-Kolmogorov equations)** Let $\mathbb{X} = (X_n : n \geq 0)$ be a Markov chain with initial distribution $\lambda$ and transition matrix $P$. Then the *n-step transition probabilities* $p_{x_i, x_j}(n) = \mathbb{P}(X_n = x_j | X_0 = x_i)$ satisfy
    
$$\begin{align}
p_{x_i, x_j}(n + m) = \sum_{x_k \in S} p_{x_i, x_k}(n)p_{x_k, x_j}(m),
\end{align}$$
    
for $x_i, x_j \in S$ and $n, m \geq 0$.

</div>
<br>

