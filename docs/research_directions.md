# Research directions

## October23: constrain both singular A4 long-map limits

The [current rank-sum continuation](../research/ai/2026-10-23-long-leg-rank-obstruction/torus_rank_sum.md)
adopts PR129's sharp rank23 source-space cap and continues PR113's
regular residual. Every A4 to M(10,10,11) candidate needs rank at most101
in each scalar-normalized long-map leading coefficient, and sum at most200.
These conditions permit arbitrary finite poles in the other maps.
They are necessary conditions, not constructions or a general exclusion.
The remaining problem is lower-rank singular assembly with exact complete
tensor identities. At sum200 the polar source-rank cap is24 and admits
a twelve-dimensional source space. New structure is needed at that
boundary. The exact adopted source and overlapping concurrent work keep
their attribution. All stated proofs remain written and unreviewed.

These are proposed investigations, not claimed results. Each task has a concrete output and an explicit path to a downstream claim.

The [fixed-two conic curve](../research/ai/2026-10-23-conic-fixed-two-curve/proof.md)
now extends PR107's entire prescribed two-jet on d nonzero, with exact
polynomial maps of degrees eight and nine and no other parameter guards.
Its kernel stays fixed, whereas PR107's prescribed third kernel
coefficient is nonzero. Determine whether that full third jet extends
with a moving kernel, or cover the remaining projective base charts of
the all-order normal-class criterion. An extension of one specified
two-jet does not classify all boundary velocities or construct the full
matrix target.

The [fixed-first conic curve](../research/ai/2026-10-23-conic-fixed-first-curve/proof.md)
now preserves PR107's entire specified first jet in two exact cubic
maps, uniformly for all complex a,b,d. Its second coefficients change
only on the boundary. The fixed-two package above now supplies an
exact extension of the prescribed full two-jet on d nonzero. An extension of this one full first jet does
not classify all possible boundary velocities.

The [polynomial conic curve](../research/ai/2026-10-23-conic-polynomial-curve/proof.md)
now realizes every cubic-component normal[1:d] for all complex a,b,d,
including d=0, with complete maps of t-degrees one and three. Combined
with PR101, its corollary makes the second-order criterion necessary and
sufficient for all-order normal-class existence on the affine base chart.
Its boundary
velocity differs from the credited first jet. The separate
[higher-conic witnesses](../research/ai/2026-10-23-conic-higher-jets/proof.md)
extend specified lower coefficients through order four universally for
d nonzero and through order fifteen at a=1,b=2,d=1. The order-fourteen jet
fixes the ten-jet coefficients through order nine; the order-fifteen jet
continues it through order thirteen. Determine whether this repeated finite
continuation has an exact algebraic description or a genuine next-order
obstruction under the full tangent freedom, then connect this rank-twelve
incidence to the full matrix target. The all-order local curve alone
does not construct M(10,10,11). Concurrent PR123 retains its separate
exact d=0 curve preserving its credited two-jet.

The [fixed-resolvent minimum-rank certificate](../research/ai/2026-10-23-resolvent-minrank/README.md)
proves rank six sharply over every field. The
[rank-six classification](../research/ai/2026-10-23-resolvent-rank-six-locus/proof.md)
now determines its 17-dimensional linear locus and common six-dimensional
image. Over an algebraically closed field, two rank-109 compressions lose
at most one direction; an explicit integer pair attains the bound. The next
structural questions concern larger rank-loss budgets and other resolvent
limits. Check the broader long-map exclusions before treating any aligned
compression as a possible matrix target.

## Active paired construction: near-full width four

The [linear-correction criterion](../research/ai/2026-10-21-correction-budget/README.md)
reduces one sufficient route to genuine degenerations
`Q(n,4) + R_n -> M(n-c,4,n-c)` along an unbounded sequence, with fixed c
and `border_rank(R_n)=O(n)`. It would imply
`omega < 30000/13433 < 2.2334`. The family is unconstructed. The active
paired branch has recovered an [exact integer Q(5,4) to M4 witness](../research/ai/2026-10-20-paired-construction/outer_product_injection.md)
and the family `Q(k+1,k) -> M(k,4,k)`. Its source width grows with k,
so it does not prove the fixed-width premise. Changed long maps now give
an [exact integer repair](../research/ai/2026-10-23-oblique-paired-repair/proof.md)
`Q(6,4) + D_19 -> M(5,4,5)`, with residual ranks `(9,11,11)`.
An explicit [six-term core degeneration](../research/ai/2026-10-23-oblique-border-repair/proof.md)
reduces the added border correction to eighteen scalars, while retaining
the nineteen-scalar ordinary correction. Its full polynomial maps and
disjoint-core family are certified; the small core has exact border rank
six. The full residual has ordinary rank exactly nineteen, while the
[equalizer lower bound](../research/ai/2026-10-23-oblique-border-equalizer/proof.md)
places its complex border rank between twelve and eighteen. This fixed
residual's optimal border rank remains open; a correction below twelve
would require changed source maps.
The resulting fixed-width family has quadratic first support and does
not meet the small-repair premise. The zero-auxiliary target
`Q(6,4) -> M(5,4,5)` remains unconstructed. Useful next work includes
smaller certified scalar repairs, changed polynomial spaces or long maps,
and an unbounded family with every auxiliary cost accounted for.
A machine-precision numerical fit remains discovery evidence only.

The [surjective long-map benchmark and finite frontier](../research/ai/2026-10-23-oblique-longmap-frontier/README.md)
make the next change of map family more precise. The benchmark has both
long maps surjective and first residual nine. Arbitrary changes only to
its four added output rows cannot improve that first rank: the fixed good
projection is injective on all thirty-six source first coordinates.
The 384 specified shift pairs and 61 valid mixed-middle corners also give
no lower first residual, within their finite stated scopes. A new attempt
must change good output rows beyond these tested controls or use a
different limiting construction. Unrestricted long maps remain open.

Optimizing only the first map with the old product long maps is now
settled by the [exact residual-rank formula](../research/ai/2026-10-23-product-longmap-residual/README.md).
For every `n>=5` in characteristic different from two, the minimum first
residual rank is `(n-1)^2-max(9-n,1)^2`, attained by the old first map.
A low-first-support construction must change at least one long map or
use a different limiting construction. The slice-space quotient formula
in that proof gives an exact screen for new fixed long-map candidates;
it does not exclude unrestricted long-map families or general degenerations.

The [fixed oblique-repair atlas](../research/ai/2026-10-23-oblique-koszul-atlas/README.md)
checks every unprojected full-space Koszul map of the one-dependency
residuals at r=3,4,5,6. None improves the earlier equalizer lower bound.
For the fixed Q(6,4) maps, stronger secant conditions or better border
repairs remain relevant; repeating these full-space ranks does not narrow
the inherited border-rank interval 12 through 18. Other projections and
maps are outside this finite check.

The fixed diagonal-shift maps in
[AI-Q64-DIAGONAL-SHIFT-CORRECTION-001](../research/ai/2026-10-23-q64-diagonal-shift/proof.md)
are now excluded: their target-minus-source correction has first-leg
flattening rank `n^2`. This result does not cover other maps. The entire
first-leg chart is now excluded by the
[fixed-long-leg extension](../research/ai/2026-10-23-q64-coordinate-long-legs/proof.md)
as long as the two long-leg
coordinate maps stay fixed: the correction flattening rank is `n^2`.
Further work must change at least one long-leg map or use a different
source family.

The family `B_(y,s)->b_(s-k_B*y,y)` and
`C_(z,v)->c_(v,z-k_C*v)` for any size-dependent `0<=k_B,k_C<n` is also
excluded for arbitrary first-leg maps: the correction flattening rank is
at least `n^2/2` for `n>=4`, uniformly over both multipliers. Further work
must use a different long-leg map or a different source family.

Even arbitrary per-index coordinate translations on both long legs are
excluded by [AI-Q64-ARBITRARY-INNER-SHIFTS-001](../research/ai/2026-10-23-q64-arbitrary-inner-shifts/proof.md):
their correction flattening rank is at least `n(n-1)/2` for every n.
Continue with non-coordinate long-leg maps or a different source family.

Independent permutations of every matched coordinate window are also
excluded by [AI-Q64-WINDOW-PERMUTATIONS-001](../research/ai/2026-10-23-q64-window-permutations/proof.md),
with correction flattening rank at least `(n-1)^2`. Broader non-coordinate
long-leg maps remain open.

The full narrow target `Q(n,2) -> M(n,2,n)` is now excluded for ordinary
maps when n is at least three, and for arbitrary first-leg Laurent poles
when both long maps remain regular and full rank. Do not repeat those
classes. Near-full outer dimensions, singular leading long maps, general
wider kernels, and nontrivial auxiliary tensors remain construction
questions. The prescribed regular-nilpotent wider quotient and the stated
tetrahedral scalar-repair models are also excluded; see the exact scope in
the linked status notes before choosing new parameters.

The [two-variable long-leg barrier](../research/ai/2026-10-23-two-variable-long-legs/proof.md)
closes another ordinary repair family: a common window dimension r on
one leg and coefficient-profile count s on the other force quadratic
repair when r*s<m, even though both maps vary by column. Full profile
spans, a failure of this strict channel gap, or genuinely singular
cancellation are necessary ways outside this particular proof. They do
not establish a construction. The credited one-variable predecessors
remain distinct pending PRs.

## R1: Review the local sharpness theorem

Status: open. Review the full all-integer proof, especially positivity of increments, the limiting slope, and the join at $a=b$. Distinguish the earlier recurrence from the local matching construction.

Deliver a proof review tied to a commit, a corrected proof, or a counterexample. A finite grid extension alone does not close this task. A Lean formalization is a separate deliverable, not a prerequisite for every discovery.

## R2: Decide compatibility with the product-filtration family

Status: settled for the three stated two-source, fixed-label families by
[AI-FILTRATION-007](../research/ai/2026-10-20-concavity-equivalence/research_note.md).
They are equivalent to separate concavity including the zero boundary for
positive, symmetric, edge-normalized profiles. The matching profile satisfies
them at all positive integer sizes. Actual character profiles already have
the boundary from the elementary `P(a,b)<=ab` restriction.

Further work must retain information absent from these families, for example
extracting several label fibers together. A new constraint must force stronger
growth for every relevant character before it can affect $\omega$.

The concurrent proof at `712c91a` supplies another compatibility argument;
see [the pinned comparison](concurrent_research.md) and its
[local proof](../research/ai/2026-10-20-affine-direct-sums/research_note.md).
Extending the completed fixed-label grid cannot produce a smaller exponent.

## R3: Search outside identical single-source sectors

Status: open. The flattening obstruction closes only shorter single-convolution sources with identical targets and the stated shared leg.

Update, October 23: [AI-MIXED-SINGLE-COPY-002](../research/ai/2026-10-23-mixed-family-twisted-cubic-screen/RESULT.md)
shows that at most seven of the ten displayed `T4` interpolation factors
can be termwise limits of the standard source evaluation factors under one
common varying shared-space change of basis. This narrows one decomposition
route. General Laurent-polynomial degenerations, cancellations, collisions,
and other target decompositions remain open. A seven-point Hilbert-Burch
flat-limit example shows that point-set curve containment alone cannot
improve the bound. Every seven-set passing the necessary syzygy screen has a
collinear triple, so any seven-point limit must be singular. A stronger test
needs node alignment or information from other factor spaces.

Update, October 20: [closed Koszul rank formulas](../research/ai/2026-10-20-koszul/research_note.md)
reject all 85 saved second-pass packings, including the former optimum. Use
these necessary tests before trying to realize another packing. They do not
exclude all alternatives or establish sufficiency.

The [four-dimensional mixed family](../research/ai/2026-10-20-koszul/research_note.md#6-an-all-size-family-that-these-necessary-tests-do-not-exclude)
survives all three full-space Koszul families and beats P_* for k>=53. Its
canonical target has a border-rank certificate, while the coordinate-weight
source ansatz is excluded by B>=12k-1. Determine its degeneration status under
general basis changes. Passing the rank screens is not a construction; a finite
model refutation still needs a growth argument.

The [all-dimension extension](../research/ai/2026-10-20-koszul/all_dimension_targets.md)
supplies that growth argument for a specific unbounded sequence: realizing its
targets with source overhead below 2.04721048 percent would force omega<9/4.
No such sequence is constructed. The coordinate-weight ansatz has an all-size
50 percent asymptotic overhead obstruction; investigate general bases or a
different construction.

Investigate unequal sectors, tensor-product sources, or explicit basis changes. State all source and target leg dimensions. Certify the resulting coefficient identities or degeneration weights exactly. Account for any auxiliary tensor rather than cancelling it without justification.

The initial monomial search omits arbitrary basis changes and uses weak estimates for unrecognized sectors. Stronger block recognition is a concrete computational task. Record whether a new score comes from a new degeneration or from a stronger estimate on an old sector.

## R4: Establish a uniform gain or an alternative growth mechanism

Status: open. The target $P(a,4a-1)\ge(3+\eta)P(a,a)$ with a character-independent $\eta>0$ is sufficient for improvement. It is not necessary, and it is not proved.

The [completed scaling and rigidity argument](../research/ai/2026-10-20-concavity-equivalence/homogeneous_rigidity.md)
now supplies the earlier curvature draft's analytic bridge from replication,
rank and concavity. No differentiability assumption is needed. An endpoint
character must have limiting shape
`K min(x,y)^(1/3)(max(x,y)+min(x,y)/2)` for some `K>0`.
Find a new asymptotic tensor constraint excluding every such amplitude, or
prove a positive normalized curvature gain. Neither is currently proved.

The [actual-character bridge](../research/ai/2026-10-20-koszul/scaling_rigidity.md)
supplies an overlapping proof with the external rescaling theorem.


A proposed solution must state its quantifiers and scale propagation. A single-size gain, a larger prefactor, or a character-dependent gain tending to zero does not establish the displayed uniform conclusion.

Deliver a proved gain, a rigorous obstruction to this particular gain, or another complete route from a tensor inequality to a smaller exponent.

The [finite amplitude route](../research/ai/2026-10-20-koszul/finite_amplitude.md)
selects S_4 to M106 as a sufficient, unconstructed degeneration. Its
[necessary tests](../research/ai/2026-10-20-koszul/finite_target_screens.md)
pass all singleton quantum functionals but exclude coordinate inputs even
with arbitrary Laurent output. The next question is a construction with
actual input mixing or a necessary test that covers such mixing. The
all-power coordinate matrix-extraction method is also excluded at a=5 by
an entropy refinement; repeating that class at these diagonals cannot
supply the finite gain.

A [smaller sufficient target](../research/ai/2026-10-20-koszul/cyclic_finite_target.md)
is A_4 to M(10,10,11), where A_4 has leg dimension 112. The minimum-slice-rank
proof excludes all constant linear maps, so a construction needs a singular
limit as well as input mixing. The later
[polynomial rank-locus theorem](../research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
closes all four ordinary A5 targets that passed the old minimum-only
screen. The [updated balanced rectangular frontier](../research/ai/2026-10-21-rectangular-ordinary-frontier/proof.md)
uses the existing higher Hankel gates and excludes every improving ordinary
single matrix shape through a=7. At a=8, M(27,28,28) is the sole sorted
necessary-test survivor; its maps remain missing. Singular A4 constructions
remain open. The [one-sided partial-unit theorem](../research/ai/2026-10-23-one-sided-unit-image/proof.md)
excludes every Laurent pole order if one long map has a regular rank110
limit, the identity lift is regular and its image rank is at least107.
In that regular-long-map chart, continue only at unit-image rank at
most106 or with a polar identity lift; singular long-leg limits are a
separate open class. The [highest-pole flag restrictions](../research/ai/2026-10-23-unit-image-pole-flags/proof.md)
force a first-map pole at rank106, with leading image in a source ruling
of dimension at most four. Its complete principal part has rank at least
six and its pole order is at least two; no simple first-map pole is possible.
At ranks102 through105 a polar first map has
one fixed Hankel factor in its highest coefficient. These constrain only
the highest pole and do not fix the lower Laurent coefficients.

## R5: Compare external formulations before duplicating work

Status: open. The [route map](route-synthesis.md) compares the spectral,
block-identity, and polynomial-separation interfaces. The
[entropy-only oriented lift](oriented-lift-relaxation.md) projects exactly to
its scalar matched-decomposition inequalities, even when decompositions share
different legs. The exact Filmus convolution neighbor, square-tripling, and
general-tripling shared-leg identities, replication degeneration, and
componentwise restrictions give concrete graph rows. The `P_*` potential
bounds every certificate using those rows and input-swap symmetry. From any
rectangular source `C(u,v)` of border rank `u+v-1` to a thin terminal
`C(q,1)`, it gives `qL<=P_*(u,v)` and
`P_*(u,v)^3<=(u+v-1)^4`, with equality only at `C(1,1)`. The general
`C(q,1)` terminal isomorphism and replication/restriction wrappers are
written but not locally formalized. A candidate constraint absent from the
scalar profile must add other exact shared-leg maps or tensor-level data. The
pinned full oriented profile laws also admit the critical common shape at
weights `(3/4,3/4,3/4)`, so those rows alone do not exclude the endpoint;
this screen is tracked as `AI-R5-ORIENTED-PROFILE-SCREEN-001`. A successful
certificate still needs
nonnegative weights satisfying every balance and terminal inflow
`L>1/d` with `(dL)^3>r^4`. No qualifying graph or smaller exponent has been
established.
The scoped row-family obstruction is tracked as
`AI-R5-CONVOLUTION-GRAPH-BARRIER-001`.

Continue by finding and certifying additional identities or endpoints that
escape the scalar potential barrier, or by finding a different tensor-level
constraint that excludes the critical spectral behavior. The numeric endpoint
inequality alone is not a certificate. Keep external lemmas attributed to
their sources.

## R6: Make search results stronger and reusable

The [ordered monomial audit](../research/ai/2026-10-23-ordered-monomial-audit/README.md)
independently replays the pinned PR118 exact certificates and checks both
orders of the input dimensions in the existing binary/ternary scopes.
All 394,960 cases are nonviolating. The first input is distinguished, so
the historical a<=b scope must not be silently treated as both orders.
Its [recognition lemma](../research/ai/2026-10-23-ordered-monomial-audit/recognition.md)
proves that arbitrary coordinate permutations cannot improve exact single
convolution recognition inside addition supports beyond the current
ordering/reversal tests. Stronger bounds for rejected sectors or actual
changes of basis remain possible. This does not prove an all-weight bound.

Status: open. Replace floating best-case ordering in a maintained search copy with exact rational ordering. Add canonical support certificates and replayable witnesses. Preserve the historical code unchanged.

A useful patch demonstrates an incorrect ranking, stronger certified block score, better search coverage, or lower computational cost at identical coverage. Report negative results with parameters and actual counts. Do not report unfinished runs as completed.

The maintained [convolution support recognizer](convolution_support.md) now
handles arbitrary independent coordinate permutations with replayable
bijections. Its relabeled C(3,4) control raises the certified block profile
from the archived slice estimate 4 to 70/9. This is stronger recognition of
an existing block, not a new degeneration or an improved exponent. The
unchanged monomial searches and PR118 ranking work remain separate.

## R7: Whole-filtration entropy beyond the balanced obstruction

Status: settled for the explicit upper certificate `U` by
[AI-UNEQUAL-ENTROPY-001](../research/ai/2026-10-20-unequal-entropy/research_note.md).
For every `a,b,c,d>=2`, its sharp ratio to `P_*(a,b)P_*(c,d)` is at most
`B=(81/350)*(1+14*sqrt(14)/27)^(4/3)`, with
`0.974772906<B<0.974772907`. Equality occurs only at `(2,2,2,2)`;
every other tuple has ratio at most `97/100`. An all-size analytic reduction,
eight polynomial cones, exact tail certificates and their finite residuals
prove this result; it is not an extrapolation from a grid.

The earlier [full-filtration note](../research/ai/2026-10-20-full-filtration/research_note.md)
supplies the optimistic score and its all-distribution bound by `U`.
Singleton input marginals retain that note's direct maximum-block bound.
The new proof is written and unreviewed. It closes this score as a way to
exclude the matching profile, without excluding other constructions or
establishing a weighted block-extraction theorem. Further construction work
must use information absent from this score.

## Work selection

The product worker's [paired-source calculation](../research/ai/2026-10-20-paired-sources/research_note.md)
now includes an [all-power rank formula](../research/ai/2026-10-20-paired-sources/all_koszul.md).
It excludes the initially selected P_6 to M(6,10,6) target at power seven.
The complete finite frontier through a=13 excludes all 239 improving,
dimension-compatible single matrix shapes modulo B/C exchange. Do not fit
those closed targets. Larger paired matrix targets, joint extraction from
paired factors, and genuinely varying recoupling bases remain construction
questions. Passing a necessary rank test would not supply a degeneration. The new
[quantum recoupling question](../research/ai/2026-10-20-quantum-recoupling/QUESTION.md)
uses genuinely varying bases near a root of unity. Its regular initial
maps have insufficient size; tensor-level cancellations remain to be found.
The [leading-flag follow-up](../research/ai/2026-10-20-graded-quantum-flags/QUESTION.md)
now closes several prescribed root flags even with arbitrary higher jets.
Changing the first-leg jet cutoff does not escape those proofs. Different
leading flags and weight-breaking projections remain construction questions.

The [paired-long-leg theorem](../research/ai/2026-10-23-paired-bundle-injectivity/proof.md)
now gives full column rank for both long-leg Koszul maps, with short
input, for every a>=2 and 0<=p<=a(a-1), over every field. Those degrees
cannot exclude a padded target. A further long-leg screen of the 28
short-leg survivors through a16 must use intermediate degrees: [183,363],
[211,419] or[241,479] for a14,15 or16. The same proof gives full row
rank above these intervals and an all-degree source rank lower bound.
These remaining degrees and the actual
target maps are open. The theorem is written and unreviewed.

The [sharp kernel-onset continuation](../research/ai/2026-10-23-paired-kernel-onset/proof.md)
also gives an all-degree source rank upper bound from fixed short input
directions. Its exact screen of the pinned 28-target frontier excludes
no target. The source lower bound settles 2,970 intermediate comparisons
beyond the endpoint intervals; the rest remain undecided. A stronger
route must control coupled short directions or supply target maps.
The [cokernel identity](../research/ai/2026-10-23-paired-kernel-onset/cokernel.md)
makes the intermediate source-rank gap exactly H^1 of the kernel bundle,
with the other rank terms explicit. Controlling its connecting maps is
the next precise obstruction question; the Euler bound alone is insufficient.

The [two-block paired frontier](../research/ai/2026-10-20-paired-direct-sums/README.md)
supplies a smaller source-size construction question. The complete
one-block/two-block search through `a=10` leaves 19 pairs, all at size ten,
after every first-leg Koszul test. Construct or exclude
`P10 -> M(4,11,10) direct_sum M(10,12,6)`; the proved conditional
implication is `omega<2.242`. Ordinary constant maps are already excluded.
The active branch is `research/paired-frontier-unequal-entropy-20261020`.
Any witness must certify its full coefficient identity and singular limit.

An exact [boundary-chain family](../research/ai/2026-10-20-paired-construction/README.md)
now constructs `P_a -> M(a,2,a)` over every field. Its score is below the
improvement threshold for every `a`. It supplies a positive calibration
for wider middle modes, disjoint chains, or singular extensions. Four
first-order Laurent fits and two bounded refinements on the specified
size-three two-block target failed their complete coefficient equations;
their numerical results are not exclusions of larger ansatz classes.

Two bounded second-order Laurent pilots also retain nonzero pole
coefficients. Narrow-source coefficient and kernel searches for
`Q_(3,2) -> M(3,2,3)`, including complex kernels, supplied no exact maps.
Further work needs a new chart, anchor, structural basis, or argument;
repeating the same local runs is not a new construction route.

The [coupled quantum families](../research/ai/2026-10-21-paired-quantum/coupled_faces.md)
provide two exactly specified intermediate tensors of format `(9,15,15)`.
The rank-two slice of `F1` excludes every further degeneration to the
selected concise minimum-slice-three target. Continue the singular
construction question from `F0`, or choose a target outside that
exclusion. Passing its Koszul tests does not prove extractability.

The [unequal root-eight continuation](../research/ai/2026-10-21-narrow-quantum/README.md)
constructs 23 exact limits of `Q_(3,2)`, all excluded from the proposed
`M(3,2,3)` target. The strongest two fail only a long-leg Koszul test among
the comparisons recorded, so every candidate must be checked on all three
legs with the correct zero padding. The original source passes all 25
such comparisons. Further searches need different bases or singular
families; passing this necessary-condition screen is not a construction.

The active fat-point construction question is quantified in the
[all-degree growth route](../research/ai/2026-10-20-concavity-equivalence/fatpoint_growth_route.md).
It requires a genuine convolution-source degeneration at cost below
`9/(7*2^(1/3))`; no such construction is supplied. New linear bases and
matrix-space degenerations are open. The finite rank screens do not decide it.
The [finite-group construction campaign](../research/ai/2026-10-20-group-potentials/README.md)
is owned on `research/full-filtration-entropy-20261020`. Rank-locus dimensions
exclude two previously reported SL(2,5) targets under general degeneration;
only (10,10,10) survives the finite degree-sum/rank-locus frontier. Constructing
that degeneration would give a smaller exponent, but no witness exists here.
Affine-group searches use exact abelian-coset and normal-table constraints.
Avoid repeating the earlier unnormalized searches without a new reason.

The [semisimple full-space continuation](../research/ai/2026-10-21-semisimple-koszul/proof.md)
supplies a new exact SL(2,F8) source and screens every improving integer
format. The selected M(18,18,25) target passes all stated necessary tests
and would imply2.245 if constructed. Its first full-D18-subgroup pilot
timed out without a pair model. The later
[subgroup-ideal proof](../research/ai/2026-10-21-sl2-f8-ideals/proof.md)
excludes that frame by244<450, independently of the timeout. The search
entry point now replays that exact obstruction before importing SAT
dependencies. A new construction must change the frame and respect the
complete-coset cuts; improving that excluded pilot cannot help.
This is distinct from the active SL(2,5) native
parity work. The general complex tests retain16 formats for SL(2,F8).
The separate affine source F8^2:C7 retains21 formats after its full-space
Koszul exclusions.

Read the current claim ledger, open issues, and active branches before selecting a task. Record the task and mathematical question before a long run. Prefer a question that can change a theorem, remove an assumption, or eliminate a specific search family.

The [complete central-cover subgroup catalog](../research/ai/2026-10-21-subgroup-ideal-catalog/README.md)
now supplies every inclusion-minimal subgroup-ideal coset cut for the
three specified targets. Further subgroup enumeration or new cyclic
classes in these same sources cannot add a minimal cut for these targets.
The [finite cube certificate](../research/ai/2026-10-21-central-cover-finite-slices/proof.md)
now forces abc<=986 for every one-copy coefficient-one coordinate/potential
single target in the split cover A5 x C2, excluding M10 and M(9,10,11).
Do not continue those split-cover searches in that class. A construction
with general complex input mixing or a different source/power remains a
separate question. The [actual nonsplit finite covers](../research/ai/2026-10-21-sl2-finite-slices/proof.md)
now exclude M10 in SL(2,F5) and every single target with abc>=2482 in
SL(2,F5) x C2, including M(13,13,15), in the same one-copy coordinate/
potential class. These three selected coordinate searches are closed.
Further work must address a different target, higher source powers or
general complex input mixing; do not infer exclusion of those cases.

The [characteristic-two cost barrier](../research/ai/2026-10-21-a5-peirce/proof.md)
now limits the global asymptotic slice-rank approach for these same three
central-cover targets. Its explicit tight limit gives source costs above
their M10 and M(13,13,15) comparison thresholds. Refining an eventual
global characteristic-two source-power slice-rank upper bound cannot
cross those thresholds. The separate finite cube exclusion uses a
finite dip below the target threshold, not a better asymptotic cost.
Map-specific restrictions, other characteristics and actual constructions
outside its stated class remain separate questions.

The [blockwise modular S5 bound](../research/ai/2026-10-21-s5-block-filtration/proof.md)
excludes coordinate/potential constructions of M20 and M(19,20,21) in
S5 x C2^2, despite their passing the general complex rank-locus and full
Koszul screens. Apply its all-power joint-rectangular inequality before
searching further central-source targets. The [finite weighted cube continuation](../research/ai/2026-10-23-s5-finite-covers/proof.md)
now excludes the one-copy M19 coordinate target and 38 additional shapes
from the previous frontier. The one-central-factor M(13,14,14) remains
open, along with the two and nine remaining shapes listed in that proof.
General complex maps and constructions from higher powers are separate
questions; do not restart the closed one-copy M19 coordinate search.

The [higher-power degree-cover boundary](../research/ai/2026-10-23-s5-higher-powers/proof.md)
now shows that no coordinate cover of the full separately bounded S5
degree majorant can exclude any of those eleven remaining targets at any
power n>=36. This includes nonmonotone and three-unequal-leg covers of
that majorant. Finer actual support, other bases or decompositions, and
powers below 36 remain separate questions; the theorem is not a lower
bound on the actual source's slice rank.

For SL(2,F8), the [modular source bound](../research/ai/2026-10-21-sl2-f8-modular/proof.md)
now constrains every source power and joint rectangular coordinate target.
It excludes repeated six-packet-plus-M7 assembly in that class, while all 16
single-target complex-test survivors remain open to this test. The
M(18,18,25) maps and general complex singular assembly are still missing.

Verification and discovery are separate activities. A new conjecture is useful when it has evidence and a testable consequence. Label it as a conjecture rather than withholding it or promoting it to a theorem.

## Source singular-space caps and the remaining flag bridge

The [all-size disjoint-unit theorem](../research/ai/2026-10-23-all-size-unit-packing/proof.md)
closes the source packing question: every complex all-singular coefficient
subspace of A_a has dimension at most a^2(2a-2), with equality attainable.
The proof covers all sizes; more fixed-size unit searches do not strengthen
this cap. The A4 consequence forces a regular leading first image to be
all-singular of dimension at most96 when a109-column regular long frame
exists. Arbitrary Laurent degenerations need not satisfy those frame or
regularity hypotheses. The next structural question is to force suitable
frames or constrain the smaller singular leading images, or construct the
target in the remaining charts. The exponent improvement remains open.

## Linear-annihilator frontier update

The [pencil-degree theorem](../research/ai/2026-10-21-hankel-pencil-degree/proof.md)
and its [complete application](../research/ai/2026-10-21-hankel-pencil-degree/application.md)
now close the former ordinary A8 rectangular and square-sum targets.
Every improving balanced single rectangular shape through a9 is excluded;
the first necessary-test survivors of that screen are at a10. The later
[Wronskian application](../research/ai/2026-10-21-hankel-wronskian-cap/application.md)
already excludes every improving ordinary A9 square sum, including the
historical partition (32,6,3), using its credited higher-input-rank gates.
Do not treat that historical candidate as an open ordinary-map target.

The new [kernel-descent strip](../research/ai/2026-10-23-hankel-equality/proof.md)
is a separate pointwise source-structure result: source rank below
ab*r+min(a,b), at deficient scalar symbol rank r, forces a constant
length-r scheme for that slice. Constancy over a whole matrix-parameter
family is not proved, and no new target exclusion is claimed. The
[primitive-degree count](../research/ai/2026-10-23-hankel-annihilator-degree/proof.md)
widened the pointwise strip to min(a(a-r),b(b-r)), with balanced
sharpness for every 2<=r<a. Adding the two moving-variable costs
remains a separate unproved conjecture, with a declared finite pilot. The
[binomial-chart minimum](../research/ai/2026-10-23-hankel-additive-cost/proof.md)
now proves that additive bound for the fixed form V^r-xz U^r and gives
the exact minimum over all polynomial initial moments in that chart.
Other primitive-degree-(1,1) supporting forms remain a separate question. Singular
constructions, including the A4 shear completion, remain separate
questions; the exponent goal still requires an actual construction or a
complete alternative implication.

The [regular-unit A4 obstruction](../research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md)
now closes every Laurent order with one regular full-rank long leg and a
regular invertible source lift of a target identity. Further A4 searches
must escape at least one of those hypotheses; increasing the other map's
pole order alone does not suffice. General singular maps remain open.


## Two regular maps: rank-budget gate

The [regular-leg frontier](../research/ai/2026-10-23-regular-leg-frontier/proof.md)
forces the two regular long A4 maps to have limiting ranks summing to at
most192. A search with both long maps regular must enter that rank region;
increasing the remaining Laurent pole order cannot evade the bound. With
one regular short and one regular long map, the sixteen high-total-rank
survivors are (100,100..107) and (90..97,110). They pass necessary tests
only. Individual scalar balancing extends the long-pair budget to every
Laurent presentation. Smaller rank pairs and exact target construction
remain open. This gate does not choose or assume a regular target unit.

## Nonsplit finite cube degree-model checkpoint

The [October 23 vector-degree continuation](../research/ai/2026-10-23-nonsplit-vector-covers/README.md)
checks source parity and the common principal cover, replays seven bounded
class-cover searches and evaluates all 3372 specified integer weight
vectors. It retains 6155844. The outcome closes only that finite weight
census; numerical class-cover optimality reports are not proof. A further
attempt should preserve finer Peirce-corner information, change basis or
change source power, rather than rerun the unchanged degree model.


## Coordinate leading-kernel gate

The [complete matching certificate](../research/ai/2026-10-23-coordinate-kernel-cap/proof.md)
closes the sixteen mixed high-total-rank pairs from the standalone
regular-leg screen if both regular constant kernels are coordinate in
the canonical source bases. Any such pair must have rank sum at most192,
even with arbitrary later mixing and Laurent poles on the third map.
Search lower leading ranks or noncoordinate leading kernels; repeating
higher jets in the closed coordinate charts cannot evade this gate.


## Dense balanced leading-rank gate

The [simple source-torus transfer](../research/ai/2026-10-23-coordinate-kernel-cap/torus_reduction.md)
removes the coordinate hypothesis from the preceding high-rank pair gate.
Every pair of individually balanced leading target-leg ranks sums to at
most192. At short leading rank100, both long leading ranks are at most92.
Search lower rank triples; arbitrary complex mixing of leading kernels
does not reopen the sixteen closed high-rank mixed pairs. The matrix
target and exponent goal remain open, and the proof is unreviewed.
