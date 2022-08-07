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





## Linearity

Here we will show some of the properties of the Riemann integral, starting with linearity. We will build the proof of linearity step by step.

<div class="lemma">

**Lemma (Riemann integral is homogeneous)** Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function. Then for any $\lambda \geq 0$, the function $\lambda f$ is integrable and also
    
$$\begin{equation}
\int_a^b \lambda f(x) dx = \lambda \int_a^b f(x) dx.
\end{equation}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Riemann integral is homogeneous</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function and $\lambda \geq 0$. Then, we have that 
    
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

**Lemma (Integral of negative function is negative of integral of function)** Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function. Then $-f$ is Riemann integrable and 
    
$$\begin{equation}
\int_a^b - f(x) dx = - \int_a^b f(x) dx.
\end{equation}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Integral of negative function is negative of integral of function</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function and $\lambda \geq 0$. Then, we have that 
    
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

**Lemma (Absolute value of integrable function is integrable)** Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function. Then $|f|$ is integrable in $[a, b]$.
    
</div>
<br>



<details class="proof">
<summary>Proof: Absolute value of integrable function is integrable</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function. Then, we have
    
$$\begin{equation}
\Big(\sup_{u \in [x_{n-1}, x_n]} f(u) \Big) - \Big(\inf_{v \in [x_{n-1}, x_n]} f(v)\Big) = \sup_{u, v \in [x_{n-1}, x_n]}|f(u) - f(v)|.
\end{equation}$$
    
Similarly, we have
    
$$\begin{equation}
\Big(\sup_{u \in [x_{n-1}, x_n]} |f(u)|\Big) - \Big(\inf_{v \in [x_{n-1}, x_n]} |f(v)|\Big) = \sup_{u, v \in [x_{n-1}, x_n]}||f(u)| - |f(v)||.
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
\Big(\sup_{u \in [x_{n-1}, x_n]} |f(u)|\Big) - \Big(\inf_{v \in [x_{n-1}, x_n]} |f(v)|\Big) \leq \Big(\sup_{u \in [x_{n-1}, x_n]} f(u)\Big) - \Big(\inf_{v \in [x_{n-1}, x_n]} f(v)\Big),
\end{equation}$$
    
which implies that for any dissection $\mathcal{D}$ we have
    
$$\begin{equation}
U_{\mathcal{D}}(|f|) - L_{\mathcal{D}}(|f|) \leq U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f),
\end{equation}$$
    
and the result follows by {ref}`Riemann's integrability condition<analysis-i-integrability>`.


</details>
<br>


    
    
<div class="lemma">

**Lemma (Additivity property of the Riemann integral)** Let $f : [a, c] \to \mathbb{R}$ be a Riemann integrable function and let $b \in [a, c]$. Then the restrictions of $f$ to $[a, b]$ and to $[b, c]$ are Riemann integrable and also 
    
$$\begin{equation}
\int_a^c f(x)dx = \int_a^b f(x)dx + \int_b^c f(x)dx.
\end{equation}$$
    
Conversely, if $f : [a, c] \to \mathbb{R}$ is Riemann integrable on $[a, b]$ and on $[b, c]$ it is also Riemann integrable on $[a, c]$ and the above equation still holds.
    
</div>
<br>



<details class="proof">
<summary>Proof: Additivity property of the Riemann integral</summary>
    
Let $f : [a, c] \to \mathbb{R}$ be a Riemann integrable function and let $b \in [a, c]$. Let also $\epsilon > 0$. Since $f$ is Riemann integrable in $[a, c]$, there exists a dissection $\mathcal{D}_{a, c} = (x_0, x_1, \dots, x_N)$ of $[a, c]$ such that
    
$$\begin{equation}
U_{\mathcal{D}_{a, c}}(f) - L_{\mathcal{D}_{a, c}}(f) < \epsilon.
\end{equation}$$
    
Further, if we add the point $x = b$ to the dissection $\mathcal{D}_{a, c}$ the difference between the upper and lower sums can only get smaller, so the above inequality would still hold. Therefore, without loss of generality, we will assume that $\mathcal{D}_{a, c}$ contains $b$. Now, consider the dissections $\mathcal{D}_{a, b} = (x_0, x_1, \dots, x_K)$ and $\mathcal{D}_{b, c} = (x_K, x_{k+1}, \dots, x_N)$, where $x_K = b$. Then
    
$$\begin{align}
L_{\mathcal{D}_{a, c}}(f) &= L_{\mathcal{D}_{a, b}}(f) + L_{\mathcal{D}_{b, c}}(f), \\
U_{\mathcal{D}_{a, c}}(f) &= U_{\mathcal{D}_{a, b}}(f) + U_{\mathcal{D}_{b, c}}(f),
\end{align}$$
    
from which we obtain
    
$$\begin{equation}
\left(U_{\mathcal{D}_{a, b}}(f) - L_{\mathcal{D}_{a, b}}(f)\right) + \left(U_{\mathcal{D}_{b, c}}(f) - L_{\mathcal{D}_{b, c}}(f)\right) < \epsilon.
\end{equation}$$
    
Because both terms in the parentheses above are non-negative, they must both be smaller than $\epsilon$, so we obtain
    
$$\begin{align}
U_{\mathcal{D}_{a, b}}(f) - L_{\mathcal{D}_{a, b}}(f) &< \epsilon, \\
U_{\mathcal{D}_{b, c}}(f) - L_{\mathcal{D}_{b, c}}(f) &< \epsilon,
\end{align}$$
    
which, by the {ref}`Riemann integrability condition<analysis-i-integrability>`, imply that the restrictions of $f$ to $[a, b]$ and to $[b, c]$ are both integrable and also
    
$$\begin{equation}
\int_a^c f(x)dx = \int_a^b f(x)dx + \int_b^c f(x)dx.
\end{equation}$$
    
Conversely, suppose $f : [a, c] \to \mathbb{R}$ is Riemann integrable on $[a, b]$ and on $[b, c]$. Since it is Riemann integrable in these two intervals, there exist dissections $\mathcal{D}_{a, b}$ and $\mathcal{D}_{b, c}$ of these two intervals such that
    
$$\begin{align}
U_{\mathcal{D}_{a, b}}(f) - L_{\mathcal{D}_{a, b}}(f) &< \epsilon, \\
U_{\mathcal{D}_{b, c}}(f) - L_{\mathcal{D}_{b, c}}(f) &< \epsilon.
\end{align}$$
    
Consider the dissection $\mathcal{D}_{a, c}$ of the interval $[a, c]$, consisting of the points of $\mathcal{D}_{a, b}$ and the points of $\mathcal{D}_{b, c}$. Then, same as before, we have
    
$$\begin{align}
L_{\mathcal{D}_{a, c}}(f) &= L_{\mathcal{D}_{a, b}}(f) + L_{\mathcal{D}_{b, c}}(f), \\
U_{\mathcal{D}_{a, c}}(f) &= U_{\mathcal{D}_{a, b}}(f) + U_{\mathcal{D}_{b, c}}(f),
\end{align}$$
    
which implies
    
$$\begin{equation}
U_{\mathcal{D}_{a, c}}(f) - L_{\mathcal{D}_{a, c}}(f) = \left(U_{\mathcal{D}_{a, b}}(f) - L_{\mathcal{D}_{a, b}}(f)\right) + \left(U_{\mathcal{D}_{b, c}}(f) - L_{\mathcal{D}_{b, c}}(f)\right) < 2\epsilon.
\end{equation}$$
    
By the {ref}`Riemann integrability condition<analysis-i-integrability>`, $f$ is Riemann integrable on $[a, c]$ and also
    
$$\begin{equation}
\int_a^c f(x)dx = \int_a^b f(x)dx + \int_b^c f(x)dx.
\end{equation}$$
    
</details>
<br>




<div class="lemma">

**Lemma (Product of Riemann integrable functions is Riemann integrable)** Let $f, g : [a, b] \to \mathbb{R}$ be Riemann integrable functions. Then $fg$ is also Riemann integrable in $[a, b]$.
    
</div>
<br>



<details class="proof">
<summary>Proof: Product of Riemann integrable functions is Riemann integrable</summary>

Let $f, g : [a, b] \to \mathbb{R}$ be Riemann integrable functions. Let $\mathcal{D} = (x_0, x_1, \dots, x_N)$ be a dissection of $[a, b]$ and let
    
$$\begin{align}
m_i = \inf_{x \in [x_{i-1}, x_i]} f(x) ~~~\text{ and }~~~ M_i = \sup_{x \in [x_{i-1}, x_i]} f(x),
\end{align}$$
    
and similarly

$$\begin{align}
l_i = \inf_{x \in [x_{i-1}, x_i]} g(x) ~~~\text{ and }~~~ L_i = \sup_{x \in [x_{i-1}, x_i]} g(x).
\end{align}$$
    
Now, if a function is Riemann integrable it is bounded, so there exists a constant $C$ such that $|f(x)|, |g(x)| < C$ for all $x \in [a, b]$. Let $u_n, v_n \in [x_{n-1}, x_n]$ for $n = 1, \dots, N$. Then we have
    
$$\begin{align}
\sum_{n=1}^N &(x_n - x_{n-1})\left(f(u_n)g(u_n) - f(v_n)g(v_n)\right) = \\
                                                                     &= \sum_{n=1}^N (x_n - x_{n-1})\left(f(u_n)(g(u_n) - g(v_n)) + g(v_n)(f(u_n) - f(v_n))\right) \\
                                                                     &= \sum_{n=1}^N (x_n - x_{n-1})\left(f(u_n)(g(u_n) - g(v_n)) + g(v_n)(f(u_n) - f(v_n))\right) \\
                                                                     &\leq C \sum_{n=1}^N (x_n - x_{n-1}) \left((M_i - m_i) + (L_i - l_i)\right) \\
                                                                     &= C (U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) + U_{\mathcal{D}}(g) - L_{\mathcal{D}}(g)).
\end{align}$$
    
Since the above inequality holds for any $u_n, v_n \in [x_{n-1}, x_n]$, it also holds when $u_n$ and $v_n$ are such that $f(u_n)g(u_n)$ and $f(v_n)g(v_n)$ are at their supremum and infimum respectively, so
    
    
$$\begin{equation}
U_{\mathcal{D}}(fg) - L_{\mathcal{D}}(fg) = C (U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) + U_{\mathcal{D}}(g) - L_{\mathcal{D}}(g)).
\end{equation}$$
    
Since $C$ is a constant and $f$ and $g$ are Riemann integrable, the right hand side term can be made arbitarily small by picking an appropriate $\mathcal{D}$. Therefore by the {ref}`Riemann integrability condition<analysis-i-integrability>`, $fg$ is Riemann integrable in $[a, b]$.

    
</details>
<br>

    
 



<div class="theorem">

**Theorem (Continuous function on closed intervals are Riemann integrable)** Let $f : [a, b] \to \mathbb{R}$ be a continuous function. Then $f$ is Riemann integrable.
    
</div>
<br>



<details class="proof">
<summary>Proof: Continuous function on closed intervals are Riemann integrable</summary>

Let $f : [a, b] \to \mathbb{R}$ be a continuous function. Suppose that $f$ is not Riemann integrable. In this case, there exists $\epsilon > 0$ such that for any $\mathcal{D}$ we have
    
$$\begin{equation}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) > \epsilon.
\end{equation}$$
    
Let $\mathcal{D}_N$ be the uniform dissection with $N$ intervals
    
$$\begin{equation}
\mathcal{D}_N = \left(0, ~\frac{1}{N}, ~\dots, ~\frac{N-1}{N}, ~1 \right).
\end{equation}$$
    
Then, by the above condition 
    
$$\begin{equation}
U_{\mathcal{D}_N}(f) - L_{\mathcal{D}_N}(f) > \epsilon ~\text{ for all } N.
\end{equation}$$
    
For any given $\mathcal{D}_N$, for some $1 \leq n \leq N$ it must hold that
   
$$\begin{equation}
\left(\sup_{x \in [x_{n-1}, x_n]} f(x)\right) - \left(\inf_{x \in [x_{n-1}, x_n]} f(x)\right) > \epsilon.
\end{equation}$$
    
For this $n$, let $u_N, v_N \in [x_{n-1}, x_n]$ be the points where $f$ attains its supremum and infimum in the interval, respectively. Note that we have $|u_N - v_N| < \frac{1}{N}$ and also that $f(u_N) - f(v_N) > \epsilon$. By the {ref}`Bolzano-Weierstrass theorem<analysis-i-bolz-weier>`, the sequence $u_1, u_2, \dots$ has a convergent subsequence, which converges to a limit $u$ and since $f$ is continuous
    
$$\begin{equation}
u_N \to u \implies f(u_N) \to f(u).
\end{equation}$$
    
Also, since $|u_N - v_N| < \frac{1}{N}$, the corresponding subsequence of $v_n$ must also converge to $u$ which implies
    
$$\begin{equation}
v_N \to u \implies f(v_N) \to f(u).
\end{equation}$$
    
However, this is a contradition because $f(u_N) - f(v_N) > \epsilon$ must hold for all $N$. Therefore, there does not exist such $\epsilon > 0$ which means that $f$ is Riemann integrable.
    
</details>
<br>
    
  
Under the hood, this result uses the fact that a function which is continuous in a bounded closed interval has a property called uniform continuity which is a stronger form of continuity. Then, any function that is uniformly continuous on a bounded interval is Riemann integrable. We'll have a closer look at this below, starting by defining uniform continuity.
    

<div class="definition">

**Definition (Uniform continuity)** Let $A \subseteq \mathbb{R}$ and let $f : A \to \mathbb{R}$. Then $f$ is uniformly continuous if for any $\delta > 0$, there exists $\epsilon > 0$ such that for all $x, x' \in A$
    
$$\begin{equation}
|x - x'| < \epsilon \implies |f(x) - f(x')| < \delta.
\end{equation}$$
    
</div>
<br>
    
    
Uniform continuity is a stronger property than regular continuity because it requires that our $\epsilon$ works for all $x, x'$ in the domain. Now, if a function is continuous on a bounded closed inteval, it is uniformly continuous on this interval, as stated and proved below.
    
    
<div class="lemma">

**Lemma (Continous functions on closed bounded intervals are unifomly continuous)** Let $f : [a, b] \to \mathbb{R}$ be a continous function. Then $f$ is also uniformly continuous. 
    
</div>
<br>


<details class="proof">
<summary>Proof: Continous functions on closed bounded intervals are unifomly continuous</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a continous function. Suppose $f$ is not unifomly continuous. Then, there exists $\delta > 0$ such that for all $\epsilon > 0$ there exist $x, x' \in [a, b]$ such that $|x - x'| < \epsilon$ and also $|f(x) - f(x')| \geq \delta$. This implies that for all $n \in \mathbb{Z}^{++}$, we can find $x_n, x_n' \in [a, b]$ such that 
  
$$\begin{equation}
|x_n - x_n'| < \frac{1}{n} \implies |f(x_n) - f(x_n')| \geq \delta.
\end{equation}$$
    
Since $x_n \in [a, b]$, by the {ref}`Bolzano-Weierstrass theorem<analysis-i-bolz-weier>` we can find a subsequence of $x_n$, say $x_{k_n}$ which converges to some limit $x$. Also because $|x_n - x_n'| < \frac{1}{n}$ the sequence $x_{k_n}'$ also converges to $x$. Then because $f$ is continuous, we have
    
$$\begin{align}
x_{k_n} \to x &\implies f(x_{k_n}) \to f(x), \\
x_{k_n}' \to x &\implies f(x_{k_n}') \to f(x),
\end{align}$$

which implies that $|f(x_{k_n}) - f(x_{k_n}')| \to 0$, contradicting our assumption that $|f(x_n) - f(x_n')| \geq \delta$. Therefore $f$ must be uniformly continuous.

</details>
<br>
    

Using this lemma, we can easily show that a continuous function on a bounded closed interval is Riemann integrable, by showing that a uniformly continuous function is Riemann integrable.
    


<div class="lemma">

**Lemma (Uniformly continuous function is Riemann integrable)** Let $f : [a, b] \to \mathbb{R}$ be a uniformly continuous function on a closed bounded interval. Then $f$ is Riemann integrable on $[a, b]$.
    
</div>
<br>



<details class="proof">
<summary>Proof: Uniformly continuous function is Riemann integrable</summary>

Let $f : [a, b] \to \mathbb{R}$ be a uniformly continuous function on a closed bounded interval and let $\delta > 0$. By the uniform continuity of $f$, there exists $\epsilon > 0$ such that for all $x, x' \in [a, b]$, we have
    
$$\begin{equation}
|x_n - x_n'| < \epsilon \implies |f(x_n) - f(x_n')| \leq \delta.
\end{equation}$$
    
Let $N$ be the smallest integer such that $\frac{1}{N} < \epsilon$, and let $\mathcal{D}_N$ be the uniform dissection with $N$ intervals
    
$$\begin{equation}
\mathcal{D}_N = \left(0, ~\frac{1}{N}, ~\dots, ~\frac{N-1}{N}, ~1 \right).
\end{equation}$$
    
Then, if $x, x'$ are within a given interval of $\mathcal{D}_N$ we have $|x - x'| < \epsilon$ which implies $|f(x) - f(x')| < \delta$. Therefore
    
$$\begin{equation}
U_{\mathcal{D}_N}(f) - L_{\mathcal{D}_N}(f) < \delta,
\end{equation}$$
    
and $f$ is Riemann integrable by the {ref}`Riemann integrability condition<analysis-i-integrability>`.
    
</details>
<br>


<div class="lemma">

**Lemma (Monotone function on bounded closed interval is Riemann integrable)** Let $f : [a, b] \to \mathbb{R}$ be a monotone function on a bounded and closed interval. Then $f$ is Riemann integrable.
    
</div>
<br>



<details class="proof">
<summary>Proof: Monotone function on bounded closed interval is Riemann integrable</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a monotone function on a bounded and closed interval. Without loss of generality suppose $f$ is monotonic increasing. Let $\epsilon > 0$ and let $\mathcal{D} = (x_0, x_1, \dots, x_N)$ be a dissection of $[a, b]$ with mesh less than $\frac{\epsilon}{f(b) - f(a)}$. Then by 
    
$$\begin{align}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) &= \sum_{n=1}^N (x_n - x_{n-1}) (f(x_n) - f(x_{n-1})) \\
                                        &< \frac{\epsilon}{f(b) - f(a)} \sum_{n=1}^N (f(x_n) - f(x_{n-1})) \\
                                        &= \epsilon,
\end{align}$$
    
which implies that $f$ is Riemann integrable by the {ref}`Riemann integrability condition<analysis-i-integrability>`.

</details>
<br>
    


<div class="lemma">

**Lemma (Bounded function continuous on open interval is Riemann integrable)** Let $f : [a, b] \to \mathbb{R}$ be a bounded function which is continuous on $(a, b)$. Then $f$ is Riemann integrable on $[a, b]$.
    
</div>
<br>



<details class="proof">
<summary>Proof: Bounded function continuous on open interval is Riemann integrable</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a bounded function which is continuous on $(a, b)$. Since $f$ is bounded, there exists $C$ such that $|f(x)| < C$ for all $x \in [a, b]$. Let $\epsilon > 0$ and define $x_0 = a, x_N = b$. Choose $x_1, x_{N-1} \in [a, b]$ be such that 
    
$$\begin{equation}
x_1 - x_0, x_N - x_{N-1} < \frac{\epsilon}{8C}.
\end{equation}$$
    
Then $f$ is continuous on $[x_1, x_{N-1}]$ and we can find a dissection $\mathcal{D} = (x_1, x_2, \dots, x_{N-1})$ of $[x_1, x_{N-1}]$ such that
    
$$\begin{equation}
U_{\mathcal{D}'}(f) - L_{\mathcal{D}'}(f) < \frac{\epsilon}{2}
\end{equation}$$
    
Then definining $\mathcal{D} = (x_0, x_1, \dots, x_{N-1}, x_N)$ to be a dissection of $[a, b]$, we have
    
$$\begin{align}
U_{\mathcal{D}}(f) - L_{\mathcal{D}}(f) &= \sum_{n=1}^N (x_n - x_{n-1}) (f(x_n) - f(x_{n-1})) \\
                                        &= 2C \cdot \frac{\epsilon}{8C} + \sum_{n=2}^{N-1} (x_n - x_{n-1}) (f(x_n) - f(x_{n-1})) + 2C \cdot \frac{\epsilon}{8C} \\
                                        &\leq \frac{\epsilon}{2} + U_{\mathcal{D}'}(f) - L_{\mathcal{D}'}(f) \\
                                        &= \epsilon,
\end{align}$$
    
which implies that $f$ is Riemann integrable by the {ref}`Riemann integrability condition<analysis-i-integrability>`.

</details>
<br>

    


<div class="corollary">

**Corollary (Piecewise linear functinons are Riemann integrable)** Let $f : [a, b] \to \mathbb{R}$ be a piecewise linear functin on the closed bounded interval $[a, b]$. Then $f$ is Riemann integrable.
    
</div>
<br>



<details class="proof">
<summary>Proof: Piecewise linear functinons are Riemann integrable</summary>

Let $f : [a, b] \to \mathbb{R}$ be a piecewise linear functin on the closed bounded interval $[a, b]$. Partition the interval $[a, b]$ into $N$ equal sub-intervals $I_1, \dots, I_N$, which may or may not contain their end-points. Let $a_n = \inf I_n$ and $b_n = \sup I_n$ be the left and right end-points of $I_n$. Since $f$ is bounded on each $[a_n, b_n]$ and also continuous on each $(a_n, b_n)$, it is Riemann integrable on $[a, b]$ by the previous lemma. By the additivity property of the Riemann integral, it is Riemann integrable on $[a, b]$ as required.
    
</details>
<br>
    


<div class="lemma">

**Lemma (Uniform dissections tend to the Riemann integral)** Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function and let $\mathcal{D}_N$ be the uniform dissection of $[a, b]$ into $N$ intervals. Then
    
$$\begin{equation}
L_{\mathcal{D}_N}(f) \to \int_a^b f(x)dx ~~~\text{ and }~~~ U_{\mathcal{D}_N}(f) \to \int_a^b f(x)dx.
\end{equation}$$
    
</div>
<br>



<details class="proof">
<summary>Proof: Uniform dissections tend to the Riemann integral</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function and let $\epsilon > 0$. Since $f$ is Riemann integrable, there exists a dissection $\mathcal{D} = (x_0, \dots, x_M)$ such that
   
$$\begin{equation}
U_{\mathcal{D}}(f) < \int_a^b f(x)dx + \epsilon.
\end{equation}$$
    
Also, since $f$ is bounded, there must be a constant $C$ such that $|f(x)| < C$ for all $x \in [a, b]$. Now let $\mathcal{D}_N$ be the uniform dissection of $[a, b]$ into $N$ intervals, that is
    
$$\begin{equation}
\mathcal{D}_N = \left(0, ~\frac{1}{N}, ~\dots, ~\frac{N-1}{N}, ~1 \right),
\end{equation}$$
    
and $\mathcal{D}_N'$ be the least common refinement of $\mathcal{D}$ and $\mathcal{D}_N$. Then
    
$$\begin{equation}
U_{\mathcal{D}_N'}(f) < U_{\mathcal{D}}(f).
\end{equation}$$
    
Further, the two upper sums $U_{\mathcal{D}_N}(f)$ and $U_{\mathcal{D}_N'}(f)$ are the same except possibly for up to $M$ intervals of $\mathcal{D}_N$ which may have been refined in $\mathcal{D}_N'$. Then, each each of the intervals of $\mathcal{D}_N$ which has been refined can reduce the value of the upper sum by at most $\frac{(b-a)}{N} \cdot 2C$. Then
    
$$\begin{equation}
U_{\mathcal{D}}(f) - U_{\mathcal{D}_N'}(f) < \frac{(b-a)}{N} \cdot 2C \cdot M,
\end{equation}$$
    
from which we obtain     
    
$$\begin{align}
U_{\mathcal{D}}(f) &< U_{\mathcal{D}}(f) + \frac{(b-a)}{N} \cdot 2C \cdot M, \\
                   &< \int_a^b f(x)dx + \epsilon + \frac{(b-a)}{N} \cdot 2C \cdot M.
\end{align}$$
    
Now for any $N > \frac{(b-a)}{2CM}$, we have
    
$$\begin{align}
U_{\mathcal{D}}(f) &< \int_a^b f(x)dx + 2\epsilon,
\end{align}$$
    
which implies that as $N \to \infty$ 
    
$$\begin{equation}
U_{\mathcal{D}_N}(f) \to \int_a^b f(x)dx.
\end{equation}$$
    
The analogous result holds for the lower sum, namely that as $N \to \infty$ 
    
$$\begin{equation}
L_{\mathcal{D}_N}(f) \to \int_a^b f(x)dx,
\end{equation}$$
    
as required.
    
</details>
<br>
    
    
    
    
<div class="definition">

**Definition (Swapping integral endpoints)** Let $a < b \in \mathbb{R}$ and $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function. We define
    
$$\begin{equation}
\int_b^a f(x)dx = -\int_a^b f(x)dx.
\end{equation}$$
    
</div>
<br>
    


<div class="theorem">

**Theorem (Fundamental theorem of calculus, part 1)** Let $f : [a, b] \to \mathbb{R}$ be a continuous function and let $F : [a, b] \to \mathbb{R}$ be defined as
    
$$\begin{equation}
F(x) = \int_a^x f(x)dx.
\end{equation}$$
    
Then $F$ is differentiable on $(a, b)$ and $F'(x) = f(x)$.
    
</div>
<br>



<details class="proof">
<summary>Proof: Fundamental theorem of calculus, part 1</summary>
    
Let $f : [a, b] \to \mathbb{R}$ be a Riemann integrable function and
    
$$\begin{equation}
F(x) = \int_a^x f(x)dx.
\end{equation}$$
    
Then for $x > a$, we have
    
$$\begin{equation}
\lim_{h \to 0} \frac{F(x + h) - F(x)}{h} = \frac{1}{h} \int_x^{x+h} f(x')dx'.
\end{equation}$$
    
Now we wish to show that the right hand side tends to $f(x)$ as $h$ tends to zero. Let $\epsilon > 0$. We have
    
$$\begin{align}
\left|\frac{1}{h} \int_x^{x+h} f(x')dx' - f(x)\right| &= \left|\frac{1}{h} \int_x^{x+h} (f(x') - f(x))dx' - \right|, \\
                                                      &= \left|\frac{1}{h} \int_x^{x+h} |f(x') - f(x)|dx' - \right|.
\end{align}$$
    
Since $f$ is continuous, there exists $\delta > 0$ such that
    
$$\begin{equation}
|f(x') - f(x)| < \epsilon \text{ for all } |h| < \delta.
\end{equation}$$
    
Therefore, for all $|h| < \delta$ we have
    
$$\begin{equation}
\left|\frac{1}{h} \int_x^{x+h} f(x')dx' - f(x)\right| < \epsilon,
\end{equation}$$
    
as required.

</details>
<br>
    

Note that this theorem requires that the integrand $f$ is continuous. This is because if $f$ is discontinuous, even at a single point, then $F$ may not be differentiable. Consider for example letting $f$ be the step function
    
$$\begin{equation}
f(x) = \begin{cases}
0 & \text{ if } x \leq 0, \\
1 & \text{ otherwise.}
\end{cases}
\end{equation}$$
    
Then, $F$ has the form
    
$$\begin{equation}
F(x) = \begin{cases}
0 & \text{ if } x \leq 0, \\
x & \text{ otherwise, }
\end{cases}
\end{equation}$$
    
which is not differentiable. A similar argument could be made for more general functions with discontinuities. However, a similar result which does not require continuity also holds.
    


<div class="theorem">

**Theorem (Fundamental theorem of calculus, part 2)** Let $F : [a, b] \to \mathbb{R}$ be a differentiable function and let $f = F'$ be Riemann integrable. Then
    
$$\begin{equation}
\int_a^b f(x) dx = F(b) - F(a).
\end{equation}$$
    
</div>
<br>
    
    

<details class="proof">
<summary>Proof: Fundamental theorem of calculus, part 2</summary>
    
Let $F : [a, b] \to \mathbb{R}$ be a differentiable function and let $f(x) = F'(x)$. Let $\mathcal{D} = (x_0, \dots, x_N)$ be a dissection of $[a, b]$ and consider
    
$$\begin{align}
F(b) - F(a) &= \sum_{n=1}^N (F(x_n) - F(x_{n-1})) \\
            &= \sum_{n=1}^N (x_n - x_{n-1})\frac{F(x_n) - F(x_{n-1})}{x_n - x_{n-1}}.
\end{align}$$
    
From the {ref}`mean value theorem<analysis-i-mean-value-theorem>` for each $n = 1, \dots, N$ there exists $z_n \in [x_{n-1}, x_n]$ such that
    
$$\begin{align}
f(z_n) = F'(z_n) = \frac{F(x_n) - F(x_{n-1})}{x_n - x_{n-1}},
\end{align}$$
    
from which we obtain
    
$$\begin{align}
F(b) - F(a) &= \sum_{n=1}^N (x_n - x_{n-1})f(z_n).
\end{align}$$
    
Now, using the fact that
    
$$\begin{align}
\inf_{z \in [x_{n-1}, x_n]} f(z) \leq f(z_n) \leq \sup_{z \in [x_{n-1}, x_n]} f(z),
\end{align}$$
    
we obtain
    
$$\begin{equation}
L_{\mathcal{D}}(f) \leq F(b) - F(a) \leq U_{\mathcal{D}}(f),
\end{equation}$$
    
and since $f$ is Riemann integrable, the gap between the lower and upper sum above can be made arbitrarily small by choosing an appropriate discretisation $\mathcal{D}$, so
    
$$\begin{equation}
\int_a^b f(x) dx = F(b) - F(a),
\end{equation}$$
    
as required.

</details>
<br>
    
    
In contrast to the previous part of the theorem, this part does not require $F'$ to be continuous. However it does require $F'$ to be integrable. This is a necessary requirement because a function can be differentiable with a derivative that is not Riemann integrable. For example, consider the function
    
    
$$\begin{equation}
F(x) = \begin{cases}
x^2 \sin \left(\frac{1}{x^2}\right) & \text{ if } x \neq 0, \\
0 & \text{ otherwise.}
\end{cases}
\end{equation}$$

This function is differentiable with derivative
    
$$\begin{equation}
F'(x) = \begin{cases}
2x \sin \left(\frac{1}{x^2}\right) - \cos \left(\frac{1}{x^2}\right) & \text{ if } x \neq 0, \\
0 & \text{ if } x = 0.
\end{cases}
\end{equation}$$
    
Since the derivative $F'$ is unbounded, it cannot be Riemann integrable. Therefore, the theorem requirement that $F'$ is Riemann integrable for the result to hold.
    
    
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
