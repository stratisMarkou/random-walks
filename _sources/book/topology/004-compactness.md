# Compactness

:::{prf:definition} Compact space
A topological space $X$ is compact if every open cover $\mathcal{V}$ of $X$ has a finite subcover $\mathcal{V}' = \{V_1, \dots, V_n\} \subseteq \mathcal{V}.$
:::

:::{prf:theorem} Closed interval is compact
The closed interval $[0, 1] \subseteq \mathbb{R}$ with the standard topology is compact.
:::

:::{dropdown} Closed interval is compact
Suppose $\mathcal{V}$ is an open cover of $[0, 1].$
Define

$$\begin{equation}
A = \{a \in [0, 1] : [0, a] \text{ has a finite subcover from } \mathcal{V} \}.
\end{equation}$$

We first show that $A$ is non-empty.
Since $\mathcal{V}$ is an open cover of $[0, 1],$ there exists $V \in \mathcal{V}$ that contains $0.$
Therefore $\{0\}$ has a finite sub-cover from $\mathcal{V}$ and $0 \in A.$

Now, let $\alpha = \sup A.$
Suppose $\alpha < 1.$
Since $\mathcal{V}$ covers $[0, 1],$ there exists open $V_\alpha \in \mathcal{V}$ with $\alpha \in V_\alpha.$
Since $V_\alpha$ is open, there exists $\epsilon > 0$ such that $B_\epsilon(\alpha) \subseteq V_\alpha.$
By the definition of $\alpha,$ the set $[0, \max(0, \alpha - \epsilon / 2)]$ has a finite subcover, to which we can add $V_\alpha$ to get a finite subcover of $[0, \min(1, \alpha + \epsilon / 2)].$
This leads to a contradiction, so $\alpha = 1.$

We finally show that $\alpha \in A.$
Repeating this argument, since $\mathcal{V}$ covers $[0, 1],$ there exists open $V_1 \in \mathcal{V}$ that contains $1,$ such that $(1 - \epsilon, 1] \subseteq V_1.$
Since $1 - \epsilon / 2 \in A,$ there exists a finite $\mathcal{V}' \subseteq \mathcal{V}$ which covers $[0, 1 - \epsilon].$
Then $\mathcal{W} = \mathcal{V}' \cup \{V_1\}$ is a finite subcover of $\mathcal{V}.$
:::