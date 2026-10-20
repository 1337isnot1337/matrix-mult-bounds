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

## Second-pass checkpoint

[Research and recovery record](research/ai/2026-10-20-session2/README.md) | [Supplementary claims](research/ai/2026-10-20-session2/claims.json) | [Verification](results/session2-2026-10-20/verification.json)

The dimension-only search covers 189 cases and finds 85 candidate scores. None is certified by dimension accounting alone. Exact tensor calculations reject two specific candidates.

The checkpoint includes draft homogeneous-profile rigidity and curvature criteria. Their missing hypotheses and unproved gains remain explicit. The stronger scoring search is incomplete, with no completed run.

The temporary second-pass files were not retained in the current runtime. Reconstructed programs and regenerated reports are labeled accordingly. All eight new checkpoint tests passed. The first-pass archive remains unchanged.

The [external source review](docs/external_followups.md) covers the three repositories suggested by the owner. It includes Filmus's finite identities-to-exponent criterion with its hypotheses. No external Lean rebuild is claimed.

## Koszul research pass

[General proof and scope](research/ai/2026-10-20-koszul/research_note.md) |
[Exact candidate audit](results/koszul-2026-10-20/candidate_audit.json)

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
