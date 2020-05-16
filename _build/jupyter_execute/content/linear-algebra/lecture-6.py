# Singular Value Decomposition

- Eigenvalue decompostition $S = Q\Lambda Q^\top$ applies only to square matrices.
- Introduce SVD, applicable to non-square matrices $A = U\Sigma V^\top$.

## SVD by solving eigendecomposition problems

1. Solve for $A^\top A = V \Sigma^\top U^\top U\Sigma V^\top  = V \Sigma^2 V^\top$, to get $V$ and $\Sigma$.
2. Then solve for $u_i = \frac{Av_i}{\sigma_i}$.

$A$ can then be written as $A = \sigma_1 v_1u_1^\top + ... + \sigma_r v_r u_r^\top$, where $r$ is the rank of $A$.

