# Close the punctured boundary and the finite affine partner chart

Written proof, unreviewed, October 21, 2026. Claim
`AI-AFFINE-PARTNER-CHART-100`. No exponent improvement is claimed.

Use the canonical A4 leading flags and the compatible rank-one partners

    u=(ab,-a,-b,1),  v=(ab,b,a,1).

Let B have its full maximal seven-space and C any mixed five-space in
its compatible maximal seven-space. All six mixed graph coefficients
and the boundary four-space are arbitrary. This note closes a=1,b=0,
then every a nonzero,b=0 by the source torus. Together with claim099
for b nonzero and claim087 for a=b=0, it excludes M(10,10,11) throughout
this affine chart, under the adopted shifted moving-plane argument.
Later regular output coefficients, delayed unequal first orders, and a
Laurent first map remain allowed. Other leading flags, smaller first
spaces, and the two projective endpoints are outside this result.

## 1. Reconstruct the boundary fiber before taking kernels

Claim088 supplies a polynomial complete 228-by88 full-B normal kernel
with an identity free block and a constant nonzero rank140 minor. Its
virtual C correction error factors polynomially through the seven-column
obstruction Psi. These identities hold at a=1,b=0; the maintained verifier
reconstructs them and only then evaluates at this point. No rational
generic kernel is specialized across a pole or a possible rank drop.

Append the sixteen necessary adapted source slices from088 to Psi,
giving a matrix Z with312 rows and seven columns, linear in88 normal
coordinates. Both Z and the complete virtual third tensor annihilate the
independent four common-plane directions. A constant complement has84
coordinates. On this complement, take the complete rational coefficient
rowspace using all312 rows. Its dimension is56. In particular, a row
selection certified only on b=1 is not used to assert completeness here.

Every row of Z annihilates the actual C five-space V, so rank Z<=2.
For the six boundary columns write S=(E0,O0,E1,O1,E2,O2) and

    Q=(O0-E0,O1-E1,O2-E2).

Ten constant combinations W of the56 coefficient rows have zero Q
projection. Their complete stable-boundary coefficient kernel has
dimension54. At every normal value,

    rank S >= rank Q + rank W.

Indeed the rows of W lie in the kernel of the boundary projection, and
the image of the rowspace of S is Q. If W is nonzero then rank Q<=1;
if W is zero the normal lies in the54-dimensional stable family.
In the rank-one case, explicit triangular two-minors are nonzero rational
multiples of squares of linear forms. Their complete kernel reductions
are84->52->48. Thus the union of these two fixed linear families covers
every necessary normal. No graph parameter has been chosen or inverted.

## 2. Source implications independent of the actual five-space

Reuse the rational source replay of099, with a fresh tensor at this
fiber. The adapted first source change is
e_(2,q,z) -> e_(2,q,z)-e_(1,q,z); the second source change is the
identity. Its unitriangular matrix is checked and hence invertible.

Three implications preserve all necessary normals:

1. A constant combination of known annihilating rows supported only
   on the mixed C coordinate must vanish, since V has nonzero mixed
   projection. This works for every mixed graph.
2. Subtract known rows from any adapted source slice. If the residual
   has a B/C support cover of at most two vertices, or joint B
   coefficient rank at most two, its actual matrix rank is at most two
   on V. Adding the old four-row/four-column cross gives rank at most
   ten. The adopted saturated target slice space Mat10 tensor I11 has
   minimum nonzero rank eleven. Therefore the target component and
   its double projection vanish; add the source rows to Z.
3. All three-minors of Z vanish. An explicitly checked minor equal to
   a nonzero rational multiple of L^3 forces L=0 over C. More generally,
   if L^3 lies in the rational span of actual three-minors, it also
   forces L=0. Every minor position and span identity is recomputed.

Every new linear restriction is followed by a complete rational kernel,
with no numerical selection of a subspace. All source indices, support
covers, and joint ranks are checked from the original virtual tensor.

## 3. Both complete families close

The stable family first reduces

    54->38->18->16->14.

Its14 variables split into two source blocks of seven. In each block,
79 actual cubic minors in84 cubic monomials span the cubes of four
independent linear forms. Exact rational rowspace membership proves
these forms vanish. The complete kernel therefore has dimension6.
Two further source additions give6->4. Two more source additions and
the pure mixed-row implication give4->0.

The rank-one projection family first reduces

    48->40->36->30->18->12->10.

Each of its two five-variable blocks has31 actual cubic minors in35
cubic monomials spanning three linear cubes. Their complete kernel
reduces10->4. Four further source slices and actual cubic minors then
give4->0. The final selected source counts are16 and12 respectively.

The certificate contains both initial families, both blocks in each
family, every complete source reduction, and both terminal closures.
The verifier checks coverage explicitly. No non-plane coordinate remains,
and the four plane directions were independently checked to survive.

## 4. Torus, corner and adopted induction

Give e_(i,j,z) in each source leg weight i+j+z. Every one of the4096
source terms has total weight18, and each leading G row is homogeneous.
For nonzero lambda the diagonal actions are invertible, preserve the
leading flags, and multiply the source by the nonzero scalar lambda^18.
The first leg absorbs this scalar. Direct symbolic coefficient checks
on both maximal frames give the parameter action

    (a,b) -> (a/lambda,b/lambda).

All frame columns are multiplied only by nonzero powers of lambda, so
actual mixed five-spaces and arbitrary boundary graphs remain in the
same class. Choose lambda=a to carry any a nonzero,b=0 to(1,0).

At a=b=0, claim087 already proves the required full-seven versus arbitrary
mixed-five closure for u=v=e3. Its finite source verifier is replayed here;
the corner is not inferred by taking a limit. For b nonzero, adopt099's
written full-line theorem and its torus transport. Its substantially
longer verifier is separately registered; this package does not report
having rerun it as part of the boundary replay.

At each first normal error t^N D from a moving boundary, adopt the
earlier shifted order argument: the correction equations occur at
N+s_B and N+s_C, and the double projection of the terminal coefficient
at N+s_B+s_C is exactly the virtual tensor used above, restricted to V.
The preceding implications force D to a common-plane motion. Absorb it
into the moving plane and increase the order. Both regular output maps
remain in rank56 boundary modules over C((t)), so cannot acquire the
110-dimensional target output legs. An arbitrary Laurent first map
does not remove this output-rank obstruction.

This completes the stated affine-chart exclusion under the adopted
written source and order lemmas. Independent mathematical review remains
open. It supplies neither an improving target nor a smaller exponent.
