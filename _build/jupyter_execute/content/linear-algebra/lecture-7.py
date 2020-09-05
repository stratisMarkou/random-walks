# Eckart-Young and PCA

## Vector norms

- $\ell_1$ norm: $||v||_1 = |v_1| + |v_2| + ... + |v_n|$
- $\ell_2$ norm: $||v||_2 = \sqrt{v_1^2 + v_2^2 + ... + v_n^2}$
- $\ell_\infty$ norm: $||v||_\infty = \max|v_i|$

## Matrix norms

- Nuclear norm: $~~~||A||_{\text{Nuclear}} = \sum_{r = 1}^R \sigma_r$
- Frobenius norm: $||A||_F = \sqrt{\sum_{nm} |a_{nm}|^2}$
- Spectral norm: $~~||A||_2 = \max \sigma_r$

**Eckart-Young theorem:** If $B$ has rank $k$ and $A_k$ is the truncated SVD of $A$ up to the $k^{th}$ largest eigenvalue, then $||A - B|| \geq ||A - A_k||$.

