# Higher jets and moving output surjections

Written local proof, unreviewed, October 20, 2026. No historical priority,
exponent improvement or independent review is claimed. The first-jet
package supplies the quantum family and its uniform slice-rank-28 minors.

## A truncated coefficient lemma

Let S(t) be an a-row matrix over R=C[[t]], with generic row rank d.
Let W be a fixed subspace of the ambient B tensor C. Suppose:

1. Every coefficient S_0,...,S_m has all its rows in W.
2. For a constant linear map pi on the ambient row-vector space,
   S_j pi=0 for j<m, and rank(S_m pi)>=k.

Then the saturated limiting rowspace contains at least k independent
vectors in W. In particular, if W=E_B tensor C+B tensor E_C, with
b=dim E_B and c=dim E_C, every regular tensor limit obtained from S(t)
with an arbitrary Laurent first-leg map has

    slice_rank <= a-k+b+c.                              (1)

To prove the assertion, write a rectangular Smith decomposition

    S(t)=U(t) diag(t^e_i) V(t),

with the d nonzero diagonal entries understood, e_i>=0, and U,V regular
invertible matrices. For e_i<=m, the constant primitive row V_i(0) is
in W: it is coefficient e_i of row i of U^-1 S. These primitive rows
are independent, and they belong to the saturated limiting rowspace.

Since S pi is divisible by t^m, the same is true of U^-1 S pi. Hence
V_i pi is divisible by t^(m-e_i) for every e_i<=m. Consequently

    S_m pi = sum_{e_i<=m} U_i(0) (V_i pi)_(m-e_i).

All e_i>m terms vanish at this order. The rank of the right side is at
most the number of indices e_i<=m, so that number is at least k. Complete
those primitive rows to a basis of the saturated limiting space, whose
dimension is at most a. Their tensor has slice cost at most b+c; each
remaining row costs one first-leg slice. Restriction on that leg gives
(1), by the same lattice argument as the preceding package.

Both hypotheses matter. In particular one cannot infer saturated-row
counts from an arbitrary coefficient matrix's rank: the polynomial matrix
[[1,t],[t,t^2]] has generic rank one and linear-coefficient rank two.

## Application to regular moving output projections

Take any of the sixteen ordered quantum root phases of orders three and
six. Let R_B(q),R_C(q) be the regularized 112-by-112 quantum local maps
from the preceding package. Their leading images E,F have dimension four.
Consider

    P(t)=L_B(t) R_B(q_B(t)),
    Q(t)=L_C(t) R_C(q_C(t)),

where each L is a regular map from dimension 112 to dimension 110 and
**L_B(0),L_C(0) are surjective**. The two nonconstant parameter arcs may
have different positive approach orders and arbitrary higher terms. The
remaining first-leg map is arbitrary Laurent, subject only to regularity
of the final tensor. No regularity is imposed before these output maps.

Saturate the R-submodules L_B(t)E and L_C(t)F inside their output modules.
They are direct summands of ranks b,c<=4. Regular invertible output gauges
make these summands constant subspaces Ehat,Fhat. This does not change the
limiting slice rank. Each contains the image at t=0 of its original
four-dimensional leading space. Since the maps at zero are surjective
with two-dimensional kernels, b,c>=2.

Let m be the earlier quantum approach order. Suppose B varies at this
order, with nonzero leading rate lambda; the opposite case is symmetric.
Every coefficient of S through order m lies in

    W=Ehat tensor C + B tensor Fhat.

Before order m it lies even in Ehat tensor Fhat. Projection on B/Ehat
kills all earlier coefficients. At order m it leaves

    lambda (pi L_B(0) R_B'(zeta_B) tensor L_C(0) G_C) T.

The opposite quantum derivative vanishes in this quotient, as does every
coefficient of L_B(t)G_B. These observations hold after the regular output
gauges as well, since their contribution from the leading map lies in
Ehat.

The map L_C(0) cannot annihilate F. Choose an output functional whose
pullback beta to F is nonzero. The preceding package's four-coordinate
slice minors and grading proof give

    rank [ (G_B+J_B,out) tensor G_C ] T |_beta >= 28

for every such beta and every nonzero lambda on J_B,out. Passing to B/E
loses at most four dimensions, leaving rank at least 24. The surjection
induced by L_B(0),

    B/E -> B'/Ehat,

has kernel dimension

    (112-4)-(110-b)=b-2 <= 2.

Thus the projected coefficient at order m has rank at least 26-b>=22.
Apply (1), with a=112 and k=26-b, to obtain

    slice_rank <= 112-(26-b)+b+c = 86+2b+c <= 98.         (2)

For an earlier C approach the bound is 86+b+2c<=98. The target
M(10,11,10), with leg dimensions 100,110,110, restricts to square M10
and therefore requires slice rank at least 100. Equation (2) excludes it
in this family. Nonconstant Puiseux arcs follow after a common ramified
base change. A constant root parameter gives generic local rank at most
four and cannot yield a concise 110-dimensional leg.

The uniform number-field slice minors, rather than a random choice of
beta, justify this conclusion over C. Moving output maps may have kernels
meeting the leading images; they need only remain surjective at t=0.
Further restrictions and complex degenerations preserve the slice bound.

Singular leading output maps of rank below 110, other leading quantum
flags and non-scalar block weights are outside this corollary. The general
matrix-multiplication exponent remains open.
