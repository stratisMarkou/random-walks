# Convergence of infinite sums

This section introduces infinite sums and presents results regarding their convergence.

(analysis-i-infinte-sums)=
## Infinite sums

An infinite sum, or series, is defined as the limit of the partial sum of the terms of a sequence.

<div class="definition">

**Definition (Convergence of infinite sums and partial sums)** Let $(a_n)$ be a real sequence and
    
$$\begin{align}
S_N = \sum^N_{n = 1} a_n.
\end{align}$$
    
If the sequence $(S_N)$ converges to some limit $s$, then we write
    
$$\begin{align}
\sum^\infty_{n = 1} a_n = s.
\end{align}$$
    
and we say that the series converges. $S_N$ is called the $N^{th}$ partial sum.
    
</div>
<br>

One necessary condition for series convergence is that the terms of the seqence tend to $0$.

<div class="lemma">

**Lemma (Series converges $\implies$ $a_n \to 0$)** If $\sum_{n = 1}^\infty a_n$ converges, then $a_n \to 0$.
    
</div>
<br>
    
<details class="proof">
<summary>Proof: Series converges \(\implies\) \(a_n \to 0\)</summary>

Suppose that $(a_n)$ is a sequence whose series $\sum_{n = 1}^\infty a_n$ converges to $s$. If $\epsilon > 0$, then we can find $N$ such that
    
$$\begin{align}
|S_n - s| < \frac{\epsilon}{2} \text{ for all } n > N,
\end{align}$$
    
and therefore also
    
$$\begin{align}
|a_{n + 1}| = |S_{n + 1} - S_n| < |S_{n + 1} - s| + |S_n - s| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon \text{ for all } n > N.
\end{align}$$
    
Therefore $|a_n|$ converges to $0$ and so does $a_n$.

</details>
<br>

<div class="lemma">

**Lemma (Partial sum of non-negative sequence bounded $\implies$ series converges)** Suppose that $a_n \geq 0$ and that the partial sums $S_n$ are bounded above. Then $\sum^\infty_{n = 1} a_n$ converges.
    
</div>
<br>

<details class="proof">
<summary>Proof: Partial sum of non-negative sequence bounded \(\implies\) series converges</summary>

Suppose that $a_n \geq 0$ is a sequence in $\mathbb{R}$ and that the partial sums $S_n$ are bounded above. The {ref}`real numbers<analysis-i-real-num>` have the {ref}`least upper bound property<analysis-i-least-upper-bound>`, which {ref}`implies<analysis-i-mono-seq-prop>` that they also have the {ref}`monotone sequences property<analysis-i-mono-seq-prop>`. $(S_n)$ is a monotonic increasing sequence that is bounded above, therefore it converges by the monotone sequences property.

</details>
<br>
    
There are several convergence tests that determine whether the series of a sequence converges, by comparing the sequnece's terms to those of another sequence. The simplest of these is the comparison test.
    
<div class="lemma">

**Lemma (Comparison test)** Let $(a_n)$ and $(b_n)$ be non-negative sequences, and suppose there exist $N, C$ such that for all $n \geq N$, $a_n \leq C b_n$. Then, if $\sum_{n = 1}^\infty b_n$ converges, so does $\sum_{n = 1}^\infty a_n$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Comparison test</summary>
    
Let $(a_n)$ and $(b_n)$ be non-negative sequences, and suppose there exist $N, C$ such that for all $n \geq N$, $a_n \leq C b_n$. We will show that the terms $S_R = \sum^R_{n = 1} a_n$ are bounded above. We have
    
$$\begin{align}
S_M - S_N = \sum^{M}_{n = N + 1} a_n \leq C \sum^{M}_{n = N + 1} b_n \leq C \sum^\infty_{n = N + 1} b_n,
\end{align}$$
    
and therefore, for all $M \geq N$ we have $S_M \leq S_N + \sum^\infty_{n = N + 1} b_n$. Since the $S_M$ are monotonic increasing and bounded, they must converge.

</details>
<br>
    
    
## Absolute convergence
    
Another notion of series convergence is absolute convergence. Absolute convergence is a stronger condition for convergence.
    
<div class="definition">

**Definition (Absolute convergence)** We say that the series $\sum^\infty_{n = 1} a_n$ converges absolutely if the series $\sum^\infty_{n = 1} |a_n|$ converges.
    
</div>
<br>
    
It is clear that if a series converges absolutely then the series itself converges, as stated by the lemma below.
    
<div class="lemma">

**Lemma (Absolute convergence)** Let $\sum^\infty_{n = 1} a_n$ converge absolutely. Then $\sum^\infty_{n = 1} a_n$ converges.

</div>
<br>


<details class="proof">
<summary>Proof: Absolute convergence</summary>
    
Let $\epsilon > 0$, $p > q$ and consider
    
$$|S_p - S_q| = \Bigg| \sum_{n = q + 1}^p a_n \Bigg| \leq \sum_{n = q + 1}^p |a_n| = U_p - U_q = |U_p - U_q|.$$
    
Since $U_N$ converges it is Cauchy, so we can find $M$ such that for all $p > q \geq M$
    
$$|S_p - S_q| \leq |U_p - U_q| < \epsilon,$$
    
which means that $S_N$ is Cauchy. Since $S_N$ is Cauchy it converges by {ref}`the general principle of convergence<analysis-i-cauchy-seqs>`.

</details>
<br>
    
Another notion of convergence is uncondtional convergence. If a series is unconditionally convergent, then the sum of any permutation of its terms converges.
    
<div class="definition">

**Definition (Unconditional convergence)** We say that the series $\sum^\infty_{n = 1} a_n$ converges unconditionally if for any bijection $\pi \mathbb{N} \to \mathbb{N}$, the series $\sum^\infty_{n = 1} a_{\pi(n)}$ converges.
    
</div>
<br>
    

<div class="lemma">

**Lemma (Absolute convergence $\iff$ unconditional convergence)** A series converges absolutely if and only if it converges unconditionally.

</div>
<br>
    
We present the proof broken into two parts.
    
<details class="proof">
<summary>Proof: Absolute convergence \(\implies\) unconditional convergence</summary>
    
Let $\pi \mathbb{N} \to \mathbb{N}$ be a bijection. We show that if the series $\sum^\infty_{n = 1} a_n$ converges absolutely, then $\sum^\infty_{n = 1} a_{\pi(n)}$ is Cauchy and that it has a convergent subsequence, {ref}`implying that that the later converges<analysis-i-cauchy-seqs>`.
    
Let $S_N = \sum^N_{n = 1} a_{\pi(n)}$ and consider
    
$$\begin{align}
|S_p - S_q| = \Bigg| \sum_{n = q + 1}^p a_{\pi(n)} \Bigg| \leq \sum_{n = q + 1}^p |a_{\pi(n)}|
\end{align}$$
    
where $p > q$. Let $\epsilon > 0$. Since $\sum^\infty_{n = 1} |a_n|$ converges, we can pick $M$ such that $\sum^\infty_{n = q + 1} |a_n| < \epsilon$. If we pick $N$ large enough such that $\{1, ..., M\} \subseteq \{\pi(1), ..., \pi(N)\}$, then for any $n > N$ we have $\pi(n) > M$. Therefore, for any $p > q > N$ we have $\{\pi(q + 1), ..., \pi(p)\} \subseteq \{M + 1, M + 2, ...\}$ and thus
    
$$\begin{align}
|S_p - S_q| \leq \sum_{n = q + 1}^p |a_{\pi(n)}| \leq \sum_{n = M + 1}^\infty |a_{\pi(n)}| < \epsilon,
\end{align}$$
    
therefore $S_N$ is Cauchy and converges by {ref}`the general principle of convergence<analysis-i-cauchy-seqs>`.

</details>
<br>
    
<details class="proof">
<summary>Proof: Unconditional convergence \(\implies\) absolute convergence</summary>
    
We prove that if a series does not converge absolutely, it does not converge unconditionally. Therefore, if a series converges unconditionally, it must be the case that it converges absolutely - otherwise a contradiction would be reached.
    
Suppose that $\sum^\infty_{n = 1} |a_n| = \infty$. Let $(b_n)$ and $(c_n)$ be the subsequences of non-negative and negative terms of the sequence $(a_n)$, respectively. Then either $\sum^\infty_{n = 1} b_n$ or $\sum^\infty_{n = 1} c_n$ must be unbounded because otherwise $\sum^\infty_{n = 1} |a_n|$ would converge. Without loss of generality, we can assume $\sum^\infty_{n = 1} b_n = \infty$. From here we can construct a sequence $0 = n_0 < n_1 < n_2 < ...$ such that for all $k$, the contribution of the terms $b_{n_{k - 1} + 1}$ through $b_{n_k}$, plus the term $c_k$ is larger than $1$, as in
    
$$\begin{align}
b_{n_{k - 1} + 1} + b_{n_{k - 1} + 2} + ... + b_{n_k} + c_k \geq 1.
\end{align}$$
    
This is possible because $\sum^\infty_{n = 1} b_n = \infty$. Letting $\pi$ be the above permutation of terms we arrive at $\sum^\infty_{n = 1} a_{\pi(n)} = \infty$ and therfore the series does not converge unconditionally.

</details>
<br>
    
If a series converges unconditionally, do all of its permutations converge to the same limit? The affirmative answer is stated and proved in the lemma below.
    

<div class="lemma">

**Lemma (Unconditional convergence $\implies$ unique limit)** If $\sum^\infty_{n = 1} a_n$ converges unconditionally, then
    
$$\begin{align}
\sum_{n = 1}^\infty a_n = \sum_{n = 1}^\infty a_{\pi(n)}.
\end{align}$$

</div>
<br>


<details class="proof">
<summary>Proof: Unconditional convergence \(\implies\) unique limit</summary>
    
If the series $\sum^\infty_{n = 1} a_n$ converges unconditionally, then it also converges absolutely. Let $\epsilon > 0$ and pick $M$ large enough such that
    
$$\begin{align}
\sum^\infty_{n = M + 1} |a_n| &< \frac{\epsilon}{2}, \\
\sum^\infty_{n = M + 1} a_{\pi(n)} &< \frac{\epsilon}{2}.
\end{align}$$
    
We can pick $N$ large enough such that
    
$$\begin{align}
\{1, ..., M\} \subseteq \{\pi(1), ..., \pi(N)\}, \\
\{\pi(1), ..., \pi(M)\} \subseteq \{1, ..., N\}.
\end{align}$$
    
Then for every $K \geq N$,
    
$$\begin{align}
\Bigg| \sum_{n = 1}^K a_n - \sum_{n = 1}^K a_{\pi(n)} \Bigg| \leq \sum_{n = M + 1}^K |a_n| - \sum_{n = M + 1}^K |a_{\pi(n)}| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
\end{align}$$
    
Since this holds for any $\epsilon > 0$ and $K \geq N$ we must have $\sum^\infty_{n = 1} a_n = \sum^\infty_{n = 1} a_{\pi(n)}$.

</details>
<br>
    
## Convergence tests
    
Appart from the comparison test, there are a lot of other useful convergence tests that we state and prove here.
    
    
<div class="lemma">

**Lemma (Alternating sequence test)** Let $(a_n)$ be a non-negative decreasing sequence with $a_n \to 0$. Then the alternating series
    
$$\begin{align}
\sum^\infty_{n = 1} (-1)^{n + 1} a_n,
\end{align}$$
    
converges.

</div>
<br>

<details class="proof">
<summary>Proof: Alternating sequence test</summary>
    
Consider the sequence
    
$$\begin{align}
S_N = \sum^N_{n = 1} (-1)^{n + 1} a_n.
\end{align}$$
    
The partial sums $S_{2n}$ and $S_{2n + 1}$ can be grouped as
    
$$\begin{align}
S_{2n} &= (a_1 - a_2) + (a_3 - a_4) + ...,
S_{2n + 1} &= a_1 - (a_2 - a_3) - (a_4 - a_5) + ...,
\end{align}$$
    
where the bracketed terms are all positive. The sequences $(S_{2n})$ and $(S_{2n + 1})$ are increasing and decreasing respectively and also
    
$$\begin{align}
0 \leq S_{2n} \leq S_{2n + 1} \leq a_1.
\end{align}$$
    
It follows from the monotonic sequences property that $(S_{2n})$ and $(S_{2n + 1})$ both converge and since $S_{2n + 1} - S_{2n} = a_{2n + 1} \to 0$, they converge to the same limit. Therefore $S_n$ also converges to that limit.

    
</details>
<br>
    
Below we state and prove three versions of the ratio test. The proofs rest on comparing the sequence in question to the geometric sum, which we know converges.
    
<div class="lemma">

**Lemma (Ratio test - version 1)** If there exists $c < 1$ such that
    
$$\begin{align}
\frac{|a_{n + 1}|}{|a_n|} \leq c,
\end{align}$$
    
for all $n$, then $\sum a_n$ converges absolutely.

</div>
<br>

<details class="proof">
<summary>Proof: Ratio test - version 1</summary>
    
Since $\frac{|a_{n + 1}|}{|a_n|} \leq c$ for all $n$, we have
    
$$\begin{align}
|a_n| \leq c^{n - 1} |a_1|.
\end{align}$$
    
Since $\sum c^{n - 1}$ converges when $|c| < 1$, $\sum |a_n|$ also converges {ref}`by the comparsion test<analysis-i-infinte-sums>` and $\sum a_n$ converges as well.

</details>
<br>
    
    
<div class="lemma">

**Lemma (Ratio test - version 2)** If there exists $c < 1$ and $N$ such that
    
$$\begin{align}
\frac{|a_{n + 1}|}{|a_n|} \leq c
\end{align}$$
    
for all $n > N$, then $\sum a_n$ converges.

</div>
<br>

<details class="proof">
<summary>Proof: Ratio test - version 2</summary>
    
Suppose there exists $c < 1$ and $N$ such that
    
$$\begin{align}
\frac{|a_{n + 1}|}{|a_n|} \leq c
\end{align}$$
    
for all $n > N$. Then the sum $\sum_{n = 1} a_{N + n}$ converges absolutely as proved in the previous lemma, and therefore $\sum_{n = 1}^N |a_n|$ converges as well.
    
</details>
<br>
    
    
<div class="lemma">

**Lemma (Ratio test - version 3)** If there exists $\rho \in (-1, 1)$ such that
    
$$\begin{align}
\frac{a_{n + 1}}{a_n} \to \rho,
\end{align}$$
    
for all $n > N$, then $\sum a_n$ converges.

</div>
<br>

<details class="proof">
<summary>Proof: Ratio test - version 3</summary>
    
Suppose there exists $\rho \in (-1, 1)$ such that
    
$$\begin{align}
\frac{a_{n + 1}}{a_n} \to \rho.
\end{align}$$
    
Then we have
    
$$\begin{align}
\frac{|a_{n + 1}|}{|a_n|} \to |\rho|,
\end{align}$$
    
which implies that there exists $N$ such that $\frac{|a_{n + 1}|}{|a_n|}$ is within $\epsilon = \frac{1 - |\rho|}{2}$ of $\rho$, implying that
    
$$\begin{align}
\frac{|a_{n + 1}|}{|a_n|} \to \frac{1 + |\rho|}{2} \leq 1,
\end{align}$$
    
and the result follows by the previous lemma.
    
</details>
<br>
    
The proof of the condensation test, stated below, includes an instructive trick of grouping sequence terms to enable comparison with another sequence.
    
<div class="theorem">

**Theorem (Condensation test)** Let $a_n$ be a decreasing non-negative sequence. Then $\sum^\infty_{n = 1} a_n < \infty$ if and only if
    
$$\begin{align}
\sum^\infty_{n = 1} 2^n a_{2^n} < \infty.
\end{align}$$

</div>
<br>

<details class="proof">
<summary>Proof: Condensation test</summary>
    
Since $(a_n)$ is decreasing we have
    
$$\begin{align}
\sum^\infty_{n = 1} a_n = &~a_1 + a_2 + (a_3 + a_4) + (a_5 + ... + a_8) + (a_9 + ... + a_{16}) + ... \\
\leq &~a_1 + a_2 + 2a_4 + 4a_8 + ... = a_1 + \sum^\infty_{n = 1} 2^{n - 1} a_{2^n}
\end{align}$$
    
which implies that if $\sum a_n$ converges, so does $\sum^\infty_{n = 1} 2^n a_{2^n}$. Going the other way around, we can write
    
$$\begin{align}
a_1 + \sum^\infty_{n = 1} 2^n a_{2^n} =&~a_1 + 2a_2 + 4a_4 + 8a_8 + ... \\
\leq &~a_1 + (a_2 + a_3) + (a_4 + a_5 + a_6 + a_7) + ... = \sum^\infty_{n = 1} a_n.
\end{align}$$

    
</details>
<br>
    
Although we have not formally defined the integral, that should be familiar to the reader, so we refer the following useful convergence test.
    
<div class="theorem">

**Theorem (Integral test)** Let $f : [1, \infty] \to \mathbb{R}$ be a decreasing non-negative function. Then
    
$$\begin{align}
\sum_{n = 1}^\infty f(n) < \infty \iff \int_1^\infty f(x) dx < \infty
\end{align}$$

</div>
<br>

<details class="proof">
<summary>Proof: Integral test</summary>
    
Since we have not yet defined formally defined the integral, we defer this proof for later.
    
</details>
<br>