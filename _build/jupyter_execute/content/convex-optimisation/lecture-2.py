# Fundamental definitions

## Affine sets

**Line:** through points $x_1$ and $x_2$ is the set

$$x = \theta x_1 + (1 - \theta) x_2, \text{ where } \theta \in \mathbb{R}.$$

**Affine set:** an affine set is a set which contains the line defined by any two of its points.

## Convex sets

**Line segment:** the line segment between two points $x_1$ and $x_2$ is the set of points

$$x = \theta x_1 + (1 - \theta) x_2, \text{ where } \theta \in [0, 1].$$

**Convex set:** a convex set contains the line segments between any two of its points. Affine sets are convex.

## Convex combinations and convex hulls

**Convex combination:** a linear combination of points $x_1, x_2, ..., x_n$ of the form

$$x = \theta_1 x_1 + \theta_2 x_2 + ... + \theta_n x_n,$$

is a convex combination if $\theta_k \geq 0$ for all $k$ and $\sum_k \theta_k = 1$.

**Convex hull:** of a set $S$, $\textbf{conv}S$, is the set of all convex combinations of $S$. It is the smallest convex set that contains $S$, as any convex superset of $S$ must contain all convex combinations of elements in $S$ and by extension $\textbf{conv}S$ as well.

## Cones and convex cones

**Cone:** a set which contains all non-negative multiples of its points

$$x \in C, \theta \geq 0 \implies \theta x \in C.$$

Cones are not necessarily convex: the set $\mathbb{R}_{+} \cup \mathbb{R}_{-}$ is a cone but is not convex.

**Conic combination:** a linear combination of points $x_1$ and $x_2$

$$x = \theta_1 x_1 + \theta_2 x_2$$

is a conic combination if $\theta_1, \theta_2 \geq 0$.

**Convex cone:** a set which contains all conic combinations of its points. Since the set of conic combinations of a set subsumes the set of convex combinations, such a set is convex as well as a cone.

**Conic hull:** of a set $C$ is the smallest set which contains all conic combinations of $C$. A conic hull is the smallest convex cone that contains $C$, by the same argument applied to convex hulls and convex sets.

## Hyperplanes and halfspaces

**Hyperplane:** a set of points of the form

$$\{x | a^\top x = b\}, a \neq 0.$$

**Halfspace:** a set of points of the form

$$\{x | a^\top x \leq b\}, a \neq 0.$$

Hyperplanes are affine and convex. Halfspaces are convex but they are not affine.

## Euclidian balls and ellipsoids

**(Euclidean) ball:** with center $x_c$ and radius $r$

$$B(x_c, r) = \{x~|~||x - x_c||_2 \leq r \} = \{x_c + ru~|~||u||_2 \leq 1 \}.$$

**Ellipsoid:** a set of the form

$$E(x_c, P) = \{x~|~(x - x_c)^\top P (x - x_c) \leq 1\} = \{x_c + Au~|~||u||_2 \leq 1 \},$$

where $P$ is a symmetric positive-definite and $A$ is non-singular.

Euclidean balls and ellipsoids are convex sets.

## Norm balls and norm cones

**Norm:** a norm is a function $||\cdot||$ that satisfies

1. $||x|| \geq 0$
2. $||cx|| = |c|~||x||$
3. $||x + y|| \leq ||x|| + ||y||$

**Norm ball:** a norm ball with center $x_c$ and radius $r$ is the set $\{x~|~||x - x_c|| \leq r\}.$

**Norm cone:** the set $\{(x, t) ~|~ ||x|| \leq t\}.$

Norm balls and norm cones are convex sets.

## Polyhedra

**Polyhedron:** the set of finitely many linear inequalities and equalities

$$Ax \preccurlyeq b, \text{ and } Cx = d,$$

where $\preccurlyeq$ is the component-wise inequality. Polyhedra are convex and can be expressed as an intersection of finitely many halfspaces (inequalities) and hyperplances (equalities).

## Positive-semidefinite cone

The set of all positive-semidefinite matrices $\mathbf{S}_+^n = \{X~|~ z^\top Xz \geq 0~\forall~z \in \mathbb{R}^n\}$ is a convex cone:

\begin{align}
X, Y \in \mathbf{S}_+^n \implies \theta_1 X + \theta_2 Y \in \mathbf{S}_+^n, \text{ if } \theta_1, \theta_2 \geq 0.
\end{align}

Similarly, the set of all positive-definite matrices $\mathbf{S}_{++}^n = \{X~|~ z^\top Xz > 0\}$ is also a convex cone:

\begin{align}
X, Y \in \mathbf{S}_{++}^n \implies \theta_1 X + \theta_2 Y \in \mathbf{S}_{++}^n, \text{ if } \theta_1, \theta_2 > 0.
\end{align}

The difference between these sets is that $\mathbf{S}_+^n$ is closed, whereas $\mathbf{S}_{++}^n$ is open. Both of these are examples of convex sets.

## Operations that preserve convexity

**Intersection:** The intersection of any number of convex sets is convex.

To show this, suppose $S_1, S_2, ...$ is a (finite or infinite) sequence of convex sets whose intersection is $S$ and $x, y \in S$, then $x, y$ are inside every $S_n$ and so is the line segment between them (by convexity of $S_n$). This implies the line segment is itself in $S$, showing $S$ is convex.

**Affine function:** An affine mapping, $f(x) = Ax + b$, of a convex set is also convex. Convexity is also preserved under inverses of affine maps, where the inverse map is defined as $f^{-1}(S)\{x~|~f(x) \in S\}$.

To show the first statement, let $S_1$ be a convex set, $S_2 = f(S_1)$ and $x, y \in S_1$. Then the line segment $\theta x + (1 - \theta) y, \theta \in [0, 1]$ is in $S_1$ and

\begin{align}
f\big(\theta x + (1 - \theta) y\big) = \theta Ax + (1 - \theta) Ay + b = \theta f(x) + (1 - \theta) f(y)~\in~f(S_2) 
\end{align}

so $S_2$ is convex. To show the second statement, let $S_2$ be a convex set, $S_1 = f^{-1}(S_2)$ and $x, y \in S_2$. Then $f^{-1}(x), f^{-1}(y) \subset S_1$, and we want to show that if $x^* \in f^{-1}(x), y^* \in f^{-1}(y)$, then the line segment $\theta x^* + (1 - \theta)y^*$ is also in $S_1$. By the convexity of $S_2$, the line segment $\theta x + (1 - \theta) y$ is in $S_2$, so:

\begin{align}
f\Big(\big\{\theta x^* + (1 - \theta)y^* | x^* \in f^{-1}(x), y^* \in f^{-1}(y)\big\}\Big) = \theta x + (1 - \theta) y \in S_2
\end{align}

and since the left hand side is in $S_2$, the argument of $f$ on the left hand side must be a subset of $S_1$ (by the definition of $f^{-1}$), showing that $S_1$ is convex.

**Perspective function:** A perspective function $f : \{x~|~ x \in \mathbb{R}^{n} \text{ and } x_n > 0\} \to \mathbb{R}^{n - 1}$ is the mapping

$$f(x) = \left(\frac{x_1}{x_{n}}, \frac{x_2}{x_{n}}, ..., \frac{x_{n-1}}{x_{n}} \right),$$

and it is a convex function. The perspective function can be interpreted as a projection of a point in $\mathbb{R}^{n}$ to the image plane of a pinhole camera. It is also closely related to homogeneous coordinates, used in graphics and computer vision - for further reading see Roberto Cipolla's [notes on Computer Vision](http://mi.eng.cam.ac.uk/~cipolla/lectures/4F12/Slides/2019-4F12-notes-3.pdf).

**Linear-fractional function:** A perspective function $f : \mathbb{R}^{n} \to \mathbb{R}^m$ is a mapping of the form

$$f(x) = \left(\frac{x_1}{x_{n}}, \frac{x_2}{x_{n}}, ..., \frac{x_{n-1}}{x_{n}} \right),$$

and is also a convex function. It is a generalisation of the perspective funtion, and equal to it if $c^\top = [0, 0, ..., 1]$ and $d = 0$.


## Proper cones, generalised inequalities, minimum and minimal elements

**Proper cone:** A convex cone is a proper cone if it is

1. Closed (contains its boundary),
2. Solid (it has non-zero interior) and
3. Pointed (does not contain a line).

Proper cones are used to define another useful concept, the generalised inequality.

**Generalised inequality:** The generalised inequalities $\preccurlyeq_K$ and $\prec_K$ with respect to a proper cone $K$ are defined as

\begin{align}
x \preccurlyeq_K y &\implies y - x \in K \\
x \prec_K y &\implies y - x \in \textbf{ int}(K).
\end{align}

In general however, we might have both $x \not \preccurlyeq_K y$ and $x \not \succcurlyeq_K y$ simultaneously, if $x$ and $y$ are not comparable under the inequality. For example, comparing the points $x = (1, 0)$ and $y = (-1, 1)$ using the inequality $\preccurlyeq_{\mathbb{R}^2_{+}}$ (where $\mathbb{R}^2_{+}$ is the positive quadrant of $\mathbb{R}^2$), we see that neither $x \preccurlyeq_{\mathbb{R}^2_{+}} y$ nor $x \succcurlyeq_{\mathbb{R}^2_{+}} y$ hold, because neither $y - x$ nor $x - y$ are in $\mathbb{R}^2_{+}$. This inequality is therefore a *partial ordering*, and we need to distinguish between different kinds of "minimum" points.

**Minimum element:** The minimum element $x$ of $S$ satisfies

$$y \in S \implies x \preccurlyeq_K y.$$

So *if $y \in S$ then $y$ is no greater than $x$*. Thus $x$ can be compared to all other points $y \in S$ and inequality can be unambiguously decided.

**Minimal element:** A minimal element $x$ of $S$ satisfies

$$y \in S, y \preccurlyeq_K x \implies x = y.$$

This means that if there is another element $y$ in $S$ such that it can be compared to $x$ and is in fact smaller than or equal to $x$, then $x = y$. The reason we define minimal elements in addition to minimum elements, is to deal with cases where not all points can be compared to each other, like the $\mathbb{R}^2_{+}$ example above. In such cases, there may not be a minimum point but there will be minimal points.

## Separating hyperplane theorem

If $C$ and $D$ are disjoint convex sets, then there exist $a \neq 0$ and $b$ such that

\begin{align}
&a^\top x \leq b \text{ for } x \in C \\
\text{ and } &a^\top x \geq b \text{ for } x \in D.
\end{align}

In other words, the plane separates the two sets. Strict inequality would require further restrictions: consider the case where $C$ is an open (does not contain its boundary) convex set and $D$ is a point on the boundary of $C$; strict equality $a^\top x > b \text{ for } x \in D$ would not hold.

## Supporting hyperplane theorem

**Supporting hyperplane:** A supporting hyperplane to $C$, at an $x_0$ on the boundary of $C$, is the set: $$\{x | a^\top x = a^\top x_0\},$$ where $a \neq 0$ and $a^\top x \leq a^\top x_0$ for $x \in C$.

**Supporting hyperplane theorem:** If $C$ is a convex set, then there exists a supporting hyperplane to $C$ at every one of its boundary points.

The supporting hyperplane theorem can be proved by using the separating hyperplane theorem. If $x_0$ is a boundary point of $C$ we can define $D = \{x_0\}$, and apply the separating hyperplane theorem to show that a separating hyperplane exists, which is also supporting because $x_0$ is on the boundary of $C$.

## Dual cones and dual generalised inequalities

**Dual cone:** the dual cone of a cone $K$ is defined as

$$K^* = \{z~|~ z^\top x \geq 0 \text{ for all } x \in K\},$$

and satisfies the useful properties:

- $K^*$ is closed and convex.
- If $K_1 \subseteq K_2$ then $K_2^* \subseteq K_1^*$.
- If $K$ has nonempty interior, then $K^*$ is pointed.
- If the closure of $K$ is pointed then $K^*$ has non-empty interior.
- $K^{**}$ is the closure of the convex hull of $K$. If $K$ is closed and convex to begin with, then $K = K^{**}$.

**Dual generalised inequalities:** The dual cones of proper cones are proper, and can also be used to define generalised inequalities

\begin{align}
x \preccurlyeq_{K^*} y &\implies y - x \in K^* \\
x \prec_{K^*} y &\implies y - x \in \textbf{ int}(K^*).
\end{align}

Two important properties that relate generalised inequalities and their duals are:

- $x \preccurlyeq_K y \iff \lambda^\top x \leq \lambda^\top y$ for all $\lambda \succcurlyeq_{K*} 0$,
- $x \prec_K y \iff \lambda^\top x < \lambda^\top y$ for all $\lambda \succcurlyeq_{K*} 0, \lambda \neq 0$,

and since $K = K^{**}$ for proper cones, the above properties also hold if $K^*$ and $K^{**}$ are swapped.

## Minimum and minimal elements via dual inequalities

We have the following conditions on minimum and minimal elements based on dual inequalities.

**Minimum element:** An element $x \in S$ is the minimum element of $S$ if and only if $x$ is the unique minimiser of $\lambda^\top z, z \in S$ for all $\lambda \succ_{K^*} 0$.

**Minimal element:** An element $x \in S$ is a minimal element of $S$ if $x$ minimises $\lambda^\top z, z \in S$ for some $\lambda \succcurlyeq_{K^*} 0$.

The converse of the above statement is generally not true. If $x$ is a minimal point, it is not true in general that there exists $\lambda \succ_{K^*} 0$, such that $x$ minimises $\lambda^\top z, z \in S$. However, if $S$ is convex, then a necessary and sufficient condition exists.

**Minimal element of a convex set:** An element $x$ of a convex set $S$, is minimal if and only if there exists $\lambda \succcurlyeq_{K^*} 0$ such that $x$ minimises $\lambda^\top z, z \in S$.

For the statements on minimal elements, the strict inequality $\lambda \succ_{K^*} 0$ plays an important role. If $\lambda \succcurlyeq_{K^*} 0$ was used in the statements, counter-examples can be easily found.

