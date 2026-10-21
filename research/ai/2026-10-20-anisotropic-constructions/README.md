# Unequal-length cyclic convolution targets

October 20-21, 2026. This package contains an AI-derived conditional
reduction, construction searches, and ordinary-restriction obstructions.
The proposed degeneration is unconstructed. No exponent below 9/4 is
established. The full-source rank-gap proof was checked by a second agent
in this generating session; no external independent review or
formalization is claimed.

Construction work now includes exact full-source restrictions
A(5,5) to M9 and to M8 plus M3; A(5,6) to M10 and to
[M8 plus A(2,3)](parity_structure_residual.md); and a
[scalar-extended restriction](parity_balancing_spin1.md)
A(2,2) plus one scalar to M3. Complete rational maps and coefficient
checks are saved. None of these constructions establishes an exponent
improvement.

The [corner-split construction](parity_structure_corner_extension.md)
also supplies A(2,2) plus one scalar from A(2,3), and gives a general
two-source restriction whenever the stated low and high long-coordinate
intervals are disjoint. It provides exact source-recycling controls.

Two newer all-size constructions retain their extra tensor explicitly.
The [full residual family](parity_structure_full_residual.md) gives
A(a,a+1) to M(2a-2) plus A(2,a-2) for a>=5, including exact maps for
A(7,8) to M12 plus A(2,5). The
[triangular quotient construction](parity_balancing_triangular.md) gives
A(a,b) plus M((a-1)(b-1)) to M(a+b-1) for every a,b>=2. Its auxiliary
matrix source cancels a stated residual on shared variables.

The [ordinary square-partition frontier](square_sum_frontier.md) now
rules out every target strong enough for this package's finite 9/4
score test from all 60 sources with 2<=a<=b and N=ab(a+b-1)<960.
The first source surviving these necessary tests is A(8,8). Its
unconstructed target M27 plus M7 would imply omega<2.2485 if the
required maps were found. The former ordinary A(7,8) target M25 plus
M5 and A(5,6) target M16 plus M4 are excluded; their conditional
numbers 2.247 and 2.248 are superseded as ordinary construction
objectives. These results do not exclude
singular full-source degenerations or arbitrary rectangular sums.

An earlier parity
degeneration of A(5,5) has 225 coordinates on each leg and 11,725 terms,
but the [annihilator proof](parity_annihilator.md) excludes its proposed
M14 plus M4 target, even for singular degenerations. The
[singular-support note](singular_support.md) preserves the exact source,
historical conditional arithmetic, score screen, and positive controls.
No improving target maps have been constructed.

## Original conditional target

Let C(a,b) be polynomial convolution, with lengths a, b and a+b-1.
Consider the cyclic product of three copies:

    A(a,b) = C(a,b) tensor C(a,b)^cyclic tensor C(a,b)^(cyclic squared).

All three source spaces have dimension N=ab(a+b-1). The starting question was

> Does A(4,5) degenerate over C to M(12,12,13)?

The source format is (160,160,160); the target format is (144,156,156).
An actual degeneration would imply the exact rational bound omega<=561/250
=2.244. It has not been found. The subsequent rank-gap argument excludes
ordinary constant maps for this target, so its remaining construction
question requires a singular degeneration. Passing a finite screen is
not evidence of existence.

This source has unequal convolution input lengths. It differs from the
balanced cyclic A_4 to M(10,10,11) target and the paired-source target in
PR #17. The route uses the existing finite-amplitude comparison and the
existing triangular-minor argument, with their hypotheses extended to
unequal lengths. It does not replace an already constructed algorithm.

## Conditional exponent implication

Let lambda be a tensor character, let its three dot-product parameters
sum to 3t, and let P be the six-orientation profile used in the existing
notes. The source A(a,b) is cyclically symmetric. It need not be invariant
under every leg permutation when a and b differ.

Suppose A(a,b) degenerates to M(l,h,n). Apply the same degeneration after
each cyclic leg permutation. Multiplying the three character inequalities
gives lambda(A(a,b)) >= (lhn)^t. Reflecting all three source legs gives the
other three convolution orientations and the reflected matrix target, so
the same reasoning gives lambda(A(a,b)^reflection) >= (lhn)^t. Their
product is P(a,b)^(6t). Since t>0,

    P(a,b) >= (lhn)^(1/3).                              (1)

This argument retains both cyclic orientations. Equating a single
three-factor character value with P(a,b)^(3t) would be unjustified.

OpenAI's shifted tripling and the existing local two-sector inequality give

    3 P(a,b) <= P(a,3b+a-1),
    2 P(3b+a-1,a) <= [3(a+b)-2]^(1/t).

Symmetry of P therefore gives, at every positive integer a,b,

    6 P(a,b) <= [3(a+b)-2]^(1/t).                       (2)

Combining (1) and (2) uniformly over characters yields

    omega <= 9 log[3(a+b)-2] / log(216 lhn).             (3)

The conversion in (3) is the detecting-character argument in OpenAI's
paper, already used in the balanced finite target note. For the selected
target, 216*l*h*n=404352 and 3(a+b)-2=25. The rational comparison has the
integer certificate

    404352^561 > 25^2250.                               (4)

Thus the unproved degeneration would give omega<=561/250. The descriptive
real number in (3) is about 2.2439806565. Equation (4) verifies only the
implication's arithmetic, not its missing premise.

## The ordinary-map minimum-rank test

In zero-based coordinates the source coefficients are one at

    X=(i,p+q,s), Y=(j,p,r+s), Z=(i+j,q,r),

where i,p,r range from 0 to a-1, and j,q,s range from 0 to b-1.
A first-space slice F has matrix entries

    F_(H-j,p+q,L-r)

in rows (j,p,L) and columns (H,q,r). Coefficients outside their ranges
are zero. The minimum rank of a nonzero slice is exactly ab.

To prove the lower bound, choose k with some F_(i,k,s) nonzero, then
the largest such i=i0 and the largest s=s0 at i0. Write k=p0+q0 in
the allowed ranges. Retain rows (j,p0,r'+s0) and columns (j'+i0,q0,r),
for 0<=j,j'<b and 0<=r,r'<a. This is a block triangular ab-square
matrix with every diagonal coefficient F_(i0,k,s0). Its determinant is
that nonzero coefficient to the ab power. A slice supported at (0,0,0)
has exactly ab nonzero entries in distinct rows and columns, proving
equality. Cyclic symmetry gives the same minimum on each space.

For an ordinary restriction to M(l,h,n), the rank-one first-space target
parameter has slice rank n. Its nonzero lift has source slice rank at
least ab. The other two maps lose rank at most their kernel dimensions.
Consequently the three necessary inequalities are

    n(l+h-1) <= 2N-ab,
    l(h+n-1) <= 2N-ab,
    h(n+l-1) <= 2N-ab.                                 (5)

At A(4,5) and M(12,12,13), the right side is 300; the left sides are
299, 288 and 288. The target passes this test with slacks 1,12,12.
The stronger rank-gap argument below excludes it despite this positive
slack.

## Gap above minimum slice rank

The [full-source proof](slice_rank_gap.md) shows, over C and for 2<=a<=b,
that every nonzero source slice has rank ab or rank at least ab+a. Its
projective minimum-rank locus is the Segre image of

    P^(a-1) x P^1 x P^(b-1),

of dimension a+b-1. The proof first writes a biform block as a polynomial
matrix. Splitting its kernel bundle on P^1 gives the exact rank formula
ab+sum min(b,mu_j). A full block-Hankel argument then forces every slice
below the next rank to have two separable factors and one rank-one
Hankel factor. A second agent in this generating session checked both
stages and the dimension argument; no external independent review is
claimed.

For A(4,5), source slice ranks are 20 or at least 24. Every lifted
rank-one first-leg parameter of M(12,12,13) would have rank at most
13+4+4=21. Ordinary maps would therefore inject the dimension-22
rank-one matrix variety into the dimension-eight minimum-rank locus.
This is impossible. Singular degenerations are not excluded.

The exact controls cover all 4,684 nonzero binary biforms in four small
formats, all 4,095 nonzero A(2,2) binary slices, and six rational examples
attaining the first rank above the minimum. The strengthened finite
screen also removes A(4,6) to M(14,14,15). Its surviving targets remain
unconstructed; the smallest source dimension among them is 225, with
A(5,5) and four target shapes listed in the saved frontier.

## The complete low-rank slice locus

The subsequent [polynomial-matrix argument](polynomial_rank_locus.md)
classifies every nonzero full-source slice below rank 2ab: its long
coordinate factor must be one fixed rank-one Hankel vector. Two nested
polynomial-multiplication injections give the lower bound ab times the
generic Hankel-symbol rank. Degree bounds force a rank-one symbol to
have a constant ratio. This strengthens the earlier rank-gap screen.

For an ordinary single matrix target whose first leg dimension exceeds
ab, the new necessary inequality is n(l+h-1)<=2N-2ab. It excludes all
four former A(5,5) rectangular survivors. For a direct sum, a selected
subsum of common leg dimension B>=2 must satisfy B+2(N-D)>=2ab, where D
is the full target leg dimension. Otherwise all three lifted subsum
spaces have coherent long factors and their source contraction has
tensor rank at most one. This excludes ordinary A(5,5) to M14 plus M3
and M14 plus M4. It does not exclude their singular versions.
Using rank-one ruling lines on all three legs further shows that every
non-scalar square block of size n requires n+2(N-D)>=2ab. Thus the
ordinary A(5,6) target M16 plus two M3 blocks is also excluded. M16
plus M4 met this strict threshold, but the stronger results below now
exclude it for ordinary maps as well.

The exact controls cover all 4,095 nonzero binary A(2,2) slices, sharp
rank-2ab examples, and integer three-leg factorization identities. The
three additional focused tests pass. The proof was checked by a second
agent in this generating session; no external independent review is
claimed.

## Higher Hankel ranks and the current ordinary frontier

The [Hankel-symbol dimension theorem](hankel_symbol_dimension.md)
adds a family of necessary conditions. For every integer r with
1<=r<min(a,b) and 3r<=a+b-1, an ordinary square block of size n obeys

    n^2>rab  implies  n+2(N-D)>=(r+1)ab.

Over C(x,z), the bounded Hankel rank of every lifted rank-one matrix
parameter forces their entire symbol span to have dimension at most r.
Selecting r long-coordinate polynomials then injects the original
complex block space into rab coefficients. The supporting scheme may
vary with x,z; no constant recurrence is assumed in this argument.
The note includes a self-contained proof of the classical scalar
Hankel/secant identification and cites a primary source for that
classical fact.

The [first-boundary theorem](hankel_boundary_dimension.md) now handles
exactly a+b-1=3r-1, for 2<=r<min(a,b). Its symbol dimension cap is
max(r,4), so the corresponding necessary condition is

    n^2>max(r,4)ab  implies  n+2(N-D)>=(r+1)ab.

A Chinese remainder argument shows that a moving rank-r line has a
pencil of annihilating polynomials, with reduced generic scheme.
The unique relation among 3r jets then forces a moving linear space
to have dimension at most two. Applying this to the two Segre rulings
gives the stated image bound. The proof was checked by two other
agents in this generating session. The
[counterexample beyond this range](hankel_segre_beyond_range.md) shows
why an unrestricted dimension-r statement cannot be assumed.

At rank exactly 2ab, a separate
[polynomial equality argument](parity_structure_equality.md) forces a
constant length-two long space. The
[three-leg factorization](hankel_rank_two.md) then has at most eight
coordinates per leg, including tangent and infinity cases. Thus when
a,b>=3 and a+b-1>=6, every block n>=3 requires n+2(N-D)>2ab.

For A(5,6), the general r=3 condition excludes even M16 alone:
16+2(300-256)=104<120 and 16^2>90. The
[exact partition enumeration](square_sum_frontier.md) combines all
these conditions with integer fourth-root bounds on the score
sum(6n)^(9/4). It excludes every improving ordinary square direct sum
from all 60 source formats with N<960. Its certified score maxima for
A(5,5) and A(5,6) are respectively 18916.994428<21952 and
26604.167197<29791. These are upper bounds over relaxed partitions,
not scores of constructed maps.

For A(7,8), the new boundary r=5 closes M25 plus M5: its lifted
rank-one slice upper bound is 293<336, whereas its M25 coefficient
space has dimension 625>280. The relaxed full square-partition maximum
is now 78910.828146<79507. Singular degenerations are outside this
argument.

The first surviving source is A(8,8). The two-block target M27 plus M7
has leg dimension 778 and passes the necessary conditions. If its
missing maps were constructed, the exact integer inequalities

    162^4497>92916^2000,
    42^4497>4465^2000,
    92916+4465>46^3

would imply omega<2.2485. The conditional arithmetic is established;
the tensor restriction is not.

Exact geometric controls include all 1,341 nonzero binary long
sequences in three small formats, 1,000 Hermite jet schemes, and 235
bounded-rank pencil checks. Counterexamples at a+b-1=3r-1 show why the
fixed-scheme line hypothesis cannot simply be removed. The tangent
factorization checks compare all 1,296,000 integer coefficients across
six choices of long spaces, using only the Python standard library.
The boundary controls add 25 exact moving-pencil specializations and
five integer relations among third-order jet schemes. The focused
tests pass. The general, equality, and boundary proofs were checked by
other agents in this generating session; no external independent
review or formalization is claimed.

## Exact construction controls

The saved positive controls now include the following ordinary
restrictions. None reaches an improving score in the finite comparison.

| Source | Exact image | Saved construction |
| --- | --- | --- |
| A(5,5) | M9 | [Integral product basis](parity_structure.md) |
| A(a,a), a>=3 | M(2a-2) plus M(a-2) | [Mixed direct-sum family](parity_structure_direct_sum.md) |
| A(5,6) | M10, or M8 plus M4 | [Integral two-block maps](parity_structure_a56.md) |
| A(5,6) | M8 plus A(2,3) | [Residual convolution source](parity_structure_residual.md) |
| A(a,a+1), a>=5 | M(2a-2) plus A(2,a-2) | [Full residual family](parity_structure_full_residual.md) |
| A(2,2) plus one scalar | M3 | [Scalar-corrected spin-one maps](parity_balancing_spin1.md) |
| A(a,b) plus M((a-1)(b-1)), a,b>=2 | M(a+b-1) | [Triangular quotient maps](parity_balancing_triangular.md) |
| A(2,3) | M4 | [Exact quotient control](parity_balancing_quotient_control.py) |
| A(8,8) | M15 | [Integral mixed seed](parity_structure_a88_seed.md) |

The residual A(2,3) construction keeps an entire convolution source in
the second block, which can later be subjected to another restriction.
Its maps have denominators dividing two, and every mixed coefficient
between the two blocks is zero.

The scalar-corrected construction has a short exact explanation. There
is a linear map J from three-by-three matrices into the twelve-variable
trace realization of A(2,2), and a fixed rational P, with

    P^(-1) J(A) P = [[A,0],[ell(A),tr(A)]].

Thus the original source produces
tr(ABC)+tr(A)tr(B)tr(C). A single disjoint scalar source, sent to the
negative trace on each leg, cancels the extra term. This explicitly
changes the source: it is not a pure A(2,2) to M3 restriction. The
complete nine-by-thirteen rational maps were replayed on all 729
coefficients, including a check by a second agent in this generating
session. No external independent review is implied.

For larger triangular quotients, the
[full-matrix correction score bound](quotient_score_barrier.md) shows
that this particular single-source comparison cannot reach the finite
9/4 score, even under the relaxed injective-map dimension condition.
Cheaper residual tensors or cancellation on shared variables require
separate constructions. The [fixed-core calculation](parity_structure_fixed_core.md)
also shows that keeping two legs of the explicit A(7,8) M12 core fixed
leaves a kernel of dimension 112; it does not exclude a construction
that changes those maps.


The [cyclic quotient-volume theorem](cyclic_quotient_volume.md) gives a
stronger geometric restriction on exact quotient equations: three
unrelated physical quotient spaces satisfy m0*m1*m2<=(a+b-1)^3 over any
field. Thus square quotient size is at most a+b-1. Even cancelling the
residual for free cannot make a single such matrix target pass the finite
9/4 comparison. This statement also covers exact quotient equations over
Laurent fields, while allowing unrestricted off-diagonal compression
families to remain outside its hypotheses.

For A(2,2), the [three-quotient determinant identity](parity_structure_three_quotients.md)
also shows that the normalized scalar correction has Frobenius norm at
least that of M3, so it cannot tend to zero in that regular exact-quotient
family. The pure A(2,3) to M4 control has zero kernel actions; all 4,096
target coefficients are checked. The A(8,8) M15 seed is similarly exact,
with a full 262,144-term integer contraction. Neither reaches the
unconstructed M27 plus M7 target.

## Earlier symmetry-restricted construction attempts

An SL2-equivariant construction can be searched through representation
multiplicities before solving for its actual coefficients. For the full
diagonal action on the three source factors, every source leg is

    V_(a-1) tensor V_(b-1) tensor V_(a+b-2),

where V_d=Sym^d(C^2). If matrix vertices carry SL2 modules U,V,W,
the target legs carry U^* tensor V, V^* tensor W and W^* tensor U.
All finite-dimensional SL2 modules are self-dual. Their irreducible
multiplicities must fit the source multiplicities on all three legs.

The exact enumerator uses the Clebsch--Gordan rule

    V_d tensor V_e = sum_(j=0)^min(d,e) V_(d+e-2j).

It enumerates every direct sum with the required total dimension and
fixed central parity, and checks all three pair products. This scope is
a chosen equivariant ansatz; arbitrary linear maps need not preserve it.
For A(4,5) and M(12,12,13), no representation triple fits. The search
also considers the diagonal action on two of the three source factors.
Its three multiplicity lists are

    (a+b-1) copies of V_(a-1) tensor V_(b-1),
    a copies of V_(b-1) tensor V_(a+b-2),
    b copies of V_(a+b-2) tensor V_(a-1).

No permutation of the selected target fits this second ansatz either.
This representation test alone does not exclude general ordinary maps
or singular degenerations; the separate rank-gap proof excludes the
selected ordinary map.
The known A_2 to M(2,3,4) target passes the two-factor representation
screen in two orderings, so the screen has a nontrivial control. A passing
representation test still does not solve the coefficient equations.

`paired_recoupling.py` is a separate exact discovery calculation. It
compares paired convolution and matrix coefficients after the inherited
Clebsch--Gordan basis change. It reports actual rational ratios rather
than recognizing matrix blocks from their dimensions. No output of this
program is a tensor-construction certificate.

## Complete diagonal-torus screen and broader discovery

The [central-block proof](torus_obstruction.md) closes the ordinary-map
construction class preserving the diagonal torus weights on the three
source factors. It allows arbitrary integer vertex weights on the matrix
target and dense maps inside each weight space. Two independent exact
enumerations agree on all 2,819 defect polynomials, 73 compatible pairs,
and two complete weight-profile triples. Both triples require an
isomorphism between a central source block with minimum slice rank four
and a target block with a rank-one slice. The explicit central triangular
minor proves the source bound for every slice, over every field.

The preceding eight ALS starts in that class had full relative errors
around 0.85235 and supplied no witness. Their reports and best arrays are
preserved. `dense_als.py` removes the weight-space restriction and checks
all 3,504,384 target coefficients. Two real starts, initialized by noisy
torus candidates, ran 60 sweeps each and reached a best error of
0.852348383062325. Three fresh complex starts ran 150 sweeps each and
reached 0.8523824047437201. The independent A(2,2) to M(2,3,4) integer
control has exactly zero residual and survives one least-squares sweep
within 2.5e-15.

The failed dense attempts are preserved with their seeds, trajectories,
best arrays, initial-array hash, and reproduction commands in
`results/anisotropic-constructions-2026-10-20/discovery-manifest.json`.
They are numerical discovery records. The ordinary-map exclusion rests
on the separate written proof. No singular degeneration to an improving
matrix target was found.

## Explicit singular intermediate tensors

`singular_support.py` now constructs three source faces by explicit
integer coordinate valuations. The step face has exact score certificates
excluding its selected large targets. The two parity faces retain three
of the four ordinary parity patterns. The parity110 face of A(5,5)
retains all 225 coordinates on each leg and 11,725 terms; six exact
modulo-101 slice calculations distinguish its full-rank slices from the
rank-224 slices of the parity000 face.

For the former parity110 target M14 plus M4, the elementary score bound
is 9,625,057, while the target's cubed leg dimension is 9,528,128. This
necessary test is passed, and exact positive restrictions to M(a,a,b)
provide coefficient controls. The stronger
[pairwise-annihilator argument](parity_annihilator.md) excludes every
square direct-sum target with leg dimension above 169, including M14
plus M4 and M14 alone. Large searches on this face were stopped.
`dense_als.py` now accepts either support face, direct-sum square
targets, and diagonal source preconditioners. Reports identify the exact
source mode and all scaling arrays used.

The [support note](singular_support.md) contains the direct slice-rank
proof of the score bound, checked by a second agent in this generating
session; no external independent review is claimed. Further support
balancing and structured-map work is being saved in separate files.

## Sources and scope

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, Sections 2, 4 and 5:
  character rules, shifted tripling, and exponent detection.
- The local [two-sector proof](../2026-10-20-truncated-algebras/two_sector_bound.md)
  supplies (2)'s second ingredient; its construction is credited rather
  than rederived as new work here.
- The balanced [cyclic finite target](../2026-10-20-koszul/cyclic_finite_target.md)
  supplies the original source and triangular-minor argument. The
  unequal-length formulation and two-orientation bookkeeping are this
  package's extensions.
- The local [cyclic recoupling](../2026-10-20-cyclic-recoupling/README.md)
  and [Clebsch--Gordan package](../2026-10-20-clebsch-gordan/README.md)
  supply the representation convention and maintained rational basis.

All local dependencies above were inspected at main
9a4ee3d05939d88730045877a6945165845f0398. The rank-gap argument has the
second-agent check recorded in its note. These checks occurred inside
the generating session; no external independent review is claimed.
The finite experiments have the exact scopes in their
reports. No improved exponent follows without the missing degeneration.
