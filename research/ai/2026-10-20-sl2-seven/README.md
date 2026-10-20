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

The [projection reduction](projected_proof.md) now separates projected
membership from exact F2 lift constraints. Its first completed 600-second
run found 1,394 projected candidates, all rejected by saved, replayed parity
circuits. The two center-pruned direct variants also timed out without a
pair-injective model. None supplies a degeneration or a nonexistence proof.
The fiber-strengthened projection encoding is a further bounded experiment;
it adds abelian-preimage occupancy clauses and the center-free C8 rule.

That fiber run has now finished: 149 projected candidates all fail exact lift
equations, and all circuits replay. The next run reuses verified circuits
and their independent right-translation orbits; its source hashes and exact
template counts are recorded by the search. No running report is committed
as a completed result.

The external [ordinary TPP screen](ordinary_tpp_screen.md) excludes unweighted
triples of this shape by the published representation-theoretic bound. It
does not exclude the weighted degeneration search. A successful witness must
use its positive weights to delete unwanted terms.
