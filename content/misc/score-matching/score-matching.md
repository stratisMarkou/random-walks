# Estimation by score matching

This page presents a useful trick due to Hyvarinen,{cite}`hyvarinen2005estimation` for estimating intractable probabilistic moodels via score-matching. Score matching can be used to train probabilistic models whose likelihood function takes the form

$$\begin{align}
p(x | \theta) = \frac{1}{Z} q(x; \theta),
\end{align}$$

where $q(x; \theta)$ is a positive function we can evaluate, but $Z$ is a normalising constant which we cannot evaluate in closed form. Such models are called non-normalised models. Non-gaussian Markov random fields are examples of such models.

## The score matching trick

The first step for the score-matching trick is to notice that taking the log and then the gradient with respect to $x$ of both sides eliminates the intractable $Z$

$$\begin{align}
\nabla \log p(x; \theta) = \nabla \log q(x; \theta),
\end{align}$$

since $Z$ does not depend on $x$. The gradient of the log-likelihood is called the score function

$$\begin{align}
\nabla \log p(x; \theta) = \psi(x; \theta).
\end{align}$$

The second step is to find a way to use the score function $\psi(x; \theta)$ along with some observed data, to estimate the parameters $\theta$. We can achieve this by defining the following score matching objective.

<div class="definition">
    
**Definition (Score matching objective)** Given a data distribution $p_d(x)$ and an approximating distribution $p(x; \theta)$ with parameters $\theta$, we define the score matching objective as
    
$$\begin{align}
J(\theta) = \frac{1}{2} \int p_d(x) || \psi(x; \theta) - \psi_d(x)||^2 dx,
\end{align}$$
    
where $\psi(x; \theta) = \nabla p(x;, \theta)$ and $\psi_d(x) = \nabla p_d(x)$ and the derivatives are with respect to $x$.
    
</div>
<br>

We observe that if $J(\theta) = 0$, then $\psi(x; \theta) = \psi_d(x)$ almost always. So we might expect that in this case the model distribution $p(x; \theta)$ and $p_d(x)$ will also be equal. This intuition is formalised by the following result.

<div class="theorem">
    
**Theorem (Score matching $\iff$ maximum likelihood)** Suppose that the probability density function of $x$ satisfies $p_d(x) = p(x; \theta)$ for some $\theta^*$ and also that if $\theta^* \neq \theta$ then $p(x; \theta) \neq p_d(x)$. Suppose also that $p(x; \theta) > 0$. Then
    
$$\begin{align}
J(\theta) = 0 \iff \theta = \theta^*.
\end{align}$$
    
</div>
<br>

<details class="proof">
<summary>Proof: Score matching \(\iff\) maximum likelihood</summary>
    
    
**Is implied by:** We can see that $\theta = \theta^* \implies J(\theta) = 0$ by substituting $p_d(x) = p(x; \theta^*)$ into $J(\theta^*)$ 
    
$$\begin{align}
J(\theta^*) &= \frac{1}{2} \int p_d(x) || \psi(x; \theta^*) - \psi_d(x)||^2 dx \\
            &= \frac{1}{2} \int p(x; \theta^*) || \psi(x; \theta^*) - \psi(x; \theta^*)||^2 dx \\
            &= 0.
\end{align}$$
    
**Implies:** Going the other direction, we can show that $J(\theta) = 0 \implies \theta = \theta^*$ by considering
    
$$\begin{align}
J(\theta) &= \frac{1}{2} \int p(x; \theta^*) || \psi(x; \theta) - \psi(x; \theta^*)||^2 dx = 0.
\end{align}$$
    
Since $p(x; \theta^*) > 0$, the above can hold only if $\psi(x; \theta) = \psi(x; \theta^*)$ for every $x$. This means that
    
$$\begin{align}
\psi(x; \theta) = \psi(x; \theta^*) + \text{const.} \implies p(x; \theta) \propto p(x; \theta^*),
\end{align}$$
    
and since $p(x; \theta^*)$ is a normalised probability distribution, we arrive at $p(x; \theta) = p(x; \theta^*)$. Now since the $p(x; \theta^*)$ is unique for the particular $\theta^*$, we have that $\theta = \theta^*$.

</details>
<br>

This result confirms the intuition that if the score functions (of the data distribution and the model) are equal, then the distributions equal as well. However, we note that this theorem assumes that $p_d(x) = p(x; \theta)$ for some $\theta$. In other words, it is assumed that the true model $p_d(x)$ is within the space of models we have hypothesised. In general this will not be true for true data, but at least the present result confirms that the expected behaviour is recovered in this idealised setting.

The last challenge is that in its definition $J(\theta)$ depends explicitly on $\psi_d(x)$, a function we do not have access to. In particular, expanding the term in the norm, we see that

$$\begin{align}
|| \psi(x; \theta) - \psi(x; \theta^*)||^2 = ||\psi(x; \theta)^\top\psi(x; \theta) - 2\psi(x; \theta)^\top\psi_d(x) + \psi_d(x)^\top\psi_d(x)||.
\end{align}$$

The first term is computable because we have access to $\psi(x; \theta)$. The latter term does not depend on $\theta$ and is therefore irrelevant for the optimisation of $J(\theta)$. However the middle term both depends on $\theta$ as well as the inaccessible score function of the data $\psi_d(x)$. Therefore this term must be considered in the optimisation of $J(\theta)$ but is also not directly computable. By using integration by parts, one can show{cite}`hyvarinen2005estimation` that this term can be rewritten in a way such that $J(\theta)$ can be estimated empirically.

<div class="theorem">
    
**Theorem (Equivalent form of $J$)** Given a score function $\psi(x; \theta)$ which is differentiable w.r.t. $x$ and satisfies some weak regularity conditions. Then the score-matching function $J$ can be writtten as
    
$$\begin{align}
J(\theta) = \int p_d(x) \sum^N_{i = 1}\left[ \partial_i \psi_i(x; \theta) + \frac{1}{2} \psi_{d, i}(x; \theta)^2 \right] dx + \text{const.},
\end{align}$$
    
where the $i$-subscript denotes the $i^{th}$ entry of vector being indexed and $\partial_i$ denotes the partial derivative with respect to $x_i$. The constant term is independent of $\theta$.
    
</div>
<br>

<details class="proof">
<summary>Proof: Equivalent form of \(J\)</summary>
    
Writing out $J$

$$\begin{align}
J(\theta) = \frac{1}{2} \int p_d(x) \left[ \psi(x; \theta)^\top\psi(x; \theta) - 2\psi(x; \theta)^\top\psi_d(x) + \psi_d(x)^\top\psi_d(x)\right] dx,
\end{align}$$
    
we see that the last term in the brackets evaluates to a constant that is independent of $\theta$. Using the fact that
    
$$\begin{align}
p_d(x) \psi_d(x) = p_d(x) \nabla \log p_d(x) = \nabla p_d(x),
\end{align}$$
    
and applying integration by parts, we obtain

$$\begin{align}
\int p_d(x) \psi(x; \theta)^\top\psi_d(x) dx &= \int \psi(x; \theta)^\top \nabla p_d(x) dx \\
&= \big[p_d(x) \psi(x; \theta) \big]_{-\infty}^{\infty} - \int p_d(x) \partial_i \psi_{d, i}(x; \theta) dx.
\end{align}$$
    
Substituting this into the expression for $J$ we arrive at
    
$$\begin{align}
J(\theta) = \int p_d(x) \sum^N_{i = 1}\left[ \partial_i \psi_i(x; \theta) + \frac{1}{2} \psi_{d, i}(x; \theta)^2 \right] dx + \text{const.}
\end{align}$$
    
</details>
<br>

The proof has used integration by parts to replace the intractable $\psi_d(x)$ term by a $p_d(x)$ term. This expression can be easily estimated if samples of $x$ are available, by replacing the expectation with respect to $p_d(x)$ by the empirical average over the samples. In this way, we can estimate the parameters $\theta$ of a non-normalised model, without resorting to computing estimates of the density $p_d(x)$.

## References

```{bibliography} ./references.bib
```