# Gaussian Processes

The Gaussian Process (GP) is a powerful nonparametric model, which can be used for tasks like regression or classification. GPs perform exctremely well in small datasets, have theoretically attractive properties and are interpretable.

## Challenges and interesting leads for study and research
- **Scaling GPs to larger datasets:** the cost of making a prediction or optimising the hyperparameters of a GP, both scale like $\mathcal{O}(N^3)$. There is a large literature on scaling GPs to larger datasets.
- **Baking physical constraints into GP priors:** sometimes, we might have a strong prior on the function we are trying to model, in the form of some constraint. Examples include modelling electromagnetic fields, or the flow of fluids, which would have to obey Maxwell and Navier-Stokes respectively.
- **Theoretical guarantees about generalisation performance:** What theoretical guarantees can one have about the generalisation performance of a GP to test data?


## New on the Gaussian Processes section

- Fully Independent Training Conditionals (FITC) approximation.

## Coming soon

- An intro to GPs for regression and classification
- Deterministic Training Conditionals (DTC) approximation.
- Variational Free Energy (VFE) approximation.