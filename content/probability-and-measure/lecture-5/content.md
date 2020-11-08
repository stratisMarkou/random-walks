# Non-measurablity and probability axioms

In this page we discuss non-measurable sets and introduce the axioms of probability. We bring an example subset of $\mathcal{P}((0, 1])$ that is not Lebesgue-measurable, because it is not contained in $\mathcal{B}$. We then introduce the axioms of probability, which are really just the properties of measure functions.

## Remarks on the Lebesgue measure

We present the following three remarks that we will refer to subsequently. The first introduces null sets, which are sets whose measure is zero. Any countable subset of $\mathbb{R}$ is a null set.

<div class="observation">

**Remark (Null sets)** A set $A \in \mathcal{A}$ is called a Lebesgue null set if $\mu(A) = 0$. Since
    
$$\{x\} = \bigcup_n (x - \frac{1}{n}, x]$$
    
and $\mu$ is a measure, we have

$$\mu(\{x\}) = \lim_{n \to \infty} \mu\left((x - \frac{1}{n}, x]\right) = 0.$$
    
By extension, for any countatble subset of $\mathbb{R}$, e.g. $\mathbb{Q}$ we have
    
$$\begin{align}
\mu(\mathbb{Q}) = \mu \left(\bigcup_{q \in \mathbb{Q}} \{q\}\right) = \sum_{q \in \mathbb{Q}} \mu(\{q\}) = 0.
\end{align}$$
    
</div>
<br>

Related to null sets, it can be shown that the class of (outer) Lebesgue measurable sets $\mathcal{M}$ on $\mathcal{B}$ (defined in the proof of Caratheodory's extension theorem), contains $\mathcal{B}$. In fact, $\mathcal{M}$ is the set of all unions of elements of $\mathcal{B}$ and of null sets of $\mathcal{B}$, as stated below.

<div class="observation">

**Remark (Outer Lebesgue measurable sets)** The measure $\mu$ is defined on $\mathcal{B}$ but in fact also on the class $\mathcal{M}$ of (outer) Lebesgue measurable sets. It can be shown that
    
$$ \mathcal{M} = \{A \cup N : A \in \mathcal{B}, N \subseteq B \text{ for some } B \in \mathcal{B} \text{ s.t. } \mu (B) = 0\}.$$
    
So $\mathcal{M}$ contains any subset of a Borell null set.
    
</div>
<br>


Lastly and unsurprisingly, the Lebesgue measure is invariant to translating the set being measured by some finite amount since

$$\mu((a + x, b + x]) = (b + x) - (a + x) = b - a = \mu((a, b]).$$

<div class="observation">

**Remark (Translation invariance)** Defining the translation by $x$ of $B \in \mathcal{B}$ as
    
$$ B + x = \{ b + x : b \in B \}, $$
    
then the Lebesgue measure of the translated set is equal to the measure of the original
    
$$\mu(B + x) = \mu(B).$$
    
We say that the Lebesgue measure is translation invariant.
    
</div>
<br>


## Non-measurable sets

We now ask whether $\mathcal{B}$ is a strict subset of $\mathcal{P}(\mathbb{R})$ or not. Equivalently we may ask whether $\mathcal{B}((0, 1])$ is a strict subset of $\mathcal{P}((0, 1])$. The answer is affirmative, since there exist sets in $\mathcal{P}((0, 1])$ which are not measurable and therefore cannot be in $\mathcal{B}((0, 1])$.

For $x, y \in (0, 1]$, let us write $x \sim y$ if $y - x \in \mathbb{Q}$, where "$-$" is modulo $1$ and we understand $\mathbb{Q}$ to be the intersection $\mathbb{Q} \cap (0, 1]$. Now using the axiom of choice we select exactly one element from each equivalence class $[x] = \{y \in [0, 1] \text{ s.t. } x \sim y\}$, and let $S \subseteq (0, 1]$ denote the resulting set. Define also the translation

$$S + q = \{S + q \text{ mod } 1, s \in S\},$$

from which it follows that $(0, 1]$ is equal to the disjoint union $\bigcup_{q \in \mathbb{Q}} (S + q)$. Suppose that the set $S$ is measurable. Then by the translation invariance of $\mu$, we have $\mu (S) = \mu (S + q)$ and hence

$$ 1 = \mu((0, 1]) = \mu\left( \bigcup_{q \in \mathbb{Q}} (S + q) \right) = \sum_{q \in \mathbb{Q}} \mu (S). $$

But $\mu(S)$ can be either zero or a finite positive constant, so the sum above will be either equal to $0$ or $\infty$, reaching a contradiction. Therefore the set $S$ cannot be measurable. We may then ask, is there any way to extend $\mu$ to $\mathcal{P}((0, 1])$? The answer is negative, as stated by the following theorem.

<div class="theorem">

**Theorem (Banach-Kuretowski)** Assuming the [continuum hypothesis](https://mathworld.wolfram.com/ContinuumHypothesis.html), there exists no measure $\mu$ on $\mathcal{P}((0, 1])$ such that $\mu((0, 1])$ and $\mu(\{x\}) = 0$ for all $x \in (0, 1]$.
    
</div>
<br>

We do not prove this theorem here. This theorem motivates the effort we put into defining and working with measurable sets instead of the power-set $\mathcal{P}(\cdot)$. It also gives a definitive (negative) answer to whether we can extend the notion of volume to arbitrary $\sigma$-algebras.

## Axioms of probability

We now introduce probability measures and spaces. These are simply measure spaces with the additional requirement $\mu(E) = 1$.

<div class="definition">

**Definition (Probability measures and spaces)** Let $\mu$ be a measure on $(E, \mathcal{E})$. If $\mu(E) = 1$, then $\mu$ is called a probability measure and $(E, \mathcal{E}, \mu)$ is called a probability space. In probability we often write probability spaces as $(\Omega, \mathcal{A}, \mathbb{P})$, where $\Omega$ is called the outcome space, $\mathcal{A}$ is called the event space and $\mathbb{P}$ is called the probability measure.
    
</div>
<br>

We are now at a position to introduce the axioms of probability. Although we refer to them as axioms, these are an immediate consequence of the definition of the above definition.

<div class="lemma">

**Corrolary (The axioms of probability)** By the definition of probability measures and spaces, we have
    
1. $\mathbb{P}(\emptyset) = 0$ and $\mathbb{P}(\Omega) = 1$.
2. Probabilities are positive, $\mathbb{P}(A) \geq 0$ for all $A \in \mathcal{A}$.
3. The probability of countable unions of disjoint events is the sum of the probabilities of the events:  \begin{align} \mathbb{P}\left(\bigcup_{n \in \mathbb{N}} A_n\right) = \sum_{n \in \mathbb{N}}\mathbb{P}\left(A_n\right) \end{align} for all disjoint $A_n \in \mathcal{A}$.
    
</div>
<br>

## Independence

Lastly, we introduce independent events. Independence is a key property of study in probability theory. Note that the independence of a potentially infinite number of events is defined in terms of *finite* sub-families of events.

<div class="definition">

**Definition (Independent events)** We call the events $(A_i : i \in I)$ independent if for all finite $J \subseteq I$ index sets we have
    
$$ \mathbb{P}\left(\bigcap_{j \in J} A_j \right) = \prod_{j \in J} \mathbb{P}(A_j).$$
    
</div>
<br>

Similarly, we can also have independent $\sigma$-algebras, as defined below.

<div class="definition">

**Definition (Independent $\sigma$-algebras)** Sub-$\sigma$-algebras $\mathcal{A}_i \subseteq \mathcal{F}$ are said to be independent if for all finite $J \subseteq I$, the events $A_j \in \mathcal{A}_j$ are independent.
    
</div>
<br>

The following theorem facilitates the study of independent events on $\pi$-systems rather than $\sigma$-algebras. If two $\pi$-systems are such that their events of one are independent to the events of the other, then the $\sigma$-algebras generated by them are indepentent.

<div class="theorem">

**Theorem (Independent $\sigma$-algebras)** Let $A_1, A_2$ be $\pi$-systems of elements in $\mathcal{F}$. Suppose that
    
$$ \mathbb{P}(A_1 \cap A_2) = \mathbb{P}(A_1)\mathbb{P}(A_2), \text{ for all } A_1 \in \mathcal{A}_1, A_2 \in \mathcal{A}_2.$$

Then $\sigma(\mathcal{A}_1)$ and $\sigma(\mathcal{A}_2)$ are independent.
    
</div>
<br>

This theorem is proved in the next section.