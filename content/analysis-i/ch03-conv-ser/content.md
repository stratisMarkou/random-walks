# Convergence of infinite sums

This section introduces infinite sums and presents results regarding their convergence.

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
    
We will show that $S_N = \sum^N_{n = 1} a_n$ has a convergent subsequence and that it is Cauchy, {ref}`which implies that the series converges<analysis-i-cauchy-seqs>`. Since $S_N = \sum^N_{n = 1} a_n$ is absolutely convergent, the series $U_N = \sum^N_{n = 1}|a_n|$ and $L_N = \sum^N_{n = 1} -|a_n|$ converge to limits $U$ and $V$. The series $U_N$ and $V_N$ are increasing and decreasing respectively, so $U_N \leq U$ and $L_N \geq L$ so
    
$$\begin{align}
L \leq L_N \leq S_N \leq U_N \leq U.
\end{align}$$
    
Therefore $S_N$ is bounded and by {ref}`Bolzano-Weierstrass<analysis-i-bolz-weier>` it has a convergent subsequence. Now let $\epsilon > 0$, $p > q$ and consider
    
$$|S_p - S_q| = \Bigg| \sum_{n = q + 1}^p a_n \Bigg| \leq \sum_{n = q + 1}^p |a_n| = U_p - U_q = |U_p - U_q|.$$
    
Since $U_N$ converges it is Cauchy, so we can find $M$ such that for all $p > q \geq M$
    
$$|S_p - S_q| \leq |U_p - U_q| < \epsilon,$$
    
which means that $S_N$ is Cauchy. Since $S_N$ is Cauchy and has a convergent subsequence, it converges.

</details>
<br>
    
