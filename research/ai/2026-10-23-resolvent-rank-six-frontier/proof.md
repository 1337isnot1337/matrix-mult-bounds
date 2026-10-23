# The complete rank-six locus and sharp compression dimension

October 23, 2026. Written and unreviewed. Ordinary matrix rank over an
arbitrary field F. No smaller matrix multiplication exponent is established.

We continue the fixed 112-dimensional space W of
[PR139](https://github.com/1337isnot1337/matrix-mult-bounds/pull/139).
Its source conventions and predecessor credits are retained in `sources.json`.
The new claims are `AI-RESOLVENT-RANK-SIX-FRONTIER-001` and
`AI-RESOLVENT-RANK109-COMPRESSION-002`.

**Result.** The rank-at-most-six locus in W is a 17-dimensional linear
subspace E. Every nonzero element of E has rank six and the same image I,
of dimension six. If P has size 110 by 112 and C has size 112 by 110,
and both have rank 109, then

\[
\dim\{X\in W:PXC=0\}\le1,\qquad \dim PWC\ge111.
\]

Both dimensions 111 and 112 occur. The lost direction, when present,
and the compression kernel/image pairs are classified below.

## 1. Adopted source and the integer seven-minors

Use the preceding proof's outer matrices

\[
S(f)_{(j,L),(H,r)}=f_{H-j,L-r},\quad
K=S(f_*),\quad f_*[i,s]=\mathbf1_{i+s=3},\quad
G(f)=K^{-1}S(f),\quad Q(f)=G(e_{00})G(f).
\]

Here i,j,r,s range from 0 through 3 and H,L from 0 through 6.
Rows and columns are lexicographically ordered. K is unimodular.
Multiplication on the left by K identifies the mixed block with

\[
B(g,f)=S(g)+S(e_{00})K^{-1}S(f).
\]

The gauge identity B(-e00,f*)=0 lets us take f03=0. In order, the
31 remaining parameters are the sixteen g coefficients followed by
the fifteen retained f coefficients, each in lexicographic order.

The exported certificate gives **26 successive seven-by-seven minors**.
At each step the specified submatrix is lower triangular and every diagonal
entry is the same current linear form ell up to a sign. Thus the minor
is plus or minus ell^7. If rank B<=6, ell=0 over every field.
The specified coefficient of ell is a unit, permitting an integer
substitution that removes one parameter. The certificate verifies every
entry of each minor and tracks the substitutions in the original coordinates.

The remaining five generators are

\[
A_i=S(e_{00})K^{-1}S(e_{i0})\quad(0\le i\le3),
\]
\[
A_4=-S(e_{10})+S(e_{00})K^{-1}
       S(e_{13}+e_{22}+e_{31}).
\]

No sample over a finite field is used to infer this elimination.
The acceptance program reconstructs S and a two-sided integer inverse of K,
then checks the 26 symbolic linear-form identities. It imports no discovery
program or prior verifier.

## 2. Polynomial normal form and complete mixed-block classification

Let R add row14 to row22 and row7 to row23, using zero-based indices.
This is a unimodular output change. Define T_i, for 0<=i<=4, by

\[
(T_i)_{7j,\,4(i+j)+3}=1,\qquad
(T_i)_{21+j,\,4i+j}=1\quad(0\le j\le2),
\]

with every other entry zero. Exact integer identities give

\[
RA_i=T_i\ (i<4),\qquad RA_4=-T_4.
\]

For p(x)=sum_i a_i x^i, the six possibly nonzero rows of sum_i a_i T_i,
in the order 0,7,14,21,22,23, are

\[
(0,0,0,p),\ (0,0,0,xp),\ (0,0,0,x^2p),\
(p,0,0,0),\ (0,p,0,0),\ (0,0,p,0).
\]

Each entry denotes the coefficient vector in its column residue r modulo4;
the polynomial degree is the H coordinate. There is no truncation, since
deg p<=4 and deg(x^2 p)<=6.
When p is nonzero these six rows are independent: the three first residues
force their constant coefficients to vanish, and
(a+bx+cx^2)p=0 forces a=b=c=0 in the polynomial domain F[x].
Their common six-dimensional image is the coordinate span of rows
0,7,14,21,22,23. Thus the rank-at-most-six mixed-block locus is exactly
the five-dimensional space spanned by A0,...,A4. Every nonzero point has
rank six, and its image before R is the same fixed six-space.

For a pure Q(f), fixing the gauge gives g=f03 e00.
In the five surviving coordinates, only A4 has a nonzero g coefficient,
namely -g10, while all have g00=0. Consequently f03 and the A4 coefficient
vanish. This proves the **pure Q locus is exactly span{Q(e_i0):0<=i<=3}**.
This intersection calculation uses the tracked original coordinates, not
only the dimensions of two spaces.

## 3. The full rank-six locus

In the middle-coordinate-first order, W has four-by-four blocks of size28.
The scalar identity, the g2 shift and the g1 shift are recovered respectively
from blocks (0,0), (1,0), and (2,0), successively when the preceding
parameters vanish. A nonzero scalar gives a rank28 block. A nonzero g2
or g1 gives a rank-at-least16 block by the prior outer-source minimum-rank
lemma. Thus a matrix of rank at most six has only its last block row nonzero:

\[
[\ G(g_0)+Q(f_3)\mid Q(f_4)\mid Q(f_5)\mid Q(f_6)\ ].
\]

Each individual block has rank at most six. Sections 1–2 show that the first
block is in the five-dimensional mixed locus and each other block is in
the four-dimensional pure locus. All four blocks have the same image.
Conversely, every combination of these blocks has rank at most six;
any nonzero block has rank six, so the whole matrix then has rank six.
The four independent block positions give dimension5+4+4+4=17.

After the fixed invertible output change diag(K,K,K,RK), write a member
as X(p), where

\[
p=(p_0,p_1,p_2,p_3)\in
\mathcal E=F[x]_{\le4}\oplus F[x]_{\le3}^{\oplus3}.
\]

Only the six output coordinates 84,91,98,105,106,107 can be nonzero.
They span I. For every nonzero p, im X(p)=I.
For a functional on I, its six coefficients identify it with

\[
q\in\mathcal V=F^{\oplus3}\oplus F[x]_{\le2},\qquad \dim\mathcal V=6.
\]

The row qX(p) is the coefficient vector of the sixteen component products
(p_j q_r)_(j,r). These have degree at most6. This exact, untruncated
polynomial product description is what the compression argument needs.
All statements about the original space follow by undoing the fixed
output change and coordinate permutation.

## 4. Elementary product-dimension lemma

Let A and B be nonzero finite-dimensional subspaces of F[x]^a and F[x]^b,
with dimensions d and e. Let A*B be the span of their component-pair
products (u_i v_j)_(i,j) in F[x]^(ab). Then

\[
\dim(A*B)\ge d+e-1.
\]

Here is a proof over every field. Order vector monomials lexicographically
by (degree,component). Echelon bases u1,...,ud and v1,...,ve have distinct
leading monomials, increasingly ordered. Embed their leading labels as
alpha=(degree,i,0) and beta=(degree,0,j) in lexicographically ordered Z^3.
The leading label of a component-pair product is alpha+beta: maximum
degree is obtained by multiplying maximum-degree terms, and the two
component indices choose the lexicographically last pair without cancellation.
The products

u1*v1, u2*v1, ..., ud*v1, ud*v2, ..., ud*ve

have strictly increasing leading labels, hence are independent.
This is an elementary argument supplied here; no external product-space
theorem or algebraic closure assumption is used.

## 5. Sharp rank109 compression and complete kernel incidence

Let U=im C and L=ker P, with dim U=109 and dim L=3. Every X with PXC=0
has rank at most6 by the ordinary rank-loss inequality. Hence the
compression kernel is a linear subspace T of the classified space E.

If T is nonzero, take X=X(p) in it. Since im X=I and rank X=6,
restricting X to the codimension-three space U leaves rank at least3.
But X(U) is contained in L, so X(U)=L, L is contained in I,
ker X is contained in U, and U=X^-1(L).

Let Q be the annihilator of L in I*, viewed inside V. It has dimension3.
For every p corresponding to T and q in Q, the row qX(p) annihilates U.
Thus the space of component-pair products Q*T lies in U-perp, of
dimension3. Section 4 gives

\[
3\ge\dim(Q*T)\ge3+\dim T-1,\qquad\dim T\le1.
\]

Therefore dim PWC is at least111.

Conversely, choose any nonzero p and any three-plane L inside I.
The preimage U=X(p)^-1(L) has dimension109. Choose P of rank109 with
kernel L, and C of rank109 with image U, padding to the stated sizes.
Then P X(p) C=0. The bound just proved shows that the entire lost
subspace is exactly span{X(p)}, so dim PWC=111.

This describes **every** nontrivial compression kernel: a unique projective
p in E and an arbitrary three-plane L in I determine U=X(p)^-1(L).
Conversely each such pair (p,L) is realized. The actual matrices P and C
may be any rank109 maps with the specified kernel and image.

For an explicit control in the transformed coordinates, take p=(1,0,0,0),
L=span{e84,e91,e98}, and U={v:v0=v1=v2=0}.
Delete these output rows and input columns and pad with zeros.
Exact rational rank of all112 compressed generators is111.
Deleting output rows0,1,2 instead makes L disjoint from I and gives
dimension112. The verifier repeats both controls over F2, F3 and F1009;
the all-field theorem follows from the proof, not from these four controls.

## Scope and remaining question

This classifies the complete low-rank locus and rank109 compression
incidence for this particular fixed W. It does not classify changing
resolvent spaces, higher Laurent corrections, or arbitrary singular tensor
degenerations. The compression bound does not by itself control how a
varying singular compression can acquire additional leading coefficients.
That requires a separate argument before any new target exclusion.
No independent mathematical review, formalization, historical priority,
or improvement below the external 9/4 baseline is claimed.
