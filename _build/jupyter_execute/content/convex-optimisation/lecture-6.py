## Generalised linear-fractional programmes

## Quadratic programmes

**Quadratic Programme:** an optimisation problem of the form

\begin{align}
&\text{minimise}&& \frac{1}{2}x^\top P x + q^\top x + c\\
&\text{subject to}&& Gx \preccurlyeq h\\
& && Ax = b\\
\end{align}

where $P \succcurlyeq 0$.

**Least squares:**

**Linear programme with random cost:**

\begin{align}
&\text{minimise}&& \tilde{c}^\top x + \gamma x^\top \Sigma x = \mathbb{E}[c^\top x] + \gamma \text{Var}[c^\top x]\\
&\text{subject to}&& Gx \preccurlyeq h\\
& && Ax = b\\
\end{align}

**Quadratically constrained quadratic programme:** 

\begin{align}
&\text{minimise}&& \frac{1}{2}x^\top P x + q^\top x + c\\
&\text{subject to}&& \frac{1}{2}x^\top P_n x + q_n^\top x + c_n \leq 0, \text{ where } n = 1, 2, ..., N\\
& && Ax = b\\
\end{align}

**Second-order cone programming:**

\begin{align}
&\text{minimise}&& f^\top x \\
&\text{subject to}&& ||A_n x + b_n||_2 \leq c_n^\top x + d_n, \text{ where } n = 1, 2, ..., N\\
& && Fx = g\\
\end{align}

## Geometric programmes

**Monomial functions:** a function of the form $$f(x) = cx_1^{a_1}x_2^{a_2}...x_n^{a_n},$$ where $\textbf{dom}~f = \mathbb{R}^n_{++}$ with $c > 0, a_i \in \mathbb{R}$.

**Posynomial function:** a function that is the sum of monomials $$ f(x) = \sum^K_{k = 1} c_kx_1^{a_{1k}}x_2^{a_{2k}}...x_K^{a_{1K}}$$ where $\textbf{dom}~f = \mathbb{R}^n_{++}$ with $c > 0, a_{ik} \in \mathbb{R}$.

**Geometric programme:** a (non-convex) problem with posynomial inequalities and monomial equality constraints \begin{align}
&\text{minimise} && f_0(x) &&&\\
&\text{subject to} && f_n(x) \leq 1, &&& n = 1,..., N\\
& && h_m(x) = 1, &&& m = 1,..., M
\end{align}

Geometric programmes are not convex but can be converted to convex ones by making a change of variables $y_i = \log x_i$ and minimise the $\log$ of $f_0$.

### Cantilever beam example

### Minimising the spectral radius of a nonnegative matrix

