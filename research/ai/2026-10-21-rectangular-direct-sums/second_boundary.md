# Hankel Segre images at the second boundary

October 21, 2026. AI-derived written proof, unreviewed. No independent review,
formalization, historical novelty or exponent improvement is claimed.
This extends the first-boundary argument in the maintained anisotropic package.

Work over an algebraically closed field of characteristic zero. Let
r<min(a,b), m=a+b-1=3r-2, and X_r be the cone of coefficient sequences with
Hankel rank at most r. Necessarily r>=3. Minimal schemes and their spans
S_Z have the meaning and the elementary apolarity proof given in
[the symbol-dimension note](../2026-10-20-anisotropic-constructions/hankel_symbol_dimension.md).
For finite schemes on P1, the span of a union has dimension min(m, length).
When its length is at most m, intersections of spans are the spans of scheme
intersections, by Hermite interpolation.

**Theorem.** If a linear map Phi: U tensor V -> F^m sends rank-one inputs
into X_r, then dim(im Phi)<=max(r,4).

## 1. Distinct schemes on a moving line intersect in at most one point

Let rank-r endpoints h_0,h_1 span a line in X_r, with distinct minimal schemes
Z_0,Z_1. If their intersection has length at least two, their union Y has
length at most 2r-2. A generic line member uses every highest jet on Y,
but also has a minimal scheme Z_t of length at most r. The union Y union Z_t
has length at most 3r-2=m. Independence of those jets forces the line member
into S_(Y intersection Z_t), contrary to its full support on Y. Thus the
intersection length is at most one. This argument allows repeated points.

## 2. A moving linear space has reduced generic scheme

Let L be a linear subspace contained in X_r, with generic Hankel rank r.
On its generic minimal-scheme stratum write Z=sum e_i z_i, with rho distinct
points and sum e_i=r. Choose an affine chart avoiding those points. After a
local algebraic root cover, a generic h is a sum of derivative evaluation
functionals of orders 0 through e_i-1 at each z_i, with nonzero top coefficients.
The multiplicities are constant on this generic stratum.

For a direction v in L, differentiate the straight line h+t v twice. Modulo
S_(Z+Z_red), whose jets extend through order e_i, the second derivative is

    sum_i c_(i,e_i-1) (dot z_i(v))^2 ev_(z_i)^(e_i+1) = 0.

If rho<r, all these jets together with S_(Z+Z_red) form a scheme of length
r+2rho<=3r-2=m. They are independent. Every root derivative therefore vanishes
in every direction. In characteristic zero the scheme map is then constant
on the irreducible generic locus. Consequently a genuinely moving L must
have rho=r: its generic scheme is reduced. This supplies the reducedness
step without assuming a pencil formula for its annihilators.

## 3. The scheme map of a moving space has dimension at most one

At a generic reduced point write h=sum c_i ev_(z_i), with r distinct z_i
and all c_i nonzero. As in the first-boundary proof, straight-line second
derivatives give

    sum_i c_i (dot z_i)^2 ev''_(z_i) = 0 modulo S_(2Z).

The relation space among the r second-derivative classes has dimension two:
the span of 3Z has dimension m=3r-2, while S_(2Z) has dimension 2r.
More precisely its vectors are

    (kappa_i P(z_i))_i,  deg P<=1,
    kappa_i = 1 / (2 product_(j!=i) (z_i-z_j)^3).

To check this formula, set Q(z)=product(z-z_i)^3. For any polynomial f of
degree at most 3r-3 and any P of degree at most one, the sum of finite
residues of fP/Q is zero. The coefficient of f''(z_i) in that residue is
kappa_i P(z_i); the other terms use f and f' and vanish in the quotient.
The two displayed vectors are independent and hence give every relation.

It follows that there are quadratic forms A(v),B(v) such that

    c_i (dot z_i(v))^2 = kappa_i (A(v)+z_i B(v)).

At each of the r>=3 distinct values z_i, the symmetric matrix of A+z_i B
has rank at most one. Every two-by-two minor is a polynomial of degree at
most two in z and has at least three roots. It vanishes identically.
The pencil spanned by A,B consists entirely of rank-at-most-one symmetric
matrices. Such a pencil has dimension at most one: two independent square
linear forms would have a rank-two sum. Thus all dot z_i are proportional
linear forms (or zero), and the scheme differential has rank at most one.
In characteristic zero its image has dimension at most one.

## 4. A moving linear space has vector dimension at most two

Suppose the scheme varies, so its image is a curve. Two generic schemes in
an irreducible family of reduced finite divisors intersect precisely in the
fixed base divisor B. One direct justification is incidence dimension: for
a nonfixed point z, containing z imposes a proper closed condition on each
of two independent parameters; their shared-point incidence has dimension
strictly smaller than the product parameter space. Fixed points account for
the only generic intersections. Section 1 gives length(B)<=1.

If B were nonempty, choose two generic h_0,h_1 and a generic point on their
line. All three minimal schemes contain B, so their union has length at most
3r-2=m. Independence of jets again contradicts the fact that the line member
uses every highest jet in Z_0 union Z_1, a scheme of length greater than r.
Therefore B is empty and two generic scheme spans are disjoint.

Put ell=dim L. A generic scheme fiber in P(L) is the open rank-r part of
P(L intersection S_Z). Since the image is one-dimensional,
dim(L intersection S_Z)=ell-1. Two disjoint such subspaces fit in L, yielding
2(ell-1)<=ell and hence ell<=2.

If the generic rank in L is s<r, then 3s<=m and the earlier fixed-scheme
argument applies. We have therefore proved: every bounded-rank linear space
of vector dimension at least three has one fixed scheme of length at most r.

## 5. The two Segre rulings

Let p,q be the generic dimensions of Phi(u,V) and Phi(U,v). If the generic
Hankel rank of Phi(u,v) is less than r, the earlier fixed-scheme theorem
already gives the desired bound. Otherwise it is r.

If p>=3, each generic ruling lies in a fixed scheme span S_(Z_u). If that
scheme varied with u, choose generic u_0,u_1 and u_0+u_1. Their three schemes
are distinct: equality of a sum scheme with an endpoint would force the other
rank-r endpoint into an intersection of length at most one. Pairwise
intersection lengths h_ij are at most one by Section 1. The third ruling
lies in (S_0+S_1) intersection S_2. Its dimension is at most two. Indeed,
if the union has length at least m, that dimension is
3r-h_01-m=2-h_01<=2. If its length is below m, it is
h_02+h_12-h_012<=2. Either case contradicts p>=3.
Thus the ruling scheme is constant and dim(im Phi)<=r. The same holds if
q>=3. In the remaining case p,q<=2, the elementary bilinear span bound
from the first-boundary note gives dim(im Phi)<=pq<=4.

This proves the theorem. No claim for m<3r-2 follows from this proof.

## 6. Ordinary tensor consequence

With the same lifted-rank and coefficient injection used in the existing
Hankel tests, a rectangular block with leg dimensions (mn,np,pm), total
target dimensions D_i and source dimension N=abm obeys

    mn > max(r,4)ab  ==>  p+2N-D_Y-D_Z >= (r+1)ab,

and its cyclic variants, when a+b-1=3r-2. This is an ordinary-map condition.
For A(7,10), r=6 and ab=70; it excludes the entire first surviving
N=1120 two-block frontier after the earlier tests. The completed finite
refinement is recorded separately. No actual improved-exponent maps result.

## Verification

The companion tests verify the two residue relations over the rationals,
the full jet ranks, the nonreduced-jet independence for every partition of
r through eight, and the sharp three-point requirement in the symmetric
pencil step. These controls support but do not independently review the
algebraic arguments above. No external result from the literature search is
used without proof; the existing apolarity and Hermite arguments retain their
attributions.
