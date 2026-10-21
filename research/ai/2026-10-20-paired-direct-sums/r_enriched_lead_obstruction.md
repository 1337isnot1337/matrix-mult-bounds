# An enriched fixed leading point still has no two-scalar extension

The reduced endpoint corner R has format 16 by 18 by 18 and the exact
90-term source described in
[the corner certificate](../2026-10-20-paired-construction/m1_endpoint_corner.md).
This note excludes one proposed leading point for a Laurent map from
R direct sum D2 to M4. The two scalar leading maps may be placed
arbitrarily. The edge and corner A subspaces may also vary. The result
does **not** exclude arbitrary border-D2 repairs of R.

## Fixed leading maps and row powers

Write the native outer basis as

\[
P=(p_0,p_1,p_2,p_3)=(1-t^4,t^2,t^3,t^5),
\]

and retain the native outer indices S={0,2} as target old indices {0,1}.
The other target outer indices {2,3} are new. The endpoint multiplication
has the four independent retained products

\[
p_0w_0=e_0,\quad p_0w_1=e_2-e_5,\quad
p_2w_0=e_2,\quad p_2w_1=e_4.
\]

The corresponding output inverse has rows e0, -e5, e2+e5, e4.
Apply it on the two endpoint long legs, as in the maintained generator.
The native interior B coordinates are b00,b01,b10,b11; the interior
C coordinates are c00,c01,c10,c11. Add the old maps

\[
b_{00}\mapsto B_{0,0},\quad b_{01}\mapsto B_{1,0},\qquad
c_{00}\mapsto C_{0,0},\quad c_{10}\mapsto C_{0,1},
\]

and send the other interior coordinates to zero at leading order.
This adds a second copy of old middle channel zero. Divide the two
complete old B rows for that channel by two. The resulting leading
tensor is exactly M(2,4,2).

The prescribed lower row powers are

\[
w_A(i,k)=-[i\text{ new}]-[k\text{ new}],\quad
w_B(i,j)=[i\text{ new}],\quad
w_C(j,k)=[k\text{ new}].
\]

Only the leading coefficients of these rows enter the proof. Higher
coefficients respecting these lower powers cannot change the pole
equation for an edge A row or its first new/old cross coefficient.

The exact check reconstructs all 4,096 coefficients of the embedded
leading tensor. Its native pre-A image W0 is the four-dimensional space
of 2 by 2 matrices tensored with I4, up to coordinate permutations.
Every nonzero element therefore has rank at least four. Its native
kernel K_R is spanned by the twelve A coordinates outside S times S.

## The first-edge support gate

For every A vector in K_R, the endpoint contribution to the first
new-B/old-C cross block uses only the six native B coordinates

\[
(y,s)\in\{0,1\}\mathbin\times\{1,3,6\}.
\]

The interior contribution uses b10 and b11, and both multiply the
single old C direction C_(0,1). The first new-C/old-B cross block has
the symmetric property: at most six endpoint C directions and one
common old B direction for its interior part. These statements are
checked on every native K_R coordinate, not only a proposed corner.

Suppose the auxiliary first cross contributes at most one additional
new-B vector. In the eight-dimensional target new-B space, choose a
nonzero functional annihilating that vector and the at most six
endpoint images. The actual contracted cross block then has old-C
support at most one, hence matrix rank at most one, regardless of the
chosen edge A subspace.

For the required matrix multiplication edge, a nonzero new-B functional
is a nonzero 2 by 4 matrix X. Its A-edge/old-C slice is, after fixed
permutations, diag(X,X), of rank twice rank(X), at least two. The source
rank bound contradicts the target identity. Thus at least two effective
auxiliary new-B vectors are necessary. The symmetric argument requires
at least two effective auxiliary new-C vectors.

## All two-scalar leading placements

Let the two old scalar products be

\[
r_\nu=b_{\nu,0}\otimes c_{\nu,0},\qquad \nu=1,2,
\]

where either vector may be zero. Every linear combination of r1 and r2
has rank at most two, so their span intersects W0 only at zero.
Consequently the complete leading kernel is

\[
K_R\oplus\ker\bigl((z_1,z_2)\mapsto z_1r_1+z_2r_2\bigr).
\]

The following three cases exhaust its scalar part.

| Dimension of span(r1,r2) | Available scalar first cross | Contradiction |
|---|---|---|
| 2 | No scalar direction remains in the leading kernel. | Neither side gains the required two vectors. |
| 1 | At most one effective cross vector per side. | Each side requires two. |
| 0 | The scalar indices with nonzero old C and those with nonzero old B are disjoint. | Two indices cannot supply two vectors on both sides. |

For dimension one, if only one product is nonzero, the kernel consists
of the other scalar coordinate, which contributes at most one vector
on either side. If both products are nonzero, proportionality of two
rank-one products makes both their old B factors and their old C
factors proportional. The single scalar kernel combination therefore
has new-B/old-C cross of the form u tensor c0, and old-B/new-C cross
of the form b0 tensor v. It contributes one vector on each side.

For dimension zero, each old product vanishes. A scalar can contribute
to the first new-B cross only if its old C factor is nonzero, forcing
its old B factor to be zero. The converse applies on the other side.
Thus the effective counts have sum at most two, whereas the two gates
require a sum of at least four.

This proves the exclusion for the fixed enriched leading maps, all
two-scalar leading placements, and all edge/corner A subspaces in the
stated valuation chart. No numerical fit was launched at this point.
Changing the leading R maps or the lower row powers is outside the
claim. The general border-D2 question remains open in this project.

## Exact verification

The verification uses only integer and rational arithmetic in the
Python standard library. It checks all leading coefficients, the full
native leading image, both endpoint support lists, both interior
opposite-support lines, and every coefficient of the target slice
identity diag(X,X). The scalar case analysis is the proof above.

```sh
python -S research/ai/2026-10-20-paired-direct-sums/r_enriched_lead_obstruction.py
python -S -m unittest discover -s tests -p test_r_enriched_lead_obstruction.py -v
```

This is a project-derived obstruction with internal checks. It has not
received external mathematical review and yields no smaller exponent.
