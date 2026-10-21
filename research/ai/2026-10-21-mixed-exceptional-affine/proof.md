# An affine family with at least38 normal directions

Written proof, unreviewed, October21,2026. Claim
`AI-MIXED-EXCEPTIONAL-AFFINE-095`. No improved exponent is established.

Work over C with the canonical A4 leading flags, partner a=b=1, the full
B maximal seven-frame and a C five-space containing the actual mixed row
m+sum h_j*d_j. Its boundary four-space is arbitrary. Adopt the source
equations and shifted moving-plane induction of claims088--094.

There is an affine three-space of graph representatives

    h=(x-y, 1-x-z, 1-x, x, y, z),       (x,y,z) in C^3.       (1)

The complete necessary normal kernel has dimension at least38 at every
point of(1), and exactly38 on a nonempty open subset. At its base point
x=y=z=0, with h=(0,1,1,0,0,0), the full38-dimensional kernel is recomputed.
The subsequent target conditions reduce it to the four common-plane
directions. The adopted induction excludes M(10,10,11) at this graph,
with arbitrary later maps and boundary four-space. This point exclusion
does not classify target constructions on all of(1).

## 1. A global source-row chart at a=b=1

Write Z0,...,Z6 for the seven312-by88 blocks reconstructed in claim094.
Every normal satisfies

    M(h)*n=0,       M=Z6+sum h_j*Zj.                         (2)

The symbolic source partition from094 splits the88 normal coordinates
into two groups of44. Every source-covector row uses only one group
across all seven columns. The checker retains28 specified source rows
from each group. In each group, concatenate the seven blocks horizontally
to obtain a28-by308 matrix V. The corresponding matrix R of all source
rows is56-by308. A nonzero28-column minor of V gives a rational matrix C
and the exact identity

    R=C*V.                                                  (3)

This identity is checked before inserting graph parameters. Consequently
the selected28-by44 matrices N0(h),N1(h) give the complete ranks of the
two blocks of(2) at every h. No specialization of a generic graph kernel
is used to identify an exceptional kernel.

## 2. Polynomial left relations on the affine family

For each block, the certificate gives a3-by28 polynomial matrix Lg(x,y,z)
of degree at most two. Direct coefficient identities give

    Lg*Ng(h(x,y,z))=0.                                      (4)

A specified three-column minor of Lg equals4 at x=y=z=0. Thus Lg has rank
three over Q(x,y,z), and Ng has rank at most25 over that field. Every
26-minor of Ng is therefore the zero polynomial. The upper bound25 holds
at every complex point, including zeros of the chosen independence minor.
Using(3), the full M has rank at most50 everywhere on(1), so its kernel
dimension is at least88-50=38.

At the base point, exact rational row reduction gives rank25 in each
block and hence rank50 for M. A50-minor of M is nonzero there. Its
nonvanishing defines a nonempty open subset of(1) on which the rank is
exactly50 and the normal dimension is38. This proves the stated generic
dimension without asserting constant rank on the exceptional remainder.

## 3. Recompute the entire base-point normal space

At h=(0,1,1,0,0,0), the checker solves all312 equations(2), obtaining an
88-by38 kernel with its identity free-coordinate block. It verifies the
four independent plane directions inside this kernel and selects a
34-dimensional complement. Both the obstruction and the virtual third
tensor receive the actual C-column shear m -> m+d1+d2.

The joint obstruction rowspace now has44 rows and six boundary columns
(E0,O0,E1,O1,E2,O2). This is smaller than the56-row spaces in the preceding
generic and34-dimensional-normal cases; their row counts are not reused.
Its rows annihilate C, so their evaluated matrix S has rank at most two.
Project its columns by Q=(O0-E0,O1-E1,O2-E2). Fourteen coefficient-row
combinations W lie in the kernel of this projection. Hence

    rank S >= rank Q + rank W.                              (5)

If W=0, the normal lies in a six-dimensional linear family. Otherwise
(5) forces rank Q<=1. Specified triangular two-minors of Q are nonzero
rational multiples of squares of linear forms. Their vanishing forces
successive complete linear-kernel dimensions

    34 -> 26 -> 20 -> 18 -> 14.                              (6)

At the end Q vanishes identically on this14-dimensional family. Every
minor position, repeated diagonal form, triangular zero and determinant
ratio is checked from the reconstructed source, with no discovery search
inside the maintained verifier. These two families cover every necessary
normal; they are upper bounds rather than asserted solution components.

## 4. Apply the remaining source equations

Use the same unitriangular64-source change as in090 and093. At each saved
stage, subtract the part of every virtual source slice in the known
obstruction rowspace. The recorded additional slices have either a cover
by at most two B/C vertices or joint B coefficient rank at most two.
The previously proved saturated target rank gap forces their restrictions
to C to vanish. The new mixed-column equations and triangular cubic
minors reduce the two families as follows:

    W=0:          6 -> 0,
    rank Q<=1:   14 -> 10 -> 4 -> 2 -> 0.                    (7)

The first family uses adapted source positions16--19 and24--31. The
second first uses those positions, then20--23 after the reduction to4.
All source indices, covers and complete coefficient ranks are checked.
The transitions10->4 and2->0 use saved three-minors equal to nonzero
rational multiples of cubes of linear forms. Over C, their vanishing
forces those forms to vanish. The other transitions in(7) are the
complete linear kernels of the added mixed-column equations.

Thus only the four common planes remain at the base graph. Claim089's
mixed-space shifted induction applies: it permits unequal delayed growth,
arbitrary later regular output maps and a Laurent first-leg map. It
excludes the saturated M(10,10,11) target for any actual C five-space
containing this row. The argument has no assumption that the original
generic32-dimensional normal frame is complete at this point.

## 5. Scope

Equation(1) is a positive-dimensional exceptional normal family, not a
matrix multiplication construction. Its generic38-dimensional normal
space is larger than the32-,34- and36-dimensional strata previously
analyzed. Only its base graph receives the complete target exclusion
above. The general affine family, other a,b, arbitrary leading flags
and the matrix multiplication exponent remain open. Exact certificate
replay and CI do not supply independent mathematical review.
