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

**Corollary (Sine and cosine formulae)** We have
    
$$\begin{align}
\sin(z + w) = \sin(z)\cos(w) + \cos(z)\sin(w) ~~~\text{ and }~~~ \cos(z + w) = \cos(z)\cos(w) - \sin(z)\sin(w).
\end{align}$$
    
</div>
<br>


    
<details class="proof">
<summary>Proof: Sine and cosine formulae</summary>

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

**Lemma (Larger derivatve implies larger function value)** Suppose $f, g : \mathbb{R} \to \mathbb{R}$ are functions which are differentiable in the interval $[x_1, x_2]$, satisfying
    
$$\begin{align}
f(x_0) = g(x_0) ~~~\text{ and }~~~ f'(x) \geq g'(x) \text{ for all } x \in [x_1, x_2].
\end{align}$$
    
Then $f$ is larger than $g$ in this interval, that is
    
$$\begin{align}
x \in [x_1, x_2] \implies f(x) \geq g(x).
\end{align}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Larger derivatve implies larger function value</summary>

Suppose $f, g : \mathbb{R} \to \mathbb{R}$ satisfy
    
$$\begin{align}
f(x_1) = g(x_1) ~~~\text{ and }~~~ f'(x) \geq g'(x) \text{ for all } x \in [x_1, x_2].
\end{align}$$
    
Then the funtion $h(x) = f(x) - g(x)$ satisfies
    
$$\begin{align}
h(x_0) = 0 ~~~\text{ and }~~~ h'(x) \geq 0.
\end{align}$$
    
Now suppose there exists $x \in [x_1, x_2]$ such that $h(x) < 0$. Then, using the {ref}`mean value theorem<analysis-i-mean-value-theorem>` there exists $x_m$ such that
    
$$\begin{align}
h'(x_m) = \frac{h(x) - h(x_1)}{x - x_1} = \frac{h(x_m)}{x - x_1}.
\end{align}$$
    
However, $h'(x_m) \geq 0$ and $x - x_1 \geq 0$. If $x - x_1 > 0$ then $h(x_m) \geq 0$, in which case we reach a contradiction beause we have already assumed $h(x_m) < 0$. If $x - x_1 = 0$, then $h(x) = h(x_m) = h(x_1) = 0$, again reaching a contradiction because we have assumed $h(x_m) < 0$. Therefore, $h(x) \geq 0$ for all $x \in [x_1, x_2]$.
    
</details>
<br>
    
    


<div class="lemma">

**Lemma (Truncation of the sine and cosine power series)** Let $x \in \mathbb{R}^+$. If $N$ is even, then
    
$$\begin{equation}
\sin x \geq \sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{(2n + 1)!} ~~~~\text{ and }~~~~ \cos x \geq \sum_{n=0}^N (-1)^n \frac{x^{2n}}{(2n)!},
\end{equation}$$
    
If $N$ is odd, then
    
$$\begin{equation}
\sin x \leq \sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{(2n + 1)!} ~~~~\text{ and }~~~~ \cos x \leq \sum_{n=0}^N (-1)^n \frac{x^{2n}}{(2n)!}.
\end{equation}$$
    
That is, if we truncate the sine or cosine power series at a positive (negative) term, the truncated sum is larger (smaller) than the infinite series.
    
</div>
<br>
    


<details class="proof">
<summary>Proof: Truncation of the sine and cosine power series</summary>
    
    
First, define
    
$$\begin{equation}
v_N(x) = \sum_{n=0}^N (-1)^n \frac{x^{2n+1}}{(2n + 1)!} ~~~\text{ and }~~~ w_N(x) = \sum_{n=0}^N (-1)^n \frac{x^{2n}}{(2n)!},
\end{equation}$$
    
and note that for $N \geq 1$ it holds that
    
$$\begin{equation}
v_N'(x) = w_{N-1}'(x) ~~~\text{ and }~~~ w_N'(x) = -v_{N-1}'(x),
\end{equation}$$
    
and also for all $N \geq 0$ we have
    
$$\begin{equation}
\sin 0 = v_N(0) = 0 ~~~\text{ and }~~~ \cos 0 = w_N(0) = 0.
\end{equation}$$
    
Further, we have 
    
$$\begin{equation}
\sin^2 x + \cos^2 x = 1 \implies -1 \leq \sin x, \cos x \leq 1.
\end{equation}$$
    
Substituting $f(x) = v_0(x)$ and $g(x) = \sin x$ in the previous lemma, noting that $f(0) = g(0)$ and $f'(x) = 1 \geq \cos x = g'(x)$ we obtain $\sin x \leq v_0(x)$ for all $x \in [0, \infty)$.
Also, $\cos x \leq 1 = w_0(x)$ for all $x \in [0, \infty)$.

Proceeding in this fashion, subsituting $f(x) = \sin x$ and $g(x) = v_1(x)$ in the lemma, and noting that $f'(x) = \cos x \geq -w_0(x) = g'(x)$ we obtain $\sin x \leq v_1(x)$ for all $x \in [0, \infty)$.
Similarly, subsituting $f(x) = \cos x$ and $g(x) = w_1(x)$ in the lemma, and noting that $f'(x) = -\sin x \geq -v_1(x) = g'(x)$ we obtain $\cos x \geq w_1(x)$ for all $x \in [0, \infty)$.
    
Repeating this procedure iteratively we see that the result holds for all $N \geq 0$.
    
</details>
<br>
    
    
    
    

<div class="definition">

**Definition ($\pi$)** We define $\frac{\pi}{2}$ to be the smallest $x \geq 0$ such that $\cos x = 0$.
    
</div>
<br>
    
    
    
<details class="proof">
<summary>Note: The definition of \(\pi\)</summary>

The above definition for $\pi$ is sensible for the following reason. From the previous lemma, we have
    
$$\begin{equation}
\cos x \leq 1 - \frac{x^2}{2!} + \frac{x^4}{4!} \implies \cos 2 \leq 1 - 2 + \frac{2}{3} < 0.
\end{equation}$$
    
Also, because $\cos 0 = 1$, by the intermediate value theorem, there must exist some $x \in [0, 2]$ such that $\cos x = 0$. We define the smallest $x \in [0, 2]$ to be $\frac{\pi}{2}$.
    
</details>
<br>

Note also that since $\sin^2 x + \cos^2 x = 1$ and $\cos \frac{\pi}{2} = 0$ by definition, we have $\sin \frac{\pi}{2} = \pm 1$. Since $\sin 0 = 0$ and $\cos x \geq 0$ for $x \in \left[0, \frac{\pi}{2}\right]$, we have $\sin x \geq 0$ for $x \in \left[0, \frac{\pi}{2}\right]$, from which we see that $\sin \frac{\pi}{2} = 1$.

    
    

<div class="lemma">

**Lemma (Trigonometric identities with $\pi$)** The following trigonometric identities hold for all $x \in \mathbb{R}$
    
$$\begin{align}
&\sin \left(z + \frac{\pi}{2}\right) = \cos(z), && \cos \left(z + \frac{\pi}{2}\right) = -\sin(z), \\
&\sin \left(z + \pi\right) = -\sin(z), && \cos \left(z + \pi\right) = -\cos(z), \\
&\sin \left(z + 2\pi\right) = \sin(z), && \cos \left(z + 2\pi\right) = \cos(z).
\end{align}$$
    
</div>
<br>
    


<details class="proof">
<summary>Proof: Trigonometric identities with \(\pi\)</summary>
    
First, we have
    
$$\begin{align}
\sin \pi &= \sin \left(\frac{\pi}{2} + \frac{\pi}{2}\right) = 2\sin \frac{\pi}{2} \cos \frac{\pi}{2} = 0, \\
\sin 2\pi &= \sin \left(\pi + \pi\right) = 2 \sin \pi \cos \pi = 0,
\end{align}$$
    
and also
    
$$\begin{align}
\cos \pi = \cos \left(\frac{\pi}{2} + \frac{\pi}{2}\right) = \cos \frac{\pi}{2} \cos \frac{\pi}{2} - \sin \frac{\pi}{2}\sin \frac{\pi}{2} &= -1, \\
\cos 2\pi = \cos \left(\pi + \pi\right) = \cos \pi \cos \pi - \sin \pi \sin \pi &= 1.
\end{align}$$
    
Now using the identity
    
$$\begin{equation}
\sin (x_1 + x_2) = \sin x_1 \cos x_2 + \cos x_1 \sin x_2,
\end{equation}$$
    
and substituting $x_1 = x$ and $x_2 = \frac{\pi}{2}$ we have
    
$$\begin{equation}
\sin \left(x + \frac{\pi}{2}\right) = \sin x \cos \frac{\pi}{2} + \cos x \sin \frac{\pi}{2} = \cos x \sin \frac{\pi}{2} = \cos x.
\end{equation}$$
    
Substituting $x_1 = x$ and $x_2 = \pi$ or $x_2 = 2\pi$ we have
    
$$\begin{align}
\sin \left(x + \pi\right) &= \sin x \cos \pi + \cos x \sin \pi = -\sin x, \\
\sin \left(x + 2\pi\right) &= \sin x \cos 2\pi + \cos x \sin 2\pi = \sin x.
\end{align}$$
    
Similarly using the identity
    
$$\begin{equation}
\cos (x_1 + x_2) = \cos x_1 \cos x_2 - \sin x_1 \sin x_2,
\end{equation}$$
    
and substituting $x_1 = x$ and $x_2 = \frac{\pi}{2}$ we have
    
$$\begin{equation}
\cos \left(x + \frac{\pi}{2}\right) = \cos x \cos \frac{\pi}{2} - \sin x \sin \frac{\pi}{2} = - \sin x.
\end{equation}$$
    
Substituting $x_1 = x$ and $x_2 = \pi$ or $x_2 = 2\pi$ we have
    
$$\begin{align}
\cos \left(x + \pi\right) &= \cos x \cos \pi - \sin x \sin \pi = - \cos x, \\
\cos \left(x + 2\pi\right) &= \cos x \cos 2\pi - \sin x \sin 2\pi = \cos x.
\end{align}$$
    
</details>
<br>
    
    
    

## Differentiating power series
    
    
<div class="lemma">

**Lemma (A complex polynomial identity)** For any $a, b \in \mathbb{C}$, it holds that
    
$$\begin{equation}
b^n - a^n - n (b - a) a^{n-1} = (b - a)^2 (b^{n-2} + 2a b^{n-3} + \dots + (n-1)a^{n-2}).
\end{equation}$$
    
</div>
<br>
    
    


<details class="proof">
<summary>Proof: A complex polynomial identity</summary>
    
Suppose $a, b \in \mathbb{C}$. Then
    
$$\begin{equation}
b^n - a^n = (b - a) \big(b^{n-1} + a b^{n-2} + \dots + a^{n-1}\big).
\end{equation}$$
    
Subtracting $n(b - a) a^{n-1}$ we obtain
    
$$\begin{align}
b^n - a^n - n(b - a) a^{n-1} &= (b - a) \big(b^{n-1} - a^{n-1} + a (b^{n-2} - a^{n-2}) + \dots + a^{n-2}(b - a)\big) \\
                             &= (b - a)^2 \big(b^{n-2} + 2a b^{n-3} + \dots + (n-1)a^{n-2}\big)
\end{align}$$
    
as required.
    
    
</details>
<br>
    
    
    
    

    
    
<div class="lemma">

**Lemma (Sum of derivatives of power series terms converges)** Let $a_n z^n$ have radius of convergence $R$. Then for all $|z| < R$, the series with terms $na_nz^{n-1}$ converges absolutely.
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Sum of derivatives of power series terms converges</summary>
    
Suppose $a_n z^n$ has radius of convergence $R$ and $z \in \mathbb{C}, r \in \mathbb{R}^+$ b such that $|z| < r < R$. Since $a_n z^n$ has radius of convergence $R$ and $0 < r < R$, the terms $|a_n| r^n$ must be bounded above by some $C \in \mathbb{R}^+$. Therefore
    
$$\begin{align}
\sum_{n = 0}^\infty n |a_n z^{n-1}| &= \sum_{n = 0}^\infty n |a_n| r^{n-1} \left(\frac{|z|}{r}\right)^{n-1} \\
                                    &= \frac{1}{r} \sum_{n = 0}^\infty n |a_n| r^n \left(\frac{|z|}{r}\right)^{n-1} \\
                                    &\leq \frac{C}{r} \sum_{n = 0}^\infty n \left(\frac{|z|}{r}\right)^{n-1}
\end{align}$$
   
and the last term is converges by the ratio test, so $n |a_n z^{n-1}|$ also converges by the comparison test. Therefore, $na_nz^{n-1}$ converges absolutely.
    
    
</details>
<br>
    
    
A corollary of the above lemma is that if $a_n z^n$ has radius of convergence $R$, then for all $|z| < R$, the series
    
$$\begin{equation}
\sum_{n=0}^\infty a_n {n \choose 2} z^{n-1},
\end{equation}$$
    
converges absolutely. We can see this by applying the previous lemma twice and dividing the resulting series by two.
    
    

    
<div class="theorem">

**Theorem (Derivative of power series)** Let $a_n z^n$ have radius of convergence $R$. For $|z| < R$, let
    
$$\begin{equation}
f(z) = \sum_{n=0}^\infty a_n z^n ~~~\text{ and }~~~ g(z) = \sum_{n=1}^\infty na_n z^{n-1}.
\end{equation}$$
    
Then $f$ is differentiable with derivative $g$.
    
</div>
<br>
    
    
<details class="proof">
<summary>Proof: Derivative of power series</summary>
    
Let $a_n z^n$ have radius of convergence $R$ and consider
    
$$\begin{equation}
f(z + h)- f(z) - hg(z) = \sum_{n=2}^\infty a_n \left((z + h)^n - a_n z^n - hnz^{n-1}\right).
\end{equation}$$
    
Using one of the previous lemmas, we have
    
$$\begin{equation}
f(z + h)- f(z) - hg(z) = \sum_{n=2}^\infty h^2 a_n  \big((z+h)^{n-2} + 2z(z+h)^{n-3} + \dots + (n-1)z^{n-2} \big).
\end{equation}$$
    
Since $a_n z^n$ has radius of convergence $R$, for small enough $h$, there exists $r$ such that $|r + h| < r < R$, so
    
$$\begin{align}
f(z + h)- f(z) - hg(z) &\leq h^2 \sum_{n=2}^\infty |a_n| \big(r^{n-2} + 2r^{n-3} + \dots + (n-1)r^{n-2} \big) \\
                       &= \frac{h^2}{r} \sum_{n=2}^\infty |a_n| {n \choose 2} r^{n-1}.
\end{align}$$
    
By the previous corollary, the series on the right hand side converges absolutely and is therefore bounded. Thus
    
$$\begin{equation}
f(z + h)- f(z) - hg(z) \leq h^2 C(z)
\end{equation}$$
    
for some $C(z)$, which implis that $f(z + h)- f(z) - hg(z) = o(z)$. Therefore $g$ is the derivative of $f$.
    
</details>
<br>
    
    
## Hyperbolic series
    

<div class="definition">

**Definition (Hyperbolic sine and cosine)** We define the hyperbolic sine and cosine as
    
$$\begin{align}
\sinh z &= z + \frac{z^3}{3!} + \frac{z^5}{5!} + \dots \\
\cosh z &= 1 + \frac{z^2}{2!} + \frac{z^4}{4!} + \dots.
\end{align}$$
    
</div>
<br>

    
    
<div class="lemma">

**Lemma (Derivatives of sinh and cosh)** We have
    
$$\begin{align}
\frac{d}{dz} \sinh z &= \cosh z \\
\frac{d}{dz} \cosh z &= \sinh z.
\end{align}$$
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Derivatives of sinh and cosh</summary>
    
From the previous lemma on the derivatives of power series we have
    
$$\begin{align}
\frac{d}{dz} \sinh z &= \frac{d}{dz} \left[z + \frac{z^3}{3!} + \frac{z^5}{5!} + \dots \right] \\
                     &= 1 + \frac{z^2}{2!} + \frac{z^4}{4!} + \dots \\
                     &= \cosh z.
\end{align}$$
    
Similarly, we have

$$\begin{align}
\frac{d}{dz} \cosh z &= \frac{d}{dz} \left[1 + \frac{z^2}{2!} + \frac{z^4}{4!} + \dots \right] \\
                     &= z + \frac{z^3}{3!} + \frac{z^5}{5!} + \dots \\
                     &= \sinh z,
\end{align}$$
    
as required.
    
</details>
<br>

    
    
    
<div class="lemma">

**Lemma (Hyperbolic trigonometrics of imaginary numbers)** We have
    
$$\begin{align}
\sinh iz &= i\sin z, \\
\cosh iz &=  \cos z
\end{align}$$

    
</div>
<br>

<details class="proof">
<summary>Proof: Hyperbolic trigonometrics of imaginary numbers</summary>
    
By the definition of the sine and the hyperbolic sine we have
    
$$\begin{align}
\sinh iz &= iz - i\frac{z^3}{3!} + i\frac{z^5}{5!} + \dots, \\
         &= i\sin z.
\end{align}$$
    
Similarly, by the definition of the cosine and the hyperbolic cosine we have
    
$$\begin{align}
\cosh iz &= 1 - \frac{z^2}{2!} + \frac{z^4}{4!} + \dots, \\
         &= \cos z.
\end{align}$$
    
</details>
<br>

    
    
<div class="lemma">

**Lemma (Hyperbolic sine and cosine identity)** We have
    
$$\begin{equation}
\cosh^2 z - \sinh^2 z = 1.
\end{equation}$$
    
</div>
<br>

<details class="proof">
<summary>Proof: Hyperbolic sine and cosine identity</summary>
    
We have
    
$$\begin{equation}
\cosh^2 z - \sinh^2 z = \cos^2 iz + \sin^2 iz = 1.
\end{equation}$$
    
</details>
<br>