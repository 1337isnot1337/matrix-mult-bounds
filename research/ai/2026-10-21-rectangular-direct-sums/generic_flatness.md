# Generic finite realization from a low crossed rank

October 21, 2026. Written proof, unreviewed. No exponent improvement.

## Statement

For an A(8,10) coefficient tensor, let n be its crossed rank. If n<=9
and both outer coefficient flattenings have rank at least three, then a
generic change of the two homogeneous long coordinates makes the inner
7-by-9 block-Hankel matrix have rank n, equal to the full 8-by-10 matrix.
Consequently the changed sequence has an n-dimensional finite realization
by flat_realization.md. Thus failure of every such coordinate chart
forces at least one outer flattening to have rank at most two.

This is a statement about finite coefficient tensors, not just slices
already assumed to have small realizations. The distinction matters for
the counterexample in outer_compression.md.

## 1. The level module and its Hilbert function

Write S=C[X,Y], D=16, and regard the moments as a linear functional

    F: S_16 tensor B -> A,

with F(X^k Y^(16-k) tensor b)=M_k b. Replace A and B by their concise
outer coefficient spaces, of dimensions r and s respectively. Thus
r,s>=3. Define the homogeneous apolar submodule N of S tensor B by

    q in N_d iff F(t q)=0 for every t in S_(16-d),

and set M=(S tensor B)/N, with all degrees above16 zero. Its degree-d
Hilbert function h_d is the rank of the catalecticant with d+1 block
columns and17-d block rows. In particular h_0=s, h_16=r, and h_9=n.
The module is generated in degree zero. Its socle is exactly M_16: if
Xq and Yq vanish in a lower degree, every complementary monomial factors
through one of them, so q was already zero in M.

The Koszul complex for X,Y computes Tor_2^S(M,C) as the socle shifted
by two. A minimal graded free resolution therefore has the shape

    0 -> S(-18)^r -> direct_sum_j S(-delta_j) -> S^s -> M -> 0.

Here delta_j>=1. These are standard graded-resolution facts, not new
claims of this repository. For 0<=d<=17, Hilbert series give

    h_d=s(d+1)-sum_j max(0,d-delta_j+1).               (1)

Consequently the successive differences h_d-h_(d-1) are nonincreasing
through degree17. There are no polynomial relations among the chosen
minimal relation columns in total degree below18.

## 2. Low rank forces a long enough plateau

If h_9-h_8>=1, concavity forces h_9>=s+9>=12, contradicting n<=9.
If h_9-h_8<=-1, concavity forces h_16<=n-7<=2, contradicting r>=3.
Hence h_8=h_9=n. Likewise h_10-h_9 cannot be positive by concavity,
and cannot be negative because it would again give h_16<=n-7<=2.
Finally h_8-h_7 cannot be positive, since it would give h_8>=s+8>=11;
it cannot be negative since the next difference is zero. Therefore

    h_7=h_8=h_9=h_10=n.                              (2)

Equation(1) now says precisely s of the relation columns have degrees
at most10; all these degrees are at most7, and their sum is n. Indeed,
zero slope counts s columns, and the value on the plateau is the sum
of their degrees. Positivity and s>=3 also give max(delta_j)<=n-s+1<=7.
All other minimal relation columns have degree at least11.

## 3. The small relation matrix is nonsingular

Let P be the s-by-s homogeneous polynomial matrix consisting of these
s columns. Its determinant cannot vanish identically. Otherwise choose
a maximal independent subcollection of t<s columns and one more column.
A nonzero t-row minor gives a polynomial dependency by the usual signed
minor construction. The total degree of that dependency is the sum of
the degrees of the selected t+1 columns, at most n<=9. This contradicts
the absence of relation-column syzygies below degree18.

Thus det(P) is a nonzero homogeneous polynomial of degree n. Let
M'=S^s/im(P). It agrees with M through degree10, since the remaining
relation generators have degree at least11. Its Hilbert function is n
in every degree at least max(delta_j)-1, hence in degrees7 through10.

Choose a linear form L not dividing det(P). Multiplication by L on M'
is injective. An elementary verification: if Lv=Pw, multiplying by the
adjugate shows det(P)w=L adj(P)v. Coprimality forces every component
of w divisible by L; cancelling L then shows v in im(P). Equal Hilbert
dimensions make multiplication by L an isomorphism in the degrees in
question. In particular L^2:M_8 -> M_10 is an isomorphism.

## 4. Inner flatness in a generic chart

Complete L to homogeneous coordinates (X',Y'=L). The full crossed
matrix is the pairing between S_7 tensor A^* and S_9 tensor B. Its
rank n is invariant under this invertible coordinate change.

The inner7-by-9 matrix restricts both sides by one factor of L. It is
the pairing between S_6 tensor A^* and S_8 tensor B given by F(L^2 tq).
The degree10 catalecticant induces an injection from M_10 into the
space dual to S_6 tensor A^*. Since L^2:M_8 -> M_10 is an isomorphism,
this restricted pairing has rank n. This proves the statement without
assuming a finite realization at the start.

## Provenance and controls

Standard inputs: the Hilbert syzygy theorem in two variables, minimal
resolution Betti numbers computed by Tor, and the Koszul resolution.
See Melody Chan, *Course Notes for Math 2520 Graduate Algebra* (March15,
2023), section36, Theorem4.21 and the following Koszul/graded-Tor proof,
printed pages49-50:
https://www.math.brown.edu/mchan2/AlgebraNotesChan.pdf
The socle computation and all uses above are explicitly given here.

`generic_flatness.py` constructs a nine-state example with outer ranks
three and three. Moving one support point to infinity makes the supplied
chart nonflat; the exact homogeneous change restores flatness, and all
17 moments are reconstructed over Q. Its complete apolar Hilbert
function is checked. These controls do not constitute independent review
of the general argument. No new-priority claim is made for the underlying
realization or graded-module techniques.
