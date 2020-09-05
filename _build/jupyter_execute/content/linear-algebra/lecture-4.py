# Eigenvalues and eigenvectors

$$A x = \lambda x$$

$$A^2 x = \lambda^2 x$$

- Writing vectors in terms of eigenvalues and eigenvectors helps
$$v = c_1 x_1 + ... + c_n x_n,~A^kv = c_1 \lambda_1^k x_1 + ... + c_n \lambda_n^k x_n$$

- Two matrices $A$ and $B$ are similar iff:$$B = M^{-1}AM$$ Similar matrices have the same eigenvalues, but not necessarily the same eigenvectors:\begin{align}
Bx = \lambda x \implies M^{-1}AMx &= \lambda x\\
A(Mx) &= \lambda (Mx)\\
\end{align}
- $AB$ and $BA$ have the same eigenvalues.
- Real symmetric matrices have real eigenvalues and orthogonal eigenvectors.
- Two ways to look at $A = X \Lambda X^{-1}$, when $X$ is full-rank: as projection but also as $AX = X \Lambda$.

