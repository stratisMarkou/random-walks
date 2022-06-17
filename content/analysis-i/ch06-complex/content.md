# Complex Power Series

<div class="definition">

**Definition (Complex power series)** A complex power series is a series of the form
    
$$\begin{equation}
\sum^\infty_{n=0} a_n z^n,
\end{equation}$$
    
where $z \in \mathbb{C}$ and $a_n \in \mathbb{C}$ for all $n$.
    
</div>
<br>



<div class="lemma">

**Lemma (Sandwich convergence test)** Suppose that the power series $\sum^\infty_{n=0} a_n z^n$ converges, and let $|w| < |z|$. Then $\sum^\infty_{n=0} a_n w^n$ converges absolutely.
    
</div>
<br>

<details class="proof">
<summary>Proof: Sandwich convergence test</summary>
    
Suppose that the power series $\sum^\infty_{n=0} a_n z^n$ converges, and let $|w| < |z|$. Then, we have
    
$$\begin{align}
\sum^\infty_{n=0} |a_n w^n| &\leq \phantom{C} \sum^\infty_{n=0} \left|a_n z^n \frac{w^n}{z^n}\right|, \\
                            &\leq \phantom{C} \sum^\infty_{n=0} |a_n z^n|\left|\frac{z^n}{w^n} \right|, \\
                            &\leq \phantom{C} \sum^\infty_{n=0} C \left|\frac{z^n}{w^n} \right| \to \ell, \\
                            &\leq C \sum^\infty_{n=0} \left|\frac{z^n}{w^n} \right| \to \ell,
\end{align}$$
    
where we have used the fact that $a_n z^n$ must be bounded by some $C$ because the series $\sum^\infty_{n=0} a_n z^n$ converges.
    
</details>
<br>


<div class="definition">

**Definition (Radius of convergence)** The radius of convergence of a power series $\sum^\infty_{n=0} a_n z^n$ is defined as
    
$$\begin{equation}
R = \sup \left\{|z| : \sum^\infty_{n=0} a_n z^n \text{ converges} \right\}.
\end{equation}$$
    
</div>
<br>



<div class="lemma">

**Lemma (Formula for radius of convergence)** The radius of convergence of a power series $\sum^\infty_{n=0} a_n z^n$ is
    
$$\begin{equation}
R = \frac{1}{\lim \sup \sqrt[n]{|a_n|}}.
\end{equation}$$
    
</div>
<br>

<details class="proof">
<summary>Proof: Formula for radius of convergence</summary>

Suppose $\sum^\infty_{n=0} a_n z^n$ is a complex power series and let $z$ satisfy
    
$$\begin{equation}
|z| < \frac{1}{\lim \sup \sqrt[n]{|a_n|}}.
\end{equation}$$
    
Then by rearranging we have
    
$$\begin{equation}
|z| \lim \sup \sqrt[n]{|a_n|} < 1,
\end{equation}$$
    
which implies that there exists $N$ such that for all $n > N$ we have
    
$$\begin{equation}
|z| \sup_{n \geq N} \sqrt[n]{|a_n|} < 1 - \epsilon \implies |a_n z^n| < (1 - \epsilon)^n.
\end{equation}$$
    
By comparing the above with a geometric series, we see that $\sum^\infty_{n=0} a_n z^n$ converges absolutely.
    
</details>
<br>


## Exponential function

<div class="definition">

**Definition (Exponential funtion)** The exponential function is defined as
    
$$\begin{equation}
e^z = \sum_{n=0}^\infty \frac{z^n}{n!},
\end{equation}$$
    
which converges for all $z \in \mathbb{C}$ by the ratio test.
    
</div>
<br>



<div class="definition">

**Definition (Convolution)** Given two sequences $(a_n)$ and $(b_n)$, their convolution $(c_n)$ is the sequence defined as
    
$$ c_n = a_0 b_n + a_1 b_{n-1} + \dots + a_{n-1} b_1 + a_n b_0. $$
    
</div>
<br>



<div class="lemma">

**Lemma (Absolute convergence of convolution)** Let $\sum^\infty_{n=0} a_n$ and $\sum^\infty_{n=0} b_n$ be two absolutely convergent series, and let $(c_n)$ be the convolution of $(a_n)$ and $(b_n)$. Then $\sum^\infty_{n=0} c_n$ converges absolutely and
    
$$ \sum^\infty_{n=0} c_n = \left( \sum^\infty_{n=0} a_n \right) \left( \sum^\infty_{n=0} b_n \right). $$
    
</div>
<br>

<details class="proof">
<summary>Proof: Absolute convergence of convolution</summary>

First, let us define
    
$$ S_N = \sum_{n=0}^N a_n, ~~ T_N = \sum_{n=0}^N b_n, ~~ U_N = \sum_{n=0}^N |a_n|, ~~ V_N = \sum_{n=0}^N |b_n|, $$
   
suppose that $S_N$ and $T_N$ converge absolutely and let
    
$$ S_N \to S, ~~ T_N \to T, ~~ U_N \to U, ~~ V_N \to V. $$
    
Since $S_N \to S$ and $T_N \to T$, we have $S_N T_N \to ST$. Also, we have
    
$$\begin{align}
S_N T_N = a_0 b_0 + (a_0 b_1 + a_1 b_1 + a_1 b_0) + \dots + (a_N b_0 + a_{N-1} b_1 + \dots + a_1 b_{N-1} + a_0 b_N).
\end{align}$$

Since $U_N \to U$ and $V_N \to V$, we have $U_NV_N \to UV$. Also, we have
    
$$\begin{align}
U_N V_N &= |a_0| |b_0| + \\
        &~~~ + (|a_0| |b_1| + |a_1| |b_1| + |a_1| |b_0|) \\
        &~~~~ \vdots \\
        &~~~ + (|a_N| |b_0| + |a_{N-1}| |b_1| + \dots + |a_1| |b_{N-1}| + |a_0||b_N|)
\end{align}$$
    
and since $U_N V_N \to UV$, the series
    
$$\begin{align}
S_N T_N &= a_0 b_0 + (a_0 b_1 + a_1 b_1 + a_1 b_0) + \dots (a_N b_0 + a_{N-1} b_1 + \dots + a_1 b_{N-1} + a_0 b_N)
\end{align}$$
    
converges absolutely, and therefore also converges unconditionally. This implies that the rearrangement
    
$$\begin{align}
\sum_{n=0}^N c_n = a_0 b_0 + (a_0 b_1 + a_1 b_0) + (a_0 b_2 + a_1 b_1 + a_2 b_0) + \dots
\end{align}$$
    
also converges to $ST$, so
    
$$\begin{align}
\sum_{n=0}^N c_n \to ST = \left( \sum^\infty_{n=0} a_n \right) \left( \sum^\infty_{n=0} b_n \right).
\end{align}$$
    
</details>
<br>



<div class="lemma">

**Corollary (Product of exponentials is exponential of sum)** For any $z, w \in \mathbb{C}$ we have
    
$$\begin{align}
e^{z+w} = e^z e^w.
\end{align}$$
    
</div>
<br>


<details class="proof">
<summary>Proof: Product of exponentials is exponential of sum</summary>

Suppose that $z, w \in \mathbb{C}$. Then, by the previous lemma
    
$$\begin{align}
e^z e^w &= \left( \sum_{n=0}^\infty \frac{z^n}{n!} \right) \left( \sum_{n=0}^\infty \frac{w^n}{n!} \right) \\
        &= \sum_{n=0}^\infty \left( \frac{1}{n!} \frac{1}{0!} z^n + \frac{1}{(n-1)!} \frac{1}{1!} z^{n-1}w + \dots + \frac{1}{1!} \frac{1}{(n-1)!} zw^{n-1} + \frac{1}{0!} \frac{1}{(n-1)!} w^n \right) \\
        &= \sum_{n=0}^\infty \frac{\left( z + w \right)^n}{n!} \\
        &= e^{z+w}.
\end{align}$$
    
</details>
<br>



<div class="lemma">

**Corollary (Derivative of exponential)** The derivative of $f(x) = e^x$ is $f(x)$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Derivative of exponential</summary>

Let $f(x) = e^x$. By the definition of the derivative
    
$$\begin{equation}
f'(x) = \lim_{h \to 0} \frac{e^{x + h} - e^x}{h} = \lim_{h \to 0} \frac{e^xe^h - e^x}{h} = e^x \lim_{h \to 0} \frac{e^h - 1}{h} = e^x \lim_{h \to 0} \frac{h + o(h)}{h} = e^x,
\end{equation}$$
    
where we have used the previous lemma and the definition of $e^x$.
    
</details>
<br>



## Trigonometric functions

<div class="definition">

**Definition (Sine and cosine)** We define the $\sin : \mathcal{C} \to \mathcal{C}$ and $\cos : \mathcal{C} \to \mathcal{C}$ functions as
    
$$\begin{align}
\sin z &= \frac{e^{iz} - e^{-iz}}{2i} = z - \frac{z^3}{3!} + \frac{z^5}{5!} + \dots, \\
& \\
\cos z &= \frac{e^{iz} + e^{-iz}}{2} = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} + \dots.
\end{align}$$
    
</div>
<br>


<div class="lemma">

**Corollary (Derivative of the sine and cosine)** We have
    
$$\begin{align}
\frac{d}{dz} \sin z &= \cos z, \\
\frac{d}{dz} \cos z &= -\sin z, \\
\sin^2 z + \cos^2 z &= 1.
\end{align}$$
    
</div>
<br>


    
<details class="proof">
<summary>Proof: Derivative of the sine and cosine</summary>

We have already shown that
    
$$\begin{equation}
\frac{d}{dz} e^z = e^z,
\end{equation}$$
   
and applying this to the definitions of the sine and the cosine we obtain
   
$$\begin{align}
\frac{d}{dz} \sin z &= \frac{ie^{iz} + ie^{-iz}}{2i} = \frac{e^{iz} + e^{-iz}}{2} = \cos z, \\
& \\
\frac{d}{dz} \cos z &= \frac{ie^{iz} - ie^{-iz}}{2} = \frac{e^{iz} - e^{-iz}}{2i} = \sin z.
\end{align}$$
    
Also, by the definition of the sine and the cosine
    
$$\begin{align}
\sin^2 z + \cos^2 z = - \frac{e^{i2z} - 2 + e^{-i2z}}{4} + \frac{e^{i2z} + 2 + e^{-i2z}}{4} = 1.
\end{align}$$
    
</details>
<br>




<div class="lemma">

**Corollary (Sine and cosine formula)** We have
    
$$\begin{align}
\sin(z + w) &= \sin(z)\cos(w) + \cos(z)\sin(w), \\
\cos(z + w) &= \cos(z)\cos(w) - \sin(z)\sin(w).
\end{align}$$
    
</div>
<br>


    
<details class="proof">
<summary>Proof: Sine and cosine formula</summary>

From the definition of the sine and cosine we have
    
$$\begin{align}
\sin(z)\cos(w) + \cos(z)\sin(w) &= \frac{e^{iz} - e^{-iz}}{2i} \frac{e^{iw} + e^{-iw}}{2} + \frac{e^{iz} + e^{-iz}}{2} \frac{e^{iw} - e^{-iw}}{2i} \\
                                &= \frac{e^{iz + iw} - e^{-iz + iw} + e^{iz - iw} - e^{-iz - iw}}{4i} + \\
                                &~~~~~~~~~~~~~+ \frac{e^{iz + iw} + e^{-iz + iw} - e^{iz - iw} - e^{-iz - iw}}{4i} \\
                                &= \frac{e^{iz + iw} - e^{-iz - iw}}{2i} \\
                                &= \sin(z + w).
\end{align}$$
    
    
Similarly, we also have
    
$$\begin{align}
\cos(z)\cos(w) - \sin(z)\sin(w) &= \frac{e^{iz} + e^{-iz}}{2} \frac{e^{iw} + e^{-iw}}{2} - \frac{e^{iz} - e^{-iz}}{2i} \frac{e^{iw} - e^{-iw}}{2i} \\
                                &= \frac{e^{iz + iw} + e^{iz - iw} + e^{-iz + iw} + e^{-iz - iw}}{4} + \\
                                &~~~~~~~~~~~~~+ \frac{e^{iz + iw} - e^{iz - iw} - e^{-iz + iw} + e^{-iz - iw}}{4} \\
                                &= \frac{e^{iz + iw} + e^{-iz - iw}}{2} \\
                                &= \cos(z + w).
\end{align}$$
    
</details>
<br>






<div class="lemma">

**Corollary (Truncation of the sine and cosine power series)** Let $x \in \mathbb{R}^+$. If $N$ is even, then
    
$$\begin{equation}
\sin x \leq \sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{(2n + 1)!} ~~~~\text{ and }~~~~ \cos x \leq \sum_{n=0}^N (-1)^n \frac{x^{2n}}{(2n)!},
\end{equation}$$
    
If $N$ is odd, then
    
$$\begin{equation}
\sin x \geq \sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{(2n + 1)!} ~~~~\text{ and }~~~~ \cos x \geq \sum_{n=0}^N (-1)^n \frac{x^{2n}}{(2n)!}.
\end{equation}$$
    
That is, if we truncate the sine or cosine power series at a positive (negative) term, the truncated sum is larger (smaller) than the infinite series.
    
</div>
<br>