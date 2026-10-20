# Research status

Date: October 20, 2026.

**No improvement below $\omega\le9/4$ is established here.** The external baseline belongs to OpenAI. The initial local work analyzes a scalar relaxation and records finite searches.

| ID | Local statement | Evidence status |
| --- | --- | --- |
| AI-SCALAR-001 | Exact pointwise-minimal profile for S1-S3 | Written proof; unreviewed |
| AI-RANK-002 | Matching profile satisfies the rank upper bound at $t=3/4$ | Written proof; unreviewed |
| AI-REPLICATION-003 | Matching profile satisfies replication at $t=3/4$ | Written proof; unreviewed |
| AI-PACKING-004 | Flattening obstruction for shorter identical-sector packing | Written proof; unreviewed |
| AI-FILTRATION-005 | Additional product-filtration inequalities | Derivation; unreviewed |
| AI-CONDITIONAL-006 | Uniform positive tripling gain implies a smaller exponent | Conditional implication; premise unproved |
| EXP-PROFILE-001 | 73,856 grid assertions and four symbolic identities | Reproduced |
| EXP-FILTRATION-002 | 353,664 inequalities over 20,736 source quadruples | Reproduced; no finite violation |
| EXP-WEIGHTS-003 | 242,668 specified weight candidates | Reproduced; no scored violation |

[Claim ledger](research/claims.json) | [Full original note](research/ai/2026-10-20/research_note.md) | [Replay report](results/bootstrap-2026-10-20/summary.json)

The general proofs, rather than their finite checks, support the all-integer statements. No independent review or Lean formalization of these local arguments is recorded.

The matching-profile result rules out improving the exponent from only its listed scalar assumptions. It neither proves $\omega\ge9/4$ nor excludes the full tensor spectrum.

The current next steps are listed in [research directions](docs/research_directions.md). Repeating a completed finite search with the same parameters is reproduction, not new research progress.

## Second-pass checkpoint

[Research and recovery record](research/ai/2026-10-20-session2/README.md) | [Supplementary claims](research/ai/2026-10-20-session2/claims.json) | [Verification](results/session2-2026-10-20/verification.json)

The dimension-only search covers 189 cases and finds 85 candidate scores. None is certified by dimension accounting alone. Exact tensor calculations reject two specific candidates.

The checkpoint includes draft homogeneous-profile rigidity and curvature criteria. Their missing hypotheses and unproved gains remain explicit. The stronger scoring search is incomplete, with no completed run.

The temporary second-pass files were not retained in the current runtime. Reconstructed programs and regenerated reports are labeled accordingly. All eight new checkpoint tests passed. The first-pass archive remains unchanged.

The [external source review](docs/external_followups.md) covers the three repositories suggested by the owner. It includes Filmus's finite identities-to-exponent criterion with its hypotheses. No external Lean rebuild is claimed.

## Product-filtration compatibility, all sizes

The [new concavity proof](research/ai/2026-10-20-affine-direct-sums/research_note.md)
settles R2 for every displayed fixed-label product-filtration inequality:
all positive integer parameters preserve the matching profile P_*.
This replaces the earlier finite-only knowledge for that family. The proof is
AI-derived, written and unreviewed; it does not construct a tensor character.

The exact regression certificates check 81,648 comparisons over 4,096 source
quadruples, plus six dedicated tests. The universal statement rests on the
written proof. Full direct sums involving multiple labels remain outside this
theorem. No exponent improvement is established.

The [affine-line construction](research/ai/2026-10-20-affine-direct-sums/direct_sums.md)
adds explicit integer-weight degenerations retaining full direct sums across
several labels. Four exact determinant-basis examples check all 4,770
coefficients. A finite assignment upper bound covers 9,600,473 maximal
relaxed matchings on 6,561 ordered source quadruples through dimension 9;
none violates P_* at t=3/4.

Other agents independently pushed a stronger fixed-label equivalence theorem
at `73b2d20` and broader entropy-score bounds at `e6d33e7`.
[The overlap record](research/ai/2026-10-20-affine-direct-sums/COORDINATION.md)
separates their work from the distinct coefficient construction here.

## Off-leading recoupling blocks and low-border-rank sources

[Full Clebsch--Gordan coefficients and coverage](research/ai/2026-10-20-clebsch-gordan/README.md)
now retain actual k>i+j blocks discarded by the old filtration. Exact axis
and diagonal-factor certificates recognize convolution blocks. One interior
five-dimensional transvectant contains C(3,3), improving its lower score from
5 to 56/9. Completed binary/ternary outer-weight screens found no matching
profile violation; their exact scopes and overlapping counts are recorded.

[Truncated-polynomial algebra sources](research/ai/2026-10-20-truncated-algebras/README.md)
have explicit border-rank certificates and permit a direct critical-parameter
test against r^(4/3). Completed binary runs through r=7, including a stronger
output-deletion score, found no violation. Work on algebra products and
nonseparable weights remains active. See [the live queue](research/ACTIVE.md).

The [two-sector source-rank inequality](research/ai/2026-10-20-truncated-algebras/two_sector_bound.md)
now gives `2P(a,b)<=(a+2b-1)^(1/t)` at all sizes. With the concurrent
critical-shape theorem, the remaining t=3/4 amplitude must satisfy
`1/Gamma(4/3)<=K<=(16/9)^(1/3)`. The interval is nonempty. A separate
all-size argument proves P_* survives this entire inequality family with
cubed score at most 27/32, so a larger grid cannot exclude it.

[Exact scalar tight-support certificates](research/ai/2026-10-20-clebsch-gordan/subrank_blocks.md)
strengthen all 101 recoupling blocks in six sources. This uses the external
scalar theorem, without assuming a weighted block-transfer theorem. Added
outer-coordinate restrictions improve a finite score but do not violate P_*.

## Exact mixed-target collision experiments

The [new mixed-target package](research/ai/2026-10-20-mixed-restrictions/README.md)
allows arbitrary shared-coordinate permutations and output-coordinate sums.
Independent integer coefficient replay verifies the saved m=2,3 controls and
a C(4,11) to T_4 degeneration. Z3 reports UNSAT for m=4,B=10 in this larger
finite ansatz; m=5,B=15 timed out. No unbounded construction or smaller
exponent is proved. The local restriction and equivariant-flattening notes
independently overlap concurrent results, which are explicitly credited.

The [capacity refinement](research/ai/2026-10-20-mixed-restrictions/collision_capacity.md)
now excludes the exact-length permutation/collision ansatz for all m>=10.
The proof is written and unreviewed; near-unit asymptotic overhead remains
open. Proved solver cuts preserve the m=2,3 SAT controls and resolve the
m=5 query as UNSAT. The m=6 run times out; it supplies no exclusion.

The [quantitative capacity theorem](research/ai/2026-10-20-mixed-restrictions/asymptotic_capacity.md)
strengthens the obstruction to asymptotic overhead at least
`3/2-sqrt(3)/4` (about 1.066987) for the coordinate-input and constant-output
ansatz, even with arbitrary canonical target-copy counts and shared source
length asymptotically at most 5m/4. This exceeds the needed approximately
1.020472. General input mixing and general Laurent shared maps remain open.
The result is written and unreviewed, with 1,599 explicit integer-matrix
controls and exact algebraic comparisons. It does not improve the exponent.
