# A corner-minor rederivation of the existing polynomial rank bound

This is an alternative proof of the bound already proved in
`polynomial_rank_locus.md`. It is not a stronger theorem, a priority claim
or independent mathematical review. Work over C. The earlier proof uses
two full polynomial multiplication injections; the following argument
uses tensor covariance and one explicit nested triangular minor.

Let a,b>=2, m=a+b-1. Use the source slice coordinates from that note:

    M_F[(j,p,L),(H,q,r)]=F_(H-j,p+q,L-r),                (1)

with j,q<b; p,r<a; L,H<m, and coefficients outside the short ranges zero.
Set h_k=F_(a-1,k,b-1). Suppose the a-by-b Hankel matrix H_h has a nonzero
rho-by-rho minor on row indices P and column indices Q. Select source rows
and columns in the following order:

    rows:    (j,p,L=r'+b-1),   j<b, r'<a, p in P;
    columns: (H=j'+a-1,q,r),   j'<b, r<a, q in Q.         (2)

The selected entry is

    F_(a-1+j'-j,p+q,b-1+r'-r).                          (3)

If j'>j it vanishes. In each diagonal j block, it vanishes if r'>r.
Every diagonal (j,r) block is the same Hankel minor H_h[P,Q]. Hence the
selected ab*rho square matrix has determinant

    det(H_h[P,Q])^(ab).                                (4)

In particular rank M_F>=ab rank H_h. All index ranges in(2) lie within
those in(1). This is a nested triangular argument; no claim is made that
the entire matrix is triangular in a single entry order.

To pass from the corner to the full polynomial symbol, write

    f_k(x,z)=sum_(i<a,s<b) F_(i,k,s) x^i z^s.

Each convolution factor is multiplication of homogeneous binary forms,
which commutes with an invertible linear change of its two variables.
Apply independent determinant-one changes on the two convolution factors
whose short inputs occur in this source leg. Their other input/output
maps act invertibly on the other source legs, so they preserve slice rank.

Choose each variable-change matrix to have second column(1,x) or(1,z),
for example [[0,1],[-1,x]]. The highest-coordinate coefficient of a
homogeneous binary form after this substitution is its value at that
second column. Thus the transformed corner sequence is exactly
(f_k(x,z))_k. Equation(4) gives, for every complex x,z,

    rank M_F>=ab rank(f_(p+q)(x,z)).                    (5)

A polynomial minor is nonzero over C(x,z) precisely when it is nonzero
at some complex point. The maximum rank on the right of(5) is therefore
the rational-function rank of the Hankel symbol. Consequently

    rank M_F>=ab rank_(C(x,z))(f_(p+q)).                 (6)

This recovers the imported theorem over C. The supplied corner checks
verify the coordinate zero pattern and repeated diagonal blocks in a
finite range. The general statement follows from(1)--(5), rather than
from extrapolating those checks. The other source's stronger field scope
continues to follow from its own polynomial-injection proof.
