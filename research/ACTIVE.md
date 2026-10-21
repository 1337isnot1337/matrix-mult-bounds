# Integrated research coordination

The exponent-improvement goal is active; no bound below 9/4 is established.
The user requests frequent integration of completed work into main and cleanup
of fully merged task branches. Preserve proof status and source attribution
when merging; integration is not theorem acceptance.

## Constructive-spectrum continuation

Branch: `research/constructive-spectrum-20261020`, PR #28, ready for review.
Pushed checkpoints `5f9b203`, `e042848`, and `e44aaff` preserve the oriented
endpoint, nonmonic coefficient, source-construction, and rank-obstruction
work. Checkpoint `eed3cbc` adds higher-rank Hankel obstructions and exact
rational constructions, including main `2a7c503`. The subsequent verifier
repair includes main `75bf6a3`: it removes an undeclared NumPy import and
passes 344 tests with only the maintained dependencies available. The current
integration also includes main `fb280ab`, with 350 tests and all five
archive replays passing in the same restricted dependency environment.
All statements retain the evidence status in `claims.json`.

The parity A(5,5) target M14 plus M4 is closed by a written obstruction
that also covers singular degenerations. All ordinary square direct-sum
targets that could pass the stated finite score are closed in
all 51 source formats of leg dimension below 784. Do not restart numerical
searches in those excluded classes. A(7,8) to M25 plus M5 is a remaining
ordinary square target at the first surviving source size; its maps are
missing. The former A(5,6) M16 targets are excluded even before further
blocks are appended. The higher-rank theorem requires 3r<=a+b-1; explicit
varying-scheme pencils show why this hypothesis cannot simply be dropped.

Productive open questions include singular degenerations of the full
sources, unequal rectangular targets, tensor powers, the nonmonic flag
system, and an interior-spectrum higher-difference theorem. The actual
family A(a,a) to M(2a−2) plus M(a−2) supplies exact multi-block controls,
but no exponent improvement. The proposed additional scalar has mixed
coefficients and must not be treated as a construction.

New composition controls are A(2,2) plus one scalar to M3, and A(5,6)
to M8 plus A(2,3). The extra source scalar in the first identity is
essential to that certificate. Scalar-defect recycling, retained residual
sources, and constructions beyond the excluded ordinary one-copy formats
remain active questions.

## Earlier coordinated integrations

The subsequent four-lane main integration at `a83bc24`, combined with the
graded-obstruction checkpoint `635bf48`, passes 162 tests. The new proofs
close two graded-weight regions but leave intermediate slopes and arbitrary
singular shared maps open. See `../docs/integration_2026-10-20.md` for pins.

The product/recoupling package entered main through PR #2 at `93f8f8a`.
PR #1 adds the Koszul/scaling/source-obstruction package and reconciles the
shared status and research-direction documents. Its combined local replay
with that main revision passes 106 tests. Both historical archives are
unchanged. Current package pointers:

- `ai/2026-10-20-koszul/ACTIVE.md`: singular shared-map and intermediate-weight
  questions; read the newly excluded constant-basis and graded regions first.
- `ai/2026-10-20-mixed-restrictions/README.md`: collision-capacity questions.
- `../docs/concurrent_research.md`: pinned results on the other active branches,
  including which proofs were inspected or adopted.

Do not delete a worker branch with unmerged commits. Fetch before starting
new work or publishing an integration, and test the combined tree.

## Product-filtration worker checkpoint retained from PR #2

Goal: continue until a rigorously supported matrix multiplication exponent
strictly below 9/4 is obtained. **ACTIVE / INCOMPLETE.** No such bound exists.
The user explicitly instructed not to stop at checkpoints and to merge
verified work into main frequently, cleaning up incorporated branches/PRs.

Checkout: `/home/cinna/matrix-mult-schur-20261020`.
Branch: `research/graded-quantum-flags-20261020`.
PR #2 merged into main at `93f8f8ab951e104cda041d3180f2401a4c0f81d3`.
Its tree equals the locally and remotely verified `20734a9` checkpoint.
PR #4 merged the quantitative capacity theorem at `34c2367` after the
required CI check passed. Its incorporated branch was removed as well.
The merged `research/product-filtration-20261020` branch was removed.
PR #10 merged the Laurent-output extension at `7d97155` after current CI;
its fully incorporated local and remote task branches were removed.
Preserve other workers' active branches and the first-pass archive.

Current results:

1. The two-sector inequality narrows the hypothetical critical amplitude to
   1/Gamma(4/3)<=K<=(16/9)^(1/3), a nonempty interval. P_* survives the
   whole family with cubed score at most 27/32. No unchanged grid is needed.
2. Full recoupling coefficients, scalar tight-support certificates, explicit
   affine direct sums, W/CW source certificates and exact finite screens are
   retained in their own packages. No scored profile violation was found.
3. Active-output disjointness and repetition capacity now give an asymptotic
   overhead lower bound 3/2-sqrt(3)/4 for coordinate input injections with
   arbitrary nonzero scalars, constant output mixing and diagonal weights.
   It permits arbitrary canonical target-copy counts and limsup A/m<=5/4.
   This exceeds the required approximately 1.020472. The proof is written
   and unreviewed. The joint-word extension now allows arbitrary Laurent
   output maps while retaining monomial input maps. Actual input mixing
   remains outside the proof.

Current queue:

PR #25 merged the exact quantum source family at `4289a7b`. The tested
head `d176af8` has the same tree; hosted CI passed and the incorporated
local and remote branches were removed. Current work is
`ai/2026-10-20-graded-quantum-flags/QUESTION.md`: leading-map obstructions
and an ungraded matrix-space construction search. The torus profile is
adopted from the other worker's merged PR23, not independently promoted.

PR #15 merged the balanced coefficient reduction at `9b2fcc3` after current
CI and 219 combined tests. The merged tree matches the verified head; its
local and remote task branches were removed. The monic equations remain
open, with no Hensel certificate from the completed small-field pilots.

The paired all-power package merged in PR #17 at `ea72ec4`. Its tree equals
the tested PR head `118cd9c`; both local and remote task branches were
removed. The combined suite at that head passed 246 tests, and hosted CI
passed. The next worker question is in
`ai/2026-10-20-quantum-recoupling/QUESTION.md`. Generic source equivalence
and root-basis controls are exact; no improving quantum limit is supplied.

1. The new paired-source calculation proves an exact 3a-2 dimensional first
   Koszul kernel for every size. It excludes full-capacity M(a,2a-1,a) and
   the otherwise promising size-five matrix direct sum. The complete size-four
   one-copy matrix-block score certificate is below the needed finite gain.
2. The new all-power formula excludes the former P_6 to M(6,10,6) target
   at power seven, with rank gap 1,456,180. The complete first-leg frontier
   through a=13 excludes all 239 improving dimension-compatible single
   matrix shapes modulo B/C exchange. The source proof works over every
   field. A separate cohomological matrix proof now gives an efficient
   alternating sum over every field, agreeing with the complex Casimir
   calculation. The complete frontier through a=16 has 28 survivors,
   first at a=14. No surviving target is constructed; proofs are unreviewed.
3. Joint extraction from paired factors or their powers, general nonmonic
   balanced coefficients, and arbitrary Laurent input families remain open.
   Do not repeat the closed regular-shared and separated-weight experiments.

The paired proof, exact kernel controls, finite budget potential and target
implication are in ai/2026-10-20-paired-sources/. Both conditional exponents
and all failed numerical fits remain nonclaims of an achieved bound.

Historical local extension validation: 184 combined tests pass after integrating
main daeae6e, with its intermediate-weight covers. The report is
results/mixed-restrictions-2026-10-20/tests-laurent-after-daeae6e.txt.
The earlier standalone extension checkpoint passed 179 tests.
Earlier merged validation: 174 combined tests after integrating 424dd92;
the earlier standalone capacity checkpoint passed 73 tests and the full
five-part archive replay
under Python 3.12.3 / SymPy 1.14.0. Logs are in
results/mixed-restrictions-2026-10-20/. Hosted run 39505129621 executed both
unittest and archive-replay steps successfully at 20734a9. An earlier billing
failure was historical infrastructure unavailability, not a test failure.

Concurrent overlaps are credited in package notes and sources.json. In
particular, canonical exact-restriction and equivariant-flattening arguments
independently overlapped d2d505c and 6bdab15. The quantitative capacity bound
is complementary to 8e0a766, retaining distinct hypotheses.
