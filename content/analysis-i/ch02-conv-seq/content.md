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
|a_n - a| < |\lambda| \epsilon, \text{ for all } n > N.
\end{align}$$
    
For that same $N$ we have
    
$$\begin{align}
|\lambda a_n - \lambda a| = |\lambda| |a_n - a| < |\lambda| \epsilon.
\end{align}$$
    
so $\lambda a_n$ converges to $\lambda a$.

</details>
<br>