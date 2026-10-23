# Singular long-leg limits and a shared correction space

The [written, unreviewed proof](proof.md) excludes the canonical A4 to
M(10,10,11) degeneration whenever either scalar-balanced long map has
leading rank at least106. Both other maps, including the identity lift,
may have arbitrary finite poles. The remaining necessary bound is rank
at most105 on each balanced long map.

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

Exact finite controls, corruption checks, full local regression and archive
replay receipts will be recorded before this package is ready to merge.
