# Estimation by score matching

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub" style="float: right;">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

Score matching a useful trick due to Hyvarinen{cite}`hyvarinen2005estimation` for learning the parameters of intractable probabilistic models.
Score matching can be used to train probabilistic models whose likelihood function takes the form

$$\begin{align}
p_\theta(x) = \frac{1}{Z_\theta} q_\theta(x),
\end{align}$$

where $q_\theta(x)$ is a positive function we can evaluate, but $Z_\theta$ is a normalising constant which we cannot evaluate in closed form.
Non-gaussian Markov random fields are examples of such models.

## The score matching trick

The first step for the score-matching trick is to notice that taking the log and then the gradient with respect to $x$ of both sides eliminates the intractable $Z_\theta$

$$\begin{align}
\nabla \log p_\theta(x) = \nabla \log q_\theta(x),
\end{align}$$

since $Z_\theta$ does not depend on $x$.
The gradient of the log-likelihood is called the score function

$$\begin{align}
\nabla \log p_\theta(x) = \psi_\theta(x).
\end{align}$$

The second step is to find a way to use the score function $\psi_\theta(x)$ along with some observed data, to estimate the parameters $\theta$.
We can achieve this by defining the following score matching objective.

:::{prf:definition} Score matching objective

Given a data distribution $p_d(x)$ and an approximating distribution $p_\theta(x)$ with parameters $\theta$, we define the score matching objective as
    
$$\begin{align}
J(\theta) = \frac{1}{2} \int p_d(x) || \psi_\theta(x) - \psi_d(x)||^2 dx,
\end{align}$$
    
where $\psi_\theta(x) = \nabla p_\theta(x)$ and $\psi_d(x) = \nabla p_d(x)$ and the derivatives are with respect to $x$.

:::

We observe that if $J(\theta) = 0$, then $\psi_\theta(x) = \psi_d(x)$ almost always.
So we might expect that in this case the model distribution $p_\theta(x)$ and $p_d(x)$ will also be equal. 
This intuition is formalised by the following result.

:::{prf:theorem} Matching scores $\iff$ matching distributions

Suppose that the probability density function of $x$ satisfies $p_d(x) = p_\theta(x)$ for some $\theta^*$ and also that if $\theta^* \neq \theta$ then $p_\theta(x) \neq p_d(x)$.
Suppose also that $p_\theta(x) > 0$. Then
    
$$\begin{align}
J(\theta) = 0 \iff \theta = \theta^*.
\end{align}$$
    
:::

:::{dropdown} Proof: Score matching $\iff$ maximum likelihood
    
    
__Is implied by:__
We can see that $\theta = \theta^* \implies J(\theta) = 0$ by substituting $p_d(x) = p_\theta(x)$ into $J(\theta^*)$ 
    
$$\begin{align}
J(\theta^*) &= \frac{1}{2} \int p_d(x) || \psi_{\theta^*}(x) - \psi_d(x)||^2 dx \\
            &= \frac{1}{2} \int p_\theta(x) || \psi_{\theta^*}(x) - \psi_{\theta^*}(x)||^2 dx \\
            &= 0.
\end{align}$$
    
__Implies:__
Going the other direction, we can show that $J(\theta) = 0 \implies \theta = \theta^*$ by considering
    
$$\begin{align}
J(\theta) &= \frac{1}{2} \int p_\theta(x) || \psi_\theta(x) - \psi_{\theta^*}(x)||^2 dx = 0.
\end{align}$$
    
Since $p_\theta(x) > 0$, the above can hold only if $\psi_\theta(x) = \psi_{\theta^*}(x)$ for every $x$. This means that
    
$$\begin{align}
\psi_\theta(x) = \psi_{\theta^*}(x) + \text{const.} \implies p_\theta(x) \propto p_\theta(x),
\end{align}$$
    
and since $p_\theta(x)$ is a normalised probability distribution, we arrive at $p_\theta(x) = p_\theta(x)$. Now since the $p_\theta(x)$ is unique for the particular $\theta^*$, we have that $\theta = \theta^*$.

:::

This result confirms the intuition that if the score functions (of the data distribution and the model) are equal, then the distributions equal as well.
However, we note that this theorem assumes that $p_d(x) = p_\theta(x)$ for some $\theta$.
In other words, it is assumed that the true model $p_d(x)$ is within the space of models we have hypothesised.
In general this will not be true for true data, but at least the present result confirms that the expected behaviour is recovered in this idealised setting.

The last challenge is that in its definition $J(\theta)$ depends explicitly on $\psi_d(x)$, a function we do not have access to.
In particular, expanding the term in the norm, we see that

$$\begin{align}
|| \psi_\theta(x) - \psi_{\theta^*}(x)||^2 = ||\psi_\theta(x)^\top\psi_\theta(x) - 2\psi_\theta(x)^\top\psi_d(x) + \psi_d(x)^\top\psi_d(x)||.
\end{align}$$

The first term is computable because we have access to $\psi_\theta(x)$.
The latter term does not depend on $\theta$ and is therefore irrelevant for the optimisation of $J(\theta)$.
However the middle term both depends on $\theta$ as well as the inaccessible score function of the data $\psi_d(x)$.
Therefore this term must be considered in the optimisation of $J(\theta)$ but is also not directly computable.
By using integration by parts, one can show{cite}`hyvarinen2005estimation` that this term can be rewritten in a way such that $J(\theta)$ can be estimated empirically.

:::{prf:theorem} Equivalent form of $J$

Let $\psi_\theta(x)$ be a score function which is differentiable with respect to $x.$
Then, under some weak regularity conditions on $\psi_\theta(x),$ the score-matching function $J$ can be writtten as
    
$$\begin{align}
J(\theta) = \int p_d(x) \sum^N_{i = 1}\left[ \partial_i \psi_{\theta, i}(x) + \frac{1}{2} \psi_{\theta, i}(x)^2 \right] dx + \text{const.},
\end{align}$$
    
where the $i$-subscript denotes the $i^{th}$ entry of vector being indexed and $\partial_i$ denotes the partial derivative with respect to $x_i$. The constant term is independent of $\theta$.
    
:::

:::{dropdown} Proof: Equivalent form of $~J$

    
Writing out $J$

$$\begin{align}
J(\theta) = \frac{1}{2} \int p_d(x) \left[ \psi_\theta(x)^\top\psi_\theta(x) - 2\psi_\theta(x)^\top\psi_d(x) + \psi_d(x)^\top\psi_d(x)\right] dx,
\end{align}$$
    
we see that the last term in the brackets evaluates to a constant that is independent of $\theta$. Using the fact that
    
$$\begin{align}
p_d(x) \psi_d(x) = p_d(x) \nabla \log p_d(x) = \nabla p_d(x),
\end{align}$$
    
and applying integration by parts, we obtain

$$\begin{align}
\int p_d(x) \psi_\theta(x)^\top\psi_d(x) dx &= \int \psi_\theta(x)^\top \nabla p_d(x) dx \\
&= \big[p_d(x) \psi_\theta(x) \big]_{-\infty}^{\infty} - \int p_d(x) \partial_i \psi_{\theta, i}(x) dx.
\end{align}$$
    
Substituting this into the expression for $J$ we arrive at
    
$$\begin{align}
J(\theta) = \int p_d(x) \sum^N_{i = 1}\left[ \partial_i \psi_{\theta, i}(x) + \frac{1}{2} \psi_{\theta, i}(x)^2 \right] dx + \text{const.}
\end{align}$$
    
:::



The proof has used integration by parts to replace the intractable $\psi_d(x)$ term by a $p_d(x)$ term.
This expression can be easily estimated if samples of $x$ are available, by replacing the expectation with respect to $p_d(x)$ by the empirical average over the samples.
In this way, we can estimate the parameters $\theta$ of a non-normalised model, without resorting to computing estimates of the density $p_d(x)$.

## References

```{bibliography}
:filter: docname in docnames
```