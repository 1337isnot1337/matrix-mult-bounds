# Research status

Date: October 20, 2026.

**No improvement below $\omega\le9/4$ is established here.** The external baseline belongs to OpenAI. The initial local work analyzes a scalar relaxation and records finite searches.

The [main integration checkpoint](docs/integration_2026-10-20.md) combines the
four research lanes and passes 160 local tests plus the five original archive
replays. Written proofs remain unreviewed, and conditional constructions remain
unproved. Active worker branches continue to carry new experiments.

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

## All-size product-filtration result

[Written proof](research/ai/2026-10-20-concavity-equivalence/research_note.md) |
[Exact proof-chain checks](results/concavity-equivalence-2026-10-20/verification.json)

AI-FILTRATION-007 settles R2 for the three fixed-label two-source families:
for every positive, symmetric profile with `F(1,b)=b`, those families are
equivalent to separate concavity including the zero boundary. The matching
profile satisfies that boundary, so it survives **all positive integer
quadruples**, beyond the previous finite grid. Actual character profiles have
the boundary from the elementary restriction `B_Y(a) tensor B_X(b) >= C(a,b)`.

The written proof is unreviewed and not formalized. New exact checks cover
11,808 inequalities and 5,184 intermediate bounds on 1,296 source quadruples,
plus 4,860 inequalities at six larger or unequal sources. This rules out an
improvement based only on adding these families to the matching-profile
relaxation; it does not exclude coupled-fiber or oriented tensor constructions.
The exponent remains unchanged.

## Scaling and critical-shape bridge

[Analytic argument](research/ai/2026-10-20-concavity-equivalence/homogeneous_rigidity.md)
completes the second-pass draft under the stated replication and rank
assumptions. AI-HOMOGENEOUS-008 gives the full homogeneous limit and forces
the displayed unique shape, up to amplitude, at `t=3/4`, without assuming
differentiability. The diagonal derivatives agree as a conclusion at equality.
Uznański's earlier oriented rescaling is explicitly attributed.

AI-CURVATURE-009 proves the conditional criterion
`omega <= 9/(4(1+delta_0))` if the normalized limiting curvature is at least
the same positive `delta_0` for every relevant character. The limit and
derivative bridge are supplied; **the positive curvature premise remains
unproved**. Compactness also explains why excluding every endpoint character
would suffice for some strict, potentially nonnumerical improvement. No such
exclusion or smaller exponent is established. These written arguments have
no independent review or Lean formalization.

Concurrent reports at `712c91a` (fixed-label compatibility) and `30219d0`
(actual-character rigidity/curvature) overlap these conclusions and are
explicitly credited in the notes. Additional content here includes the
filtration converse and boundary counterexample, direct scalar limit proof,
and compactness consequence. These overlapping conclusions are not counted
as independent new advances or independent review.

AI-FATPOINT-GROWTH-010 gives a concrete conditional target using the all-degree
extension of the Koszul worker's fat-point tensor. A source cost factor below
`9/(7*2^(1/3))`, about `1.020472`, would beat 9/4. The cost-one case would imply
the rational bound `125/56`. **The source degeneration is unconstructed**, so
neither number is a new exponent result. The proof, exact threshold certificate
and 528 finite rank-identity checks are in the
[construction route](research/ai/2026-10-20-concavity-equivalence/fatpoint_growth_route.md).

The same branch now proves an arbitrary exact-restriction cost of at least two
for the canonical fat-point targets, using their special rank-`ka` slice.
This strengthens the concurrent maximum-slice estimate. The construction
must be singular. Fixed-shared-coordinate attempts are closed by the other
worker's stronger catalecticant obstruction at `6bdab15`; the active graded
discovery therefore includes an unrestricted shared basis. The completed
Chebyshev search covers 18,440 candidates and gives no finite profile violation.
No floating fit is accepted as a certificate.

## Selected SL(2,7) finite target

The [SL(2,7) lane](research/ai/2026-10-20-sl2-seven/README.md) derives its
complex group algebra block sizes through exact rational class-algebra
idempotents, without importing a character table. Integer root intervals
certify that a degeneration to M(16,16,17) would imply omega < 2247/1000.
**No such degeneration is constructed.** The source cost comparison is
conditional evidence for selecting this finite target, not an exponent bound.
Its SAT adapter credits and pins the concurrent group worker's implementation.
The exact source and graded-verifier checkpoint passes all 59 local tests.
The first 600-second run ended at its time limit with zero pair-injective
models and no witness. It provides no impossibility proof.

The follow-up [central-involution argument](research/ai/2026-10-20-sl2-seven/central_involution_proof.md)
shows that a pair differing by a central involution in one set forces the
other pair map to inject into the central quotient. For shape (16,16,17),
all three sets must therefore avoid central pairs. This adds 504 sound binary
clauses to coordinate-potential discovery. Exact checks cover 334 cancelling
two-term trades and the strict counting threshold. The claim concerns this
construction class, not every complex tensor degeneration.

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

Concurrent results are indexed with pinned commits in
[the collaboration review](docs/concurrent_research.md). They close the old
fixed-label filtration question and supply additional constructions and
obstructions, with their stated review and verification limits. They do not
establish an exponent improvement.
## Concurrent product-filtration constructions

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

## Whole-filtration entropy investigation

Branch `research/full-filtration-entropy-20261020` studies the whole support
`i+j=k`, separately from the other workers' Koszul and matched-row audits.
[Written proof](research/ai/2026-10-20-full-filtration/research_note.md) |
[Exact certificates](results/full-filtration-2026-10-20/entropy_certificate.json).

- AI-FULL-ENTROPY-001: an analytic dual certificate bounds every probability
  distribution in the explicitly defined optimistic entropy score.
- AI-BALANCED-ENTROPY-002: for every integer `n>=2`, that score for the balanced
  source `C(n,n)^2` is at most `39/40` of its matching source profile. The proof
  uses 3,794 exact block tests for sizes 2--22 and a positive-coefficient
  polynomial for every size at least 23.
- EXP-FULL-ENTROPY-001: all 20,736 source tuples through size 12 admit exact
  upper certificates over their entire probability simplex.

These are unreviewed analytic results and exact finite certificates. The
optimistic score is not claimed as a proved weighted block-extraction theorem.
The all-size unequal-source inequality remains open. This rules out one
proposed escape in the stated scope; the exponent remains `9/4`.

## Exact finite-group construction campaign

[Research note](research/ai/2026-10-20-group-potentials/research_note.md) |
[Reports](results/group-potentials-2026-10-20/) |
[Integer-only verifier](research/ai/2026-10-20-group-potentials/verify_reports.py).

The SL(2,5) source degrees are now checked from nine primitive central
idempotents, with all 81 products verified over Q(sqrt(5)). Exact integer-root
intervals show that a degeneration of one of the three reported target shapes
would imply `omega <= 2249/1000`. **That degeneration is unconstructed.**

A new written, unreviewed determinant-divisor argument excludes a target
`M(n,n,p)` whenever a source irrep degree `d>N-np` is not divisible by `n`.
It removes three small affine-group candidates under arbitrary basis changes,
beyond the coordinate-potential search class. It does not exclude the SL(2,5)
targets or establish a smaller exponent.

The exact search has a genuine (3,3,3) control degeneration and 479 verified
Farkas cuts across two control/candidate runs. The larger target runs timed out
or returned SAT-solver UNSAT without proof traces; these are not independently
checked nonexistence results. Construction research continues.

The [rank-locus dimension proof](research/ai/2026-10-20-group-potentials/rank_locus_proof.md)
now excludes the original SL(2,5) shapes **(9,9,12)** and **(9,10,11)** under
arbitrary complex tensor degeneration. The explicit source rank-eight variety
has dimension 14, forcing required source dimensions 122 and 124, respectively,
against the actual dimension 120. This is a written, unreviewed proof, not a
SAT-derived exclusion.

An exact finite enumeration of every sorted shape passing the degree-sum gate
at 9/4 leaves only **(10,10,10)** after this screen. That shape and selected
larger affine-group candidates remain unconstructed. The same rank-locus
screen removes several affine cases that had only untraced SAT negatives.
The abelian-coset ceiling lemma and exact normal-subgroup tables further
strengthen discovery constraints; these restrictions do not constitute an
exponent improvement.

The [normal-subgroup Fourier proof](research/ai/2026-10-20-group-potentials/ternary_fourier_proof.md)
excludes three four-point unique-sum sets in C3^4. Its elementary integer
bound is 1232 versus the Parseval requirement 1088. This excludes the
coordinate-potential (16,16,16) ansatz in index-four extensions of that group;
it does not exclude arbitrary complex degeneration. The proof is unreviewed.

An exact finite affine-source frontier leaves 58 conditional candidate shapes
among 45 groups of order at most 250 with normal prime subgroup at most 61.
New F4^3:C3 offset searches checked 426 pair-injective candidates, all rejected
by exactly replayed Farkas circuits. No qualifying degeneration was found.

A further [fiber-mean argument](research/ai/2026-10-20-group-potentials/crossed_means_proof.md)
excludes an entire affine-plane base family in F4^3:C3, including arbitrary
other plane directions and offsets. Its hypothesis is scalar invariance of
two complementary base-plane sums. Two opposite strict mean inequalities
give the contradiction. This written proof is unreviewed and has a narrower
scope than arbitrary group-algebra degeneration. Another 2000 discovered
direction assignments have exactly replayed mean certificates.

The [F8 source campaign](research/ai/2026-10-20-group-potentials/octal_research.md)
now has exact local packing frontiers and a streaming whole-support verifier.
The F8^2:C7 frontier reduces 3942 local direction triples to 342 classes;
global constructions remain unresolved. In F8^3:C7, 87 proposed deletions
from an explicit pair-injective parent fail exactly replayed potential
constraints. Another 10752 symmetry-transformed circuits verify exactly.
The resulting hole-hitting search timed out. No target degeneration or
exponent improvement follows from these source and obstruction certificates.
