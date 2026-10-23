# Which changes escape the fixed external decomposition obstruction?

The earlier external-grid-seed package excludes direct termwise reuse of
the pinned AlphaTensor M(4,5,5) rank-76 decomposition in one Q(6,4)
evaluation-grid alignment. It leaves changes to that decomposition open.

The selected questions are precise:

1. Can a finite sequence of standard shared-factor flips permit rank
   reduction or deletion of a nonempty subset by a physical stabilizer
   degeneration?
2. Can rank-increasing splits followed by a common physical stabilizer
   degeneration produce a different rank-76 border decomposition with
   fewer distinct first-leg directions?
3. Does the resulting seed meet the necessary grid-incidence conditions?

The first question has a negative answer for this exact seed. The second
has an explicit positive answer. Neither answer constructs maps from
Q(6,4), proves a new rank record, or improves the exponent. The third
question has a negative answer for these two witnesses in the specified
termwise alignment. The later fixed-component proof preserves that
exclusion under every finite standard flip of either seed. Counting
distinct directions alone is insufficient.

The [six-split continuation](../2026-10-23-gauged-splits/README.md)
answers positively whether another simultaneous deletion can use
separate factor gauges on each discarded term. For a common physical
one-parameter family, it is sufficient that the sum of the three factor
valuations in each discarded tensor be positive. Requiring every arrow
to raise one common flag without term-dependent gauges may be stronger.
The exact six-term witness separates these two conditions. Larger
batches, useful factor changes in the new component, and actual source
maps remain open. Any accepted witness must replay the full surviving
Laurent tensor, including every error coefficient.

This package separates a finite exact certificate from its written
mathematical implication. All work is owner-directed AI research, with
no independent review or formalization.
