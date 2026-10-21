# A complete screen of common seven-vertex maps

October 21, 2026. This finite calculation covers one common physical
vertex on each of seven consecutive charge diagonals in the A(8,8)
physical grid. It finds no exact M7 map in that family which also
leaves the required weight-zero directions for the displayed M27
profile. It does find sixteen low-rank partial constructions, each
retaining all 343 desired terms and adding 498 unwanted terms.

## The complete family and the necessary rank test

Choose seven physical vertices (i_c,q_c), with 0<=i_c,q_c<8 and

\[
i_c-q_c=d+c,\qquad c=0,\ldots,6.
\]

The shift d ranges from -7 to 1. These nine strips contain exactly
1,290,240 vertex choices. The proposed common map is

\[
E_{uv}\mapsto F(i_u,q_u+i_v,q_v).
\]

Two target rows collide precisely when their source first and last
indices coincide and their charge differences coincide. Equivalently,
for some nonzero separation delta there are both a pair c,c+delta
with equal i values and a pair e,e+delta with equal q values. The
search rejects such collisions as soon as both pairs occur.

Given neighboring target matrix units E_uv and E_wz, their contraction
against the remaining source leg selects at most one coordinate:

\[
F(q_w+i_z-q_v,\ i_u+q_z,\ q_u+i_v-i_w),\tag{1}
\]

when both short indices are between zero and seven. At weight zero
the target indices obey u+w=v+z. Different source coordinates in
(1) have disjoint supports as functions of the neighboring units,
so the contraction rank is exactly their number.

The displayed M27 profile requires 53 source directions at weight
zero, out of 64. Therefore the fixed small pair must have rank at
most 11. The set of exposed coordinates grows monotonically as
vertices are added. This permits exact pruning of any partial
choice which already exposes twelve coordinates.

## Results and certificates

Only 15,189 partial assignments are visited. Accounting for every
completion below a pruned branch partitions all 1,290,240 full
choices. Sixteen survive the injectivity and rank tests. Every one
has zero-weight pair rank 9 and total pair rank between 111 and 113.
Their full rank profiles are recorded, including the separate
capacity checks at every source weight.

For each surviving choice the checker enumerates all 2,401 pairs of
neighboring target matrix units using (1). Its complete tensor image
has 841 unit coefficients: the 343 matrix multiplication coefficients
and 498 additional coefficients. Because the maps are monomial and
injective, each unwanted coefficient is a single nonzero product;
changing nonzero constant row scalars cannot cancel it.

One representative has

\[
i=(0,2,4,6,1,3,5),\qquad q=(3,4,5,6,0,1,2).
\]

The low ranks therefore do not certify a matrix tensor. These
near-seeds are retained with all vertex coordinates and exact rank
profiles for possible changes involving mixed source maps.

## A direct Laurent-rescaling obstruction

Each of the sixteen images contains an unwanted triple of diagonal
target units E_ii,E_jj,E_kk, and its two cyclic placements. The
checker records one such orbit. The three pure diagonal target terms
(E_ii,E_ii,E_ii), (E_jj,E_jj,E_jj), and (E_kk,E_kk,E_kk) are desired
matrix terms.

On each tensor leg, the unwanted orbit and these three desired terms
use exactly the same multiset of rows. Their total valuations under
any coefficientwise Laurent rescaling are therefore equal. Retaining
every desired term at valuation zero makes the sum of the three
unwanted valuations zero. They cannot all have positive valuation.
Thus a diagonal degeneration of these monomial row maps cannot
remove all extras while retaining all 343 desired coefficients.

This does not rule out an intervening change of basis or new mixed
source coefficients. The saved claim is only about coefficientwise
rescaling of the displayed maps.

## A useful counterexample to an overly broad rank bound

The physical vertices (0,0),(7,6) give an exact M2 with consecutive
charges zero and one. Its zero-weight pair contraction exposes only
F(0,0,0) and F(7,13,6), so its rank is two. Consequently a proposed
general bound r0>=2n-1 for all common physical-vertex M_n maps is
false. This positive control is checked separately from the failed
M7 choices.

## Replay

The complete maintained replay uses only the Python standard library:

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_m7_vertex_screen.py
```

An optional C++ implementation produced the same branch counts and
survivors during discovery; it is not required for replay. The finite
family, exact support failures, and balanced Laurent certificates
are all explicit. No arbitrary-map obstruction or new exponent is
claimed.
