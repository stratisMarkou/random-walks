# Main limit theorems

## Convergence in mean-square and law of large numbers

<div class='definition'>

**Definition (Mean square convergence)** We say that a sequence of random variables $Z_1, Z_2, ...$ converges in mean square to a limit variable $Z$ if 
 
  $$\begin{align}
  \mathbb{E}\left((Z_n - Z)^2\right) \to 0 \text{ as } n \to \infty,
  \end{align}$$

and write this as $Z_n \to Z$ in mean square as $n \to \infty$.

</div>
<br>

<div class='theorem'>

**Theorem (Mean square law of large numbers)** Let $X_1, X_2, ...$ be a sequence of independent random variables each with mean $\mu$ and variance $\sigma^2$. Then
 
 $$\begin{align}
 \frac{1}{N}\sum_{n = 1}^N X_n \to \mu \text{ as } n \to \infty \text{ in mean square}.
 \end{align}$$

</div>
<br>

<br>


<details class="proof">
<summary>Proof: Mean-square law of large numbers</summary>

The partial sum $S_N = X_1 + X_2 + ... + X_N$ has mean
    
$$\begin{align}
\mathbb{E}\left(\frac{1}{N}S_N\right) &= \frac{1}{N}\left[\sum_{n = 1}^N X_n\right] = \mu
\end{align}$$
    
and variance
    
$$\begin{align}
\text{Var}\left(\frac{1}{N} S_N\right) &= \frac{1}{N^2}\left[\mathbb{E}(S_N^2) - \mathbb{E}(S_N)^2\right]\\
&= \frac{1}{N} \sigma^2.
\end{align}$$
    
Where in the first line we used the fact $\text{Var}(aX) = a^2\text{Var}(X)$. Therefore as $N \to \infty$, $S_N \to \mu$ in mean square.

</details>
<br>

## Convergence in probability and weak law of large numbers


<div class='definition'>

**Definition (Convergence in probability)** We say that a sequence of random variables $Z_1, Z_2, ...$ converges in probability to $Z$ as $n \to \infty$ if for all $\epsilon > 0$
    
  $$\begin{align}
  \mathbb{P}\left(|Z_n - Z| > \epsilon\right) \to 0, \text{ as } n \to \infty,
  \end{align}$$
    
and write this as $Z_n \to Z$ in probability as $n \to \infty$.

</div>
<br>


<div class='theorem'>

**Theorem (Conv. in mean square $\implies$ conv. in probability)** If $Z_1, Z_2, ...$ is a sequence of random variables and $Z_n \to Z$ in mean square, then $Z_n \to Z$ in probability.

</div>

<br>


<details class="proof">
<summary>Proof: Convergence in mean square \(\implies\) convergence in probability</summary>

To show this result, we use Chebyshev's inequality
    
$$\begin{align}
\mathbb{P}(|X| \geq t) \leq \frac{\mathbb{E}\left(X^2\right)}{t^2},
\end{align}$$
    
which proved below. Now set $X_n = Z_n - Z$ and $t = \epsilon > 0$ and let $n \to \infty$ to obtain
    
$$\begin{align}
\mathbb{P}(|Z_n - Z| \geq \epsilon) \leq \frac{\mathbb{E}\left((Z_n - Z)^2\right)}{\epsilon^2} \to 0 \text{ as } n \to \infty,
\end{align}$$
    
where we have used the assumption that $Z_n \to Z$ in mean square, so $\mathbb{P}\left(|Z_n - Z| \geq \epsilon\right) \to 0$ as $n \to \infty$.

</details>
<br>


<div class='theorem'>

**Theorem (Chebyshev's inequality)** If $X$ is a random variable and $\mathbb{E}\left(X^2\right)$ is finite then
 
 $$\begin{align}
 \mathbb{P}(|X| \geq t) \leq \frac{\mathbb{E}\left(X^2\right)}{t^2}.
 \end{align}$$

</div>
<br>

<div class='theorem'>

**Theorem (Weak law of large numbers)** Let $X_1, X_2, ...$ be a sequence of independent random variables each with mean $\mu$ and variance $\sigma^2$. Then
 
 $$\begin{align}
 \frac{1}{N}\sum_{n = 1}^N X_n \to \mu \text{ as } n \to \infty \text{ in probability}.
 \end{align}$$

</div>
<br>


<details class="proof">
<summary>Proof: Weak law of large numbers</summary>

We have shown that as \(N \to \infty\), the partial sum
    
$$\begin{align}
S_N = X_1 + X_2 + ... + X_N
\end{align}$$
    
converges to $\mu$ in mean square. Convergence in mean square implies convergence in probability, therefore $S_N$ converges to $\mu$ in probability too.
    

</details>
<br>


Unlike the mean-square law of large numbers, the weak law holds even when $\sigma^2$ is infinite, provided that the $X_n$ all come from the same distribution - this result is proved at the end of this chapter.


## Central limit theorem

<div class='theorem'>

**Theorem (Central limit theorem)** Let $X_1, X_2, ...$ be a sequence of independent and identically distributed random variables, each with mean $\mu$ and variance $\sigma^2$. Then the random variable
 
 $$\begin{align}
 Z_N = \frac{S_N - N\mu}{\sqrt{N}\sigma}, \text{ where } S_N = X_1 + X_2 + ... + X_N
 \end{align}$$
    
 satisfies, as $N \to \infty$,
    
 $$\begin{align}
 \mathbb{P}(Z_N \leq z) \to \int^z_{-\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2} du, \text{ for } x \in \mathbb{R}.
 \end{align}$$

</div>
<br>

<div class='theorem'>

**Theorem (Continuity theorem with mgfs)** Let $X_1, X_2, ...$ be a sequence of random variables with moment generating functions $M_1, M_2 ...$ and suppose that as $n \to \infty$
 
 $$\begin{align}
 M_n(t) \to e^{\frac{1}{2}t^2} \text{ for } t \in \mathbb{R}
 \end{align}$$
    
 Then
    
 $$\begin{align}
 \mathbb{P}(Z_n \leq z) \to \int^z_{-\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2} du, \text{ for } x \in \mathbb{R}.
 \end{align}$$

</div>
<br>



<details class="proof">
<summary>Proof: Central limit theorem</summary>

Let $U_n = X_n - \mu$, so that the $U_n$ are independent and identically distributed with mean $0$ and variance $\sigma^2$. We will show that the mgf of 
    
$$\begin{align}
Z_N = \frac{S_N - N\mu}{\sigma\sqrt{N}}, \text{ where } S_N = X_1 + X_2 + ... + X_N
\end{align}$$
    
converges to the mgf of the standard normal. Then, by applying the continuity theorem for mgfs, the distribution function of $Z_N$ converges to the standard normal distribution. Writing out the mgf of $Z_N$
    
$$\begin{align}
M_{Z_N}(t) &= \mathbb{E}\left(\exp(tZ_N)\right)\\
&= \mathbb{E}\left[\exp\left(\frac{t}{\sqrt{N}\sigma} \sum^N_{n=1} U_n \right)\right]\\
&= \left[ M_U\left(\frac{t}{\sigma\sqrt{N}}\right) \right]^N
\end{align}$$
    
where we have used the fact that the mgf of a sum of independent random variables ($U_n$ in this case) is equal to the product of the mgfs of the random variables. Now, taking the Taylor expansion of $M_{U_n}(t)$ about $0$
    
$$\begin{align}
M_{U_n}(t) &= 1 + t\mathbb{E}(U_n) + \frac{1}{2}t^2\mathbb{E}(U_n^2) + o(t^2)\\
&= 1 + \frac{1}{2} \sigma^2 t^2 + o(t^2)
\end{align}$$
    
so that 
    
$$\begin{align}
M_{Z_N}(t) = \left[ 1 + \frac{1}{2} \frac{t^2}{N} + o\left(\frac{1}{N}\right) \right]^N \to e^{\frac{1}{2}t^2} \text{ as } N \to \infty.
\end{align}$$
    
Therefore $M_{Z_N}(t) \to e^{\frac{1}{2}t^2}$ as $N \to \infty$ and by the continuity theorem for mgfs, the distribution function of $Z_N$ converges to the standard normal distribution:
    
$$\begin{align}
\mathbb{P}(Z_N \leq z) \to \int^z_{-\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}u^2} du, \text{ for } x \in \mathbb{R}.
\end{align}$$

</details>
<br>


## Large deviations

We are sometimes interested in the probability that a sum of i.i.d. random variables $S_N = X_1 + X_2 + ... + X_N$ will deviate from its mean by an amount proportional to $N$, i.e. $\mathbb{P}(S_N - \mu N > aN)$. The large deviation theorem relates the probability of a large deviation to a quantity called the Fenchel-Legendre transform, defined below.

<div class='definition'>

**Definition (Fenchel-Legendre transform)** Given a random variable $X$, with moment generating function $M$, its Fenchel-Legendre transform is
    
  $$\begin{align}
  \Lambda^*(a) = \sup\left\{at - \Lambda(t) : t \in \mathbb{R}\right\}, \text{ where } a \in \mathbb{R},
  \end{align}$$
    
where $\Lambda(t) = \log M(t)$.

</div>
<br>

The large deviation theorem then takes the following form.

<div class='theorem'>

**Theorem (Large deviation theorem)** Let $X_1, X_2, ...$ be independent, identically distributed random variables with mean $0$ and a common generating function $M(t) = \mathbb{E}(e^{tX})$ which is finite in some neighbourhood $[-\delta, \delta]$ of the origin. Let $a > 0$ be such that $\mathbb{P}(X > a) > 0$. Then $\Lambda^*(a) > 0$ and
    
   $$\begin{align}
   \frac{1}{N} \log \mathbb{P}(S_N > aN) \to - \Lambda^*(a), \text{ as } N \to \infty.
   \end{align}$$

</div>
<br>

The proof of this theorem can be found in *Probability and Random Processes*{cite}`grimstir` (section 5.11), but is ommitted from the book and these notes. Instead we prove below that

$$\begin{align}
\frac{1}{N}\log\mathbb{P}(S_N > aN) \leq -\Lambda^*(a).
\end{align}$$


<details class="proof">
<summary>Proof: Partial proof of the large deviation theorem</summary>
    
Let $X_1, X_2, ...$ be a sequence of independent and identically distributed random variables with zero mean and common moment generating function $M(t)$, and define $S_N = X_1 + ... + X_N$. For any strictly increasing function $g(\cdot) : \mathbb{R} \to \mathbb{R}$, we have
  
$$\begin{align}
S_N > aN \iff g(S_N) > g(aN).
\end{align}$$

The exponential function $g(x) = e^x$ is strictly increasing and in addition it is non-negative, so
    
$$\begin{align}
\mathbb{P}(S_N > aN) = \mathbb{P}(g(tS_N) > g(taN)) \leq \frac{M(t)^N}{e^{taN}}, \text{ for } t > 0,
\end{align}$$
    
by the {ref}`Markov inequality <prob-intro-markov-jensen>`. Minimising over $t$ we obtain
    
$$\begin{align}
\mathbb{P}(S_N > aN) \leq \inf \left\{ \frac{M(t)}{e^{ta}} : \text{ for } t > 0 \right\}^N
\end{align}$$
    
Taking a logarithm of each side, we arrive at the result
    
$$\begin{align}
\frac{1}{N}\log \mathbb{P}(S_N > aN) \leq - \sup \left\{ ta - \Lambda(t) : \text{ for } t > 0 \right\} = - \Lambda^*(a).
\end{align}$$
    
</details>
<br>
    
## Convergence in distribution
    
<div class='definition'>

**Definition (Convergence in distribution)** The sequence $X_1, X_2, ...$ is said to converge in distribution, or to converge weakly, to $X$ as $n \to \infty$ if
    
  $$\begin{align}
  \mathbb{P}(X_n \leq x) \to \mathbb{P}(X \leq x), \text{ for any } x \in C,
  \end{align}$$
    
where $C$ is the set of reals at which the distribution function of $X$ is continuous. If the above holds, we write $X_n \implies X$.

</div>
<br>
    
Convergence in distribution is a weaker condition than convergence in probability. If the condition $x \in \mathbb{R}$ was used instead of $x \in C$ above, there would exist examples of sequences of random variables that would converge in probability but not in distribution. By requiring that the criterion for convergence holds only where $\mathbb{P}(X \leq x)$ is continuous, we avoid these cases and make convergence in probability a special case of the weaker criterion of convergence in distribution, as stated by the following theorem.
    
<div class='theorem'>

**Theorem (Conv. in probability $\implies$ conv. in distribution)** Let $X_1, X_2, ...$ be a sequence of variables and $X_n \to X$ in probability, then $X_n \implies X$.

</div>
<br>
    
Below are two proofs for this result. The first is a textbook proof from the book,{cite}`grimmettprob` based on inequalities.
    
<details class="proof">
<summary>Proof (a): Convergence in probability \(\implies\) convergence in distribution</summary>
 
Let $X_1, X_2, ...$ be a sequence of random variables which converges in probability to another random variable $X$. Let $x$ be any point where the distribution function of $X$ is continuous. Now consider
  
$$\begin{align}
\mathbb{P}(X_n \leq x) &= \mathbb{P}(X_n \leq x, X \leq x + \epsilon) + \mathbb{P}(X_n \leq x, X > x + \epsilon)\\
&\leq \mathbb{P}(X \leq x + \epsilon) + \mathbb{P}(X - X_n > \epsilon)\\
&\leq \mathbb{P}(X \leq x + \epsilon) + \mathbb{P}(|X - X_n| > \epsilon)
\end{align}$$
    
Similarly we can switch the roles of $X_n$ and $X$ to obtain
    
$$\begin{align}
\mathbb{P}(X \leq x - \epsilon) &= \mathbb{P}(X \leq x - \epsilon, X_n \leq x) + \mathbb{P}(X_n \leq x - \epsilon, X > x)\\
&\leq \mathbb{P}(X_n \leq x) + \mathbb{P}(X_n - X > \epsilon)\\
&\leq \mathbb{P}(X_n \leq x) + \mathbb{P}(|X_n - X| > \epsilon).
\end{align}$$
    
Combining these two inequalities we obtain
    
$$\begin{align}
\mathbb{P}(X \leq x - \epsilon) - \mathbb{P}(|X_n - X| > \epsilon) \leq \mathbb{P}(X_n \leq x) \leq \mathbb{P}(X \leq x + \epsilon) + \mathbb{P}(|X - X_n| > \epsilon),
\end{align}$$
    
and taking $\epsilon$ to $0$ we obtain

$$\begin{align}
\mathbb{P}(X \leq x) \leq \mathbb{P}(X_n \leq x) \leq \mathbb{P}(X \leq x) \iff \mathbb{P}(X_n \leq x) = \mathbb{P}(X \leq x),
\end{align}$$
    
where we have used the facts that $X_n \to X$ in probability and that $\mathbb{P}(X \leq x)$ is continuous at $x$.
    
</details>
<br>
    
The second is an alternative proof which includes a diagram, that is hopefully more intuitives.
    
<details class="proof">
<summary>Proof (b): Convergence in probability \(\implies\) convergence in distribution</summary>
    
The set $Z_n \leq z$ corresponds to the yellow, red, green and pink regions below, and the set $Z \leq z$ corresponds to the blue, orange, green and pink regions. Therefore the difference $\mathbb{P}(Z_n \leq z) - \mathbb{P}(Z \leq z)$ is equal to the sum of the probability measure on the blue and orange regions, minus that of the yellow and red regions. We wish to show this difference goes to $0$ as $n \to \infty$.
    
Since $|Z_n - Z| \geq \epsilon$ corresponds to $(\text{white + green + blue + yellow})$ and $\mathbb{P}(|Z_n - Z| \geq \epsilon) \to 0$ as $n \to \infty$, the yellow and blue areas have $0$ probability in the $n \to \infty$ limit. Assuming $\mathbb{P}(Z \leq z)$ is continuous in $z$ at $z = z_0$, then the red and orange areas must also have $0$ probability in the $n \to \infty$ limit, otherwise the continuity condition would be contradicted. Therefore
    
$$\lim_{n \to \infty} \big | \mathbb{P}(Z_n \leq z) - \mathbb{P}(Z \leq z) \big |  = 0,$$
    
and the variables converge in distribution.

```{figure} ./img/conv-in-prob-proof.svg
---
height: 500px
width: 500px
name: conv-in-prob-proof
---
Illustration for the argument that convergence in probability implies convergence in distribution. The presence of a darker border indicates that the corresponding region contains the border itself - the cyan region does not contain its border. See text for explanation.
```
    
</details>
<br>


    
    
<div class='theorem'>

**Theorem (Conv. in distribution to $c$ $\implies$ conv. in probability to $c$)** Let $X_1, X_2, ...$ be a sequence of variables and which coverges in distribution to a constant $c$. Then $X_n$ converges to $c$ in probability also. 

</div>
<br>

## Characteristic functions for the limit theorem and weak law


<div class='theorem'>

**Theorem (Continuity theorem with characteristic functions)** Let $X, X_1, X_2, ...$ be random variables with characteristic functions $\phi, \phi_1, \phi_2 ...$. Then $X_N \implies X$ as $N \to \infty$ if and only if
 
 $$\begin{align}
 \phi_N(t) \to \phi(t) \text{ as } N \to \infty, \text{ for } t \in \mathbb{R}.
 \end{align}$$

</div>
<br>
    


## References

```{bibliography} ./references.bib
```
    