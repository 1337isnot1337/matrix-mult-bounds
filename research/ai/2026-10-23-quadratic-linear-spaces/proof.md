# Sharp dimension-six bounds for small biform slice spaces

October 23, 2026. Owner-directed Codex research, written and unreviewed.
Same-session checking is not independent mathematical review or
formalization. These are bounds on linear spaces of slices of one
crossed biform block, with no compatible tensor target or improved
matrix-multiplication exponent.

The only local mathematical prerequisites are the merged
[quadratic kernel-index formula](../2026-10-23-quadratic-kernel-indices/proof.md)
and its [structural dichotomy](../2026-10-23-quadratic-kernel-indices/dichotomy.md).
The binary upper bound has an explicit seven-matrix certificate. The
all-field geometric bound uses the factor loci of bidegree-(2,2) forms.
These two arguments have different field hypotheses, stated separately.

## 1. Literal source and the two conditions

For a field K let

    V_K={f(x,z): deg_x f<=2 and deg_z f<=2},  dim V_K=9.

Write f=u(x)+z v(x)+z^2 w(x). Use the full crossed source matrix

    R(f)[(j,L),(H,r)] = [x^(H-j) z^(L-r)] f,
      0<=j,r<3,       0<=L,H<5.                          (1)

Thus R(f) is 15 by 15, with the rows ordered first by j and then L,
and the columns first by H and then r. All coefficients outside the
given polynomial range are zero. This is the literal R_(3,3) source
from the pinned original biform note. No row, column, or endpoint is
discarded.

A K-linear subspace W of V_K has a **K-point rank cap r** if
rank_K R(f)<=r for every f in W. It has a **geometric rank cap r**
if that inequality holds for every f in W tensor_K Kbar, where Kbar
is an algebraic closure. Equivalently, all (r+1)-minors restrict to
zero polynomials in the coordinates of W. Geometric rank caps imply
K-point rank caps. Over an infinite field the converse holds, because
a polynomial vanishing on all K-points of an affine space is zero.
Over a finite field the converse can fail; Section 6 gives an explicit
failure for the source (1).

**Theorem A (binary points).** If W is an F2-linear subspace of V_F2
whose F2-point rank cap is 14, then dim W<=6. The same sharp bound
holds for an F2-point rank cap of 12.

**Theorem B (geometric rank twelve).** Over every field K, a subspace
W of V_K with geometric rank cap 12 has dim_K W<=6. The bound is
sharp over every field. In particular it also bounds K-point rank-12
families when K is infinite.

Theorem A also bounds F2-defined spaces with a geometric cap of 14,
since this is a stronger hypothesis. It does not assert a geometric
rank-14 bound for arbitrary fields. Theorem B does not classify all
geometric equality cases.

## 2. Seven full-rank binary slices

Encode the nine coefficients by a binary mask: bit 3j+i is the
coefficient of x^i z^j. Consider the span T of the masks 84,174,311,
corresponding to

    t1=x^2+xz+z^2,
    t2=x+x^2+(1+x^2)z+xz^2,
    t3=1+x+x^2+(x+x^2)z+x^2 z^2.                        (2)

Their seven nonzero binary sums are distinct, so T has dimension
three. The following table is a compact exact certificate. For each
mask, lift its nine bits to the integers 0,1 and form (1) over Z.

| Mask | Binary combination | det R for the 0,1 coefficient lift |
| --- | --- | --- |
| 84 | t1 | -1 |
| 174 | t2 | 7 |
| 250 | t1+t2 | 3 |
| 311 | t3 | 1 |
| 355 | t1+t3 | 43 |
| 409 | t2+t3 | 1 |
| 461 | t1+t2+t3 | 1 |

The additions in the middle column take place over F2; the integer
lift is taken after those additions. Each determinant is odd, so
every nonzero vector of T has rank 15 over F2. The maintained exact
verifier reconstructs all seven full integer matrices and recomputes
these determinants, as well as their binary ranks.

If dim W>=7, elementary subspace dimension gives

    dim(W intersection T)>=dim W+dim T-dim V_F2>=1.

Such an intersection contains a nonzero full-rank slice, contradicting
the rank-14 cap. Therefore dim W<=6. A rank-12 cap is stronger, so
the same upper bound applies. This proves the upper part of Theorem A
without an exhaustive subspace search or a polynomial-identity inference
from the binary points.

## 3. Rank twelve is a vertical or horizontal factor condition

We prove the geometric statement over an algebraically closed field k.
Homogenize f separately to a form F of bidegree (2,2) in
X0,X1 and Z0,Z1. Write

    F=U(X) Z0^2+V(X) Z0 Z1+W(X) Z1^2.

For this section only, W(X) denotes the third coefficient form, not
a linear family. A vertical linear factor is a nonzero homogeneous
linear polynomial in X dividing F; a horizontal one is such a
polynomial in Z. Both include the relevant point at infinity.

Remove the monic affine gcd g from u,v,w and denote the resulting
primitive maximum degree by D, so 0<=D<=2. The earlier kernel-index
proof gives mu1+mu2=3D and

    rank R(f)=9+min(3,mu1)+min(3,mu2).                   (3)

Its structural sequel gives the possible ranks 9,12,14,15. More
specifically, D=0 gives rank9, D=1 gives rank12, and D=2 gives
mu1 in {0,2,3}, with rank12,14,15 respectively. At positive primitive
degree, mu1=0 is equivalent to a fixed homogeneous k-rational z-root
of the primitive biform, hence to a horizontal linear factor. These
are precisely the merged prerequisites imported here.

The original coefficient forms U,V,W have homogeneous gcd of degree
2-D. To check the endpoint in this statement, put d=deg g and
homogenize the primitive triple to degree D. Its three homogeneous
members have no common zero, including at infinity: the affine Bezout
identity excludes finite common roots, and at least one leading
coefficient of degree D is nonzero. The common factor of the original
forms is therefore exactly

    homogenize(g) times X0^(2-d-D),

up to a nonzero scalar, of degree 2-D. The exponent is nonnegative
because the original coefficient degrees are at most two.

Since k is algebraically closed, this gcd has a linear factor exactly
when D<=1. Thus D<=1 is equivalent to a vertical linear factor of F.
When D=2, equation (3) and the fixed-root characterization show that
rank R(f)<=12 is equivalent to a horizontal linear factor. Conversely,
a horizontal factor remains after removing an x-only gcd, and gives
rank at most12 by the same formula (with the D=0 case already included).
We have proved the set-theoretic equality

    { [F] in P8 : rank R(f)<=12 } = V_X union V_Z,         (4)

where V_X and V_Z are the vertical- and horizontal-factor loci.
Equation (4) concerns the underlying reduced point locus, not equality
of determinantal ideals or scheme structures. Repeated factors and
characteristic two cause no exception to the argument.

## 4. The projective dimension bound

Multiplication gives a morphism

    P(k[X0,X1]_1) x P(k[X0,X1]_1 tensor k[Z0,Z1]_2)
      =P1 x P5 -> P8,             ([l],[G]) -> [lG].     (5)

The product of two nonzero polynomials is nonzero, so the coefficient
formula defines this morphism everywhere. Its image is exactly V_X.
The source is projective (for example by the Segre embedding), hence
proper, and the target is separated. Its image is closed by Stacks
[29.42.7](https://stacks.math.columbia.edu/tag/01W6), using
[29.44.5](https://stacks.math.columbia.edu/tag/01W7) for properness.

The source is irreducible: its standard affine open A1 x A5=A6 is
dense and irreducible. Its image is irreducible as well, since a
decomposition into two proper closed subsets would pull back to such
a decomposition of the source. Projective-space and product dimensions
give dim(P1 x P5)=6, and image dimension cannot increase. Thus

    dim V_X<=6,               dim V_Z<=6.                (6)

The dimension inputs are Stacks
[33.34.1](https://stacks.math.columbia.edu/tag/0B2P),
[33.20.5](https://stacks.math.columbia.edu/tag/0B2M), and
[33.20.4](https://stacks.math.columbia.edu/tag/0B2L).
No generic-fiber calculation or separability assumption is needed.

Both V_X and V_Z contain all nine coordinate monomials

    X0^(2-i) X1^i Z0^(2-j) Z1^j,    0<=i,j<=2,

because each monomial has a linear factor in each variable pair.
These nine points span P8. Hence neither factor locus can equal a
projective linear subspace of dimension at most six.

Suppose a geometric rank-12 family had vector dimension at least
seven. After extending scalars to k and selecting a seven-dimensional
subspace, its projectivization is a P6 contained in (4). This P6 is
irreducible, so it lies in V_X or V_Z. The selected factor locus is
closed irreducible, has dimension at most six, and contains a closed
irreducible P6. It must equal that P6: a proper inclusion would append
one more member to a chain of irreducible closed subsets and give
dimension at least seven. This contradicts the preceding spanning
observation. Therefore dim W<=6. Scalar extension preserves vector
dimension, completing the upper bound over the original field K.

## 5. Sharpness over every field

Fix a horizontal linear factor defined over K, for example Z1.
The forms

    F=Z1 G,         G of bidegree (2,1),

form a six-dimensional vector space, since G has six independent
monomial coefficients. Multiplication by Z1 is injective. Every
member has a horizontal factor, so its geometric rank is at most12
by Section 3 after extension to Kbar. Dehomogenization gives the
particularly simple basis

    z, xz, x^2 z, z^2, xz^2, x^2 z^2.                   (7)

This proves sharpness for Theorem B and for both binary caps in
Theorem A. Fixed vertical factors give another set of examples.

## 6. Separate finite classification and a scalar-extension failure

The complete binary census in the saved report is additional finite
evidence. It is not needed for either upper-bound proof. It computes
all 511 nonzero literal source ranks and enumerates all 788,035
six-dimensional subspaces of F2^9 through their unique three-dimensional
orthogonal complements in reduced row-echelon form. It finds:

- Exactly six dimension-six spaces with F2-point rank cap12. These
  are the three fixed rational vertical-factor spaces and the three
  fixed rational horizontal-factor spaces.
- Exactly twenty dimension-six spaces with F2-point rank cap14.
  Fourteen are the coefficient compression spaces U tensor F2^3 or
  F2^3 tensor U, with U one of the seven two-dimensional coefficient
  subspaces. There are six additional binary spaces.

These statements classify the finite binary dimension-six spaces only.
They do not classify geometric equality cases over arbitrary fields.
For the fourteen compression spaces the census checks the cap directly
on all binary vectors; no additional all-field compression theorem is
imported here.

One of the six extra spaces has the basis

    1, x^2, (1+x+x^2)z, z^2, xz^2, x^2 z^2.             (8)

Its 63 nonzero binary vectors have ranks9,12,14 with counts15,18,30,
respectively. This space does not have a geometric rank cap of14.
Let F4=F2[alpha]/(alpha^2+alpha+1). The vector in its scalar extension

    f=x^2+(1+x+x^2)z+(x+alpha x^2)z^2                   (9)

has determinant det R(f)=1 in F4. The verifier constructs the full
matrix (1) using exact four-element field arithmetic and checks this
determinant. Thus all binary vectors can satisfy a rank cap while an
extension-field vector of the same linear family violates it.

The complete census and (9) are reported as reproducible finite
calculations. The dimension bounds instead rest on the seven displayed
odd determinants, elementary linear algebra, the merged point-locus
criterion, and the projective argument above.

## 7. Relevance and limits

The new bounds concern a whole first-source subspace rather than one
slice: seven independent binary source directions force a rank15 slice,
and seven geometrically rank-at-most12 directions are impossible over
every field. To use either obstruction in a target construction one
must still prove that the proposed maps impose the corresponding rank
cap on this full source block. No such compatible three-leg maps are
constructed here.

The proof preserves the original source and kernel-index attribution;
primary geometry versions and exact local hashes are in
[sources.json](sources.json). Review status remains written and
unreviewed regardless of finite replay or CI.
