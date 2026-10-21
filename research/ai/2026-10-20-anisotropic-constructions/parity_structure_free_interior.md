# The source inside the two physical endpoints

October 21, 2026. The following construction is exact:

\[
A(a,a)|_{\mathrm{free}}
\longrightarrow M_{a-1}\oplus M_{a-1}\oplus M_{a-2},\qquad a\ge3.\tag{1}
\]

For the live A(8,8) source, its maps use only the 722 free source
coordinates left after fixing both physical endpoint rows and columns.
The target is M7 direct sum M7 direct sum M6, with leg dimension 134
and 902 nonzero tensor coefficients. This identifies exact usable
structure inside the affine anchor fiber. Compatibility with the
fixed boundary maps of the full M27 direct sum M7 target remains a
separate requirement.

## The physical source and its free coordinates

Use the common source order F(i,k,s), with 0<=i,s<a and 0<=k<=2a-2.
The physical matrix is

\[
W(F)_{(i,q),(p,s)}=F(i,p+q,s),\qquad
T(F_X,F_Y,F_Z)=\operatorname{tr}(W(F_X)W(F_Y)W(F_Z)).\tag{2}
\]

The original source orders on the three legs are respectively
X=(i,k,s), Y=(s,i,k), and Z=(k,s,i). These are actual permutations
in the exported maps.

Put h=a-1. The two physical endpoint states are H=(h,0) and L=(0,h).
A coefficient F(i,k,s) contributes to a row or column at one of these
endpoints exactly when at least one of the following holds:

\[
(i=h,\ k\le h),\quad(i=0,\ k\ge h),\quad
(s=0,\ k\ge h),\quad(s=h,\ k\le h).\tag{3}
\]

Deleting these coefficients leaves three disjoint coordinate sets:

| Set | First and last indices | Long index | Dimension |
| --- | --- | --- | --- |
| Low | 0<=i,s<h | 0<=k<h | h cubed |
| Center | 1<=i,s<h | k=h | (h-1) squared |
| High | 1<=i,s<=h | h<k<=2h | h cubed |

Thus the free coefficient space has dimension
2(a-1)^3+(a-2)^2. Its physical matrices act on a^2-2 states.
For a=8 these dimensions are 722 and 62.

The low matrices are supported on physical states {0,...,h-1} squared.
The high matrices are supported on {1,...,h} squared. Their overlap
has dimension (h-1)^2, and their union is the entire physical interior.
The central coefficients also join the two outer parts: the terms
with p=0,q=h and p=h,q=0 cross between those parts. Consequently the
three coordinate sets themselves are not three independent tensor
summands.

The tensor using only the low cube is the cyclic product of three
truncated one-variable convolution tensors. Reversing each long
coordinate identifies it with the Frobenius multiplication tensor of
the algebra C[x,y,z]/(x^h,y^h,z^h). The high cube is its reflected copy.
The center alone is M_(a-2), after the transpose used below.

## Explicit maps and the mixed coefficients

For a target matrix unit E_IJ, use the following common source point
with coefficient one:

| Target block | Vertex indices | Source point F(i,k,s) | Vertex charges |
| --- | --- | --- | --- |
| Low M_h | 0<=I,J<h | (I,J,0) | I |
| High M_h | 0<=I,J<h | (h-I,2h-J,h) | -I |
| Center M_(h-1) | 0<=I,J<h-1 | (J+1,h,h-1-I) | -I |

Every selected coordinate satisfies (3)'s complement. Within the low
block, the three source equations give the usual matrix cycle
E_IJ,E_JK,E_KI. Reflection gives the high block. For the central
block, substituting the third row of the table gives exactly the same
cycle; the exchanged I,J in the first source index is essential.

All mixed coefficients vanish. In a cycle with one central and two low
variables, a long index h would have to equal a first short index at
most h-1 plus a last short index zero. Two central and one low variable
give the same contradiction on a neighboring central leg. Reflection
handles the corresponding high cases. With low and high variables
only, one long index is forced outside its range. With all three
categories present, one of the two cyclic orientations forces a high
long index greater than h to equal a central first index plus zero;
the other forces a low long index less than h to equal a central first
index plus h. These cover all placements of distinct blocks.

The selected rows and source columns are distinct in each map. Hence
the maps are surjective onto the claimed direct sum. Their charges
are preserved under the common grading i+s-k, as the last column of
the table records.

## The affine boundary completion equation

Order physical states as the two endpoints followed by the interior.
For any three target-to-source linear maps in a fixed boundary fiber,
write

\[
J_i(A)=\begin{pmatrix}P_i(A)&R_i(A)\\ C_i(A)&D_i(A)\end{pmatrix},
\qquad D_i=D_i^0+F_i.\tag{4}
\]

The blocks P_i,R_i,C_i and D_i^0 are fixed by the boundary source
coefficients. The free term F_i belongs to the 722-dimensional source
space above, represented on the 62-dimensional physical interior.
It is not an arbitrary 62 by 62 matrix.

Direct block multiplication gives the exact equation

\[
\begin{aligned}
\operatorname{tr}(J_XJ_YJ_Z)
={}&\operatorname{tr}(D_XD_YD_Z)
 +\sum_{\rm cyc}\operatorname{tr}(D_XC_YR_Z)+K,\\
K={}&\operatorname{tr}(P_XP_YP_Z)
 +\sum_{\rm cyc}\operatorname{tr}(P_XR_YC_Z).
\end{aligned}\tag{5}
\]

The three summands outside the interior cubic are linear in the
corresponding D block. This formula retains the boundary slack terms
present in the flexible anchor seed.

For target variables supported on the 25 interior vertices of the
large block, or on the separate small block, the endpoint block P is
zero. The two opposite extreme slices force its diagonal entries to
zero, and torus grading forces its off-diagonal entries to zero.
The blocks R and C may still be nonzero. Thus the remaining target
M25 direct sum M7 must be completed through the cubic in D plus the
three linear terms in (5). The exact interior direct sum (1) supplies
candidate pieces for this equation; it does not remove the linear
boundary terms automatically.

## Replay and scope

`parity_structure_free_interior.py` uses only the Python standard
library. It exports all three integral 134 by 960 maps for a=8,
enumerates every one of the 262,144 source terms, and compares the
complete image with M7 direct sum M7 direct sum M6. The replay checks
every mixed coefficient, the free-column condition, all map charges,
and rejection of a changed nonzero map coefficient. The same complete
calculation was also run for a=3,4,5,6,7.

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_free_interior.py
```

These are exact restriction and decomposition statements. They do not
establish the missing full target or a smaller matrix multiplication
exponent. They were produced in this generating session; no external
independent review or priority is claimed.
