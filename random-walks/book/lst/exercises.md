# Exercises

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

$\newcommand{\vd}{\vdash}$
$\newcommand{\dvd}{\models}$
$\newcommand{\imp}{\Rightarrow}$
$\newcommand{\or}{\vee}$
$\newcommand{\and}{\wedge}$

::::{admonition} Exercise 1.1
:class: tip
Which of the following are tautologies?
1. $(p_1 \imp (p_2 \imp p_3)) \imp (p_2 \imp (p_1 \imp p_3))$
2. $((p_1 \or p_2) \and (p_1 \or p_3)) \imp (p_2 \or p_3)$
3. $(p_1 \imp (\neg p_2)) \imp (p_2 \imp (\neg p_1))$

:::{dropdown} Solution
__Proposition 1:__
This is a tautology because the only way a valuation of this proposition can be false is if

$$\begin{align}
v(p_1 \imp (p_2 \imp p_3)) &= 1,
v(p_2 \imp (p_1 \imp p_3)) &= 0.
\end{align}$$

The second condition can occur only if $v(p_2) = 1$ and $v(p_1 \imp p_3) = 0,$ which can in turn occur only if $v(p_1) = 1$ and $v(p_3) = 0.$
But if all of these conditions hold, then

$$\begin{equation}
v(p_1 \imp (p_2 \imp p_3)) = 0,
\end{equation}$$

which means that

$$\begin{equation}
v(p_1 \imp (p_2 \imp p_3)) \imp (p_2 \imp (p_1 \imp p_3)) = 1.
\end{equation}$$

Therefore the proposition is a tautology.

__Proposition 2:__
This is not a tautology because if $v(p_1) = 1$ and $v(p_2) = v(p_3) = 0,$ we have

$$\begin{align}
v(p_1 \or p_2) &= 1,
v(p_1 \or p_3) &= 1,
v((p_1 \or p_2) \and (p_1 \or p_3)) &= 1,
v(p_2 \or p_3) &= 0,
\end{align}$$

which implies that 

$$\begin{equation}
v(((p_1 \or p_2) \and (p_1 \or p_3)) \imp (p_2 \or p_3)) = 0.
\end{equation}$$

__Proposition 3:__
This is a tautology.
The only way for a valuation of this proposition to be false is if

$$\begin{align}
v(p_1 \imp (\neg p_2)) &= 1,
v(p_2 \imp (\neg p_1)) &= 0.
\end{align}$$

The latter of these conditions can occur only if $v(p_2) = 1$ and $v(\neg p_1) = 0,$ so $v(p_1) = 1.$
But that would imply $v(p_1 \imp (\neg p_2)) = 0.$
Contradiction.
:::
::::


::::{admonition} Exercise 1.2
:class: tip
Write down a proof of $\perp \imp q.$
Use this to write down a proof of $p \imp q$ from $\neg q.$

:::{dropdown} Solution

__Part 1:__
First, we show that if $a, b, c$ are propositions, then $a \imp c$ can be proved from $a \imp b$ and $b \imp c.$
To show this, we can use the steps

1. $(a \imp (b \imp c)) \imp ((a \imp b) \imp (a \imp c))$ from axiom 2.
2. $(b \imp c) \imp (a \imp (b \imp c))$ from axiom 1.
3. $(b \imp c)$ by hypothesis.
4. $(a \imp (b \imp c))$ by modus ponens on (2) and (3).
5. $(a \imp b) \imp (a \imp c)$ by modus ponens on (1) and (4).
6. $(a \imp b)$ by hypothesis.
7. $(a \imp c)$ by modus ponens on (5) and (6).

Now, consider the following steps

1. $\perp \imp (\neg q \imp \perp)$ from axiom 1.
2. $\perp \imp \neg \neg q,$ since this is the same as (2).
3. $\neg \neg q \imp q,$ by axiom 3.

We therefore have $\perp \imp \neg \neg q$ and $\neg \neg q \imp q.$
Repeating the first proof with $a = \perp, b = \neg \neg q, c = q,$ we obtain a proof for $\perp \imp q.$

__Part 2:__
We show that $\neg p \vd p \imp q.$
From the deduction theorem, we have $\neg p \vd p \imp q$ if and only if $\{\neg p, p\} \vd q.$
This is equivalent to $\perp \vd q,$ so we are done.
:::
::::

::::{admonition} Exercise 1.3
:class: tip
Use the deduction theorem to show that $p \vd \neg \neg p.$

:::{dropdown} Solution
Note that $\neg \neg p = \neg p \imp \perp.$
Therefore $p \vd \neg \neg p$ if and only if $p \vd \neg p \imp \perp.$
By the deduction theorem, this holds if and only if $\{p, \neg p\} \vd \perp,$ which we know holds.
We conclude that $p \vd \neg \neg p.$
:::
::::