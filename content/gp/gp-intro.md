# Gaussian Processes

The Gaussian Process (GP) is a powerful nonparametric model, which can be used for tasks like regression, classification and many other learning tasks. GPs perform exctremely well in small datasets, have theoretically attractive properties and are interpretable.

## Challenges and research areas

**Scaling GPs to larger datasets:** the cost of making a prediction or optimising the hyperparameters of a GP, both scale like $\mathcal{O}(N^3)$ in the number of training datapoints $N$. Similarly, sampling from a GP posterior also incurs a cost cubic in the number of test locations.

**Baking physical constraints into GP priors:** sometimes, we might have a strong prior on the function we are trying to model, which can be often stated in the form of a prior. Examples include modelling electromagnetic fields, which would have to obey Maxwell's equations.

**Theoretical guarantees about generalisation performance:** what theoretical guarantees can one have about the generalisation performance of a GP to test data?