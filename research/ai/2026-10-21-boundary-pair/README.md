# An exact boundary pair for every size

Date: 2026-10-21

Status: proved by the explicit integer maps below. This is a local construction. It does not provide a complete family of all degree sectors and does not improve the matrix multiplication exponent by itself.

## Conventions and statement

Let P_d denote polynomials of degree at most d. The convolution tensor C(a,b) is polynomial multiplication P_(a-1) times P_(b-1) into P_(a+b-2). A restriction is specified by input polynomials and output coefficient functionals.

Write H(r,s) for the same convolution tensor with its output as the shared leg:
H(r,s) = sum_(j=0)^(r-1) sum_(k=0)^(s-1) x_(j+k) y_j z_k.

For every integer m >= 3, over every field, the construction gives
C(m+2,m+1) degenerates to H(2,m-1) plus_X H(m-1,2).
The shared leg has dimension m. Each of the two other target legs has dimension m+1. The shared bases of the two blocks can be made identical by the choice of upper output duals.

## 1. Shared polynomials and boundary moments

Use the ordered m-dimensional space
U = (t^2,...,t^(m-2), a, b, c),
a = t+t^(m-1), b = 1+t+t^m, c = t+t^(m+1).
The initial list is empty when m=3.

Let delta_j extract the coefficient of t^j in P_(2m+1). Define
E0 = delta_0-delta_m+delta_(2m),
E1 = delta_1-delta_(m-1)-delta_m-delta_(m+1)
     +delta_(2m-1)+2 delta_(2m)+delta_(2m+1).

Direct substitution gives E0(U)=E1(U)=E0(t^m U)=E1(t^m U)=0.

The following integral functionals are dual to the ordered vectors (u_i,t^m u_i). Indices i start at zero. For 0 <= i <= m-4 use
d_i = delta_(i+2), e_i = delta_(m+i+2).
For the final three indices use
d_(m-3)=delta_(m-1),
d_(m-2)=delta_0,
d_(m-1)=delta_1-delta_0-delta_(m-1),
e_(m-3)=delta_(2m-1),
e_(m-2)=delta_(2m),
e_(m-1)=delta_(2m+1).

Thus d_i(u_j)=e_i(t^m u_j)=delta_ij and both cross pairings vanish. In particular U+t^m U has dimension 2m in every characteristic. E0 and E1 are independent, so they form its entire two-dimensional annihilator.

## 2. The boundary block

Take the second-input basis (t,t^2,...,t^(m-1)) and the two output rows (E0,E1). Set n=m-1 and change the shared basis to
r_1=a-b,
r_j=t^(m-j) for 2 <= j <= m-2,
r_(m-1)=b,
r_m=c.

This change is unimodular. The two m-by-n coefficient matrices are exactly
A = [-I_n; 0],
B = [-J; e_n^T],
where J has entries one on the diagonal and the two adjacent diagonals, and zero elsewhere.

These matrices are equivalent over the integers to H(n,2). Here is a self-contained verification of that claim. Transpose the pencil:
P(lambda) = A^T + lambda B^T
          = [-I_n-lambda J, lambda e_n].

A polynomial kernel vector is
v(lambda) = (lambda adj(I_n+lambda J)e_n, det(I_n+lambda J)).
It has degree at most n. Write v(lambda)=v_0+...+lambda^n v_n.

The last coordinate of v_0 is one and its other coordinates are zero. For k>=1 the first n coordinates of v_k are (-J)^(k-1)e_n plus an integral combination of the earlier Krylov vectors. The matrix
[e_n, J e_n, ..., J^(n-1)e_n]
is antitriangular with antidiagonal entries one: J^k e_n first reaches coordinate n-k with coefficient one. Its determinant is therefore plus or minus one. Consequently (v_0,...,v_n) is an integral unimodular basis.

The coefficient identities in P(lambda)v(lambda)=0 give
A^T v_0=0,
A^T v_i=-B^T v_(i-1) for 1<=i<=n,
B^T v_n=0.
The n vectors A^T v_1,...,A^T v_n form an integral unimodular output basis, since A^T=[-I_n,0]. In these bases the two maps are the two consecutive coordinate deletions, with a possible sign change. This is exactly H(n,2). All transformations remain invertible after reduction to any field.

## 3. The opposite block

In the original shared basis set
L_j = d_j + e_(j+1), 0 <= j <= m-2.
On the two second-input polynomials (1,t^m), the coefficient equations are
L_j(u_i)=delta_(i,j),
L_j(t^m u_i)=delta_(i,j+1).
Thus this block is H(2,m-1).

The boundary block normalization in section 2 changes the shared basis. To obtain a common shared basis for both blocks, apply that shared basis change first and retake the duals of its vectors and their t^m multiples. The 2m-dimensional independence proved in section 1 guarantees these duals, and the same formula for L_j then gives the canonical opposite block. This retuning does not change E0 or E1 or their vanishing equations. Alternatively, retaining the displayed d_i and e_i gives the two blocks with independent shared bases.

## 4. The degeneration

The second-input polynomials (1,t^m,t,...,t^(m-1)) are a basis of P_m. Give (1,t^m) weight zero and the remaining m-1 polynomials weight one. Give the upper output rows L_j weight zero and the boundary output rows E0,E1 weight minus one. Give the shared rows weight zero.

The only negative-weight coefficients pair U or t^m U with E0 or E1. Section 1 proves all of them vanish. The weight-zero coefficients are exactly the two blocks in sections 2 and 3. The remaining cross block has weight one.

Therefore the transformed tensor has the exact form T_0+epsilon T_1, where T_0 is the stated shared-output pair. This gives genuine three-factor Laurent linear maps for the claimed degeneration.

## 5. What this leaves open

Embedding the pair into a larger convolution source may use a polynomial f and the ideal inputs f(1,t^m) and f(t,...,t^(m-1)). Extending the construction to all inner sectors requires compatible quotient input spaces and output functionals. Quotient representatives may need graph lifts y+f q(y); forcing literal low-degree representatives adds an unjustified restriction.

This note proves the boundary pair only. It makes no claim that the inner sectors admit simultaneous completion with B=N+O(m), nor that any exponent smaller than 9/4 follows.

## Verification

The adjacent dependency-free JavaScript verifier uses exact BigInt arithmetic. It checks the dual identities, all negative coefficients, both displayed boundary matrices, the opposite block, and the Krylov determinant. The committed report replays m=3 through 20. The proof above establishes the result for every m>=3; the finite replay is a reproducibility check.

A separate standard-library Python implementation,
`verify_integer_maps.py`, constructs the coefficient vectors of v(lambda),
performs the unimodular basis changes, and retunes all upper duals. It
exports actual canonical integer maps in a common shared basis and
expands the original convolution coefficients. For m=3 through 20 it
checks all 50,028 target coefficient positions exactly. Its receipt is
`results/ai/2026-10-21-boundary-pair/integer-maps-verification.json`.

The written proof and same-session checks have no external mathematical
review or local formalization. The construction is not asserted to have
historical priority.
