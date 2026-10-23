# A pairwise-resultant obstruction to classifying three-term biform ranks

October 23, 2026. Owner-directed AI-assisted mathematics. Written exact
certificate, without independent mathematical review or formalization.
This is a one-slice theorem. It proves no matrix tensor degeneration and no
improvement to the exponent 9/4.

## Literal matrix and recurrence

For any field K and integers a>=2, b>=3 put m=a+b-1. For nonzero
f(x,z)=u(x)+z*v(x)+z^2*w(x), with deg u,deg v,deg w<a, the original
cyclic-source coefficient matrix has rows (j,L), 0<=j<b, 0<=L<m,
columns (H,r), 0<=H<m, 0<=r<a, and entries

    R[(j,L),(H,r)] = [x^(H-j) z^(L-r)] f.

Only row groups L=0,...,a+1 can be nonzero. A row dependence consists of
polynomials lambda_L(x)=sum_(j=0)^(b-1) lambda_(j,L)*x^j and satisfies

    u*lambda_r + v*lambda_(r+1) + w*lambda_(r+2) = 0
    for r=0,...,a-1.                                          (1)

Indeed, the coefficient of x^H in the r-th equation is the corresponding
column pairing. The degrees are at most (a-1)+(b-1)=m-1, so checking
all H=0,...,m-1 is equivalent to the full polynomial identities.
Consequently, for b>=3,

    rank R = (a+2)*b - dim_K{(lambda_0,...,lambda_(a+1)):
                            deg lambda_L < b and (1) holds}.  (2)

This extends the affine-in-z recurrence in PR209; it does not assume
that that PR has merged.

## Exact determinant family

Set a=b=3 and

    u=x^2,       v=1+x^2,       w=1+t*x+c*x^2,

with t,c algebraically independent over Z. Under the stated row and
column order, R is a 15-by-15 matrix with entries in Z[t,c]. Its
exact determinant is

    det R = t*(2*c^3 - 2*c*t^2 + t^4).                    (3)

One derivation applies twelve integer-unit row/column pivots to R. A
row-major choice of the first remaining +1 or -1 entry, followed by
row clearing (and normalization of negative pivots), leaves sign -1
and the 3-by-3 block

    [ -(2*c+1)*t,       t,  c+t^2 ]
    [    -c-t^2,       c,      t ]
    [         -t,       t,      c ]

whose negative determinant is (3). This gives an exact polynomial
identity over Z and hence after specialization to every field.

For a deliberately independent acceptance route, verify.py builds
all 225 entries from the original coefficient rule and computes the
integer determinant by fraction-free Bareiss elimination. It checks
(3) at every (c,t) in {0,...,15}^2. Every matrix entry has degree at
most one in each variable and the determinant has degree at most 15 in
each variable. Polynomial interpolation over Q therefore proves the
identity from these 256 exact integer comparisons, without relying on
a computer-algebra simplifier or the 12-pivot derivation.

The three pairwise polynomial resultants are

    Res(u,v) = 1,       Res(u,w) = 1,
    Res(v,w) = (1-c)^2 + t^2.                            (4)

The first two use the repeated root x=0 of u. For the third, mod v we
have x^2=-1 and w=(1-c)+t*x; taking the norm gives (4).
These are identities in Z[c,t], with resultants in the indicated order.

## Same degrees and identical resultants, different ranks

Take two specific triples:

    A: (u,v,w) = (x^2, 1+x^2, 1+2*x^2),  (c,t)=(2,0);
    B: (u,v,w) = (x^2, 1+x^2, 1+x+x^2), (c,t)=(1,1).

Over every field of characteristic different from two, each of their
three coefficient polynomials has degree two, all three pairwise
resultants are exactly one, and the common gcd is one. In particular,
the primitive coefficient triple also has degree two in both examples.
Nevertheless,

    rank R_(3,3)(A) = 14;          rank R_(3,3)(B) = 15. (5)

For B, (3) specializes to det R=1, which is a full-rank certificate
over every field. For A, (3) gives det R=0. The polynomials

    lambda_0 =  3+5*x^2,
    lambda_1 =  1+x^2,
    lambda_2 = -1-3*x^2,
    lambda_3 =  1+x^2,
    lambda_4 = -1+x^2

satisfy all three equations (1) exactly over Z and constitute a
nonzero left-kernel vector after every field specialization. Deleting
zero-based row 3, indexed (j=0,L=1), and zero-based column 1, indexed
(H=1,r=0), leaves a 14-by-14 matrix of determinant -4. Therefore A
has rank at least 14 whenever characteristic is not two, proving (5).
In characteristic two, A has rank 12; its z^2 coefficient ceases to
have degree two, so it is not a same-degree counterexample there.

Thus individual degrees, primitive triple degree, and even the exact
values of all three pairwise resultants do not determine the rank of
a three-term cyclic-source biform slice. This refutes that particular
coarse-invariant classification, not all conceivable resultant-type
invariants. It does not prove a source-space dimension bound.

## Verification, provenance, and precise next question

From the repository root:

    python -I research/ai/2026-10-23-three-term-resultant-obstruction/verify.py
    python -m unittest discover -s tests -p 'test_three_term_resultant_obstruction.py' -v

The standard-library verifier checks 256 interpolation points, the
nonzero integer minor, the integral row relation, both determinant
specializations, and ranks in characteristics 2,3,5,7,11,101. The
all-field statement requires the algebraic proof above; these are
finite machine checks of its specified determinant and minors.

Source coefficients and the rank convention come from the maintained
research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md
(blob 04d28c6a05027a7756891f47d28327de850a7501). The long-affine
recurrence is credited to the superseded PR209 at
4247f42eeb305163d299f908144b5915d1c238c5. No external theorem
beyond elementary determinant and resultant identities is imported.

Next question: For a=3 and arbitrary b>=3, compute the two
polynomial-kernel minimal indices of the recurrence (1) directly from
u,v,w, and determine which higher-order subresultant or syzygy
invariants, in addition to pairwise resultants, distinguish the
splitting patterns. The observed rank difference concerns the
15-by-15 b=3 slice: both examples have full column rank for
b=4,...,9 by exact modular certificates (a nonzero minor modulo 101
implies a nonzero integer minor). No claim for every b is made, and
there is no evidence of an asymptotic tensor-rank advantage.
The full-source-to-target exponent implication remains unconstructed.
