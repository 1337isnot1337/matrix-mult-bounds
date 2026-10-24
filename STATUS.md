# Research status

## Geometric quadratic equality classification over every field

The [quadratic equality package](research/ai/2026-10-24-quadratic-equality/README.md)
classifies every six-dimensional geometric rank-at-most-fourteen family in the
nine-coefficient R_(3,3) block over every field: it is the full space with a
common nonzero kernel vector or a common nonzero left-kernel vector.
In odd characteristic, the tangent quadratic at an invertible coefficient
point has rank at least five, excluding a six-space through such a point.
In characteristic two, the proof classifies the singular five-dimensional
middle-coefficient section and excludes noncompression extensions using
polynomial source determinants and a highest-degree factor argument.
Both proofs descend to the original field. Claims
`AI-ODD-QUADRATIC-EQUALITY-001` and `AI-CHAR2-QUADRATIC-EQUALITY-002` remain
written and unreviewed. The retained five odd-prime controls and five symbolic
characteristic-two source identities are corroboration, not independent review.
Compatible tensor maps, submaximal families and larger blocks remain open.
No exponent improvement is established.

## Sharp geometric rank14 dimension bound over every field

The [quadratic determinant package](research/ai/2026-10-23-quadratic-determinant/README.md)
proves that a geometrically rank-at-most-14 linear family of the complete
nine-coefficient R_(3,3) block has dimension at most six over every field.
A fixed-factor family attains six.
The universal integer identity
`2048 det(R)=det(M) det(2 adj(H)-tr(adj(H)) I)`, with
`H=M^T J M J` and `J=[[0,0,-2],[0,1,0],[-2,0,0]]`, splits the argument.
The coefficient-singular branch has dimension at most six by an elementary
incidence proof. At every invertible zero of the degree-twelve factor,
a three-dimensional tangent subspace has a nondegenerate quadratic
second variation. A seven-dimensional linear family would intersect it
in a two-dimensional totally isotropic space, which is impossible.
This local algebra argument includes nonsemisimple matrices and all odd
characteristics. In characteristic two, an integral form of the invariant
factors the literal source determinant as D^2 G, with D=det(M). On the
hyperplane m11=0 it becomes D^5. An elementary classification of singular
six-spaces and an explicit full-rank extension exclude a seven-space.
Finite examples are separate corroboration.

An independent rational proof lifts the prior binary full-rank certificate
by clearing denominators and removing a common power of two. Its full-rank
three-space is a Q-point assertion, not a geometric full-rank family.
Claims `AI-QUADRATIC-DETERMINANT-INVARIANT-001`,
`AI-RATIONAL-QUADRATIC-LINEAR-CAP-002`, and
`AI-GEOMETRIC-QUADRATIC-LINEAR-CAP-003`, and
`AI-CHAR2-GEOMETRIC-QUADRATIC-CAP-004` remain written and unreviewed.
The separate equality package above now classifies maximal families over every field. No compatible tensor target or exponent
improvement follows from these block-subspace results.

## Exact rational quadratic attainment

The [rational quadratic package](research/ai/2026-10-23-quadratic-rational-attainment/README.md)
gives the exact nonzero balanced rank set over Q for every a>=3:
`{a^2,a^2+a,a^2+2a}`, with `a^2+2a-1` added precisely when
`gcd(a+1,210)>1`. It applies the merged line-bundle criterion to the
Jacobian in the smooth case, importing Mazur's rational torsion theorem
with its original credit. A separate gluing argument handles all singular
and doubled boundaries without assuming a rational point on the curve.
Explicit integer recurrence witnesses supply orders two, three, five,
and seven. The integer identities give orders two, three and five over
every field, and seven outside characteristic two. The new order-five
model is outside the previously failed
sixteen sign lifts. Claim `AI-RATIONAL-QUADRATIC-SPECTRUM-001` is written
and unreviewed. This is an individual quadratic-block classification,
with no source-space bound, compatible tensor target or exponent gain.

## Explicit split and doubled quadratic attainment

The [split-quadratic formula](research/ai/2026-10-23-quadratic-split-attainment/proof.md)
computes the recurrence kernel for `(z-x)(z-t*x)` over every field with
`t` nonzero. For `t!=1`, the balanced one-unit defect occurs exactly when
`t^(a+1)=1`; for the doubled graph `t=1`, it occurs exactly when the
positive characteristic divides `a+1`. The explicit kernel gives the
rectangular rank as well; the exceptional index pair affects the rank
only when b=a. Roots of unity or the doubled graph therefore attain all
four balanced quadratic ranks over every algebraically closed field,
for every a>=3. This does not assert universal attainment over the
rationals or a particular finite field. Claims
`AI-SPLIT-QUADRATIC-RANK-001` and `AI-ALGEBRAICALLY-CLOSED-QUADRATIC-SPECTRUM-002`
are written and unreviewed. No tensor target or exponent improvement follows.

## Sharp dimension-six bounds for quadratic slice families

The [quadratic linear-space package](research/ai/2026-10-23-quadratic-linear-spaces/README.md)
proves a sharp dimension-six bound for F2-linear families of the complete
nine-coefficient R_(3,3) biform block that avoid rank15. The proof uses
seven full-rank matrices in a three-dimensional subspace and dimension
intersection. Independently, over every field, a geometrically rank-at-most-12
family has dimension at most six, by the vertical/horizontal factor loci.
A fixed-factor family attains both bounds. Exact finite enumeration finds
six binary extremal rank12 spaces and twenty rank14 spaces. Six of the
latter lie outside coefficient compression; an explicit F4 point in one
has rank15, demonstrating the scalar-extension boundary. Claims
`AI-BINARY-QUADRATIC-LINEAR-CAP-001` and
`AI-GEOMETRIC-QUADRATIC-RANK12-CAP-002` are written and unreviewed;
`AI-BINARY-QUADRATIC-EXTREMAL-CENSUS-003` is finite-experiment evidence.
These are block-subspace results, with no compatible tensor maps or
matrix-multiplication exponent improvement.

## Exact binary quadratic attainment from a degree-zero line bundle

The [torsion criterion](research/ai/2026-10-23-quadratic-torsion/proof.md)
identifies the balanced one-unit defect, for primitive degree two without
a fixed ground-field root, with triviality of `O_C(a+1,-a-1)` on the
associated bidegree-(2,2) curve. This works over every field, including
reduced singular and doubled curves. Over F2 it gives the exact nonzero
quadratic-in-z rank set for every a>=3:
`{a^2,a^2+a,a^2+2a}`, with `a^2+2a-1` added exactly when
`gcd(a+1,30)>1`. The proof uses a geometric order bound and explicit
order-two, order-three and order-five witnesses; it does not extrapolate
finite periodicity. Separate exact controls partition264 triples into16
projective orbits and compare176 literal source ranks. Claims
`AI-QUADRATIC-TORSION-CRITERION-001` and `AI-BINARY-QUADRATIC-SPECTRUM-002`
are written and unreviewed. The binary classification is restricted to
quadratic-in-z blocks, with no full cyclic-source or exponent result.

## Rational-root heights restrict the quadratic indices

The [structural sequel](research/ai/2026-10-23-quadratic-kernel-indices/dichotomy.md)
shows that a minimum recurrence vector either has degree at least
`ceil((a-1)D/2)` or comes from a rational root of height h and degree
`(a+1)h`. It proves this through explicit polynomial Hankel kernel bases
and the arbitrary-field matrix-polynomial index-sum theorem. An irreducible
homogeneous quadratic forces the higher range; a sufficiently low rational
root height determines both indices exactly. As a concrete consequence,
the complete nonzero fifteen-by-fifteen biform-block rank spectrum at
a=b=3 is `{9,12,14,15}` over every field. Rank thirteen is impossible,
and explicit universal witnesses attain all four remaining values.
For every balanced a=b>=3 quadratic-z family, ranks lie in
`{a^2,a^2+a,a^2+2a-1,a^2+2a}`; universal attainment at larger sizes
is not asserted. The one-below-full value requires primitive D=2.
Claim `AI-QUADRATIC-INDEX-DICHOTOMY-002` is written and unreviewed.
This does not classify all slices of the full cyclic tensor or supply
an exponent improvement.

## General quadratic biform ranks from two kernel indices

The [quadratic-kernel theorem](research/ai/2026-10-23-quadratic-kernel-indices/proof.md)
makes the rank of every nonzero `u(x)+z*v(x)+z^2*w(x)` slice computable
over any field, with coefficient degrees below a, a>=2 and b>=3.
After common-factor normalization, let D be the largest coefficient degree.
The two polynomial-kernel indices sum to aD; the first is the first degree
at which the explicit recurrence coefficient matrix has a nonzero kernel,
which occurs by floor(aD/2). The full source rank is
`ab+min(b,mu1)+min(b,mu2)`. For positive D, a zero first index is equivalent
to a fixed ground-field linear factor in the homogeneous z-quadratic.
This specializes the prior kernel-bundle identity and adds an effective
two-index procedure. Exact finite controls compare 2050 complete source
matrices, including the earlier equal-resultant ranks14/15 and their
characteristic-two behavior. Claim `AI-QUADRATIC-KERNEL-INDICES-001` is
written and unreviewed. No source-space cap, compatible matrix target,
singular degeneration or exponent improvement is established.

## All-field ranks of single-top-polynomial biforms

The [top-coefficient biform theorem](research/ai/2026-10-23-top-coefficient-biforms/proof.md) computes the literal cyclic-source matrix R_(a,b) for every f(x,z)=c_0+...+c_(e-1)*z^(e-1)+w(x)*z^e with 1<=e<b, nonzero constant c_0, constant lower coefficients, and nonzero polynomial w of x-degree d<a. Over every field, its exact rank is ab + sum_(j=0)^(e-1) min(b,d*floor((a+j)/e)). The leading polynomial-kernel vectors form a triangular residue basis, giving a complete all-field proof. The new controls pass 3,372 full-matrix modular comparisons and 24 independent-implementation rational matrix ranks. Claim AI-TOP-COEFFICIENT-BIFORM-RANK-001 is proof-written-unreviewed. It does not classify arbitrary quadratic-in-z coefficients, build a three-leg tensor target, or improve omega below 9/4. The separate [continuation](research/ai/2026-10-23-top-coefficient-biforms/CONTINUATION.md) records exact scope and provenance.

## Full-channel paired maps: overlap and leading rank loss

The [column-overlap proof](research/ai/2026-10-23-column-overlap/proof.md)
allows arbitrary full channel matrices at each retained polynomial column.
For fixed injective routing, an overlap graph bounds the leading target
slice intersection. Saturation accounts for new directions from singular
leading blocks, even with arbitrary first-map and auxiliary Laurent poles.
At fixed width and near-full outer dimensions, all but o(n) invertible
leading blocks force auxiliary border rank n^2-o(n^2). Equal positive
fractions above 1/m of invertible leading blocks also force quadratic
cost by the stated quantitative bound. General column-mixing maps and
more extensively singular leading blocks remain open. Claim
`AI-PAIRED-COLUMN-OVERLAP-001` is written and unreviewed. Exact separated
window restrictions and a full-channel sharp flattening example test its
scope; no exponent improves.

## The prescribed full conic two-jet extends to all orders

The [fixed-two-jet curve](research/ai/2026-10-23-conic-fixed-two-curve/proof.md)
preserves every entry of PR107's B0,B1,B2,C0,C1,C2 and the two supplied
kernel corrections Y1=Y2=0. For every complex a,b,d with d nonzero and
c=-d^3, it gives exact polynomial maps of degrees eight and nine over
Q[a,b,d,d^-1], with actual d-pole bounds five and six. There are no
additional a,b or Delta guards. The complete product stays on the same
twelve first-source coordinates; constant minors1,1,-1 give formal
ranks14,14,12. Exact replay checks all18 product orders and all352800
kernel coefficient positions. Six focused tests and a separate sparse
Laurent reconstruction pass. Claim `AI-CONIC-FIXED-TWO-CURVE-001` is
written and unreviewed. This closes the prescribed two-jet question on
the stated chart. PR107's full third jet, which has a nonzero kernel
correction, remains a separate question. No full matrix target or
improved exponent is established.

## The prescribed full conic first jet extends to all orders

The [fixed-first-jet curve](research/ai/2026-10-23-conic-fixed-first-curve/proof.md)
strengthens the earlier cubic-component construction: for every complex
a,b,d with c=-d^3, both full constant and first coefficient maps of
PR107 extend to exact cubic maps B(t),C(t) over Q[a,b,d]. The supplied
first source-kernel correction is also preserved. Complete source
replay checks all seven possible product coefficients; the fixed kernel
and unit minors give formal ranks14,14,12. The construction includes
d=0 and the linear-component intersections without parameter inverses.
Claim `AI-CONIC-FIXED-FIRST-CURVE-001` is written and unreviewed.
Its second coefficients differ by boundary terms, so preservation of
PR107's full two-jet is not asserted here. The full matrix target and
an improved exponent remain unconstructed.

## Polynomial all-order curves on the cubic conic component

The [all-order criterion](research/ai/2026-10-23-conic-polynomial-curve/all_order_criterion.md)
completes normal-class existence on the full affine conic base chart:
for every complex a,b,c and nonzero[lambda:mu], a suitable first tangent
extends to a formal (indeed polynomial) incidence curve exactly when
`(a-c)*(b+c)*(c*lambda^3+mu^3)=0`. Necessity is PR101's complete
second-order obstruction; sufficiency combines its linear-component
curves with the polynomial cubic-component curve below. Claim
`AI-CONIC-ALL-ORDER-CRITERION-002` is written and unreviewed. All
projective normal directions are included; other projective base charts
and extension of a prescribed full tangent remain distinct questions.

The [polynomial-curve proof](research/ai/2026-10-23-conic-polynomial-curve/proof.md)
constructs an exact curve for every complex a,b,d with c=-d^3, including
d=0. The two fourteen-row maps have polynomial t-degrees one and three,
with coefficients in Q[a,b,d] and no parameter denominators. Their
complete contraction stays on the same twelve first-source coordinates;
constant unit minors certify formal ranks14,14,12. Literal replay checks
all five possible product coefficients against the original4096-term
source. The first normal class is exactly[1:d] and never vanishes.
The curve changes the boundary part of the first tangent, so it does not
settle extension of a prescribed full first or second jet. Claim
`AI-CONIC-POLYNOMIAL-CURVE-001` is written and unreviewed. The full
M(10,10,11) target and a smaller exponent remain unconstructed.

## Mixed conic lifts through order four and a rational order-ten witness

The [higher-jet proof](research/ai/2026-10-23-conic-higher-jets/proof.md)
extends PR107's mixed family through order four for every complex a,b,d
with d nonzero and c=-d^3. The explicit coefficients lie in
Q[a,b,d,d^-1], with d-pole order at most three. A separate rational
witness extends the point a=1,b=2,d=1 through order ten. Both preserve
PR107's constant, first and second coefficients. The symbolic and
rational acceptance programs contract the literal 4096-term source
and check every moving-kernel coefficient, with leading ranks14,14,12.
Claims `AI-CONIC-MIXED-FOURTH-JET-001` and
`AI-CONIC-RATIONAL-TENTH-JET-002` are written and unreviewed. These are
rank-twelve incidence jets with specified lower coefficients. The separate
polynomial curve above gives all-order existence after allowing boundary
velocity to change; it does not preserve these specified lower jets.

## Third-order lifts on the mixed cubic conic component

The [third-jet witness](research/ai/2026-10-23-conic-third-jets/proof.md)
extends PR101's first jet through order three for every complex a,b,d
with d nonzero and c=-d^3, after changing its second coefficient. The
coefficient ring is Q[a,b,d,d^-1], with poles of order at most two in d.
Independent symbolic replay rebuilds the 4096-term integer source and
checks all 19600 moving-kernel coefficients at each positive order;
leading minor determinants1,1,-1 give map row ranks14 and first-source
rank12 throughout this chart. An earlier explicit rational point also
has a separate standard-library replay. Claims
`AI-CONIC-RATIONAL-THIRD-JET-001` and `AI-CONIC-MIXED-THIRD-JET-002`
are written and unreviewed. The later packages above supply fourth-order
lifts and all-order existence for the normal class, with their distinct
lower-coefficient conditions. The full matrix target remains open.
No smaller exponent is established.

## Sharp rank six in the fixed-resolvent matrix space

The [fixed-resolvent certificate](research/ai/2026-10-23-resolvent-minrank/README.md)
proves that its 112-dimensional limiting matrix space has minimum nonzero
ordinary matrix rank exactly six over every field. Thirty-one triangular
six-by-six minor identities eliminate every parameter of the difficult
outer block, and an explicit rank-six witness proves sharpness. Thus every
two-sided compression with total rank loss at most five is injective.
At rank109 on both long maps, a lost direction must have rank six and obey
the stated kernel/image alignment. Claim `AI-RESOLVENT-SHARP-MINRANK-001`
is written and unreviewed. This refines the fixed-resolvent space from
PR103; its narrow target application is superseded by the regular-long-map
argument. General singular trajectories, all rank-six matrices and an
improved exponent are not settled.

## Nonsplit vector-degree continuation: no finite bound gain

The [vector-degree experiment](research/ai/2026-10-23-nonsplit-vector-covers/README.md)
checks every original nonsplit coefficient, finding the 95 principal
degree triples of even total at most eight. Seven bounded class-cover
runs replay exactly, and a complete 3372-vector integer weight census
combining degree and the saved principal cover retains the cube bound
6155844. Claim `EXP-NONSPLIT-VECTOR-COVERS-001` is a finite experiment.
Numerical optimality reports are not accepted as class-wide exclusion
certificates. No improved bound or exponent follows. A new attempt needs
additional basis structure or a changed source/basis/power.

## All-order A4 exclusion with a partial regular unit image

The [partial-unit-image argument](research/ai/2026-10-23-regular-unit-image/proof.md)
extends the previous invertible-unit Laurent chart. A4 cannot degenerate
to M(10,10,11) if one long map C is regular with full-rank limit, the
source lift of the target identity is regular, and its limiting image
`S(0) C(0)` has rank at least109. In particular, singular source units
of corank one are included. Independent source frames and varying
left inverses first force both other maps to be regular; the existing
ordinary-map obstruction finishes the argument. Every finite pole order
is covered. Claims `AI-PARTIAL-UNIT-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-EXCLUSION-002` are written and unreviewed. Exact finite
controls verify the rank budgets and projection recovery, without
formalizing the proof. Rank108, singular long-leg limits and polar unit
lifts remain open. No matrix target or smaller exponent is established.

## Finite covers close the selected nonsplit coordinate targets

The [actual nonsplit source certificate](research/ai/2026-10-21-sl2-finite-slices/proof.md)
gives a 98-slice cover for SL(2,F5), excluding M10 in characteristic two
and in the maintained one-copy coefficient-one coordinate/potential
class over C. For SL(2,F5) x C2 its cube has a 6155844-slice cover, below
2535^2=6426225. Cyclic symmetry gives abc<=2481 for any single rectangular
target, excluding the selected M(13,13,15). Independent replay checks
rank120, all1728000 original nonsplit coefficients, full block degrees,
and grouped cube coordinate counts with multiplicity13824000. Claim
`AI-NONSPLIT-FINITE-COVERS-001` is written and unreviewed. Together with
the split-cover result, this closes the three selected one-copy
central-cover coordinate/potential targets. General complex input mixing,
other targets and arbitrary higher source powers remain open. No smaller
exponent is established.

## Complete affine conic tangents and second jets

The [conic second-jet proof](research/ai/2026-10-21-conic-second-jets/proof.md)
computes the complete seventy-dimensional tangent module of the rank-twelve
incidence of two fourteen-row maps of the canonical source. Its boundary
family has dimension68 and uses three independent polynomial planes.
For every affine a,b,c and every nonzero normal class[lambda:mu], some
representative extends through order two exactly when
`(a-c)*(b+c)*(c*lambda^3+mu^3)=0`. All68 boundary motions are included;
pure fibers are checked separately from the mixed Laurent chart.
An exported polynomial two-jet on c=-d^3 passes direct all-source replay,
including d=0, while its uncorrected third coefficient has184 nonzero
entries. The other two factors admit exact linear incidence curves.
Claims `AI-CONIC-TANGENT-001`, `AI-CONIC-SECOND-JET-002` and
`AI-CONIC-POLYNOMIAL-JET-003` are written and unreviewed. The later polynomial-curve package completes all-order existence on
the cubic component for a suitable first representative. Other projective
base charts, the separate12-by8 problem and the full matrix target remain open. The exponent remains9/4.

## Finite cube bounds split-cover coordinate target volume

The [full-source cube certificate](research/ai/2026-10-21-central-cover-finite-slices/proof.md)
gives a characteristic-two slice cover of 973422 for `(A5 x C2)^3`, below
the exact finite slice rank 1000000 of M1000. Cyclic symmetry gives the
single-target volume bound abc<=986. It excludes the maintained one-copy
coefficient-one coordinate/potential M10 and M(9,10,11) constructions in
the split cover. The verifier checks all 216000 A5 coefficients and enumerates
all 1728000 one-leg cube coordinates. A direct argument from the external
arbitrary-field bounded-rank matrix-space theorem supplies the target
lower bound. Claim `AI-SPLIT-COVER-CUBE-EXCLUSION-001` is written and
unreviewed. The separate nonsplit note above addresses its selected
coordinate targets. General complex degenerations and constructions
from arbitrary higher powers remain open. No smaller
exponent is established.

## Regular unit charts and full-source calibrations

The [unit-chart proof](research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md)
excludes A4 to M(10,10,11) at every Laurent order when one long map is
regular with full-rank limit and a target identity has a regular source
lift with invertible limiting slice. The other long map and remaining
first-map coefficients may have arbitrary finite poles. Regularized
correction products have rank at most two; the source minimum rank 16
eliminates first-map poles and then forces 100 dimensions into at most 98.
Claim `AI-CYCLIC-REGULAR-UNIT-003` is written and unreviewed. Singular
long-leg limits and singular or polar unit lifts remain outside it.

The [integer slice proof](research/ai/2026-10-21-cyclic-slice-determinants/proof.md)
gives a literal unimodular full-rank slice of A_a for every a>=1 and every
field. At a=2,3,4, exact Krylov/Bezout certificates prove the full source
determinant is reduced over C; its submaximal minors have no nonconstant
common divisor. Normalized slice commutators also attain full rank in
those sizes. These calibration facts reject two proposed full-source invariant
premises. They do not exclude matrix targets or factor arguments after
compression or leading-flag restriction. Claims `AI-CYCLIC-UNIMODULAR-001`
and `AI-CYCLIC-REDUCED-DETERMINANTS-002` are written and unreviewed.
The general singular A4 target and exponent question remain open.


## Characteristic-two source-cost barrier for the central covers

The [A5 tight-limit certificate](research/ai/2026-10-21-a5-peirce/README.md)
checks an explicit basis and all 216,000 source coefficients, giving a
tight 277-term limit. A rational distribution and integer entropy
comparison prove a written lower barrier for asymptotic slice-rank costs
in characteristic two: above 517/5 for A5 x C2 and SL(2,F5), and above
976613/5000 for SL(2,F5) x C2. An explicit central-cover limit transfers
the certificate to both covers. These values exceed the selected M10
and cyclic M(13,13,15) comparison thresholds, so eventual global source
slice-rank bounds of this kind cannot close those targets. This barrier
alone leaves finite-power tests and constructions undecided; the separate
cube result above now closes the one-copy split-cover coordinate class.
Claim `AI-CENTRAL-COVER-SLICE-BARRIER-001` is written and
unreviewed; no smaller exponent is established.

## Modular SL(2,F8) bound across source powers

The [modular source proof](research/ai/2026-10-21-sl2-f8-modular/proof.md)
constructs an exact 125-dimensional semisimple quotient over F2 and F8,
certifies a 379-dimensional nilpotent kernel, and separates the 64-dimensional
central summand. The resulting all-power coordinate/potential slice bound
is 1035637/2304, below 450. It excludes the joint six M(8,9,9) packets plus
M7 across source powers, extending the prior one-copy coordinate assembly
obstruction. All 16 general-test single-matrix survivors remain unexcluded,
including M(18,18,25). Claim `AI-SL2-F8-MODULAR-001` is written and
unreviewed; arbitrary complex maps and the exponent goal remain open.

## Complete subgroup-ideal catalog

The [complete finite catalog](research/ai/2026-10-21-subgroup-ideal-catalog/README.md)
certifies all 455 subgroups in 65 conjugacy classes of the three active
central-cover sources. Integer annihilators and matching modular ranks
give every averaging-ideal dimension. In PSL(2,5) x C2, noncyclic
order-four and order-six subgroups add 550 minimal forbidden cosets per
leg of M10 beyond central pairs and the earlier five-cycle cuts.
The other two specified targets have no additional minimal subgroup
coset cuts. This is completeness for a finite necessary-condition method,
not exclusion of the targets. The weighted 3-by-3 control passes. A new
600-second search reached 34 model events and 32 replayed parity
contradictions with no pair-injective lift; it ended at its time limit.
Claims `EXP-SUBGROUP-IDEAL-CATALOG-001`
and `AI-SPLIT-NONCYCLIC-COSETS-001` remain finite or written and unreviewed.
Arbitrary complex maps and the exponent below 9/4 remain open.

## Complete coupled boundary rank-two reduction

The [coupled cubic proof](research/ai/2026-10-21-coupled-boundary-rank-two/proof.md)
shows that both canonical boundary obstruction matrices have rank at most
two precisely when both are zero. Its 232 universal determinant identities
reduce the normal dimensions 228 to 96, 56, 32 and 28. An invertible
coefficient transformation identifies the final space with the complete
biform normal family. Combined with the sharp balanced gap and prior
projective classification, this gives the necessary conic classification
for non-plane balanced boundary normals under the credited third-gap
conditions. Four focused tests pass. Later compatibility, an all-order
10-by-10 conclusion, the separate 12-by-8 case and a matrix target remain
open. These proofs are written and unreviewed; the exponent remains 9/4.

## A gap for balanced two-dimensional boundary quotients

The [gap proof](research/ai/2026-10-21-balanced-puncture-gap/proof.md)
shows that a complex rank-one-free matrix space of dimension at least
two, amplified by Mat2 and quotiented by kernels of size at most two
on each leg, leaves first dimension zero or at least three. The bound
is sharp. Its constant-rank-two reduction imports the classical complex
Kronecker form, with the rank cases and quotient arguments supplied.
Within the actual 28-dimensional boundary normal family, low first rank
at most two therefore forces complete cancellation, whose projective
survivors were already classified. The coupled cubic proof now supplies
entry into that family from the two rank bounds. Six focused tests and
the registered 423801-pair finite pilot retain separate scopes. The proofs
are written and unreviewed; no matrix target or smaller exponent.

## Blockwise modular bounds for S5 central sources

The [central-block proof](research/ai/2026-10-21-s5-block-filtration/proof.md)
splits F2[S5] into exact 88- and 32-dimensional blocks and counts their
radical flags separately. It gives an all-power, joint-rectangular bound
for coordinate/potential constructions in S5 x C2^r. In particular the
source with two central factors has asymptotic slice rank below 389.
This excludes M(20,20,20) and M(19,20,21), two formats which pass the
existing complex rank-locus and every full Koszul test. The M19 and
one-factor M(13,14,14) targets remain unconstructed and unexcluded by this
bound. Claim `AI-S5-BLOCK-FILTRATION-001` is written and unreviewed;
arbitrary complex maps remain open and no smaller exponent is established.

## Balanced punctures of the third biform core

The [balanced-puncture proof](research/ai/2026-10-21-biform-balanced-puncture/proof.md)
classifies complete cancellation at the 10-by-10 boundary threshold. The
full auxiliary matrix action forces product quotient kernels; the biform
syzygy space has dimension at most three. The actual core is now
classified on every projective chart: non-plane cancellations occur
exactly for `g=(r*x0+s*x1)*(r*y0-s*y1)`, with arbitrary residual linear
forms and a two-dimensional normal fiber. Sixteen disjoint cases with
constant unit minors and exact residual identities cover every complex
parameter value. Nine focused tests pass. These are written, unreviewed
structural results. Projected first ranks one/two and later coefficients
remain open. No matrix target or exponent improvement is established.

## Uniform Hankel caps and dimension refinements

The [Wronskian proof](research/ai/2026-10-21-hankel-wronskian-cap/proof.md)
gives dim L<=r for every characteristic-zero linear space of a-by-b Hankel
matrices of rank at most r<min(a,b), with an exact rational witness generator.
The package also proves [scalar-Hankel saturation at its dimension equality](research/ai/2026-10-21-hankel-wronskian-cap/boundary_saturation.md)
and [a dimension loss for proper crossed-rank parameter images](research/ai/2026-10-21-hankel-wronskian-cap/proper_sections.md).
The [exact application](research/ai/2026-10-21-hankel-wronskian-cap/application.md)
adopts the concurrent rectangular worker's higher-input-rank and bundle
bounds with source credit. It closes every improving ordinary A9 square
sum, and a proper-section equality case at A12. Its240 balanced rectangular
survivors are a pinned comparison, not the full concurrent all-source frontier.
All proofs remain written and unreviewed. No target maps or exponent gain.

## S5 split-source continuation

The [S5 x C2 package](research/ai/2026-10-21-s5-split/README.md) derives
an exact conditional2.247 comparison for M(13,14,14), with margin verified
using integer root intervals. Its actual weighted3-by3 control passes.
Two SAT runs reached their600-second limits without a projected model;
the local runs exported32 exact parity contradictions and no lift, all
replayed. A finite F2 ideal certificate checks the radical
powers and leaves the target unexcluded by that filtration. Claims
`AI-S5-SPLIT-028` and `EXP-S5-RADICAL-029` are conditional/finite. The target
and any smaller exponent remain unconstructed.

The same source investigation now checks S5 x C2 squared and its
conditional M19 gate at2.247. A600-second native run found no pair model.
A [central four-point matching lemma](research/ai/2026-10-21-s5-split/central_slice_proof.md)
adds a written unreviewed necessary cut beyond pair injectivity and the
existing commuting trades. Its finite control has an exact five-row
Farkas circuit. The smaller M(18,18,20) projected run exported one such
cut and no lift; direct colored search reached two collisions. The
alternative S5 x C4 basis has the same conditional degree cost, with its
four-matching obstruction following from pair injectivity alone.
The warm colored continuations reached1,218 and1,427 pair-injective
models respectively; all have exactly replayed Farkas contradictions.
The sampler now incorporates the existing commuting-trade condition.
Claims031/032/033 supply no improving target or smaller bound.

## Subgroup-ideal cuts on the central-cover targets

The [subgroup-ideal proof](research/ai/2026-10-21-subgroup-ideal/proof.md)
shows that a full subgroup coset in one coordinate vertex set bounds the
other-pair product by dim C[G]e_HC[G]. Exact five-cycle dimensions80,88,160
exclude such cosets in all legs of the two M10 targets and the order240
M(13,13,15) target. Integer annihilator and modular lower-rank certificates
replay, including a real positive equality control. The revised split-cover
search uses these necessary cuts. Claim `AI-SUBGROUP-IDEAL-027` is written
and unreviewed; the targets outside this coset condition remain open and
the exponent remains9/4.

## Joint central-sign search in SL(2,5)

The [joint sign investigation](research/ai/2026-10-20-sl2-five-native-parity/README.md)
adds a native encoding and conditional parity learning for the open
M(10,10,10) target. Two 600-second searches found no pair-injective lift.
All 506 exported parity contradictions replay exactly, with positive and
negative encoding controls. This is a finite discovery result
(`EXP-SL2-NATIVE-024`), not a source exclusion. The source and its conditional
2.247 comparison retain their existing attribution; no bound was improved.

The same package now derives an exact source certificate for the split
cover PSL(2,5) x C2, with degrees two copies of1,3,3,4,5. Its M10 target
passes the conditional2.247 gate and the rank-locus screen, and a genuine
weighted3-by3 control passes. This is the new conditional lead
`AI-SPLIT-COVER-SOURCE-026`; the improving target remains unconstructed.
Complete projected triple-translation classes encode the necessary pair
capacity without relying on an SL(2,5) cocycle.

## Modular obstruction for small Heisenberg sources

The [modular application](research/ai/2026-10-20-heisenberg-seven/modular_proof.md)
of Petrov's external filtration excludes coordinate/potential constructions
passing the ordinary degree gate for every tensor power of H_p, for each
odd prime p<=47. It covers finite rectangular direct sums through cyclic
symmetrization and the credited tight-support entropy theorem. Exact rational
certificates and 1,485 finite group-algebra generator controls accompany
written, unreviewed claim `AI-HEIS-MODULAR-025`. Arbitrary complex maps remain
open; no smaller exponent was established. This retires the earlier bounded
H_7 coordinate searches for this gate.

## Hankel pencils and the ordinary frontier

The [linear-annihilator proof](research/ai/2026-10-21-hankel-pencil-degree/proof.md)
bounds Hankel Segre images when1<=r<min(a,b) and5r<2(a+b), using the classical
index sum theorem and a kernel-bundle calculation. It extends the earlier
fixed-scheme and first-boundary ranges; all claims remain written and
unreviewed. The [exact application](research/ai/2026-10-21-hankel-pencil-degree/application.md)
adds453 exclusions to the5139-format balanced rectangular scan through a12.
Every improving ordinary single rectangular target through a9 is excluded;
494 necessary-test survivors remain, first at a10. All improving ordinary
A8 square direct sums are also excluded. A9's square candidate(32,6,3)
remains unconstructed. Singular degenerations remain open; omega is9/4.

## Uniform mixed-axis closure

The [auxiliary-projection proof](research/ai/2026-10-21-mixed-axis-incidence/proof.md)
closes the ten-dimensional family left by claim091, for every complex a
and nonzero t at b=1. A polynomial rank13 minor remains nonzero over
C(ell) at every parameter pair. Its two-dimensional relation space has
only one rank-one direction; applying this to two identical blocks and
then two cubic minors leaves only the four common-plane normals.
Claim `AI-MIXED-AXIS-CLOSURE-092` is written and unreviewed. It excludes
this axis under the prior shifted induction; general mixed-row graphs
remain open. The exponent remains9/4.

## Every graph outside finitely many partner values

The [generic-partner proof](research/ai/2026-10-21-generic-partner-all-graphs/proof.md)
excludes every mixed graph and boundary four-space at each a in a nonempty
open subset U of the partner line b=1, containing2. Uniform54/48 enclosures,
exact source/cubic identities over Q(a), and79 rank guards leave only the
four common planes. The adopted induction excludes M(10,10,11) there for
arbitrary later maps; the torus extends to b nonzero with a/b in U.
Claim `AI-GENERIC-PARTNER-ALL-GRAPHS-098` is written and unreviewed. The
remaining partner values form a finite set which is not yet classified.
This excludes every graph at a good partner, rather than only generic
graphs. Other flags and sources remain open; the exponent remains9/4.

## Every mixed graph at the equal nonzero partner

The [all-graph proof](research/ai/2026-10-21-all-mixed-graphs-a1/proof.md)
closes the canonical full-B seven-frame against every mixed C five-space
at a=b=1, including all six graph coefficients and arbitrary boundary
four-spaces. Uniform source equations, exact cubic identities and an
exhaustive four-branch split leave only the four common planes. The
adopted shifted induction excludes M(10,10,11) for arbitrary later maps;
the source torus extends this to a=b nonzero. Claim
`AI-ALL-MIXED-GRAPHS-A1-097` is written and unreviewed. Claim098 now covers all but finitely many partner values on b=1;
exceptional ratios and other flags remain open. The exponent remains9/4.

## A uniform mixed-normal dichotomy

The [all-graph reduction](research/ai/2026-10-21-global-mixed-normal-dichotomy/proof.md)
at a=b=1 encloses every necessary normal, modulo the four common planes,
in two fixed linear families of dimensions54 and36. Eight rational square
identities and four polynomial mixed-row identities force the rank-one
projection alternative to projection zero for all six graph coefficients,
including exceptional fibers. Claim `AI-GLOBAL-MIXED-NORMAL-DICHOTOMY-096`
is written and unreviewed. Claim097 subsequently eliminates both families
at this partner. The dichotomy itself does not assert an exponent gain.

## An affine family of larger mixed normal spaces

The [exceptional affine-family proof](research/ai/2026-10-21-mixed-exceptional-affine/proof.md)
gives h=(x-y,1-x-z,1-x,x,y,z), at a=b=1, with necessary normal dimension
at least38 everywhere and exactly38 generically. Two degree-two polynomial
left-relation certificates prove the all-parameter rank upper bound.
At h=(0,1,1,0,0,0), a complete38-dimensional kernel, square minors and
additional source equations eliminate all34 non-plane directions; the
adopted induction excludes M(10,10,11) there for arbitrary later maps.
Claim `AI-MIXED-EXCEPTIONAL-AFFINE-095` is written and unreviewed. Its entire
affine family is now included in claim097 at the same partner.

## An open set of arbitrary mixed graphs

The [generic graph proof](research/ai/2026-10-21-generic-mixed-graphs/proof.md)
excludes the canonical seven-by-five target case on an explicitly defined
nonempty Zariski-open set of all six graph coefficients and a at b=1.
A rational point certificate uses two fourteen-variable normal blocks:
559 cubic minors in each generate all2380 quartic forms. Exact rank
modulo32003 proves the relevant rational minors are nonzero. Symbolic
source blocks and a fixed normal chart make this an open-set theorem,
not an extrapolation to all parameters from a finite test. The checked
torus extends it to an open set for b nonzero. Claim
`AI-GENERIC-MIXED-GRAPHS-094` is written and unreviewed. A remaining target
would require its entire affine four-plane of graph representatives to
lie in the exceptional fiber. Claim097 closes all graphs at a=b nonzero;
claim098 reduces the remaining partner chart to finitely many values.
The exponent remains9/4.

## Two-coordinate rank strata and exceptional graph closure

The [two-coordinate chart proof](research/ai/2026-10-21-mixed-two-coordinate-chart/proof.md)
classifies every complex parameter pair in m+t*d0+h*d1 at a=b=1:
normal dimensions32 off two points,36 at the origin and34 at (1,1).
A polynomial frame is complete away from those points, certified by
matched minors and all complex exceptional-root controls. The full
exceptional normal system at (1,1) reduces to the four plane directions
and excludes that graph under the prior shifted induction. Claim
`AI-MIXED-TWO-COORDINATE-STRATA-093` is written and unreviewed. The subsequent
claim097 excludes this whole target chart; the exponent remains9/4.

## Uniform mixed-axis reduction

The [axis reduction](research/ai/2026-10-21-mixed-axis-family/proof.md) covers every complex a
and nonzero t for the mixed row m+t*d0 at b=1. A rank minor t^18 and
Laurent-unit certificates reduce the initial32 normals to four plane
directions plus a necessary10-dimensional quotient family. Projection
minors work uniformly through all exceptional a values. Claim
`AI-MIXED-AXIS-REDUCTION-091` is written and unreviewed; its reduction
alone is not an axis exclusion. The subsequent claim092 above closes
its remaining family. The exponent remains9/4.

## Four mixed five-space graph families

The [graph-family proof](research/ai/2026-10-21-mixed-five-space-graphs/proof.md) excludes four specified
nontrivial mixed rows at partner a=b=1, with arbitrary four-dimensional
boundary parts. Exact quadratic-minor spans over Q force a stable-row
kernel, and target-slice equations reduce its dimensions10->2->0. The
modular calculation certifies rational rank and applies over C. Claim
`AI-MIXED-FIVE-GRAPH-CONTROLS-090` is written and unreviewed. Fifteen
parameterized graph charts still need analysis; the exponent remains9/4.

## Pure mixed five-spaces on the nonzero partner chart

The [pure-row five-space proof](research/ai/2026-10-21-pure-mixed-five-spaces/proof.md)
forces only plane normals when the B first space is the full seven-frame
and the C five-space contains its pure mixed partner, for every chart
parameter with b nonzero. A stable row subspace and a minimum-rank-two
projection split32 quotient parameters into families of dimensions6 and14;
both vanish under the remaining target conditions. All complex a are
covered polynomially after b=1 normalization, including coalescing modes.
Claim `AI-PURE-MIXED-FIVE-SPACES-089` is written and unreviewed. General
mixed-row graphs remain open, and the exponent remains9/4.


## Uniform adapted mixed source slices

The [adapted-source proof](research/ai/2026-10-21-mixed-five-space-uniform/proof.md)
extends the first sixteen low-rank source slices across the entire
two-parameter rank-one partner chart. Their projected third slices have
only the mixed B row remaining and must vanish in a matrix-target lift.
Claim `AI-MIXED-FIVE-SPACE-LOW-SLICES-088` has exact polynomial certificates
and a written unreviewed proof. The full five-space closure remains open
away from the earlier coordinate partner; the exponent is still9/4.


## Mixed seven-by-five coordinate partner

The [five-space point proof](research/ai/2026-10-21-mixed-five-space-residues/proof.md)
forces the four common-plane normals for every complex mixed five-space
opposite the full seven-frame at u=v=e3. Exact source-slice covers, cubic
minors and mixed-column equations give dimensions88,68,54,30,18,12,4.
The shifted induction excludes the matrix target at this partner and its
reversal. Claim `AI-MIXED-FIVE-SPACE-POINT-087` is written and unreviewed.
Other partner lines remain open; the exponent remains9/4.


## Arbitrary mixed hyperplanes on either leg

The [mixed-hyperplane proof](research/ai/2026-10-21-rankone-mixed-hyperplanes/proof.md)
excludes every rank-one mixed first pair with both effective dimensions
at least six, including arbitrary complex subspaces, graphs and delayed
unequal orders. On all228 normal parameters, each leg's rank-one obstruction
has only its mixed column remaining; a mixed hyperplane kills that column
without assuming opposite-leg equations. Claim
`AI-RANKONE-MIXED-HYPERPLANES-086` is written and unreviewed. The necessary
ordinary both-mixed first-rank sum is at most twelve, with only seven-by-five
rank-one pairs remaining at that threshold. The exponent is still 9/4.


## Uniform maximal rank-one mixed frames

The [seven-frame proof](research/ai/2026-10-21-rankone-seven-frames/proof.md)
excludes every maximal seven-by-seven rank-one mixed first pair at these
flags, with arbitrary graphs and delayed unequal orders. A fixed normal
minor stays nonzero polynomially over the entire parameter chart; only
four plane directions remain. Claim `AI-RANKONE-SEVEN-FRAMES-085` is
written and unreviewed. The necessary ordinary first-rank sum when both
mixed projections are nonzero is now at most thirteen. Smaller mixed
spaces and other flags remain open; the exponent remains 9/4.


## Invertible mixed lines: all-order output-growth obstruction

The new [five-frame proof](research/ai/2026-10-21-invertible-five-frame/proof.md)
excludes every compatible invertible mixed-line first pair at the canonical
flags, including arbitrary boundary graphs and delayed unequal orders.
A rank-ten cross and exact five-dimensional annihilators force both output
maps to have generic rank at most five. Claim
`AI-INVERTIBLE-FIVE-FRAME-084` is written and unreviewed. Its separate cubic
control passes complete source replay through degree three; it supplies
no matrix target. The exponent remains 9/4. Rank-one mixed partners and
other first spaces remain construction questions.


Date: October 21, 2026.

**No improvement below $\omega\le9/4$ is established here.** The external baseline belongs to OpenAI. The initial local work analyzes a scalar relaxation and records finite searches.

## Nonlocal maps, exact projection cost, and source capacity

Three completed [nonlocal operator pilots](research/ai/2026-10-20-paired-direct-sums/q_metaplectic_history.md)
retain all saved maps, all 123 sampled records, and their actual
1,000-update stops. The Fourier/chirp/reflection basis depends on the
source size. Complete replays check 40,736 output positions; none gives
an exact matrix target. The first two error plateaus agree with a
separate rational projection construction. That literal projected
tensor has an error whose A-flattening contains
`(3/4) I_((n-5)^2)`, so its repair needs quadratic auxiliary border rank.
The floating-point maps are not exactified by this comparison, and
other joint maps remain open.

The [source-capacity proof](research/ai/2026-10-21-correction-budget/source_capacity.md)
gives a necessary condition even when auxiliary summands have singular
local maps. For fixed-width Q(n,b), a subquadratic border-rank correction
and positive limiting outer ratios imply
`rho*sigma<=1`, `rho*h<=b`, and `sigma*h<=b`. The target volume therefore
obeys `rho*sigma*h<=b`; changing the target shape cannot improve the
critical coefficient allowance beyond its equal-width, near-full value.
This is not a construction or a general exponent barrier.

A [source update](research/ai/2026-10-21-pass-packing/README.md)
records Rafael Pass's arXiv:2610.28627v1 constructive proof of the same
9/4 bound. Its generalized packing count suggests a scalar rule that
already follows exactly from the existing concavity and shifted-tripling
assumptions. This equivalence concerns that scalar rule, not the full
tensor maps or every possible use of the external construction.

Checkpoint `27d7a75`, integrating main `8a07bed`, completed 578 local
tests: 577 passed and one optional NumPy discovery control was skipped.
All five archive replays passed. The complete 638-line transcript and
machine-readable result are in its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint12-validation.json).
Five hosted static checks passed; no hosted test or archive job was
observed for that commit. This continuation incorporates main `b113866`,
including its sixteen-parameter mixed two-jet family and the fixed-space
third-coefficient obstruction. That obstruction retains its stated seed
scope and written, externally unreviewed status. The earlier test count
does not describe the enlarged tree.

## Critical correction allowance and new construction tests

The [critical-coefficient criterion](research/ai/2026-10-21-correction-budget/critical_coefficient.md)
allows a nonzero auxiliary border-rank coefficient at growth rate
`n^(3/2)`. For one unbounded, character-independent family
`Q(n,b) + R_n -> M(l_n,h,r_n)`, with limiting outer ratios rho and sigma,
the sufficient condition is
`limsup border-rank(R_n)/n^(3/2) < (rho*sigma*h)^(3/4) - (4/3)*sqrt(b)`.
At near-full width four, the coefficient `4/25` is admissible by an exact
rational comparison. This would imply a qualitative strict improvement
below 9/4. **The family is unconstructed, and no numerical exponent gap
is supplied by this conditional argument.**

For the fixed endpoint corner R, the [one-scalar proof](research/ai/2026-10-20-paired-construction/m1_corner_one_scalar.md)
excludes `R + D1 -> M4` even by degeneration, using a closed Grassmannian
incidence condition. The [two-scalar proof](research/ai/2026-10-20-paired-construction/m1_corner_two_scalar_ordinary.md)
excludes ordinary restrictions from `R + D2`; its projection argument
does not extend to arbitrary degenerations. A separate
[enriched leading-point gate](research/ai/2026-10-20-paired-direct-sums/r_enriched_lead_obstruction.md)
excludes every two-scalar placement in one specified Laurent chart.
The general border-D2 question remains open.

Two [completed additional pilots](research/ai/2026-10-20-paired-direct-sums/q64_m1_free_kernel_and_reduced_corner.md)
preserve the exact M1 lead while freeing its corner kernel, or seek the
diagonal-deleted M4 target from R. Both fail their full coefficient
conditions. Their saved maps, all 62 sampled history records, actual
1,500-update stops, and complete coefficient replays are retained.
Numerical small singular values are not exact rank certificates.

The [centered aggregation calculation](research/ai/2026-10-21-centered-orientations/README.md)
constructs four shared-input partial transposes with twelve corrections
of size `n^(4/3)`. Its leading source costs `n^2`; a separate six-factor
source has endpoint coefficient 64. Neither meets the paired-source
budget. A full-format closed-orbit argument prevents this fixed tensor
from degenerating to the same-orientation matrix target, and its literal
orientation repair has quadratic flattening rank. No map from Q is given.

Checkpoint `25600a7`, integrating main `e00622f`, completed 565 local tests:
564 passed and one optional NumPy discovery control was skipped. All five
archive replays passed. Its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint11-validation.json)
retains the complete transcript and final result. Five hosted static
checks passed; no hosted test or archive job was observed for that commit.
This continuation incorporates main `8a07bed` and the packages above.
The prior count does not describe the enlarged tree.

## Smaller leading maps and partial targets

The [endpoint corner calculation](research/ai/2026-10-20-paired-construction/m1_endpoint_corner.md)
constructs an exact `16 x 18 x 18` tensor R from Q(6,4). It then excludes
every degeneration of this R to M4: every restriction to the required
long-leg dimensions retains a nonzero slice of rank at most three,
whereas M4 has minimum nonzero slice rank four. The projective incidence
argument makes this obstruction closed under limits. The result concerns
the stated inherited corner kernel, not arbitrary Q(6,4) maps.

The [M1 leading-point package](research/ai/2026-10-20-paired-direct-sums/q64_m1_leading_history.md)
excludes one fixed sparse leading seed by a first-edge support deficit,
for all source outer sizes at least four. A different endpoint seed passes
that support test. Its three inherited outer rows leave exactly the
corner kernel used above. Two completed searches that let the leading
maps move retain all saved coefficients and sampled histories; neither
satisfies the Laurent equations or the necessary leading-rank condition.

The [partial-target proof](research/ai/2026-10-21-bulk-partial/README.md)
excludes another specified first-cross chart without assuming tight
saturation. A polynomial pencil over `C[u]/(u^4)` forces a required
rank-four edge to have rank at most two. Twelve bounded partial-target
probes also retain their maps and actual stops. No all-size bulk
construction has been found. Restoring the stated omitted diagonals
would have linear auxiliary rank if such a construction existed.

The [graded correction calculation](research/ai/2026-10-21-quantum-correction/README.md)
excludes up to four homogeneous scalar corrections for one fixed
root-of-unity quantum tensor and three specified assignments of six
corrections. Slice ranks and a nonzero normalized-slice commutator give
the exact obstructions. Ungraded maps and general Laurent families are
outside these results.

The [leading-M4 search archive](research/ai/2026-10-21-leading-m4-search/README.md)
preserves 39 terminal points from seven finite search families, their
available histories and discovery source snapshots. A standard-library
replay checks all 576 source terms and 4,096 output positions at every
point. No exact lead with the needed kernel dimension was found. The
archive documents a corrected norm-penalty derivative and preserves
the earlier runs as historical evidence. These points are not 39
independent restarts, and full intermediate maps were not retained.

A separate [history correction](research/ai/2026-10-20-paired-direct-sums/q64_ridge_metadata_correction.md)
restores 90 sampled ridge-parameter snapshots in three previously
published full-flag artifacts from their original emitted records.
The recorder now copies the mutable parameter list. Saved maps,
coefficient errors, actual stops, and mathematical statuses are unchanged.

Checkpoint `9d8b240`, integrating main `11aca0f`, completed all 485 local
tests successfully; all five archive replays and nine hosted checks also
passed. Its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint10-validation.json)
preserves the full machine-readable completion result. The separately
retained live text stream is incomplete and is identified as such.
This continuation incorporates main `e00622f` and the packages above;
the earlier test count does not describe that enlarged tree.

## Paired constructions with boundary and correction budgets

An [exact integer construction](research/ai/2026-10-20-paired-construction/outer_product_injection.md)
now gives `Q(5,4) -> M(4,4,4)`, and more generally
`Q(k+1,k) -> M(k,4,k)` for every k at least two. Two unimodular
polynomial-multiplication maps supply the local tensor maps. The small
witness has 25, 20, and 20 nonzero entries, all in `0,+1,-1`; all 400
source terms and 4,096 output coefficients are checked exactly. This
construction works over every field. It does not improve the exponent.
The same product-subspace method at fixed source width four requires
`2k<=n+3`, so it does not supply the needed near-full family at large n.

The [linear-correction criterion](research/ai/2026-10-21-correction-budget/README.md)
shows that an unbounded family `Q(n,4) + R_n -> M(n,4,n)`, with auxiliary
border rank at most `Cn` for a fixed C, would imply
`omega < 30000/13433 < 2.2334`. The same conclusion allows outer dimensions
`n-c` for any fixed c. The cyclic error terms vanish asymptotically, and
the strict rational comparison has an integer certificate. **These
construction premises remain unproved; this is not an achieved exponent.**

The [larger correction budget](research/ai/2026-10-21-correction-budget/superlinear_budget.md)
allows auxiliary border rank `O(n^alpha)` for any fixed `1<=alpha<3/2`.
Its conditional bound is `max(B_b,9/4-(3/2-alpha)^2)`, with B_b defined
by the existing source-profile equation. At width four, `alpha=4/3` or
`137/100` still gives `omega<30000/13433<2.2334`, if the unbounded
near-full construction exists. Even `o(n^(3/2))` would give a qualitative
strict improvement. This relaxes the missing construction premise; it
does not supply the required tensor maps.

The [ordinary narrow-source proof](research/ai/2026-10-20-paired-construction/narrow_ordinary_all_n.md)
excludes `Q(n,2) -> M(n,2,n)` for every n at least three. It uses a
classified two-dimensional kernel and the cited constant-rank matrix-space
bound. A [minimum-slice theorem](research/ai/2026-10-20-paired-construction/narrow_rank_locus.md)
gives `rank Q(n,m)(X) >= rank(X)+m^2-1`; the minimum locus consists exactly
of rank-one X. Full narrow long-leg quotients lose at most one first-leg
direction. The [regular-long-leg extension](research/ai/2026-10-20-paired-construction/narrow_regular_long_legs_obstruction.md)
excludes Laurent families of every first-leg pole order when both long
maps remain regular and surjective at zero. Singular leading long maps
remain outside that result. A [wider jet obstruction](research/ai/2026-10-20-paired-construction/wider_jet_obstruction.md)
excludes the specified regular-nilpotent quotient for every `m>=2` and
`n>=m+1`, while other wider kernels remain open.

The [finite-symmetry package](research/ai/2026-10-20-paired-direct-sums/scalar_and_symmetry.md)
excludes ordinary tetrahedral-equivariant `P3 + trivial scalars -> M3`
with the stated physical representations, for any number of scalars.
All three exact correction phases have nonsingular twelve-by-twelve
equation matrices. Sixteen complete numerical checkpoints replay to their
reported failed-search metrics; these failures alone are not exclusions.

These are written, externally unreviewed deductions and finite controls.
Current constructive work seeks `Q(6,4) -> M(5,4,5)` and scalable formulas
beyond the injection template's dimension limit. The exact small witness
does not meet the unbounded fixed-width family premise.

The [sixteen completed extension searches](research/ai/2026-10-20-paired-direct-sums/q64_search_history.md)
retain all map coefficients and iteration histories. Twelve ordinary fits
and four prescribed Laurent fits give no exact witness. A separate native
coefficient replay checks their reported objectives, including every pole
and every explicit scalar cost. The ordinary product component and the
Laurent runs' non-nilpotent operator errors explain particular failed
searches; they are not general obstructions.

The [boundary-column calculation](research/ai/2026-10-20-paired-construction/outer_product_boundary.md)
excludes an all-order extension that keeps the integer seed's old long-map
columns fixed. Arbitrary new boundary columns lose at most one first-leg
direction; a full next-size matrix extension needs at least `2k+1`.
For Q(6,4), these numbers are one and nine. Changes to the old columns
remain open and are being searched separately.

The [mixed-middle extension](research/ai/2026-10-20-paired-construction/mixed_middle_boundary.md)
proves the same leading rank lower bound of 35 when the seed's four middle
polynomials can mix across the two-dimensional factor. A polynomial syzygy
argument forces an injective projection, so changing only the new boundary
columns still cannot supply the required nine-dimensional kernel. Outer
polynomial spaces in P5 remain outside this argument.

The [balanced-support lemma](research/ai/2026-10-21-nearfull-quantum/README.md)
closes all diagonal Laurent weights for two specified regular quantum
families, even followed by arbitrary further degenerations to their full
matrix targets. Exact rational marginal certificates and Koszul deficits
supply its hypotheses. It does not exclude different leading families,
auxiliary corrections, or the separate recovered integer construction.

Checkpoint `cfa12ba`, integrating main `63eecee`, passes all 467 local
regression tests and all five archive replays on an isolated checkout.
Site packages are disabled for these runs; maintained verification uses
the declared dependencies. Its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint8-validation.json)
records the exact tree and log hashes. All nine observed hosted checks,
including CI, also pass. The next integration includes main `fc8207e`;
this historical test count applies only to `cfa12ba`.

The [external rank-76 seed screen](research/ai/2026-10-21-external-grid-seed/README.md)
replays all 10,000 coefficients of a known AlphaTensor M(4,5,5) algorithm.
An exhaustive finite-field calculation excludes a termwise assignment of
that fixed decomposition to the Q(6,4) evaluation grid in one specified
leg alignment: nine rank-four groups can hold at most 72 of its 76 vectors.
Different decompositions and general maps remain open. This is a failed
reuse attempt, not a new multiplication algorithm or exponent.

The [complete-flag experiments](research/ai/2026-10-20-paired-direct-sums/q64_full_flag_history.md)
retain six further searches and every coefficient of their best maps.
None satisfies the exact Laurent equations. The complete grading has
5,050 required positions; exact shear controls and numerical derivative
checks verify the implemented gauge conventions. Small residuals and
three small trace moments still do not establish nilpotent error.

A [smaller leading-seed calculation](research/ai/2026-10-20-paired-construction/small_leading_jet.md)
excludes the stated first-jet extension of one fixed M(2,4,2) seed inside
Q(6,4) plus one scalar. Both complete rational first-edge systems have
rank 52 and zero aligned image. Other leading maps and higher valuation
patterns remain open.

Checkpoint `1e0e468`, integrating main `fc8207e`, completed 476 tests with
475 passing and one claim-ledger failure: the external-grid experiment
used an unsupported status label. The label is corrected to the existing
`finite-experiment` category in this continuation. Its five archive
replays passed. The [failed-checkpoint receipt](results/paired-checkpoints-2026-10-21/checkpoint9-validation.json)
retains the completion record and hosted failures; it does not describe
the corrected tree as fully verified.

## Audit of a separately claimed exponent improvement

The [bounded Sun audit](research/ai/2026-10-21-sun-audit/README.md) checks
parts of the external preprint arXiv:2610.13971v1. Its proposed
`D16 tensor (14 CW3 + 6 CW2 + 7 W + 5 D4) -> M32` degeneration would imply
`omega<=2.2`. The proposed complete
three-factor Laurent map has not been reconstructed or verified here.

Exact calculations find 50 normalization discrepancies among 354 literal
support occurrences; a stated local scaling repairs all of them. All 256
normalized Walsh equations and the checked five-empty-module identities
hold. A particular packetwise reading of the chart pullback would require
a border-rank-five source to contain `M2`; an explicit determinant-one
Koszul minor gives border rank at least six and excludes that reading.
The preprint's later assembly retains outer rows and additional records,
so this packetwise obstruction is not presented as a refutation of its
global claim. Standard full-space Koszul tests necessarily pass for the
proposed global source and cannot resolve this gap. No external smaller
exponent is adopted on the basis of this audit.

Checkpoint `89c0287`, integrating main `8722b36`, passes all 385 local
regression tests and all five archive replays. Every hosted check also
passes at that commit. The [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint4-validation.json)
records the exact tree, commands, environment, and log hashes. These checks
do not change the mathematical review status of the research.

## Constructive continuation and source obstructions

The constructive continuation records fifty-six local claims,
AI-ORIENTED-ENDPOINT-052 through AI-CHANGED-CORNER-MODULE-107,
in [the claim ledger](research/claims.json). All general arguments are
written and unreviewed. Same-session agent checks and exact finite replays
do not constitute independent mathematical review.

The [spin-one module construction](research/ai/2026-10-20-anisotropic-constructions/spin_module14.md)
now gives exact rational maps from A(4,8) to M(3,3,14) and from A(8,8)
to M(3,3,28). Its nonproduct first map absorbs the earlier scalar
correction into the larger source, with no extra scalar summand. All
source and target coefficients are checked exactly. The first response
is confined to 192 coordinates, leaving enough linear room for the
unconstructed target M27 plus M6 plus M3. That target would imply
omega below 2.24975; this is a conditional comparison, not a new bound.

A separate [changed corner construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner_shifted.md)
gives M(4,4,12) with exact response rank 164 and fixed-first-map
flattening rank 481. It passes two necessary tests for extending toward
M27 plus M7. Its other square-matrix entries remain unconstructed.
The original corner variant, with response rank 186, is also preserved.

The [exact crossed-module construction](research/ai/2026-10-20-anisotropic-constructions/crossed_module11.md)
gives a rational restriction from C(2,4) tensor C(2,8) to M(2,2,11).
Its [full-source lifts](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_cross_module_lifts.md)
give A(4,8) to M(4,4,11) and A(8,8) to M(4,4,22), with every desired
and unwanted coefficient checked from the original source tensors.
These improve the corresponding coordinate-module controls from eight
and sixteen channels to eleven and twenty-two. The first target leg
still has only sixteen directions; compatible square extensions are
missing. Neither rectangular restriction establishes a smaller exponent.

The [four-factor flattening proof](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_crossed_flattening.md)
proves that eleven and twenty-two are optimal within the corresponding
product first-map branch. It also excludes extending the old sixteen
first images to M27, even with arbitrary other-leg maps. The
[saved-seed response certificate](research/ai/2026-10-20-anisotropic-constructions/crossed_module_response.md)
separately excludes retaining the old other-leg maps. The newer spin
and corner constructions change the first core; these scoped
obstructions do not rule them out.

The [two-source capacity inequality](research/ai/2026-10-20-anisotropic-constructions/two_source_budget.md)
requires equal source leg dimensions N at least ceil(3 n^2 / 4) for a
direct sum of two sources to degenerate to M_n. Explicit complementary
block-zero trace tensors attain this dimension threshold. Combining this
necessary condition with the finite convolution budget first leaves
2 A(11,12) to M62, which is unconstructed. The recorded ordinary
majority-block factorization at that size is separately excluded.

An [exact carry contradiction](research/ai/2026-10-20-anisotropic-constructions/bitwise_hankel_projection.md)
closes one specified two-copy spin1 projection family. The completed
[moving physical-compression experiment](research/ai/2026-10-20-anisotropic-constructions/parity_structure_rectangular_compression.md)
retains all 1,210,000 target coefficients and explicit scale normalization.
Its final normalized residual is about 5.4627, so it supplies no target
identity or singular family. These records preserve exact controls and
the actual limitations of the searches.

The [new focused receipt](results/anisotropic-constructions-2026-10-20/crossed-module-focused-validation.json)
pins the artifact hashes and includes concurrent main through `8a07bed`.
It records 38 completed tests: 36 passed and two optional numerical
controls skipped in the maintained environment. All four compression
control tests pass separately with NumPy and SciPy available.
The [complete regression receipt](results/anisotropic-constructions-2026-10-20/crossed-module-full-validation.json)
pins checkpoint `1f813bb`: 496 tests completed, with 493 passed and
three optional skips. All five [original archive replays](results/anisotropic-constructions-2026-10-20/crossed-module-archive-validation.json)
passed unchanged. The later spin, corner, response and flattening
packages have separate focused validation; they are not included in
that 496-test count.
Their [35-test focused receipt](results/anisotropic-constructions-2026-10-20/changed-core-focused-validation.json)
checks all four new packages, main's mixed second-order family through
`21f54c3`, and the repository ledger, sources, archives and links with no
skips or failures.
The [full spin-and-corner regression receipt](results/anisotropic-constructions-2026-10-20/spin-corner-full-validation.json)
pins checkpoint `4ed2b52`: 513 tests completed, with 510 passed and
three optional skips. The later integration of main's mixed third-order
proof at `b113866` has a separate
[27-test focused receipt](results/anisotropic-constructions-2026-10-20/spin-corner-main-integration-validation.json),
with no skips or failures.

The [support-peeling proof](research/ai/2026-10-20-anisotropic-constructions/torus_support_peeling.md)
now excludes **every ordinary A88 to M27 plus M7 restriction whose matrix-unit
images are homogeneous for the fixed source grading**, including unrelated
vertex charge lists and profiles with holes. Exact rank budgets successively
force all three map images into coordinate spaces of dimensions
960, 922, 834, and finally 468, below the required 778. The primary verifier
checks 492 removals through integer separating lines, independently of the
discovery hull algorithm. A separately written full-source replay agrees
on every retained coordinate set. Ungraded maps and arbitrary singular
degenerations remain open, and the exponent is unchanged.

The [mixed-grading extension](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_mixed_grading.md)
shows that, on at least two legs of any ordinary target restriction,
at least 19 matrix-unit images must each use three or more source weights.
It uses separate coordinate masks and injectivity inherited from the full
maps. An exact M12 plus M3 change of basis provides a positive control
with balanced cross-weight cancellation; it does not enlarge that target.

Two [Laurent collision controls](research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_extension.md)
give explicit singular limits from the existing three matrix cores.
The larger limit retains all 134 intermediate directions per leg, including
24 off-diagonal directions, with complete negative-power cancellation.
The [scalar-power construction](research/ai/2026-10-20-anisotropic-constructions/scalar_power_recycling.md)
reuses corrections to realize A22 squared plus A22 plus M3 to M9 with
165 source coordinates per leg. Its all-power residual has exact flattening
rank 9^k-8^k, and its complete source cost does not cross the finite gate.
These are constructed identities and scoped cost bounds, not smaller
exponent claims.

- The [oriented endpoint analysis](research/ai/2026-10-20-critical-character-extension/README.md)
  gives a common critical amplitude and a quantitative stability bound.
  A certified fifth-difference stencil separates that hypothetical profile
  from quantum characters and the classified edge of the spectrum. The
  corresponding test for interior spectral points remains unproved.
- The [nonmonic target normalization](research/ai/2026-10-20-new-source-constructions/README.md)
  gives an all-size unimodular normalization. At size four, a sampled chamber
  reduces the coefficient system to 95 zero equations and two orbit
  relations. Exact elimination has 65 unit pivots. No exact solution or
  Hensel certificate has been found.
- The [full polynomial rank locus](research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
  classifies cyclic-source slices below twice their minimum rank. It gives
  an ordinary-map obstruction for every nonscalar square target block.
  The [Hankel-symbol dimension theorem](research/ai/2026-10-20-anisotropic-constructions/hankel_symbol_dimension.md)
  extends the obstruction to every rank r with r<min(a,b) and
  3r<=a+b-1. A separate [equality argument](research/ai/2026-10-20-anisotropic-constructions/parity_structure_equality.md)
  and [three-leg factorization](research/ai/2026-10-20-anisotropic-constructions/hankel_rank_two.md)
  close the rank-2ab boundary for square blocks of size at least three.
  The [first-boundary theorem](research/ai/2026-10-20-anisotropic-constructions/hankel_boundary_dimension.md)
  extends the Segre-image bound to a+b-1=3r-1, with dimension cap max(r,4).
  [Exact partition enumeration](research/ai/2026-10-20-anisotropic-constructions/square_sum_frontier.md)
  now excludes every improving ordinary square direct sum from all 60 source
  formats with leg dimension below 960, and from A(5,12) at dimension 960.
  The former A(7,8) target M25 plus M5 is excluded. The first surviving
  format is A(8,8): M27 plus M7 would imply omega<2.2485, but its maps are
  missing. Singular full-source degenerations remain open.
- An [explicit parity degeneration](research/ai/2026-10-20-anisotropic-constructions/parity_balancing.md)
  has positive rational marginal certificates and cyclic asymptotic
  slice-rank capacity about 212.716257. A stronger
  [pairwise-annihilator obstruction](research/ai/2026-10-20-anisotropic-constructions/parity_annihilator.md)
  bounds every square direct-sum target of that one-copy source by leg
  dimension 169, including arbitrary singular degenerations. A single M13
  is also excluded. The proposed M14 plus M4 target is therefore closed.
- The [integral direct-sum construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_direct_sum.md)
  gives actual restrictions A(a,a) to M(2a−2) plus M(a−2), for every a≥3.
  Complete coefficient controls cover a=3 through 6, including M8 plus M3
  from A(5,5). An additional proposed scalar block fails mixed-coefficient
  checks and is explicitly rejected.
- A new [rational matrix identity](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin1.md)
  gives an actual restriction from A(2,2) plus one scalar to M3. All 729
  target coefficients are checked exactly. The additional scalar is part
  of the source, so this does not assert a restriction from A(2,2) alone.
- The [residual construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_residual.md)
  gives A(5,6) to M8 plus the full A(2,3) tensor. Exact maps also give M10
  alone and M8 plus M4. These constructions retain useful smaller sources
  for composition. A [corner split](research/ai/2026-10-20-anisotropic-constructions/parity_structure_corner_extension.md)
  supplies A(2,2) plus one scalar from A(2,3). These maps do not improve
  the exponent.


- The [all-size retained-residual construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_full_residual.md)
  gives A(a,a+1) to M(2a-2) plus A(2,a-2), for every a>=5. The complete
  A(7,8) to M12 plus A(2,5) witness has an integer-only replay. A fixed-core
  extension bound limits that particular core to total leg dimension 256.
- The [triangular lift](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_triangular.md)
  gives A(a,b) plus M((a-1)(b-1)) to M(a+b-1). Its residual is retained.
  [Score limits](research/ai/2026-10-20-anisotropic-constructions/quotient_score_barrier.md)
  close the stated single full-correction comparison and independent corner
  supplier. A [cyclic determinant identity](research/ai/2026-10-20-anisotropic-constructions/parity_structure_three_quotients.md)
  prevents the scalar correction from vanishing in the exact A22 quotient
  family. The [cyclic quotient-volume theorem](research/ai/2026-10-20-anisotropic-constructions/cyclic_quotient_volume.md)
  further proves m0*m1*m2<=(a+b-1)^3 for three unrelated exact physical
  quotients over every field. Even free residual cancellation cannot pass
  the single-target finite comparison in that class. Unrestricted
  off-diagonal compression maps remain open.
- Exact integral controls include A(2,3) to M4 with zero quotient-kernel
  action and [A(8,8) to M15](research/ai/2026-10-20-anisotropic-constructions/parity_structure_a88_seed.md).
  The latter has 462 nonzero entries per map and a complete sparse replay.
  These controls do not construct the larger improving target.

- A new [torus-compatible exact seed](research/ai/2026-10-20-anisotropic-constructions/parity_structure_torus_seed.md)
  gives A(8,8) to M12 plus M3. The [monotone physical-vertex construction](research/ai/2026-10-20-anisotropic-constructions/monotone_endpoint_seeds.md)
  gives exact endpoint M4 and M8 controls. The latter construction's literal
  common coordinate code has a [size limit](research/ai/2026-10-20-anisotropic-constructions/coordinate_compression_limit.md):
  every A88 M27 construction must leave that code on each target leg.
- The [recorded endpoint maps](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_torus_anchors.md)
  have full row rank 778 on all three legs. They satisfy all six extreme
  slices of the M27 plus M7 target and the complete endpoint M4 tensor.
  Each rational map has denominator 64 and 782 nonzero entries. The other
  target coefficients cannot all be satisfied with that boundary fixed:
  a [direct affine-slice contradiction](research/ai/2026-10-20-anisotropic-constructions/torus_affine_slices.md)
  forces a coefficient to equal one where the target requires zero.
  A [four-map relation](research/ai/2026-10-20-anisotropic-constructions/fixed_anchor_obstruction.md)
  excludes completion of the preserved first Hadamard seed with its stated
  maps fixed. Both saved seeds remain valid controls for their partial
  identities, and both fixed boundary families are now nonextendable.
- The [degree-13 pencil proof](research/ai/2026-10-20-anisotropic-constructions/torus_degree13_pencils.md)
  excludes every ordinary grading-preserving restriction with the original
  symmetric 27-plus-7 charge profile, including arbitrary boundary maps.
  It combines the [two-leg rank chain](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_rankone_13_chain.md),
  exact source symmetries, universal product identities and all 256
  singular-projection patterns. This does not exclude the ungraded frontier.
- A [saturated-block rank inequality](research/ai/2026-10-20-anisotropic-constructions/torus_saturated_blocks.md)
  excludes the common width-13 profile: its target block has rank 9,
  while saturation of the two input spaces requires rank at least 12.
  A separate [cube determinant](research/ai/2026-10-20-anisotropic-constructions/torus_saturated_pencil.md)
  excludes specified saturated degree-13 pairs even with unequal vertex
  charge lists. Neither argument addresses arbitrary singular limits.
- The [graded fixed-core bound](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_fixed_core_weights.md)
  excludes keeping two complete copies of the displayed M4, M6 or M8 core
  while extending to the original profile. The [free-interior construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_free_interior.md)
  gives A(a,a) with both physical endpoints deleted to
  M(a-1) plus M(a-1) plus M(a-2), for every a>=3. Its fixed M7 channels
  also fail an exact extension-rank test; movable small-block maps remain open.
- The [complete common-vertex M7 screen](research/ai/2026-10-20-anisotropic-constructions/parity_structure_m7_vertex_screen.md)
  covers 1,290,240 choices. Sixteen pass the necessary weight-zero rank
  gate, but all retain 498 unwanted coefficients. Exact balanced cycles
  obstruct removing those extras by coefficientwise Laurent rescaling.
- The earlier [common-profile classification](research/ai/2026-10-20-anisotropic-constructions/parity_structure_common_profiles.md)
  also closes all common integer charge lists by exact enumeration and
  local proofs. Its [zero-grade lemma](research/ai/2026-10-20-anisotropic-constructions/parity_structure_zero_grade_rank.md)
  gives minimum slice rank a for the zero-grade A(a,a) tensor. The later
  peeling proof removes the need to enumerate profiles for the main exclusion.
  [Unequal-profile partial maps](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_unequal_profiles.md)
  retain exact M12 plus M3 controls; their full targets are explicitly
  excluded. Optional numerical objective code is preserved with separate
  small controls and introduces no maintained dependency.
- The [simple-pole argument](research/ai/2026-10-20-anisotropic-constructions/compression_simple_poles.md)
  excludes a nonzero simple pole in the fixed A22 compression chart when
  the trace tensor must have a finite limit. It does not cover arbitrary
  pole supports or moving physical bases. A separate [stabilizer invariant](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_stabilizer.md)
  excludes the saved dyadic A33 numerical seed from the stated target
  stabilizer orbit, with a complete integer-only modular replay. It does
  not exclude changing that seed or general A33 maps.

The [combined validation receipt](results/anisotropic-constructions-2026-10-20/residual-boundary-validation.json)
records 368 passing tests and five unchanged archive replays at `8b09235`.
This computational coverage does not change the proof-review status.

The [torus-anchor checkpoint receipt](results/anisotropic-constructions-2026-10-20/torus-anchors-validation.json)
records 391 passing tests and five unchanged archive replays for `fa74fee`
combined with main `f67467d`. That receipt predates the new fixed-boundary,
degree-13 and saturated-block packages; it is not their validation receipt.

The [support-peeling checkpoint receipt](results/anisotropic-constructions-2026-10-20/torus-peeling-validation.json)
records the complete 447-test suite at `bb64dae`: 446 passed and the optional
NumPy control skipped. All five original archive replays passed unchanged.
This pin includes main through `b0a54f2` and claims through 093; the newer
mixed-grading, Laurent, scalar-power and concurrent-main additions pass
the [separate 16-test focused suite](results/anisotropic-constructions-2026-10-20/torus-construction-controls-validation.json).
The claim ledger, source registry, archive manifest and relative links also
pass their repository checks. Current hosted validation is required before
merge.

These results identify constructions and obstructions within stated classes.
They establish no smaller matrix multiplication exponent.

The earlier checkpoint `e44aaff`, integrated against main `a44451d`, passed
323 regression tests and all five original archive replays. Its
[validation receipt](results/anisotropic-constructions-2026-10-20/integration-validation.json)
records the commands and log hashes. The historical archives are unchanged.
Checkpoint `eed3cbc` incorporated main `2a7c503` and passed 338 local regression
tests and all five archive replays. Its
[validation receipt](results/anisotropic-constructions-2026-10-20/integration-hankel-validation.json)
records the commands and exact log hashes. Hosted validation then found an
undeclared NumPy import in the rank-two checker. The checker now uses Python
integers only and reproduces the same 1,296,000 coefficient comparisons.
The repaired tree includes main `75bf6a3` and passes 344 tests plus all five
archive replays with site packages disabled and only the declared SymPy and
mpmath dependencies available. The
[repair receipt](results/anisotropic-constructions-2026-10-20/integration-maintained-validation.json)
records this environment and the original hosted failure. CI and finite
replays do not change the proofs' review status.

## Earlier integration checkpoints

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

The [F8 variable-plane continuation](research/ai/2026-10-20-group-potentials/octal_research.md#variable-planes-after-the-first-main-integration)
now searches independently chosen normal-fiber planes. Its encodings pass
a complete known-model audit, and an independent integer checker validates
the affine fibers and pair maps. The first native-parity run checks four
candidates, including a reused control; all fail exact potential constraints.
This extends discovery coverage and supplies no improved exponent.

The current next steps are listed in [research directions](docs/research_directions.md). Repeating a completed finite search with the same parameters is reproduction, not new research progress.

The [fixed cubic F8 parent obstruction](research/ai/2026-10-20-octal-parent-barrier/research_note.md)
excludes every single strict-coordinate-potential target from vertex subsets
of that 56-point parent from passing the usual 9/4 degree-sum gate. An
explicit circuit orbit forces a seven-cycle hole inequality; exact integer
optimization bounds the target volume by 92,928, including rectangular
shapes. The checker verifies 10,752 circuits and independently enumerates
all 4,782,969 hole patterns. This written proof is unreviewed and concerns
only that parent and construction method. It gives no exponent improvement.

A complete local continuation checks all 3,060 single-plane changes in the
F8 base `[1,8,2,16,4,32]`, keeping all short directions fixed. Every change
fails a necessary pair-quotient packing. This finite scope is replayed by
`tests/test_octal_single_plane.py`; it does not exclude simultaneous changes
or other bases. Two native-parity pilots yield only reused controls and
untraced UNSAT answers. Neither gives an exponent improvement.

The [C29 near-capacity classification](research/ai/2026-10-20-c29-near-capacity/research_note.md)
proves that every three-point unique-sum triple in C29 consists of arithmetic
progressions. Two exact enumerations agree on its six ordered normalized
cases. A complete fiber-direction filter for C29:C4 leaves twelve size-ten
configurations, and the identity-quotient offset telescoping condition rejects
them all. Thus the stated injective-pair-map construction with strict vertex
potentials cannot have all three sizes at least ten. This written argument
is unreviewed; general tensor degenerations and smaller unequal targets
remain open. No smaller exponent follows.

The [C29 unequal-target followup](research/ai/2026-10-20-c29-near-capacity/rectangular_note.md)
closes the same coordinate-potential one-source degree-sum route for all
single matrix shapes. The full sorted rank-locus frontier leaves only
(9,9,11), (9,10,10), and (10,10,10). Complete finite filters and identity
gluing now exclude all three in the stated construction class. This is
an unreviewed obstruction, not a general degeneration exclusion or an
improvement of the arithmetic exponent.

## General semisimple Koszul continuation

The [full-space semisimple screen](research/ai/2026-10-21-semisimple-koszul/proof.md)
applies the existing exact matrix Koszul formulas to general complex
degenerations of group algebras. It excludes five of the26 remaining F8
formats, including(16,16,26), while21 still pass, including(19,19,19).
These exclusions have broader scope than the coordinate-construction
barriers below. The written derivation and imported rank proofs are unreviewed.

The same package exactly derives the504-element SL(2,F8) source degrees
1,7,7,7,7,8,9,9,9 by rational central algebra. Its degree/rank-locus/full-Koszul
frontier leaves16 formats. A genuine M(18,18,25) degeneration would imply
exponent at most2.245 by the certified conditional comparison; no such
degeneration is supplied. One fixed-full-D18 subgroup pilot timed out with
zero pair models in180 seconds. Only its small M(18,1,1) control is verified.

The [SL(2,F8) subgroup-ideal followup](research/ai/2026-10-21-sl2-f8-ideals/proof.md)
applies a concurrent worker's averaging lemma with new exact central
projection upper bounds308,440,244 for subgroup orders8,9,18. Complete
unipotent-eight and dihedral-eighteen cosets are forbidden on every leg of
all16 remaining coordinate formats. For M(18,18,25), nine-cycle cosets are
also forbidden in the two size-eighteen families. This now excludes the
first fixed-full-D18 frame by a written unreviewed proof; its historical
timeout is not used as proof. Remaining coordinate sets and general tensor
maps remain open. No exponent improvement follows.

## Abelian-normal coset Koszul obstruction

The [normal-coset proof](research/ai/2026-10-20-normal-coset-koszul/research_note.md)
restricts a coordinate-potential group construction to its abelian normal
subgroup. The classical three-slice commutator bound then requires
`3 sum k_a^2 - number(k_a=1) <= 2|H|` for common-coset vertex minima.
An explicit rank-129 integer matrix versus source upper bound 128 closes
the entire F8 size-nineteen maximum-three-fiber ansatz, including every
variable plane and offset in the prior search. A separate difference-space
argument bounds all size-nineteen F2^6 normal fibers by four.

The same proof excludes the full stated F4^3:C3 size-twelve coordinate
class and every C31:C6 candidate with all normal fibers at least two. It
does not exclude general complex degenerations. The proof is unreviewed.
A complete seven-fiber count screen with sizes in {2,3,4} leaves 1,566
necessary patterns; they have no constructed directions, offsets or
potentials. The exponent remains 9/4.

The [rectangular coset followup](research/ai/2026-10-20-normal-coset-koszul/rectangular_note.md)
now excludes the full size-nineteen F8 construction class, including every
four-point, one-point and empty fiber pattern. A rank formula for rectangular
normal blocks, a pair-averaging argument and 466,859 independently replayed
alignment bytes cover all 505 cyclic count classes. Thus no balanced target
in this stated F8^2:C7 coordinate-potential source-cost route beats 9/4.
General tensor degenerations and unequal targets with a side below nineteen
remain open. This written proof is unreviewed and gives no exponent improvement.

The [higher-slice unequal followup](research/ai/2026-10-20-f8-unequal/research_note.md)
also excludes every target of side sizes at least (16,16,26), in any order,
in this construction frame. All32 small integer pencils and520710 count
pairs are replayed exactly; seven-slice averaging gives8970/7>1280.
The proof is written and unreviewed. A (16,20,21) count pattern survives
the stated three-, five- and seven-slice necessary tests. Two restricted
nonlinear graph searches found no target: one reported untraced UNSAT,
the other timed out. The separately verified (4,4,3) positive control
does not pass the exponent gate. The arithmetic exponent remains9/4.

The [complete F8 coordinate closure](research/ai/2026-10-21-f8-coordinate-closure/proof.md)
now closes every unequal format in this one-source route. New even-slice
rectangular pencils reject the former(16,20,21) count survivor. Exact replay
checks64 pencils,9539875 pair tags and90 residual alignments across all12
minimal formats. Thus no single F8^2:C7 target through injective pair maps
and strict vertex potentials passes its usual source-degree gate at any
positive exponent at most9/4. The written proof is unreviewed. Arbitrary
complex degenerations, joint extraction and tensor powers remain open;
no arithmetic exponent improvement is established.

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

The subsequent exact projection/lift reduction found 1,394 projected
SL(2,7) candidates in its first 600-second run. All fail the lift equations;
all 1,394 saved parity circuits replay using integer group arithmetic.
No candidate has reached a full degeneration witness. Ten focused controls
check the source, subgroup normalization, lift equations against exhaustive
small sign choices, certificate tampering and the cyclic-eight fiber rule.
The fiber-strengthened run separately rejected 149 candidates by replayed
circuits. Verified small parity cores can now be reused across independent
right translations and set permutations, with source hashes and explicit
occurrence clauses. These finite rejections are not a complete exclusion.
The first run with those templates separately rejected 619 candidates by
replayed circuits and supplied no pair-injective lift or tensor witness.

## Heisenberg source and coordinate frontier

The [Heisenberg lane](research/ai/2026-10-20-heisenberg-five/README.md)
derives the order-125 source degrees from explicit shift/phase operators.
Its conditional M10 comparison passes at 2247/1000, but the
[normal-coset incidence proof](research/ai/2026-10-20-heisenberg-five/normal_coset_closure.md)
now excludes every single target passing the source's 9/4 gate in the
injective-pair-map, strict-vertex-potential class. It applies the concurrently
merged rectangular Koszul bound, exhausts 3003 balanced and 410333 unequal
count cases, and uses affine-line pair-count contradictions. It does not
exclude arbitrary complex degenerations or establish a smaller exponent.

Separately, [stabilizer averaging](research/ai/2026-10-20-heisenberg-five/coset_averaging.md)
bounds the volume of the stated full cyclic-coset class by p^4 for every
odd prime p. Exact finite controls cover subgroup triples at p=3,5,7,
all 400 two-coset circuits at p=5 and 38 progression circuits at p=11.
These are written, unreviewed construction obstructions. The original
untraced SAT reports are retained as discovery history and are not proof
premises.

## Selected direct-product group target

The [SL(2,5) x C2 lane](research/ai/2026-10-20-sl2-five-c2/README.md)
selects M(13,13,15). Exact rational central idempotents derive the first
factor's degrees; the standard direct-product theorem repeats them twice.
Integer root intervals give a conditional omega < 2247/1000 comparison, and
the concurrent rank-locus screen requires 217<=240, so it does not exclude
the target. **The target degeneration is unconstructed.**

The adapter checks an order-48 subgroup and 60 center orbits, applies the
central-pair exclusions and reuses the pinned integer acceptance verifier.
Six controls check the source, projection, an embedded positive weighted
control, the unchanged SL(2,7) certificate and exact finite rejection replay.
The two initial 600-second target searches, with and without projected
inverse-class capacities, ended without a pair-injective model. These
timeouts exclude nothing. A separate structured-parent enumeration rejects
all 1,000 explicitly generated ten-point section triples by independently
replayed positive integer Farkas circuits; its finite scope is documented in
the [parent note](research/ai/2026-10-20-sl2-five-c2/structured_note.md).
The larger target remains open.

The [projected continuation](research/ai/2026-10-20-sl2-five-c2/projected_note.md)
adds necessary four-pair fiber capacities and binary equations over the
projected involutions. The first binary-filter run has 2,765 replayed
capacity certificates and 2,474 replayed parity certificates, plus 3,794
untraced solver cores and one budget skip. It produces no lift or witness;
the exact circuits do not upgrade the untraced parts into a complete proof.
All 720 full-space Koszul comparisons pass for this target. A separate
(12,12,17) comparison is also conditional on an unconstructed degeneration.

The [central cocycle extension](research/ai/2026-10-20-sl2-five-c2/pair_saturation.md)
uses the zero sum of all four central colors in a saturated projected pair
fiber. It yields exact equations for both bits, including the twisted
SL(2,5) bit. The first run rejects 169 candidates by replayed circuits.
A separate learning run has 244 replayed circuits, 1,075 learned necessary
rows, and one untraced inner refutation. Neither constructs a lift or
establishes a complete exclusion. All 4,096 normalized small lifts were
checked; the 128 with injective pair maps satisfy the necessary equations.

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

The [intermediate-weight slice covers](research/ai/2026-10-20-koszul/intermediate_weights.md)
(AI-INTERMEDIATE-WEIGHT-COVERS-033) give exact source-cost constraints for
constant matrices followed by the specified shared and monomial weights.
For slopes alpha/beta tending to r in [1,2], the asymptotic source ratio is
at least 2-r/2. At the balanced direction (2,1), the finite bound is
B>=k*(N+floor(m/2))-(m-1). Thus the m=4,B=10k target is excluded for k>=2
within this class, including the previous k>=53 finite-profile target.
Single-copy m=4 and the growing-m balanced route remain open. The proof is
written and unreviewed; exact covers and small independent matching checks
validate finite cases without establishing an exponent improvement.

The [finite amplitude criterion](research/ai/2026-10-20-koszul/finite_amplitude.md)
(AI-FINITE-AMPLITUDE-CRITERION-034) offers a separate target: a universal
13/12 improvement over P_*(4,4) for near-endpoint characters would imply
omega<=2.249. **That finite lower bound is unproved.** An exact integer
certificate checks the conditional implication only. The accompanying
dimension screen (AI-MATRIX-EXTRACTION-DIMENSION-035) closes the analogous
direct-sum matrix-product extraction method for symmetrized C(a,a) at
a=2,3; a=4 survives the screen. Eleven retained floating permutation fits
in a different construction class supplied no exact witness.
The concrete finite alternative is to degenerate the product of all six
leg permutations of C(4,4) to M(106,106,106). That unconstructed target
would also imply omega<=2.249. The source/target leg dimensions pass, but
the group worker's abelian opposite-relation argument excludes coordinate
maps with diagonal weights. A Holder bound also excludes all-power
coordinate extractions into independent matrix products at this diagonal
(AI-COORDINATE-MATRIX-EXTRACTION-037). General linear cancellation remains open.

The [finite-target screens](research/ai/2026-10-20-koszul/finite_target_screens.md)
sharpen that distinction. An explicit binomial scaling gives uniform quantum
marginals for every C(a,b), so all singleton quantum functionals permit H106
(AI-QUANTUM-CONVOLUTION-SCREEN-038). An elementary entropy deficit excludes
all-power coordinate-and-weight independent-matrix extraction also at a=5
(AI-COORDINATE-ENTROPY-LOSS-039). Allowing arbitrary Laurent output maps while
retaining coordinate inputs still bounds square targets from S_4 by n<=93
(AI-LAURENT-OUTPUT-MATRIX-SCREEN-040); thus H106 needs input mixing.
These are written, unreviewed proofs. Exact controls cover 256 marginal
normalizations, 4877 rational convolution pairs and 43681 four-type bipartite
component count pairs. No new degeneration or smaller exponent is established.

The [smaller cyclic target](research/ai/2026-10-20-koszul/cyclic_finite_target.md)
uses three convolution factors and leg dimension 112. Its unconstructed
M(10,10,11) target would imply omega<=2.248 (AI-CYCLIC-FINITE-TARGET-041).
Every nonzero source slice has matrix rank at least 16, which excludes
constant linear maps to this target (AI-CYCLIC-MINIMUM-SLICE-RANK-042).
The all-a minimum-rank locus is also classified; its dimension excludes
constant restriction A_5 to M(13,13,17) (AI-CYCLIC-MINIMUM-RANK-LOCUS-043).
All 4095 nonzero F2 slices at a=2 agree with the minimum-rank formula;
the 27 equality cases agree exactly with the stated factorization.
These written proofs are unreviewed and leave singular degenerations open.

The [cyclic recoupling experiment](research/ai/2026-10-20-cyclic-recoupling/README.md)
(EXP-CYCLIC-RECOUPLING-044) now computes exact coefficients after a basis
change mixing all three factors on each leg. At a=4 its 2539 scalar blocks
factor into 175 representation-degree blocks. Sampled searches using exact
scores find no matching-profile violation. The full a=4 grouped binary
weight run also finishes with no violation across 1797505 distinct supports;
its best score ratio is about 0.258426. A separate exact determinant
certificate excludes interpreting the central 4-by-4-by-4 multiplicity
tensor as M2 under constant maps (AI-CYCLIC-CENTRAL-MULTIPLICITY-045).
This finite experiment supplies reusable coefficient data, not a degeneration
achieving the required gain.

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

The [Laurent-output extension](research/ai/2026-10-20-mixed-restrictions/laurent_capacity.md)
retains the same overhead lower bound when the output matrix is an arbitrary
Laurent family and the two inputs remain coordinate injections with Laurent
scalars. A joint index-and-valuation word supplies one common arithmetic
interval for the rank argument. An exact size-three control verifies the
broader model. This written proof leaves actual input mixing open.

## Paired convolution source ranks

The [paired-source proof](research/ai/2026-10-20-paired-sources/research_note.md)
computes an exact first Koszul kernel of dimension 3a-2 for two oppositely
oriented convolutions. It excludes the full-capacity matrix target for all
sizes under arbitrary complex degeneration, and excludes a promising
size-five direct sum. A complete integer budget certificate also bounds
the one-copy size-four factorwise matrix-block method below the finite
profile-improvement threshold. These written and finite results do not
exclude joint extraction from the full source or its powers.

The [all-power formula](research/ai/2026-10-20-paired-sources/all_koszul.md)
now gives every first-leg source rank. A separately derived matrix formula,
crediting Landsberg--Ottaviani's kernel inclusion, supplies exact comparison
ranks over C, and a second cohomological argument gives the same ranks
over every field. These written, unreviewed arguments exclude the initially
selected P_6 to M(6,10,6) target at power seven. Its former conditional
2.235 implication therefore has an excluded premise. The complete finite
frontier through a=13 contains 239 improving dimension-compatible single
matrix targets, modulo B/C exchange; all are excluded by saved rank
witnesses. The frontier through a=16 has 28 survivors, first at a=14.
No surviving target is constructed; joint extraction remains open.

The [two-block frontier](research/ai/2026-10-20-paired-direct-sums/README.md)
now enumerates every one-block or two-block matrix target through `a=10`.
After exact score comparisons and every first-leg Koszul degree, none
survives through `a=9`; at `a=10`, 19 pairs survive modulo B/C exchange
(EXP-PAIRED-DIRECT-SUM-FRONTIER-001). The selected target is
`P10 -> M(4,11,10) direct_sum M(10,12,6)`, in formats
`(100,190,190) -> (100,164,182)`. Its existence would force
`15840^t+25920^t<=3364`, hence `omega<1121/500=2.242`
(COND-PAIRED-DIRECT-SUM-002). Exact integer powers certify this implication.
**The degeneration is unconstructed.** Ordinary constant restrictions are
excluded; passing 100 first-leg rank comparisons does not supply singular
maps. These results do not constitute an exponent improvement.

The [boundary-chain construction](research/ai/2026-10-20-paired-construction/README.md)
now gives explicit restrictions `P_a -> M(a,2,a)` for every integer `a>=2`,
with coefficients `0,1,-1` (AI-PAIRED-CHAIN-001). A telescoping identity
proves the family over the integers, and full coefficient and ordinary
matrix-product checks cover `a=2,...,8`. The first `P2 -> M2` witness
includes four exact off-support cancellations. This is a positive tensor
construction, but its finite character gate has strict slack at `t=3/4`
for every `a`, so it does not improve the exponent. Its specific quotient
does not extend to square `M(a,a,a)` at `a=3,4,5`.

The [Laurent pilots](research/ai/2026-10-20-paired-direct-sums/laurent_search.md)
record four first-order alternating fits and two bounded refinements for
`P3 -> M(1,3,3) direct_sum M(3,3,2)`. Every completed run retains nonzero
full coefficient error or uncancelled poles. Exact positive and negative
controls check the coefficient verifier, and six saved coefficient arrays
replay the reported residuals. These finite failures do not exclude the
target or establish a degeneration (EXP-PAIRED-LAURENT-003).

The [second-order continuation](research/ai/2026-10-20-paired-direct-sums/higher_jet_search.md)
retains two completed degree-two Laurent searches with all pole and target
equations. Both have nonzero pole coefficients (EXP-PAIRED-HIGHER-JET-004).
The [narrow-source searches](research/ai/2026-10-20-paired-direct-sums/narrow_source_search.md)
test `Q_(3,2) -> M(3,2,3)` using eight full coefficient fits and ten kernel
compression runs, including two complex runs. None produces a construction.
Closure-only fits approach nearly singular normalization matrices; condition,
commutant, and trace-form checks reject those false leads. An exact algebra
recognition criterion and positive and negative controls accompany the
searches (EXP-NARROW-SOURCE-005, LEM-NORMALIZED-SLICE-006). All 24 new saved
points recontract to their reported metrics. Two lagging intermediate
checkpoints were recovered by deterministic reruns matching the complete
original numerical histories. These finite experiments imply neither
existence nor nonexistence of the proposed target.

The [complete narrow-source Koszul screen](research/ai/2026-10-20-paired-construction/narrow_koszul_exact.md)
computes all 25 exterior-degree comparisons on all three legs for
`Q_(3,2) -> M(3,2,3)` (EXP-NARROW-KOSZUL-001). Signed coefficient matrices
give exact rational ranks, with independent modulo-two eliminations
matching every value. The long target legs are padded from six to eight
coordinates before comparison. All tests pass; this supplies neither
the desired maps nor an exponent improvement.

## Varying quantum recoupling

The [quantum family](research/ai/2026-10-20-quantum-recoupling/family.md)
uses rational Clebsch--Gordan changes of basis that vary with q. Explicit
local factors keep the generic source isomorphic to convolution. Exact
controls check 196 projection positions, 360 invariant equations and 30
small basis/root configurations. At q=i, the rowwise-regular cyclic maps
have ranks 8,32,64 at a=2,3,4 over Q(i). This calibration produces ordinary
restrictions and does not supply the size-four matrix target. Coupled
singular normalizations remain open; no exponent improvement is claimed.

The [paired quantum calibration](research/ai/2026-10-21-paired-quantum/README.md)
checks 64 prescribed local maps and 353 rational-function source identities
(AI-PAIRED-QUANTUM-001). At size ten and root order fourteen, the specified
rowwise regular first map has rank 91, below the selected target's 100.
Two small regular limits have matching matrix-tensor dimensions but fail
exact slice-algebra closure tests. These calculations concern the stated
normalization only.

Two [coupled Laurent families](research/ai/2026-10-21-paired-quantum/coupled_faces.md)
now give exact intermediate tensors `P3 -> F0,F1`, each of format `(9,15,15)`
(AI-PAIRED-QUANTUM-002). The verifier checks all 288 nonzero rational-function
coefficients, proves cancellation of every pole, and records 241 and 108
nonzero rational leading coefficients. Both tensors pass every first-leg
Koszul test for the small two-block target, but an invertible source slice
excludes an ordinary restriction. `F1` has a rank-two first slice, and a
closed projective incidence argument excludes every further degeneration
to that concise target, whose minimum first-slice rank is three. Further
singular extraction from `F0` remains a construction question. These are
actual intermediate degenerations, not matrix direct sums or smaller
matrix multiplication exponents.

The [unequal quantum extension](research/ai/2026-10-21-narrow-quantum/README.md)
gives explicit generic local maps for every `Q_(n,m)`, with an all-size
coefficient identity and 841 finite controls (AI-NARROW-QUANTUM-001).
Twenty-three specified root-eight Laurent families for `Q_(3,2)` have
complete exact coefficient and valuation certificates. Nine limits lose
first-leg concision, ten have rank-one slices that exclude all further
degenerations to the target, and four fail a Koszul comparison. Two of
those four pass every first-leg test but fail a long-leg test by one rank
(`62<63`). These are fixed-family exclusions; other bases, weights, and
singular maps remain open.

## Polynomial flags and numerical calibration

The [polynomial flag argument](research/ai/2026-10-20-singular-flags/normal_form.md)
reduces arbitrary constant matrices followed by strict target-compatible
weights to decreasing input-degree flags and increasing output-pivot flags.
An equal-degree coefficient is a product of nonzero pivots. This excludes
the earlier m=4,B=10 grading eta=(7,14,21,0), and forces B>=N+m-1 in the
stated separated cone. The proof is written and unreviewed. Balanced orders
and arbitrary Laurent input mixing remain open; the additive cost does not
close the asymptotic construction question.

An [exact source-family calibration](research/ai/2026-10-20-singular-flags/masked_residuals.md)
has partial squared error t^(-6) while full squared error is
t^(-6)+2t^2+t^8. The retained balanced complex pilot likewise has no valid
certificate: its smallest partial residual is about 5.25e-8, but the full
relative error is about 61501 at the best parameter in the recorded interval.
All discovery reports remain experiments. Exact controls preserve known
m=2,3,4 limits through the full normal-form reduction.

The [balanced coefficient system](research/ai/2026-10-20-balanced-coefficients/elimination.md)
now gives an exact algebraic construction problem in a restricted monic
flag ansatz: 53 integer polynomial conditions of degree at most 12 in 57
parameters, after 68 coefficients are eliminated by unimodular systems.
An exactly checked finite-field solution with full-row-rank Jacobian would
lift to characteristic zero by standard Hensel theory. No qualifying point
or complex degeneration has been found. Monic pivots are an additional
restriction; the written reduction does not settle general constant maps.

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
The all-size unequal-source inequality is now settled by the
[sharp unequal-source proof](research/ai/2026-10-20-unequal-entropy/research_note.md)
(AI-UNEQUAL-ENTROPY-001). For every four lengths at least two, the explicit
upper certificate has ratio at most
`B=(81/350)*(1+14*sqrt(14)/27)^(4/3)`, with
`0.974772906<B<0.974772907`, attained only at `(2,2,2,2)`.
Every other tuple has ratio at most `97/100`. Eight all-size polynomial
cones, 216 small-minimum tail certificates and 37 proved residual cases
support the analytic proof. It is written and unreviewed. The sharpness
statement concerns `U`, not the entropy optimum or the exponent.

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

## Exact small cyclic mixed-map construction

[AI-CYCLIC-MIXED-RESTRICTION-046](research/ai/2026-10-20-cyclic-mixed-map/README.md)
supplies explicit integer maps for the ordinary restriction
A_2 -> M(2,3,4). All 576 coefficients agree exactly, including all 552
required zeros; the identity holds over every field. The three matrices
have 40 nonzero entries in total, all +/-1. This strengthens the earlier
rational M(2,3,3) witness, which is retained with its discovery history.
The certificate has no independent mathematical review or Lean
formalization. Its profile lower bound is weaker than the existing scalar
bound, so it does not improve the exponent. Larger mixed or singular
constructions remain open.

The [all-power full-capacity argument](research/ai/2026-10-20-cyclic-mixed-map/full_capacity.md)
(AI-CYCLIC-FULL-CAPACITY-047) excludes arbitrary complex degenerations
from A_a^r to direct sums of square matrix products that use every source
coordinate. It combines an all-power minimum-slice-rank formula with
external polystability theory. In particular A_5 -> M15 and S_4 -> M112
are excluded even with singular maps. The smaller H1100 and H106 targets
remain open; this gives no uniform asymptotic gap or exponent improvement.
The proof is written and unreviewed. Finite controls check 112 triangular
minors plus an independent tensor-square coefficient expansion.

[AI-CYCLIC-CENTRAL-POLYSTABILITY-048](research/ai/2026-10-20-cyclic-recoupling/central_polystability.md)
strengthens the earlier ordinary-map exclusion for the degree-(6,6,6)
central multiplicity block B: B cannot degenerate to M2 over C. Four exact
rational polynomial identities prove smoothness of its associated cubic;
external stability theorems and cyclic symmetry yield a closed special-linear
orbit. The earlier determinant obstruction then excludes the required
isomorphism. This concerns B itself, without cancelling its accompanying
scalar tensor. The proof remains unreviewed and gives no exponent gain.

## Graded cyclic construction pilots

[EXP-CYCLIC-GRADED-PILOTS-049](research/ai/2026-10-20-cyclic-singular-search/README.md)
records four exact kernel certificates blocking one-sided new-vertex
extensions of two fixed M(2,3,3) witnesses. Changing the old maps or using
more general Laurent maps remains open. Two 16-start weighted ALS searches
and two refinements supplied no exact M3 degeneration. Saved diagnostics
include large omitted coefficients; masked residuals are not certificates.
The exponent is unchanged.

## Equivariant cyclic construction obstruction

[AI-CYCLIC-EQUIVARIANT-050](research/ai/2026-10-20-cyclic-equivariant/README.md)
proves an all-size five-coefficient polynomial obstruction to diagonal-SL2
equivariant A_a to M_(2a-1) degeneration with irreducible vertex actions.
Exact representation counts also exclude all choices of matrix-vertex
representations for the specified H1100 equivariant ansatz; A2 to M3 is
closed by combining the count with the polynomial identity. General maps
that break this symmetry remain open. The proof is unreviewed; the exponent
is unchanged.

[EXP-CYCLIC-CARTAN-FRONTIER-051](research/ai/2026-10-20-cyclic-equivariant/torus.md)
relaxes the action to its torus. Exactly one necessary H1100 vertex-character
triple survives an exhaustive 89-case integer coefficient search. This
selects 3854 allowed map entries, but supplies no construction. Completed
32-start A2 and six-start H1100 pilots found no exact witness; several of
the latter escaped to large norms.

## Changed first jets at the quantum root flags

[AI-QUANTUM-EXTENSION-SPACES-075](research/ai/2026-10-21-quantum-extension-spaces/proof.md)
uses the concurrent partial-saturation argument to force dim W1=12 for
M(10,10,11) with the prescribed rank-four leading images. Exact rational
constraints classify all changed first derivatives: 20 dimensions per new
output row and 532 coupled leading-row parameters, totaling 4772 for two
110-row maps. The bilinear next component has first flattening rank 25
and maximum matrix-slice rank at most eight. Other second-jet terms remain
free, and no complete degeneration or smaller exponent is established.
The proof is written and unreviewed.

[AI-QUANTUM-BOUNDARY-TRAP-076](research/ai/2026-10-21-quantum-extension-spaces/proof.md)
excludes all orders when the four leading output rows stay in explicit
56-dimensional boundary spaces; the other rows may vary arbitrarily.
A separate necessary bound caps the second partial saturated space at
37 dimensions for all compatible first derivatives. Moving leading rows
outside those spaces remains open, and compatible first-order directions
that do so exist. These written proofs are unreviewed.

## Maximal first jets with moving leading rows

[AI-QUANTUM-MAXIMAL-JET-077](research/ai/2026-10-21-moving-boundary-flags/proof.md)
extends the boundary obstruction to moving leading rows when both outside
first-jet quotient ranks are 16. Exact linear systems leave only four
normal directions. They move a common polynomial plane, and a formal
induction confines the full maps to spaces of dimension 56. Thus these
maximal first extensions cannot reach M(10,10,11) at any order. At least
one first extension must be rank-deficient for a possible construction
with the same leading maps. The written proof is unreviewed; delayed
growth and other flags remain open, and the exponent is unchanged.

[AI-QUANTUM-RANK-FOUR-078](research/ai/2026-10-21-moving-boundary-flags/rank_deficient.md)
strengthens the necessary first-extension threshold: at least one quotient
rank must be at most twelve. Every nonzero one-leg obstruction has rank
at least four, proved by three rounds of exact triangular minors and
linear restrictions. Thus arbitrary quotient spans of dimension at least
thirteen on both sides are excluded at every order. The lower-rank and
delayed cases remain open; this is a written unreviewed result, with no
exponent improvement. The concurrently inspected second-jet package at
d8de82f already gives the stronger conditions W2=W0 and rank sum at most
24 (at most20 with mixed directions); the rank-four certificate is retained
as auxiliary structure, with no claim to improve that target frontier.

## Exact mixed second-order family

[EXP-MIXED-TWOJET-FAMILY-079](research/ai/2026-10-21-mixed-first-jets/family.md)
constructs sixteen independent leading-row directions with first-extension
quotient ranks14 and6. Explicit maps and regular first-row corrections
solve every coefficient equation through order two for every combination
of the parameters. The separate constructor and full coefficient verifier
retain all136 quadratic monomials. The active output formats are18 and10;
later growth and a matrix target remain unconstructed. An exact nonzero
third coefficient is retained as an order-boundary check. This finite
polynomial certificate does not improve the exponent.

[AI-MIXED-THIRD-ORDER-080](research/ai/2026-10-21-mixed-first-jets/third_order.md)
now excludes the target for these fixed 14-by-6 first subspaces at every order.
The exact normal space has dimension 16. Successive universal matrix-rank
covers impose six plus six independent constraints, leaving only the four
common-plane tangents. Arbitrary correction-row freedoms vanish from the
projected obstruction, and formal induction bounds both map ranks by 56.
This is an unreviewed scoped proof; other mixed spaces and delayed growth
remain open, and the exponent is unchanged.

[AI-MIXED-PENCIL-FRONTIER-081](research/ai/2026-10-21-mixed-first-jets/pencil_frontier.md)
extends this exclusion to **every** maximal mixed pair of quotient ranks
14 and 6, in either order. Exact source symmetries reduce the pencils to
two representatives. Target slice-rank divisibility bounds the generic
projected third space by dimension two; twelve cubic minors force it to
vanish and leave only plane motion. The necessary mixed first-rank sum
therefore drops from 20 to **19**. If both mixed projections are nonzero,
the block argument already gives sum at most 16. These are scoped,
unreviewed obstruction results, with no change to the exponent. The
concurrent third-boundary proof at `1068ce9`, Section 5, independently
proves a broader target-side third-rank ceiling; that overlap is credited
in the pencil note.

## Simultaneous mixed first projections

[AI-BOTH-MIXED-FIRST-SPACES-082](research/ai/2026-10-21-both-mixed-first-spaces/proof.md)
shows that when both mixed projections are nonzero, each must be a line,
even with arbitrary boundary graph corrections. Rank-one lines have a
unique partner relation and quotient ranks at most 7 each. Invertible
mixed lines force quotient ranks exactly 1 each. The necessary sum in
this case drops from 16 to **14**. Exact compatible 7-by-7 and 1-by-1
first spaces are retained; their polynomial maps still have first rank 12.
The invertible-line example leaves 72 normal directions before further
lifting equations. This is a written, unreviewed local classification,
not a matrix target or exponent improvement.

## Invertible-line lifting equations

[EXP-INVERTIBLE-LINE-LIFTS-083](research/ai/2026-10-21-invertible-line-lifts/calculation.md)
reduces the selected invertible seed's normal dimension from 72 to 40
using the target's zero projected third block. A specified 36-direction
ansatz has sixteen exact quadratic conditions for second leading rows
and third new rows. A retained compatible control has uncorrected first
rank 13. Third leading rows and later coefficients remain to solve;
these equations do not classify arbitrary corrections or construct the
matrix target. The linear decomposition is not a nonlinear gauge reduction.

## Regular root flags and Laurent first-leg maps

The [saturated-rowspace argument](research/ai/2026-10-20-graded-quantum-flags/saturation.md)
proves a source-leading-map slice bound while allowing an arbitrary Laurent
first leg and arbitrary regular higher jets on the other two legs. Exact
root-map certificates give ceilings 62,44,64,68,86 at orders 4,8,12,16,24,
below the size-four target's required slice rank 100. A separate
[central-weight proof](research/ai/2026-10-20-graded-quantum-flags/graded_obstruction.md)
excludes sixteen order-three/six phase pairs under the stated grading
hypotheses, using explicit nonzero coefficients over Q(zeta_6).
The unique Cartan profile is adopted from claim 051; the second integer
recursion only checks that earlier result. All new proofs are written and
unreviewed. Different flags, ungraded constructions and powers remain open.

## Candidate quantum quotient and weight-block comparisons

[AI-CYCLIC-ROOT-MODULES-053](research/ai/2026-10-20-cyclic-weight-blocks/root_quotient.md)
realizes the formal negative-singlet vertex character as an actual quantum
quotient at a root of unity. The quotient keeps a divided-power connection
that would be lost by treating its ordinary-generator pieces independently.
This supplies target representation data, not the required tensor maps.

[EXP-CYCLIC-BLOCK-FLATTENINGS-054](research/ai/2026-10-20-cyclic-weight-blocks/README.md)
retains 14364 grading upper comparisons and 3924 modular source-rank
comparisons on the selected A3, A4, A5 blocks. None excludes its target.
The specified quantum leading flags closed by PR33 remain closed, and no
exponent improvement is established.

## Size-five Cartan frontier

[AI-CYCLIC-CARTAN-SCREENS-052](research/ai/2026-10-20-cyclic-equivariant/a5.md)
uses exhaustive character factorizations and a five-inequality dual certificate
to exclude three of the four size-five targets that passed the general
constant-map screens, within the specified Cartan-intertwining class.
M(14,14,15) still passes the displayed character and extreme-slice tests.
An actual degeneration to it would imply omega<2.245; it is unconstructed.
Completed 32-start size-three and six-start size-five pilots produced no exact witness.

## Quantum first jets with constant output projections

The [first-jet saturation proof](research/ai/2026-10-20-quantum-jet-filtration/proof.md)
removes the grading assumption for the prescribed order-three/six quantum
curves. Thirty-two nonzero 64-by-64 minors give a full-output slice ceiling
56, allowing arbitrary Laurent first-leg maps and all nonzero approach rates,
orders and higher terms. A separate uniform inactive-slice argument gives
ceiling 94 after arbitrary constant codimension-two output projections
before taking the limit. Both ceilings are below the target's required 100.
Claims AI-FIRST-JET-SATURATION-001 and AI-QUANTUM-CURVE-JETS-002 are written
and unreviewed. Six completed finite-field coefficient pilots are retained
as discovery data only. Parameter-dependent projections, different leading
flags and non-scalar block weights remain open; the exponent is unchanged.

The [higher-jet extension](research/ai/2026-10-20-higher-jet-quantum-flags/higher_jets.md)
also permits moving output maps that remain surjective at the limit, with
slice ceiling 98. Leading output ranks below 110 remain open. Separately,
[256 single-leading-block flags](research/ai/2026-10-20-higher-jet-quantum-flags/blocks.md)
in the specified two-layer family have saved minors giving ceiling 97 for
regular full-output limits; pre-limit projections are outside that finite
cover. The new proofs are written and unreviewed. None gives an exponent gain.

The [second-jet spanning certificate](research/ai/2026-10-21-second-jet-rank-one/rank_one.md)
sharpens PR45's bound37 to W2=W0 of dimension12 at its canonical leading
flags. Twenty-six exact rank-two slices span the entire25-dimensional
bilinear image. Including the complete second derivatives and row correction
leaves every potential second target residue below the minimum matrix rank11.
The actual bilinear first-jet product must therefore vanish. Its effective
first-row rank sum is at most24, or20 after a mixed component. These proofs
are written and unreviewed; higher-order lifting and the exponent goal remain
open. Canonical extension data and their earlier classification retain PR45's
credit.

## Local audit of an external tensor-degeneration preprint

The [exact local audit](research/ai/2026-10-21-sun-local-audit/README.md)
reconstructs selected maps from arXiv:2610.13971v1, with the inspected HTML
pinned by hash. It finds a repairable scalar normalization omission and
verifies four local Laurent leading tensors, four generic endpoint blocks,
and 256 crossed-group identities. The complete M32 maps remain unverified;
the preprint's claimed exponent improvements are not adopted.

A separate elementary centroid argument excludes a bridge that first
collapses to the fixed zero-fibre tensor D256 tensor M2 and then seeks M32.
This narrower obstruction does not exclude every enriched assembly.
The audit and written proof remain AI-derived and externally unreviewed.

The [packetwise follow-up](research/ai/2026-10-21-sun-local-audit/packet_lift.md)
shows that an individual printed generic packet contribution contains M2,
whose exact Koszul rank exceeds that packet's stated border-cost ceiling.
It excludes a lift preserving each such contribution, while allowing the
possibility of different global maps with interpacket cancellation.

## Source-weight windows and full original-source Laurent fibers

Claims `AI-WEIGHT-WINDOWS-098` and `AI-ORIGINAL-JET-FIBERS-099` preserve
two completed local packages. No exponent below 9/4 is established.

Every ordinary A88 to M27 plus M7 restriction needs at least one
matrix-unit image whose source weights span at least four. The exact
width-three containing-space sequence is 960,948,906,844,622, contradicting
the required 778 dimensions. Width four is a proved fixed point of this
particular screen. An explicit slice over Q(phi), phi^2=phi+1, has rank 384
although its middle homogeneous component has rank 512. It supplies one
cancellation direction, not full target maps. See
[the proof and exact acceptance certificate](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_weight_windows.md).

The original-source Laurent construction has generically invertible
960-by960 maps on all three legs, exact cancellation of every negative
power, and 28,316 nonzero constant coefficients. A recorded coordinate
projection is concise in format 936 by 936 by 935. However, 42 selected rows
per leg cover the complete constant support, so its slice rank is at
most 126. The intended M27 plus M7 target has slice rank 778. Consequently
this limit cannot reach the target by restriction or further degeneration.
The full source and other Laurent families remain open. See
[the complete maps, fiber equations, and cover proof](research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_original_fibers.md).

The source-map, fiber-system, rank, coordinate-cover, and tamper checks
pass in the same generating session. The proof status remains written
and unreviewed externally. The next construction searches use moving
physical compression spaces and the exact weight-mixing module equations.

The [corrected prolongation family](research/ai/2026-10-21-corrected-prolongation/proof.md)
constructs complete second jets with fixed boundary first frames. Exact
off-diagonal constraints reduce532 leading parameters to172; all36 remaining
quadratic obstructions vanish identically. Twenty-eight independent leading
directions still leave the fixed boundary spaces. Two exported rational
witnesses verify the entire first and second coefficients, including both
source-row corrections. These are finite-order data, not a matrix limit.
The boundary-frame matrix-target lifting question is closed by the following
third-order argument; the exponent goal remains open and the proof is unreviewed.

The [third-order boundary trap](research/ai/2026-10-21-third-boundary-trap/proof.md)
excludes these full boundary first frames at every order, including delayed
and unequal first-growth orders. An exact normal calculation leaves28
parameters; the third block has coefficient image24 and sharp minimum
nonzero first rank8. The matrix target forces first rank at most2. Only
four common polynomial-plane motions remain, and formal induction traps
both regular leg maps in dimension56. Ordinary effective first rank sum24
is therefore excluded; the necessary sum is at most23. A separate general
consequence forces third first rank at most2 on K_inf for every admissible
ordinary first pair at these flags. The complete PR49 second jets remain
valid finite data. These proofs are written and unreviewed; different first
subspaces and leading flags remain open, and no exponent improvement follows.

The [arbitrary-hyperplane extension](research/ai/2026-10-21-boundary-hyperplanes/proof.md)
now excludes both first boundary dimensions at least11 at every order,
including delayed unequal growth. It covers every complex hyperplane.
Boundary obstruction matrices have minimum nonzero rank2. The full third
matrix span is S0 tensor Mat2, with dim S0=20 in Mat6x6 and no rank-one
matrix; exact polynomial identities certify this. A general compression
lemma loses at most5 slice dimensions under two arbitrary hyperplanes.
First rank at least8 therefore leaves at least3, above the target ceiling2.
At ordinary first order one effective rank is at most10 and the total is
at most22. Pairs12,10 remain open. The proofs are written and unreviewed;
no matrix-multiplication exponent improvement follows.

The [biform third-core theorem](research/ai/2026-10-21-biform-third-core/proof.md)
identifies the entire third tensor as the4,2,2 outer-product tensor times
a4-by6-by6 core. Its matrices lie in the kernel of ordinary biform
multiplication of degrees(1,2) and(2,1), under determinant-one basis
changes. This gives a short rank-one exclusion and improves the actual
two-hyperplane loss bound from5 to the sharp value3. A general sharp
projection lemma for losses1,3 and conditioned obstruction minimum4 then
exclude every arbitrary boundary first pair of dimensions at least11,9,
in either order, including delayed unequal growth. The necessary ordinary
first-rank sum at these flags is now at most20. Pure boundary pairs12,8
and10,10 remain at that threshold; a retained general losses2,2 control
shows why the new projection lemma alone cannot close them. These are
written unreviewed proofs, not an exponent improvement.

The [integrable boundary shear](research/ai/2026-10-21-integrable-boundary-shears/proof.md)
gives an exact two-parameter non-plane family at effective first ranks10,10.
Both source rowspaces move, while the full112-by14-by14 contraction stays
constant with first rank12. For every nonzero parameter pair the moving
14-dimensional spaces are complete mutual annihilators on the fixed
100-dimensional source kernel; exact polynomial chart minors prove this.
The resulting degree-two maps satisfy all-order coefficient equations
with zero source-row corrections. Their generic row ranks are14, so
this family cannot reach the110-dimensional target legs. It establishes
integrability of two additional normal directions, not an improving matrix
limit. Higher-rank completions and the exponent goal remain open; the
construction and completeness proof are written and unreviewed.

The [updated ordinary rectangular frontier](research/ai/2026-10-21-rectangular-ordinary-frontier/proof.md)
applies the already proved polynomial/Hankel gates to every improving
sorted single matrix format for balanced a=2,...,12. Of5139 formats,4192
are excluded and947 survive. All improving ordinary shapes through a7
are closed; a8 has exactly M(27,28,28), with legs756,784,756, as a survivor.
Its maps are unconstructed. The existing spectral implication would give
omega<=191/85 if that premise were supplied, certified by the recorded
integer comparison; no exponent improvement is established. The earlier
polynomial-rank-locus note already excluded all four A5 ordinary targets;
this scan updates the stale minimum-only research queue and retains that
prior credit. A separate corner-minor note rederives the existing rank
inequality, without claiming a new general theorem or independent review.
