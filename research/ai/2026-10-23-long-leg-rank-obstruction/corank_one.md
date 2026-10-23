# The A4 obstruction extends to a long-map limit of rank 109

October 23, 2026. Written and unreviewed. No smaller exponent.

This continues [the kernel-residual proof](proof.md). The source minimum-rank
classification is imported, with its existing proof status, from
[the prior source note](../2026-10-20-koszul/cyclic_finite_target.md), Section 4.

Claim `AI-A4-CORANK-ONE-LONG-001` is the new equality-case continuation.
The full-rank kernel mechanism retains the concurrent PR113 credit in
[proof.md](proof.md).

## Statement

There is no complete complex Laurent degeneration

    A4 -> M(10,10,11)

whose 112-by-110 long map C is regular and has rank at least 109 at
zero. The other long map and the first map may have arbitrary finite
Laurent poles. The assertion also holds with the two long legs exchanged.

The preceding regular-long-leg theorem handles rank 110. This note
handles rank 109 by classifying the equality case in its rank bound.
It does not exclude leading ranks at most 108 on both long maps.

## 1. Residual identity at the equality boundary

Use the source slice convention

    M(F)_((j,p,L),(H,q,r))=F_(H-j,p+q,L-r).

All source legs have dimension 112, and every nonzero source slice has
rank at least 16. Let E=Mat_10 and Xi(X)=X tensor I_11.

Scalar-normalize F and the other long map B inversely so that F is
regular and F0=F(0) is nonzero. The matrix C is unchanged. Choose an
invertible V in Mat_10 with F0(V) nonzero. Such a V exists because
invertible matrices are a dense open set and span Mat_10.

Set S=M(F(V)) and H=Xi(V)^(-1). The unit normalization in the preceding
proof gives regular matrices D=S C H and T_X, satisfying

    B D=I_110,       T_X(0)=Xi(X).

For every X, the regular residual

    W_X=M(F(X)) C-D T_X

has its columns in the two-dimensional kernel of B over C((t)). Hence

    rank W_X(0)<=2,
    M(F0(X)) C0=D0 Xi(X)+W_X(0).                       (1)

Let L=im C0. Its dimension is 109, so it has codimension three in the
112-dimensional source column space. If X has rank one and F0(X) is
nonzero, then

    16 <= rank M(F0(X))
       <= rank(M(F0(X)) C0)+3
       <= rank Xi(X)+2+3=16.                         (2)

Every inequality is therefore an equality. In particular

    rank M(F0(X))=16,
    rank(M(F0(X)) C0)=13.                            (3)

The source matrix has a 96-dimensional kernel. Its restriction to L
has kernel dimension 109-13=96, so

    ker M(F0(X)) is contained in L.                 (4)

Consequently the fixed three-dimensional annihilator L^perp lies in
the row space of every nonzero matrix M(F0(X)) with rank-one X.

## 2. Common row vectors force one source ruling

The credited minimum-rank classification says that every rank-16
source parameter has the form

    F_(i,k,s)=u_i h_k v_s,
    h_k=alpha^(6-k) beta^k,

up to nonzero scalar factors, with u,v nonzero homogeneous binary
cubics. Put S_d for the space of homogeneous binary forms of degree d.
The slice matrix factors, up to the displayed coordinate ordering, as

    U(u) tensor H(h) tensor V(v),

where

    U(u)_(j,H)=u_(H-j),
    H(h)_(p,q)=h_(p+q),
    V(v)_(L,r)=v_(L-r).

The row spaces of these factors are respectively

    u*S_3 subset S_6,
    span(alpha^3,alpha^2 beta,alpha beta^2,beta^3),
    C^4.

Both U(u) and V(v) have rank four. Therefore the full row space is

    (u*S_3) tensor span(h_short) tensor C^4.          (5)

Fix any nonzero lambda in L^perp. By (4), lambda belongs to every row
space (5) arising from a nonzero F0(X), with X rank one.

First, the middle line span(h_short) is fixed: a nonzero tensor cannot
belong to U tensor h tensor V and U tensor h' tensor V for distinct
one-dimensional middle subspaces. The degree-three Veronese map is
injective on P^1, so the line spanned by h itself is also fixed.

Apply a fixed linear functional to the middle factor of lambda that
does not kill h_short. Among the four resulting S_6 coefficients choose
one nonzero coefficient w. It is fixed and belongs to u*S_3 for every
relevant u. Thus every such projective cubic u divides the same nonzero
homogeneous sextic w.

There are only finitely many projective cubic divisors of a nonzero
binary sextic over C. This follows by factoring w into its finitely
many linear factors with multiplicities. There are at most 20 possible
divisors of degree three.

The rank-one parameter variety P^9 times P^9 is irreducible. Remove
the proper closed subset where F0 vanishes. Its image under F0 remains
irreducible and is contained in the finite union of the source spaces

    u tensor h tensor S_3

indexed by those cubic divisors. It therefore lies in one such space.
Equivalently, the projective u direction is fixed. Rank-one matrices
span E, so

    im F0 is contained in u0 tensor h0 tensor S_3,
    rank F0<=4.                                      (6)

No classification of all linear rank-one preservers is needed. The
common source row vector is stronger than preservation of the minimum
rank locus alone.

## 3. A small-codimension kernel contains an invertible matrix

For completeness, a linear subspace Q of Mat_m consisting entirely
of singular matrices has dimension at most m(m-1).

Here is the needed square-matrix proof. Let r be the maximum rank in Q.
The assertion is immediate when r=0. Otherwise choose a rank-r member
and apply constant invertible row and column changes so it is
diag(I_r,0). For each matrix in Q write blocks

    [ P  A ]
    [ B  C ]

with the same (r,m-r) split. The matrix diag(I_r,0)+t X has rank at
most r over C(t). Its Schur complement is zero. The coefficients of
t and t^2 give C=0 and B A=0.

Applying the latter identity to X+Y yields

    B_X A_Y+B_Y A_X=0.

Thus the image of Q under X -> (A_X,B_X) is totally isotropic for the
nondegenerate symmetric bilinear form

    ((A,B),(A',B')) -> tr(B A'+B' A)

on a space of dimension 2r(m-r). A totally isotropic subspace is
contained in its orthogonal complement, so its dimension is at most
r(m-r). The kernel of this block projection has dimension at most r^2.
Hence dim Q<=r^2+r(m-r)=mr<=m(m-1), as claimed.

By (6), ker F0 has dimension at least 100-4=96. Since 96>10*9=90,
there is an invertible X in ker F0.

## 4. The unit residual now gives a contradiction

The chosen invertible V satisfies F0(V) nonzero. By (6), it belongs
to a single minimum-rank source ruling, so M(F0(V)) has rank 16.
Because C0 has rank 109, restriction loses at most three ranks:

    rank D0=rank(M(F0(V)) C0 H)>=13.                  (7)

For the invertible X in ker F0, equation (1) gives

    D0 Xi(X)=-W_X(0).

The right side has rank at most two. The matrix Xi(X) is invertible,
so the left side has rank rank D0>=13. This is impossible.

## Scope

This argument uses the original A4 source minimum-rank classification,
the regular kernel residual, elementary binary-form divisibility,
irreducibility of the rank-one Segre variety, and the supplied
bounded-rank-subspace argument. It allows every finite Laurent order.

The source minimum-rank locus and ordinary obstruction remain credited
to the predecessor. There is no independent external review or formal
proof. No matrix degeneration or exponent improvement is constructed.

The corank-two case has one rank of slack in (2), so this equality-case
argument does not classify it. The previously available source
slice-rank gap excludes ranks 17 through 19, but this proof does not use
that stronger input.
