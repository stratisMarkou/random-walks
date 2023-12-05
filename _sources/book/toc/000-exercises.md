# Excercises

The following are my solutions to exercises from the book Sipser, _Introduction to the Theory of Computation_.
Here I repeat some exercise statements for completeness.
Any mistakes in the exercise statements or the solutions are my own.


## Chapter 1

::::{admonition} Exercise 1.1
:class: tip

Consider the DFAs $M_1$ and $M_2$ (see book).
For each DFA

1. What is the start state?
2. What is the set of accept states?
3. What sequence of steps does the machine go through on the input $aabb$?
4. Does the machine accept the input $aabb$?
5. Does the machine accept the empty string $\epsilon$?


:::{dropdown} Solution

1. The start state of $M_1$ is $q_1$. The start state of $M_2$ is $q_1$.
2. The set of accept states of $M_1$ is $\{q_2\}$. 
The set of accept states of $M_2$ is $\{q_1, q_4\}$.
3. Given the input $aabb$, $M_1$ goes through the sequence of states $q_1, q_2, q_3, q_1, q_1$. 
Given the same input, $M_2$ goes through the sequence $q_1, q_1, q_1, q_2, q_4$.
4. $M_1$ does not accept $aabb$, because when it receives this input it finishes at state $q_1$ which is not an accept state.
By contrast $M_2$ accepts $aabb$ because it finishes at $q_4$ which is an accept state.
5. $M_1$ does not accept $\epsilon$, since its initial state $q_1$ is not an accept state.
However, $M_2$ accepts $\epsilon$ since its initial state $q_1$ is an accept state.
:::
::::



::::{admonition} Exercise 1.2
:class: tip

Give formal descriptions for the FSAs in Excercise 1.1.

:::{dropdown} Solution

The FSA $M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)$ is defined as

$$\begin{align}
Q_1 &= \{q_1, q_2, q_3\} \\
\Sigma &= \{a, b\} \\
\delta_1(q, s) &= \begin{cases}
q_2 & q = q_1, s = a \\
q_1 & q = q_1, s = b \\
q_3 & q = q_2 \\
q_1 & q = q_3, s = a \\
q_1 & q = q_3, s = b
\end{cases} \\
F_1 &= \{q_2\}
\end{align}$$

The FSA $M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)$ is defined as

$$\begin{align}
Q_1 &= \{q_1, q_2, q_3, q_4\} \\
\Sigma &= \{a, b\} \\
\delta_2(q, s) &= \begin{cases}
q_1 & q = q_1, s = a \\
q_2 & q = q_1, s = b \\
q_3 & q = q_2, s = a \\
q_4 & q = q_2, s = b \\
q_2 & q = q_3, s = a \\
q_1 & q = q_3, s = b \\
q_3 & q = q_4, s = a \\
q_4 & q = q_4, s = b \\
\end{cases} \\
F_2 &= \{q_1, q_4\}
\end{align}$$
:::
::::



::::{admonition} Exercise 1.11
:class: tip

Prove that any NFA can be converted to an equivalent NFA with a singla accept state.

:::{dropdown} Solution

Given an NFA $M$ with accept states $F$, we can define another NFA $M'$ which has:

1. one additional state $q'$
2. $\epsilon$ transitions pointing from all states in $F$ to $q'$
3. accept state set $F' = \{q'\}$.

$M'$ and $M$ accept the same strings, and has a single final state.
:::
::::



````{admonition} Exercise 1.20
:class: tip

Let $\Sigma = \{a, b\}$.
For each of the regular expressions below give two example strings which are in the language, and two which are not:

1. $a^* b^*$
2. $a(ba)^*b$
3. $a^* \cup b^*$
4. $(aaa)^*$
5. $\Sigma^*a\Sigma^*b\Sigma^*a\Sigma^*$
6. $aba \cup bab$
7. $(\epsilon \cup a)b$
8. $(a \cup ba \cup bb)\Sigma^*$

```{dropdown} Solution

1. $a$ and $b$ are in the language, but $ba$ and $bab$ are not.
2. $ab$ and $abab$ are in the language, but $b$ and $bb$ are not.
3. $a$ and $b$ are in the language, but $ba$ and $bab$ are not.
4. $\epsilon$ and $aaa$ are in the language, but $a$ and $aa$ are not.
5. $aba$ and $abba$ are in the language but $b$ and $bb$ are not.
6. $aba$ and $bab$ are in the language, but $a$ and $b$ are not.
7. $b$ and $ab$ are in the language, but $a$ and $ba$ are not.
8. $a$ and $ba$ are in the language, but $b$ and $\epsilon$ are not.
```
````



::::{admonition} Exercise 1.31
:class: tip

For any string $w = w_1 w_2 \dots w_n$, the reverse of $w$, written $w^R$, is the string $w$ in reverse order, $w_n \dots w_2 w_1$.
For any language $A$, let $A^R = \{w^E | w \in A\}$.
Show that if $A$ is regular, so is $A^R$.

:::{dropdown} Solution

Suppose $A$ is a regular language over $\Sigma$, so there exists a DFA $M = (Q, \Sigma, \delta, q_0, F)$ that recognises it.
Let $q_0'$ be a new state and let $M' = (Q', \Sigma, \delta', q_0', F')$ be an NFA with the state set $Q' = Q \cup \{q_0'\}$, the transition function $\delta'$ defined as

$$\delta'(q, a) = \begin{cases}
F & q = q_0' \\
\{r \in Q | \delta(r, a) = q\} & q \neq q_0'
\end{cases}$$

and the accept state set $F = \{q_0\}$.
This NFA is equivalent to running $M$ in reverse nondeterministically and it recognises $A^R$.
Therefore $A^R$ is regular.


:::
::::




::::{admonition} Exercise 1.32
:class: tip

Let

$$ \Sigma_3 = \left\{
\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix},
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix},
\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix},
\dots,
\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix}
\right\} $$

$\Sigma_3$ contains all size $3$ columns of zeros and ones.
A string of symbols in $\Sigma_3$ gives three rows of zeros and ones.
Consider each row to be a binary number and let

$$ B = \{w \in \Sigma_3^* | \text{ the bottom row of } w \text{ is the sum of the top two rows}\}. $$

Show that $B$ is regular.


:::{dropdown} Solution

Consider the language $B^R$.
We will describe an NFA $M = (Q, \Sigma_3, \delta, q_0, F)$, which will perform addition of the binary numbers represented by the symbols of $\Sigma_3$.
Let $Q = \{q_0, q_1\}$ be the set of states and $F = \{q_0\}$.
We will use these states to keep track of the carry in the addition operation.
For $a \in \Sigma_3$, we will use the notation $a_1, a_2$ and $a_3$ to denote the first, second and third entries of $a$.
Then, let the transition function $\delta$ be

$$\delta(q, a) = \begin{cases}
q_0 & q = q_i, (i + a_1 + a_2) \mod 2 = a_3, (i + a_1 + a_2) // 2 = 0 \\
q_1 & q = q_i, (i + a_1 + a_2) \mod 2 = a_3, (i + a_1 + a_2) // 2 = 1
\end{cases}$$

Where $//$ denotes integer division.
This NFA accepts exactly those strings in $B^R$, which is therefore regular.
Since $B^R$ is regular, so is $B$, which shows the required result.

:::
::::





::::{admonition} Exercise 1.33
:class: tip

Let

$$ \Sigma_2 = \left\{
\begin{bmatrix}
0 \\
0
\end{bmatrix},
\begin{bmatrix}
0 \\
1
\end{bmatrix},
\begin{bmatrix}
1 \\
0
\end{bmatrix},
\dots,
\begin{bmatrix}
1 \\
1
\end{bmatrix}
\right\} $$

$\Sigma_2$ contains all size $2$ columns of zeros and ones.
A string of symbols in $\Sigma_2$ gives three rows of zeros and ones.
Consider each row to be a binary number and let

$$ C = \{w \in \Sigma_2^* | \text{ the bottom row of } w \text{ is three times the bottom row}\}. $$

Show that $C$ is regular.


:::{dropdown} Solution

Consider the language $C^R$.
We will describe an NFA $M = (Q, \Sigma_2, \delta, q_0, F)$, which will perform multiplication by $3$, checking if the bottom number is $3$ times the top number.
Let $Q = \{q_0, q_1, q_2\}$ be the set of states and $F = \{q_0\}$.
We will use these states to keep track of the carry.
As with the previous exercise if $a \in \Sigma_2$, we will use the notation $a_1$ and $a_2$ to denote the first and second entries of $a$.
Then, let the transition function $\delta$ be

$$\delta(q, a) = \begin{cases}
q_0 & q = q_i, (3a_1 + i) \mod 2 = a_2, (3a_1 + i) // 2 = 0 \\
q_1 & q = q_i, (3a_1 + i) \mod 2 = a_2, (3a_1 + i) // 2 = 1 \\
q_2 & q = q_i, (3a_1 + i) \mod 2 = a_2, (3a_1 + i) // 2 = 2
\end{cases}$$

where $//$ denotes integer division.
This NFA accepts exactly those strings in $C^R$, which is therefore regular.
Since $C^R$ is regular, so is $C$, which shows the required result.

:::
::::




::::{admonition} Exercise 1.34
:class: tip

Let $\Sigma_2$ be the same as in the previous problem.
A string of symbols in $\Sigma_2$ gives three rows of zeros and ones.
Consider each row to be a binary number and let

$$ D = \{w \in \Sigma_2^* | \text{ the bottom row of } w \text{ is a larger number than the bottom row}\}. $$

Show that $D$ is regular.


:::{dropdown} Solution

We will describe an NFA $M = (Q, \Sigma_2, \delta, q_0, F)$, which will compare two numbers in $D$ bit by bit.
Let $Q = \{q_e, q_s, q_l\}$ be the set of states and $F = \{q_l\}$.
As with the previous exercise if $a \in \Sigma_2$, we will use the notation $a_1$ and $a_2$ to denote the first and second entries of $a$.
Then, let the transition function $\delta$ be

$$\delta(q, a) = \begin{cases}
q_e & q = q_e, a_1 = a_2 \\
q_s & q = q_e, a_1 < a_2 \\
q_s & q = q_s, \\
q_l & q = q_e, a_2 > a_2 \\
q_l & q = q_l \\
\end{cases}$$

This NFA accepts exactly those strings in $D$, which is therefore regular.

:::
::::




::::{admonition} Exercise 1.34
:class: tip

Let $\Sigma_2$ be the same as in the previous problem.
A string of symbols in $\Sigma_2$ gives three rows of zeros and ones.
Consider each row to be a binary number and let

$$ D = \{w \in \Sigma_2^* | \text{ the bottom row of } w \text{ is a larger number than the bottom row}\}. $$

Show that $D$ is regular.


:::{dropdown} Solution

We will describe an NFA $M = (Q, \Sigma_2, \delta, q_0, F)$, which will compare two numbers in $D$ bit by bit.
Let $Q = \{q_e, q_s, q_l\}$ be the set of states and $F = \{q_l\}$.
As with the previous exercise if $a \in \Sigma_2$, we will use the notation $a_1$ and $a_2$ to denote the first and second entries of $a$.
Then, let the transition function $\delta$ be

$$\delta(q, a) = \begin{cases}
q_e & q = q_e, a_1 = a_2 \\
q_s & q = q_e, a_1 < a_2 \\
q_s & q = q_s, \\
q_l & q = q_e, a_2 > a_2 \\
q_l & q = q_l \\
\end{cases}$$

This NFA accepts exactly those strings in $D$, which is therefore regular.

:::
::::




::::{admonition} Exercise 1.41
:class: tip

For languages $A$ and $B$, let the perfect shuffle of $A$ and $B$ be the language

$$ \{w | w = a_1 b_1 \dots a_k b_k, \text{ where } a_1, \dots, a_k \in A \text{ and } b_1, \dots, b_k \in B, \text{ where } a_i, b_i \in \Sigma\}.$$

Show that the class of regular languages is closed under the perfect shuffle.

:::{dropdown} Solution

Let $A$ and $B$ are regular.
Since they are regular, there exist DFAs $M_A = (Q_A, \Sigma, \delta_A, q_A, F_A)$ and $B = (Q_B, \Sigma, \delta_B, q_B, F_B)$ that recognise them respectively.
Let $M = (Q, \Sigma, \delta, q_0, F)$ be the NFA defined as follows.
Let $a, b$ be two new states and let $Q = Q_A \times Q_B \times \{a, b\}$.
Let the initial state be $q_0 = (q_A, q_B, a)$, $F = F_A \times F_B \times \{b\}$ and the transition function be

$$
\delta((q_A, q_B, q), s) = \begin{cases}
(\delta_A(q_A, s), q_B, b) & q = a \\
(q_A, \delta_B(q_B, s), a) & q = b
\end{cases}.
$$

This NFA accepts exactly those strings in the perfect shuffle of $A$ and $B$, so the class of regular languages is closed under the perfect shuffle.

:::
::::




::::{admonition} Exercise 1.43
:class: tip

Let $A$ be any language.
Define $\texttt{DROPOUT}(A)$ to be the language containing all strings that can be obtain by removing one symbol from a string in $A$.
Thus

$$\texttt{DROPOUT}(A) = \{xz | xyz \in A \text{ where } x, z \in \Sigma^*, y \in \Sigma\}.$$

Show that the class of regular languages is closed under the $\texttt{DROPOUT}$ operation.


:::{dropdown} Solution

Let $A$ be a regular language.
Since $A$ is regular, there exists a machine $M_A$ that recognises it.
Define a new NFA $M = (Q, \Sigma, q, \delta, F)$, by making two copies of $M_A$, called $M_1 = (Q_1, \Sigma, q_1, \delta_1, F)$ and $M_2 = (Q_2, \Sigma, q_2, \delta_2, F_2)$, and combining them in the following way.
Let the state space be $Q = Q_1 \cup Q_2$, the initial state be $q = q_1$ and the set of final states be $F_2$, and the transition function be

$$ \delta(q_i, a) = \begin{cases}
\delta_1(q_i, a) & q_i \in Q_1, a \neq \epsilon \\
\delta_2(q_i', a) & q_i \in Q_1, a = \epsilon \\
\delta_2(q_i, a) & q_i \in Q_2 \\
\end{cases} $$

where if $q_i \in Q$, we write $q_i'$ to denote the state in $Q_2$ which is the copy of $q_i$.
The NFA $M$ recognises exactly those strings which are equal to a string in $A$, except a single symbol has been replaced by an $\epsilon$.
Therefore $A$ is regular.
:::
::::




::::{admonition} Exercise 1.44
:class: tip

Let $B$ and $C$ be languages over $\Sigma = \{0, 1\}$. Define

$$ B \overset{1}{\gets} C = \{w \in B | \text{ for some } y \in C, \text{ strings } w \text{ and } y \text{ contain equal numbers of } 1\text{s}\}$$

Show that the class of regular languages is closed under the $\overset{1}{\gets}$ operation.

:::{dropdown} Solution

Let $B$ and $C$ be regular languages over $\Sigma = \{0, 1\}$.
We will describe an NFA that recognises $B \overset{1}{\gets} C$.
Since $B$ and $C$ are regular, there exist DFAs $M_B$ and $M_C$ that recognise them.
Modify the DFA $M_C$ by replacing all its $0$ transitions by $\epsilon$ transitions and adding $0$ transition self-loops to every state, to obtain an NFA $M_C'$.
This NFA recognises the language

$$ L(M_C') = \{w \in \{0, 1\}^* | \text{ for some } y \in C, \text{ strings } w \text{ and } y \text{ contain equal numbers of } 1\text{s}\}.$$

Taking the intersection machine of $M_B$ and $M_C'$ produces a machine $M$ which recognises $L(M_B) \cap L(M_C')$, which is the language $B \overset{1}{\gets} C$.

:::
::::




::::{admonition} Exercise 1.45
:class: tip

Let $A / B = \{w | wx \in A, x \in B\}$.
If $A$ is regular and $B$ is any language, show that $A / B$ is regular.


:::{dropdown} Solution

Since $A$ is regular, there exists a DFA $M = (Q, \Sigma, \delta, q_0, F)$ which recognises it.
Now we describe an NFA $M'$ which recognises $A / B$.
Let $M' = (Q, \Sigma, \delta, q_0, F')$, where $F'$ is the set of states in $Q$ from which a state in $F$ is reachable given an input $x$ with $x \in B$.
Therefore, the machine $M'$ accepts a string $w$ if and only if $wx \in A$ for some $x \in B$, so $M'$ recognises $L(A / B)$, which therefore is regular.
:::
::::




::::{admonition} Exercise 1.46
:class: tip

Prove that the following languages are not regular.

1. $\{0^n 1^m 0^n | m, n \geq 0\}$
2. $\{0^m 1^n | m \neq n\}$
3. $\{w | w \in \{0, 1\}^* \text{ is not a palindrome}\}$
4. $\{wtw | w, t \in \{0, 1\}^+\}$

:::{dropdown} Solution

__Part 1:__
Suppose $A_1 = \{0^n 1^m 0^n | m, n \geq 0\}$ is regular.
Then by the pumping lemma, it has a pumping length $p$.
Consider the string $s = 0^p 1^p 0^p$.
Since $s \in A_1$, by the pumping lemma, it can be written as $s = xyz$ with $|xy| < p$ and $|y| \geq q$, and $xy^nz \in A_1$ for all $n = 1, 2, \dots$.
Since $|xy| < p$, both $x$ and $y$ are made up entirely of zeros.
So the string $xy^nz$ contains an an unequal number of leading and trailing zeros, so it is not in $A_1$.
This is a contradiction, so $A_1$ cannot be regular.

__Part 2:__
Suppose $A_2 = \{0^m 1^n | m \neq n\}$ is regular.
Then, its complement $A_2'$ is also regular.
From here on, the solution is essentially the same as for part 1.
By the pumping lemma, $A_2'$ has a pumping length $p$.
Consider the string $s = 0^p 1^p$.
Since $s \in A_2$, by the pumping lemma, it can be written as $s = xyz$ with $|xy| < p$ and $|y| \geq q$, and $xy^nz \in A_2$ for all $n = 1, 2, \dots$.
Since $|xy| < p$, both $x$ and $y$ are made up entirely of zeros.
So the string $xy^nz$ is of the form $0^k 1^m$ with $k \neq m$, so it is not in $A_2'$.
Therefore $A_2'$ is not regular, and neither is $A_2$.


__Part 3:__
Suppose $A_3 = \{w | w \in \{0, 1\}^* \text{ is not a palindrome}\}$ is regular.
Then, its complement $A_3'$ is also regular.
By the pumping lemma, $A_3'$ has a pumping length $p$.
Consider the string $s = 0^p 1^p 0^p$.
Since $s \in A_3$, by the pumping lemma, it can be written as $s = xyz$ with $|xy| < p$ and $|y| \geq q$, and $xy^nz \in A_2$ for all $n = 1, 2, \dots$.
Since $|xy| < p$, both $x$ and $y$ are made up entirely of zeros.
So the string $xy^nz$ contains an an unequal number of leading and trailing zeros, so it is not a palindrome, and therefore cannot be in $A_3'$.
Therefore, $A_3'$ is not regular and neither is $A_3$.


__Part 4:__
Suppose $A_4 = \{wtw | w, t \in \{0, 1\}^+\}$ is regular.
By the pumping lemma, $A_4$ has a pumping length $p$.
Fix some $t = 1$ and consider the string $s = 0^p 1^p t 0^p 1^p$.
Since $s \in A_4$, by the pumping lemma, it can be written as $s = xyz$ with $|xy| < p$ and $|y| \geq q$, and $xy^nz \in A_2$ for all $n = 1, 2, \dots$.
Since $|xy| < p$, both $x$ and $y$ are made up entirely of zeros.
So if $|y| = k$ the string $s_n = xy^{n+1}z$ has the form $s_n = 0^{p + nk}  1^p t 0^p 1^p$.
However, $s_n$ cannot be written in the form $wt'w$ for any $w, t' \in \{0, 1\}^+$, so $s_n \not \in A_4$ for any $n \geq 1$.
This is a contradiction, so $A_4$ cannot be regular.

:::
::::




::::{admonition} Exercise 1.47
:class: tip

Let $\Sigma = \{0, \#\}$ and let

$$ Y = \{w | w = x_1 \# x_2 \# \dots \# x_k \text{ for } k \geq 0, \text{ each } x_i \in 1^*, \text{ and } x_i \neq x_j \text{ for } i \neq j\}.$$

Prove that $Y$ is not regular.

:::{dropdown} Solution

Suppose $Y$ is regular.
Then by the pumping lemma, it has a pumping length $p$.
Fix an integer $k = 2p$ and consider the string $s = x_1 \# x_2 \# \dots \# x_k \in Y$ where $x_i = 1^i$ for $i = 1, 2, \dots$.
Since $s \in A_1$, by the pumping lemma, it can be written as $s = xyz$ with $|xy| < p$ and $|y| \geq q$, and $xy^nz \in Y$ for all $n = 1, 2, \dots$.
There are two cases.

__Case 1:__
If $y$ contains a $\#$ it can be written as $w_1\#w_2$.
Then $s = xy^3z = xw_1\#w_2w_1\#w_2w_1\#w_2z$, and the substring $w_2w_1$ is repeated, so $s \not \in Y$.
Therefore if $Y$ is regular, $y$ cannot contain a $\#$.

__Case 2:__
Since $y$ does not contain a $\#$ it can be written as $1^+$, and also it is a substring of $x_i$ for some $i < p$.
Then $s = xy^2z$ and $i + |y| < p$, it follows that $s$ contains the substring $\#x_i\# y = \#1^{i + |y|}\#$ twice, which cannot occur, reaching a contradiction.
Therefore $Y$ cannot be regular.

:::
::::




::::{admonition} Exercise 1.48
:class: tip

Let $\Sigma = \{0, 1\}$ and let

$$ D = \{w | w \text{ contains an equal number of occurences of the substrings } 01 \text{ and } 10\}.$$

Prove that $D$ is regular.

:::{dropdown} Solution

Let $\Sigma = \{0, 1\}$.
We will describe a DFA $M = (Q, \Sigma, \delta, q_0, F)$, that recognises $D$.
Let $Q = \{q_0, q_1, q_2, q_3, q_4\}$, $F = \{q_1, q_3\}$ and let the transition function $\delta$ be

$$\begin{equation}
\delta(q, a) = \begin{cases}
q_1 & q = q_0, a = 0 \\
q_1 & q = q_1, a = 0 \\
q_2 & q = q_1, a = 1 \\
q_2 & q = q_2, a = 1 \\
q_1 & q = q_2, a = 0 \\
q_3 & q = q_0, a = 1 \\
q_3 & q = q_3, a = 1 \\
q_4 & q = q_3, a = 0 \\
q_4 & q = q_4, a = 0 \\
q_3 & q = q_4, a = 1
\end{cases}
\end{equation}$$

This DFA recognises exactly those strings in $D$, which is therefore regular.

:::
::::




::::{admonition} Exercise 1.51
:class: tip
:name: toc-ex-151

Let $x$ and $y$ be strings and $L$ be any language.
We say that $x$ and $y$ are _distinguishable by $L$_ if some string $z$ exists whereby exactly one of the strings $xz$ and $yz$ is a member of $L$;
otherwise, for every string $z$, we have $xz \in L$ whenever $yz \in L$ and we say that $x$ and $y$ are indistinguishable by $L$.
If $x$ and $y$ are indistinguishable by $L$ we write $x \equiv_L y$.
Show that $\equiv_L$ is an equivalence relation.

:::{dropdown} Solution

To show that $\equiv_L$ is an equivalence relation, we must show that it satisfies the three properties of equivalence relations: reflexivty, symmetry and transitivity.
Let $x, y, w$ be strings.

__Reflexivity:__
We have that $x \equiv_L x$ because $xz \in L$ whenever $xz \in L$ for any string $z$.
So reflexivity is satisfied.

__Symmetry:__
Suppose $x \equiv_L y$, so $xz \in L \iff yz \in L$ for all strings $z$, otherwise $x$ and $y$ would be distinguishable.
Since $\iff$ is symmetric we have $zx \in L \iff zy \in L$, and $\equiv_L$ is symmetric.

__Transitivity:__
Supose $x \equiv_L y$ and $y \equiv_L w$.
Then $xz \in L \iff yz \in L$ and $yz \in L \iff wz \in L$ for all strings $z$.
Therefore $xz \in L \iff wz \in L$ for all strings $z$, and $\equiv_L$ is transitive.
:::
::::




::::{admonition} Exercise 1.52 (Myhill-Nerode theorem)
:class: tip
:name: toc-myhill-nerode-theorem

Let $L$ be a language and let $X$ be a set of strings.
We say that $X$ is pairwise distinguishable by $L$ if every two distinct strings in $X$ are distinguishable by $L$.
Define the index of $L$ to be the maximum number of elements in a set that is pairwise distinguishable by $L$.
The index of $L$ may be infinite or finite.

1. Show that, if $L$ is recognised by a DFA with $k$ states, $L$ has index at most $k$.
2. Show that, if the index of $L$ is a finite number $k$, it is recognised by a DFA with $k$ states.
3. Conclude that $L$ is regular if and only if it has finite index.
Moreover, its index is the size of the smallest DFA recognising it.

:::{dropdown} Solution

__Part 1:__
Let $L$ be recognised by a DFA, $M$, with $k$ states.
Suppose that the index of $L$ is greater than $k$.
Then, there exists a set $S$ containing $k + 1$ distinct strings which are all pairwise distinguishable by $L$.
Consider passing each of the strings in $S$ as input to $M$.
At the end of reading each of the strings, $M$ will be in some state.
By the pigeonhole principle, since there are more than $k$ strings and only $k$ states, two strings, say $s_1 \in S$ and $s_1 \in S$ must end up in the same final state.
Then, for any string $z$, including the empty string, the strings $s_1 z$ and $s_2 z$ will end up in the same final states, so they are either both accepted or both rejected by $M$, which means they are indistinguishable.
This is a contradiction, so $L$ cannot have an index greater than $k$.

__Part 2:__
Suppose that $L$ has a finite index $k$.
Then, there exists a finite set of strings of size $k$, say $S = \{s_1, \dots, s_k\}$, which is pairwise distinguishable by $L$.
We know, from {ref}`Exercise 1.51 <toc-ex-151>`, that indistinguishability under $L$ is an equivalence relation $\equiv_L$.
Now note that any string $z$ is indistiguishable from at least one string in $S$ (because if not, then the index of $L$ would be larger than $k$) and at most one string in $S$ (beacuse if $z \equiv_L s_i, s_j \in S$, then $s_i \equiv_L s_j$), so any string $z$ is indistinguishable from exactly one string in $L$.
Therefore the equivalence relation $\equiv_L$ forms exactly $k$ equivalence classes over the set of all finite strings, and $s_1, \dots, s_k$ are representatives of these classes.
Let $\pi(x)$ denote the equivalence class of a string $x$.
Now, define a DFA $M = (Q, \Sigma, q_0, \delta, F)$ as follows.
Let $\Sigma$ be the alphabet over which $L$ is defined.
Then, let $Q = \{\pi(s_1), \dots, \pi(s_n)\}$ be the states, $q_0 = \pi(\epsilon)$, $\delta(q, a) = \pi(xa)$ where $x$ is any string that satisfies $\pi(x) = q$ be the transition function, and $F = \{\pi(x) \in Q | x \in L\}$ be the set of initial states.
We need to show that this $M$ is well defined, that is we need to show that $\delta(q, a) = \pi(xa)$ gives the same answer regardless of which representative $x$ of $q$ we pick.
To show this, let $x, y$ be strings such that $\pi(x) = \pi(y) = q$.
Then $x$ and $y$ are in the same equivalence class so they are indistinguishable, so $xa$ and $ya$ are also indistinguishable, so $\pi(xa) = \pi(ya)$ as required and $\delta$ is well defined.
This DFA accepts exactly the strings in $L$ and no strings outside $L$, so it recognises $L$.


__Part 3:__
If $L$ is regular, then it is recognised by a DFA with a finite number of states so, by part 1, the index of $L$ is finite.
Conversely, if the index of $L$ if finite then, by part 2, it is recognised by a DFA, so it is regular.
Therefore $L$ is regular if and only if it has a finite index.
In addition, the index of $L$ is the size of the smallest DFA recognising it: part 2 implies that if the index of $L$ is $k,$ then it is recognised by a DFA with $k$ states and part 1 implies that $L$ cannot be recognised by a DFA with fewer than $k$ states.
:::
::::




:::{margin}
The problem in exercise 1.59 was first studied by Černý, who conjectured that a $k$-state synchronisable DFA has a synchronising sequence of length at most $(k-1)^2$.
The best known [upper bound](https://arxiv.org/pdf/1901.06542.pdf), by Shitov, is $\alpha O(k^3) + o(k^3)$ with $\alpha \leq 0.1654$.
Eppstein gave a [polynomial time algorithm](https://www.ics.uci.edu/~eppstein/pubs/Epp-SJC-90.pdf) for finding synchronising strings with length cubic in $k$ and Trahtman proved a [special case](https://arxiv.org/pdf/2105.09105.pdf) of Černý's conjecture for aperiodic DFAs.

:::

::::{admonition} Exercise 1.59
:class: tip

Let $M = (Q, \Sigma, \delta, q_0, F)$ be a DFA and let $h$ be a state of $M$ called its _home_.
A _synchronising sequence_ for $M$ and $h$ is a string $s \in \Sigma^*$  where $\delta(q, s) = h$ for every $q \in Q$.
(Here we have extended $\delta$ to strings, so that $\delta(q, s)$ equals the state where $M$ ends up when $M$ starts at state $q$ and reads input $s$.)
Say that $M$ is _synchronisable_ if it has a synchronising sequence for some state $h$.
Prove that if $M$ is a $k$-state synchronisable DFA, then it has a synchronising sequence of length  at most $k^3$.
Can you improve on this bound?

:::{dropdown} Solution

Let $M = (Q, \Sigma, \delta, q_0, F)$ be a $k$-state synchronisable DFA.
Since it is synchronisable, there exists a synchronising sequence $s = s_1\dots s_N$ where $s_1, \dots, s_N \in \Sigma$, with synchronising state $h$.
Let $q_i \neq q_j \in Q$ be two distinct states.
Since $h$ is a synchronising sequence, then $\{\delta(q_i, s), \delta(q_j, s)\} = \{h\}$.

Now consider the sequence of sets $P_n = \{\delta(q_i, s_1\dots s_n), \delta(q_j, s_1\dots s_n)\}$ for $n = 0, 1, \dots, N$.
If $P_n = P_{n+k}$ for any $0 \leq n \leq N - 1$ and any $k > 1$, we can obtain a shortened version of $s$, say $s'$,  with length $|s'| = N - k$, which still satisfies $\delta(q_i, s') = \delta(q_j, s') = h$, by removing the substring $s_{n+1} \dots s_{n+k}$ from $s$ to obtain $s' = s_1 \dots s_{n} s_{n+k+1} \dots s_N$.
We can repeat this procedure to obtain a string $s'$ which, when fed into $M$, produces a sequence of pairs of states such that no pair is repeated and the final pair is equal to $\{h\}$.
Because no pair is repeated, the maximum length of $s'$ is $k(k+1)/2$ by the pigeonhole principle.
Therefore for each pair of unique states $q_i \neq q_j \in Q,$ there exists a sequence $s'_{ij}$ which maps them both to $h$.

Now consider placing a distinct marker on each state, which moves according to the transition function when an input is fed into $M$.
Once two markers enter the same state, they cannot separate and stay joined.
By the result above, we can join any two markers with at most $k(k+1)/2$ symbols, regardless of the state from which state they are in, so we can join all of them with at most $k^2(k+1)/2$ symbols (by joining the first and the second marker, then joining the third marker to the already joined first and second markers, and so on).
This shows the required result, and slightly improves on it.
:::
::::




::::{admonition} Exercise 1.63
:class: tip

1. Let $L$ be an infinite regular language. Prove that $L$ can be split into two disjoint infinite regular languages.
2. Let $B$ and $D$ be two languages. Write $B \Subset D$ if $B \subset D$ and $D$ contains infinitely many strings not contained in $B$. Show that if $B$ and $D$ are two regular languages where $B \Subset D$, then we can find a regular language $C$ where $B \Subset C \Subset D$.

:::{dropdown} Solution

__Part 1:__
Let $L$ be an infinite regular language over $\Sigma$.
Since it is regular, by the {ref}`regular pumping lemma<toc-dfa-pumping-lemma>`, there exists a pumping length $p$ for $L$.
Since $L$ is infinite, it must contain strings of arbitrarily large lengths.
Choose a string $s \in L$ longer than $p$ which, by the pumping lemma can be written in the form $s = xyz$ such that $|y| \geq 1$ and $xy^nz \in L$ for all $n \geq 1$.
Therefore, $L$ contains strings for each of the lengths $|x| + n|y| + |z|$.
We will split $L$ in two other regular languages, one which contains all strings in $L$ that have length $|x| + 2n|y| + z$, and another which contains all the rest of the strings.

To do this, we can build a DFA $M$ which contains $N = |x| + 2|y| + |z| + 1$ states, and accepts all strings of length $|x| + 2n|y| + |z|$ for $n > 1$.
Let $M = (Q, \Sigma, \delta, q_1, F)$ have states $Q = \{q_0, q_1, \dots q_N\}$, initial state $q_0$, final state set $F = \{q_N\}$ and transition function

$$\delta(q_n, a) = \begin{cases}
q_{n+1} & n < N \\
q_{|x| + |z| + 1} & n = N
\end{cases}.$$

The DFA $M$ accepts all strings of length $N = |x| + 2n|y| + |z|$ for $n \geq 1$.
Since the class of regular languages is closed under intersections and complements, the language $L \cap L(M)$ is regular and thus also $L \cap (L \cap L(M))'$ is regular.
Both $L \cap L(M)$ and $L \cap L(M)'$ are infinite, disjoint and their union equals $L$, as required.

__Part 2:__
Suppose $B$ and $D$ are two regular languages where $B \Subset D$.
The assumption $B \Subset D$ means that the language $G = D \cap B'$, which is regular, is also infinite.
Then, by the previous result in part 1, we can split $G$ into two infinite regular disjoint languages $G_1$ and $G_2$ such that $G_1 \cup G_2 = G$.
Setting $C = B \cup G_1$ shows the required result.
:::
::::




::::{admonition} Exercise 1.67
:class: tip

Let the rotational closure of language $A$ be $\text{RC}(A) = \{yx | xy \in A\}$.
1. Show that for any language $A$, we have $\text{RC}(A) = \text{RC}(\text{RC}(A))$.
2. Show that the class of regular languages is closed under rotational closure.


:::{dropdown} Solution

__Part 1:__ 
Let $A$ be a language.
If $x \in A$, then the image of $\{x\}$ is the set of all strings which are cyclic permutations of the symbols in $x$.
Since the set of all cyclic permutations of a string includes the string itself, $\text{RC}(A) \subseteq \text{RC}(\text{RC}(A)).$
Conversely, applying two cyclic permutations to a string gives another cyclic permutation of the same string, so $\text{RC}(\text{RC}(A))\subseteq \text{RC}(A),$ concluding that $\text{RC}(A) = \text{RC}(\text{RC}(A))$.

__Part 2:__ 
Suppose $A$ is a regular language, so there exists a DFA $M = (Q, \Sigma, \delta, q_0, F)$ which recognises it.
Suppose $|Q| = N.$
Let $q_0'$ be a new initial state, and $Q_{n, 1}, Q_{n, 2}$ be copies of $Q$ for $n = 1, \dots, N.$
Let the $m^{th}$ state in $Q$ be denoted $q_m,$ and let the corresponding copies in $Q_{n, 1}$ and $Q_{n, 2}$ be $q_{n, m, 1}$ and $q_{n, m, 2}$ respectively.
Similarly, let the $k^{th}$ final state in $F$ be $f_k$ and let the corresponding copies in $Q_{n, 1}$ and $Q_{n, 2}$ be $f_{n, k, 1}$ and $f_{n, k, 2}$ respectively.
Finally, let $\delta_{n, 1}, \delta_{n, 2}$ be copies of $\delta$ for $n = 1, \dots, N.$

Now, $\epsilon$ transitions from $q_0'$ to each $q_{n, n, 1}.$
Also, add $\epsilon$ transitions from each $f_{n, k, 1}$ to $q_{n, 0, 2}.$
Let the states $q_{n, n, 2}$ for $n = 1, \dots, N$ be the final states, and let the transition function be the collection of the $\epsilon$ transitions described above, together with the individual transition functions $\delta_{n, 1}$ and $\delta_{n, 2}$ for $n = 1, \dots, N.$
Let us determine the language recognised by this NFA, by breaking down the transition into two stages.

__First stage:__
In the first stage, the NFA can first make a transition to any $q_{n, n, 1},$ without reading in a symbol.
Then, in the first stage, the NFA can make any sequence of transitions in $Q_{n, 1},$ according to $\delta_{n, 1}$ until it reaches a state $f_{n, k, 1}$ which is a copy of the final state $f_k$ from $F.$
At this point, the NFA has read a sequence of symbols $x_1\dots x_p$ that is a suffix of a string in $A,$ and it cannot have reached a terminal state.

__Second stage:__
Then, in the second stage, the NFA can make a transition to $q_{n, 0, 2},$ which is a copy of the initial state $q_0$ from $Q,$ without reading a symbol.
Then, the NFA can make a sequence of transitions in $Q_{n, 2}$ according to $\delta_{n, 2}$ until it reaches a final state $q_{n, n, 2},$ which is a copy of the state $q_n$ from $Q.$
During this second stage, the NFA reads a sequence of symbols $y_1, \dots, y_q$ if and only if it is a prefix of a string in $A,$ and also if after reading it, the original DFA $M$ would end up in state $q_n.$

__Conclusion:__
Threfore, the NFA reads a sequence of symbols $x_1\dots x_p y_1 \dots y_q$ if and only if: (1) starting from state $q_n,$ the DFA $M$ would end up in a final state after reading $x_1\dots x_p$ and also (2) the DFA $M$ would end up in state $q_n$ after reading $y_1 \dots y_q.$
Therefore, the NFA accepts a string $s$ if and only if it can be written as $s = y_1\dots y_q x_1\dots x_q$ where $x_1\dots x_p y_1 \dots y_q \in A,$ so it recognises $\text{RC}(A).$

:::
::::
