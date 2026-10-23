# An elementary gap for arbitrary biform coefficient matrices

October 23, 2026. Owner-directed Codex work, written and unreviewed.
No independent mathematical review, formalization, historical priority or
matrix-multiplication exponent improvement is claimed.

## 1. Statements and relationship to the existing proof

Let K have characteristic zero, let 2 <= a <= b, and put m=a+b-1.
For a nonzero polynomial f(x,z) of degrees at most a-1 in x and b-1
in z, use the maintained crossed coefficient matrix

    R(f)_((j,L),(H,r)) = f_(H-j,L-r),                  (1)

where 0<=j<b, 0<=r<a and 0<=H,L<m. An unavailable coefficient is zero.
This is the literal biform block from the credited cyclic source note.

The existing block lemma in `slice_rank_gap.md`, Section 1, states

    rank R(f) = ab                    if f=u(x)v(z),
    rank R(f) >= ab+a                 otherwise.       (2)

That proof imports splitting of vector bundles on the projective line.
We prove the same assertion by affine coordinate changes, polynomial
factorization and integer minors. We also prove

    rank R((alpha*x+beta*z)^e) = a(b+e)                (3)

for every 1<=e<a and alpha*beta != 0. More generally, if an irreducible
factor depending on both variables occurs in f with multiplicity e, then

    rank R(f) >= ab+ae.                               (4)

Factorization and multiplicity in (4) are taken over an algebraic closure
of K. The extension does not change matrix rank: a minor with entries in
K is zero in the extension exactly when it was zero in K. Thus it suffices
to work over an algebraically closed characteristic-zero field below.

These are ordinary matrix ranks. Reproving the source lemma does not
extend an ordinary-restriction exclusion to singular degenerations.
The previous theorem, full-slice argument and applications retain their
original credit and status. Their original files are not edited.

## 2. Affine covariance with the crossed indices

Let T_n(c) be the coefficient matrix for p(x) -> p(x+c) on polynomials
of degree below n:

    T_n(c)_(i,k) = binom(k,i)*c^(k-i)   for i<=k,
                  0                    otherwise.

It is triangular with diagonal one and inverse T_n(-c). Polynomial
multiplication commutes with substitution. Applying this separately to
the x multiplication and the z multiplication in (1) gives the exact
identity, in its displayed row and column orders,

    R(f(x+c,z+d))
      = [T_b(-c)^T tensor T_m(d)] R(f)
                               [T_m(c)^T tensor T_a(-d)].       (5)

For example, the x coefficient multiplication matrix has row H and
column j. Substitution changes it by T_m(c) on the left and T_b(-c)
on the right. Crossing H and j in R gives the transposes in (5).
All four matrices are invertible. In particular affine translations
preserve the literal crossed rank; this is not an assumption about an
uncrossed flattening.

Scaling both variables gives

    R(f(tx,tz))_((j,L),(H,r))
       = t^(L-j) R(f)_((j,L),(H,r)) t^(H-r).           (6)

For t nonzero these are invertible diagonal row and column scalings.
If the lowest total degree of f is e, the entries of
R(t^(-e)f(tx,tz)) are polynomial in t. Every minor whose size exceeds
rank R(f) vanishes for all t nonzero, hence vanishes identically and
also at zero. Therefore

    rank R(lowest homogeneous part of f) <= rank R(f). (7)

Equations (5)-(7) justify the degeneration actually used below.

## 3. Exact rank of a power of a mixed linear form

First take g=(x+z)^e, with 1<=e<a. The only possibly nonzero columns
of R(g) have H<b+e. There are exactly a(b+e) such columns, proving
the upper bound in (3).

We construct a nonsingular square minor using all these columns.
Partition them by d=H-r, where -(a-1)<=d<=b+e-1. Put

    r0=max(0,-d),
    r1=min(a-1,b+e-1-d),
    c=r1-r0+1,
    j0=max(0,d-e).

In the d block select columns (H,r)=(d+r0+v,r0+v) and rows
(j,L)=(j0+u,j0+u+e-d), for 0<=u,v<c. Every index is available:
j0>=0 and j0+c-1<b, since b>=a; the displayed L ranges lie between
0 and a+e-1, which is below m. Columns from a different d have zero
entries in these rows. The selected block is

    B_(u,v) = binom(e,k+v-u),   k=d+r0-j0.             (8)

Here 0<=k<=e. Thus the union of these blocks is a square minor of
order a(b+e), up to row and column permutations.

We give the required elementary positivity argument for (8). On the
acyclic graph with vertices (time,height), a step changes time by one
and height by either zero or one. B_(u,v) counts the paths of length e
from height u to height k+v. Expand its determinant as a signed sum of
families of paths with permuted destinations. Cancel intersecting
families by taking the earliest time of an intersection, then the
lexicographically first pair of starting labels intersecting at that
time, and swapping their tails at the common vertex. Prefixes through
that time do not change, so this is an involution; the destination
permutation changes by a transposition, reversing the sign.

The uncancelled families have no common vertices. Their height order
cannot change, because two heights change by at most one at each step;
an order reversal would first require equality at an integer time.
Consequently every uncancelled permutation is the identity. At least
one such family exists: use the same fixed choice of k upward steps
in all paths, translated by their distinct starting heights. Thus

    det B is a positive integer.                      (9)

This is the classical nonintersecting-path determinant argument. Its
credit remains with Lindstrom and Gessel-Viennot; the needed special
case and cancellation proof are reproduced here, not imported as an
unproved structural premise. See Gessel-Viennot, *Binomial determinants,
paths, and hook length formulae*, Sections 1-2, printed pages 300-303,
DOI [10.1016/0001-8708(85)90121-5](https://doi.org/10.1016/0001-8708(85)90121-5).
The exact inspected primary PDF and hash are recorded in `sources.json`.

In characteristic zero (9) is nonzero. Hence the complete minor is
nonsingular, proving (3) for alpha=beta=1. In general, each entry is
multiplied by alpha^(H-j)*beta^(L-r). Independent nonzero diagonal
scalings on rows and columns therefore give (3) for all alpha,beta.
A nonzero scalar multiplying g also leaves rank unchanged.

Characteristic zero matters for (3). At a=b=3,e=2, the rank is 15
in characteristic zero but 14 in characteristic two. We make no
all-characteristic assertion for this power formula or this proof.

## 4. A mixed factor supplies the required local degeneration

Suppose an irreducible factor h depending on both variables has exact
multiplicity e in f, so f=h^e*g and h does not divide g. There is an
affine zero (c,d) of h at which h_x, h_z and g are all nonzero.
Here is an elementary justification of that existence, including the
points that can fail in positive characteristic.

Over the rational function field K(x), h is irreducible as a polynomial
in z. Indeed h is primitive as a z polynomial over K[x], and clearing
denominators from a putative factorization contradicts irreducibility
in K[x,z]. Both h_x and h_z are nonzero in characteristic zero. Neither
is divisible by h: their total degrees are strictly smaller. The same
holds for g by hypothesis. Localization does not change this: clearing
a rational-function denominator could only add a nonzero polynomial
in x, which the mixed irreducible h cannot divide. Hence h is coprime,
in K(x)[z], to
h_x*h_z*g. The Euclidean algorithm and clearing its denominators give

    A(x,z)*h + B(x,z)*h_x*h_z*g = D(x),               (10)

for polynomials A,B and a nonzero polynomial D in x. Choose c avoiding
the finitely many zeros of D and the leading z coefficient of h.
The polynomial h(c,z) has positive degree, hence has a root d in the
algebraically closed field. Equation (10) forces h_x(c,d), h_z(c,d)
and g(c,d) all to be nonzero. This proves the asserted existence.

After translating x by c and z by d, the lowest homogeneous part of f is

    g(c,d)*(h_x(c,d)*x+h_z(c,d)*z)^e.                 (11)

Both coefficients in that linear form are nonzero. Since deg_x h>=1,
e<=deg_x f<=a-1, so (3) applies. Equations (5), (7), (11) and (3)
give rank R(f)>=a(b+e), proving (4).

Every polynomial factors into irreducibles. If none of its irreducible
factors depends on both variables, it is a product u(x)v(z). Conversely
such a product has no mixed factor. Thus a nonseparable f always has
at least one mixed factor, and e>=1 in (4) proves the lower half of (2).

For f=u(x)v(z), the matrix is, up to permutations, the tensor product
of the two coefficient multiplication matrices. Multiplication by a
nonzero polynomial over a field is injective, so their ranks are b
and a. Their tensor product has rank ab. This proves the other half
of (2), and also shows that the gap is sharp: x+z attains ab+a.

## 5. Evidence and limits

The proof quantifies every size and every biform over characteristic
zero. The verifier instead checks an explicit finite control inventory:
power minors, their active-column upper bounds, literal affine covariance,
selected mixed-factor limits and a characteristic-two boundary. The
test module uses a separate symbolic backend for ranks and polynomial
substitutions. Those computations support the argument; they do not
certify the universal factorization/existence argument by enumeration.

This package supplies an alternative input for the existing block gap.
It leaves the original bundle proof and every downstream dependency
ledger unchanged. A later package may explicitly adopt this elementary
proof without silently rewriting the provenance of prior results.
No target degeneration, source-space dimension classification,
independent review, formalization or exponent improvement follows here.
