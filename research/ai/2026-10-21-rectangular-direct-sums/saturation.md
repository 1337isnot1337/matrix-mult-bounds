# Low-rank input saturation closes the first rectangular frontier

October 21, 2026. Owner-directed AI-derived proof and finite exact certificates.
Written and unreviewed; no independent review, formalization, or historical
priority claim. This is an ordinary-restriction obstruction, not an exponent
improvement. It supersedes the open-candidate interpretation of the first
checkpoint in this package.

## 1. A linear projection lemma

**Lemma.** Let F be algebraically closed of characteristic zero, let
Phi: Mat(u,v;F) -> W be linear, and let k be a nonnegative integer. If

    dim(im Phi) < (k+1)^2,

then Phi of the rank-at-most-k matrices is Zariski dense in im Phi.
When k>=min(u,v) the conclusion is immediate.

Here is a self-contained proof of the remaining case. Suppose a nonzero
polynomial on im Phi vanishes on all those images. Its pullback P is a nonzero
polynomial on Mat(u,v), depends on at most d=dim(im Phi) linear forms, and
vanishes on every matrix of rank at most k. Choose the least rank s of a
matrix A where P(A) is nonzero. Then s>=k+1. Choose s-dimensional column
and row spaces containing A, and restrict P to their full s-by-s matrix
space. The resulting polynomial Q is nonzero and vanishes on every singular
matrix. Thus the irreducible generic determinant Delta_s divides Q. This
standard determinant fact also follows by polynomial division in one entry
on the dense open set where its complementary cofactor is nonzero.

If d<s^2, the restricted list of linear forms has a nonzero kernel direction
B. Hence the directional derivative D_B Q is identically zero. Write
Q=Delta_s^e R with e>=1 and Delta_s not dividing R. Differentiation and
unique factorization give

    Delta_s divides e (D_B Delta_s) R,

so Delta_s divides D_B Delta_s. Characteristic zero ensures e is nonzero.
Its smaller degree forces D_B Delta_s=0. But the determinant has no nonzero
constant translation direction: its cofactors are linearly independent
polynomials. For example, evaluating at rank-(s-1) matrices whose adjugates
are individual matrix units tests each entry of B separately. Therefore
B=0, a contradiction. We obtain d>=s^2>=(k+1)^2, proving the lemma.

The strict inequality is sharp: the identity projection on Mat(k+1,k+1)
has image dimension (k+1)^2, and its rank-at-most-k locus is not dense.
No rank-preserver classification or genericity assumption on Phi is used.

## 1b. A stronger version using the dimension of the closed target

Let X be a closed algebraic subset of W. Suppose Phi sends every rank-at-most-k
matrix into X, where k>=1. If

    dim X < k(k+2),

then the entire linear image of Phi lies in X. There is no ambient-dimension
bound in this version.

Indeed, if some image lies outside X, choose a polynomial f vanishing on X
but not identically on the image, and repeat the minimum-rank argument above.
It produces an s-by-s matrix subspace, s>=k+1, on which Phi is INJECTIVE:
any kernel direction would make the restricted polynomial translation-invariant
and contradict its determinant factor. Its rank-at-most-k variety has dimension
k(2s-k), as seen on the chart with an invertible leading k-by-k block.
The injective linear image of this variety is contained in X, forcing

    dim X >= k(2s-k) >= k(k+2),

a contradiction. The strictness is necessary: the identity map on Mat(k+1)
with X its determinant hypersurface has dim X=k(k+2).

For Hankel rank at most r, with r<min(a,b), the existing scalar apolarity
argument gives dim X<=2r. A length-r scheme on P1 is specified by its degree-r
annihilator up to scale (r parameters), and its functional span has r vector
parameters. Lower ranks are included in the same bound. Thus it is sufficient
that 2r<k(k+2), often allowing a smaller input rank than the ambient bound.
For instance r=6 or r=7 needs only k=3 regardless of a+b-1. The separately
certified linear-space dimension cap is still required; this dimension argument
does not by itself assert that every bounded-Hankel-rank linear space has
vector dimension at most r in every format.

## 2. Two finite Hankel-space dimension certificates

For a+b-1=15 write H(h)=(h_(i+j)), an a-by-b Hankel matrix. The exact
certificates prove:

- Every linear space of 7-by-9 Hankel matrices of rank at most 6 has vector
  dimension at most 6.
- Every linear space of 8-by-8 Hankel matrices of rank at most 7 has vector
  dimension at most 7.

To reduce these statements to finite checks, act on coefficient vectors by
h_j -> t^j h_j. This multiplies H on the left and right by invertible diagonal
matrices for nonzero t, so preserves rank. A putative a-dimensional bounded-
rank space has a limit in the Grassmannian as t tends to zero. Explicitly,
normalize its finitely many Plucker monomials by their minimum power of t.
The limit remains in the Grassmannian and in the closed bounded-rank locus.
It is fixed by the diagonal action. Since the fifteen coefficient weights
are distinct, a fixed subspace is a coordinate subspace. Consequently it
would be spanned by a subset of a coordinate vectors among h_0,...,h_14.

There are binomial(15,7)=6435 such spaces for format (7,9), and
binomial(15,8)=6435 for format (8,8). For EVERY subset the certificate gives
an integer coefficient vector supported on that subset and an a-by-a minor
whose determinant is nonzero modulo 101. Its determinant is therefore a
nonzero integer, and the same coordinate subspace cannot have bounded rank
over any characteristic-zero extension field. This disproves the proposed
Grassmannian limit and proves both dimension bounds for arbitrary subspaces.

The compact witness file records, in lexicographic support order, a trial
count and minor-column bitmask. Coefficients are reconstructed by the stated
32-bit linear congruential generator with seed 271828. This is a deterministic
witness encoding, not a probabilistic acceptance criterion. The generator
uses modular elimination; the verifier independently computes each selected
minor by integer Bareiss elimination and checks its nonzero residue. All
12870 supports are covered; no unsuccessful case is discarded.

This finite argument does not assert an unproved all-size Hankel-space theorem.

## 3. Applying saturation to the cyclic convolution symbol

Let A(a,b) have common source dimension N=ab(a+b-1). A concise direct-sum
target has total leg dimensions D_X,D_Y,D_Z. For an individual rectangular
block M(m,n,p), its first dual space is Mat(m,n); a rank-at-most-3 parameter
has target matrix-slice rank at most 3p. An ordinary lift to the source has
matrix-slice rank at most

    3p + (N-D_Y) + (N-D_Z).                         (1)

The maintained [polynomial injection proof](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
gives rank(source slice)>=ab rank(Hankel symbol), over F=C(x,z). Thus if
(1)<(r+1)ab, the symbol of every rank-at-most-3 parameter has Hankel rank at
most r. Identities initially stated for complex parameters extend to F:
parameterize rank-at-most-3 matrices as UV, and all relevant minors are
polynomial identities in U,V,x,z. We may then pass to an algebraic closure.

The symbol map has target coefficient dimension a+b-1=15<16=(3+1)^2.
Section 1 therefore forces the ENTIRE symbol image, not just its rank-one
or rank-three image, into the same closed Hankel rank locus. For (a,b)=(7,9)
and r=6, or (a,b)=(8,8) and r=7, Section 2 bounds this full image by r.
Select r long-coordinate projections that are injective on it over F.
Each selected coordinate is a biform with ab complex coefficients. This
provides a complex-linear injection from the full block parameter space into
r copies of the ab-dimensional coefficient space, exactly as in the earlier
Hankel-symbol argument. We conclude the necessary condition

    mn > r ab  ==>  3p + 2N-D_Y-D_Z >= (r+1)ab.      (2)

The two cyclic counterparts also hold. The condition is not valid for arbitrary
singular degenerations: the ordinary lifted-rank inequality (1) is essential.

## 4. Explicit contradictions and completed refinement

For A(7,9) -> M(27,27,28) plus M(6,6,2), N=945, ab=63 and
(D_X,D_Y,D_Z)=(765,768,768). In the first leg,

    3*28+(945-768)+(945-768)=438 < 7*63=441,
    27*27=729 > 6*63=378.

Condition (2) excludes that ordinary restriction. The same exact test
excludes every one of the 19 first-checkpoint A(7,9) survivors.

For the earlier square target A(8,8) -> M27 plus M7, the total dimensions
are (778,778,778), and

    3*27+2*(960-778)=445 < 8*64=512,
    27^2=729 > 7*64=448.

Thus that previously surviving ordinary square target is excluded as well.
All 552 first-checkpoint two-block survivors at A(8,8) are excluded by (2).
The saved refinement records a block index, leg index, lifted-rank upper bound,
symbol threshold and injection contradiction for every excluded pair.

Combined with the first-checkpoint screen, **none of the 62 source formats
with 2<=a<=b and N<=960 has an ordinary two-positive-rectangular-block target
passing the stated finite 9/4 score gate.** The conclusion does not cover
three or more summands, arbitrary singular limits, or tensor powers.

The displayed 2.2495 and other conditional numbers in the earlier note have
not become algorithms. Their ordinary-map premises are now excluded in this
scope; singular target questions remain separate. A smaller exponent remains
unproved.

## 5. Reproduction and review limits

    python research/ai/2026-10-21-rectangular-direct-sums/saturation.py --directory results/rectangular-direct-sums-20261021
    python -m unittest discover -s tests -p test_rectangular_saturation.py -v

The general projection and Grassmannian arguments are written proofs. Their
small symbolic controls and the exhaustive finite Hankel witnesses are not
independent mathematical review. The projection lemma is presented as a local
derivation, with no historical novelty claim. The original convolution rank
injection and external exponent framework retain their existing attributions.
