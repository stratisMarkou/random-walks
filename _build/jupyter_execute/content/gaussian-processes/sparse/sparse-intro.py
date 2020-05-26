# Sparse Gaussian Processes

## How can sparsity help GPs scale?

To speed up hyperparameter learning and inference Gaussian Processes, it's clear that we'll have to give up something: if we want to work with the *exact* marginal likelihood and the *exact* predictive posterior

$$\begin{align}
p(\mathbf{y} | \mathbf{X}) &= \mathcal{N}\left(\mathbf{y}; \mathbf{0}, \mathbf{K}_{\mathbf{X}\mathbf{X}} + \sigma^2 \mathbf{I}\right),\\
p(\mathbf{y}^* | \mathbf{x}^*, \mathbf{y}, \mathbf{X}) &= \mathcal{N}\left(\mathbf{y}^*; \mathbf{K}_{\mathbf{x}^*\mathbf{X}} \left(\mathbf{K}_{\mathbf{X}\mathbf{X}} + \sigma^2 \mathbf{I} \right)^{-1} \mathbf{y}, \mathbf{K}_{\mathbf{x}^*\mathbf{x}^*} - \mathbf{K}_{\mathbf{x}^*\mathbf{X}} \left(\mathbf{K}_{\mathbf{X}\mathbf{X}} + \sigma^2 \mathbf{I} \right)^{-1}\mathbf{K}_{\mathbf{X}\mathbf{x}^*}\right),
\end{align}$$

we cannot do any better than suffering $\mathcal{O}(N^3)$ cost when calculating either quantity, because they both involve the inverse of an $N \times N$ covariance matrix. If we want to scale GPs to larger datasets *we cannot consider correlations between all datapoints* because of the cubic cost of inverting the associated covariance. One idea for scaling GPs to larger data is to make some approximations about the structure of the covariance matrix, such as an independence assumption between certain variables, which will make the matrix inversion cheaper.

## Literature on sparse Gaussian Processes


### Sparse Approximation methods
- Fully Independent Training Conditionals (FITC) approximation, originally called SPGP.
- Deterministic Training Conditionals (DTC) approximation.
- Variational Free Energy (VFE) approximation.
- Partial Independent Training Conditionals (PITC) approximation.

### Review papers
- *Turner, Yan and Bui*, A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation.
- *Quinonero-Candela and Rasmussen*, A Unifying View of Sparse Approximate Gaussian Process Regression.




```{toctree}
:hidden:
:titlesonly:


dtc
fitc
vfe
```
