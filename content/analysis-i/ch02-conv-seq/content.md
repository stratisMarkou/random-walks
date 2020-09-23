# Convergence of sequences

This section introduces sequences and deals with results regarding their convergence.

(analysis-i-sequences)=
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
\bigg|\frac{1}{n} - 0\bigg| = \frac{1}{n} < \epsilon, \text{for all } n \geq N.
\end{align}$$
    
We have
    
$$\begin{align}
\frac{1}{n} < \epsilon \implies n > \frac{1}{\epsilon}.
\end{align}$$
    
and by the {ref}`Archimedian property<analysis-i-real-num>`, there exists such that $N > \frac{1}{\epsilon}$. Then 
    
$$\begin{align}
0 < \frac{1}{n} \leq \frac{1}{N} < \epsilon \text{ for all } n \geq N,
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
    
    
## Convergence lemmas
    
    
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

**Lemma (Convergence $\implies$ bounded)** Every convergent sequence is bounded.
    
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

**Lemma (Reciprocal of a sequence)** If $a_n \to a$, $a_n \neq 0$ and $a \neq 0$ then $\frac{1}{a_n} \to \frac{1}{a}$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Reciprocal of a sequence</summary>
    
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
\left | \frac{1}{a_n} - \frac{1}{a} \right | = \left | \frac{a_n - a}{a_n a} \right | = \left | \frac{1}{a_n a} \right | \left | a_n - a \right | < \epsilon, \text{ for all } n > \max(N_1, N_2) = N^*,
\end{align}$$
    
proving the result.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Quotient of sequences)** If $a_n \to a$, $b_n \to b$, $b_n \neq 0$ and $b \neq 0$ then $\frac{a_n}{b_n} \to \frac{a}{b}$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Quotioent of sequences</summary>
    
If $b_n \to b$, $b_n \neq 0$ and $b \neq 0$, then $\frac{1}{b_n} \to b$ by the lemma on the inverse of a sequence. From this, the product of the sequences $a_n$ and $\frac{1}{b_n}$ converges to $\frac{a}{b}$, by the lemma on products of sequences.

</details>
<br>
    
    
    
<div class="lemma">

**Lemma (Sandwich rule)** If $a_n \leq b_n \leq c_n$, $a_n \to \ell$ and $c_n \to \ell$, then $c_n \to \ell$ also.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Sandwich rule</summary>
    
Let $\epsilon > 0$. Since $a_n \to \ell$ and $c_n \to \ell$, there exist $N_a$ and $N_c$ such that
    
$$\begin{align}
|a_n - a| &< \epsilon, \text{ for all } n > N_a, \\
|c_n - c| &< \epsilon, \text{ for all } n > N_c.
\end{align}$$
    
Now since $a_n \leq b_n \leq c_n$
    
$$\begin{align}
|b_n - \ell| \leq \max \{|a_n - \ell|, |c_n - \ell|\} < \epsilon ~~~\text{ for all } n > \max\{N_a, N_c\} = N^*.
\end{align}$$
    
Therefore $b_n \to \ell$ as $n \to \infty$.

</details>
<br>
    
(analysis-i-mon-seq-prop)=
## Monotone sequences   
    
<div class="definition">

**Definition (Monotone sequences)** A sequence $(a_n)$ is increasing (decreasing) if $a_n \leq a_{n + 1}$ for all $n$. It is *strictly* increasing (decreasing) if $a_n < a_{n + 1}$ for all $n$. A sequence is (strictly) monotone if it is (strictly) inceasing or (strictly) deceasing.
    
</div>
<br>
    
    
<div class="definition">

**Definition (Monotone sequences property)** An ordered field $\mathbb{F}$ has the monotone sequences property if every increasing (decreasing) sequence that is bounded above (below) converges.
    
</div>
<br>
    

<div class="lemma">

**Lemma (Least upper bound $\implies$ monotone sequences property)** If an ordered field has the {ref}`least upper bound property<analysis-i-least-upper-bound>`, also has the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`.
    
</div>
<br>

<details class="proof">
<summary>Proof: Least upper bound \(\implies\) monotone sequences property</summary>
    
Suppose $\mathbb{F}$ is an ordered field with the least upper bound property and that $(a_n)$ is an increasing sequence that is bounded above. Then by the least upper bound property, it has a least upper bound $a \in \mathbb{F}$. We will now show that $(a_n)$ converges to $a$.
       
Let $\epsilon > 0$. There must exist a positive integer $N$ such that $|a_n - a| < \epsilon$ for some $n > N$. If that were not the case, then $|a_n - a| \geq \epsilon$ for all $n > N$ (and by extension $|a_n - a| \geq \epsilon$ for all positive integer $n$, since the sequence $|a_n - a|$ is decreasing), which is a contradiction because $a$ is supposed to be a least upper bound and we have just shown that $a - \frac{\epsilon}{2}$ is also an upper bound for $(a_n)$. Since there exists $N$ such that
    
$$\begin{align}
|a_n - a| < \epsilon \text{ for some } n > N,
\end{align}$$
    
and the sequence $|a_n - a|$ is decreasing, we have
    
$$\begin{align}
|a_n - a| < \epsilon \text{ for all } n > N,
\end{align}$$
    
showing that the sequence converges to $a$ and $\mathbb{F}$ has the monotone sequences property.

</details>
<br>

    
<div class="lemma">

**Lemma (Sequence upper bound also bounds the limit)** Let $(a_n)$ be a sequence and suppose $a_n \to a$. If $a_n \leq x$ for all $n$, then $a \leq x$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Sequence upper bound also bounds the limit</summary>
    
If $a > x$, then we can set $\epsilon = a - x$ and find $N$ such that $|a_N - a| \leq \epsilon$, from which it follows that $a_N - x > 0$, reaching a contradiction.

</details>
<br>
    

<div class="lemma">

**Lemma (Monotone sequences $\implies$ archimedean property)** If an ordered field $\mathbb{F}$ has the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`, it also has the {ref}`archimedean property<analysis-i-sequences>`.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Monotone sequences \(\implies\) archimedean property</summary>
    
Suppose $\mathbb{F}$ is an ordered field with the monotone sequences property. The sequence with terms $a_n = \frac{1}{n}$ is decreasing and its terms are bounded below by $0$ and by the monotone sequences property, it converges to a limit $\delta$. By the previous lemma, $\delta \geq 0$. If we assume $\delta \neq 0$ we reach a contradiction, because we can set $\epsilon = \frac{\delta}{2}$ and observe that for all $n > \frac{\delta}{2}$
    
$$\begin{align}
\frac{1}{n} \leq \frac{\delta}{2} \implies |\frac{1}{n} - \delta| > \frac{\delta}{2} = \epsilon.
\end{align}$$
    
Thus $a_n$ cannot converge to $\delta > 0$ so we must have $\delta = 0$, and $\frac{1}{n} \to 0$.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Monotone sequences $\implies$ least upper bound property)** If an ordered field $\mathbb{F}$ has the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`, it also has the {ref}`least upper bound property<analysis-i-least-upper-bound>`.
    
</div>
<br>
    

<div class="lemma">

**Lemma (Limit uniqueness)** A sequence can have at most one limit.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Limit uniqueness</summary>
    
Suppose a sequence $(a_n)$ has two distinct limits $a$ and $b$. Suppose $a < b$ and set $\delta = b - a$. For any $\epsilon > 0$ there exist $N_a$ and $N_b$ such that
    
$$\begin{align}
& |a_n - a| < \epsilon \text{ for all } n > \max\{N_a, N_b\},
& |b_n - b| < \epsilon \text{ for all } n > \max\{N_a, N_b\}.
\end{align}$$
    
Setting $\epsilon = \delta$ we arrive at a contradiction, because the above expressions cannot hold simultaneously when $\epsilon \leq \delta$.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Monotone sequences $\implies$ least upper bound property)** If $\mathbb{F}$ is an ordered field with the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`, then it also has the {ref}`least upper bound property<analysis-i-least-upper-bound>`.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Monotone sequences \(\implies\) least upper bound property</summary>
    
Suppose $\mathbb{F}$ is an ordered field with the monotone sequences property, and let $S$ be a subset of $\mathbb{F}$ that is bounded above by some element $u_0 \in \mathbb{F}$. Pick $v_0 \in \mathbb{F}$ such that it is not an upper bound for $\mathbb{F}$. Proceeding by repeated bisection, if $\frac{v_n + u_n}{2}$ is an upper bound set $u_{n + 1} = \frac{v_n + u_n}{2}$ and $v_{n + 1} = v_n$, otherwise set $v_{n + 1} = \frac{v_n + u_n}{2}$ and $u_{n + 1} = u_n$. With this definition we have
    
$$\begin{align}
u_n - v_n = \frac{u_0 - v_0}{2^n}.
\end{align}$$
    
Since $\mathbb{F}$ has the monotone sequences property, it also has the archimedean property. Therefore the sequence $\frac{1}{n}$ converges to $0$ and by the sandwich rule
    
$$\begin{align}
u_n - v_n = \frac{u_0 - v_0}{2^n} \leq \frac{u_0 - v_0}{n} \to 0
\end{align}$$
    
implies that $u_n - v_n$ also converges to $0$. Since $u_n$ is a decreasing sequence that is bounded below by $v_0$, it converges to a limit $s$, and by extension $v_n$ also converges to $s$. We now show that $s = \sup S$.
    
If $s$ is not an upper bound, then there must exist $t \in S$ such that $s < t$, and since $u_n \to s$ there must also exist $m$ such that $u_m < t$, contradicting the fact that $u_m$ is an upper bound. To see that $s$ is the least upper bound, let $t < s$. Since $u_n \to s$ we can find $m$ such that $t < u_n$, implying that $t$ is not the upper bound.   
    
Therefore $s$ is a least upper bound and $\mathbb{F}$ has the least upper bound property.

</details>
<br>
    
(analysis-i-bolz-weier)=
## Bolzano-Weierstrass theorem
    
<div class="lemma">

**Lemma (Nested intervals property)** Let $\mathbb{F}$ be an ordered field with the monotone sequences property. If $I_1 \supseteq I_2 \supseteq ...$ are closed and bounded non-empty intervals, then

$$\begin{align}
\bigcap_{n = 1}^\infty I_n \neq \emptyset
\end{align}$$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Nested intervals property</summary>

Let $\mathbb{F}$ be an ordered field with the monotone sequences property, and $I_1 \supseteq I_2 \supseteq ...$ be closed and bounded non-empty intervals. Writing $I_n = [a_n, b_n]$ we have $a_1 \leq a_2 \leq ...$ and $b_1 \geq b_2 \geq ...$. The sequence $a_n$ is increasing and upper bounded by $b_1$ since $a_n \leq b_n \leq b_1$. By the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`, $(a_n)$ converges to a limit $a$.
    
We now show that $a_n \leq a \leq b_n$ for all $n$. First, for any $n$ it must be true that $a_n \leq a$, because if $a_n > a$ for any $a$, then for all $m \geq n$ we would have $a_m \geq a_n > a$ and since $a_m$ converges to $a$ we would arrive at the contradiction $a > a$. Second, for any $n$ we have $a_m \leq b_m \leq b_n$ for all $m \geq n$, implying that $a \leq b_n$, since the {ref}`an upper bound of a sequence also bounds the limit of the sequence<analysis-i-mon-seq-prop>`.
    
Thus for all $n$ we have $a_n \leq a \leq b_n$, implying that $a \in I_n$ for all $n$.

</details>
<br>
    
    
A useful consequence of the nested intervals property is the Bolzano-Weierstrass theorem.
    
<div class="theorem">

**Theorem (Bolzano-Weierstrass)** Let $\mathbb{F}$ be an ordered field with the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`. Every bounded sequence in $\mathbb{F}$ has a convergent subsequence.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Bolzano-Weierstrass theorem</summary>

Let $\mathbb{F}$ be an ordered field with the {ref}`monotone sequences property<analysis-i-mon-seq-prop>` and $(a_n)$ be a bounded sequence, with upper and lower bounds $u_0$ and $v_0$ respectively. Proceed by repeated bisection starting from $I_0 = [u_0, v_0]$, defining
    
$$\begin{align}
w_n = \frac{u_n + v_n}{2}
\end{align}$$

and selecting setting the interval $I_n$ equal to $[v_n, w_n]$ or $[w_n, u_n]$, whichever contains an infinite number of terms (if both contain an infinite number, select one arbitrarily), and renaming the left and right sides of $I_n$ to $v_{n+1}$ and $u_{n+1}$ respectively.
    
Since each interval $I_k$ contains infinitely many terms of $(a_n)$, we can define a strictly increasing sequence of integers $(n_k)$ such that $a_{n_k} \in I_k$. By the nested intervals property

$$\begin{align}
\bigcap_{n = 1}^\infty I_n \neq \emptyset
\end{align}$$

so there exists $a \in \bigcap_{n = 1}^\infty I_n$. We will show that $a_{n_k} \to a$. Let $\epsilon > 0$. By the archimedean property, we can find $K$ such that
    
$$\begin{align}
u_k - v_k = \frac{u_0 - v_0}{2^K} \leq \epsilon
\end{align}$$
    
and because $a \in [v_k, u_k]$ and $a_{n_k} \in [v_k, u_k]$ we have

$$\begin{align}
|a_{n_k} - a| < \epsilon \text{ for all } k \geq K.
\end{align}$$

</details>
<br>
    
    
(analysis-i-cauchy-seqs)=
## Cauchy sequences
    

<div class="definition">

**Definition (Cauchy sequence)** A sequence $(a_n)$ is Cauchy if for any $\epsilon > 0$, there exists some $N \in \mathbb{N}$ such that whenever $p, q \geq N$ we have
    
$$\begin{align}
|a_p - a_q| < \epsilon.
\end{align}$$
    
</div>
<br>
    
<div class="lemma">

**Lemma (Convergent $\implies$ Cauchy)** Every convergent sequence is a Cauchy sequence.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Convergent \(\implies\) Cauchy</summary>

Let $(a_n)$ be a sequence that converges to $a$ and $\epsilon > 0$. Then there exists $N$ such that
    
$$\begin{align}
&|a_p - a| < \frac{\epsilon}{2} \text{ for all } p > N,\\
&|a_q - a| < \frac{\epsilon}{2} \text{ for all } p > N.
\end{align}$$
    
from which it follows that
    
$$\begin{align}
|a_p - a_q| \leq |a_p - a| + |a_q - a| = 0 < \epsilon \text{ for all } p, q > N,
\end{align}$$
    
hence $(a_n)$ is Cauchy.

</details>
<br>
    
    
<div class="theorem">

**Theorem (The general principle of convergence)** Let $\mathbb{F}$ be an ordered field with the {ref}`monotone sequences property<analysis-i-mon-seq-prop>`. Then every {ref}`Cauchy sequence<analysis-i-cauchy-seqs>` of $\mathbb{F}$ converges.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: The general principle of convergence</summary>

Let $\mathbb{F}$ be an ordered field with the {ref}`monotone sequences property<analysis-i-mon-seq-prop>` and $(a_n)$ be a {ref}`Cauchy sequence<analysis-i-cauchy-seqs>` in $\mathbb{F}$. Then $(a_n)$ is eventually bounded because by the Cauchy condition, there exists $N$ such that $|a_n - a_N| \leq 1$ for all $n > N$. Therefore it is also bounded, and by the {ref}`Bolzano-Weierstrass theorem<analysis-i-bolz-weier>` it has a convergent subsequence $(a_{n_k})$. Therefore the sequence $(a_n)$ converges (to the same limit as its subsequence) concluding the proof.

</details>
<br>
    
    
    
<div class="definition">

**Definition (Complete ordered field)** An ordered field in which every Cauchy sequence converges is called a completer ordered field.
    
</div>
<br>    
    
<div class="lemma">

**Lemma (Archimedean and Cauchy $\implies$ monotone sequences)** If $\mathbb{F}$ be a compete ordered field with the archimedean property, it also has the monotone sequences property.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Archimedean and Cauchy \(\implies\) monotone sequences</summary>



</details>
<br>
    
    
## Limit infimum and supremum
    
<div class="definition">

**Definition (Limit supremum and infimum)** Let $(a_n)$ be a bounded sequence. We define the limit supremum as
    
$$\begin{align}
\limsup_{n \to \infty} a_n = \lim_{n \to \infty} \left(\sup_{m \geq n} a_m\right),
\end{align}$$

and the limit infimum as
    
$$\begin{align}
\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left(\inf_{m \geq n} a_m\right).
\end{align}$$
    
</div>
<br>

<div class="lemma">

**Lemma (Equality of limit infimum/supremum and convergence)** Let $(a_n)$ be a bounded sequence. Then
    
$$\begin{align}
a_n \to a \iff \liminf a_n = \limsup a_n = a.
\end{align}$$
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Equality of limit infimum/supremum and convergence</summary>



</details>
<br>