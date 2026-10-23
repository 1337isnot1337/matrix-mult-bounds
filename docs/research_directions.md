# Research directions

The [quadratic-z constant-endpoint classification](../research/ai/2026-10-23-quadratic-z-middle/proof.md)
now gives the exact all-field rank
`ab+min(b,ceil(a/2)*d)+min(b,floor(a/2)*d)` of every
`alpha+z*v(x)+gamma*z^2` slice, with both nonzero outer coefficients
constant and `d=deg(v)` (zero for v=0). The
[three-term counterexample](../research/ai/2026-10-23-three-term-resultant-obstruction/proof.md)
already separates ranks with identical coefficient degrees and pairwise
resultants in characteristic different from two. The general quadratic
continuation below now computes both minimal indices for arbitrary outer
coefficients. Its root-height dichotomy now restricts the first index;
attainability within the remaining high interval and constraints on linear
families remain open.
Use PR209's row-polynomial
convention with full degree endpoints, while retaining PR207/208 ownership
of diagonal Toeplitz cases. One-slice rank information is insufficient to claim
a better matrix-multiplication exponent: compatible three-leg maps
and the complete implication remain missing.

The [quadratic-kernel classification](../research/ai/2026-10-23-quadratic-kernel-indices/proof.md)
gives a finite exact procedure for the two kernel indices of arbitrary
`u(x)+z*v(x)+z^2*w(x)` with coefficient degrees below a, a>=2 and b>=3,
and hence its literal slice-matrix rank. For D>0 after common-factor
normalization, the zero first-index case is characterized by a fixed
ground-field linear factor.
The [root-height dichotomy](../research/ai/2026-10-23-quadratic-kernel-indices/dichotomy.md)
now bounds the first index and proves the full a=b=3 biform-block
rank spectrum. The next question is which splitting types in the remaining
high interval are attainable for each a,D and field, and how factor geometry
constrains linear families rather than individual slices. Preserve exact
full-output coefficients and distinguish
these individual-slice constraints from a source-space cap or a full
matrix target. The claim remains written and unreviewed.

The [single-top-polynomial biform rank theorem](../research/ai/2026-10-23-top-coefficient-biforms/proof.md) settles, over every field, the literal one-slice ranks for f(x,z)=c_0+...+c_(e-1)*z^(e-1)+w(x)z^e with constant lower coefficients, c_0 nonzero, and arbitrary polynomial w of degree d<a. The formula is ab+sum_j min(b,d*floor((a+j)/e)). It is a distinct special-family formula. The general quadratic continuation now treats arbitrary u(x)+z*v(x)+z^2*w(x) with a bounded two-index test and a rational-root-height restriction, including the complete a=b=3 biform-block rank spectrum. Its remaining high-interval attainability and linear-family questions, and higher z-degree families with several nonconstant coefficient polynomials, remain open. Keep this separate from the diagonal Toeplitz lane credited to PR207 and the affine-in-z lane credited to PR209; a single rank formula is not a tensor target.

The [three-term resultant obstruction](../research/ai/2026-10-23-three-term-resultant-obstruction/proof.md) disproves classification of individual R_(3,3) ranks from primitive coefficient degree and all three pairwise resultants alone. The exact determinant separates rank 14 and 15 despite identical invariants. The general quadratic continuation now computes both minimal indices of the recurrence u*lambda_r+v*lambda_(r+1)+w*lambda_(r+2)=0 for arbitrary degree-<a coefficients by a bounded exact coefficient-matrix test. The root-height dichotomy now restricts those indices; the remaining structural question is to describe attainable positive-index strata and compatible linear families through subresultants or polynomial-factor geometry; require a full three-leg source-to-target map before claiming a smaller exponent. Do not repeat PR207's diagonal Toeplitz lane.

These directions combine independent branch checkpoints. Read the cited
continuations together: later scoped obstructions can close an earlier proposed
search, while broader singular constructions may remain open. Historical test
receipts and intermediate frontier values are not current validation claims.
Written proofs remain unreviewed unless their individual evidence record says
otherwise.

## Rank-two first-slice gap and mixed first maps (October 23)

The [paired rank-two gap](../research/ai/2026-10-23-paired-rank-two-gap/proof.md) gives rank S_Y >= b(b+1) for every rank-two first coefficient matrix of Q(n,b), sharply. At width four this is 20, strengthening the generic previous 17 for rank two. To apply it to an ordinary corrected target, prove that a sufficiently large residual-annihilator family has source coefficient rank two and then control compression losses through the two actual long kernels. The theorem alone does not imply that arbitrary mixed first maps have rank-two images, nor does it extend to singular Laurent maps. A future construction should provide actual tensor maps or prove a precise rank-two-image implication, not assert an exponent gain from the source rank gap alone.

## Full-source singular maps: escape the closed constant-compression family

The [independent coordinate census](../research/ai/2026-10-23-a4-coordinate-compressions/proof.md)
now has sharp outer image dimension 40, so every independent coordinate
compression of the fixed two-sided A4 family is excluded. Its exact
equality witnesses retain a sharper bound for that finite class. The
separate universal theorem below closes arbitrary complex subspaces U
and W through graded flags and exact minor identities.

The [two-sided A4 conjugation result](../research/ai/2026-10-23-conjugation-limit/proof.md)
computes the complete limiting space for `g=I+t^-1 N`, with the fixed
rank-sixteen square-zero source slice N. A full matrix target can occur
after constant long-leg compression only on the locus
`dim(P L C)<=103`, where at least nine leading directions disappear.
All principal two-coordinate deletions are excluded by a complete exact
census. The [universal compression proof](../research/ai/2026-10-23-a4-compression-algebra/proof.md)
now excludes every constant compression in this fixed family. Do not
repeat those searches. The next constructive question is whether moving
compressions or a different singular path avoid the obstruction. A candidate must
supply every target coefficient; a large limiting-space dimension alone
does not identify matrix multiplication.

The [exact low-rank reduction](../research/ai/2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md)
reduces this fixed family's constant-compression question to the explicit
46-dimensional outer space `E=G+[G,G00]+G00 G G00` in `Mat28`.
The new theorem proves that no rank-26 pair has
`dim(Phat E Chat)<=37`: every such image has dimension at least 38.
It retains arbitrary complex input/output subspaces through a torus
limit and exact minor arguments. This closes the constant-compression
question for the specified path. A new positive trajectory must leave
that class and still supply complete re-saturation and all target
coefficient identities. The theorem does not claim the bound 38 is sharp.

The [recorded two-factor and nonnilpotent follow-ups](../research/ai/2026-10-23-conjugation-limit/EXPLORATION.md)
already close every principal coordinate compression for those two exact
families. Their full rational re-saturation coverage is retained. A new
experiment should change the compression class or singular family and
still use complete target coefficient identities as its acceptance test.

The [full-right-inverse Laurent criterion](../research/ai/2026-10-23-regular-unit-projector/proof.md)
gives a general map-regularity theorem without a low-rank-spanning target
hypothesis. Its A4 unit-image corollary is subsumed by concurrent PR113's
written exclusion of every chart with one regular full-rank long map,
including polar original units. The criterion's rank101 equality is not
an active A4 gap. PR125 and PR142 separately use shared correction spaces
and source ruling geometry to address singular balanced long-map limits.
All these results remain written and unreviewed, with no constructed
matrix target or exponent improvement.

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

The [diagonal-polynomial block theorem](../research/ai/2026-10-23-diagonal-biform-ranks/proof.md)
now computes single-source-slice ranks for f(xz) from d explicit
Toeplitz ranks, and completely resolves the quadratic case over every
field. The next independent question is simultaneous rank loss among
the central Toeplitz blocks at degree>=3. Such single-slice information
must not be confused with a full matrix-tensor degeneration or an
exponent bound. The binomial and arbitrary-biform workers retain their
separate question ownership.

## One-dependency residual slice geometry (October 23)

The [exact rank strata](../research/ai/2026-10-23-oblique-slice-strata/proof.md)
settle the ordinary one-leg contraction ranks of PR147's fixed
one-dependency residual, including both first-leg rank-two components.
They do not determine the residual's border rank or a nonlinear orbit
closure. A useful next step would be a rigorous border-rank condition
using these projective contraction strata that beats the prior equalizer
lower bound; ordinary decomposition-specific peeling does not suffice.
Do not re-run this completed rank-strata census without a new invariant.

The [affine-z biform rank theorem](../research/ai/2026-10-23-affine-z-biform-ranks/proof.md) classifies all individual R_(a,b)(u(x)+z*v(x)) ranks as ab+min(b,a*d) over every field and all a,b>=2. It is a restricted one-slice result and does not imply a matrix target. Its separate next question is the polynomial row-syzygy module for u+z*v+z^2*w, including falsifiable tests of degree-only rank predictions. PR207 owns the diagonal f(xz) Toeplitz defects; do not duplicate that lane.

## Paired maps after the Laurent channel obstruction

The [formal channel lemma](../research/ai/2026-10-23-laurent-channel-barrier/proof.md)
now excludes arbitrary Laurent pole cancellation for the common low
channel-rank families of pending PR157, PR173 and PR179, including
near-full outer targets and arbitrary auxiliary maps. Increasing only
the pole order in these classes cannot meet the subquadratic repair
criterion. A construction should instead produce full generic channel
rank, remove the common factorization, or use genuinely nonlocal maps.
The precise hypotheses concern the full K((t)) family, not just its lead.
The [rank-margin refinement](../research/ai/2026-10-23-laurent-channel-barrier/rank_margin.md)
strengthens auxiliary border rank to d+h-rho-1 for d>=1 and rho<h,
while preserving the first-flattening bound d. Its constant improvement
at fixed width does not change the remaining construction problem.

## October23: operational barrier includes arbitrary common-input mixtures

The [rank representation](../research/ai/2026-10-23-common-input-rank-barrier/proof.md)
extends the polynomial operational barrier to every actual complex
degeneration among finite Full/Mid partial sums at the same full first
dimension, with arbitrary widths, multiplicities and first-leg bases.
Two long-leg dimension inequalities already settle heterogeneous targets
from identical source blocks. The prior Pass-packing argument remains
available with fewer structural dependencies. New construction work must
leave the stated Full/Mid class, for example through shared-output blocks
or smaller first subspaces. Supply complete tensor identities for a
candidate that survives the necessary rank screens. No smaller exponent
or unrestricted lower bound follows from these method obstructions.

## October 23: escape the rational-normal-curve obstruction

The [mixed candidate](../research/ai/2026-10-23-mixed-longlegs-candidate/global_rnc_obstruction.md)
is excluded for every independent target first identification, despite
passing every ordinary Koszul degree and the stated Schur screens. Its
rank-one third-slice first projection is a finite union of smooth
quartics; proper incidence and Hilbert polynomial rigidity normalize any
proposed first map and reach the120<130 catalecticant contradiction.

Find a score-improving target whose rank-one projection permits a singular
quartic limit. Width-one Full blocks are one concrete mechanism because
their projection is all of the first projective space. Check the required
multiplicity, dimension balance and A-leg Koszul inequalities before
more expensive rank computations. Then supply actual Laurent maps or a
complete orbit-closure proof. Passing these requirements is still not a
construction. Source copies with independent first identifications are
outside the current canonical-source theorem and form a separate question.

The [all-size first-gap classification](../research/ai/2026-10-23-rank20-ruling/all_sizes.md)
now gives a sharp source linear-space dimension2a at rank cap a^2+a for
all a>=2, with a uniform Laurent ruling obstruction. This is written and
unreviewed; selected-size source and margin controls are finite evidence.
Higher rank caps still require additional geometry.

The [rank20 source classification](../research/ai/2026-10-23-rank20-ruling/proof.md)
proves a sharp vector linear-space bound eight and extends the singular
long-leg exclusion below to balanced leading rank105. Remaining A4 target
candidates must have leading ranks at most104 on both long maps. The
next source-geometry cap is21: the rank20 classification is not asserted
there, and finite sparse examples cannot supply that universal premise.
All these obstructions remain written and unreviewed, without a target
construction or exponent improvement.

The [shared-correction ruling criterion](../research/ai/2026-10-23-singular-long-ruling/proof.md)
now excludes an A4 target whenever either scalar-balanced long-map limit
has rank at least106, even with arbitrary poles in both other maps and
the original identity lift. Every remaining candidate must have rank at
most105 in both balanced long-map limits. The next source-geometry
question is a dimension bound for linear spaces of slices of rank at
most20: at c105 the existing gap no longer places the whole ruling image
in the minimum cone. No such sharper bound or target construction is
assumed. This written unreviewed continuation credits PR113's correction
mechanism and the existing source gap, including its external splitting
dependency. It is separate from local conic incidence and does not lower
the exponent.

The [geometric diagonal-source theorem](../research/ai/2026-10-23-geometric-diagonal-ranks/proof.md) gives a closed formula and explicit kernel bases for all central Toeplitz rank defects of geometric-coefficient diagonal slices. It builds on concurrent PR207's broader all-degree decomposition. Remaining work must go beyond this coefficient family, or use the exact defect spaces in a *compatible three-leg* tensor construction. Low rank in a single source slice is not a degeneration. Claim AI-GEOMETRIC-DIAGONAL-RANKS-001 is written and unreviewed, and there is no exponent gain.

These are proposed investigations, not claimed results. Each task has a concrete output and an explicit path to a downstream claim.

The [prescribed third-jet criterion](../research/ai/2026-10-23-conic-fixed-third-obstruction/proof.md)
now gives order-four and all-order extension exactly on Delta=0, on the
d-nonzero mixed chart. The [full two-jet curve](../research/ai/2026-10-23-conic-fixed-two-curve/proof.md)
uses a different third coefficient and still extends at every point of
that chart. The projective normal-class theorem below now checks all
base-chart ranks and transitions. Describe which other prescribed
third coefficients extend; normal-class existence leaves that question
distinct. Mere homogenization alone would not establish the boundary
rank hypotheses.

The [fixed-two conic curve](../research/ai/2026-10-23-conic-fixed-two-curve/proof.md)
now extends PR107's entire prescribed two-jet on d nonzero, with exact
polynomial maps of degrees eight and nine and no other parameter guards.
Its kernel stays fixed, whereas PR107's prescribed third kernel
coefficient is nonzero. The fixed-third criterion above now settles its
extension locus. The projective criterion above covers the remaining
base charts. An extension of one specified two-jet does not classify
all boundary velocities or construct the full matrix target.

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
The projective extension separately supplies the remaining base charts.
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
now proves rank six sharply over every field. The
[complete low-rank locus](../research/ai/2026-10-23-resolvent-rank-six/proof.md)
is a 17-dimensional linear space with common six-dimensional image; rank
seven is absent. Two rank109 compressions lose at most one direction over
algebraically closed fields, sharply. The [loss-seven bound](../research/ai/2026-10-23-resolvent-loss-seven/proof.md)
now leaves at most two kernel directions at total loss seven, sharply,
and extends the bounds to every field. The next structural question is
total loss eight, where rank-eight matrices outside the classified locus
can enter the compression kernel. Check broader long-map exclusions
before treating any aligned compression as a possible matrix target.
The independently retained [all-field locus](../research/ai/2026-10-23-resolvent-rank-six-locus/README.md),
[compression-frontier implementation](../research/ai/2026-10-23-resolvent-rank-six-frontier/README.md),
and [finite-certificate implementation](../research/ai/2026-10-23-resolvent-rank-six-finite/proof.md)
have separate evidence records and retain their individual field hypotheses.
The earlier [rank-six family pilot](../research/ai/2026-10-23-resolvent-rank6-family/proof.md)
is a predecessor construction inside this classified locus. Other directions
include a different nilpotent, higher resolvent corrections, or varying singular
compressions; none of these classifications constructs the full matrix target.

## Paired long-leg rank screen

Conditional on the unreviewed filtered-bundle proof in PR #169, an exact
comparison closes degrees 183–209, 211–241, and 241–274 for every saved
short-leg survivor at `a=14,15,16`, respectively. The remaining
intermediate degrees and any actual source-rank upper bounds are open.
Continue only with a new structural source-rank bound, exact intermediate
ranks for smaller cases, or a proof that the target comparison cannot
exclude the saved formats. The finite comparison is in
[`paired-long-leg-target-screen`](../research/ai/2026-10-23-paired-long-leg-target-screen/README.md).

The [exact binomial biform formula](../research/ai/2026-10-23-binomial-biform-ranks/proof.md)
calibrates all two-monomial coordinate pairs, including nondivisor
offsets, with no characteristic restriction when both coefficients
are nonzero. At equal offset d the rank deficit from a(a+d) is
`r(d-r)`, where r is a modulo d. Use the exact formula before treating a
nondivisor pair as forbidden. It does not classify larger supports or
their bounded-rank linear spaces. The elementary binomial gap can also
replace the specific input in PR148 after an explicit dependency update.

The [complete fixed-resolvent rank-six locus](../research/ai/2026-10-23-resolvent-rank-six-frontier/README.md)
is a 17-dimensional constant-image space over every field. Two rank109
compressions lose at most one dimension, with all nontrivial kernel/image
pairs classified. The next structural question is whether this polynomial
normal form controls the additional leading coefficients introduced by
varying singular compressions or a changed resolvent. Constant compression
alone does not answer it. Check the broader long-map exclusions before
treating any such trajectory as a possible matrix target.

The [singular-long-rank theorem](../research/ai/2026-10-23-singular-long-rank/proof.md)
now excludes A4 target charts in which either scalar-balanced long map
has limit rank at least 106. Do not repeat those charts. Both ranks at
most 105 remain open. At rank105 the active-ruling argument reaches
source rank20; a sharper bound on linear spaces in that source rank
locus is one concrete next question. The result uses the previous
source rank gap and PR113's unit-kernel correction and proves no target.

## The existing polynomial operations have an external barrier

Amanov, van den Berg and Zuiddam, [arXiv:2610.30054v1](https://arxiv.org/html/2610.30054v1),
prove an operational barrier for their formal preorder.
The existing polynomial ingredients and stated combination rules cannot
improve the square or rectangular exponent bounds by themselves.
An additional search constraint must arise from a new tensor relation
or an argument outside that specified calculus.

The [local paired-repair deduction](../research/ai/2026-10-23-operational-repair-barrier/README.md)
shows that formal near-full fixed-width repairs cannot cost `O(n^alpha)`
for any fixed `alpha<2`. Its finer `n^2/ln n` coefficient is optimal over
the entire external F_theta family, including the simplex corners.
Optimizing those parameters cannot strengthen that leading coefficient.
This barrier does not exclude actual tensor degenerations. The paired construction target below remains open.
New maps must be verified directly, including their auxiliary costs.

## Active paired construction: finite maps and concentrated residuals

The [residual-rank criterion](../research/ai/2026-10-23-residual-rank-repair/proof.md)
gives a finite stopping condition. For an actual complex degeneration
`Q(n,b) + E -> M(l,h,r)`, let D be the smallest product of two certified
residual flattening ranks. The strict comparison
`(lhr)^(3/4)>D^(3/4)+sqrt(2b(2n+b-1)^3)/3` would imply `omega<9/4`.
No unbounded extension is needed for this qualitative finite implication.
No map passing it is known here. The smallest full-target source formats
under this paired criterion have largest leg 441, at Q(21,8) and Q(21,9).
For width four, Q(200,4) to M(199,4,199) with residual ranks at most
(2,796,796) is another sufficient, unconstructed finite target.

For a numerical exponent bound, the earlier
[linear-correction criterion](../research/ai/2026-10-21-correction-budget/README.md)
asks for genuine `Q(n,4) + E_n -> M(n-c,4,n-c)` along an unbounded sequence,
with fixed c and `border_rank(E_n)=O(n)`. It would imply
`omega < 30000/13433 < 2.2334`. The new residual-rank proof also accepts
first residual rank `O(n^(7/10))` and both long ranks `O(n)` for the same
conditional rational ceiling. More generally, sublinear first-rank growth
has the quantified gamma-dependent bound in that proof. These families
remain unconstructed.

The active paired branch has an
[exact integer Q(5,4) to M4 witness](../research/ai/2026-10-20-paired-construction/outer_product_injection.md)
and the family `Q(k+1,k) -> M(k,4,k)`. Its source width grows with k,
so it does not prove the fixed-width premise. The small target
`Q(6,4) -> M(5,4,5)` remains a discovery problem beyond the recovered
product-subspace dimension limit; it does not pass the finite improvement
criterion by itself. Search for nonproduct long maps, singular limits,
or identities whose residual is concentrated in a small first-leg space.
Deliver exact coefficient identities and rank certificates. A small
floating residual norm does not establish any of these premises.

The [variable-coefficient shift-window theorem](../research/ai/2026-10-23-shift-window-long-legs/QUESTION.md)
rules out subquadratic ordinary corrections to M(n,m,n) for fixed m when
B bulk coefficients have polynomial degree at most m-2, shared recurrence
order below m or, more generally, a common proper m-shift span, while C is
Toeplitz and both bandwidth and exceptional-column counts are sublinear.
For Q(6,4), investigate exact full-rank-window B coefficient maps outside
the existing diagonal-shift and product charts. This is an exploratory
finite target: the theorem's bound is zero at n=6,m=4 and does not establish
that full span is necessary for M(5,4,5). No matrix target or exponent bound
is proved.

The [first-support capacity theorem](../research/ai/2026-10-23-first-support-capacity/README.md)
requires generic long-map surjectivity whenever auxiliary first rank is
below the target's outer dimensions, even for Laurent maps with cancelling
poles. Fixed widths below four incur quadratic first-support repair.
For ordinary maps, a dual first map of the form H(x,y)F(u)(x)G(v)(y)
with fixed nonzero H incurs at least `max(0,2n-10c-19)` first support;
the companion capped bound is stronger near its n>=9c+14 threshold.
Searches for smaller errors must change that first-map form or use a
singular construction. These bounds leave linear repair costs open and
do not classify arbitrary first maps.

The [diagonal continuation](../research/ai/2026-10-23-diagonal-first-support/README.md)
now allows arbitrary off-diagonal perturbations that vanish on the
diagonal. If `L(u u^T)=H F(u)G(u)` as a polynomial identity, the
n=200,c=1 ordinary target requires first residual rank at least 176,
or 188 with injective F,G. Its shift-transpose example shows that low
coefficient rank on a Segre section alone does not recover the earlier
product class. An actual construction must address the two shared
long-map kernels. This diagonal theorem still permits linear repairs
and does not apply to Laurent degenerations.

The [fixed oblique-repair atlas](../research/ai/2026-10-23-oblique-koszul-atlas-extended/README.md)
checks every unprojected full-space Koszul map of the one-dependency
residuals at r=3,4,5,6. None improves the earlier equalizer lower bound.
For the fixed Q(6,4) maps, stronger secant conditions or better border
repairs remain relevant; repeating these full-space ranks does not narrow
the inherited border-rank interval 12 through 18. Other projections and
maps are outside this finite check.

The [all-size divisor source caps](../research/ai/2026-10-23-divisor-source-caps/proof.md)
give a sharp cap ad for every proper divisor d of a throughout rank
ceilings a(a+d-1),...,a(a+d)-1. This generalizes the credited A4 cap8
without a new A4 cutoff. Their singular-long-leg corollary can be used
as a necessary test for other balanced sizes. Nondivisor strips, rank
ceilings outside the proved intervals and actual target constructions
remain open to this method; finite grid extensions do not prove them.

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

The [staircase counterexample](../research/ai/2026-10-23-source-staircase-spaces/proof.md)
provides a 68-dimensional source space of rank at most 92. A universal
cap of 57 below rank 96 is therefore false; do not pursue it. Seek a
valid cap on a smaller rank interval or exploit additional structure of
actual cancellation kernels. The [sharp rank-37 cap](../research/ai/2026-10-23-rank37-source-spaces/proof.md)
may also help mixed target-leg questions, but such an application needs
its own complete support argument and has not been asserted here.

The [rank-80 source theorem](../research/ai/2026-10-23-torus-rank80/proof.md)
originally bounded source dimension by 50 below slice rank 80 and the
balanced long-rank sum by 144. The source cap is now sharpened to 44 above;
the target sum is not asserted sharp. Seek source-space
bounds at higher slice ranks, or use additional source structure in the
saturated support inequality on the surviving region. Check explicit supported-row and supported-column spaces before
proposing a numerical cap at a higher threshold. The separate individual
rank-101 cap remains.

The [order-ideal source theorem](../research/ai/2026-10-23-torus-order-ideal/proof.md)
now proves a sharp dimension32 cap below slice rank64 and reduces the
balanced long-rank sum to at most160. The three exact lowering actions
and elementary Grassmannian argument apply to other source rank
thresholds. Seek new complete ideal/minor certificates there, while
keeping the target bound necessary and the surviving region unconstructed.
The individual rank101 cap also remains in force.

The [rank-48 source-space theorem](../research/ai/2026-10-23-torus-rank-frontier/proof.md)
forces the two scalar-balanced long-map ranks to sum to at most176,
strengthening concurrent PR122's sum192 bound. The separate
[sharp rank23 cap](../research/ai/2026-10-23-torus-low-rank/proof.md)
limits each rank to at most101. Do not repeat the excluded region.
Determine bounds for larger low-rank source spaces, or add source-specific
constraints to the saturated target-support inequality on the remaining
region. Neither the dimension24 bound nor sum176 is asserted sharp.
The [initial singular-long theorem](../research/ai/2026-10-23-singular-long-rank/proof.md)
retains the credited regular kernel correction and active-ruling argument;
its former rank105 boundary has been superseded by these extensions.

The [rank91 core theorem](../research/ai/2026-10-23-rank91-core/proof.md)
forces mixed balanced pair sums at most 133 and total leading rank at
most 198. It retains the long-pair bound 136 and all frozen202 exclusions.
The high-threshold continuation below restricts each positive long rank
to 1 through 12 or 20 when the short rank is 100. Arbitrary complex
kernels, higher coefficients and finite Laurent poles on the remaining
map are allowed. The two surviving total-198
integer triples are (62,66,70) and (62,70,66); neither constructs a
target presentation. The new source cap is 67 strictly below rank 91,
without a sharpness claim.

A bounded next question concerns the long pair (66,70). Its cancellation
kernel must have dimension at least 64 and uniform slice rank at most
88, with compression defects (46,42). The existing 64-dimensional
staircase has uniform rank at most 88, so a universal source dimension
cap below 64 cannot settle this pair. Determine whether a 64-space can
satisfy the actual split compression condition. An incidence-preserving
ideal reduction and explicit row/column cover certificates may help;
no classification or exclusion at this endpoint is claimed here.

The [high-threshold source maxima](../research/ai/2026-10-23-high-rank-source-caps/proof.md)
are now 84, 88, 92 and 96 at strict slice-rank thresholds 100, 104,
108 and 112. Their staircase witnesses rule out smaller universal
caps at those same thresholds. The complete Laurent target consequence
at full short leading rank 100 is the necessary long-rank set
{1,...,12,20}, including the gap 13 through 19. Determine whether any
surviving ranks admit target-compatible cancellation kernels and the
complete target equations. The numerical endpoint (100,20,20) is only
a screen endpoint. This full-short result and the rank91 global
refinement have separate source proofs; both necessary conditions apply
in this checkpoint.

The [projective conic criterion](../research/ai/2026-10-23-conic-projective-criterion/proof.md)
now completes the affine prerequisite on every point of the three
projective base lines. Some representative of a nonzero normal class
extends to all orders exactly when
`(a1*r-a0*s)*(b1*r+b0*s)*(s*lambda^3+r*mu^3)=0`.
The first boundary velocity is free. Complete unit certificates establish
the ranks at infinity, and literal source reversal swaps the normal
coordinates. The set of liftable classes has exactly three irreducible
graph components; this is not an incidence-scheme classification.
The projective chart-coverage question is therefore closed. Further work
must address specified boundary velocities or local moduli, or prove an
explicit bridge from this rank-twelve incidence to a full matrix target.
The existing affine criterion stays correct within its original scope.
Neither this global local-incidence result nor its exact curves construct
M(10,10,11) or improve the exponent.

The [credited total202 prerequisite](../research/ai/2026-10-23-leading-rank202/proof.md)
retains its complete all-order support argument and historical arithmetic
screen. Its former numerical endpoint (70,66,66) is excluded by the
rank91 continuation above. Neither screen constructs target-compatible
kernels or a Laurent presentation.

The [sharp source caps below ranks 84 and 88](../research/ai/2026-10-23-rank84-rank88-spaces/proof.md)
are 56 and 60. The [new sharp caps below ranks 92 and 96](../research/ai/2026-10-23-rank92-rank96-spaces/proof.md)
are 68 and 72, attained by spaces with maximum slice ranks 91 and 95.
Smaller universal dimension caps at those same strict thresholds are
impossible. Different thresholds and the special structure of actual
cancellation kernels remain distinct questions.

The [sharp rank-80 source theorem](../research/ai/2026-10-23-rank80-sharp-spaces/proof.md)
settles that dimension cap at 44. Its explicit 44-space has maximum
rank 79, so a smaller universal cap at the same threshold is impossible.
Determine the consequences for mixed target-leg ranks with a complete
support argument, or exploit additional structure of actual cancellation
kernels. A source-space sharpness example is not a target degeneration.

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

The [shift-separation barrier](../research/ai/2026-10-23-paired-shift-separation/README.md)
extends the channel-rank obstruction to one finite-band long-leg map with
variable column coefficients: a displayed profile decomposition whose
combined shift rank is below the middle width still forces a quadratic
ordinary residual. Any next variable-coefficient construction must reach
shift rank at least the middle width or leave this ordinary finite-band
model. The written result is unreviewed and gives no exponent improvement.

The paired-source long-leg continuation proves that both long-leg Koszul
maps of `P_a` have full column rank through `p=a` and gives an all-degree
rank floor from interpolation-block support. At `p=a+1` that floor dominates
both long-leg target ranks for four `a=15` and six `a=16` survivors. The exact
`a=3` atlas is full through `p=6` and has rank `57185/57915` at `p=7`; a
finite `a=4,p=5` atlas also has full rank modulo two across 524 bidegree
blocks. At `a=3,p=8`, the rank is `54135/57915`. The first kernels at
`(a,p)=(2,3)` and `(3,7)` have exact `SL2 x SL2` decompositions, consistent
with a possible first-defect boundary `p=a(a-1)+1`; the larger `p=8` kernel
has dimension `3780`. The exact `a=3` rank profile is now known through
`p=14`; the `a=4` boundary remains open. General
higher-degree ranks remain open. See the [proof and exact controls](../research/ai/2026-10-23-paired-long-legs/long_leg_low_degrees.md)
and the [finite kernel analysis](../research/ai/2026-10-23-paired-long-legs/kernel_module_types.md).

## R1: Review the local sharpness theorem

An internal line-by-line [proof audit](../research/reviews/2026-10-23-scalar-profile/PROOF_REVIEW.md)
at base `dcd209a` found no gap, including positivity of the increments, limiting
slope, and join at $a=b$. This does not count as independent mathematical
review; that review and formalization of the full pointwise-minimality
proof remain open. The auxiliary finite slope estimate is separately checked
in the [scalar-profile Lean project](../formal/scalar-profile/README.md).

The outstanding deliverable is an independent proof review, a correction, or a
counterexample. The internal review and finite grids do not close that task.
Distinguish the earlier recurrence from the local matching construction. A
Lean formalization is separate and is not required for every discovery.

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
single matrix shape through a=7. The original a=8 M(27,28,28) survivor was later closed by the
rectangular saturation continuation; further ordinary frontiers are
tracked by the rectangular direct-sum and finite-state packages. Singular A4 constructions
remain open. The [one-sided partial-unit theorem](../research/ai/2026-10-23-one-sided-unit-image/proof.md)
excludes every Laurent pole order if one long map has a regular rank110
limit, the identity lift is regular and its image rank is at least107.
This was an intermediate regular-long-map threshold. The later
one-regular-leg theorem removes the unit-image and identity-lift
hypotheses, and subsequent source-cap results restrict the singular case. The [highest-pole flag restrictions](../research/ai/2026-10-23-unit-image-pole-flags/proof.md)
force a first-map pole at rank106, with leading image in a source ruling
of dimension at most four. Its complete principal part has rank at least
six and its pole order is at least two; no simple first-map pole is possible.
At ranks102 through105 a polar first map has
one fixed Hankel factor in its highest coefficient. These constrain only
the highest pole and do not fix the lower Laurent coefficients.
These highest-pole calculations remain scoped predecessor constraints;
they do not reopen a regular-long-map case excluded by the broader theorem.

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

The [width-two score theorem](../research/ai/2026-10-23-width-two-monomial/proof.md)
now closes the original scorer for C(2,b) and C(b,2) at all sizes and
all integer weights, with exact equality classification. Its finite
replay covers every support through b=10. Further searches for a score
violation need minimum input size at least three or a stronger valid
sector score; increasing width-two weight bounds alone cannot help.

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

The [width-two support theorem](../research/ai/2026-10-23-width-two-support/proof.md)
closes the historical score on every support subset when either input
dimension is two, for all weights and both input roles. Its scope retains
the single-slice fallback on unrecognized components. New score searches
should use both input dimensions at least three or improve that fallback.

Status: completed for the three recorded search scopes. The
[maintained exact search](../research/ai/2026-10-23-exact-monomial-search/README.md)
orders candidates by rational scores and retains deterministic support and
sector certificates for its exact leaderboards. It replays 12,976 binary,
209,692 ternary, and 20,000 seeded random candidates, with no scored
violation of the profile. A regression test demonstrates that distinct
rational ratios can map to the same float; another preserves the distinguished
shared-leg role. The historical code remains unchanged. Broader weight
families, arbitrary basis changes, stronger unrecognized-block scores, and
any exponent implication remain open.

The maintained [convolution support recognizer](convolution_support.md) now
handles arbitrary independent coordinate permutations with replayable
bijections. Its relabeled C(3,4) control raises the certified block profile
from the archived slice estimate 4 to 70/9. This is stronger recognition of
an existing block, not a new degeneration or an improved exponent. The
unchanged monomial searches and PR118 ranking work remain separate.

The [ordered-input continuation](../research/ai/2026-10-23-ordered-monomial-search/README.md)
completes both input roles in the historical binary/ternary scopes with
24,708/370,252 exact candidates and no violation. An all-size alternating
family shows that the omitted orientation can score strictly better, so
`a <= b` is not a score-preserving or pointwise-dominating reduction.
Stronger recognition or another shared-axis class is needed for new work
at these alphabets and dimension limits; repeating this census is not new
coverage. PR118 retains its separate exact-ranking contribution.

The [nonshared projection continuation](../research/ai/2026-10-23-monomial-projections/README.md)
supplies one stronger estimate: optimize the existing component score over
literal y/z coordinate deletions before splitting components. It improves
581 of 1,623 scores in the complete small ordered binary census through
a+b=8; the a+b=9 binary and a+b=8 ternary continuations improve 1,817 of
4,197 and 6,486 of 24,699. None has a source-profile violation.
This changes the estimate on an
old degeneration, rather than discovering a new degeneration. Larger
projection censuses and stronger per-component estimates remain questions.

The [whole-sector recognition theorem](../research/ai/2026-10-23-monomial-recognition/proof.md)
closes one possible strengthening: on an additive coefficient-one support,
arbitrary coordinate permutations reveal no whole convolution block beyond
the archived sorted-index/reversal test. Stronger scores must use proper
restrictions, additional degenerations, general linear bases or a stronger
bound on nonconvolution sectors. Swapping the two input axes changes the
shared-axis component score; a<=b alone is not a symmetry reduction.

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
now excludes 38 additional shapes from the previous frontier, including
the one-copy M19 coordinate target. At that checkpoint, the two one-central-factor shapes M(13,13,15)
and M(13,14,14), together with nine two-central-factor shapes, were
listed for further work; use the finer covers below for the later frontier.
General complex maps and constructions from higher powers are separate
questions; do not restart the closed one-copy M19 coordinate search.

The [complete SL(2,F8) subgroup catalog](../research/ai/2026-10-23-sl2-f8-subgroup-catalog/README.md)
now supplies every inclusion-minimal averaging-ideal coset cut for the
sixteen saved formats. Use its new order14 cuts on every target leg and
order6 cuts where the other-pair product exceeds455. More subgroup
enumeration in this source cannot add a minimal cut for these formats;
change the necessary condition, construction frame, source or power.

The [finer full-source covers](../research/ai/2026-10-23-s5-peirce-covers/proof.md)
lower the caps to abc<=2576 and abc<=6415. They exclude five additional
two-central-factor shapes, leaving (16,16,25), (16,19,21), (14,19,24),
and (16,20,20). The one-central-factor frontier is unchanged. Further
finite-cover work must use the actual source support: the refined
degrees need not be radical indices, and their triple-degree budget
must be checked separately from the maximum one-leg degree.

The [higher-power degree-cover boundary](../research/ai/2026-10-23-s5-higher-powers/proof.md)
now shows that no coordinate cover of the full separately bounded S5
degree majorant can exclude any of the eleven targets in its original finite-cube checkpoint at any
power n>=36. This includes nonmonotone and three-unequal-leg covers of
that majorant. Finer actual support, other bases or decompositions, and
powers below 36 remain separate questions; the theorem is not a lower
bound on the actual source's slice rank.
That original eleven-target list is the theorem's pinned input, not a claim
that all eleven survive the later finer actual-support covers.

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

The [invertible leading-kernel continuation](../research/ai/2026-10-23-leading-defect/proof.md)
provides a general method for square matrix targets. Its A4 sum204
corollary is weaker than the written sum176 checkpoint in
[PR129](https://github.com/1337isnot1337/matrix-mult-bounds/pull/129),
with later integrated source-cap results giving still stronger scoped
frontiers. Those later results govern subsequent A4 candidate selection. Use
the general kernel lemma in another source or a remaining chart; do not
reopen the already covered defect20..27 interval as a new frontier.

The [one-regular-long-leg A4 obstruction](../research/ai/2026-10-23-one-regular-leg/proof.md)
now closes every Laurent order with either long map regular of rank110 at
zero, without assumptions on the source lift of the target identity. A
regular right-inverse kernel correction removes the earlier unit-image
hypotheses. Further A4 constructions must have rank at most109 in both
long-leg leading coefficients after scalar balancing. Increasing pole
orders while keeping a full-rank long-leg limit cannot escape this proof.
The [singular-long-gap continuation](../research/ai/2026-10-23-singular-long-gap/proof.md)
uses the minimum source gap and a polynomial rank-one-preserver argument
to extend that exclusion to regular limiting long-leg ranks106--109.
This method first forced both scalar-balanced leading ranks to at most105.
At rank105 its lifted rank budget reaches20, so it no longer forces
minimum-rank source images. Later singular-long-rank and source-cap results
listed here further restrict that historical boundary and govern current
candidate selection. The general singular problem remains open; no target
is constructed.

The [singular-unit resolvent obstruction](../research/ai/2026-10-21-singular-unit-resolvent/proof.md)
also closes the specified square-zero resolvent ansatz on a nonempty open
dense set of constant codimension-two compression pairs, allowing arbitrary
first-map Laurent poles. A continuation must address its explicit
candidate-space rank-drop locus, moving compressions, or a different
unit trajectory. This is a conditional chart exclusion, not a general
singular-unit obstruction.

The [unbalanced single-rectangular inventory](../research/ai/2026-10-23-unbalanced-rectangular-frontier/README.md)
now covers every cyclic source2<=a<=b with N<=1377. The adopted written
gates exclude2110 of2113 improving shapes. Only A(8,9) survives, with
targets M(28,31,31), M(29,30,31) and M30. Seek actual maps for these
formats or a stronger valid obstruction. Their rank-seven Hankel case
fails the strict linear-annihilator hypothesis35<34 and cannot be
excluded by extending that theorem's numerical range without proof.
This finite single-target result does not cover rectangular direct sums
or general singular maps.

The [regular-unit A4 obstruction](../research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md)
now closes every Laurent order with one regular full-rank long leg and a
regular invertible source lift of a target identity. The
[rank-locus continuation](../research/ai/2026-10-23-unit-image-rank-gap/proof.md)
weakens invertibility to a regular unit image of rank at least107,
including source unit slices of corank at most three. The
[stacked-product refinement](../research/ai/2026-10-23-unit-image-stacked-rank/proof.md)
further reaches image rank105, including corank at most five, by a2q
rank count and a bounded rank-one kernel. Retained rank104, singular
long-leg limits and polar unit lifts remain outside that proof.
Further A4 searches must escape its hypotheses; increasing the other map's
pole order alone does not suffice. General singular maps remain open.

## Joint central-cover matrix-plus-scalars checkpoint

The [exact nonsplit cube continuation](../research/ai/2026-10-23-central-cover-joint-frontier/README.md)
closes every strict improving one-copy coefficient-one coordinate/
potential target M(a,b,c) plus r scalar tensors from SL(2,F5). Its
1012332 source cube bound rejects all three earlier-screen survivors.
Do not continue that complete family in the stated class. Arbitrary
complex maps without the good reduction, more general joint matrix
families and higher source powers remain separate open questions.
The next finite target is exactly two matrix components plus scalar
components, with all three leg dimensions at most120. For components
`M(a_i,b_i,c_i)`, the cyclic cube expands over ordered triples `(i,j,k)`
to `M(a_i*b_j*c_k, b_i*c_j*a_k, c_i*a_j*b_k)`; sum the exact rectangular
slice-rank values, then combine with the joint rank-profile, Koszul and
cost gates. A complete enumeration is still needed before claiming an
exclusion.

The [complete unbalanced square-sum application](../research/ai/2026-10-23-unbalanced-square-frontier/README.md)
now fills the source-dimension gap through1377. All70 formats below1152
are excluded for an improving ordinary square direct sum; the first
necessary-test survivor is A(8,9), not the balanced A9 source. In
particular its unconstructed single M30 target passes this package's adopted gates
and has an exact conditional exponent certificate5621/2500. Construct
its actual coefficient maps or find a stronger obstruction in this
unbalanced format. The
[Wronskian application](../research/ai/2026-10-21-hankel-wronskian-cap/application.md)
already excludes all improving ordinary A9 square direct sums, superseding
the A9 survival under the older adopted gates. The unbalanced A(8,9)
question remains distinct.
The earlier balanced single-rectangular enumeration and all singular
construction questions retain their stated scopes.

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

## Rank84/88 interval refinement and the sum136 boundary

The [sharp source-cap continuation](../research/ai/2026-10-23-rank84-88-source-caps/proof.md)
closes balanced long leading sums137..144 and forces sum at most136.
Source dimensions below matrix ranks84 and88 are exactly bounded by56
and60, with the prior staircase examples attaining those dimensions.
At balanced ranks68,68 a prior64-dimensional source space of rank at
most88 already meets the two dimension/rank cancellation-kernel conditions.
A universal cap smaller than64 at rank at most88 is therefore impossible;
examine actual two-sided compression incidence or compatible higher maps.
No such kernel or target has been constructed, and the proofs are unreviewed.

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

## Fifth-power continuation for two-matrix candidates

The [nonsplit two-matrix screen](../research/ai/2026-10-23-nonsplit-two-matrix-targets/README.md)
uses fifth-, sixth- and seventh-power source bounds of 9874344844,
991166716704 and 100070673945707 to exclude eight, ten and one rows from a
pinned 144-candidate two-matrix frontier. Its earlier pair census and
complex screens are not regenerated, and the other 125 candidates only
pass these necessary screens. The next finite continuation is to build and
replay an eighth-power source cover against those 125 candidates. This
remains within the existing one-copy coefficient-one good-reduction
premise and does not claim an exponent improvement.

The [sharp pencil family](../research/ai/2026-10-23-hankel-index-sharpness/proof.md)
now realizes every integer equality in the Hankel annihilator degree
budget. At `(a,b,r)=(10,10,8)` it has constant projective rank and
quadratic annihilator, so a weak-inequality extension of the prior
pencil-linearity argument is false. Every linear Hankel extension of this
prescribed seed is now classified: the unique maximal one has dimension
2epsilon, equal to four at A10. Do not try to grow a larger linear ruling
while retaining this entire pencil. Other quadratic pencils and genuinely
bilinear Segre images remain open. These results neither change the
ordinary target frontier nor decide the separate A9 square-sum equality
question.

## Quadratic Hankel lines inside the saturated four-space

The [four-space line criterion](../research/ai/2026-10-23-hankel-fourspace-pencils/proof.md)
gives `det N=-4*Delta*chi^3` for arbitrary lines in moments 3,7,11,15.
Under chi nonzero, Delta nonzero closes every linear extension beyond
that four-space. Delta zero gives a seven-dimensional common tangent
space; the full displayed paired exceptional family, beta cubed different
from one, is nevertheless closed by quadratic and higher rank equations.
Continue with other chi-nonzero/Delta-zero
lines or quadratic pencils outside this four-space. Do not infer that
seven common tangent directions supply seven linear extension directions.

For the three A(8,9) survivors, use the stronger recorded input-rank
constraints: rank at most three in selected nonsquare first-parameter
spaces, or rank at most two for M30, must map to Hankel rank at most7.
Determine the resulting symbol-image dimension using these determinantal
input varieties. No such stronger dimension theorem is currently proved.

## Rank-three input continuation for unbalanced A(8,9)

The [rank-three proof](../research/ai/2026-10-23-rank-three-hankel/proof.md)
excludes the ordinary M(28,31,31) and M(29,30,31) formats from PR138's
unbalanced single-target inventory. A Borel-fixed projection budget
and a codimension-two result for large rank-seven Hankel sections
contradict their rank-three parameter images. The proof is written and
unreviewed. M30 remains open: its rank-two image constraint is compatible
with a13-through16-dimensional symbol image under the same budget.
Seek a stronger rank-two image theorem, explicit M30 maps, or singular
constructions. Do not transfer the rank-three exclusion to that case.
