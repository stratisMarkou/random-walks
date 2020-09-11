# Convergence of sequences

This section introduces sequences and deals with results regarding their convergence.

## Sequences

Analysis deals with properties of objects like sequences, series, functions, derivatives and integrals defined with respect to the real or the complex numbers. We therefore need to define the real numbers. Instead of doing so directly however, we define an object called a *field*, which has all the necessary properties on which to do analysis, and the reals can be shown to be an example of a field.

<div class="definition">

**Definition (Sequence)** A sequence $a$ is a function $a : \mathbb{N} \to \mathbb{R} (\text{ or } \mathbb{C})$. We denote the terms of the sequence as $a_n$ and an alternative notation for the sequence itself is $(a_n)$.
    
</div>
<br>

Now we can define what it means for a sequence to converge. Informally a sequence converges to a limit $\ell$ if after a certain term, all terms are within a small distance to $\ell$, where the small distance can be chosen to be arbitrarily small.

<div class="definition">

**Definition (Convergence of a sequence)** Let $(a_n)$ be a sequence and $\ell \in \mathbb{R}$. We say that $a_n$ converges to $\ell$, tends to $\ell$ or $a_n \to \ell$, if for all $\epsilon > 0$, there are some $N \in \mathbb{N}$ such that whenever $n > N$, $|a_n - \ell| < \epsilon$, or in other words
    
$$\begin{align}
\forall \epsilon > 0, \exists N \text{ such that } |a_n - \ell| < \epsilon.
\end{align}$$
    
In this case, we say that $\ell$ is the limit of $a_n$.
    
</div>
<br>


<div class="lemma">

**Lemma (Archimedean property - alternative statement)** The sequence $a_n = \frac{1}{n}$ converges to $0$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Archimedean property - alternative statement</summary>

Let $\epsilon > 0$. We want to show there exists N such that
    
$$\begin{align}
|1 / n - 0| = 1/n < \epsilon, \text{for all } n \geq N.
\end{align}$$
    
We have
    
$$\begin{align}
\frac{1}{n} < \epsilon \implies n > \frac{1}{\epsilon}.
\end{align}$$
    
and by the {ref}`Archimedian property<analysis-i-real-num>`, there exists such $N > 1 / \epsilon$. Then 
    
$$\begin{align}
0 < \frac{1}{n} \leq {1}{N} < \epsilon \text{ for all } n \geq N,
\end{align}$$
    
arriving at the result.

</details>
<br>

    
<div class="definition">

**Definition (Bounded and eventually bounded sequence)** A sequence $(a_n)$ is bounded if there exists $C$ such that
    
$$\begin{align}
|a_n| \leq C, \text{ for all } n.
\end{align}$$
    
A sequence is eventually bounded if there exist $N, C$ such that
    
$$\begin{align}
|a_n| \leq C, \text{ for all } n \geq N.
\end{align}$$
    
</div>
<br>
    

<div class="lemma">

**Lemma (Eventually bounded $\iff$ Bounded)** Every sequence that is eventually bounded is bounded, and vice versa.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Eventually bounded \(\iff\) bounded</summary>

Every sequence that is bounded is also eventually bounded trivially, considering we can set $N = 1$. Suppose $(a_n)$ is eventually bounded, so that
    
$$\begin{align}
|a_n| \leq C, \text{ for all } n \geq N.
\end{align}$$
    
Now taking $C^* = \max \{|a_1|, |a_2|, ..., |a_{N - 1}|, C\}$, we see that $|a_n| \leq C^*$, so $(a_n)$ is bounded.

</details>
<br>
    
    
Intuitively, if two sequences converge so does the sum of their terms, as stated by the result below.

    
<div class="lemma">

**Lemma (Sum of sequences)** If $a_n \to a$ and $b_n \to b$, $a_n + b_n \to a + b$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Sum of sequences</summary>

Let $\epsilon > 0$. Since $a_n \to a$ and $b_n \to b$, there exists $N$ such that
    
$$\begin{align}
|a_n - a| \leq \frac{epsilon}{2} \text{ and } |b_n - b| \leq \frac{epsilon}{2}, \text{ for all } n \geq N.
\end{align}$$
    
Then we have
    
$$\begin{align}
|(a_n + b_n) - (a + b)| \leq |a_n - a| + |b_n - b| \leq epsilon, \text{ for all } n \geq N,
\end{align}$$
    
arriving at the result.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Scalar multiplication of sequences)** If $a_n \to a$ and $\lambda \in \mathbb{R}$, then $\lambda a_n \to \lambda a$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Scalar multiplication of sequences</summary>

Let $\epsilon > 0$. If $a_n \to a$ and $\lambda \in \mathbb{R}$, there exists $N$ such that
    
$$\begin{align}
|a_n - a| < \frac{\epsilon}{|\lambda|}, \text{ for all } n > N.
\end{align}$$
    
For that same $N$ we have
    
$$\begin{align}
|\lambda a_n - \lambda a| = |\lambda| |a_n - a| < \epsilon, \text{ for all } n > N,
\end{align}$$
    
so $\lambda a_n$ converges to $\lambda a$.

</details>
<br>
    
    
    
<div class="lemma">

**Lemma (Product of bounded and $0$-limit sequence)** If $(a_n)$ is bounded and $b_n \to 0$, then $a_n b_n \to 0$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Product of bounded and \(0\)-limit sequence</summary>

If $(a_n)$ is bounded, there exists $C > 0$ such that $|a_n| < C$ for all $n$. Further if $b_n \to 0$, there exists $N$ such that for any value of $\epsilon > 0$
    
$$\begin{align}
|b_n - b| < \frac{\epsilon}{C}, \text{ for all } n > N.
\end{align}$$
    
For that same $N$ we have
    
$$\begin{align}
|a_nb_n - 0| = |a_nb_n| \leq |a_n| |b_n| < \epsilon, \text{ for all } n > N
\end{align}$$
    
so $a_nb_n$ converges to $0$.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Convergence $\implies$ bounded)** Every convergent sequence is bounded
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Convergence \(\implies\) bounded</summary>
    
If $a_n \to a$, then there exists $N$ such that
    
$$\begin{align}
|a_n - a| < \epsilon, \text{ for all } n > N.
\end{align}$$
    
Therefore the sequence is eventually bounded and by extension it is also bounded.

</details>
<br>
    
    
    
<div class="lemma">

**Lemma (Product of sequences)** If $a_n \to a$ and $b_n \to b$, then $a_n b_n \to ab$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Product of sequences</summary>
    
If $a_n \to a$ then $(a_n)$ is bounded, and also if $b_n \to b$ then the sequence $\epsilon_n = b_n - b$ converges to $0$. The product of a bounded sequence and a $0$-limit sequence converges to $0$, so $a_n \epsilon_n \to 0$. Therefore
    
$$\begin{align}
a_n b_n = a_n (\epsilon_n + b) \to ab.
\end{align}$$

</details>
<br>
    
    
<div class="lemma">

**Lemma (Inverse of a sequence)** If $a_n \to a$, $a_n \neq 0$ and $a \neq 0$ then $\frac{1}{a_n} \to \frac{1}{a}$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Inverse of a sequence</summary>
    
Let $\epsilon > 0$. If $a_n \to a$, $a_n \neq 0$ and $a \neq 0$, there exists $N_1$ such that
    
$$\begin{align}
|a_n - a| < \frac{a}{2}, \text{ for all } n > N_1,
\end{align}$$
    
and $N_2$ such that
    
$$\begin{align}
|a_n - a| < \frac{\epsilon a^2}{2}, \text{ for all } n > N_2,
\end{align}$$
    
implying that
    
$$\begin{align}
\left | \frac{1}{a_n} - \frac{1}{a} \right | = \left | \frac{a_n - a}{a_n a} \right | \leq \left | \frac{1}{a_n a} \right | \left | a_n - a \right | < \epsilon, \text{ for all } n > \max(N_1, N_2) = N^*,
\end{align}$$
    
proving the result.

</details>
<br>