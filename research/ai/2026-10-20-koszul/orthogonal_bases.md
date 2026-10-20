# Orthogonal polynomial bases: an all-size obstruction and a finite permutation audit

October 20, 2026. AI-derived written arguments, unreviewed. No smaller exponent
is proved. The new source basis changes are examined explicitly; they are not
silently covered by the earlier fixed-coefficient obstruction.

## 1. Construction class

Let q_0=1,q_1,q_2,... be polynomials with deg(q_i)=i and nonzero leading
coefficient. Suppose a linear functional ell makes them orthogonal, with
ell(q_i q_j)=0 for i!=j and h_i=ell(q_i^2)!=0. Express polynomial
multiplication in these bases on the three factors. This is a basis change
of C(m,B), with factor dimensions (m,B,B+m-1).

Consider coordinate selection, permutations on Y/Z, nonzero rescaling, and
diagonal parameter weights. Target sectors are the canonical T_(m,k) from
`all_dimension_targets.md`. Initially retain shared coordinate X_i as degree
i; Section 4 also permits a common permutation of the shared coordinates.
Coordinate collisions and general subsequent linear combinations are outside
this construction class.

The intended C(2,m-1) sector forces the shared weights to have the form
w_i=beta+alpha*i: subtract the zero-weight equations in its two rows. For m=2
the two weights already have this form. Absorb beta into another factor.

## 2. Positive slope reduces to the earlier catalecticant obstruction

This part needs only degree grading, not orthogonality. Let Q have the
coefficients of q_i as its columns, so Q is upper triangular and Q^T is the
change on the tensor's input factor. For alpha>0, combine diagonal weighting
with the convolution's torus symmetry

\[
X_i\mapsto\epsilon^{-\alpha i}X_i,\quad
Y_j\mapsto\epsilon^{-\alpha j}Y_j,\quad
Z_l\mapsto\epsilon^{\alpha l}Z_l.
\]

The transformed shared matrix has entries

\[
\bigl(D_X Q_m^T D_X^{-1}\bigr)_{ij}
=[t^j]q_i(t)\,\epsilon^{\alpha(i-j)}.
\]

Its limit is the invertible diagonal matrix of leading coefficients. Its
inverse is regular at zero. After applying that inverse, there is a
degeneration with shared factor fixed, to a diagonally rescaled T_(m,k).
All changes on the other factors can be arbitrary Laurent-polynomial maps.

The catalecticant rank of a diagonally rescaled output block is at least the
rank used in `source_obstructions.md`: rows and columns still separate into
the disjoint groups r-a=c-s, and each previously nonzero group remains
nonzero. Each group has rank at least one. Consequently

\[
B\ge kN+k\lfloor(m-1)^2/4\rfloor-\lfloor(m-1)/2\rfloor,
\qquad N=m(m+1)/2. \tag{1}
\]

Thus a triangular polynomial-basis change does not escape the obstruction
when the shared weights increase with degree.

## 3. Nonpositive slope has a stronger spacing obstruction

Write c_(i,j)^l for the coefficient of q_l in q_i q_j. Orthogonality gives

\[
h_l c_{i,j}^l=\ell(q_iq_jq_l)=h_j c_{i,l}^j. \tag{2}
\]

In particular these two coefficients vanish together. For j<l and d=l-j,
the leading coefficient of q_d q_j shows c_(d,j)^l!=0, so its reverse in
(2) also is nonzero.

The X_0 term of each target sector has one Y/Z coordinate pair. Since q_0=1,
those source coordinates must have the same index; call it the sector's
center. All mk centers are distinct because sectors use disjoint Y and Z
coordinates. If two centers differ by d with 1<=d<m, the two reverse cross
terms of degree d both occur. Their weights sum to

\[
2(w_d-w_0)=2\alpha d.
\]

Both cross terms must have strictly positive weight. This is impossible for
alpha<=0. The centers therefore have spacing at least m, giving

\[
B\ge m(mk-1)+1. \tag{3}
\]

The smaller bound (1) holds in either case (the right side of (3) is no
smaller for m>=2,k>=1). Its overhead tends to 50 percent uniformly in k.
It cannot meet the less-than-2.04721048-percent construction criterion.
This is an all-size result for the stated degree-preserving identification,
not a theorem about arbitrary shared-factor transformations.

## 4. Shared-coordinate permutations and a Chebyshev audit

Now identify target X_i with source q_(pi(i)). Zero equations give
w_(pi(i))=beta+alpha*i. The preceding positive-slope triangular argument
does not apply to an arbitrary permutation pi, so it cannot be reused without
another argument.

First, pi^{-1}(0) must be an endpoint. If it were r with 1<=r<=m-2, the
C(2,m-1) block would have two X_r entries at distinct diagonal source
coordinates. The two crossed positions are intended to carry the distinct
shared coordinates X_(r-1) and X_(r+1). By (2), each of those source degrees
also occurs at the opposite crossed position. Killing both unwanted terms
would require each shared weight to be greater than the other. This is
impossible. Reversing all three coefficient orders in every target block
allows us to assume pi(0)=0. For alpha<=0, the spacing argument still works:
w_d-w_0=alpha*pi^{-1}(d)<=0 for every d>0.

For alpha>0, specialize to Chebyshev polynomials. The exact identity is

\[
q_iq_j=(q_{i+j}+q_{|i-j|})/2\quad(i,j>0),\qquad q_0q_j=q_j.
\]

It follows directly by substituting t=(z+z^{-1})/2 and
q_i(t)=(z^i+z^{-i})/2; these polynomial identities do not require a numerical
orthogonality calculation. A source coefficient at (i,j,l) is nonzero exactly
when one of i,j,l is the sum of the other two.

For a C(2,m-1) block, let its Y coordinates be c,d and its Z coordinates
z_0,...,z_(m-2). Since pi(0)=0, z_0=c. At column b the intended source degrees
are pi(b) and pi(b+1). Each must be the earliest in the ordering pi among
all source degrees occurring at its Y/Z position; otherwise an unwanted term
has smaller or equal weight and cannot disappear. These conditions give a
finite exact path enumeration:

- Start with pi(0)=0, z_0=c.
- At step b, z_b is one of c+pi(b), |c-pi(b)|.
- The next degree pi(b+1) is one of d+z_b, |d-z_b|, lies below m, and has not
  appeared earlier. Every alternative source degree must appear later.
- All Z coordinates must be distinct, and the final ordering must contain
  all degrees 0,...,m-1.

For a nonidentity ordering, it suffices to consider c<m. If c>=m, write
s=|d-c|=pi(1). The sum-index alternatives are too large. Avoiding a previous
degree forces z_b=c-bs when d=c+s and z_b=c+bs when d=c-s, and then
pi(b)=bs. Covering all m degrees forces s=1 and the identity ordering. The
induction uses bs<m<=c and excludes the other Z choice because it gives
the previously visited degree (b-1)s. Also |d-c|<m, so for c<m the search
has d<2m-1. All relevant coordinates fit inside 0,...,2m-2.

The integer-only enumerator completed every m from 4 through 38. For each
nonidentity ordering it found at most one possible center c. This has a useful
consequence at those fixed m: T_(m,k) includes both C(2,m-1) and its transpose
C(m-1,2). By symmetry of the Chebyshev support, their centers belong to the
same enumerated set, but disjoint sectors require distinct centers. Therefore
no nonidentity shared ordering works, for any k or any B>=kN, at these m.
Together with (1)-(3), the low-overhead route is excluded in this coordinate
class for 4<=m<=38. This finite permutation fact is not asserted for all m.

The discovery run at m=39 timed out after 5,600,000 recursion nodes; it is
not an exhaustion certificate. Center uniqueness beyond 38 remains an open
combinatorial question. The mathematical reduction to the finite path search
and the implementation still require independent review.

## 5. Exact positive controls and validation boundary

The m=2 and m=3 support witnesses were also normalized exactly. Their
coefficients are 1 or 1/2; solving the linear exponent equations gives
explicit powers of two on the factor coordinates, verified against every
surviving coefficient. These agree with the existence of the earlier small
controls and are not new exponent bounds.

`chebyshev_centers.py` is the maintained integer-only path enumeration.
Tests compare it with independent permutation/coordinate enumeration for
m=2,...,6, check 64 polynomial multiplication identities, and replay every
projected source coefficient in the small normalized witnesses. The maintained
run records completion through 38; `chebyshev_discovery_summary.jsonl` also
retains the discovery run's timeout label at 39. No floating LP outcome is
used in the obstruction above.

Concurrent commit `d2d505c` on `research/filtration-compatibility-20261020`
also reports a Chebyshev-basis search, using binary, random and cut-distance
weights and scoring recognized sectors. This overlaps the choice of basis,
but does not contain the all-size orthogonal-basis obstruction or the
permutation/center reduction above. Its reported search is attributed in
`docs/concurrent_research.md`; it was not replayed here.
