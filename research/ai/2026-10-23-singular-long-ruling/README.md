# Singular long-leg limits and a shared correction space

The [written, unreviewed proof](proof.md) excludes the canonical A4 to
M(10,10,11) degeneration whenever either scalar-balanced long map has
leading rank at least106. Both other maps, including the identity lift,
may have arbitrary finite poles. The remaining necessary bound is rank
at most105 on each balanced long map.

The [rank20 continuation](../2026-10-23-rank20-ruling/proof.md) strengthens
the long-map threshold to105 and the remaining necessary bound to104.
Its [all-size version](../2026-10-23-rank20-ruling/all_sizes.md) supplies
the corresponding first-gap source classification at every square size.
The present proof's older minimum-cone boundary is retained with its
original scope and controls.

This continues concurrent PR113's full-rank-long-map exclusion. The
regular right-inverse projector leaves a single shared correction column
space of dimension at most two. The prior source gap places each leading
rank-one target ruling in the minimum source cone. An injective target
ruling has dimension ten, while linear spaces in that cone have dimension
at most four. Applying the quotient by the shared correction space forces
the leading first map to vanish, contradicting scalar balancing.

The source, gap and minimum-locus results retain their existing credit.
The gap imports Grothendieck's 1957 splitting theorem over P^1(C), with
the original source and its exact use recorded in [sources.json](sources.json).
See [the registered question](QUESTION.md) for the question's scope.

No independent mathematical review, formalization, arbitrary degeneration
exclusion, constructed matrix target or exponent improvement is claimed.
At limiting rank105, the proof's source cap reaches20; an actual rank20
slice makes the adopted minimum-cone argument insufficient. A sharper
rank-at-most20 linear-space classification is not assumed.

Reproduce the exact controls and focused regressions from the repository
root with its maintained dependencies installed:

```sh
python research/ai/2026-10-23-singular-long-ruling/verify.py
python -m unittest discover -s tests -p test_singular_long_ruling.py -v
```

The frozen report at `results/singular-long-ruling-2026-10-23/controls.json`
contains nine shared-correction families (including a zero-rank unit image),
twelve injective target rulings, six actual rank16 source slices, an actual
rank20 boundary slice, and seven long-limit rank cases. A negative control
has two individual rank-one corrections spanning two column dimensions;
individual rank bounds alone cannot replace the shared-space argument.
Mutation checks reject false common ranks, an unsupported c105 exclusion
by this older minimum-cone argument, changed source pins, removed splitting
attribution and inflated review status.

Run `verify.py --write` only to regenerate controls, followed by replay
without that flag. The [combined validation receipt](../../../results/rank20-ruling-2026-10-23/validation.json)
records the full hosted regression at610f2a9 on Python3.10 and3.14,
all five archive replays and34 focused integration tests at e57e144.
PR142 includes this complete package for combined integration. Earlier
local full runs were interrupted by a reboot and are not counted as
passing; final-head hosted CI remains required. Finite controls do not
formalize the proof's all-order quantifiers or establish independent review.
