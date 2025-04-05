# Propositional calculus

:::{prf:definition} Proposition
:label: lst:def-proposition
Let $P$ be a set of _primitive propositions,_ (e.g. $p, q, r$).
The set of _propositions_, written as $L$ or $L(P)$ is defined inductively by

1. If $p \in P,$ then $p \in L.$
2. $\perp \in L,$ where $\perp$ is a proposition read as "false."
3. If $p, q \in L,$ then $(p \implies q) \in L.$

Equivalently, if $P$ is a primitive set of propositions, then

$$\begin{align}
L_0 &= \{\perp\} \cup P \\
L_{n+1} &= L_n \cup \{(p \implies q): p, q \in L_n\}
\end{align}$$

and $L = L_0 \cup L_1 \cup L_2 \cup \dots.$
:::

:::{margin}
One way to read the definition of $\neg$ is as follows.
$\neg p$ means the same as "$p$ implies $\perp,$" because the only way $\neg p$ can be true is if $p$ is false (given a false assumption, any conclusion is true).
Similarly, we can read the definition of $\wedge$ and $\vee,$ based off our definition of $\neg.$
:::
:::{prf:definition} Logical symbols
We define the symbols $\neg, \wedge, \vee$ as

$$\begin{align}
\neg p &= p \implies \perp \\
p \wedge q &= \neg (p \implies \neg q) \\
p \vee q &= (\neg p) \implies q  \\
\end{align}$$

where $p, q \in L.$
:::


## Semantic entailment

Semantic entailment assigns truth values to propositions, where we declare each proposition to either be "true" or "false" according to a _valuation_.

:::{prf:definition} Valuation
:label: lst:def-valuation
A valuation on $L$ is a function $v: L \to \{0, 1\},$ such that

$$\begin{align}
v(\perp) &= 0, \\
v(p \implies q) &= \begin{cases}
0 & \text{ if } v(p) = 1, v(q) = 0, \\
1 & \text{ otherwise }. \\
\end{cases}
\end{align}$$
:::

We interpret $v(p)$ to be the truth value of $p,$ with $0$ and $1$ denoting "false" and "true" respectively.

:::{prf:lemma} Equivalent valuations and extension to valuation
Suppose $P$ is a set of primitive propositions, and $L$ is the set of propositions derived from it.
Then
1. If $v$ and $v'$ are valuations with $v(p) = v'(p)$ for all $p \in P,$ then $v = v'.$
2. For any function $w: P \to \{0, 1\},$ we can extend it to a valuation $v: L \to \{0, 1\}$ such that $v(p) = w(p)$ for all $p \in P.$
:::

:::{dropdown} Proof: Equivalent valuations and extension to valuation
Suppose $P$ is a set of primitive propositions, and $L$ is the set of propositions derived from it.

__Part 1:__
Suppose that $v, v': L \to \{0, 1\}$ are valuations such that $v(p) = v'(p)$ for all $p \in P.$
By the defintion of {prf:def}`valuation<lst:def-proposition>`, $v(\perp) = v'(\perp),$ so $v(p) = v'(p)$ for all $p \in L_0.$
Suppose $p \in L_1.$
By the defintion of {prf:def}`proposition<lst:def-proposition>`, for all $p \in L_1,$ $p$ must be in the form $q \implies r$ for some $q, r \in L_0.$
Again, by the defintion of {prf:def}`valuation<lst:def-valuation>`, we have $v(q \implies r) = v'(q \implies r),$ which means that $v(p) = v'(p).$
Therefore $v(p) = v'(p)$ for all $p \in P.$
We proceeed inductively to show that $v(p) = v'(p)$ for all $p \in L_n$ for any $n.$

__Part 2:__
Suppose $w: P \to \{0, 1\}.$
Define $v: L \to \{0, 1\}$ to agree with $w$ on $P,$ that is $v(p) = w(p)$ for all $p \in P,$ and set $v(\perp) = 0.$
We then define $v$ inductively on $L_n$ according to {prf:ref}`lst:def-valuation` to obtain a valuation on $L.$
:::


:::{prf:definition} Tautology
:label: def:lst-tautology
We say $t$ is a tautology, written $\models t,$ if $v(t) = 1$ for any valuation $v: L \to \{0, 1\}.$
:::

To show that a statement is a tautology, we can use a [truth table](https://en.wikipedia.org/wiki/Truth_table), which is a big table that summarises the value that a valuation function takes on each proposition for each inductive step.
We can write out all possible starting combinations of truth values on $P,$ and the resulting propositions in $L,$ until we determine the value of the proposition we are after.
If the value of this proposition is true for any starting combination of truth values of $P,$ then it is a tautology.

:::{margin}
Note that here we have reused the symbol $\models$ that we introduced in our definition of {prf:ref}`tautology<def:lst-tautology>`.
This is not really an abuse of notation because the statement $\models t$ is equivalent to the statement $\emptyset \models t.$
:::
:::{prf:definition} Semantic entailment
:label: lst:def-semantic-entailment
For $S \subseteq L, t \in L$ we say $S$ entails $t,$ $S$ semantically implies $t$ or $S \models t,$ if for any $v$ such that $v(s) = 1$ for all $s \in S,$ we have $v(t) = 1.$
:::

:::{prf:definition} Truth and model
If $v(t) = 1,$ then we say that $t$ is true in $v,$ or $v$ is a model of $t.$
For $S \subseteq L,$ a valuation $v$ is a model of $S$ if $v(s) = 1$ for all $s \in S.$
:::

## Syntactic implication

:::{prf:definition} Proof axioms and modus ponens
:label: lst:def-proof-axioms-and-modus-ponens
We define the following three statements as the proof axioms
1. $p \implies (q \implies p),$
2. $(p \implies (q \implies r)) \implies ((p \implies q) \implies (q \implies r)),$
3. $(\neg \neg p) \implies p.$

We define the deduction rule of _modus ponens_ as:
from $p$ and $p \implies q$ we can deduce $q.$
:::

:::{prf:definition} Proof and syntactic entailment
:label: lst:def-proof-and-syntactic-entailment
For any $S \subseteq L,$ a proof of $t$ from $S$ is a finite sequence $t_1, t_2, \dots, t_n$ of propositions, with $t_n = t,$ such that each $t_i$ is one of the following:

1. An axiom;
2. A member of $S$;
3. A proposition $t_i$ such that there exist $j, k < i$ with $t_j$ being $t_k \implies t_i.$

If there is a proof of $t$ from $S,$ we say that $S$ proves, or syntactically entails $t,$ written $S \vdash t.$
If $\emptyset \vdash t,$ we say $t$ is a theorem and write $\vdash t.$
In a proof of $t$ from $S,$ $t$ is the conclusion and $S$ is the set of hypothesis or premises.
:::


:::{prf:lemma} Deduction theorem
Let $S \subseteq L$ and $p, q \in L.$
Then $S \vdash (p \implies q)$ if and only if $S \cup \{p\} \vdash q.$
:::

:::{dropdown} Proof: Deduction theorem
Let $S \subseteq L$ and $p, q \in L.$

__Implies:__
If $S \vdash (p \implies q),$ then there is a proof of $p \implies q$ from $S.$
Now, let $S \cup \{p\}$ be our set of assumptions.
We can append $p$ to the proof of $p \implies q$ from before, and then apply {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` to obtain $q.$

__Is implied by:__
Suppose $S \cup \{p\} \vdash q.$
This means there is a proof $t_1, t_2, \dots, t_n$ of $q$ from $S \cup \{p\}.$
We will show that $S \vdash p \implies t_i,$ which in turn amounts to a proof of $S \vdash p \implies q,$ by appending the statements of each $S \vdash p \implies t_i$ together.

From the {prf:ref}`definition of proof<lst:def-proof-and-syntactic-entailment>` there are finitely many possibilities for $t_i.$
We consider each of these separately.

__Case 1:__
$t_i$ is an {prf:ref}`axiom<lst:def-proof-axioms-and-modus-ponens>`.
We can write down
1. $t_i$ since $t_i$ is an axiom.
2. $p \implies (p \implies t_i)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
3. $p \implies t_i$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>`.

__Case 2:__ 
$t_i \in S.$
In this case, we have that
1. $t_i$ since $t_i$ is an assumption.
2. $p \implies (p \implies t_i)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
3. $p \implies t_i$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>`.

__Case 3:__
$t_i = p.$

__Case 4:__
$t_i$ has been obtained by modus ponens.
Then we have some $j, k < i$ such that $t_k = (t_j \implies t_i).$
We can assume that $S \vdash p \implies t_j$ and $S \vdash p \implies t_k$ by induction on $i.$
We can write down

1. $t_j \implies t_i$ is already known.
2. $p \implies (t_j \implies t_i)$ by {prf:ref}`axiom 1 and modus ponens<lst:def-proof-axioms-and-modus-ponens>`, similarly to the steps in the first two cases.
3. $(p \implies (t_j \implies t_i)) \implies ((p \implies t_j) \implies (p \implies t_i))$ by {prf:ref}`axiom 2<lst:def-proof-axioms-and-modus-ponens>` on (2).
4. $(p \implies t_j) \implies (p \implies t_i)$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` on (2) and (3).
5. $p \implies t_j$ is already known.
6. $p \implies t_i$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` on (4) and (5).
:::