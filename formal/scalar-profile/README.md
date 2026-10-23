# Finite scalar-profile slope lemma

This Lean project formalizes the finite estimate used to replace the limiting
slope step in Section 2.2 of the initial scalar-profile note. For a discrete
concave row `f` satisfying the tripling inequality at `b`, it proves

```text
2 * f b <= (2*b + a - 1) * (f (b+1) - f b).
```

Here `a,b ≥ 1`, and discrete concavity means the increments
`f (n+1) - f n` are nonincreasing for `n ≥ 1`. With `N = 2*b+a-1`, we have
`b+N = 3*b+a-1`. Concavity bounds the finite sum of the `N` increments from
`b` to `b+N` by `N` times the first increment; tripling bounds the same net
increase below by `2*f b`. The argument does not take a limit. This project
formalizes that cross-multiplied slope estimate only; it does not formalize the
full scalar profile theorem or any tensor consequence.

With Lean 4.31.0 and Mathlib 4.31.0 installed, run:

```sh
lake exe cache get
lake build
```
