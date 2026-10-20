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
