# The degree-13 proof depends only on boundary multiplicities

## Extended scope

The proof in [torus_degree13_pencils.md](torus_degree13_pencils.md)
continues to exclude an ordinary grading-preserving restriction of
`A(8,8)` to `M27 direct_sum M7` under the following weaker assumptions.
The three 27-dimensional vertex spaces can have different charge
lists, all supported on 0 through 14. For each of these vertex spaces,

\[
 m(0)=m(1)=m(13)=m(14)=1,\qquad m(2)\ge2,\quad m(12)\ge2.
 \tag{1}
\]

The seven-dimensional summand has no parameters at weights 13, -13,
14, or -14 on any leg. Its other charges need not equal the earlier
consecutive choice. All three target-to-source maps may vary freely
within their weight blocks.

This extension requires no common charge list and no symmetry of the
interior multiplicities. It remains an ordinary graded restriction
obstruction. Singular limits, ungraded maps, and profiles violating
(1) are not excluded. No exponent improvement follows.

Only the rank-chain dependency of the earlier proof needs to be
checked again. Its two universal product tables, endpoint projection
containments, mixed-type exclusions, and Boolean classification use
only the four singleton boundary charges and the absence of auxiliary
parameters at degrees 13 and 14. They do not use the interior counts.

## The two-leg rank chain under (1)

Write the target legs in the order

\[
 X\in\operatorname{Hom}(V,U),\qquad
 Y\in\operatorname{Hom}(W,V),\qquad
 Z\in\operatorname{Hom}(U,W).
\]

Assume the type `C` pure degree-13 row occurs on both `X` and `Y`:
the unit from the charge-zero column to the charge-13 row maps to
a nonzero multiple of `F(6,0,7)`. The extreme units already map to
nonzero multiples of `F(7,0,7)`. Use the source channel lists `R,C,K`
from [the rank-chain proof](parity_balancing_rankone_13_chain.md).

The two selected `X` slices force the three-dimensional channel
rowspace `C_Z(2)` to contain `m_W(2)` independent forms joining
the charge-two vertices of `W` to the charge-14 vertex of `U`,
and one further form joining the charge-one vertex of `W` to the
charge-13 vertex of `U`. If `m_W(2)>2`, these are more than three
independent forms and already give a contradiction. Otherwise
`m_W(2)=2`, and they determine the whole rowspace of `C_Z(2)`.

The `m_U(12)` forms joining the charge-zero vertex of `W` to the
charge-12 vertices of `U` are distinct from these three forms.
Consequently their coefficients vanish on every row of `C_Z(2)`.
The exact shared source coordinate

\[
 C_Z(2)_0=R_Z(12)_0
\]

then makes the first of the three `R_Z(12)` channels vanish on
this `m_U(12)`-dimensional target input subspace.

The positive extreme `Y` slice requires a bilinear form of rank
`m_U(12)` on that subspace. Only two physical channels remain, so
`m_U(12)>2` gives a contradiction. In the only remaining case
`m_U(12)=2`, the remaining two-by-two coefficient block is invertible.

Use the pure type `C` row on `Y` and the identity

\[
 K_X(12)=(F(5,6,0),C_X(13)_0,C_X(13)_1).
\]

The first channel has coefficient zero by the previous paragraph.
Inverting the remaining two-by-two block forces the two rows of
`C_X(13)` to span exactly the two forms joining the charge-12
vertices of `U` to the charge-13 vertex of `V`. The extreme `Y`
slice at charge 13 also puts the independent form joining the
charge-13 vertex of `U` to the charge-14 vertex of `V` in that
same two-dimensional rowspace. This is impossible.

Thus two different legs cannot both have type `C` under (1).
The proof also covers the cases of a larger multiplicity at
charge 2 or 12; it does not silently replace them by two.

## Why the symmetry transfers still apply

The class (1) is preserved by reflecting every vertex charge
`c` to `14-c`, and by permuting the three vertex spaces. It is
not necessary to identify an individual nonsymmetric list with
its own reflection.

The physical anti-automorphism

\[
 \tau(W)=S W^T S,\qquad S e_{(i,q)}=e_{(q,i)},
\]

sends `F(i,k,s)` to `F(s,k,i)` and preserves source weights. On
the target, transpose the matrix units, reverse the cyclic leg
order, and give each resulting dual vertex basis the reflected
charges `14-c`. A transposed unit then has weight
`(14-c_column)-(14-c_row)=c_row-c_column`, as required. The two
trace reversals preserve the tensor identity. This operation
transfers type `C` to type `D` in another profile satisfying (1).

Physical reflection sends `F(i,k,s)` to
`F(7-i,14-k,7-s)` and reverses source weights. Reflect the target
charges at the same time. This transfers type `C` to type `B`,
and the composition of the two operations transfers it to type
`A`. The auxiliary summand still has no parameters at the four
excluded degrees after these transformations.

Since the type `C` proof applies to every profile satisfying (1),
each of the four types can occur on at most one leg throughout
this class. The complete cyclic classification and contradictions
in the earlier degree-13 proof now apply verbatim. This proves
the extended statement.

## Consequence for common profiles

In particular, start with multiplicity two at charges 2 through
12 and singleton multiplicities at 0, 1, 13, and 14. Raising the
multiplicity at any one of the eleven interior charges from two
to three gives 27 vertices and satisfies (1). All eleven common
profiles are excluded, including the nonsymmetric placements
and the placements at charges 2 and 12. The same reasoning
permits different interior placements on the three vertex spaces.

This is an implication of the written proof, not a conclusion
from enumerating the eleven examples. The exact coordinate
identities and determinant calculations remain those already
replayed in the linked rank-chain, symmetry, and pencil packages.
The boundary multiplicity argument was checked by another agent
in this generating session; no external independent review or
formalization has occurred.
