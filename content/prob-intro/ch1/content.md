# Events and Probabilities


## Sample and event spaces

Given an experiment $\mathcal{E}$, we denote the set of possible outcomes of $\mathcal{E}$ by $\Omega$ and we call this the **event space**. The members $\omega \in \Omega$ are called **elementary events**. For example, in an experiment where a die is tossed once, we could define the elementary events to be the outcome of the toss and $\Omega$ to be

$$ \Omega = \{1, 2, 3, 4, 5, 6\}$$

As their name suggests, elementary events represent experimental outcomes which are atomic, and are used to express the outcomes we are actually interested in. For example, we could ask whether the outcome of tossing the die is even, i.e. whether it is in the set $\{2, 4, 6\}$. In probability theory, experimental outcomes like this are naturally represented as sets of elementary events, that is in terms of subsets of $\Omega$: in addition to the sample space $\Omega$, we define **event spaces** which we use to represent the events that we are interested in. These event spaces are defined to have certain properties which enable reasoning about probabilities of unions, intersections and complements of events.


<div class='definition'>

**Definition (Event space)** The collection $\mathcal{F}$ of subsets of the sample space $\Omega$ is called an event space if

$$\begin{align}
&\mathcal{F} \text{ is non-empty}\\
&\text{if } A \in \mathcal{F} \text{ then } A^C = \Omega \setminus A \in \mathcal{F}\\
&\text{if } A_1, A_2, ... \in \mathcal{F} \text{ then } \bigcup^\infty_{i = 1} A_i \in \mathcal{F}
\end{align}$$

</div>

<br>

Note that an event space is always defined with respect to a sample space, and a sample space can have more than one event spaces defined on it. Three consequences of the above definition are that any event space $\mathcal{F}$:

1. Contains the empty set $\emptyset$ and the whole set $\Omega$. Since $\mathcal{F}$ is non-empty, it contains at least one set $A$, and by definition also $A^C$, as well as $A \cup A^C = \Omega$. Thus $\Omega \in \mathcal{F}$ and also $\emptyset = \Omega^C \in \mathcal{F}$.
2. Is closed under *finite* unions of its elements. We can write any finite union of the form $A_1 \cup A_2 ... A_n$ as a countably infinite union $B_1 \cup B_2 ...$, where $B_i = A_i$ for $i \leq n$ and $B_i = \emptyset$ otherwise, proving that $A_1 \cup A_2 ... A_n \in \mathcal{F}$.
3. Is closed under countable intersections of its subsets. We can write the intersection of $A, B \in \mathcal{F}$ as $A \cap B = \Omega \setminus (A \cap B)^C$ and since $(A \cap B)^C = A^C \cup B^C \in \mathcal{F}$, then $A \cap B \in \mathcal{F}$.

## Probability measures

We have defined the sample space $\Omega$ and the event space $\mathbb{F}$ of the experiment, but we are still missing the probabilities of the experimental outcomes. This is achieved by a mapping called the **probability measure** which assigns a probability to each event in $\mathcal{F}$.


<div class='definition'>

**Definition (Probability measure)** A mapping $\mathbb{P} : \mathcal{F} \to \mathbb{R}$ is called a **probability measure** on $(\Omega, \mathcal{F})$ if

1. $\mathbb{P}(A) \geq 0$ for $A \in \mathcal{F}$.
2. $\mathbb{P}(\Omega) = 1$.
3. it is **countably additive** in that if $A_1, A_2 ... \in \mathcal{F}$ are disjoint, then \\[\mathbb{P}\left(\sum^\infty_{n = 1}A_n\right) = \sum^\infty_{n = 1}\mathbb{P}\left(A_n\right).\\]

</div>

<br>

Using conditions (1) and (2) above we can also show that $\mathbb{P}(\emptyset) = 0$. From this and condition (3) we can also show that probability measures are also **finitely additive**.

## Probability spaces

Sample spaces, event spaces and probability measures can be combined into a probability space associated with our experiment.

<div class='definition'>

**Definition (Probability space)** A **probability space** is a triplet $(\Omega, \mathcal{F}, \mathbb{P})$ of objects such that

1. $\Omega$ is a non-empty set.
2. $\mathcal{F}$ is an event space on $\Omega$.
3. $\mathbb{P}$ is a probability measure on $(\Omega, \mathcal{F})$.

</div>

<br>

From the definitions of $\Omega$, $\mathcal{F}$ and $\mathbb{P}$ follow several basic facts:

1. If $A, B \in \mathcal{F}$, then $A \setminus B \in \mathcal{F}$.
2. If $A_1, A_2, ... \in \mathcal{F}$, then $\cap^\infty_{n = 1}A_n \in \mathcal{F}$.
3. If $A \in \mathcal{F}$ then $\mathbb{P}(A) + \mathbb{P}(A^C) = 1$.
4. If $A, B \in \mathcal{F}$ then $\mathbb{P}(A \cup B) + \mathbb{P}(A \cap B) = \mathbb{P}(A) + \mathbb{P}(B)$.
5. If $A, B \in \mathcal{F}$ and $A \subseteq B$ then $\mathbb{P}(A) \leq \mathbb{P}(B)$.

## Conditional probability, independence and Bayes' rule

Often we may have partial information about the outcome of an experiment, and want to adjust our beliefs about the outcome based on these beliefs. We are therefore interested in the probability of some event $A$ occuring, given that another event $B$ occurs. This updated probability is called a conditional probability.


<div class='definition'>

**Definition (Conditional probabiility)** Given $A, B \in \mathcal{F}$ and $\mathbb{P}(B) > 0$, the **conditional probability** of $A$ given $B$, $\mathbb{P}(A | B)$, is defined as

$$\mathbb{P}(A | B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}.$$

</div>

<br>

The condition $\mathbb{P}(B) > 0$ is in place to ensure that the division is defined, or equivalently that $\mathbb{P}(A | B)$ is a sensible quantity: if $\mathbb{P}(B)= 0$ then $B$ would never occur so the statement $A | B$ is senseless. The definition of the conditional probability is often referred to as the **product rule**, while the finite additivity of $\mathbb{P}$ defined earlier, is often referred to as the **sum rule**.

In some cases, information coming from one event might not give us any information about another event, in the sense that the probability of $A | B$ is equal to the probability of $A$, in which case we say $A$ and $B$ are **conditionally independent**.

<div class='definition'>

**Definition (Independence)** Events $A, B \in \mathcal{F}$ are called **independent** if

$$ \mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B)$$

</div>

<br>

This definition of independence is slightly more general than the statement "$A, B$ are independent $\iff$ $\mathbb{P}(A | B) = \mathbb{P}(A)$" in the sense that it allows for $\mathbb{P}(B) = 0$. Conditional probabilities define valid probability spaces too, in the sense of the following result.


<div class='theorem'>

**Theorem (Conditional probability space)** If $(\Omega, \mathcal{F}, \mathbb{P})$ iis a probability space and $B \in \mathcal{F}$ with $\mathbb{P} > 0$, then $(\Omega, \mathcal{F}, \mathbb{Q})$ where $\mathbb{Q} : \mathcal{F} \to \mathbb{R}$ and $\mathbb{Q}(A) = \mathbb{P}(A | B)$ is also a probability space.

</div>

<br>

This can be be proved by showing that $\mathbb{Q}$ satisfies the three conditions of probability measures.

## The partition theorem and Bayes' rule

Often, calculating probabilities of interest is made easier by applying the partition theorem shown below. This follows from the definition of conditional probability and the additivity of probability measures.


<div class='theorem'>

**Theorem (Partition theorem)** If $B_1, B_2, ...$ is a partition of $\Omega$, in the sense that the $B_n$ are all disjoint and their union is $\Omega$, then

$$\mathbb{P}(A) = \sum_n \mathbb{P}(A | B_n)\mathbb{P}(B_n).$$

</div>

<br>

The partition theorem is closely related to Bayes' rule, which takes a central role in probabilistic inference.

## Continuity
