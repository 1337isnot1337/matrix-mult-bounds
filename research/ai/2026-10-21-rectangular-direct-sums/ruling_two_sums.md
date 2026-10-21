# Ruling-gate refinement of the ordinary two-summand frontier

October21,2026. Finite application of the new written, unreviewed ruling
lemma. Passing a gate is not a tensor construction or an exponent gain.

The prior complete scan through source leg dimension1500 retained4469
ordinary targets with exactly two positive rectangular summands. Applying
the new ruling-dimension gate excludes3717 of those targets and leaves752:

- A89:50 predecessors, all50 excluded.
- A(8,10):3425 predecessors,2761 excluded,664 retained.
- A99:994 predecessors,906 excluded,88 retained.

The other source formats were already closed by the prior gates. Together
with the updated single-target scan, this closes all improving ordinary
one- or two-block targets through source leg dimension1152 in the stated
source family. It does not close three or more summands, larger sources,
tensor powers, or general singular degenerations.

For each target block, the lift rank is computed using the total target
leg dimensions, including the other summand. The scalar Hankel image of
rank-at-most-k inputs then gives the k-ruling dimension constraint. The
existing cap certificates cover every source format used here. The general
proof assumptions are unchanged by having another positive summand.

## Reproducible predecessor identity

The three input manifests store only the two oriented shapes per record.
`ruling_two_sums.py` reconstructs the complete previous record, including
leg dimensions, exact score intervals and strict-score status. Its SHA-256
must match both the manifest and the previously published full survivor
hash in `extended-frontier.json`. All4469 predecessor records have certified
strict score gain. This prevents dropping, adding or reordering a target
silently when applying the new gate.

The replay computes every new witness and stores hashes of the excluded
and retained full records. It also publishes every retained pair of shapes.
The earlier report is retained as the predecessor snapshot rather than
being overwritten to make its old counts look current.

The original range through dimension960 was already closed. The extended
predecessor report exhausts all24 additional formats through dimension1500.
Only the three formats above had survivors, so the refinement is complete
relative to that earlier exhaustive scan. No independent review or historical
priority is claimed for the general mathematical lemmas.
