# The complete rank-six locus of the fixed-resolvent space

October 23, 2026. Written and unreviewed. No exponent improvement.

## 1. Source and statements

Use exactly the source matrices, unit, normalization and limiting space W
of `AI-RESOLVENT-SHARP-MINRANK-001`, pinned in `sources.json`. That prior
result proves dim W=112 and minimum nonzero ordinary matrix rank six over
every field. Its source conventions and PR103 resolvent construction retain
their original credit. This note classifies its low-rank locus; it concerns
ordinary matrix rank, not tensor slice rank.

For 0<=i,s<=3 write e_is for the coefficient basis of the outer source.
As in the predecessor, let S(f) have entries f_(H-j,L-r), let
K=S(e_03+e_12+e_21+e_30), and put G(f)=K^-1 S(f) and
Q(f)=G(e_00)G(f). All are 28-by-28 matrices, with the predecessor's
lexicographic orders. The inverse of K is integral.

Let

    R = {0,7,14,21,22,23},
    E = K^-1 span{e_r : r in R},
    T = Q(e_13+e_22+e_31) - G(e_10),
    V = span{Q(e_00), Q(e_10), Q(e_20), Q(e_30), T},
    V_Q = span{Q(e_00), Q(e_10), Q(e_20), Q(e_30)}.

Here e_r in the formula for E denotes an output coordinate vector, not an
outer-source coefficient. The distinction fixes the image coordinates.

**Outer-block theorem.** Over every field, in
X={G(g)+Q(f): f,g in F^16}, the locus of matrices of rank at most seven
is exactly V. Its dimension is five, and every nonzero member has rank six
and image E. In the subspace Q(F^16), that locus is exactly V_Q, of
dimension four. Neither space contains a matrix of rank seven.

**Full-space theorem.** Put the middle coordinate first as in the
predecessor. The locus of matrices in W of rank at most seven is the
17-dimensional linear subspace

    W_6 = { matrices with only final block row (B0,B1,B2,B3) nonzero:
            B0 in V and B1,B2,B3 in V_Q }.

Every nonzero member has rank six and the same image
E_full = e_3 tensor E. Thus W has no matrix of rank seven.

**Critical compression theorem.** Over an algebraically closed field,
let P be 110-by-112 and C be 112-by-110, each of rank 109. Then

    dim ker(X -> PXC, X in W) <= 1,
    dim PWC >= 111.

The bound 111 is attained. A nonzero kernel requires ker P to be a
three-dimensional subspace of the fixed E_full, strengthening the
predecessor's final-28-dimensional-layer condition. These are statements
about this fixed limiting space and these compression factors only.

## 2. Exact outer-block certificate

Multiplication on the left by K sends X to

    {S(g)+S(e_00)K^-1 S(f)}.

The relation Q(e_03+e_12+e_21+e_30)=G(e_00) allows the gauge f_03=0:
replace f by f-f_03(e_03+e_12+e_21+e_30) and g by g+f_03 e_00.
The predecessor proves independence of the resulting 31 generators.

The supplied `certificate.json` has 26 elimination stages. At each stage
it gives eight distinct rows and columns forming a lower triangular
submatrix, with every diagonal entry equal to plus or minus one linear
form ell in the remaining parameters. The corresponding determinant is
plus or minus ell^8. If the represented matrix has rank at most seven,
then ell=0 over any field. A coefficient of ell is 1 or -1, so substitution
removes one parameter over the integers. There is no division by a
possibly vanishing parameter or by a field characteristic.

`verify.py` reconstructs all source slices from their literal indices,
computes K^-1 by rational elimination, and checks that it is an integral
two-sided inverse. It checks every entry above each selected diagonal,
each complete diagonal linear form, and each unit substitution. It tracks
the substitutions back to the original 31 coordinates. After 26 steps
the surviving five basis vectors are exactly

    f_00, f_10, f_20, f_30,
    -g_10 + f_13 + f_22 + f_31.

This is an identity of parameter spaces, not a finite sample. The replay
also checks that all five surviving matrices after multiplication by K
have zero rows outside R. Hence their span has rank at most six. The
predecessor's minimum-rank-six theorem makes every nonzero member have
rank exactly six. Its image is therefore the entire six-dimensional E.
The predecessor's independence also proves dimension five.

For a pure Q(f), gauge fixing produces g=f_03 e_00. In V the g coefficient
is instead a multiple of -e_10. Thus f_03=0 and the fifth basis coefficient
is zero. The remaining f is supported on e_i0, which proves the claimed
intersection V_Q. This argument includes the originally ungauged f_03
parameter and does not assume it vanishes in advance.

The discovery search merely selected the minors. The proof uses only the
replayed integer identities and the pinned predecessor theorem.

## 3. From the outer block to W

The predecessor supplies the following block description of W:

- a scalar multiple of I112;
- J2 tensor G(g2) and J1 tensor G(g1), where J2 and J1 shift the middle
  coordinate upward by one and two respectively;
- the final block row, with B0=G(g0)+Q(f3) and B1,B2,B3 arbitrary in Q(F^16).

A nonzero scalar leaves a rank-28 block at (0,0). After that scalar is
zero, a nonzero g2 leaves a block of rank at least 16 at (1,0). After g2
is zero, a nonzero g1 leaves such a block at (2,0). The rank-16 assertion
is the predecessor's all-field outer-source minimum-rank theorem.
Consequently a matrix of rank at most seven has only its final block row.

Every block of that row also has rank at most seven. Section 2 forces
B0 into V and the others into V_Q. Conversely, all four such blocks
have image in E, so their horizontal concatenation has rank at most six.
The predecessor's full-space lower bound makes it six whenever nonzero.
Independence of the original block positions and the dimensions in
Section 2 give 5+4+4+4=17. The image is E_full for every nonzero member.
This proves the complete locus and the gap at rank seven.

## 4. Critical compression

Let U=im C and L=ker P. Their dimensions are 109 and three. If a nonzero
X in W satisfies PXC=0, the elementary rank-loss bound gives rank X<=6.
Section 3 makes rank X=6 and im X=E_full. Also X(U) is contained in L,
and restriction to the codimension-three U loses at most three ranks.
It follows that X(U)=L and L is contained in E_full. The kernel of X|U
has dimension 106, equal to dim ker X, so

    ker X subset U,    U = X^-1(L).

These equality constraints agree with the predecessor but now use the
fixed six-dimensional image instead of an unspecified image in a layer.

For every X in the compression kernel, its quotient map factors as

    F^112/U -> E_full/L.

For nonzero X this is a surjection between three-dimensional spaces,
hence is invertible. Moreover the linear map from the compression kernel
to these three-by-three matrices is injective: a nonzero X cannot have
image contained in L, since its image has dimension six.

A linear space of square matrices over an algebraically closed field in
which every nonzero element is invertible has dimension at most one.
Indeed, for independent invertible A,B the polynomial det(A+tB) has
positive degree three with nonzero leading coefficient. It has a root,
but A+tB is nonzero there, a contradiction. Apply this elementary argument
to the quotient maps. Thus the compression kernel has dimension at most
one and dim PWC>=112-1=111.

For sharpness, choose any nonzero X0 in W_6 and any three-space L inside
E_full. Its preimage U=X0^-1(L) has dimension 106+3=109. Choose a map P
of the required size with kernel L and a map C of the required size with
image U; both have rank 109. Then PX0C=0. The proved upper bound on the
kernel dimension makes it exactly one. This gives dim PWC=111. This
existence construction is valid over every field; the universal upper
bound on the kernel dimension here is claimed over algebraically closed
fields. No arbitrary-field constant-rank-subspace theorem is assumed.

## 5. Scope and next question

All source-locus and rank-gap assertions hold over every field by integer
identities. The critical-compression dimension bound uses algebraic
closedness explicitly. All proofs remain written and unreviewed.

The result classifies the equality locus left open by the predecessor.
It does not construct M(10,10,11), classify a different resolvent, or
exclude arbitrary singular Laurent trajectories. Larger total rank-loss
budgets require additional analysis. The first new question is the exact
compression-kernel dimension for total rank-loss seven, where the absent
rank-seven stratum still forces every lost direction into W_6.
