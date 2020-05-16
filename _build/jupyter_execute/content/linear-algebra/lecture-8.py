# Vector and matrix norms (again)

## Vector norms

The $\ell_p$ norm is defined as:

\begin{align}
||x||_p = \big(|x_1|^p + |x_2|^p + ... + |x_n|^p \big)^{1/p}
\end{align}

This is a norm (nonngeative, linear scaling, triangle inequality conditions) iff $p$ > 0. For various values of $p$ we get the norms:

- $\ell_0$ norm: $||x||_0 = \text{ \# non-zero components}$, (not really a norm).
- $\ell_1$ norm: $||x||_1 = |x_1| + |x_2| + ... + |x_n|$
- $\ell_2$ norm: $||x||_2 = \sqrt{x_1^2 + x_2^2 + ... + x_n^2}$
- $\ell_\infty$ norm: $||x||_\infty = \max|x_i|$

## Matrix norms

Norms are invariant under transformation by an orthogonal matrix:

- Nuclear norm: $~~~||A||_{\text{Nuclear}} = \sum_{r = 1}^R \sigma_r$
- Frobenius norm: $||A||_F = \sqrt{\sum_{nm} |a_{nm}|^2} = \sqrt{\sum_{r = 1}^R \sigma_r^2}$
- Spectral norm: $~~||A||_2 = \max \sigma_r$

