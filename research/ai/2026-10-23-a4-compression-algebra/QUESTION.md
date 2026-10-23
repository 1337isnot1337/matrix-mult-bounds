# Can any constant A4 compression lose nine directions?

## Resolution

The [completed proof](proof.md), claim
`AI-A4-ARBITRARY-COMPRESSION-001`, gives image dimension at least 38
for every complex rank-26 pair. It retains arbitrary subspaces inside
the torus weight spaces and has exact acceptance for all 2,809 graded
budget pairs. The prior reduction therefore excludes all constant
rank-110 compressions of the specified full conjugation family.

The next constructive question requires moving long-map compressions
or a different singular path. Any candidate must supply complete
re-saturation and every matrix-target coefficient identity. The theorem
is written and unreviewed; it does not construct a target or improve
the exponent. The original question below records the starting point.

## Original question

October 23, 2026. Owner-directed research continuation on
`research/a4-compression-algebra-20261023-ab94`, based on local `5bce59f`.

The preceding complete low-rank reduction leaves an explicit question
over the complex numbers. Let G be the normalized 16-dimensional outer
source space, F=G00, and

    E = G + [G,F] + FGF,    dim(E) = 46,    E subset Mat28.

Prove that every pair of rank-26 maps P: C^28 -> C^26 and
C: C^26 -> C^28 satisfies dim(P E C)>=38, or produce an exact pair
with dimension at most37. Equivalently, for every 26-dimensional U and
two-dimensional W, prove

    dim {X in E : X(U) subset W} <= 8,

or certify a counterexample. The question quantifies over arbitrary
complex subspaces, not just coordinate deletions or sampled flags.

The algebraic route will examine the rank-at-most-four locus of E, the
filtration determined by F, explicit low-rank minors, and a possible
polynomial-module description. A positive candidate must include exact
full-rank compression maps and the full projected coefficient span. A
negative result must account for every complex U and W.

A universal bound of38 would close arbitrary constant compressions in
the one specified two-sided conjugation family. A counterexample would
only pass its necessary compression test; complete re-saturation and
all matrix-target coefficient identities would still be required.

The preceding full-space reduction, source formulas, source unit and
minimum-rank-six theorem retain their existing attribution in
[LOW_RANK_REDUCTION.md](../2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md)
and [its sources](../2026-10-23-conjugation-limit/sources.json).
No new theorem, full target or exponent improvement is asserted by this
question checkpoint.
