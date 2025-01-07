# Exercises

<script async defer src="https://buttons.github.io/buttons.js"></script>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" aria-label="Star stratisMarkou/random-walks on GitHub">Star</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/issues" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-issue-opened" data-size="large" aria-label="Issue stratisMarkou/random-walks on GitHub">Issue</a>
<a class="github-button" href="https://github.com/stratisMarkou/random-walks/subscription" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-eye" data-size="large" aria-label="Watch stratisMarkou/random-walks on GitHub">Watch</a>
<a class="github-button" href="https://github.com/stratisMarkou" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Follow @stratisMarkou on GitHub">Follow</a>

::::{note} Exercise 1.1
Show that the sequence $2015, 20015, 200015, 2000015, \ldots$ converges in the 2-adic metric on $\mathbb{Z}$.

:::{dropdown} Solution
We show that the sequence converges to $15$ in the 2-adic metric.
Let $a_n$ be the $n$th term of the sequence.
Then $a_n - 15 = 2 \times 10^{n + 3}.$
Note that $2 \times 10^{n + 3}$ is divisible by $2^{n + 4}.$
Therefore, $|a_n - 15|_2 = 2^{-(n + 4)} \to 0$ as $n \to \infty.$
:::
::::