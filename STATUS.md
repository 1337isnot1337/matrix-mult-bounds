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

## Koszul research pass

[General proof and scope](research/ai/2026-10-20-koszul/research_note.md) |
[Exact candidate audit](results/koszul-2026-10-20/candidate_audit.json) |
[Supplementary claim ledger](research/ai/2026-10-20-koszul/claims.json)

Written, unreviewed formulas now give every Koszul-flattening rank of a
convolution in every leg orientation, including padding of the shared space.
They reject **all 85 specific packings** saved by the second-pass dimension
search. This does not exclude alternative packings for those sources.

In particular, the former best candidate needs border rank at least 30 while
its source has rank 21. The all-size proof permits arbitrary independent
identifications of the shared block spaces. Exact coefficient matrices check
180 oriented cases and 27 padded cases; those finite checks are not the proof.

The matrix-multiplication exponent remains unchanged. New constructions must
pass these tests and still provide actual tensor identities.

The [agent-board review](docs/agent_board_review.md) attributes four external
research reports and records a checked correction: the published
Massarenti-Raviolo exact-rank bound excludes the board's n=34 through 37 search
window. At n=38 only rank 3585 survives the two lower bounds used here. This
does not exclude or construct border-rank algorithms.

Two further results sharpen the next construction target:

- [Mixed-sector survivor](research/ai/2026-10-20-koszul/research_note.md#6-an-all-size-family-that-these-necessary-tests-do-not-exclude):
  an explicit all-k family passes every full-space Koszul test on all three legs. Its score exceeds
  P_* from k=53 onward (first source C(4,530), ratio 37206/37205). The degeneration
  is unconstructed. Its canonical target has an explicit border-rank-10k
  certificate, but coordinate selection plus diagonal weights cannot realize it
  from that source: this restricted ansatz requires source length at least
  12k-1. Arbitrary changes of basis remain outside the obstruction.
- [Actual-profile rigidity](research/ai/2026-10-20-koszul/scaling_rigidity.md):
  Uznański's rescaling theorem and a one-sided derivative proof remove the second
  pass's missing analytic bridge and global C1 assumption. Every critical
  character must have the stated homogeneous profile. The curvature criterion
  now applies to actual characters, but a uniform positive curvature gain remains
  unproved. No exponent improvement follows yet.

The [all-dimension extension](research/ai/2026-10-20-koszul/all_dimension_targets.md)
now provides explicit targets T_m of dimensions (m,N,N), N=m(m+1)/2,
with border rank N and an all-size full-space Koszul survival proof. A source
degeneration C(m,B_m) to repeated copies, at asymptotic overhead below
9/(7*cuberoot(2))-1, would imply a smaller exponent. At zero overhead the
proved **conditional** implication gives omega<=125/56. The source
degenerations are unconstructed. Coordinate selection and diagonal weights
require asymptotically 50 percent overhead, so that ansatz cannot meet the
criterion. Exact replay covers 20,153 interpolation coefficients, 3,276
shared-leg Koszul degrees, and 495 gap-formula cases; five dedicated tests pass.

[Broader source obstructions](research/ai/2026-10-20-koszul/source_obstructions.md)
now exclude ordinary linear restrictions at low overhead, even with arbitrary
bases. A catalecticant argument also excludes arbitrary polynomial Y/Z changes
when X keeps its binary-form coefficient structure. General shared-factor
changes remain open. Exact coefficient controls construct the m=2 all-k and
m=3,k=1 cases; these fixed dimensions do not meet the growth criterion.
Bounded real/complex orbit fits found no new certificate and are not exclusions.
The polynomial-matrix argument in that note also shows why every projected
shared Koszul test and every linear equivariant Young/Pieri test of its stated
form must pass against this border-rank-B target. It does not cover all
other-factor or nonlinear invariants.

The concurrent minimum-slice argument strengthens the ordinary-restriction
overhead to asymptotically 100 percent; it is adopted with attribution to
`d2d505c`. A new [polynomial-basis audit](research/ai/2026-10-20-koszul/orthogonal_bases.md)
excludes degree-ordered orthogonal coordinate degenerations at low overhead
for all dimensions. Its exact Chebyshev permutation reduction additionally
excludes nonidentity shared orders for m=4,...,38, for every k and admissible B.
The latter is a finite enumeration, not an all-size theorem. Independent
small enumerations and normalized small construction controls pass. General
shared-factor transformations remain open.

A further [biform proof](research/ai/2026-10-20-koszul/arbitrary_shared_basis.md)
shows that the same catalecticant lower bound survives **every constant
invertible shared basis**, including independent identifications of the target
blocks. It therefore closes the enlarged constant-G graded search as well.
The proof uses a standard projective-dimension argument and remains unreviewed;
360 exact transformed-block ranks and independent coefficient checks support
its implementation. A genuinely singular shared map is still outside it.
The same proof extends to all matched bilinear blocks with no zero divisors.
It excludes the dominant-degree weight region alpha>(m-1)*abs(beta).
A separate explicit slice support cover excludes 0<alpha<=beta, requiring
B>=k*(2N-floor(m^2/4)-1)-(m-1). These close the recorded dominant-degree
experiment and two concurrent mixed-weight directions. Intermediate slopes
and general singular shared maps remain open; no exponent is improved.

Concurrent results are indexed with pinned commits in
[the collaboration review](docs/concurrent_research.md). They close the old
fixed-label filtration question and supply additional constructions and
obstructions, with their stated review and verification limits. They do not
establish an exponent improvement.

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
