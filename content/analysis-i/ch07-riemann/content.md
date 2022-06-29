# Riemann integral


(analysis-i-riemann-def)=
## Riemann integral definition

<div class="definition">

**Definition (Dissection)** Let $[a, b] \subset \mathbb{R}$ be a closed interval. A dissection $\mathcal{D} = (x_0, x_1, \dots, x_N)$ of $[a, b]$ is a finite sequence $a = x_0 < x_1 < \dots < x_N = b$.
    
</div>
<br>

    

<div class="definition">

**Definition (Upper and lower sums)** Given a function $f : \mathbb{R} \to \mathbb{R}$ and a dissection $\mathcal{D}$ of $[a, b]$, we define the lower and upper sums as
    
$$\begin{align}
L_{\mathcal{D}}(f) &= \sum_{n=1}^N (x_n - x_{n-1}) \inf_{x \in [x_{n-1}, x_n]} f(x), \\
U_{\mathcal{D}}(f) &= \sum_{n=1}^N (x_n - x_{n-1}) \sup_{x \in [x_{n-1}, x_n]} f(x).
\end{align}$$
    
</div>
<br>

    

<div class="definition">

**Definition (Refining dissections)** If $\mathcal{D}_1$ and $\mathcal{D}_2$ are both dissections of $[a, b]$, we say that $\mathcal{D}_2$ refines $\mathcal{D}_1$ if every point of $\mathcal{D}_1$ is contained in $\mathcal{D}_2$.
    
</div>
<br>

    
    
<div class="lemma">

**Lemma (Refining dissections and upper and lower sums)** Suppose $\mathcal{D}_1, \mathcal{D}_2$ are dissections of $[a, b]$ and $\mathcal{D}_2$ refines $\mathcal{D}_1$. Then for any function $f : \mathbb{R} \to \mathbb{R}$, we have

$$\begin{equation}
L_{\mathcal{D}_1}(f) \leq L_{\mathcal{D}_2}(f) ~~~\text{ and }~~~ U_{\mathcal{D}_1}(f) \geq U_{\mathcal{D}_2}(f).
\end{equation}$$
    
</div>
<br>


<details class="proof">
<summary>Proof: Refining dissections and upper and lower sums</summary>
    
Suppose $\mathcal{D}_1 = (x_0, x_1, \dots, x_N)$ is a dissection of $[a, b]$ and consider a function $f : \mathbb{R} \to \mathbb{R}$. Suppose $\mathcal{D}$ refines $\mathcal{D}_1$ and contains one additional point $z$ where $x_{n-1} < z < x_n$ for some $n \in \{1, 2, \dots, N\}$. Then, by the definition of the lower sum, we have
    
$$\begin{align}
L_{\mathcal{D}_1}(f) &= \left((x_1 - x_0) \inf_{x \in [x_0, x_1]} f(x) \right) + ~ \dots ~ + \left((x_N - x_{N-1}) \inf_{x \in [x_{N-1}, x_N]} f(x) \right) \\
                     ~\\
                     &= \left((x_1 - x_0) \inf_{x \in [x_0, x_1]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((z - x_{N-1}) \inf_{x \in [x_{N-1}, x_N]} f(x)\right) + \left((x_N - z) \inf_{x \in [x_{N-1}, x_N]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((x_N - x_{N-1}) \inf_{x \in [x_{N-1}, x_N]} f(x) \right) \\
                     ~\\
                     &\leq \left((x_1 - x_0) \inf_{x \in [x_0, x_1]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((z - x_{N-1}) \inf_{x \in [z, x_N]} f(x)\right) + \left((x_N - z) \inf_{x \in [z, x_N]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((x_N - x_{N-1}) \inf_{x \in [x_{N-1}, x_N]} f(x) \right) \\
                     ~\\
                     &= L_{\mathcal{D}}(f).
\end{align}$$
    
Therefore, by adding one point to the dissection $\mathcal{D}_1$, the resulting lower sum can only become larger. Proceeding recursively to add all of the points of $\mathcal{D}_2$ into $\mathcal{D}_1$, we arrive at
    
$$\begin{equation}
L_{\mathcal{D}_1}(f) \leq L_{\mathcal{D}_2}(f).
\end{equation}$$
    
Repeating this argument for the upper sum we have
    
$$\begin{align}
U_{\mathcal{D}_1}(f) &= \left((x_1 - x_0) \sup_{x \in [x_0, x_1]} f(x) \right) + ~ \dots ~ + \left((x_N - x_{N-1}) \sup_{x \in [x_{N-1}, x_N]} f(x) \right) \\
                    ~\\
                     &= \left((x_1 - x_0) \sup_{x \in [x_0, x_1]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((z - x_{N-1}) \sup_{x \in [x_{N-1}, x_N]} f(x)\right) + \left((x_N - z) \sup_{x \in [x_{N-1}, x_N]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((x_N - x_{N-1}) \sup_{x \in [x_{N-1}, x_N]} f(x) \right) \\
                     ~\\
                     &\geq \left((x_1 - x_0) \sup_{x \in [x_0, x_1]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((z - x_{N-1}) \sup_{x \in [z, x_N]} f(x)\right) + \left((x_N - z) \sup_{x \in [z, x_N]} f(x)\right) + ~ \dots ~ + \\
                     &~~~~~ + \left((x_N - x_{N-1}) \sup_{x \in [x_{N-1}, x_N]} f(x) \right) \\
                     ~\\
                     &= U_{\mathcal{D}}(f).
\end{align}$$
    
Therefore, by adding one point to the dissection $\mathcal{D}_1$, the resulting upper sum can only become smaller. Again, proceeding recursively, we arrive at
    
$$\begin{equation}
U_{\mathcal{D}_1}(f) \geq U_{\mathcal{D}_2}(f).
\end{equation}$$
    
</details>
<br>

    

<div class="definition">

**Definition (Least common refinement)** Suppose $\mathcal{D}_1$ and $\mathcal{D}_2$ are dissections of $[a, b]$. The least common refinement of $\mathcal{D}_1$ and $\mathcal{D}_2$ is the dissection containing all, and only those, points contained in $\mathcal{D}_1$ and $\mathcal{D}_2$.
    
</div>
<br>


<div class="lemma">

**Lemma (Upper sum larger than lower sum)** Suppose $\mathcal{D}_1$ and $\mathcal{D}_2$ are dissections of $[a, b]$. Then

$$\begin{equation}
L_{\mathcal{D}_1}(f) \leq U_{\mathcal{D}_2}(f).
\end{equation}$$
    
</div>
<br>


<details class="proof">
<summary>Proof: Upper sum larger than lower sum</summary>
    
Suppose $\mathcal{D}_1$ and $\mathcal{D}_2$ are dissections of $[a, b]$, and let $\mathcal{D}$ be the smallest common refinement of $\mathcal{D}_1$ and $\mathcal{D}_2$. Then

$$\begin{equation}
L_{\mathcal{D}_1}(f) \leq L_{\mathcal{D}}(f) \leq U_{\mathcal{D}}(f) \leq U_{\mathcal{D}_2}(f).
\end{equation}$$
    
</details>
<br>

    

<div class="definition">

**Definition (Upper and lower integrals, Riemann integral)** Suppose $f : \mathbb{R} \to \mathbb{R}$ and $[a, b] \subset \mathbb{R}$. We define the lower and upper integrals of $f$ over $[a, b]$ as

$$\begin{align}
\underline{\int_a^b} f(x) dx = \sup_{\mathcal{D}} ~ L_{\mathcal{D}}(f) ~~~~\text{ and }~~~~ \overline{\int_a^b} f(x) dx = \inf_{\mathcal{D}} ~ U_{\mathcal{D}}(f).
\end{align}$$
    
If the lower and upper integrals are equal, we call their value the Riemann integral of $f$ over $[a, b]$, and write this as $\int_a^b f(x)dx$. Whenever the Riemann integral of a function exists on an inteval, we say the function is Riemann-integrable in this interval.
    
</div>
<br>


(analysis-i-integrability)=
## Riemann integrability


We will consider two examples, one of a function which is Riemann integrable, and another of a function which is not Riemann integrable. First, we will define the mesh of a dissection, which we will use in these examples and also later.


<div class="definition">

**Definition (Mesh)** Let $\mathcal{D} = (x_0, x_1, \dots, x_N)$ be a dissection of $[a, b]$. The mesh of $\mathcal{D}$ is defined as $\max_n (x_{n+1} - x_n)$.
    
</div>
<br>


<details class="example">
<summary>Example: A function that is Riemann integrable</summary>

Now, as an example, consider the function $f(x) = x : \mathbb{R} \to \mathbb{R}$. Let's compute its Riemann integral over $[a, b]$. Since $f(x)$ is increasing in $x$, taking the infimum or the supremum over an interval is easy. For any dissection $\mathcal{D} = (x_0, x_1, \dots, x_N)$, we have

$$\begin{align}
L_{\mathcal{D}} &= \sum_{n=1}^N (x_n - x_{n-1}) \inf_{x \in [x_{n-1}, x_n]} x \\
               &= \sum_{n=1}^N (x_n - x_{n-1}) x_{n-1} \\
               &= \sum_{n=1}^N \left(x_n x_{n-1} - x_{n-1}^2 \right) \\
               &= \sum_{n=1}^N \left(\frac{x_n^2}{2} - \frac{x_{n-1}^2}{2} + x_n x_{n-1} - \frac{x_n^2}{2} - x_{n-1}^2 \right) \\
               &= \frac{1}{2}\sum_{n=1}^N \left(x_n^2 - x_{n-1}^2\right) + \frac{1}{2}\sum_{n=1}^N \left(x_n - x_{n-1}\right)^2 \\
               &= \frac{1}{2} \left(b^2 - a^2\right) - \frac{1}{2}\sum_{n=1}^N \left(x_n - x_{n-1}\right)^2
\end{align}$$

Now, if we pick the $\mathcal{D} = \mathcal{D}_N = (x_0, x_1, \dots, x_N)$ to be the uniform dissection where $x_n - x_{n-1} = N^{-1}$, we have 

$$\begin{equation}
L_{\mathcal{D}_N} = \frac{1}{2} \left(b^2 - a^2\right) - \frac{1}{2N} \to \frac{1}{2} \left(b^2 - a^2\right) ~~~\text{ as }~~~ N \to \infty.
\end{equation}$$

Similarly for the upper sum, we have

$$\begin{equation}
U_{\mathcal{D}_N} = \frac{1}{2} \left(b^2 - a^2\right) + \frac{1}{2N} \to \frac{1}{2} \left(b^2 - a^2\right) ~~~\text{ as }~~~ N \to \infty.
\end{equation}$$

Therefore $L_{\mathcal{D}_N}$ and $U_{\mathcal{D}_N}$ tend to the same value and $f(x) = x$ is Riemann integrable.
    
</details>
<br>
    
<details class="example">
<summary>Example: A function that is <b>not</b> Riemann integrable</summary>

Now, consider the function $f(x) : \mathbb{R} \to \mathbb{R}$ defined as
    
$$\begin{equation}
f(x) = \begin{cases} 1 &\text{ if } x \in \mathbb{Q} \\ 0 &\text{ otherwise.} \end{cases}
\end{equation}$$
    
and consider its Riemann integral over the interval $[0, 1]$. Given a dissection $\mathcal{D} = (x_0, x_1, \dots, x_N)$, any closed subinterval $[x_{n-1}, x_n]$ will contain a rational point, that is in $\mathbb{Q}$, and also an irrational point, that is not in $\mathbb{Q}$. Therefore
    
$$\begin{equation}
\inf_{x \in [x_{n-1}, x_n]} f(x) = 0 ~~~\text{ and }~~~ \sup_{x \in [x_{n-1}, x_n]} f(x) = 1,
\end{equation}$$
    
from which it follows that for any mesh $\mathcal{D}$
    
$$\begin{equation}
L_{\mathcal{D}}(f) = 0 \implies \sup_{\mathcal{D}} L_{\mathcal{D}}(f) = 0 ~~~\text{ and }~~~ U_{\mathcal{D}}(f) = 1 \implies \inf_{\mathcal{D}} U_{\mathcal{D}}(f) = 1.
\end{equation}$$
    
Therefore $f$ is not Riemann integrable.
    
</details>
<br>
    
    
<div class="lemma">

**Lemma (Riemann integrability condition)** Let $f(x) = x : \mathbb{R} \to \mathbb{R}$ be a function and $[a, b] \subset \mathbb{R}$ be a closed interval. Then $f$ is Riemann integrable over $[a, b]$ if and only if for any $\epsilon > 0$ there exists a dissection $\mathcal{D}$ such that
    
$$\begin{equation}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) < \epsilon.
\end{equation}$$
    
</div>
<br>

<details class="proof">
<summary>Proof: Riemann integrability condition</summary>

Let $f(x) = x : \mathbb{R} \to \mathbb{R}$ be a function and $[a, b] \subset \mathbb{R}$ be a closed interval.

Suppose that for any $\epsilon > 0$ there exists a dissection $\mathcal{D}$ such that
    
$$\begin{equation}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) < \epsilon.
\end{equation}$$
    
Then we also have
    
$$\begin{equation}
\inf_{\mathcal{D}} U_{\mathcal{D}}(f) - \sup_{\mathcal{D}} L_{\mathcal{D}}(f) < \epsilon.
\end{equation}$$
    
which, by the defition of the upper and lower Riemann integrals we can write as
    
$$\begin{equation}
\underline{\int_a^b} f(x) dx - \overline{\int_a^b} f(x) dx < \epsilon.
\end{equation}$$
    
Since $\epsilon > 0$ can be picked to be arbitrarily small, we have 

$$\begin{equation}
\underline{\int_a^b} f(x) dx = \overline{\int_a^b} f(x) dx,
\end{equation}$$
    
so $f$ is Riemann integrable.

Conversely, suppose $f$ is Riemann integrable in $[a, b]$, with integral $\int_a^b f(x) dx$, and let $\epsilon > 0$. Since $f$ is Riemann integrable, there must exist a dissection $\mathcal{D}_{\epsilon, U}$ such that 
    
$$\begin{equation}
U_{\mathcal{D}_{\epsilon, U}}(f) < \int_a^b f(x) dx + \frac{\epsilon}{2}.
\end{equation}$$
    
Similarly, there must also exist a dissection $\mathcal{D}_{\epsilon, L}$ such that 
    
$$\begin{equation}
L_{\mathcal{D}_{\epsilon, L}}(f) > \int_a^b f(x) dx - \frac{\epsilon}{2}.
\end{equation}$$
    
Now letting $\mathcal{D}$ be the least common refinement of $\mathcal{D}_{\epsilon, L}$ and $\mathcal{D}_{\epsilon, U}$, we have
    
$$\begin{equation}
U_{\mathcal{D}}(f) \leq U_{\mathcal{D}_{\epsilon, U}}(f) < \int_a^b f(x) dx + \frac{\epsilon}{2},
\end{equation}$$
    
and similarly we have
    
$$\begin{equation}
L_{\mathcal{D}}(f) \geq L_{\mathcal{D}_{\epsilon, L}}(f) > \int_a^b f(x) dx - \frac{\epsilon}{2}.
\end{equation}$$
    
putting these together we arrive at
    
$$\begin{equation}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) < \epsilon,
\end{equation}$$
    
which is the required result.
    
</details>
<br>





## Riemann integral linearity

Here we will show some of the properties of the Riemann integral, starting with linearity. We will build the proof of linearity step by step.

<div class="lemma">

**Lemma (Riemann integral is homogeneous)** Let $f : \mathbb{R} \to \mathbb{R}$ be a function that is Riemann integrable in the interval $[a, b] \subset \mathbb{R}$. Then for any $\lambda \geq 0$, the function $\lambda f$ is integrable and also
    
$$\begin{equation}
\int_a^b \lambda f(x) dx = \lambda \int_a^b f(x) dx.
\end{equation}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Riemann integral is homogeneous</summary>
    
Let $f : \mathbb{R} \to \mathbb{R}$ be a function that is Riemann integrable in the interval $[a, b] \subset \mathbb{R}$ and $\lambda \geq 0$. Then, we have that 
    
$$\begin{align}
\inf_{x \in [x_{n-1}, x_n]} \lambda f(x) =  \lambda \inf_{x \in [x_{n-1}, x_n]} f(x)
\end{align}$$
    
which implies that for any dissection $\mathcal{D}$ we have

$$\begin{align}
L_{\mathcal{D}}(\lambda f) = \lambda L_{\mathcal{D}}(f),
\end{align}$$
    
and similarly for the upper sum. Therefore, also 

$$\begin{align}
\sup_{\mathcal{D}} L_{\mathcal{D}}(\lambda f) &= \lambda \sup_{\mathcal{D}} L_{\mathcal{D}}(f) = \lambda \int_a^b f(x) dx.
\end{align}$$
    
Also, the analogous result for the upper sum holds, specifically

$$\begin{align}
\inf_{\mathcal{D}} U_{\mathcal{D}}(\lambda f) &= \lambda \inf_{\mathcal{D}} U_{\mathcal{D}}(f) = \lambda \int_a^b f(x) dx.
\end{align}$$
    
Therefore $\lambda f$ is integrable and also

$$\begin{equation}
\int_a^b \lambda f(x) dx = \lambda \int_a^b f(x) dx,
\end{equation}$$
    
as required.

</details>
<br>




<div class="lemma">

**Lemma (Integral of negative function is negative of integral of function)** Let $f : \mathbb{R} \to \mathbb{R}$ be a function that is Riemann integrable in the interval $[a, b] \subset \mathbb{R}$. Then $-f$ is integrable and 
    
$$\begin{equation}
\int_a^b - f(x) dx = - \int_a^b f(x) dx.
\end{equation}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Integral of negative function is negative of integral of function</summary>
    
Let $f : \mathbb{R} \to \mathbb{R}$ be a function that is Riemann integrable in the interval $[a, b] \subset \mathbb{R}$ and $\lambda \geq 0$. Then, we have that 
    
$$\begin{align}
\inf_{x \in [x_{n-1}, x_n]} - f(x) =  - \sup_{x \in [x_{n-1}, x_n]} f(x)
\end{align}$$
    
which implies that for any dissection $\mathcal{D}$ we have

$$\begin{align}
L_{\mathcal{D}}(- f) = - U_{\mathcal{D}}(f),
\end{align}$$
    
and similarly for the upper sum

$$\begin{align}
U_{\mathcal{D}}(- f) = - L_{\mathcal{D}}(f).
\end{align}$$
    
From this it follows that

$$\begin{align}
\sup_{\mathcal{D}} L_{\mathcal{D}}(- f) &= - \inf_{\mathcal{D}} U_{\mathcal{D}}(f) = - \int_a^b f(x) dx,
\end{align}$$
    
and also, analogously for the upper integral, we have

$$\begin{align}
\inf_{\mathcal{D}} U_{\mathcal{D}}(- f) &= - \sup_{\mathcal{D}} L_{\mathcal{D}}(f) = - \int_a^b f(x) dx.
\end{align}$$
    
Therefore $- f$ is integrable and also

$$\begin{equation}
\int_a^b - f(x) dx = - \int_a^b f(x) dx,
\end{equation}$$
    
as required.

</details>
<br>


<div class="lemma">

**Lemma (Sum of integrable functions is integrable)** Let $f, g : \mathbb{R} \to \mathbb{R}$ be functions which are Riemann integrable in an interval $[a, b] \subset \mathbb{R}$. Then $f + g$ is also Riemann integrable in $[a, b]$ and
    
$$\begin{equation}
\int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx.
\end{equation}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Sum of integrable functions is integrable</summary>
    
Let $f, g : \mathbb{R} \to \mathbb{R}$ be functions which are Riemann integrable in an interval $[a, b] \subset \mathbb{R}$, and also let $\epsilon > 0$. Since $f$ and $g$ are Riemann integrable, there exist corresponding dissections $\mathcal{D}_f$ and $\mathcal{D}_g$ such that
    
$$\begin{equation}
U_{\mathcal{D}_f}(f) - L_{\mathcal{D}_f}(f) < \frac{\epsilon}{2} ~~~\text{ and }~~~ U_{\mathcal{D}_g}(g) - L_{\mathcal{D}_g}(g) < \frac{\epsilon}{2}.
\end{equation}$$
    
Let $\mathcal{D}$ be the least common dissection of $\mathcal{D}_f$ and $\mathcal{D}_g$. Then since {ref}`refining a dissection<analysis-i-riemann-def>` can only reduce the difference betwen the upper and lower sums, we have
    
$$\begin{equation}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) < \frac{\epsilon}{2} ~~~\text{ and }~~~ U_{\mathcal{D}}(g) - L_{\mathcal{D}}(g) < \frac{\epsilon}{2}.
\end{equation}$$
    
We also have the fact that the upper sum satisfies
    
$$\begin{align}
\sup_{x \in [x_{n-1}, x_n]} (f(x) + g(x)) &\leq \sup_{x \in [x_{n-1}, x_n]} f(x) + \sup_{x \in [x_{n-1}, x_n]} g(x) \implies U_{\mathcal{D}}(f + g) \leq U_{\mathcal{D}}(f) + U_{\mathcal{D}}(g),
\end{align}$$
    
and similalry for the lower sum
    
$$\begin{align}
\inf_{x \in [x_{n-1}, x_n]} (f(x) + g(x)) &\geq \inf_{x \in [x_{n-1}, x_n]} f(x) + \inf_{x \in [x_{n-1}, x_n]} g(x) \implies L_{\mathcal{D}}(f + g) \geq L_{\mathcal{D}}(f) + L_{\mathcal{D}}(g).
\end{align}$$

From this we can write
    
$$\begin{equation}
U_{\mathcal{D}}(f + g) - L_{\mathcal{D}}(f + g) \leq U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) + U_{\mathcal{D}}(g) - L_{\mathcal{D}}(g) < \epsilon,
\end{equation}$$
    
which by the {ref}`Riemann integrability condition<analysis-i-integrability>` implies that $f + g$ is integrable and also
    
$$\begin{equation}
\int_a^b f(x) + g(x) dx = \int_a^b f(x) dx + \int_a^b g(x) dx.
\end{equation}$$

</details>
<br>
    
    


<div class="lemma">

**Lemma (Linearity of the Riemann integral)** Let $f, g : \mathbb{R} \to \mathbb{R}$ be functions which are Riemann integrable in an interval $[a, b] \subset \mathbb{R}$, and let $\lambda, \mu \in \mathbb{R}$. Then $\lambda f + \mu g$ is also Riemann integrable in $[a, b]$ and
    
$$\begin{equation}
\int_a^b (\lambda f(x) + \mu g(x)) dx = \lambda \int_a^b f(x)dx + \mu \int_a^b g(x)dx.
\end{equation}$$
    
</div>
<br>
    

<details class="proof">
<summary>Proof: Linearity of the Riemann integral</summary>
    
Let $f, g : \mathbb{R} \to \mathbb{R}$ be functions which are Riemann integrable in an interval $[a, b] \subset \mathbb{R}$, and let $\lambda, \mu \in \mathbb{R}$. Then by the previous lemmas, we have
    
$$\begin{align}
\int_a^b (\lambda f(x) + \mu g(x)) dx &= \int_a^b \lambda f(x) dx + \int_a^b \mu g(x) dx \\
                                      &= \lambda \int_a^b f(x) dx + \mu \int_a^b g(x) dx,
\end{align}$$
    
as required.

</details>
<br>

    
## Further properties
    
    
<div class="lemma">

**Lemma (Larger function implies larger integral)** Let $f, g : \mathbb{R} \to \mathbb{R}$ be functions which are Riemann integrable in an interval $[a, b] \subset \mathbb{R}$. Then if $f(x) \leq g(x)$ for all $x \in [a, b]$ we have
    
$$\begin{equation}
\int_a^b f(x) dx \leq \int_a^b g(x) dx.
\end{equation}$$
    
</div>
<br>

    
<details class="proof">
<summary>Proof: Larger function implies larger integral</summary>
    
Let $f, g : \mathbb{R} \to \mathbb{R}$ be functions which are Riemann integrable in an interval $[a, b] \subset \mathbb{R}$ and suppose that $f(x) \leq g(x)$ for all $x \in [a, b]$. Then, from the previous lemmas we have
    
$$\begin{equation}
\int_a^b f(x) dx - \int_a^b g(x) dx = \int_a^b f(x) dx + \int_a^b - g(x) dx = \int_a^b (f(x) - g(x)) dx.
\end{equation}$$
    
Since $f(x) - g(x) \leq 0$, we have $U_{\mathcal{D}}(f - g) \leq 0$, and also
    
$$\begin{equation}
\int_a^b (f(x) - g(x)) dx \leq U_{\mathcal{D}}(f - g) \leq 0,
\end{equation}$$
    
which implies that
    
$$\begin{equation}
\int_a^b f(x) dx \leq \int_a^b g(x) dx.
\end{equation}$$

</details>
<br>


    
<div class="lemma">

**Lemma (Absolute value of integrable function is integrable)** Let $f : \mathbb{R} \to \mathbb{R}$ be a function that is Riemann integrable in the interval $[a, b] \subset \mathbb{R}$. Then $|f|$ is integrable in $[a, b]$.
    
</div>
<br>



<details class="proof">
<summary>Proof: Absolute value of integrable function is integrable</summary>
    
Let $f : \mathbb{R} \to \mathbb{R}$ be a function that is Riemann integrable in the interval $[a, b] \subset \mathbb{R}$. Then, we have
    
$$\begin{equation}
\sup_{u \in [x_{n-1}, x_n]} f(u) - \inf_{v \in [x_{n-1}, x_n]} f(v) = \sup_{u, v \in [x_{n-1}, x_n]}|f(u) - f(v)|.
\end{equation}$$
    
Similarly, we have
    
$$\begin{equation}
\sup_{u \in [x_{n-1}, x_n]} |f(u)| - \inf_{v \in [x_{n-1}, x_n]} |f(v)| = \sup_{u, v \in [x_{n-1}, x_n]}||f(u)| - |f(v)||.
\end{equation}$$
    
By the triangle inequality, we have
    
$$\begin{equation}
||f(u)| - |f(v)|| \leq |f(u) - f(v)|,
\end{equation}$$
    
and combining this with the equations above we arrive at
    
$$\begin{equation}
\sup_{u, v \in [x_{n-1}, x_n]}||f(u)| - |f(v)|| \leq \sup_{u, v \in [x_{n-1}, x_n]} |f(u) - f(v)|.
\end{equation}$$
    
Therefore we have
    
$$\begin{equation}
\sup_{u \in [x_{n-1}, x_n]} |f(u)| - \inf_{v \in [x_{n-1}, x_n]} |f(v)| \leq \sup_{u \in [x_{n-1}, x_n]} f(u) - \inf_{v \in [x_{n-1}, x_n]} f(v),
\end{equation}$$
    
which implies that for any dissection $\mathcal{D}$ we have
    
$$\begin{equation}
U_{\mathcal{D}}(|f|) - L_{\mathcal{D}}(|f|) \leq U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f),
\end{equation}$$
    
and the result follows by {ref}`Riemann's integrability condition<analysis-i-integrability>`.


</details>
<br>











<div class="definition">

**Definition ()** 
    
</div>
<br>


<div class="lemma">

**Lemma ()** 
    
</div>
<br>



<details class="proof">
<summary>Proof: </summary>

</details>
<br>
