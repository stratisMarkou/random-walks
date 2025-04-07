# Propositional calculus

$\newcommand{\vd}{\vdash}$
$\newcommand{\dvd}{\models}$
$\newcommand{\imp}{\Rightarrow}$


:::{prf:definition} Proposition
:label: lst:def-proposition
Let $P$ be a set of _primitive propositions,_ (e.g. $p, q, r$).
The set of _propositions_, written as $L$ or $L(P)$ is defined inductively by

1. If $p \in P,$ then $p \in L.$
2. $\perp \in L,$ where $\perp$ is a proposition read as "false."
3. If $p, q \in L,$ then $(p \imp q) \in L.$

Equivalently, if $P$ is a primitive set of propositions, then

$$\begin{align}
L_0 &= \{\perp\} \cup P \\
L_{n+1} &= L_n \cup \{(p \imp q): p, q \in L_n\}
\end{align}$$

and $L = L_0 \cup L_1 \cup L_2 \cup \dots.$
:::

:::{margin}
One way to read the definition of $\neg$ is as follows.
$\neg p$ means the same as "$p$ implies $\perp,$" because the only way $\neg p$ can be true is if $p$ is false (given a false assumption, any conclusion is true).
Similarly, we can read the definition of $\wedge$ and $\vee,$ based off our definition of $\neg.$
:::
:::{prf:definition} Logical symbols
:label: lst:def-logical-symbols
We define the symbols $\neg, \wedge, \vee$ as

$$\begin{align}
\neg p &= p \imp \perp \\
p \wedge q &= \neg (p \imp \neg q) \\
p \vee q &= (\neg p) \imp q  \\
\end{align}$$

where $p, q \in L.$
:::


## Semantic entailment

Semantic entailment assigns truth values to propositions, where we declare each proposition to either be "true" or "false" according to a _valuation_.

:::{prf:definition} Valuation
:label: lst:def-valuation
A valuation on $L$ is a function $v: L \to \{0, 1\},$ such that

$$\begin{equation}
v(\perp) = 0,~~ v(p \imp q) = \begin{cases}
0 & \text{ if } v(p) = 1, v(q) = 0, \\
1 & \text{ otherwise }. \\
\end{cases}
\end{equation}$$
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
By the defintion of {prf:def}`proposition<lst:def-proposition>`, for all $p \in L_1,$ $p$ must be in the form $q \imp r$ for some $q, r \in L_0.$
Again, by the defintion of {prf:def}`valuation<lst:def-valuation>`, we have $v(q \imp r) = v'(q \imp r),$ which means that $v(p) = v'(p).$
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
1. $p \imp (q \imp p),$
2. $(p \imp (q \imp r)) \imp ((p \imp q) \imp (q \imp r)),$
3. $(\neg \neg p) \imp p.$

We define the deduction rule of _modus ponens_ as:
from $p$ and $p \imp q$ we can deduce $q.$
:::

:::{prf:definition} Proof and syntactic entailment
:label: lst:def-proof-and-syntactic-entailment
For any $S \subseteq L,$ a proof of $t$ from $S$ is a finite sequence $t_1, t_2, \dots, t_n$ of propositions, with $t_n = t,$ such that each $t_i$ is one of the following:

1. An axiom;
2. A member of $S$;
3. A proposition $t_i$ such that there exist $j, k < i$ with $t_j$ being $t_k \imp t_i.$

If there is a proof of $t$ from $S,$ we say that $S$ proves, or syntactically entails $t,$ written $S \vdash t.$
If $\emptyset \vdash t,$ we say $t$ is a theorem and write $\vdash t.$
In a proof of $t$ from $S,$ $t$ is the conclusion and $S$ is the set of hypothesis or premises.
:::

::::{prf:example} $p \imp p$ is a theorem
:label: lst:ex-p-imp-p-is-a-theorem
We have that $\vd p \imp p,$ that is, $p \imp p$ is a theorem.

:::{dropdown} Proof
1. $(p \imp ((p \imp p) \imp p)) \imp ((p \imp (p \imp p)) \imp (p \imp p))$ by {prf:ref}`axiom 2<lst:def-proof-axioms-and-modus-ponens>`.
2. $p \imp ((p \imp p) \imp p)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
3. $(p \imp (p \imp p)) \imp (p \imp p)$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` on (1) and (2).
4. $p \imp (p \imp p)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
5. $p \imp p$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` on (3) and (4).
:::
::::


:::{prf:theorem} Deduction theorem
:label: lst:thm-deduction-theorem
Let $S \subseteq L$ and $p, q \in L.$
Then $S \vdash (p \imp q)$ if and only if $S \cup \{p\} \vdash q.$
:::

:::{dropdown} Proof: Deduction theorem
Let $S \subseteq L$ and $p, q \in L.$

__Implies:__
If $S \vdash (p \imp q),$ then there is a proof of $p \imp q$ from $S.$
Now, let $S \cup \{p\}$ be our set of assumptions.
We can append $p$ to the proof of $p \imp q$ from before, and then apply {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` to obtain $q.$

__Is implied by:__
Suppose $S \cup \{p\} \vdash q.$
This means there is a proof $t_1, t_2, \dots, t_n$ of $q$ from $S \cup \{p\}.$
We will show that $S \vdash p \imp t_i,$ which in turn amounts to a proof of $S \vdash p \imp q,$ by appending the statements of each $S \vdash p \imp t_i$ together.

From the {prf:ref}`definition of proof<lst:def-proof-and-syntactic-entailment>` there are finitely many possibilities for $t_i.$
We consider each of these separately.

__Case 1:__
$t_i$ is an {prf:ref}`axiom<lst:def-proof-axioms-and-modus-ponens>`.
We can write down
1. $t_i$ since $t_i$ is an axiom.
2. $p \imp (p \imp t_i)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
3. $p \imp t_i$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>`.

__Case 2:__ 
$t_i \in S.$
In this case, we have that
1. $t_i$ since $t_i$ is an assumption.
2. $p \imp (p \imp t_i)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
3. $p \imp t_i$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>`.

__Case 3:__
$t_i = p.$
From {prf:ref}`lst:ex-p-imp-p-is-a-theorem` we know $\vdash p \imp p,$ so $p \imp t_i.$

__Case 4:__
$t_i$ has been obtained by modus ponens.
Then we have some $j, k < i$ such that $t_k = (t_j \imp t_i).$
We can assume that $S \vdash p \imp t_j$ and $S \vdash p \imp t_k$ by induction on $i.$
We can write down

1. $t_j \imp t_i$ is already known.
2. $p \imp (t_j \imp t_i)$ by {prf:ref}`axiom 1 and modus ponens<lst:def-proof-axioms-and-modus-ponens>`, similarly to the steps in the first two cases.
3. $(p \imp (t_j \imp t_i)) \imp ((p \imp t_j) \imp (p \imp t_i))$ by {prf:ref}`axiom 2<lst:def-proof-axioms-and-modus-ponens>` on (2).
4. $(p \imp t_j) \imp (p \imp t_i)$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` on (2) and (3).
5. $p \imp t_j$ is already known.
6. $p \imp t_i$ by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` on (4) and (5).
:::


:::{prf:theorem} Soundness theorem
:label: lst:thm-soundness-theorem
If $S \vd t,$ then $S \dvd t.$
:::

:::{dropdown} Proof: Soundness theorem
Suppose $S \vd t.$
Then, there exists a proof $t_1, \dots, t_n$ of $t$ from $S.$
Now, suppose that $v: L \to \{0, 1\}$ is a valuation with $v(s) = 1$ for all $s \in S.$
We will show that $v(t_i) = 1$ for all $t_i$ in the proof.

If $t_i$ is an {prf:ref}`axiom<lst:def-proof-axioms-and-modus-ponens>`, then $v(t_i) = 1$ because all three axioms are tautologies.
If $t_i$ is a hypothesis, then $t_i \in S$ and $v(t_i) = 1$ by assumption.
If $t_i$ has been obtained by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>`, then there are some $j, k < i$ such that $t_k = t_j \imp t_i.$
This means that $v(t_j) = 1$ and $v(t_j \imp t_i) = 1$ so we must have $v(t_i) = 1.$

We conclude that $v(t_i) = 1$ for all $t_i$ in the proof, including $t_n$ which is equal to $t.$
Therefore $S \dvd t.$
:::


:::{prf:definition} Consistent
:label: lst:def-consistent
$S$ is inconsistent if $S \vd \perp.$
S is consistent if it is not inconsistent.
:::



:::{prf:lemma} Consistent assumptions can be extended
:label: lst:lem-consistent-assumptions-can-be-extended
For {prf:ref}`consistent<lst:def-consistent>` $S \subseteq L$ and $p \in L,$ at least one of $S \cup \{p\}$ and $S \cup \{\neg p\}$ is consistent.
:::

:::{dropdown} Proof: Consistent assumptions can be extended
Suppose $L$ is a set of propositions, $S \subseteq L$ and $p \in L.$
Suppose $S \cup \{p\}$ and $S \cup \{\neg p\}$ are both inconsistent.
Then, we have $S \cup \{p\} \vd \perp$ and $S \cup \{\neg p\} \vd \perp.$
By the {ref}`deduction theoremlst:thm-deduction-theorem`, we have that $S \vd p \implies \perp$ and also that $S \vd (\neg p) \implies \perp.$
Note that $(\neg p) = p \imp \perp,$ and using {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` from the proof of $p$ from $S,$ we have $S \vd \perp.$
Therefore $S$ is inconsistent which is a contradiction, and at least one of $S \cup \{p\}$ and $S \cup \{\neg p\}$ has to be consistent.
:::


:::{prf:theorem} Model existence
:label: lst:thm-model-existence
Let $L$ be a countable set of propositions.
If $S \dvd \perp,$ then $S \vd \perp.$
In other words, if $S$ has no model, then $S$ is {prf:ref}`inconsistent<lst:def-consistent>`.
Equivalently, if $S$ is {prf:ref}`consistent<lst:def-consistent>`, then $S$ has a model.
:::


:::{dropdown} Proof: Model existence
Assume $L$ is countable and list it as $\{t_1, t_2, \dots\}.$
Let $S \subseteq L$ be consistent and define $S_0 = S.$
Then by {prf:ref}`lst:lem-consistent-assumptions-can-be-extended`, at least one of $S \cup \{t_1\}$ and $S \cup \{\neg t_1\}$ is consistent.
Define $S_1$ to be the consistent one.
Then, let $S_2$ be $S_1 \cup \{t_2\}$ or $S_1 \cup \{\neg t_2\},$ such that $S_2$ is consistent, and continue inductively.

Set $\bar{S} = S_0 \cup S_1 \cup \dots.$
Then $p \in \bar{S}$ or $\neg p \in \bar{S}$ for each $p \in L$ by construction.
Also, we know that $\bar{S}$ is consistent:
if $\bar{S} \vd \perp,$ then since proofs are finite, there is some $S_n$ that contains all the assumptions used in the proof of $\bar{S} \vd \perp.$
Hence $S_n \vd \perp,$ but we know that all $S_n$ are consistent.
Finally, we check that $\bar{S}$ is deductively closed:
if $\bar{S} \vd \perp,$ we must have $p \in \bar{S}$ because otherwise we would have $\neg p \in \bar{S},$ which would be a contradiction.

Finally, we show that $\bar{S}$ has a model.
Define $v: L \to \{0, 1\}$ by

$$\begin{equation}
v(p) = \begin{cases}
1 & \text{ if } p \in \bar{S} \\ 
0 & \text{ otherwise. }
\end{cases}
\end{equation}$$

Since $\bar{S}$ is deductively closed, we only need to show that $v$ is indeed a {prf:ref}`valuation<lst:def-valuation>`.
By {prf:ref}`lst:def-valuation`, for $v$ to be a valuation it needs to satisfy a condition on $v(\perp)$ and a condition on $v(p \imp q).$
First, we have $v(\perp) = 0,$ since $\perp \not \in \bar{S}$ because $\bar{S}$ is consistent.
Second, we check $v(p \imp q)$ for each possible combination of values that $v$ can take on $p$ and $q.$

__Case 1:__
Suppose $v(p) = 0.$
Then by the definition of $v,$ we have $p \not \in \bar{S}$ and $\neg p \in \bar{S}.$
We want to show that $p \imp q \in \bar{S}.$

Now, note that to show $p \imp q \in \bar{S}$ it suffices to show $\neg p \vd p \imp q.$
This is because if $\neg p \vd p \imp q,$ then since $\bar{S} \vd \neg p,$ we have $\bar{S} \vd p \imp q.$
We can show this by noting that

1. $\vd \perp \imp (\neg q \imp \perp)$ by {prf:ref}`axiom 1<lst:def-proof-axioms-and-modus-ponens>`.
2. $\vd \perp \imp (\neg \neg q)$ by the {prf:ref}`definition of negation<lst:def-logical-symbols>`.
3. $\perp \vd \neg \neg q$ by the {prf:ref}`deduction theorem<lst:thm-deduction-theorem>`.
4. $\{p, \neg p\} \vd \neg \neg q.$
5. $\{p, \neg p\} \vd q$ by {prf:ref}`axiom 3<lst:def-proof-axioms-and-modus-ponens>`.
6. $\neg p \vd p \imp q$ by the {prf:ref}`deduction theorem<lst:thm-deduction-theorem>`.

We conclude that $\neg p \vd p \imp q,$ which implies $\bar{S} \vd p \imp q,$ so $p \imp q \in \bar{S}$ and $v(p \imp q) = 1$ as required.

__Case 2:__
Suppose $v(p) = 1, v(q) = 0.$
Then, $p \in \bar{S}, q \not \in \bar{S}.$
We want to show that $p \imp q \not \in \bar{S}.$
Suppose instead that $p \imp q \in \bar{S}.$
Then, $\bar{S} \perp p \imp q$ and since $p \in \bar{S},$ then by {prf:ref}`modus ponens<lst:def-proof-axioms-and-modus-ponens>` we have $\bar{S} \per q$ which means $q \in \bar{S},$ which is a contradiction.
Therefore $p \imp q \not \in \bar{S}$ and $v(p \imp q) = 0$ as required.

__Case 3:__
Suppose $v(p) = 1, v(q) = 1.$
Then, $p \in \bar{S}, q \in \bar{S}.$
We want to show that $p \imp q \in \bar{S}.$
By the axiom 1, we have $\perp q \imp (p \imp q),$ and by the deduction theorem we have $q \perp (p \imp q).$
Since $\bar{S} \perp q,$ we have  $\bar{S} \perp (p \imp q),$ and since $\bar{S}$ is deductively closed, we have $p \imp q \in \bar{S}.$
We conclude that $v(p \imp q) = 1$ as required.

This covers all possible cases for $v$ on $p$ and $q,$ so we conclude $v$ is a valuation on $L$ such that $v(s) = 1$ for all $s \in \bar{S},$ so $v$ is a model of $\bar{S},$ and also of $S.$
So $S$ has a model.
:::


:::{prf:theorem} Adequacy theorem
:label: lst:thm-adequacy-theorem
Let $S \subseteq L, t \in L.$
Then $S \models t$ implies $S \vd t.$
:::

:::{dropdown} Proof: Adequacy theorem
Let $S \subseteq L, t \in L.$
Suppose $S \models t.$
Then $S \cup \{\neg t\} \models \perp.$
By the model existence theorem, this means that $S \cup \{\neg t\} \vd \perp.$
By the deduction theorem, we have $S \vd \neg t \implies \perp.$
By the definition of negation we have $S \vd \neg \neg t,$ and by axiom 3 we have $S \vd t.$
:::


:::{prf:theorem} Completeness theorem
Let $S \subseteq L$ and $t \in L.$
Then $S \models t$ if and only if $S \vd t.$
:::

:::{dropdown} Proof: Completeness theorem
Suppose $S \subseteq L$ and $t \in L.$

__Implies:__
If $S \models t,$ then $S \vd t$ by {prf:ref}`lst:thm-adequacy-theorem`.

__Is implied by:__
If $S \vd t,$ then $S \models t$ by {prf:ref}`lst:thm-soundness-theorem`.
:::


:::{prf:theorem} Compactness theorem
:label: lst:thm-compactness-theorem
Let $S \subseteq L$ and $t \in L$ with $S \models t.$
Then, there is some finite $S' \subseteq S$ with $S' \models t.$
:::

:::{dropdown} Proof: Compactness theorem
Let $S \subseteq L$ and $t \in L$ with $S \models t.$
By the completeness theorem, $S \vd t.$
Since proofs are finite, there exists a finite subset of assumptions $S' \subseteq S$ which proves $t,$ so $S' \vd t.$
Applying the completeness theorem again, we have $S' \models t.$
:::

:::{prf:theorem} Decidability theorem
:label: lst:thm-decidability-theorem
Let $S \subseteq L$ be a finite set and $t \in L.$
Then, there exists an algorithm that determines, in finite and bounded time, whether or not $S \vd t.$
:::

:::{dropdown} Proof: Decidability theorem
Let $S \subseteq L$ be a finite set and $t \in L.$
By the completeness theorem, we have $S \vd t$ if and only if $S \models t.$
We can check $S \models t$ by making a truth table for $t.$
:::
