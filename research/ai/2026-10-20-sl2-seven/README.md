# Selected finite group lane: SL(2,7)

Question: construct and exactly verify a group-potential degeneration from the
complex group algebra of SL(2,7) to M(16,16,17). No such construction is supplied
at selection. No smaller exponent is claimed.

The exact source calculation now derives the degree list
`(1,3,3,4,4,6,6,6,7,8,8)`, whose squares sum to 336. Exact root intervals
certify a conditional omega < 2247/1000 gate; see [the proof](source_proof.md).
The concurrent rank-locus screen does not immediately exclude the target.
The necessary degeneration remains missing. This is not a new exponent bound.

This lane differs from the other worker's active SL(2,5) and affine-group
searches. `import.json` pins immutable copies of its integer group verifier,
SAT encoding and exact Farkas machinery, with attribution. The imported files
are preserved. A separate adapter chooses p=7 and the target shape.

Validation enumerates the group directly from determinant-one 2x2 matrices
over F7, derives the degree list through rational central idempotents, and
certifies the strict exponent comparison with rational root intervals.
Any accepted potentials must pass integer group-product verification. A timed-out or
untraced SAT run is not an impossibility proof.

The first bounded run (seed 20261320, CaDiCaL 1.9.5 interface, 600-second
budget) ended at the time limit with no pair-injective candidate and no
accepted witness. It generated about 2.5 million conflicts. This is search
diagnostic data, with no proof trace and no nonexistence conclusion.
The source certificate, Borel coverage and final report are retained under
`results/sl2-seven-2026-10-20/`.

The [central-involution lemma](central_involution_proof.md) supplies 504
additional necessary binary clauses for this target. The center-pruned run
uses the same seed and budget, so any changed behavior is attributable to
the strengthened encoding rather than a seed reroll. Its outcome will be
recorded separately; no running checkpoint is a completed result.
