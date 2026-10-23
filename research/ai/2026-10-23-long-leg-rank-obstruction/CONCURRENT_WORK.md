# Concurrent work and the current boundary

October 23, 2026. This is an additive attribution and scope record.
Earlier proofs and finite reports in this package retain their exact
checkpoint contents; their stated boundaries describe those arguments.

## The regular kernel argument

[PR113](https://github.com/1337isnot1337/matrix-mult-bounds/pull/113),
at `08ac3e983e270cf3df4e26d960ceb16415f7ef31`, records the regular
right-inverse kernel residual and full-rank-long-leg exclusion. This
package already credits that concurrent checkpoint. Its own proof of
the residual is a self-contained rederivation, not a priority claim.

## Concurrent rank106 continuations

[PR125](https://github.com/1337isnot1337/matrix-mult-bounds/pull/125),
at `fc0a139ef447a4d8640f0fdf1781836ea7fa868a`, excludes a regular long-map
limit of rank at least106 by a shared-correction target-ruling argument.

[PR132](https://github.com/1337isnot1337/matrix-mult-bounds/pull/132),
at `f9bce104af5e50d796488a1c8d5ff4d8d02ba260`, reaches the same rank106
threshold through coherent-factor propagation and rank-one preservers.
Its method overlaps the independent preserver argument in this package's
gap_extension.md. Both concurrent continuations retain their own stated
dependencies and review status. This package makes no priority claim
for that threshold or the overlapping mechanism.

## Adopted rank23 source cap and rank102 exclusion

[PR129](https://github.com/1337isnot1337/matrix-mult-bounds/pull/129),
at `9eca895e3618ad1f560e0565dc30134478e88da8`, proves that every linear
space of A4 source slices of rank at most23 has dimension at most eight.
Its elementary diagonal specialization and matching minors attain the
bound and imply that both scalar-normalized long ranks are at most101.

The proof in `adopted/pr129_torus_low_rank_proof.md.txt` is an exact byte copy
of that commit's source file. Its original relative links are retained;
the immutable repository link in torus_rank_sum.md is the canonical
location. The Git blob identity is checked locally as well as SHA-256.

The new [sum200 continuation](torus_rank_sum.md) adopts this source cap
and applies it to the entire leading polar first-map image. It does not
claim the source cap, its finite minors, or the individual rank102
exclusion as new results of this package.

## Concurrent rank20 classification

[PR142](https://github.com/1337isnot1337/matrix-mult-bounds/pull/142),
at `036671f072123569bd764808ff57d18128ff11d0`, classifies the entire
rank-at-most20 biform locus using a quadratic common divisor in one
variable. It proves the sharp dimension-eight source-space bound and
applies it to leading rank105. Its exact classification is more specific
than the dimension consequence needed here. PR129's cap already gives
that dimension consequence and a stronger individual long-rank exclusion.
No normalized sum200 result appears in either pinned checkpoint.

All cited AI-derived source results remain at their stated written-proof
status. Adoption, same-session checking, and passing tests do not give
external independent review or formalization. None constructs a smaller
matrix-multiplication exponent.
