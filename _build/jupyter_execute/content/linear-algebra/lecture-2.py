# Multiplying and Factoring Matrices


## Five matrix factorisations
Five matrix factorisations:

- $A = LU$ by elimination
- $A = QR$ by Gramm-Schmitt
- $S = Q \Lambda Q^\top$ by eigenproblem of a symmetric matrix
- $A = X \Lambda X^{-1}$ diagonalisation of $A$ by the eigenvector matrix $X$
- $A = U \Sigma V^\top$ singular value decomposition (SVD)

## LU factorisation by elimination

- A recipe for $A = LU$ factorisation in square matrices.
    - Subtract the first row from each other row enough times so that the first entry of the other rows is 0. Repeat using the second row, subtracting it from the third row onwards in the same way. Continue until the last row is reached. The resulting matrix is $U$ - upper-triangular. $L$ contains ones along its diagonal and the number of times each row was subtracted from each other row, in the appropriate position, so that $LU = A$.
    - A complication arises when the leading term of a row being subtracted is $0$. In that case, we can swap that row with another one that we haven't worked with yet and continue as normal. If no other row with a non-zero leading term can be found, then it can be shown that $A$ has a zero eigenvalue, i.e. it is singular.
    
- $LU$ elimination can be viewed as peeling off a part of the matrix at each elimination step.

## Four fundamental subspaces

If an $n \times m$ matrix $A$ has rank $r$, then:

1. $C(A) = C(A^\top) = r$.
2. $N(A) = m - r$, $C(A)$ and $N(A^\top)$ are orthogonal.
3. $N(A^\top) = n - r$, $C(A^\top)$ and $N(A)$ are orthogonal.

