# Exact quadratic biform ranks from two kernel indices

October 23, 2026. Owner-directed Codex mathematics. Written and unreviewed;
no independent mathematical review, formalization, historical-priority
claim, tensor degeneration, or smaller exponent is asserted.

This package specializes the existing biform kernel-bundle rank identity
to a recurrence with two free polynomial coordinates, and makes its two
indices computable by a bounded exact coefficient-matrix test. The bundle
identity is credited prior work, not a new general biform theorem. The
previous affine, constant-endpoint quadratic, and one-polynomial-top
formulas retain their credit. PR216's identical-resultant examples show
why the new indices contain information not captured by those coarse
invariants. Source versions and this distinction are in [sources.json](sources.json).

## 1. Literal matrix and statement

Let K be any field, a>=2, b>=3, and m=a+b-1. Let u,v,w in K[x]
not all be zero, with each nonzero polynomial of degree less than a.
Set f(x,z)=u(x)+z v(x)+z^2 w(x). Use the maintained crossed matrix

    R_(a,b)(f)[(j,L),(H,r)] = [x^(H-j) z^(L-r)] f,

with 0<=j<b, 0<=r<a, and 0<=L,H<m. Unavailable coefficients are
zero. This is exactly the biform block in the pinned
[slice-rank note](../2026-10-20-anisotropic-constructions/slice_rank_gap.md),
with bm rows and am columns.

Let g be the monic gcd of the nonzero members of u,v,w, and write

    u=g u0,  v=g v0,  w=g w0,
    D=max(deg u0,deg v0,deg w0),

using deg 0=-infinity. Thus gcd(u0,v0,w0)=1 and 0<=D<a.
For each integer ell>=0, form the coefficient matrix C_ell with
rows (r,k), 0<=r<a and 0<=k<=ell+D, and columns (L,j),
0<=L<a+2 and 0<=j<=ell. Its entry is

    C_ell[(r,k),(L,j)] = [x^(k-j)] c_(L-r)(x),             (1)

where c_0=u0, c_1=v0, c_2=w0, and c_s=0 outside s=0,1,2.
Negative polynomial indices also give zero.

**Theorem.** There are unique integers 0<=mu1<=mu2 such that the
polynomial kernel of

    u0 lambda_r+v0 lambda_(r+1)+w0 lambda_(r+2)=0,
                         r=0,...,a-1,                     (2)

has a basis of vector degrees mu1,mu2 with independent leading
coefficient vectors. They satisfy

    mu1+mu2=aD,                                            (3)
    nullity C_ell=(ell+1-mu1)_+ +(ell+1-mu2)_+,             (4)

where q_+=max(q,0). In particular,

    delta=min {ell: nullity C_ell>0},
    0<=delta<=floor(aD/2),
    (mu1,mu2)=(delta,aD-delta).                             (5)

The original full crossed matrix has exact rank

    rank_K R_(a,b)(f)
      =(a+2)b-(b-mu1)_+-(b-mu2)_+
      =ab+min(b,mu1)+min(b,mu2).                            (6)

The conclusion allows zero endpoints, v=0, arbitrary common factors,
and every characteristic. When D=0, both indices are zero and rank is
ab. The zero biform is excluded from the theorem and has rank zero.
The test in (5) is independent of b; it determines (6) simultaneously
for every admissible source width b>=3.

## 2. The complete left-kernel recurrence

Only row groups L=0,...,a+1 can be nonzero, because f has z-degree
at most two. All these groups occur in the literal matrix: b>=3
implies a+1<=m-1. Some can themselves vanish when coefficients are
zero; retaining them is harmless. The remaining row groups are zero.

Encode a dependence among these (a+2)b retained rows by

    lambda_L(x)=sum_(j=0)^(b-1) lambda_(j,L) x^j.

Its product with the column (H,r) is the coefficient of x^H in

    u lambda_r+v lambda_(r+1)+w lambda_(r+2).               (7)

The degree of each product is at most (a-1)+(b-1)=m-1.
Every coefficient H=0,...,m-1 is present among the original columns.
Consequently a row dependence is in the left kernel if and only if
(7) is identically zero for every r. No leading coefficient or output
endpoint is discarded.

Dividing (7) by the common nonzero g is valid in the domain K[x].
It leaves exactly (2), with the same bounds deg lambda_L<b.
This argument removes a common factor from the equations; it does
not replace the original source by a truncated coefficient map.
Rank-nullity on the retained rows therefore gives (6) once their
bounded-degree kernel dimension is known.

## 3. A rank-two bundle and the sum of the indices

Homogenize u0,v0,w0 to the common degree D in variables X,Y:

    U(X,Y)=X^D u0(Y/X),   V(X,Y)=X^D v0(Y/X),
    W(X,Y)=X^D w0(Y/X).

These forms have no common zero on P1, even after field extension.
On X!=0 this follows from gcd(u0,v0,w0)=1, equivalently a polynomial
Bezout identity. At X=0 at least one leading coefficient of degree D
is nonzero. This verifies the point at infinity, including cases
where some of the three polynomial degrees are smaller than D.

Use U,V,W in the shifted a-by-(a+2) recurrence matrix to define

    O^(a+2) -> O(D)^a.

At each geometric point its rows are the coefficient vectors of

    z^r (U+Vz+Wz^2),       r=0,...,a-1.

They are linearly independent: multiplication by a nonzero polynomial
in z is injective. Thus the bundle map is surjective at every point,
and its kernel E fits into an exact sequence

    0 -> E -> O^(a+2) -> O(D)^a -> 0.                      (8)

It has rank two and degree -aD. The arbitrary-field splitting theorem
for vector bundles on P1 gives

    E=O(-mu1) direct sum O(-mu2),    mu1<=mu2.              (9)

Both mu_i are nonnegative, since E is a subbundle of a trivial bundle:
a positive-degree line bundle has no nonzero map to O. Taking degrees
in (8)-(9) proves (3). This is the specialization to z-degree two
of the existing biform bundle calculation. No matrix-polynomial index
sum theorem is needed in addition to the cited splitting theorem.

Restrict (9) to the affine chart X!=0. It supplies a K[x]-basis of
all polynomial solutions of (2). Each basis column is the
dehomogenization of a vector of homogeneous degree mu_i, so its vector
degree is at most mu_i. The two images in the fiber X=0 are independent,
because (8) is a subbundle inclusion. They are precisely the leading
coefficient vectors of these columns. Thus the degrees are exactly
mu_i and their leading vectors are independent. For arbitrary polynomial
multipliers h1,h2, this also proves the predictable-degree identity

    deg(h1 lambda^(1)+h2 lambda^(2))
       =max(deg h1+mu1,deg h2+mu2),                        (10)

with the usual convention for zero terms. In particular these degrees
are the two minimal polynomial-kernel indices. Their unordered values
are unique, either by uniqueness of splitting or by the nullity
function below.

## 4. Bounded-degree kernels and a finite certificate

Twist (8) by O(ell). Global sections of E(ell) identify with
polynomial solutions of (2) of vector degree at most ell. Indeed,
homogenizing those polynomials to degree ell turns (2) into the
homogeneous bundle equation, and dehomogenizing reverses that step.
The map on global sections is precisely C_ell in (1), because all
output coefficients from zero through ell+D are retained.

The elementary count h0(O(n))=(n+1)_+ applied to (9) proves (4).
Taking ell=b-1 in Section 2 proves the literal source-rank formula
(6). It follows immediately that the first nonzero nullity occurs
at ell=mu1. By (3), mu1<=floor(aD/2), proving (5).

There is also an elementary existence check at the last search degree:
C_ell has a(ell+D+1) rows and (a+2)(ell+1) columns, whose difference is

    2(ell+1)-aD>0  when ell=floor(aD/2).

Thus the search cannot reach that bound without finding a kernel.
For D=0 it starts and ends at ell=0, where C_0 has rank a and
nullity two, yielding mu1=mu2=0.

An exact certificate can record only the first degree delta, a nonzero
kernel vector for C_delta, and full column rank for C_(delta-1) when
delta>0. A kernel at any earlier degree would persist by viewing its
polynomial vector at degree delta-1, so this adjacent check rules out
all earlier degrees. The theorem then fixes mu2=aD-delta and every
later nullity. Replaying the complete nullity function and the original
matrix for selected widths provides additional finite controls; those
controls are not the proof of the all-size statement.

## 5. The first stratum: a fixed linear factor

There is a useful intrinsic description of delta=0. Assume D>0.
Then

    mu1=0  if and only if  u0(x)s^2+v0(x)st+w0(x)t^2=0     (11)

as a polynomial identity for some [s:t] in P1(K). Equivalently the
primitive homogeneous z-quadratic
 u0 Z0^2+v0 Z0 Z1+w0 Z1^2 has a fixed K-linear factor. Both homogeneous
endpoints are included, so u0=0 or w0=0 supplies such a factor.

To prove this, let T be the span in K^3 of the coefficient triples
of u0,v0,w0. It has dimension at least two: dimension one would
make the three polynomials scalar multiples of one polynomial,
and primitivity would then give D=0. A nonzero constant recurrence
solution lambda has every row

    (lambda_r,lambda_(r+1),lambda_(r+2)),  0<=r<a,

in T's orthogonal complement. At least one row is nonzero, since
these intervals cover all coordinates. Therefore dim T=2 and this
a-by-three Hankel matrix has rank one.

For clarity, the required rank-one classification is elementary.
If lambda_0 is zero and the first nonzero coordinate has index j<a+1,
a consecutive two-by-two minor with upper-left index j-1 is
-lambda_j^2, a contradiction. Hence only the final coordinate is
nonzero. If lambda_0 is nonzero, rank one makes every row a multiple
of (lambda_0,lambda_1,lambda_2). Overlapping rows give successively
lambda_j=lambda_0 q^j, q=lambda_1/lambda_0, including q=0.
These are exactly the coherent sequences

    lambda_L=c s^(a+1-L)t^L.

Inserting one into (2) yields (11); the cases s=0 and t=0 are read
at the last and first recurrence equation, respectively. Conversely,
(11) makes this displayed coherent sequence, with c=1, a nonzero
constant solution. This proves the criterion over K without
algebraic closure or a characteristic restriction.

When it applies, the other index is aD and (6) becomes

    rank R=ab+min(b,aD).

Consequently, when aD>b, the exact lower stratum is

    rank R=ab+b  if and only if  mu1=0,

and hence precisely the fixed-linear-factor locus of (11). If both
indices are positive, either one reaches b and the other contributes
positively, or both are below b and their sum is aD>b. In both cases
the rank is strictly larger than ab+b. The strict inequality aD>b
is essential: when aD<=b, formula (6) gives rank ab+aD for every
splitting, so rank does not distinguish the two indices.

For D=0 the indices are already zero regardless of whether the
constant homogeneous quadratic has a K-rational linear factor;
that case must not be included in equivalence (11).

## 6. Prior results, usefulness, and limits

The constant-outer-coefficient family has indices
floor(a/2)D and ceil(a/2)D by its previously proved predictable-degree
formula. The affine case has indices 0,aD when represented with a
zero quadratic coefficient. The one-polynomial-top formula of PR217
is another explicitly solved special family. Those classifications
are credited rather than re-imported as proof dependencies here.

PR216 treats a=b=3 and
 f=x^2+z(1+x^2)+z^2(1+t x+c x^2).
Over characteristic different from two, its two examples (c,t)=(2,0)
and (1,1) have identical coefficient degrees and pairwise resultants,
yet ranks fourteen and fifteen. In the present formula aD=6: those
ranks correspond to indices (2,4) and (3,3). Their stated source and
field scope retain PR216's attribution. A verifier may reconstruct
them directly from (1) and the literal source without importing any
implementation from that pull request.

The general bundle rank identity is already present in the pinned
slice-rank note. The new package's role is the complete quadratic
specialization, a finite first-kernel test recovering both indices,
its field and boundary audit, and the constant-index criterion.
It replaces inadequate degree/resultant data by an exact computable
invariant; it does not express that invariant using only the three
coefficient degrees. In particular, it supplies no new linear-space
cap, compatible three-leg target maps, singular degeneration, or
asymptotic exponent implication. Finite acceptance evidence and a
written proof do not constitute independent mathematical review.
