# Integrated research coordination

The [general quadratic kernel package](ai/2026-10-23-quadratic-kernel-indices/proof.md)
determines individual slice ranks through two polynomial-kernel indices,
whose sum is aD and whose first nonzero-kernel degree is computable by a
bounded exact coefficient-matrix test. It explains the distinct indices
of the earlier equal-resultant examples. For D>0 after common-factor
normalization, it characterizes the zero first index by a fixed ground-field
linear factor. Do not repeat coefficient
degree or pairwise-resultant-only searches. The root-height dichotomy in
`ai/2026-10-23-quadratic-kernel-indices/dichotomy.md` now bounds the first
index and proves the a=b=3 biform-block spectrum {9,12,14,15}. Determine
attainable splitting types in the remaining high interval, constrain linear
families, or impose compatible three-leg maps. These single-slice results
do not supply a matrix target. Written, unreviewed.

The [full-channel overlap theorem](ai/2026-10-23-column-overlap/proof.md)
closes fixed polynomial-column routing when almost all leading channel
blocks remain invertible, even with arbitrary first/auxiliary Laurent
poles. Full channel rank alone does not evade this bound. For fixed-width,
near-full outer targets in the stated regular-channel setting, further
construction must mix source polynomial columns or use the precisely
quantified extensive leading rank loss. Exact separated-window examples
retain the narrower positive construction Q(n,m) to M(floor(n/m),m,floor(n/m)).
Claim `AI-PAIRED-COLUMN-OVERLAP-001` remains written and unreviewed.

The [independent coordinate class](ai/2026-10-23-a4-coordinate-compressions/README.md)
is now complete: all 142,884 outer deletion pairs have dimension at least
40, with two exact equality witnesses. This excludes all independent
coordinate long-leg compressions of the fixed A4 conjugation family;
their maximum leading loss is six. Continue with arbitrary noncoordinate
flags in the [algebra question](ai/2026-10-23-a4-compression-algebra/QUESTION.md),
not another coordinate census. Claim `AI-A4-INDEPENDENT-COORDINATE-004`
remains written and unreviewed.

October 23 rank-two paired-source continuation: branch research/paired-rank-two-gap-20261023-auto2 proves a sharp all-field b(b+1) raw first-slice rank for every rank-two coefficient matrix of Q(n,b), with a Kronecker minimal-index formula and exact controls. Scope is independent of current PR147 residual geometry, PR164 diagonal factor hypotheses, and PR211 Laurent auxiliary-channel barrier. This source theorem does not construct a target and does not improve omega. Written, unreviewed; full regression and archive replay are required before merge.

The October 23 three-term biform continuation is in ai/2026-10-23-three-term-resultant-obstruction/proof.md. The exact R_(3,3) determinant t(2c^3-2ct^2+t^4) provides two characteristic-not-two coefficient triples with identical degrees and all pairwise resultants equal to one but ranks 14 and 15. An integral row kernel, determinant-one control, -4 minor, and 256-point exact determinant certificate are retained. The general quadratic continuation now computes the two polynomial-kernel minimal indices for u*lambda_r+v*lambda_(r+1)+w*lambda_(r+2)=0 by a bounded exact test. The root-height dichotomy now restricts those indices; attainable positive-index strata and compatible linear families remain open beyond that restriction. This is separate from PR207 diagonal Toeplitz and superseded PR209 affine-in-z work, and is not an exponent improvement.

The [single-top-polynomial biform theorem](ai/2026-10-23-top-coefficient-biforms/proof.md) now gives exact R_(a,b) ranks over every field for constant lower z coefficients and an arbitrary polynomial top x coefficient, with a residue-triangular polynomial-kernel proof. It is a strict one-slice statement and remains proof-written-unreviewed. The reproducible 3,372 modular and 24 rational rank controls passed. PR209's affine-z work and PR207's diagonal-polynomial work retain their own attribution. The general quadratic continuation now supplies an effective two-index test for arbitrary quadratic coefficients, a structural root-height restriction, and the complete a=b=3 biform-block rank spectrum. Remaining work concerns high-interval attainability, compatible linear families, or higher z-degree families with several nonconstant coefficient polynomials. No three-leg degeneration or improvement below 9/4 follows. Concurrent PR214 branch consolidation must be reconciled before merge.

The October 23 quadratic-z middle-polynomial package
`ai/2026-10-23-quadratic-z-middle/proof.md` gives an all-field exact
rank formula for the literal `alpha+z*v(x)+gamma*z^2` source slice
when the two outer coefficients are nonzero constants. It derives the
full two-generator polynomial-kernel basis and exact degree constraints,
with 580 exhaustive and 960 seeded modular checks, 135 spectrum checks,
940 explicit kernel vectors and a separate 36-case rational acceptance.
This adopts and credits PR209's polynomial-row technique but not its
theorem, and avoids PR207/208's diagonal-polynomial family. Claim
`AI-QUADRATIC-Z-MIDDLE-RANK-001` remains written, unreviewed.
The [general quadratic continuation](ai/2026-10-23-quadratic-kernel-indices/proof.md)
now computes both minimal degrees for nonconstant outer coefficients;
the root-height dichotomy restricts the first index, while attainable
splitting types and compatible linear families remain open. No full tensor target or
improved exponent is claimed. Keep this branch isolated until required
current-head CI and mathematical review gates have been checked.

This consolidated coordination log retains source-branch checkpoints and their
pinned validation receipts. Statements that tests or integrations were pending
refer to those checkpoints, unless a later receipt is explicitly supplied.
Current merged-head validation is recorded separately. Later results supersede
older next steps only within their stated hypotheses; no review-status promotion
is implied.

The [two-sided full-source conjugation investigation](ai/2026-10-23-conjugation-limit/README.md)
now has a complete limiting-space certificate and a written necessary
condition: arbitrary constant 110-coordinate compressions must lose
at least nine leading directions to permit `M(10,10,11)`. Every one
of the 6,216 principal coordinate deletions loses at most four, so that
finite class is closed. Keep the projected leading space distinct from
the full re-saturated limit; the proof explicitly bounds newly recovered
directions. The remaining question in this family is the locus
`dim(P L C)<=103`. Moving compressions and genuinely different singular
paths remain possible. Claims `AI-A4-TWOSIDED-RANKLOSS-001` and
`AI-A4-TWOSIDED-COORDINATE-002` are written and unreviewed. No full
target or exponent improvement is established.

The [low-rank-locus reduction](ai/2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md)
makes that remaining question explicit: find, or exclude, a 26-dimensional
U and two-dimensional W for which at least nine matrices in the fixed
46-dimensional outer space E send U into W. Equivalently a rank-26
compression of E must have image dimension at most 37. All killed
112-dimensional limiting matrices are confined to this outer block.
Claim `AI-A4-TWOSIDED-LOWRANK-003` is written and unreviewed; a universal
lower bound of 38 and all successful full-target maps remain unproved.

The two [recorded follow-up families](ai/2026-10-23-conjugation-limit/EXPLORATION.md)
are complete for principal coordinate compressions: the product of the
specified noncommuting square-zero factors and the moving unit from their
nonnilpotent sum both have no surviving pair. All 221 cases requiring
re-saturation in the latter family were checked over Q. Do not repeat
that finite coverage; arbitrary noncoordinate compressions remain open.

The October 23 diagonal-biform continuation is in
[ai/2026-10-23-diagonal-biform-ranks/QUESTION.md](ai/2026-10-23-diagonal-biform-ranks/QUESTION.md).
An elementary conserved-index decomposition proves that an individual
R_a(f(xz)) has rank a^2 plus d central Toeplitz ranks. A complete
quadratic criterion gives ranks a^2+2a or a^2+2a-1 over every field,
with the coefficient-one deficit exactly when a=2 mod 3. Exact finite
replay passes 312 block formula instances, 112 literal full matrices
and the saved controls. The claim is written, unreviewed and deliberately
separate from PR171 and PR186. Next: simultaneous central Toeplitz rank
defects for degree>=3; no matrix tensor or exponent is established.

The independent one-dependency residual rank-strata continuation is in
`ai/2026-10-23-oblique-slice-strata/proof.md`. It uses PR147's pinned
adapted formula and does not edit or subsume the active border-rank
package. Over all fields the first-leg slice ranks are exactly 0,2,4,
with a two-component projective rank-two locus. Formulas for all second
and third slice ranks are proved via disjoint support decompositions.
The next separate question is whether this intrinsic rank geometry can
sharpen an actual border-rank invariant; no such sharpening is claimed.

The October 23 affine-z biform checkpoint is at research/ai/2026-10-23-affine-z-biform-ranks/QUESTION.md. A written all-field syzygy proof yields exact one-slice rank ab+min(b,a*d) for arbitrary long-affine coefficients u(x)+z*v(x), including both orderings of a,b>=2. Exhaustive and seeded finite controls have passed; claim AI-AFFINE-Z-BIFORM-RANK-001 remains written and unreviewed. The [general quadratic continuation](ai/2026-10-23-quadratic-kernel-indices/proof.md) now supplies an exact two-index procedure, while PR216 retains credit for the counterexample to degree/resultant-only data. PR207 owns the diagonal Toeplitz problem. Neither a full target nor a bound below 9/4 is established.

## Laurent channel barrier continuation

`research/laurent-stencil-20261023-ab94` supplies the formal extension of
pending PR157/173/179 under their common generic channel-rank deficit.
See `ai/2026-10-23-laurent-channel-barrier/proof.md`. Arbitrary Laurent pole
orders and arbitrary auxiliary maps cannot reduce the resulting quadratic
repair bound, even for near-full targets and moving profile bases.
The remaining constructive task is a full generic channel-rank periodic
or nonlocal encoding, with complete tensor coefficients and an explicit
repair cost. No target or improved exponent has been built. Prior ordinary
branches remain separate and retain credit. The rank-margin follow-up
in `ai/2026-10-23-laurent-channel-barrier/rank_margin.md` raises the
auxiliary border-rank floor to d+h-rho-1 when d>=1 and rho<h; the first
flattening floor stays d. At fixed width this sharpens the finite bound
without changing the constructive task. All three claims remain written
and unreviewed, with separate frozen-suite and follow-up receipts.

The October23 operational-barrier continuation is in
`ai/2026-10-23-common-input-rank-barrier/proof.md`, on PR131.
Every actual complex degeneration among Full/Mid partial sums at the
same full first dimension preserves the rectangular operational
potential, even with mixed widths and independent first-leg bases.
For identical source blocks the two long dimensions already force that
comparison. The first Pass-packing checkpoint is retained separately.
New construction work must leave this fixed-dimension Full/Mid class;
shared-output blocks are one concrete question. Passing necessary rank
screens does not supply a tensor map. The proofs remain unreviewed.

The prescribed full third-jet question is now settled on d nonzero in
`ai/2026-10-23-conic-fixed-third-obstruction/proof.md`: order-four,
formal and polynomial extension are equivalent to Delta=0. Off that
locus, the explicit dual obstruction kills all 4336 fourth unknowns;
on it, two exact linear branches preserve every supplied coefficient.
Seven focused tests, complete literal-source acceptance and a separate
internal algebra audit pass. This is a new checkpoint following PR136;
the latter's full two-jet extension remains valid. The projective
criterion below now covers the normal-class base charts. Future work
can address other prescribed jets or local moduli; the fixed-third
extension question is settled. The claim remains written and unreviewed.

The prescribed full two-jet question is now closed on d nonzero by
`ai/2026-10-23-conic-fixed-two-curve/proof.md`. Exact maps of degrees
eight and nine preserve all six supplied B/C coefficients through order
two and Y1=Y2=0. Every complete product coefficient through order17,
the unit leading minors and exact prior-byte pins pass acceptance; six
focused tests and a separate sparse reconstruction pass. PR107's full
third jet with its nonzero moving-kernel correction is settled by
the fixed-third criterion above. The projective criterion above now
closes the remaining base-chart question. Do not
mistake this extension of one specified two-jet for extension of every
representative or a complete matrix target. This round's PR136 package
is frozen for final integration and current-head CI; subsequent research
belongs in a separate checkpoint. Written and unreviewed.

The fixed-first continuation in
`ai/2026-10-23-conic-fixed-first-curve/proof.md` now gives exact cubic
maps preserving both full first coefficients of PR107, for all complex
a,b,d including d=0. Six focused tests and a separate literal-source
contraction pass. The prescribed second coefficients differ only in
boundary entries; the new fixed-two package above now extends the
specified full two-jet on d nonzero. The earlier normal-class criterion remains unchanged. Keep
these local incidence curves distinct from a full matrix target; all
claims remain written and unreviewed.

The October23 polynomial-conic continuation is in
`ai/2026-10-23-conic-polynomial-curve/proof.md`. A complete degree-one /
degree-three polynomial pair realizes every cubic-component normal[1:d]
for every complex a,b,d, including d=0. All original-source coefficients
and unit rank minors replay exactly; the seven focused tests pass. This
closes existence of an all-order representative for those normal classes,
while leaving prescribed boundary velocities and lower jets distinct.
Next: describe the remaining local moduli and determine how this
rank-twelve incidence can constrain or support a full matrix target.
The companion all-order criterion now makes PR101's second-order
condition necessary and sufficient for existence on the entire affine
base chart and every projective normal direction, allowing boundary
velocity to vary. The new projective package covers the other base charts
without changing that correct affine statement.
Full regression and archived replay are required before merge. Written,
unreviewed; no full M(10,10,11) target or exponent improvement.

The October23 higher-conic continuation is in
`ai/2026-10-23-conic-higher-jets/proof.md`, following PR107 at86b5142.
The explicit mixed fourth-order family and rational tenth-order witness
pass direct source replay. A separate checkpoint on
`research/conic-fourteen-jet-continuation-20261023` extends the rational
witness through order fourteen, preserving maps through order nine and
source corrections through Y9. It then extends that witness through order
fifteen, preserving maps and source corrections through order thirteen.
Standard-library literal replays check all 4096 source terms at each order.
The checkpoint is based on the frozen PR136 head pending that integration.
The fixed-two package above supplies an all-order extension of
its own specified coefficients on d nonzero. The earlier polynomial curve
changes boundary velocity and has a broader parameter chart. Full local
regression and historical replay remain required before integration. The
claims retain written, unreviewed status and do not construct the matrix
target.

The October23 continuation on `research/conic-third-order-20261023`
studies `ai/2026-10-23-conic-third-jets/QUESTION.md`, following merged
PR101 at `539b539` and integrating nonsplit main `dcd209a`. It supplies
an explicit rational third-order family for all complex a,b,d with
d nonzero and c=-d^3, with the credited first jet and changed second
coefficient. Independent original-source symbolic replay checks all
three orders and constant unit leading minors; a separate rational
point passes standard-library replay. The later packages above supply
fourth-order and all-order results with explicit lower-jet distinctions.
This remains local rank-twelve incidence; no full matrix-target
construction follows.

The [ordered-input monomial census](ai/2026-10-23-ordered-monomial-search/README.md)
is on `research/exact-search-review-01a16975`. It completes both input
orientations in the historical binary/ternary scopes and proves an all-size
failure of pointwise swap dominance. The 24,708/370,252 cases contain no
profile violation. Do not repeat these inventories. Next work should change
the scoring bound or shared-axis class. No exponent improvement or independent
review is claimed; the package has no dependency on unmerged PR118.

The width-two continuation on `research/frontier-continuation-01a16975`
settles its [all-weight score question](ai/2026-10-23-width-two-monomial/QUESTION.md).
The written path proof closes the original scorer for C(2,b) and C(b,2)
at every size, with sharp deficits and a complete equality-support count.
All 59,046 sign-word/orientation controls through b=10 pass. Repeating
bounded width-two weight searches cannot beat this score. Minimum input
size three and stronger block scores remain separate questions. The
proof is unreviewed; no smaller exponent is established.

The nondivisor width-two source-cap continuation is on
`research/nondivisor-cap-20261023`, in
[the registered question](ai/2026-10-23-nondivisor-cap/QUESTION.md).
Its bounded A5 discovery finds rank-at-least35 witnesses in every one
of19 size11 order ideals. Acceptance minors and an all-size width-two
proof are being developed; no complex source-space cap is claimed from
that screen alone. PR129 retains the order-ideal method and PR171 the
separate binomial rank calculation. No exponent improvement is claimed.

The nondivisor pairwise-family continuation studies
`ai/2026-10-23-nondivisor-pairwise-family/QUESTION.md` on
`research/nondivisor-pairwise-family-20261023`, from main`3008d70`.
A rederived binomial Toeplitz determinant proves full active rank
a(a+d) for(1+xz)^d in characteristic zero. At a=2d+1, an ad+1
coordinate support passes all pairwise entry-cover bounds at ceiling
a(a+d)-1 yet contains that higher-rank power slice. Exact source-block
and cover controls are pending. The proof does not require unmerged
parent packages and claims no nondivisor dimension cap or exponent gain.

The rank-three input continuation is in
`ai/2026-10-23-rank-three-hankel/QUESTION.md`, branch
`research/rank-three-hankel-obstruction-20261023`. Its written argument
excludes the two nonsquare A(8,9) formats from PR138 through a Borel-fixed
projection budget and large Hankel sections. The remaining ordinary M30
rank-two parameter-image question is the next scope. General Hankel
pencil and constant-scheme-strip workers retain their existing scopes.
No singular exclusion, independent review or smaller exponent is claimed.

For fixed m>=2 and target M(n,m,n), the independent
[two-Toeplitz-long-leg question](ai/2026-10-23-toeplitz-long-legs/QUESTION.md)
excludes every ordinary Q(n,m) map with both bulk long-leg filters of
sublinear bandwidth and sublinearly many exceptional columns from the
subquadratic correction budget, even with arbitrary first-leg mixing.
The written polynomial-symbol proof is unreviewed. Five exact tests pass.
Next target is genuinely variable-coefficient long-leg maps or singular
Laurent cancellation; PR #145's shift chart and PR #147's product
residual are separate active work. No smaller exponent established.

The binomial-rank continuation studies
`ai/2026-10-23-binomial-biform-ranks/QUESTION.md` on
`research/binomial-biform-ranks-20261023`, from main`3008d70`.
The proposed exact rank is a^2+sum min(n_i,m_j) over the unequal residue
lengths modulo the two coordinate offsets. At equal offset d this is
a^2+ad-r(d-r), r=a modulo d. A field-independent path proof includes
both binomial orientations and nonzero coefficients. All114 exact
minor/cover controls and seven focused tests pass; full regression
and current-head CI remain pending. This is separate from the running PR148
validation and supplies no nondivisor dimension cap or exponent gain.

The ordered monomial audit on `research/continuation-01a16975` is recorded in
`ai/2026-10-23-ordered-monomial-audit/QUESTION.md`. Its independent checker
replays all 60 retained PR118 records and completes 394,960 binary/ternary
ordered cases, including 172,292 new a>b cases, without a scored violation.
An elementary recognition proof closes arbitrary coordinate relabeling as
a way to turn a rejected addition-support sector into one full convolution.
Eight focused tests pass, including all-bijection checks on 511 supports.
Full regression and archive replay are pending. Further R6 work needs a
stronger sector bound or a changed support/basis class. The all-size proof
is written and unreviewed; no exponent improvement is claimed.

The width-two support continuation is on
`research/continuation-01a1697b`, with its precise question in
`ai/2026-10-23-width-two-support/QUESTION.md`. An all-size graph argument
bounds the historical score for every support subset of C(2,b) and C(b,2).
The path deficit identity and two-hub equality classification are written
and unreviewed. This is distinct from PR118's exact finite-search ranking.
Do not rerun width-two weight searches with the same scoring rule to seek
a violation; use input dimensions at least three or a stronger sector
estimate. No improved exponent is claimed.

The [two-variable long-leg question](ai/2026-10-23-two-variable-long-legs/QUESTION.md)
is on `research/frontier-continuation-20261023` (PR179). The written
ordinary-map proof retains a common B window span and bounds the second
leg's coefficient-profile dimension, forcing quadratic repair when
r*s<m. Both long maps may vary. Six exact coefficient/rank controls pass over F2, F3 and F101;
focused and full regression are being completed; general full-profile maps and Laurent
cancellation remain outside the result. No exponent improvement.

The [variable shift-window proof](ai/2026-10-23-shift-window-long-legs/proof.md)
excludes ordinary fixed-width Q(n,m) repairs when one long leg has a
common coefficient-window span of rank below m and the other is Toeplitz:
its residual requires n^2-o(n^2) border rank under sublinear bandwidth and
exceptions. Arbitrary first-leg mixing is allowed. Exact finite controls
pass; the written proof is unreviewed. Full-rank B shift windows in Q(6,4)
with exact correction identities are the next constructive target. PRs
#145, #147 and #157 have separate scopes. No exponent improvement.

The unbalanced ordinary frontier continuation is in
`ai/2026-10-23-unbalanced-square-frontier/README.md`, branch
`research/unbalanced-square-frontier-20261023` (PR117). The complete
N<=1377 square-sum screen covers82 source formats and52310 dimensions;
only A(8,9) and A(9,9) survive the adopted gates. The later
[Wronskian application](ai/2026-10-21-hankel-wronskian-cap/application.md)
already excludes all improving ordinary A9 square direct sums. The saved
A9 survival is historical; the A(8,9) question remains distinct. The separate
single-rectangular continuation (PR138) leaves only three A(8,9) formats
and owns their stronger rank-two/rank-three parameter-image question.
The existing general Hankel pencil and constant-scheme workers retain
those proof scopes. No target maps or smaller exponent are supplied.

## One-slice seed audit: October 23

The standalone `research/one-slice-seed-20261023` continuation is recorded
in [the one-slice audit](ai/2026-10-23-one-slice-seed-audit/README.md).
The attributed external speedup gives actual structured degenerations
from powers of the existing Q(5,4) seed. A uniform ceiling shows that
one appended one-slice tensor and one-slice extraction leave the existing
endpoint scalar profile feasible, for every power and slice choice.
Repeating that unchanged scalar optimization is not a new route.
Multiple slices, successive extractions, other seeds and additional
tensor information remain open. Six focused tests and the metadata
checks pass locally. The [retained full regression](../results/one-slice-seed-audit-2026-10-23/validation.json)
records all 864 tests in 203 modules and five archive replays at frozen
commit `42360e9`, with no skipped tests. Three incomplete attempts remain
excluded and preserved. The proof is written and unreviewed; current-head
hosted CI and any later integration are separate from that full-run record.
No exponent improvement is claimed.

## Fixed-resolvent minimum rank: October 23

The [diagonal first-support follow-up](ai/2026-10-23-diagonal-first-support/README.md)
is integrated into `research/repair-support-capacity-20261023` and PR164,
from the validated support-capacity checkpoint `7690348`. It assumes only a fixed-polynomial
product on L(u u^T), allowing arbitrary diagonal-vanishing changes
off the diagonal and arbitrary ordinary long maps. The n=200,c=1
example requires first residual rank at least 176, or 188 for injective
diagonal factors. An exact joint kernel budget supplies the general
bound. All 37 [integration checks](../results/first-support-capacity-2026-10-23/diagonal-followup.json)
pass at `26f4fb8`; all 721 prior Python files are unchanged. The 879-test
combined inventory is not a fresh full-suite run. The proof remains
written and unreviewed. The
[question record](ai/2026-10-23-diagonal-first-support/QUESTION.md)
distinguishes the rank-only counterexample from an actual tensor map.
Next: a construction outside this diagonal class or a repair that
accounts for its permitted linear cost. Laurent families remain outside
the theorem; no smaller exponent is established.

The [repair-support checkpoint](ai/2026-10-23-first-support-capacity/README.md)
is on `research/repair-support-capacity-20261023`, from main `3008d70`.
The universal Laurent theorem bounds first-support repair from both
long-map annihilators. The separate ordinary fixed-polynomial first-map
theorem allows arbitrary long maps and requires at least 371 first
support for the n=200,c=1 example. Eight focused tests and the full
871-test regression at `66c4636` pass without skips; all five archive
replays match. The [validation receipt](../results/first-support-capacity-2026-10-23/README.md)
retains each complete group and its exact commit. The proofs remain
unreviewed. The [question and overlap record](ai/2026-10-23-first-support-capacity/QUESTION.md)
distinguishes PR157's finite-bandwidth Toeplitz long maps and PR142's
cyclic source loci. Next: an actual construction with a genuinely mixed
first map, or exact ordinary shared-kernel geometry outside the fixed-H
class. Generic long-map surjectivity does not extend the ordinary slice
obstruction to singular families. No smaller exponent is established.

The complete F8 subgroup continuation studies
`ai/2026-10-23-sl2-f8-subgroup-catalog/QUESTION.md`. Its exact386-subgroup,
12-class certificate closes the subgroup-averaging full-coset catalog for
the sixteen saved SL(2,F8) coordinate targets. New order14 cuts occur on
all48 target legs; order6 cuts also occur on ten. Further subgroup
enumeration in this source cannot add a minimal cut for these formats.
Next work needs stronger necessary conditions or actual constructions
outside the surviving filters. PR84 retains packet-assembly ownership.
Written and unreviewed; no general complex exclusion or smaller exponent.

## Exact rational monomial support ranking: October 23

The R6 continuation is on research/exact-rational-score-20261023,
draft PR118. Its maintained copy orders scores exactly and certifies the
retained leaderboard supports. All 242,668 candidates across the archived
binary, ternary, and seeded random scopes replay with zero score violations.
The archive remains unchanged. Local full regression and hosted CI are
pending; the result is finite and does not improve the exponent.
The [fixed-resolvent rank-six checkpoint](ai/2026-10-23-resolvent-minrank/README.md)
is on `research/resolvent-minrank-six-20261023`. Its exact certificate
settles the minimum matrix rank of the 112-dimensional limiting space
from PR103 and removes its generic-compression qualification whenever
the total rank-loss budget is at most five. Five focused tests pass,
including literal-source reconstruction and certificate tampering.
The next local question is whether a rank-six direction can satisfy the
required double-corank-one alignment and the higher Laurent equations.
Broader long-map results should be checked before using that question
as a target-construction route. The written proof remains unreviewed.

The October23 singular-long-leg continuation is in
`ai/2026-10-23-long-leg-rank-obstruction/torus_rank_sum.md`, on PR137.
The current deduction adopts PR129's sharp rank23 source-space cap and
requires normalized long-rank sum at most200. PR129 already bounds each
individual rank by101; the three extra pairs excluded here are recorded
explicitly. Search only within both conditions. At sum200 the leading
source cap becomes24 and a twelve-dimensional source space exists, so
the dimension-eight argument stops. Earlier simpler checkpoints are
preserved with their dependencies and concurrent-work credits. Complete
exact Laurent identities are still needed. The proofs remain unreviewed.

The singular-long-gap continuation studies
`ai/2026-10-23-singular-long-gap/QUESTION.md` on
`research/singular-long-gap-20261023`, based on PR113 at `08ac3e9`.
It extends the regular unit-kernel correction to rank-deficient long-leg
limits. The proposed minimum-rank-gap and polynomial-preserver proof
excludes limiting ranks106--109 in addition to110; the polynomial proof
includes fixed-row/column cases via the credited Flanders bound.
Exact witness controls and focused tests are being recorded before
full regression and integration. Claims remain written and unreviewed;
no exponent improvement is registered. The earlier PR110/119 target checkpoints
were closed as subsumed at the written-proof level by PR113.

The highest-pole continuation is on `research/pole-ruling-20261023`,
stacked on PR121, in
[the pole-flag package](ai/2026-10-23-unit-image-pole-flags/proof.md).
At regular unit-image rank106 the first map must be polar, with leading
image in a source ruling of dimension at most four. The complete principal
part has rank at least six. Its small-principal-rank argument excludes
ranks at most five at every pole order and rules out every simple first-map pole. At ranks102 through105
any polar first map has a fixed Hankel leading factor. Four focused,
18 metadata and three archive-integrity tests pass; these are necessary
highest-coefficient restrictions, not lower-pole or target solutions.
The underlying all-order source arguments remain written and unreviewed.

The next R6 continuation is `research/monomial-projections-19de7080`,
dependent on PR187. Its proof and exact acceptance program are in
`ai/2026-10-23-monomial-projections/`. Nonshared y/z coordinate projections
improve 581 of 1,623 binary scores through a+b=8, 1,817 of 4,197 through
a+b=9, and 6,486 of 24,699 ternary scores through a+b=8. Every maximum
ratio is one, with no exact violation; the finite scopes overlap.
Four focused tests pass, including all 64 supports of a 2-by-3 grid against
all coordinate masks and witness replay with the optimizer disabled.
This is a stronger estimate on old supports. Full regression and hosted CI
remain pending. Stacked draft PR200 targets PR187 until it merges.
General linear mixing and exponent improvement are open.

The R6 continuation on `research/monomial-recognition-19de7080` studies
`ai/2026-10-23-monomial-recognition/proof.md`. Its monotone-path argument
proves complete whole-convolution recognition under coordinate permutations
for additive coefficient-one supports. Six focused tests include all 63
nonempty 2-by-3 supports against brute-force coordinate permutations, all 511
nonempty 3-by-3 supports against the archived recognizer, and an exact
input-orientation counterexample. Complete ordered censuses check 24,708
binary and 370,252 ternary candidates with no score above the source profile.
All five archive replays pass; the full regression is running. PR187 is a
draft until validation is complete. PR118's maintained exact ranking retains
its separate ownership and credit. Stronger proper restrictions and general
linear bases remain separate questions. No exponent improvement.

The October 23 singular-long-rank continuation is in
`ai/2026-10-23-singular-long-rank/proof.md` on
`research/a4-singular-long-rank-20261023`. It excludes a scalar-balanced
long-map rank of 106 or higher, without restrictions on the other
Laurent poles or the target-unit lift. The regular kernel correction
is credited to PR113; the new step combines the source rank gap with
injectivity on an active target ruling. Four focused tests pass.
The original rank105 boundary reaches rank20 source slices; the later
rank23 source-space cap above now excludes it. Full regression and archive replay are required before this
submission is ready to merge. The claim remains written and unreviewed.

## Paired repair continuation: October 23

The active branch `research/operational-repair-20261023` and PR130 contain
the external formal-calculus repair barrier and the conditional finite and
asymptotic residual-rank criteria. The actual tensor-map question remains
open. Construction searches focus on nonproduct long maps and small
first-leg residual support; neither finite arithmetic nor the formal
monotones provide an improving tensor map. See
`ai/2026-10-23-residual-rank-repair/proof.md` for exact stopping criteria.
The coordinated agents in this session are not independent reviewers.

All 875 local tests and all five archive replays passed at `121be1c`, with
no optional skips. See `../results/paired-repair-2026-10-23/validation.json`.
Main commit `3008d70` is integrated with all earlier Python files unchanged;
its five new tests and eighteen repository/profile/support checks pass. See
`../results/paired-repair-2026-10-23/main-integration.json`. Current-head
hosted checks are pending. The separate
[PR147](https://github.com/1337isnot1337/matrix-mult-bounds/pull/147)
records the fixed-product-map residual minimum and an exact changed
decoder with a nineteen-scalar ordinary repair and an eighteen-scalar
formal degeneration from Q(6,4) to M(5,4,5). Its small correction core has
ordinary rank seven and border rank six; full-residual optimality is open.
That small construction does not pass the finite exponent gate. Continue
with new long-map geometry or certified residual structure; do not repeat
the unchanged formal-parameter optimization or fixed-map rank census.

The coordinate-kernel continuation is in
`ai/2026-10-23-coordinate-kernel-cap/QUESTION.md`, branch
`research/coordinate-kernel-cap-01a1691e`. An exported complete8008-subset
matching certificate closes the sixteen mixed high-rank pairs when both
regular constant kernels are coordinate. The third Laurent map and all
higher regular jets remain arbitrary. Written and unreviewed; arbitrary
complex leading kernels are now covered by the separate written source-torus
transfer. Every pair of balanced leading ranks has sum at most192; lower
rank triples and the target remain open.

The two-regular-leg continuation is in
`ai/2026-10-23-regular-leg-frontier/QUESTION.md`, branch
`research/regular-leg-rank-frontier-01a1691e`, PR122. The written source
compression bounds force the two regular long limiting ranks to sum to
at most192. A standalone mixed screen leaves sixteen high-rank pairs,
separate from concurrent one-regular-leg exclusions. The proofs are
unreviewed and no target or exponent gain is claimed.

The binomial supporting-chart continuation is on
`research/hankel-additive-cost-20261023`, with the question in
`ai/2026-10-23-hankel-additive-cost/QUESTION.md`. It supplies a written
unreviewed exact minimum over all polynomial initial moments of
f_(k+r)=xz*f_k, using residue-key ranks and a diagonal weight limit.
The general additive inequality for other primitive-degree-(1,1)
supporting forms remains open. The source packages of PR134 are frozen
for their separate required checks. No exponent improvement is claimed.

The deficient-symbol kernel-descent continuation is on
`research/hankel-equality-20261023` (PR115), with its question in
`ai/2026-10-23-hankel-equality/QUESTION.md`. Its written unreviewed
pointwise strip is separate from all matrix-parameter family claims.
The supporting-degree follow-up is on
`research/hankel-annihilator-degree-20261023` (PR134). It counts both
inner ranks exactly, widens the pointwise strip, and separates its
unproved additive-cost question from the proved maximum bound.
Ordinary A9 square sums were already excluded by the Wronskian
application; those exclusions retain their prior credit.

The [mixed-output candidate is excluded](ai/2026-10-23-mixed-longlegs-candidate/global_rnc_obstruction.md)
by a written global RNC argument, including arbitrary singular first maps,
polar or mixed long maps, and independent target first identifications.
All ordinary Koszul degrees and the stated Schur family still pass; do
not repeat them. Third conciseness and the finite union of target quartics
force a smooth source-curve limit, allowing first-map normalization and
the120<130 catalecticant contradiction. The canonical target also has
ordinary, smoothable and cactus rank178; its border rank is unresolved.

The next question is to escape the finite-quartic projection condition.
Width-one Full blocks or a different target structure can change that
geometry, but they must still satisfy the exact score, dimension and rank
conditions. Current work checks how many such blocks are needed and
whether the present source format has enough score capacity. Keep the
candidate exclusion separate from any broader unproved class barrier.

The sharp-kernel continuation is in
`ai/2026-10-23-paired-kernel-onset/proof.md`, worktree
`/tmp/matrix-paired-kernel-01a168f9`, branch
`research/paired-kernel-01a168f9`. It continues PR169 without changing its
worktree while the full local regression runs. A written all-field proof
gives a fixed-short-input kernel formula and makes the full-column
endpoint sharp for every a. A cokernel Euler formula isolates the exact
intermediate-rank gap as H^1 of the kernel bundle. Six focused tests pass, including 45
independent source kernels at a=3 and all 25,254 target-bound comparisons.
The screen leaves all 28 matrix targets unresolved. Next: coupled short
directions and bounds on this H^1, including the extension maps. Do not
count the fixed-input lower bound as a complete source kernel formula.

The paired-long-leg continuation studies
`ai/2026-10-23-paired-bundle-injectivity/QUESTION.md`, in the isolated worktree
`/tmp/matrix-paired-bundle-01a168f9`, branch
`research/paired-bundle-01a168f9`. A written all-field proof gives
full column rank for 0<=p<=a(a-1) on both long legs with short input.
Those degrees cannot exclude any padded target. The remaining question
is a(a-1)+1<=p<=a(2a-1)-a-1 and whether it excludes any of the 28
short-leg survivors through a16. Above that interval the map has full
row rank; the proof also bounds its kernel in every degree. The explicit
a2,p3 integer kernel rules out extending full
column rank to every degree. Modular source ranks remain lower bounds,
not complex source upper bounds. This is separate from active singular-
unit, group-source and boundary work. No smaller exponent is established.

## Rank20 ruling continuation, October23

PR142 on `research/rank20-ruling-20261023` owns
`ai/2026-10-23-rank20-ruling/QUESTION.md`, continuing PR125. A written
rank20 quadratic-factor classification gives a sharp source linear-space
bound eight and extends the singular-long criterion to balanced leading
rank105. Its all-size continuation gives dimension2a at cap a^2+a for
every a>=2, with the same stated external dependency and selected controls.
The next A4 cap21 is not covered. Exact controls and34 integrated focused
tests pass. Full hosted regression at610f2a9 passes on Python3.10 and3.14,
with three optional skips per version; all five archive replays pass.
The receipt is in `results/rank20-ruling-2026-10-23/validation.json`.
PR142 includes the full PR125 package for combined integration. Earlier
local full runs were interrupted by reboot; final-head CI remains required.
No independent review, formalization, target construction or exponent gain.

## Singular long-leg ruling continuation, October23

PR125 on `research/singular-long-ruling-20261023` owns
`ai/2026-10-23-singular-long-ruling/QUESTION.md`. The shared rank-two
correction column space and prior source gap give a written exclusion
whenever either balanced long-map limit has rank at least106, with
arbitrary poles in the other maps. It adopts and credits concurrent
PR113's regular correction mechanism, extending its full-rank premise.
Exact controls and complete validation are in progress. The next bound
would require linear-space geometry at source rank20; the minimum-cone
argument is not asserted there. No exponent improvement or independent
review. Older unit-image rank thresholds below are historical method
boundaries, not the frontier after these continuations.

The divisor-source-cap continuation studies
`ai/2026-10-23-divisor-source-caps/QUESTION.md` on
`research/divisor-source-caps-20261023`, isolated on main `3008d70`, retaining PR129 at `9eca895` as method credit.
It generalizes the torus coordinate method to every proper divisor d
of every balanced source size a: the proposed sharp dimension cap is
ad throughout rank ceilings a(a+d-1),...,a(a+d)-1. Divisor cycles and
a d^2-fold residue decomposition supply the upper bound; a d-row strip
attains it. All110 exact minors,330 residue identities and60 divisor
strip controls pass. The exact nondivisor pair limit is also recorded; final regression evidence is pending. This is distinct
from the owned A4 rank24 and joint-rank
frontiers and claims no new A4 cutoff or smaller exponent.

The asymmetric-boundary continuation studies
`ai/2026-10-23-asymmetric-boundary/QUESTION.md`. The nonzero rank-four
conditioned branch forces the smaller first span to be H tensor C2.
Both joint supports of every non-plane joint-zero core are at least three;
a sharp one-sided zero-or-four gap excludes that entire joint-zero branch
from the12-by8 target third-rank ceiling. Next: classify the rank-two locus
of the42-by6 conditioned matrix M and construct its actual third tensor.
The conic-lifting investigation remains with its active worker. These are
written, unreviewed reductions; the full asymmetric case and exponent
improvement remain open.

The equalizer follow-up is integrated into PR147 from `2c1e026`. Its
[receipt](../results/oblique-repair-2026-10-23/equalizer-followup.json)
records 35 focused and repository checks, all seven new tests, unchanged
earlier Python files and standalone certificate replay. The 910-test
combined inventory does not relabel the earlier full regression.

The [equalizer follow-up](ai/2026-10-23-oblique-border-equalizer/README.md)
is on `research/oblique-border-equalizer-20261023`, based on the frozen
`49904d7` integration below. It proves border lower bound `2r+2` for the
fixed one-dependency residual and improves the n=6 interval to twelve
through eighteen. Seven new standard-library tests check all eight
controls, four source hashes, the unit240 minor and full native identity.
The earlier implementation and test files remain byte-identical. This
is an incremental check, not a new complete-suite run. Claim
`AI-OBLIQUE-BORDER-EQUALIZER-001` is written and unreviewed; optimal
border rank and better source maps remain open.

PR147 now combines the paired ordinary and border constructions, the exact
full-residual ordinary-rank proof and the scoped long-map frontier on
`research/oblique-border-repair-20261023`. Main `3008d70` is integrated.
The [validation record](../results/oblique-repair-2026-10-23/README.md)
retains complete frozen runs of 871 and 884 tests, all five archive replays
at each checkpoint, and 63 integration checks at `aeafc7b`. All nineteen
added tests pass; the 903-test combined inventory is not a new full-suite run.
Incomplete attempts are retained and excluded. Current-head hosted CI is
still required. The following branch notes retain their original scope.

The [full-residual ordinary-rank follow-up](ai/2026-10-23-oblique-border-repair/full_residual_rank.md)
is on `research/oblique-full-ordinary-rank-20261023`, based on `b6c38513`.
It proves ordinary rank `4r-1` for the fixed residual when `n=b+2`,
so the full n=6 residual has ordinary rank nineteen. Horizontal and
vertical support projections each force `2(r-2)` terms, leaving the
core of rank seven. Seven focused tests cover eight exact family
controls, unit support minors, the native exported source maps, unchanged
source hashes and negative certificates. The previous implementations
and tests remain unchanged. Claim `AI-OBLIQUE-FULL-ORDINARY-RANK-004`
is written and unreviewed. Optimal full-residual border rank and better
source maps remain open.

The [long-map frontier checkpoint](ai/2026-10-23-oblique-longmap-frontier/README.md)
is on `research/oblique-longmap-frontier-20261023`, based on `b6c385`, for
the existing paired-repair PR. A surjective Q(6,4) benchmark attains first
residual nine. An all-field unit-minor proof gives lower bound nine for
every first map and arbitrary added-row fillers with the good rows fixed;
it does not assert equality for every filler choice. Separate finite
coverage consists of 384 inner-dependent shift controls and 61 exact,
injective mixed-middle corners, plus 20 singular modular controls.
Seven focused standard-library tests cover all saved records, five source
pins and tamper cases. Keep the universal fixed-row scope distinct from
the finite screens. General changed long maps and Laurent constructions
remain open. The earlier implementations, scalar costs and review statuses
are unchanged.

The subsequent [border-repair continuation](ai/2026-10-23-oblique-border-repair/proof.md)
is on `research/oblique-border-repair-20261023`, based on the ordinary-map
checkpoint `53fed211`. A six-term polynomial core has leading coefficient
exactly K and a matching unit Koszul minor. It supplies the complete
degeneration `Q(6,4) + D_18` to `M(5,4,5)`, while the nineteen-term
ordinary correction below remains unchanged. Disjoint cores give border
cost `4rd-2min(d,b-1)^2`. Seven focused tests cover all seventy-two saved
family controls, all four source hashes, full native polynomial maps and
negative certificate controls. The result is written and unreviewed;
the whole residual's optimal border rank remains open. Construction of
changed maps with substantially smaller first support remains the main
asymptotic question.

The same branch now includes a separate
[ordinary-rank proof for the core](ai/2026-10-23-oblique-border-repair/ordinary_rank.md).
Explicit quadratic kernels and their cubic factor identities leave only
two six-term support patterns, both excluded over every field. Thus the
isolated core has ordinary rank seven and border rank six. Six additional
focused tests replay the finite proof inputs and reject false records.
Claim `AI-OBLIQUE-CORE-RANK-SEVEN-003` remains written and unreviewed.
The separate follow-up above uses two specific support splittings to
prove full-residual ordinary optimality in the one-dependency family.
No general additivity for embedded cores is asserted. The source maps
and four pinned files are unchanged.

The October 23 paired-map continuation is on
`research/product-longmap-residual-20261023`, based on main `fe602e4`.
Its [oblique construction](ai/2026-10-23-oblique-paired-repair/proof.md)
changes the long maps and gives `Q(6,4) + D_19 -> M(5,4,5)` over every
field. The actual residual has ranks `(9,11,11)`; all nineteen rank-one
terms and complete coefficients replay exactly. A separate nonproduct
middle-space control has its own twenty-four-term certificate. Seven
focused tests cover these constructions, their all-size formulas and
invalid-input controls. The near-full fixed-width family still has
quadratic first support; no smaller exponent follows. Pending PR130 is
pinned only for endpoint cost comparisons and is not a local replay
dependency. The next constructive questions are smaller scalar repairs
and changed map families with subquadratic first support.

The companion [all-size proof](ai/2026-10-23-product-longmap-residual/README.md)
allows an arbitrary first map while retaining both old product long maps.
The exact minimum first residual rank is
`(n-1)^2-max(9-n,1)^2` for every `n>=5` in characteristic different from
two. Six focused tests pass, including direct rational paired ranks
through `n=12` and at `n=16`, larger one-factor controls, and finite-field
checks. Both packages remain written and unreviewed. The oblique decoder
demonstrates the importance of the fixed-long-map hypothesis: at n=6
the old maps force minimum first residual rank sixteen, while the new
maps attain nine. No unrestricted tensor obstruction or smaller exponent
is established.

The paired-long-leg continuation is on
`research/paired-long-legs-20261023`. Its written, unreviewed result proves
both long-leg Koszul maps injective for `0<=p<=a`, by exact interpolation,
the full-spark evaluation basis, and a two-block compatibility argument at
`p=a`. At every degree the same proof gives a rank floor from wedges using
at most `a-1` interpolation blocks. At `p=a+1`, it dominates both target
long-leg ranks for four `a=15` and six `a=16` survivors, but neither rank for
the other survivors. A finite exact atlas for `a=3` is injective through `p=6`
and has rank `57185/57915` at `p=7`. The general higher-degree ranks remain
open. A further exact bidegree control has full rank modulo two at `(a,p)=(4,5)`
across 524 blocks; it is a finite check only. The first kernel defects at
`(a,p)=(2,3)` and `(3,7)` have exact `SL2 x SL2` decompositions that fit the
conjectural boundary `p=a(a-1)+1`; the `(3,8)` kernel has dimension 3,780.
The exact `a=3` atlas is complete through `p=14`; the `a=4` boundary remains
untested.
Modular source ranks are lower bounds, not complex source upper
bounds. This is separate from active singular-unit, group-source and
boundary work.

The rank84/88 source-cap continuation is in
`ai/2026-10-23-rank84-88-source-caps/QUESTION.md`, branch
`research/rank84-source-cap-01a1691e`. Exact acceptance verifies all1404/118
remaining ideals and sharp caps56/60, improving the balanced long sum144
to136. This follows PR129 and PR155 with retained credit. The next gap is
actual two-sided kernel incidence: the prior64-dimensional rank88 source
space meets the two numerical conditions at68,68 but is not a kernel
construction. Written and unreviewed; no target or exponent gain.

The next source-frontier checkpoint is in
`ai/2026-10-23-rank37-source-spaces/proof.md` and
`ai/2026-10-23-source-staircase-spaces/proof.md`. A sharp cap of 16 now
holds strictly below rank 37. An explicit 68-space of rank at most 92
rules out the proposed cap 57 below rank 96. Do not repeat that premise.
Twelve focused tests cover all thirteen size-17 minors, the coherent
rank-20 witness, and all 140 finite staircase controls. The all-size
staircase statement has a separate counting proof. This checkpoint
follows PR129; its target sum144 was the bound at that checkpoint.
Later integrated source-space caps give further scoped restrictions. The sharp
rank-80 cap above resolves that source question. Further work may use
actual compression-kernel structure. Claims remain written and unreviewed.

The rank-80 continuation in `ai/2026-10-23-torus-rank80/proof.md`
now proves source-space dimension at most 50 below slice rank 80 and the
necessary balanced long-rank sum 144. All 35 integer minors, the complete
24-ideal size-51 inventory, 112 literal block factorizations and 12321
rank-pair controls pass; all 2926 pairs above 144 are excluded, including
1096 newly excluded pairs in sums 145 through 160. Eight focused tests
and a separate internal exhaustive audit pass. Neither bound is claimed
sharp. Freeze PR129 at this checkpoint for final integration and current
CI. Subsequent work may seek a cap at rank 96 or stronger support bounds
inside the remaining region, in a separate investigation. All claims
remain written and unreviewed, with no constructed matrix target.

The order-ideal continuation in
`ai/2026-10-23-torus-order-ideal/proof.md` proves the sharp source-space
cap32 below slice rank64 and the necessary balanced long-rank sum160.
Its reusable lowering lemma permits finite order-ideal certificates at
other rank thresholds. Eight focused tests pass; acceptance independently
enumerates all611 size33 ideals, rebuilds all4096 source terms and checks
all336 integer lowering identities and611 odd64-minors. All1830 integer
rank pairs above160 are excluded, including840 newly removed pairs in
sums161 through176. Next: larger-rank source spaces and constraints inside
the remaining target frontier. Full regression and current-head CI are
still gates; mathematical claims remain written and unreviewed.

The rank-48 continuation in `ai/2026-10-23-torus-rank-frontier/proof.md`
now proves source-space dimension at most24 below slice rank48. The
credited saturated support inequality then gives balanced long-rank
sum at most176, retaining PR122's prior sum192 attribution. Combined
with the individual rank102 exclusion, any candidate has both ranks
at most101 and sum at most176. Eight new focused tests pass; exact
controls enumerate all12321 rank pairs and exclude all990 above176.
No sharpness or construction at the surviving boundary is claimed.
Next: larger low-rank source spaces or additional support constraints
within the remaining frontier. Full regression, archive replay and
current-head CI remain merge gates; all proof claims are unreviewed.

The torus follow-up in `ai/2026-10-23-torus-low-rank/proof.md` strengthens
the singular-long result: arbitrary complex source subspaces of slice
rank at most23 have dimension at most8, so remaining scalar-balanced
long-map ranks are at most101. The rank24 threshold permits a literal
12-plane and needs a different argument. Eight focused tests pass across
the two packages. PR129 carries both checkpoints; full regression and
historical replay remain the merge gates.

## External-seed double-leg follow-up

The [two-stage anchor package](ai/2026-10-23-double-leg-anchor/README.md)
is based on PR162 (which depends on PR154 and PR128). Four additional
two-W after eleven-U/two-W split variants each contract all fifteen
discarded tensor products under the inherited one-parameter physical
family. The 76 survivors have 65/76/54 factor directions. All variants
pass the previous U and W weighted inequalities, including equality
144=9*16 for the stronger W weights. Nevertheless all four fail the
actual nine-flat W cover: the unchanged zero-weight W35 has maximum
weight15 among 23426 possible anchor-plus-three finite-field spans.
This is a complete scoped static-cover exclusion, not a complete
source-map exclusion. Next: a physical family removing or changing
W35, an actual nine-cover and simultaneous source maps; do not repeat
the now-closed four W-substitution variants. Written unreviewed;
omega remains at its prior bound.

The next external-seed checkpoint is on
`research/mixed-leg-error-20261023`, following PR154 and incorporating
main `3008d70`. The `ai/2026-10-23-mixed-leg-splits/README.md` package
gives eleven U and two W replacements, 89 exact expanded terms and
76 surviving border terms with direction counts 65/76/56. Full Laurent
replay checks 10000 constant positions and all 506 positive coefficients.
The seed passes the prior U and W weight inequalities (214<=216 and
141<=144). Its new static W weighting has total 152 and rank-four cap 16,
verified over 367290 four-subsets, so its present directions still need
ten groups. This does not close flips or refactorizations of the new seed.

The same branch's `ai/2026-10-23-quadratic-error/README.md` supplies complete-error power
trace tests. Every one-term deletion from a minimum refactorization of
the named ten-split five-term block is excluded, including Laurent
coefficients. Two specified V69 families are also excluded. Do not treat
individual nilpotence or trace zero as a complete deletion certificate:
the sum with the original error must contract. New factor configurations
and full source maps remain the construction questions; no smaller
exponent is established.

The October 23 external-seed continuation is in
`ai/2026-10-23-flip-escape/ACTIVE.md`, on PR128's
`research/flip-escape-20261023` branch. Two exact split border seeds have
76 terms and 72 or 71 distinct U directions. Their finite standard-flip
components are now excluded from the specified termwise Q(6,4) grid:
50 fixed W directions already require ten rank-four groups. The
five-split component also has a positive trace obstruction to any further
nonempty-subset stabilizer deletion. Do not repeat standard flip walks
on those two seeds aiming at that grid. A broader per-term factor-gauge
test now gives an exact six-split seed with 70 U directions in
`ai/2026-10-23-gauged-splits/README.md`. Its discarded tensors contract
even though a mixed trace prevents common contraction of the unscaled
arrows. The new component has 47 permanent W directions with an exact
nine-group rational cover and a matching weighted lower bound in
`ai/2026-10-23-six-split-grid/README.md`. The follow-up branch
`research/gauged-batches-20261023` proves in
`ai/2026-10-23-six-split-mobile-obstruction/README.md` that its mobile
planes cannot fit any saturated nine-space cover. Do not repeat finite
flip searches on this six-split seed for that grid. The same follow-up
exports ten- and eleven-split witnesses in
`ai/2026-10-23-large-gauged-batches/README.md`, with 66 and 65 U directions.
The eleven-split seed passes the prior weighted U inequality; the ten-split
seed has exact cross-component span contacts. Neither fact constructs
cross-component moves or source maps. Next: actual decomposable factors
in component flattening images, replacements on other legs, and full
Laurent replay of useful refactorizations. No maximum split-batch theorem,
general source-map exclusion, new rank record, or smaller exponent is
established. The follow-up depends on PR128; accepted certificates there
remain unchanged.

The current general A4 leading-rank bounds are total at most 198,
mixed pair sums at most 133, and long-pair sum at most 136, from
`ai/2026-10-23-rank91-core/proof.md`. If the short leading rank is
100, `ai/2026-10-23-high-rank-source-caps/proof.md` further restricts
each positive long rank to 1 through 12 or 20. These are necessary
conditions for complete Laurent presentations, with no target
construction or sharp-target assertion. The total-202 package is a
credited historical screen; its former endpoint is excluded. The
source cap 67 strictly below rank 91 is not claimed sharp; the
distinct cap 68 strictly below rank 92 is sharp. All claims remain
written and unreviewed.

The projective conic question is closed for normal-class existence by
`ai/2026-10-23-conic-projective-criterion/proof.md`, on branch
`research/conic-projective-global-20261023`. Every point of the three
projective base lines has ranks 14, 14 and 12 and tangent dimensions
68 plus 2. A nonzero normal class lifts exactly when
`(a1*r-a0*s)*(b1*r+b0*s)*(s*lambda^3+r*mu^3)=0`, allowing a suitable
first boundary velocity. Source reversal transports the class by
`[lambda:mu] -> [mu:lambda]`. The liftable set has exactly three
irreducible graph components; no extra component comes from infinity.
This is a set-theoretic statement, not a full incidence-scheme claim.
All three missing curvature strata and all eight polynomial families
replay, with seven focused tests passing. The affine criterion remains
a correct scoped prerequisite. This checkpoint awaits its dedicated PR
and integration gates; do not repeat the closed chart-coverage task.
Prescribed boundary velocities, the remaining local moduli and the bridge
to a full matrix target are distinct questions. Claim
`AI-CONIC-PROJECTIVE-CRITERION-001` remains written and unreviewed, without
independent mathematical review, formalization or an exponent gain.

The high-threshold source continuation is
`ai/2026-10-23-high-rank-source-caps/proof.md`, on isolated branch
`research/a4-high-rank-source-caps-20261023`, based on frozen PR176
at 658e2d5. It proves sharp caps 84/88/92/96 strictly below source
ranks 100/104/108/112, with exact staircase ranks 96/100/104/108.
At full short leading rank 100, each positive long leading rank must
lie in {1,...,12,20}. The numerical endpoint (100,20,20) is not a
target construction. Complete literal-source, profile, minor and
full-short integer controls are exported in the new result directory.
All five claims remain written and unreviewed.

This work preserves every file in the total-202 and rank-92/rank-96
packages. The rank91 source proof has separate prerequisites and is also
integrated here; its global198/mixed133/long136 bounds remain current.
The current source maxima cannot be lowered at the same strict
thresholds; future work must use other thresholds or extra structure
of actual cancellation kernels. Entries below retain earlier checkpoints.

The current A4 target refinement is
`ai/2026-10-23-rank91-core/proof.md`, frozen at
`36d0eb145ae9e8619e1a03376b367576fb3b7210` on isolated branch
`research/a4-rank91-core-20261023`. It proves mixed balanced pair sums
at most 133, retains the long-pair bound 136, and bounds total balanced
leading rank by 198. At short rank 100, the high-threshold continuation restricts
each positive long leading rank to 1 through 12 or 20. The source theorem gives dimension at most 67 when
every slice has rank strictly below 91; this cap is not claimed sharp.
Four equality profiles reduce to eight strip ideals, each containing
one common 56-coordinate rank91 core or its transpose.

The complete censuses cover 20,706 pairs and 1,050,804 triples. They
retain every frozen202 exclusion and remove 60 additional pairs and
5,250 additional triples. The only total-198 numerical survivors are
(62,66,70) and (62,70,66), with no target construction or target-sharpness
claim. Eight focused tests, nine metadata/archive tests and standalone
exact acceptance pass. Their receipt and frozen-byte comparisons are
in `results/rank91-core-2026-10-23/validation.json` at repository root;
this focused validation does not claim a full-suite or hosted-CI run.

The unchanged `ai/2026-10-23-leading-rank202/proof.md` is a credited
prerequisite, frozen at commit `658e2d54fa7b506f7d8fd51eeec7788f23a00e91`.
Its all-order support arguments, every-pair136 prerequisite and exact
floor constraints remain in force. The former total-202 endpoint
(70,66,66) is excluded by the new strict rank91 source theorem.

The next actual compression question is unproved. At either surviving
total-198 endpoint, the long pair (66,70) requires a cancellation kernel
of dimension at least 64 and uniform slice rank at most 88, with split
compression defects (46,42). An existing 64-dimensional staircase has
uniform rank at most 88, so a universal source cap below 64 cannot
settle this pair. Determine whether any such space satisfies that
specific split compression condition, using an incidence-preserving
reduction and row/column cover certificates if useful. No classification,
exclusion of all possible kernels, or target realization is claimed.

The unchanged source package
`ai/2026-10-23-rank92-rank96-spaces/proof.md` settles sharp dimensions
68 below rank 92 and 72 below rank 96, with maximum ranks 91 and 95
attained by its explicit spaces. Together with the prior sharp caps
56 and 60 below ranks 84 and 88, these close the corresponding universal
source-dimension questions. Do not propose smaller caps at those same
strict thresholds. Further progress must use other thresholds, extra
compression-kernel structure, or a complete target construction.
All new claims remain written and unreviewed. The projective conic
package in PR168 stays separate and frozen. Entries below preserve
earlier investigation checkpoints and their credited results.

The sharp rank-80 checkpoint is in
`ai/2026-10-23-rank80-sharp-spaces/proof.md`: the maximum source-space
dimension is exactly 44 when every slice has rank below 80. All 1,709
size-45 ideals are excluded by saved integer minors, and the explicit
44-space has maximum rank 79. Six focused tests pass, including all
1,721 minors and the fixed support cover. Do not seek a smaller universal
dimension cap at this threshold. The separate target-leg application
must prove its own saturated support inequality and exceptional endpoint
case before claiming a stronger target frontier. This package follows
PR129 and remains written and unreviewed.

The October 23 nonsplit continuation is in
`ai/2026-10-23-nonsplit-vector-covers/ACTIVE.md`. Exact source parity and
seven cover replays pass; 3372 primitive weight vectors give no gain over
6155844. This is a bounded finite outcome, not a class-optimality proof.
Do not repeat the unchanged census.

The October 23 joint-target continuation is in
`ai/2026-10-23-central-cover-joint-frontier/ACTIVE.md`. A new exact
1012332-slice nonsplit cube cover closes every strict improving target
in the stated one-matrix-plus-scalars one-copy coordinate/potential
family. Further work must change that target family, maps or source power.

The stacked-product continuation studies
`ai/2026-10-23-unit-image-stacked-rank/QUESTION.md` on
`research/unit-image-stacked-rank-20261023`, based on PR110's rank107
package. A combined regularized product sharpens3q to2q; a rank-one
kernel bound permits a noninjective first limit. The written argument
reaches unit-image rank105, with rank104 outside the strict first-pole
estimate. All48 exact block controls pass; regression checks are pending. No general
A4 exclusion, independent review or exponent improvement is claimed.

The unit-image rank-gap continuation studies
`ai/2026-10-23-unit-image-rank-gap/QUESTION.md`, from main `1c04903` on
`research/unit-image-rank-gap-20261023`. Its written argument uses the
existing below-rank32 source classification in place of the partial-unit
theorem's row-kernel dimension count, extending the retained-image
threshold to107. Varying retractions supply first-map injectivity.
Rank106 is outside the first-pole estimate. Exact finite controls pass;
the regression suite is pending and both new claims remain unreviewed.

The partial-frame continuation studies
`ai/2026-10-23-partial-regular-frames/QUESTION.md` on
`research/partial-regular-frames-20261023`. Its written proof allows
poles in the unselected long-map and unit coefficients, provided two
109-column regular frames survive. A new column-contraction dimension
bound forces the last long map regular. All four strict margins are
positive at109 and the two dimension margins become equality at108.
Exact finite controls, all853 local tests (three optional skips) and all five archive replays pass; final combined-head hosted CI is pending.
The frames are hypotheses, not a general degeneration classification.

The partial-unit-image continuation studies
`ai/2026-10-23-regular-unit-image/QUESTION.md` on
`research/regular-unit-image-20261023`. The written all-order argument
compresses to 109 independent unit-image directions and recovers the
entire long map through varying left inverses. It replaces an invertible
A4 unit by `rank(S(0) C(0))>=109`, including corank-one unit slices.
Exact matrix controls, all849 local tests (three optional skips) and
all five archive replays pass. PR105 merged at1c04903 after final-head CI;
the proof remains unreviewed. Rank108 is an equality boundary of this
method. Singular long-leg limits and polar units remain open; no general
degeneration or exponent claim.
This is the historical PR105 validation receipt. The later one-sided,
one-regular-leg, and source-cap results supersede its open rank thresholds
without altering that recorded test evidence.

The pure-fiber continuation on `research/conic-pure-criterion-20261023`
studies `ai/2026-10-23-conic-pure-criterion/QUESTION.md`, depending on
mixed-component PR107 at `752d51d`. It certifies an exact polynomial
curve on c=d=0 for every a,b. Combining that pure fiber with the mixed
family and old linear components gives the complete third-order
normal-class criterion, identical to the order-two criterion. Next:
mixed fourth-order compatibility and a possible all-order mixed lift.
The 14-row incidence remains distinct from the full matrix target.

The one-sided unit-image continuation is published in PR121 on
`research/verified-frontier-20261023`, from main `1c04903`.
Its [written proof](ai/2026-10-23-one-sided-unit-image/proof.md) strengthens
regularity to `rank(S(0) C(0))>=107`, retaining a regular full-rank long
map and regular identity lift. All target rows are kept and the final
kernel count uses the original long map. Five focused and18 metadata
tests pass, as do all five archive replays. Current-head hosted full
regression is pending; the prior interrupted local full run is not a
completion claim.
This supersedes the earlier rank108 equality boundary of the partial-unit
method, without changing the prior pinned proof. The later one-regular-leg theorem supersedes this unit-image threshold;
subsequent singular-long-rank and source-cap results refine the remaining
singular case. No exponent improvement
or independent mathematical review is claimed.

The S5 staircase continuation is on `research/s5-staircase-cover-boundary-20261023`,
stacked on PR111. Its `ai/2026-10-23-s5-staircase-covers/` package exhausts
891888 monotone first-leg thresholds with two equal legs; all eight costs
match the weighted cube covers. For r=1, the three-unequal-leg census now
accounts for all77392758 threshold pairs and retains the same bound; seven
focused tests pass, including separate compiled replay. Finer source support
and nonmonotone covers are separate next questions. No exponent improvement.

The S5 finite-cover continuation is on `research/s5-finite-power-covers-20261023`
(PR111), with its question and exact proof in `ai/2026-10-23-s5-finite-covers/`.
Separate weights give actual-source cube bounds 6867542 and 42493572 for
S5 x C2 and S5 x C2^2, excluding 38 additional frontier shapes, including
the selected one-copy M19 coordinate target. M(13,14,14) remains open. Five focused
tests, all five archive replays and every hosted regression group at e16c7e3
pass. The local full-suite run was interrupted without a completion receipt;
final integrated-head hosted CI remains the merge gate. All claims are written and unreviewed,
with no arbitrary-complex or higher-source-power exclusion or exponent gain.

## Actual nonsplit finite covers: October 23 continuation

Main and all open PRs checked at `d833eb0`. The owned
`research/sl2-finite-slices-20261021` branch finishes the actual nonsplit
source question in `ai/2026-10-21-sl2-finite-slices/ACTIVE.md`.
The independent dense-field certificate gives a 98-slice cover for
SL(2,F5) and a 6155844-slice cube cover for SL(2,F5) x C2, excluding
the selected M10 and M(13,13,15) targets in the stated characteristic-two
and one-copy coefficient-one coordinate/potential class. The retained
844-test regression and archive replay passed again at exact commit
`6cd7f3a`; PR102 integrates conic main `539b539` with both claim sets
retained unchanged. Claim `AI-NONSPLIT-FINITE-COVERS-001` remains written
and unreviewed. Higher source powers and general complex input mixing
remain open. No smaller exponent is established.

The affine-conic continuation studies
`ai/2026-10-21-conic-second-jets/QUESTION.md`. The complete tangent module
has dimension70:68 independent boundary fields and two conic normals.
The full second-order criterion for a nonzero normal class is
`(a-c)*(b+c)*(c*lambda^3+mu^3)=0`, allowing a suitable boundary velocity
and moving source kernel. A polynomial two-jet on c=-d^3 is exported;
its uncorrected third coefficient is nonzero. The later polynomial
curve above establishes all-order existence after changing boundary
velocity. Keep this14-row local incidence distinct from the full matrix
target and from fixed lower-jet extension. The projective base coverage is
now supplied above; the separate 12-by-8 case remains open. Written,
unreviewed, no smaller exponent.

The singular-unit continuation studies
`ai/2026-10-21-singular-unit-resolvent/QUESTION.md`, resumed at main d833eb0.
The fixed rank-16 square-zero resolvent with constant PC=I110 is excluded
for every Laurent first map when its candidate limiting-space rank is112.
An exact minor proves a nonempty open dense locus; a source grading gives
a common invariant dimension incompatible with Mat10. Next: determine
the exceptional rank-drop locus or remove that rank hypothesis. Moving
compressions and other unit trajectories remain outside the result.
Written and unreviewed; no exponent improvement.

The all-size packing continuation studies
`ai/2026-10-23-all-size-unit-packing/QUESTION.md` on
`research/all-size-unit-packing-20261023`. Its written all-field recurrence
proves a^2 disjoint unimodular units at every size and the sharp complex
all-singular source-space cap a^2(2a-2). Exact finite controls and focused
tests pass; full validation is pending. Further unit-packing searches in
this family are closed by the all-size argument. The remaining bridge is
to leading images and partial frames of arbitrary singular target maps,
or an actual construction outside those charts. No exponent gain.

The source-cap continuation studies
`ai/2026-10-23-source-singular-space-cap/QUESTION.md` on
`research/source-singular-space-cap-20261023`. Its written global argument
uses sixteen disjoint unimodular unit supports and a rank-preserving
distinct-weight limit to bound every all-singular complex source subspace
by96 dimensions, with a sharp zero-row kernel. A regular first lift must
therefore have leading rank at most96 if a109-column regular long frame
exists. Exact finite witnesses and focused tests pass; full validation
is pending. This is no arbitrary degeneration exclusion or exponent gain.

The asymmetric regular-frame continuation studies
`ai/2026-10-23-asymmetric-regular-frames/QUESTION.md` on
`research/asymmetric-regular-frames-20261023`. A unital rank upgrade
permits unequal frame dimensions106/110 and107/109. For a full regular
long map and regular unit lift this lowers the unit-image threshold to106,
including unit corank at most four. The complete strict-budget scan and
exact controls pass; the written proof remains unreviewed and full
validation is pending. The required frames are hypotheses. Rank105 and
general Laurent degenerations remain outside the argument.

The coupled-boundary continuation studies
`ai/2026-10-21-coupled-boundary-rank-two/QUESTION.md`. Simultaneous
boundary obstruction ranks at most two force both complete matrices to
vanish, by 232 cubic identities reducing 228 parameters to the prior
28-dimensional family. The balanced gap and projective conic certificate
then classify non-plane low-first-rank normals in the credited model.
Next: higher-order compatibility of that conic family, with the separate
12-by8 case kept distinct. Four focused tests pass. No smaller exponent.

The balanced-gap continuation studies
`ai/2026-10-21-balanced-puncture-gap/QUESTION.md`. A written complex
matrix-space proof establishes a sharp zero-or-three gap under balanced
two-dimensional quotients, importing the classical Kronecker form for
constant-rank-two pencils. Low projected first rank in the actual
28-dimensional boundary-compatible family now forces the complete
cancellation classified in PR94. The companion coupled cubic package now
supplies the prerequisite from simultaneous rank bounds; later
compatibility remains open.
Six focused tests pass. The exponent remains 9/4; all proofs unreviewed.

The balanced-puncture continuation studies
`ai/2026-10-21-biform-balanced-puncture/QUESTION.md`, from main 00d5133.
Complete third-block cancellation now forces auxiliary product kernels
and a biform syzygy space of dimension at most three. Every projective
chart is classified exactly: the common factor is
`(r*x0+s*x1)*(r*y0-s*y1)`, with a two-dimensional non-plane normal fiber.
The next questions are projected first rank one/two and higher-order
compatibility of these surviving directions.
The mixed-graph, Ferrers, rectangular and group-source workers retain
their existing ownership. No smaller exponent is established.

The uniform-cap worker now studies
`ai/2026-10-21-hankel-wronskian-cap/QUESTION.md`. A self-contained binomial-
shear/Wronskian proof covers every characteristic-zero bounded-Hankel
linear space, with an exact rational witness generator. The application now
adopts the concurrent higher-ruling, saturation and crossed-locus bounds
with exact pins, adding a scalar-Hankel equality case and a proper-section
dimension loss. It closes all improving ordinary A9 square sums. The finite
balanced comparison remains separate from the full all-source frontier. The older A9 square candidate
is already excluded by that concurrent three-ruling test; the new source-
gap draft is a separate structural question, not a stronger frontier claim.
PR75 merged at4695298 with exact tested/merged tree equality and all current
checks green; its completed local and remote task branches are removed.

## Constructive continuation after the ordinary frontier update

PR54 preserves recovered claims118 through122 and124, and adds exact
claims125 and126. The new auxiliary M(1,1,9) cancels a specified scalar
defect if the missing reduced maps can be found. Its six full mixed
responses vanish. An actual changed source basis escapes the old
compression hyperplane, but no M9 identity is constructed.

The concurrent Hankel–Segre proof in PR75 at1721a4e9 closes the former
ordinary A8 matrix endpoints within its stated scope. Do not repeat
ordinary A8 completion searches without addressing that written proof.
The constructive agents now pursue singular reduced-source maps and
changed local-basis limits. All finite numerical residuals are discovery
measurements, not witnesses. No exponent below9/4 is established.

The Ferrers worker now studies
`ai/2026-10-21-ferrers-ruling-cap/QUESTION.md`. A projective kernel
compression gives the sharp bilateral ruling cap, and openness of
low-rank dominance removes the hook case for a closed target with bounded
linear spaces. The application strengthens the scalar-Hankel tests and
adds67 balanced rectangular exclusions over PR83. General proofs remain
unreviewed, and no smaller exponent is established. PR83's separate
checkout continues exact-head main integration; its branch is not retired
until the actual merge and tree audit. Refresh concurrent ownership before
selecting a new construction question.

The pencil-degree worker now studies
`ai/2026-10-21-hankel-pencil-degree/QUESTION.md`. Its written Hankel Segre
bound in the strict5r<2(a+b) range closes the former ordinary A8 targets,
all balanced single rectangular formats through a9, and every improving
ordinary A8 square direct sum. The new exact frontier has494 survivors
through a12, first at a10. The later Wronskian application already
excludes all improving ordinary A9 square sums, including (32,6,3).
Pointwise source-gap structure and the A4 higher-rank shear completion
are separate questions; do not reopen that historical ordinary target.
The smaller exponent is unproved. PR64 merged at e5bc0bb with equal tested
and merged trees; its completed local and remote branches are removed.

The mixed-frame worker now studies
`ai/2026-10-21-all-rankone-seven-five/QUESTION.md`. A complete endpoint
source closure and physical reversal now cover every projective rank-one
partner in the canonical seven-by-five class under100. Move to smaller
first spaces or other flags; repeating this closed class is not a new
construction route. The written proof is unreviewed and omega is unchanged.

The mixed-frame worker now studies
`ai/2026-10-21-global-mixed-normal-dichotomy/QUESTION.md`. All six graph
parameters at a=b=1 reduce to fixed54- and36-dimensional quotient normal
families. Exact square and polynomial row identities collapse the rank-one
projection alternative to projection zero. Both families remain open.

The mixed-frame worker now studies
`ai/2026-10-21-mixed-exceptional-affine/QUESTION.md`. A new affine family
has at least38 normal directions, exactly38 generically. Its base graph
is fully excluded after recomputing all38 directions. The rest of the
family and exceptional affine four-planes remain open. Claim095 records
polynomial family identities separately from finite discovery grids.

The mixed-frame worker now studies
`ai/2026-10-21-generic-mixed-graphs/QUESTION.md`. Two fourteen-variable
normal blocks have exact quartic-spanning certificates at a rational
point. Their symbolic source partition and fixed56-equation normal chart
prove a nonempty open exclusion in all seven b=1 graph/partner parameters,
extended to b nonzero by the source torus. The remaining problem is affine
four-planes contained in the exceptional fibers. Constant-unit elimination
of the44-coordinate normal blocks is the next structural calculation.
PR74 contains the complete two-coordinate rank strata and exceptional
fiber proof; it incorporates main's PR40 and reruns CI with a30-minute
budget after a confirmed20-minute timeout. No exponent gain is established.

The rectangular worker now studies the one-unit factor criterion in
`ai/2026-10-21-rectangular-direct-sums/one_unit_pairing.md`. Primitive
kernel pencils must pair separably. The fixed-pencil Hankel tangent
image has dimension149 at the known641 slice; integrability is unproved.
The explicit high-half convolution family now integrates134 dimensions
of these deformations, with generic source slice rank641. Its separate
one-factor spaces have dimensions79 and63, leaving the smaller side one
coordinate short for a direct target ruling. Full target maps remain open.
A broader double-plus-six-simple-support family now has dimension141 and
full ambient span1360. A later scoped linearity proof excludes that explicit distinct-support
family as the generic rank-two target image. General confluent closures
and other critical source components remain open.
This is separate from the continuing degree-two/three Laurent map searches.

The rectangular worker has now applied the ruling gate to every hash-verified
predecessor two-block survivor:3717 exclusions and752 remaining through
dimension1500. Ordinary one- and two-block targets through dimension1152
are closed under the written lemmas. The degree-two Laurent construction
search continues independently; numerical residuals are not certificates.

The mixed-frame worker now studies
`ai/2026-10-21-mixed-five-space-graphs/QUESTION.md`. Four specified nontrivial
graph families close at partner a=b=1, each with arbitrary boundary part.
Quadratic-minor spans replace stalled triangular-minor cuts. The general
problem reduces to fifteen two-coordinate graph charts; they remain open.
PR67 merged at e25a287 with equal source/squash trees and its completed
local and remote branches removed. No exponent gain is established.

The mixed-frame worker now studies
`ai/2026-10-21-pure-mixed-five-spaces/QUESTION.md`. Pure mixed rows close
the seven-by-five case for b nonzero, with exact polynomial certificates
for every a after scaling b=1. The remaining quotient normals split into
six- and fourteen-dimensional families, and both terminal systems close.
The unresolved question is arbitrary mixed-row graphs; their pure-row
containment must not be assumed. Remaining partner strata are also open.
PR66 merged at294aca8 with equal source/squash trees and its completed
local and remote branches removed. No exponent gain is established.

The mixed-frame worker now studies
`ai/2026-10-21-mixed-five-space-uniform/QUESTION.md`. The first sixteen
low-rank source slices are now certified throughout the two-parameter
partner chart, with polynomial adapted sources and correction factors.
The remaining five-space incidence system has not been classified.
A direct rational determinantal calculation reached its300-second limit
without a result; this is an incomplete calculation, not an exclusion.
PR63 merged at5931b89 with equal source/squash trees and completed branches
removed. The coordinate-partner package PR65 is queued. No exponent gain.

The mixed-frame worker now studies
`ai/2026-10-21-mixed-five-space-residues/QUESTION.md`. At u=v=e3, arbitrary
mixed five-spaces opposite the full seven-frame force only plane normals.
The exact elimination uses low-rank source slices, cubic minors and
mixedness; it closes the former four-source residual at this point.
The two-parameter virtual tensor is constructed, but direct coordinate
support covers do not extend the elimination uniformly. Adapted source
combinations and the other partner points remain under investigation.
PR62 merged at99ce778 with equal source/squash trees and its completed
branches removed. PR63 is queued after current checks. No exponent gain.

The [balanced ordinary rectangular scan](ai/2026-10-21-rectangular-ordinary-frontier/QUESTION.md)
now uses the existing polynomial and higher Hankel gates. Every improving
single ordinary shape through source leg dimension1152 is now excluded
by the later saturation and two-ruling arguments. This closes both the
former A88 to M(27,28,28) and A89 to M30 ordinary candidates. Singular
degenerations remain open. At this checkpoint, the only ordinary survivor through dimension1500
was A(8,10) to M(32,33,33), with no maps supplied; see the two-ruling proof
and `ai/2026-10-21-rectangular-direct-sums/next_ordinary_target.md`. The quantum worker's separate positive question remains
a higher-rank completion of the A4 integrable boundary shear. PR61 merged
at e24894f after current checks, with exact tested/merged tree equality;
its completed task branches are removed.
The later [critical finite-state argument](ai/2026-10-21-rectangular-direct-sums/critical_finite_states.md)
closes that last ordinary candidate through dimension1500 under its
written, unreviewed premises. It does not classify singular degenerations.

The quantum worker now studies
`ai/2026-10-21-integrable-boundary-shears/QUESTION.md`. A complete exact
two-parameter non-plane family exists at first ranks10,10. Its local
rowspaces have rank14, its tensor has first rank12, and those spaces are
complete mutual annihilators away from the origin. It is not the matrix
target. The next question is a higher-rank completion or an obstruction
that includes these moving flags, rather than another finite jet of the
same low-rank family. PR58 merged at93b2223 with exact tested/merged tree
equality and all current checks passing; its task branches are removed.

The quantum worker's current question is
`ai/2026-10-21-biform-third-core/QUESTION.md`. The complete normal third
tensor has a biform syzygy core. Arbitrary boundary first pairs of
dimensions at least11,9 are excluded at every order by a sharp puncture
lemma and conditioned obstruction certificate. The necessary ordinary
first-rank sum is at most20; pure pairs12,8 and10,10 remain at that
threshold. PR57 merged at eb97dbe with exact tested/merged tree equality;
its completed local and remote branches are removed.

The quantum worker now studies the question in
`ai/2026-10-21-boundary-hyperplanes/QUESTION.md`. Arbitrary boundary first
spans of dimensions at least11 on both sides are excluded at every order,
including delayed unequal growth. The proof uses a rank-one-free matrix
space and a general two-hyperplane compression lemma. Ordinary first-rank
sum is at most22, with one rank at most10. Smaller pairs and other leading
flags remain open. PR55 merged at18a06b3 after current CI, with exact
tested/merged tree equality; its completed local and remote branches are gone.

The quantum worker's current question is
`ai/2026-10-21-third-boundary-trap/QUESTION.md`. Full boundary first frames
of effective dimensions12,12 are excluded at every order, including delayed
and unequal first-growth orders, by a new third-block rank gap and the
moving-boundary induction. PR49's complete second jets remain finite
controls. For every ordinary first pair at these flags, the corrected
projected third coefficient on K_inf must have first rank at most2.
The next construction question concerns other first subspaces or leading
flags; coordinate omissions alone do not settle the general question.

The mixed-jet worker continues in
`ai/2026-10-21-rankone-mixed-hyperplanes/QUESTION.md`. Each arbitrary mixed
hyperplane now forces its leg's complete seven-frame normal equations
without any opposite-leg assumption. This excludes all rank-one pairs
with both first dimensions at least six by a written all-order proof.
The ordinary both-mixed first-rank sum is at most twelve; investigate
arbitrary seven-by-five spaces and smaller pairs for actual output growth.
Coordinate seven-by-five survivors examined so far have third residues
confined to a rank-one output entry, below the target gap; this is a
scratch-control finding, not an all-subspace exclusion. The concurrent
boundary-shear family remains credited as a non-plane integrability control
with output ranks fourteen and no matrix target. No exponent gain is claimed.

The quantum worker previously constructed the complete172-parameter
second-jet family in `ai/2026-10-21-corrected-prolongation/`. Its finite
coefficient witnesses are retained; the full boundary-frame matrix target
is excluded by the third-order boundary trap. PR47 merged at `fc8207e` with exact tested/merged tree equality;
its task branches are removed. The new family has effective first ranks12
on each side, outside the13-per-side hypothesis in PR48. No improving
matrix tensor limit is constructed.

The quantum worker's current question is
`ai/2026-10-21-second-jet-rank-one/QUESTION.md`: the canonical changed jets
now have no second partial-space growth, by a new rank-two spanning
certificate. Prolong the coupled leading-row directions through the complete
second-order cokernel equations before attempting third-order construction.
The prior moving-projection and256-block package merged through PR44 at
`d2ed2e9`; its tested/merged trees match and both task branches were removed.
Canonical first-jet extension data are adopted from PR45 at `b0a54f2`.

The exponent-improvement goal is active; no bound below 9/4 is established.
The user requests frequent integration of completed work into main and cleanup
of fully merged task branches. Preserve proof status and source attribution
when merging; integration is not theorem acceptance.

## Paired-source continuation

The conditional [paired long-leg target screen](ai/2026-10-23-paired-long-leg-target-screen/README.md)
compares both exact target ranks for all 28 saved survivors in the degrees
covered by the associated-graded source bound from unmerged PR #169. The
screen closes only the windows `183–209`, `211–241`, and `241–274` at
`a=14,15,16`, conditional on that still-unreviewed proof. Other intermediate
degrees and exact source ranks remain open.

The [shift-separation package](ai/2026-10-23-paired-shift-separation/README.md)
extends the ordinary channel-rank obstruction to a variable-coefficient
long-leg map with combined shift rank below the middle width, while the
other long leg remains finite-band Toeplitz. Its all-field flattening
bound is `g_B*g_C`; the exact finite control passes. The proof is written
and unreviewed. Arbitrary full shift-rank maps, Laurent cancellations and
the construction question remain open; no exponent improvement follows.

The current continuation integrates main `b113866`. Checkpoint `27d7a75`
completed 578 tests, with 577 passes and one optional NumPy skip, and
all five local archive replays. Five hosted static checks passed; no
hosted test workflow was observed at that commit. The complete receipt
is retained. New packages require validation on their own pushed tree.

The three size-dependent nonlocal operator pilots are complete and
preserved, with no exact witness. Their rational product-projection
reference requires quadratic rank for a literal repair. The generalized
Pass packing count is already implied by the scalar concavity program.
The new source-capacity proof bounds feasible target dimensions when
the auxiliary border rank is subquadratic. These are scoped findings,
not exponent improvements.

Three agents now pursue and independently audit quantum long maps with
all required factor exchanges, and Cauchy/displacement identities in the
native Q tensor. Negative Laurent terms and every auxiliary correction
must be counted. The scalar coefficient allowance is not permission to
treat factor exchanges, inverse maps across different legs, or omitted
tensor coefficients as free.

The next checkpoint integrates main `8a07bed` and extends the conditional
correction budget to a strict nonzero coefficient at order `n^(3/2)`.
At near-full width four, auxiliary border rank at most
`(4/25)*n^(3/2)+o(n^(3/2))` would suffice. There are no maps satisfying
this unbounded family premise. Checkpoint `25600a7` completed 565 local
tests with 564 passes and one optional NumPy skip; all five local archive
replays and five observed hosted static checks passed. No hosted test
workflow was observed for that commit.

The fixed endpoint corner with one scalar is now excluded by a closed
incidence argument. Two scalars are excluded for ordinary maps, and a
separate exact gate closes the stated enriched Laurent leading point.
The general border-D2 repair remains open. The fixed-lead/free-kernel
and diagonal-deleted-corner pilots have both completed and failed exact
acceptance; their complete saved maps and histories are preserved.

The centered shared-input aggregation has been fully costed: it retains
different partial-transpose orientations, and neither of its known
source bounds meets the paired budget. The fixed full-format tensor is
excluded as a matrix degeneration. That fixed tensor is a closed task.
Three agents now coordinate an actual Q-source construction through
noncommuting shift operators, displacement identities, and bounded
size-dependent Fourier/chirp/reflection probes with exact small controls.
Any auxiliary tensor must be included in the complete character cost.

PR #35, `research/paired-frontier-unequal-entropy-20261020`, continues with
three coordinated agents on exact recovery and scalable near-full
width-four maps. The small target `Q(5,4) -> M4` now has a complete
integer witness, recovered from numerical rowspaces and verified without
floating-point arithmetic. The same proof gives `Q(k+1,k) -> M(k,4,k)`.
It supplies no exponent improvement; its fixed-width dimension limit
does not permit a near-full large-n extension. The next target is
`Q(6,4) -> M(5,4,5)` beyond that template's limit.
The branch supplies a conditional linear-correction criterion, complete
ordinary narrow-source obstructions, and explicitly limited symmetry and
jet exclusions. Full narrow ordinary fits and the excluded regular-long-leg
Laurent class are closed tasks. The required width-four unbounded family
remains open. Checkpoint `cfa12ba` passes 467 local tests and five archive
replays. The next checkpoint `1e0e468` completed 476 tests with one
unsupported claim-status failure and five passing archive replays. The
status label is repaired in the current continuation; its enlarged tree,
including main `11aca0f`, is checkpoint `9d8b240`: all 485 local tests,
five archive replays, and nine hosted checks passed. The next continuation
integrates main `e00622f` and needs its own full validation.

The boundary-only extension of the integer seed is now excluded at every
Laurent order: its leading first-leg kernel has dimension at most one,
whereas the next matrix size needs nine. The constructive search therefore
allows old long-map columns to move and seeks exact leading points with
larger kernels. All diagonal Laurent weights of the two prescribed
near-full quantum families are also excluded by a balanced-support lemma.
The quantum lane now examines structured corrections and different maps.
The complete Q54 numerical discovery history is retained separately from
the exact integer witness; small residuals alone remain insufficient.

The correction allowance now extends to `O(n^alpha)` for any fixed
`alpha<3/2`; `alpha=4/3` retains the conditional bound below 2.2334.
Constructive work examines the bulk of the quantum target with explicitly
costed missing diagonals and different smaller leading points with more
kernel slack. The fixed M2-leading monomial first-jet chart is excluded.
Six complete-flag fits are preserved with exact grading/gauge controls;
their low residuals do not pass exact Laurent acceptance.

Claim `AI-Q64-DIAGONAL-SHIFT-CORRECTION-001` now excludes one explicit
shift-diagonal map family: its residual has an `n^2`-rank first-leg
flattening for every n. This does not close the general paired-source
question. The next construction search must change a leg map or source
family and charge the complete auxiliary border rank.

The [fixed-long-leg continuation](ai/2026-10-23-q64-coordinate-long-legs/proof.md)
allows an arbitrary linear map on the first leg. The stacked `(0,0)` and
`(1,1)` projected blocks have rank `n^2` for every such map, so a linear-cost
correction is impossible while both long-leg coordinate maps stay fixed.
Changing either long-leg map or the source family remains open.

The [inner-index shift continuation](ai/2026-10-23-q64-inner-shifted-coordinates/proof.md)
covers every size-dependent pair `0<=k_B,k_C<n` in
`B_(y,s)->b_(s-k_B*y,y)` and
`C_(z,v)->c_(v,z-k_C*v)`. For arbitrary first-leg maps the correction
flattening rank is at least `n^2/2` for `n>=4`. High multipliers remove
the entire matched `j=2` source block; the off-diagonal support argument
handles the remaining low-multiplier range. This closes all such
size-dependent inner-index shifts.

The [arbitrary inner-shift package](ai/2026-10-23-q64-arbitrary-inner-shifts/proof.md)
now allows independent translations on all four inner indices of each long
leg. For any first-leg map the correction flattening rank is at least
`n(n-1)/2` for every n. It bounds the target/source slice-space
intersection using adjacent C-shift terms; the proof is unreviewed. General
non-coordinate long-leg maps remain open.

The [matched-window permutation package](ai/2026-10-23-q64-window-permutations/proof.md)
allows an independent permutation of every matched long-leg coordinate
window. Its target/source slice-space intersection has dimension at most
`2n-1`, giving correction flattening rank at least `(n-1)^2` for every
first-leg map. The proof remains unreviewed.

The inherited M1 endpoint corner has now been constructed exactly and
excluded from degenerating to M4 by a closed low-slice-rank obstruction.
The smaller sparse M1 lead has an all-size first-edge support deficit.
Moving leading maps and changing the corner kernel remain open. The two
completed moving-leading fits failed their coefficient and leading-rank
conditions; the current free-kernel fit has no exact certificate either.
The next reduced questions are a diagonal-deleted M4 target and a
one-scalar correction to the corner. The natural fixed-endpoint corner
family loses too many long-leg dimensions to scale directly, so either
small success would still require an additional extension argument.

The quantum lane closes the stated small homogeneous corrections to
one fixed root-of-unity point and a fixed monomial first-cross chart for
the partial bulk target. Arbitrary ungraded and differently singular
maps remain open. Its next constructive question examines centered
tensor aggregation, including the transpose orientation and all-size
source costs. The 39 terminal leading-M4 points and twelve partial-bulk
records are preserved as finite search evidence. A documented metadata
repair restores sampled ridge histories without changing tensor maps.

The central-group worker merged H_5 incidence through PR #42 at bfc5243,
the all-power modular application through PR #78 at b95abc2, and the
native two-cover package through PR #73 at80737e6. Their tested and
merged trees match, and their completed topic branches are removed.
PR #79 adds the written subgroup-ideal cuts and is ready with auto-merge
enabled. The constructive source on research/s5-split-20261021 is now
S5 with central C2, C2 squared or C4. The exact2.247 comparisons pass
conditionally; actual improving targets remain missing. The E4 central
matching lemma has a strict-potential proof, while C4 matching is already
excluded by a color-sum argument. The direct colored sampler reached two
collisions for M(18,18,20); both four-color bases are being continued.
No smaller exponent is established. Preserve ongoing discovery reports.

The quantum worker's current question is in
`ai/2026-10-20-quantum-jet-filtration/QUESTION.md`. Exact first-jet certificates
close the prescribed order-three/six parameter curves even for ungraded
constant output projections before the limit. Parameter-dependent output
maps and different block weights remain open; unchanged approach-rate pilots
are no longer a construction question. These are unreviewed local proofs,
not a bound below 9/4.

The quantum worker continues in
`ai/2026-10-20-higher-jet-quantum-flags/QUESTION.md`, after PR41 merged at
`f67467d`. Both local and remote PR41 branches were removed after exact
merged/tested tree equality. The higher-jet follow-up closes regular moving
surjections that stay full rank at the limit and a distinct 256-pair
full-output block family. Singular leading output maps, multiple leading
blocks and larger block-weight gaps remain open construction questions.

## Constructive-spectrum continuation

PR #28 is merged at `8722b361fde7713949b8f0e72fab681066ce10bd`.
Its tested head was `4c88acad6b163ebb20011dd947a4092df003533f`, whose tree
matches the squash merge. All required hosted jobs pass; the Python 3.10
job reports 353 completed tests. Earlier checkpoints retain their exact
local test receipts, including 350 tests at `bf4d187`.
PR #38 is merged at `fc460bf25fb106ab5de38863d37d1ac4cbfd12dc`.
Its tested head `f87d3037c9d559ba6972d4738a7d88209dbc8627` has the same
source tree, with every current hosted check passing. It preserves the
boundary proof, frontier update, and exact retained-residual maps. The complete
local suite at `8b09235` passes 368 tests and all five archive replays
using only maintained verification dependencies. The initial Markdown
link-check failure and its notation repair are retained in the validation
receipt. Concurrent main `5c28a60` is integrated; its changes concern
external-source attribution and the source-registry count assertion.
All statements retain the evidence status in `claims.json`.

The parity A(5,5) target M14 plus M4 is closed, including singular
degenerations of that face. For full sources, exact ordinary square-target
frontiers now exclude all 60 source formats with N<960. The new
first-boundary Hankel argument excludes the former A(7,8) M25 plus M5
candidate. It requires a+b-1=3r-1 and uses cap max(r,4); do not extrapolate
it to arbitrary degrees. Singular full-source degenerations remain open.

The first surviving ordinary source is A(8,8). Its unconstructed target
M27 plus M7, D=778, would imply omega<4497/2000=2.2485. A completed integral
M15 seed is available, but it is substantially smaller. No improving maps
are supplied. The frontier proof, saved report, and tests must stay in sync.

Exact retained residual maps give A(a,a+1) to M(2a-2) plus A(2,a-2), a>=5.
The A(7,8) M12 core has a fixed-core extension limit D<=256; moving cores
are outside that limit. The triangular construction gives A(a,b) plus
M((a-1)(b-1)) to M(a+b-1), with the full correction retained. Single full
matrix corrections and the stated independent corner supplier cannot
pass their score tests. Three regular A22 quotient kernels cannot make
the scalar correction vanish while preserving the exact normalized M3.
More generally, any three exact cyclic physical quotients satisfy
m0*m1*m2<=(a+b-1)^3, including over Laurent fields. Even free cancellation
is insufficient in that quotient class for the single-target finite gate.

Active constructive work includes relaxed physical compression maps with
both off-diagonal blocks free, singular coefficient families, unequal
rectangular targets, tensor powers, and the earlier nonmonic flag system.
An interior-spectrum higher-difference theorem also remains open. Do not
repeat searches in the excluded ordinary formats or exact quotient class.
[PR #43](https://github.com/1337isnot1337/matrix-mult-bounds/pull/43)
is merged at `e00622fc3e3179f2c87ac3185f2158c39b2fe707`. Its source tree
matches the tested head `df9e12c`. All current hosted checks passed;
Python 3.10 ran 471 tests, with 470 passed and one optional control skipped.
The fully incorporated local and remote topic branches were removed.
The continuation branch `research/weight-mixing-20261021` was integrated in
[PR #51](https://github.com/1337isnot1337/matrix-mult-bounds/pull/51).
Its first checkpoint `5d5cc6d` passes all hosted checks. The pushed
checkpoint `1f813bb` adds exact crossed modules, two-source capacity,
a projected carry obstruction, and the completed compression search
with its actual residual. It incorporates main's corrected second-jet
family at `8a07bed`. Its full local suite completes 496 tests: 493 pass
and three optional controls skip; all five archive replays pass. All
hosted checks for that checkpoint pass. Checkpoint `4ed2b52` incorporates
main's mixed second-order family at `21f54c3` with the new spin, corner
and fixed-map packages. Its 35 focused tests and full 513-test suite
pass, with three optional skips in the full suite. All current hosted
checks for `4ed2b52` pass; hosted Python 3.10 also runs 513 tests with
three skips. The final integration incorporates main's third-order
mixed-space proof at `b113866` and is pushed at `dab88a6`, with 27 passing
focused checks. All hosted checks pass for that revision; Python 3.10
completes 517 tests. PR #51 is merged at `46e343c`, whose tree exactly
matches the tested head. The fully incorporated local and remote topic
branches are removed. Further assembly work is on
`research/spin-assembly-20261021`, based on that verified merge.
Its exact packages through claim 113 pass 31 focused checks, including
the complete rational maps and repository invariants. PR #54 is pushed
at `1b94457`; all hosted checks pass, with 530 tests and three optional
skips on Python 3.10. The next checkpoint incorporates main's
third-boundary theorem at `18a06b3` together with claims 114 through 117.
Its separate 36-test receipt pins the new maps, proofs, and repository
integration. The newer packages are outside the earlier 530-test count.
The earlier PR #43 checkpoints `fa74fee`, `574cb35`, and `bb64dae` are
incorporated in main. The first,
combined with main `f67467d`, passed 391 tests and all five archive replays
using only maintained dependencies. The second adds 24 passing focused
tests. The complete third-checkpoint suite ran 447 tests: 446 passed and
the optional NumPy control skipped. All five original archive replays
passed. Its receipt pins `bb64dae` and main `b0a54f2`; newer packages have
separate focused checks. Claims 075 through 097 now include the exact partial maps,
both fixed-boundary noncompletion proofs, the graded core bound, the
free-interior family and its fixed-channel limits, the two-leg rank chain,
the complete original-profile degree-13 obstruction, the width-13 rank
contradiction, the finite common-vertex M7 screen, and the saturated pencil
determinant, the complete common-profile classification, unequal-profile
partial controls, the universal homogeneous support-peeling obstruction,
the quantitative mixed-grading requirement, two complete Laurent collision
controls, and scalar-power correction reuse with exact source-cost accounting.
The saved map bytes and their positive partial identities remain unchanged.
Checkpoint `9d676ab` includes concurrent main through `63eecee`. Its 16
focused construction/concurrent-main tests and 18 repository/profile checks
pass. The subsequent merge includes `fc8207e`, preserves all 137 claim
records, and passes the five new second-jet tests with maintained dependencies.

All ordinary maps that send target matrix units homogeneously into the
fixed source grading are now excluded for A88 to M27 plus M7, including
every unequal vertex profile. The exact support-peeling sequence is
960 to 922 to 834 to 468, which contradicts the required map rank 778.
The primary separator certificate and an independent full-source replay
agree. The earlier profile candidates are historical partial controls.

The ungraded A88 frontier remains open. Construction work now studies
maps mixing several source weights, genuine Laurent cancellation, and
tensor-power recycling with explicit residual and source-cost accounting.
Every ordinary construction needs at least 19 images with three or more
source weights on each of at least two legs. The exact three-weight M12
plus M3 maps remain a smaller-target change of basis. The completed original-source
Laurent chart uses invertible 960-direction maps before the limit and has
a concise projection of format 936 by 936 by 935. Its exact 126-slice
cover excludes the intended square target and every further degeneration
to that target. The moving physical-compression search retains complete
target normalization but has produced no singular family. Claims 098 and 099 preserve
this result and the requirement that some ordinary target image span at
least four source-weight steps. An exact golden-ratio slice supplies a
three-weight cancellation direction. Exact rational maps now give
C(2,4) tensor C(2,8) to M(2,2,11), A(4,8) to M(4,4,11), and A(8,8)
to M(4,4,22). Claims 100 through 103 preserve these maps, the sharp
two-source dimension condition, the narrow carry obstruction and the
completed numerical chart. The active construction question is whether
changed subspaces or coupled copies can retain a large rectangular module
while leaving enough original-source directions for a full square target.
A separate exact flattening argument closes the old fixed-first-map
family. Claims 104 through 107 preserve this obstruction, the old
fixed-seed response proof, the new spin-one module M(3,3,28), and the
changed corner module M(4,4,12) with response rank 164. The active
ordinary question is square assembly from these changed cores. For
the spin core, M27 plus M6 plus M3 has enough kernel dimensions and
would imply omega below 2.24975, but the required maps are missing.
The agents are computing exact preimages for additional matrix rows,
repairing retained maps, and testing extensions with dimension slack.
None of these results lowers the exponent yet.
Claims 108 through 110 now give the full saved-core preimages, an exact
Y-map endpoint repair with response rank 191, and the ensuing fixed-map
extension exclusion at dimension 778. The endpoint repair changes the
map and meets the dimension allowance, but its retained Z map forces
a new-row response of rank at most one. Claims 111 through 113 give a
different four-chain spin module, finite boundary-discovery records,
and eight simultaneous exact single-channel attachments. The combined
tensor glues M(3,3,27) to M(3,8,1) along three third-leg variables;
all 237,897 target coefficients are checked. This is a partial tensor:
each added vertex still lacks 26 channels. The agents are changing
retained maps jointly and constructing Laurent cancellation to complete
compatible channels. Claims 114 through 117 now preserve an exact
891-parameter core-preserving family, a Laurent endpoint cancellation
and two-channel attachment, a balanced M(3,3,32) module, and a complete
M(3,7,27) construction. The last construction has first response rank
576 and cannot retain its other-leg maps in an ordinary extension with
first dimension greater than 405. The balanced module allows five
channels to be removed before reaching 27, providing a different
family of coupled changes. The full square and rectangular improving
targets remain missing; the dimension-774 alternative remains open.
Pure A22
tensor powers cannot cross the current sixfold square-sum gate even by
dimension, so recycling work requires a different source budget or a real
source compression.
All three research slots remain assigned. Current hosted checks are
required before merging; preserve concurrent worker files.

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

The separate higher-power investigation is on
`research/persistent-frontier-01a1697a` (PR183), with its proof in
`ai/2026-10-23-s5-higher-powers/proof.md`. It supplies a written,
unreviewed method boundary: all coordinate covers of the full degree
majorant cost too much for PR111's eleven remaining targets whenever
n>=36. The actual source's slice rank is not bounded below. Finer support,
other bases and powers below 36 remain open. It does not duplicate
PR140's monotone cube census; PR111 is an integration prerequisite.

- Outer-compression consequence: `ai/2026-10-21-rectangular-direct-sums/outer_compression.md`. Both outer rank-two strata are too small for an injective target leg. The missing classification of nonregular critical slices remains open.
- Written ordinary-target closure under audit: `ai/2026-10-21-rectangular-direct-sums/critical_finite_states.md`. Generic realization and all minimal finite-state strata are now addressed; no singular-degeneration exclusion follows. Preserve earlier frontier outputs as historical arithmetic scans, with this subsequent proof disposition.
- Expanded ordinary single-target frontier:74 candidates remain through source size2000. The first two larger targets fail only the diagonal SL2 capacity ansatz. General maps and singular degenerations remain open. Numerical degree-two and zero-padded degree-three continuations are active, with all completed checkpoints labeled numerical.
- Larger equivariant leads: representation capacity alone passes a bounded A(24,24) to M124 family, but all four physical-subset triples fail known or new ordinary obstructions. The new invariant-slice bound does not rule out singular degenerations. The bounded a24..36 search is complete: all4070 capacity triples fail the prior shared-top obstruction or the new ordinary-only slice bound.
- Laurent numerical work: raw degree-three continuation completed without an exact identity. A scale-normalized objective now removes Laurent-variable residual suppression; smoke and derivative checks are recorded, including a rejected ill-conditioned attempt. The stable-floor normalized search is in progress.

## S5 finite-cover continuation

The full-source Peirce refinement continues on
`research/s5-peirce-finite-covers-20261023`, in
`ai/2026-10-23-s5-peirce-covers/`. Replaying all original source
coefficients validates finer degree assignments and cube bounds 6638912
and 41159136. Five additional r=2 shapes are excluded; the remaining
four are (16,16,25), (16,19,21), (14,19,24), and (16,20,20).
The r=1 M(13,14,14) comparison remains open. All five focused tests pass;
full integrated-head CI is pending. This result changes the degree input
and does not contradict PR140's finite boundary for the coarser radical
majorants. It does not depend on PR140 or establish an exponent gain.

The central-group correction continuation owns
`ai/2026-10-21-s5-scalar-repair/QUESTION.md` on
research/s5-scalar-repair-20261021. The exact eight-scalar gate passes at
2.2499, but its improving witness is missing. A new diagonal-rank lemma
and nine coordinate-disjoint Farkas circuits exclude rank-eight Laurent
corrections to the first trade-free candidate with fixed group coordinates
and arbitrary integer vertex weights. Other candidates and mixed group
maps remain open. Weighted commuting discovery is continuing.
