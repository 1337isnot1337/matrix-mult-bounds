# Four mixed-row graph families

Written proof, unreviewed, October 21, 2026. Claim
`AI-MIXED-FIVE-GRAPH-CONTROLS-090`. Work over C at the canonical leading
flags, with the complete B seven-frame and partner parameters a=b=1.
Write the maximal C frame as (d0,...,d5,m), in the coordinate order of
the preceding uniform five-space package. Let V be any five-dimensional
subspace containing m+h, where h is one of

    (1,0,0,0,0,0), (0,0,0,0,0,1),
    (1,1,1,1,1,1), (2,-1,1,3,-2,1).

Every target-admissible normal is a common-plane direction. The adopted
shifted-order induction therefore excludes M(10,10,11) for these first
spaces, including arbitrary four-dimensional boundary parts, arbitrary
higher maps, delayed unequal first-growth orders and a Laurent first map.
This is four specified graph families, not a classification of all graphs
or an improvement of the matrix multiplication exponent.

## Actual mixed-row equations

Adopt the 88-dimensional full-B normal kernel, virtual C correction and
third tensor J from claim088. The correction error factors through the
C obstruction Psi, so it vanishes on every actual V contained in ker Psi.
The sixteen adapted low-rank source slices from that claim also vanish
on V by the target rank gap.

Use the invertible C basis shear U with last column (h,1). In the new
coordinates e6 is the actual vector m+h in V. Apply U to every C factor
of Psi and J. This transports the correction identity; it does not assert
that the original V contains the pure row m.

The last columns of Psi and the sixteen source slices give 312 linear
equations in 88 normals. In each specified case their complete rational
kernel has dimension32. The four plane directions annihilate both full
Psi and full J. A rational complement has dimension28. The verifier checks
that this complement and the four planes span the complete kernel.

Stack Psi and those vanishing source slices into Z(d), where d has28
coordinates. Its mixed column is zero and its rows annihilate V, giving
rank Z(d)<=2. Constant rational row operations on its joint coefficient
matrix give a56-row basis, preserving its pointwise rowspace for every
complex d. Denote its boundary columns by (E0,O0,E1,O1,E2,O2).

## Quadratic minors and a stable row subspace

Project the rowspace by Q=(O0-E0,O1-E1,O2-E2). The kernel of this projection
on joint row combinations gives10 rows W(d) in the rowspace of Z(d),
with W_odd=W_even. The coefficient kernel of W has dimension10.

For all four graphs, the following stronger projection property holds:

    rank Q(d)<=1 implies d=0.                         (1)

First use repeated triangular two-minors whose diagonal entries are
nonzero rational multiples of the same linear form. Such a minor forces
that form to vanish. For h=(1,0,0,0,0,0), the parameter counts are

    28 -> 14 -> 10 -> 4 -> 0.

For h=(0,0,0,0,0,1), the first reduction is28->26. For the other two
graphs, this preliminary step leaves28. On the residual spaces, collect
the coefficients of selected two-minors in the monomial basis x_i*x_j,
i<=j. The saved witnesses certify full square coefficient rank as follows:

| Graph | Residual parameters | Quadratic coefficient rank |
| --- | ---: | ---: |
| (0,0,0,0,0,1) | 26 | 351 |
| (1,1,1,1,1,1) | 28 | 406 |
| (2,-1,1,3,-2,1) | 28 | 406 |

The verifier constructs each determinant polynomial directly from the
rational linear coefficient matrix and performs exact elimination modulo
the prime32003. Every coefficient denominator is checked to be a unit
modulo that prime. The square coefficient determinant has nonzero
reduction, so it is a nonzero rational number. Consequently the selected
minors span the full space of quadratic monomials over Q, and also over C.
If Q has rank at most one, these minors vanish, hence every x_i^2 vanishes
and x=0. This proves (1) over C; it is not inference from a finite sample
of parameter values or from classification only over a finite field.

For every fixed d, the image of Row(Z(d)) under the projection is Row(Q(d)),
and its kernel contains Row(W(d)). Thus

    rank Z(d) >= rank Q(d)+rank W(d).

If d is nonzero, (1) gives rank Q(d)>=2. Since rank Z(d)<=2, W(d)=0.
The same conclusion holds for d=0. Every admissible normal therefore
lies in the explicitly computed10-dimensional kernel of W.

## The remaining target slices

Use the same unitriangular source change as the pure-row proof, now at
a=b=1. Subtract rows of Z from the source slices. These subtractions
vanish on the actual V and leave its restricted third tensor unchanged.
For twelve further adapted sources (original indices29,30,32,33,43,44,
46,47,50,51,53,54), the residual slice has rank at most two. The verifier
certifies this by a support cover using at most two row/column vertices,
or by the rank of its complete joint B coefficient matrix.

The old cross has rank at most eight and a nonzero target matrix has rank
at least eleven. These rank-at-most-two projected slices therefore vanish
on V. Their mixed-column equations reduce10 parameters to2. Four further
sources (indices36,37,39,40) obey the same rank bound after these equations;
their mixed-column equations reduce2 parameters to0. All four graph cases
follow the same dimension sequence, with exact rational row reductions.

Only the four common-plane normals remain. The shifted-order argument of
the third-boundary and pure-row proofs applies to these actual first
spaces: at every first remaining normal error, the double-new-output
coefficient is the corrected J used above. Absorb its plane direction and
repeat. The output maps stay in moving boundary modules of rank56, below
the two110-dimensional target legs. Arbitrary later coefficients and
unequal positive first-growth orders do not change this conclusion.

## A finite chart cover for the next question

There is a useful elementary reduction for general graphs. If V has
dimension5 and nonzero mixed projection in H=C^6 plus span(m), then
W=V intersect H has dimension4. The quotient H/W has dimension2 and is
spanned by the images of the six coordinate vectors. Some pair of these
images is a basis. For the corresponding coordinate two-plane S,
H=W direct-sum S. Subtracting an element of W from any m+h in V gives
a unique representative m+h' with h' in S.

There are fifteen choices of S. Thus a proof for arbitrary graph
coefficients on those fifteen charts, with the associated transversality
condition, would cover all mixed five-spaces. The four fixed graphs above
do not prove those parameterized statements. The chart cover is standard
linear algebra, without a novelty claim. The partner parameter and
exceptional chart strata remain part of the open problem.

The discovery phase tried a single fixed normal minor for six graph
variables. Its normalized perturbation has nonzero trace, so that
particular nilpotent-inverse certificate fails. Numerical axis controls
also exhibit normal-dimension jumps at special partner/graph values.
Neither generic kernel dimensions nor those controls justify discarding
exceptional strata. No global first-rank frontier or exponent is changed.
