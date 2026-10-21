# A varying quantum recoupling family

Written local derivation, unreviewed, October 20, 2026. No exponent
improvement or historical priority is claimed. Work first over Q(q).

## 1. Convention and the highest projection

Use [Arun Ram, Quantum SL2, updated September 25, 2012](https://soimeme.org/~arunram/Notes/QuantumSL2.html)
for the defining relations and the coproduct

    Delta(E)=E tensor K+1 tensor E,
    Delta(F)=F tensor 1+K^-1 tensor F,
    Delta(K)=K tensor K.

Write [n]=(q^n-q^-n)/(q-q^-1), interpreted as a Laurent polynomial.
On V_m with basis v_i, 0<=i<=m, set

    K v_i=q^(m-2i) v_i,
    E v_i=[m-i+1] v_(i-1),
    F v_i=[i+1] v_(i+1),

with absent basis vectors zero. The highest projection
V_m tensor V_n -> V_(m+n) has coefficients

    c(i,j)=q^(i(n-j)) [m choose i] [n choose j]
                           /[m+n choose i+j].                (1)

It sends v_i tensor w_j to c(i,j) u_(i+j). To check E, divide the
intertwiner equation by c(i,j). It reduces to

    q^-j [i]+q^i [j]=[i+j].

The F equation similarly reduces to

    q^(n-j) [m-i]+q^(-m+i) [n-j]=[m+n-i-j].

Both identities follow immediately from the definition of [n]. Endpoint
equations use zero coefficients outside the displayed ranges. Normalizing
c(0,0)=1 fixes (1).

Formula (1) factors into three local nonzero diagonal factors:

    A_i=q^(in+binom(i,2)) [m choose i],
    B_j=q^binom(j,2) [n choose j],
    C_s=q^-binom(s,2)/[m+n choose s].

Indeed ij=binom(i+j,2)-binom(i,2)-binom(j,2). Thus the tensor with
coefficients (1) is isomorphic over Q(q) to C(m+1,n+1). This is an exact
source identity, without a claim about what happens at a singular q.

## 2. A trilinear invariant version

The highest embedding V_h -> V_m tensor V_n, h=m+n, sends its s-th
divided-power basis vector to

    sum_(i+j=s) q^(j(i-m)) v_i tensor w_j.

The coproduct of F checks this formula by the same quantum-integer
identity. A self-duality V_h* -> V_h takes phi_s to d_s u_(h-s), where

    d_s=(-1)^s q^(s(h-s-1))/[h choose s].

For example, intertwining E requires
d_(s+1)=-q^(h-2s-2) [s+1] d_s/[h-s], which the formula satisfies.
Apply the highest embedding and this self-duality to the invariant
coevaluation tensor. The resulting coefficients, on i+j+k=h, are

    f(i,j)=(-1)^s q^(j(i-m)+s(h-s-1))/[h choose s], s=i+j.  (2)

They also have a local diagonal factorization:

    A'_i=q^-binom(i,2),
    B'_j=q^(-mj-binom(j,2)),
    G_s=(-1)^s q^(binom(s,2)+s(h-s-1))/[h choose s].

Consequently (2), with the third coordinate reversed, is isomorphic to
the same convolution source. The finite controls check the complete E
and F coefficient equations for (2), separately from the source identity.

## 3. A generic basis that can coalesce at a root

For 0<=k<=min(m,n), the highest vector of weight m+n-2k in V_m tensor V_n
has coefficients t_i on v_i tensor w_(k-i), with t_0=1 and

    t_(i+1)=-t_i [n-k+i+1]/[m-i] q^(-n+2k-2i-2).

Generate the remaining columns by Delta(F)^ell/[ell]!. At q=1 these
specialize to the ordinary highest vectors and their divided-power
descendants. The classical Clebsch--Gordan decomposition proves that the
columns form a basis there. Their determinant is therefore a nonzero
rational function of q, so they form a basis over Q(q) as well. The code
inverts each fixed-weight block exactly.

For a polynomial uniformizer Phi(q), let nu be its order. Dividing each
column by its minimum entry order makes all entries regular. The order
of the resulting determinant is

    nu(det B)-sum_columns min_rows nu(B_entry).

It is nonnegative. A positive value means that the normalized columns
coalesce at Phi=0. This is a basis statement, not a tensor construction.

## 4. Local maps on the cyclic convolution source

Set D=a-1, h=2D. Use three copies of (2), with their first and second
coordinates on edges (A,B), (B,C), (C,A), and the reversed third
coordinate at the remaining leg. Each grouped leg has the ordered form
V_D tensor V_D tensor V_h. Its generic source equivalence is the same
local diagonal map on each leg:

    diag(i,j,z)=A'_i B'_j G_(h-z).

First recouple V_D tensor V_D and then couple each V_(2D-2k) with V_h.
Let Q(q) be the inverse of that composed basis matrix. The local matrix

    M(q)=Q(q) diag(diag(i,j,z))

is invertible over Q(q). Applying M(q) on the three cyclic legs is
therefore a legitimate varying-basis source family. This construction
does not assume that arbitrary regrouping is a quantum intertwiner;
the source equivalence follows from the explicit local factorization.

Near a complex root zeta, every entry has a Laurent expansion in q-zeta.
If additional row weights and an overall tensor scalar make every
coefficient regular, the constant tensor is a genuine degeneration.
One must check every coefficient, including required zeros. Singular
basis determinants alone do not perform this step.

As a calibration, multiply each row of M(q) by the inverse of its minimum
entry order at Phi=q^2+1 and take its residue over Q(i). All three local
maps are now regular, so their constant contraction is an ordinary
restriction. Exact fixed-weight elimination gives ranks 8,32,64 at
a=2,3,4. In particular that normalization cannot produce a tensor with
a leg of dimension 110 at size four. This leaves coupled singular
normalizations and higher tensor-level cancellations untested.
