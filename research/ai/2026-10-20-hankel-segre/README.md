# Higher Hankel secants and cyclic-source restrictions

## Question and result

Can an ordinary restriction of the cyclic convolution source `A(5,6)`
produce `M16` direct sum `M4`, the first unresolved square-sum target in
the earlier necessary-condition screen?

The written proof in `hankel_segre_obstruction.md` answers **no** for
ordinary restrictions. It uses higher secants of the rational normal
curve, with nonreduced supporting divisors included. If
`r<min(a,b)` and `a+b-2>=3r-1`, then a square block of size `n` in a
target of common leg dimension `D` must satisfy

\[
n^2>rab\quad\Longrightarrow\quad
n+2\bigl(ab(a+b-1)-D\bigr)\ge(r+1)ab.
\]

The new statement is an AI-derived written proof. A separate research
agent checked its geometric steps and suggested an exposition fix about
extending a polynomial identity to a function field. This is not external
peer review or formal verification. Its imported source-slice bound and
Hankel/secant identification are cited precisely in the proof.

## Finite frontier

The exact screen covers every square direct-sum partition for all 52
source formats `2<=a<=b` with `N=ab(a+b-1)<=800`. All 51 formats with
`N<784` fail the strict score needed by this finite-target route at
`omega=9/4`. The first source passing the necessary conditions is
`A(7,8)`, `N=784`; its maximizing relaxed partition is
`[25,5,2,1,1]`, with `D=656`. That is a score-surviving partition, not a
constructed restriction.

In particular, `A(5,6)->M16+M4` fails at ranks `r=2` and `r=3`, and
`A(5,6)->M16` alone fails at `r=3`. The old conditional exponent
calculation for the former target remains a valid arithmetic implication
if a singular degeneration is eventually found.

The existing scalar and three-leg rank-one tests are retained unchanged.
The source definition, those tests, and the finite-target score are from
the constructive-spectrum branch, pinned at
[`e44aaff22af7863e0a1f5db66d187ae997c82184`](https://github.com/1337isnot1337/matrix-mult-bounds/tree/e44aaff22af7863e0a1f5db66d187ae997c82184/research/ai/2026-10-20-anisotropic-constructions).
`higher_hankel_frontier.py` adapts that branch's
`square_sum_frontier.py`; it uses integer fourth-root enclosures and an
exact integer knapsack over all partition dimensions.

## Reproduction

Run from the repository root, using the standard library only:

```sh
python research/ai/2026-10-20-hankel-segre/hankel_segre_controls.py --output results/local/hankel_segre_controls.json
python research/ai/2026-10-20-hankel-segre/higher_hankel_frontier.py --maximum-source-dimension 800 --output results/local/higher_hankel_frontier_800.json
python -m unittest discover -s tests -p test_hankel_segre.py -v
```

The committed reports are under `results/2026-10-20-hankel-segre/`.
The finite controls cover 1,225 divisor-span intersections, 470 support
union examples, and four coherent source slices, including repeated
points and infinity, over the prime field with 101 elements. These
checks support the indexing and examples; they do not prove the
universal geometry.

## Limits and active target

The proof uses actual ordinary linear maps. It does not exclude a
singular degeneration, where source lifts can lose rank only in the
limit. No smaller exponent follows from this package.

The missing construction `A(5,6)` degenerating to `M16+M4` remains an
active way to obtain a strict improvement if a complete degeneration is
found. The new obstruction shows why a search restricted to ordinary
maps cannot succeed at that target.

## Subsequent main-branch continuation

The later [first-boundary theorem](../2026-10-20-anisotropic-constructions/hankel_boundary_dimension.md)
and [updated square-sum frontier](../2026-10-20-anisotropic-constructions/square_sum_frontier.md)
exclude the ordinary A(7,8) target that survived the relaxed screen here.
The saved 52-format experiment and its exact data are preserved as their
original finite scope; they no longer identify the current first survivor.
The later main note records that larger frontier. Neither result excludes
unrestricted singular degeneration or improves the exponent.
