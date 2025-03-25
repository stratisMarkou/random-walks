# Connectivity

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>


:::{prf:definition} Connected space
A topological space $X$ is disconnected if $X$ can be written as $A \cup B,$ where $A$ and $B$ are disjoint, non-empty open subsets of $X.$
We say $A$ and $B$ disconnect $X.$
A space is connected if it is not disconnected.
:::

:::{prf:definition} Connected subspace
Given a subset $A$ of a topological space $X,$ we say that $A$ is connected if $A$ is connected as a subspace of $X.$
:::

:::{prf:lemma} Equivalent condition for connectedness
A space $X$ is disconnected if and only if there exists a contunuous surjective $f: X \to \{0, 1\}$ with the discrete topology.
:::

:::{dropdown} Proof
Suppose $X$ is disconnected.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $X = A \cup B.$
Define $f: X \to \{0, 1\}$ by

$$f(x) = \begin{cases}
0 & \text{if } x \in A, \\
1 & \text{if } x \in B.
\end{cases}$$

Now, we note that $f$ is surjective because $A$ and $B$ are non-empty.
In addition, $f$ is continuous because $f^{-1}(\{0\}) = A$ and $f^{-1}(\{1\}) = B$ are open.
Thus, $f$ is continuous and surjective.

Conversely, suppose there exists a continuous surjective $f: X \to \{0, 1\}$ with the discrete topology.
Then the disjoint sets $f^{-1}(\{0\})$ and $f^{-1}(\{1\})$ are non-empty (because $f$ is surjective) and open (because $f$ is continuous).
Thus, $X$ is disconnected.
:::


:::{prf:theorem} Closed inverval is connected
The closed interval $[0, 1]$ with the standard topology is connected.
:::

:::{dropdown} Proof
Suppose $[0, 1]$ is disconnected.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $[0, 1] = A \cup B.$
Without loss of generality, we may assume that $1 \in B.$
Since $A$ is non-empty, $\alpha = \sup A$ exists and $\alpha \in [0, 1].$
There are two possibilities, either $\alpha \in A$ or $\alpha \in B.$

If $\alpha \in A,$ then $\alpha < 1$ and we immediately have a contradiction because, since $A$ is open, there exists an open interval $(\alpha - \varepsilon, \alpha + \varepsilon) \subseteq [0, 1]$ contained in $A$ for some $\varepsilon > 0,$ which means that $\alpha$ cannot be the supremum of $A.$
Therefore, $\alpha \in B.$
However, again, this raises a contradiction because, since $B$ is open, there exists an open interval $(\alpha - \varepsilon, \alpha + \varepsilon) \subseteq [0, 1]$ contained in $B$ for some $\varepsilon > 0,$ which means that $\alpha$ cannot be the supremum of $A.$
Thus, $[0, 1]$ is connected.
:::


:::{prf:lemma} Image of connected space under continuous map is connected
Let $f: X \to Y$ be a continuous map.
If $X$ is connected, then $f(X)$ is connected.
:::

:::{dropdown} Proof
Suppose $f(X)$ is disconnected.
Then there exist disjoint, non-empty open sets $A$ and $B$ such that $f(X) = A \cup B.$
Define $U = f^{-1}(A)$ and $V = f^{-1}(B).$
Then $U$ and $V$ are disjoint, non-empty open sets in $X,$ and $X = U \cup V.$
Therefore $X$ is disconnected, which is a contradiction.
Thus, $f(X)$ is connected.
:::
