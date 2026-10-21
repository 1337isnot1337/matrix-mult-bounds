# Saturation at the Hankel dimension boundary

October21,2026. AI-assisted written proof, unreviewed. This is an extension
of the concurrent strict projection-saturation lemma in one target family.
No independent review, historical priority, tensor construction, or exponent
gain is claimed.

Work over an algebraically closed field of characteristic zero. Let X_r
be the cone of length m=a+b-1 moment sequences whose a-by-b Hankel rank
is at most r, with1<=r<min(a,b). If a linear map

    Phi:Mat_(u,v) -> F^m

sends every rank-at-most-k matrix into X_r, where k>=1, then

    2r<=k(k+2)  ==>  im Phi is contained in X_r.             (1)

The concurrent `saturation.md` proves the strict case2r<k(k+2). The new
point is equality. Once(1) holds, the uniform Wronskian cap bounds the
whole linear image by r.

## 1. The minimum-rank argument imported from the strict lemma

Suppose some image is outside X_r. Choose a polynomial f vanishing on X_r
but not on the whole image, and choose a matrix of smallest rank s where
f composed with Phi is nonzero. Then s>=k+1. Restrict to its full s-by-s
row and column matrix space. The polynomial there is nonzero but vanishes
on all singular matrices, hence has the generic determinant as a factor.

The same argument in the concurrent lemma proves that Phi on this matrix
space is injective. Briefly, any nonzero kernel direction would make the
polynomial translation-invariant. Differentiating its maximal determinant
factor in that direction would force the determinant to divide a polynomial
of smaller degree, so all determinant cofactors would give a zero direction.
Their independence contradicts that direction being nonzero. Characteristic
zero is used in differentiating the determinant multiplicity.

Thus an injective linear image of the rank-at-most-k variety in Mat_s,
of dimension k(2s-k), is contained in X_r. The scalar annihilator description
gives dim X_r<=2r. At equality2r=k(k+2), it follows that s=k+1.

## 2. Nondegeneracy handles the larger ambient dimensions

The cone X_r is irreducible and spans F^m. Here is the needed classical
scalar-Hankel justification. Degree-r binary forms up to scale parametrize
the length-r schemes on P1. For each form q, the annihilator of q*S_(m-1-r)
is an r-dimensional vector space. These kernels form a vector bundle over
P^r; its incidence image is exactly X_r by the elementary scalar Hankel
annihilator theorem. That image is closed under the proper projective
parameter projection and is irreducible. The cone contains every coherent
evaluation sequence, which span F^m by Vandermonde interpolation.

Since r<min(a,b), m>=2r+1=(k+1)^2. If m>(k+1)^2, the injective image of
Mat_(k+1) is a proper linear subspace. Its contained rank-k variety has
dimension k(k+2)=2r, so its closure would be all of X_r. This would put the
nondegenerate X_r in that proper subspace, a contradiction.

## 3. Hypersurface degrees handle the last ambient dimension

It remains that m=(k+1)^2=2r+1. The strict inequalities a,b>r then force
a=b=r+1. The cone X_r is the zero set of the determinant of the generic
(r+1)-by-(r+1) scalar Hankel matrix. This determinant is an irreducible
polynomial of degree r+1. Indeed its zero set is irreducible by Section2,
and it is not a higher power: at h_(r-1)=1 with all other moments zero,
its derivative with respect to h_(2r) is the nonzero determinant of the
leading r-by-r anti-identity matrix.

Phi restricted to Mat_(k+1) is now a linear isomorphism onto F^m. Its
singular determinant hypersurface is mapped onto X_r, since both are
irreducible of dimension m-1 and one contains the other. Linear isomorphisms
preserve the degree of an irreducible hypersurface. The former degree is
k+1, whereas the latter is r+1. Equality2r=k(k+2) requires k even and at
least two, and r>k, so these degrees differ. This final contradiction proves(1).

Thus the strict scalar-Hankel saturation test can be extended to equality.
The first new cases are(k,r)=(2,4),(4,12),(6,24). The proof does not assert
this extension for arbitrary closed target varieties: the identity map on
Mat_(k+1), with its determinant hypersurface as target, remains the exact
counterexample at the general dimension boundary.

The finite controls compare both hypersurface degrees and test the strict
hypotheses. The all-size result rests on the proof above and the explicitly
credited minimum-rank lemma, not on a finite screen. Arbitrary singular
source-to-target maps remain outside the ordinary lifting application.
