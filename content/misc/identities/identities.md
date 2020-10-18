# Useful identities

This is a collection of useful identities in probability and linear algebra.

## Gaussian distributions


<div class="lemma">

If $p(\mathbf{x}) = \mathcal{N}(\mathbf{x}; \mathbf{m}, \boldsymbol{\Sigma})$ and $\mathbf{f} : \mathbb{R}^n \to \mathbb{R}^m$ is a (differentiable) function, then
    
$$\begin{align}
\mathbb{E}_p \left[ \mathbf{f}(\mathbf{x})~(\mathbf{x} - \mathbf{m})^\top \right] = \mathbb{E}_p\left[ \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right] \boldsymbol{\Sigma},
\end{align}$$
    
where the jacobian matrix is given by
    
$$\begin{align}
\left[ \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right]_{ij} = \frac{\partial f_i}{\partial x_j}.
\end{align}$$
    
</div>
<br>
