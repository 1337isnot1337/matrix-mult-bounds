# Exact endpoint seeds with boundary slack

October 21, 2026. These are exact monomial restrictions of the full
cyclic convolution source. They are small partial targets, not the
missing M27 direct sum M7 construction or a smaller exponent.

## A monotone graph construction

Choose distinct short indices i_0,...,i_(n-1) in {0,...,a-1}, and
values q_u in {0,...,b-1}, such that q_u is nonincreasing when i_u
increases. Associate vertex u with the physical pair (i_u,q_u).
On each common physical source leg send the matrix variable E_uv to
the coordinate

\[
F(i_u,q_u+i_v,q_v),\qquad\text{with coefficient }1.\tag{1}
\]

The original three source orders are X=(i,k,s), Y=(s,i,k), and
Z=(k,s,i). These permutations specify the actual three maps.

No two target matrix units share a source coordinate. Its first
coordinate fixes u, and its middle coordinate then fixes i_v and
hence v. Every matrix multiplication term occurs exactly once.

To rule out an additional trace cycle, consider three selected
variables indexed by (u,v), (v',w), (w',u'). The source equations are

\[
q_u-q_{u'}=i_{v'}-i_v,\quad
q_{v'}-q_v=i_{w'}-i_w,\quad
q_{w'}-q_w=i_u-i_{u'}.\tag{2}
\]

Put d_u=i_u-i_(u'), and similarly for v and w. Monotonicity gives
(i_u-i_(u'))(q_u-q_(u'))<=0. Combining the three such inequalities
with (2) gives

\[
d_ud_v\ge0,\qquad d_vd_w\le0,\qquad d_wd_u\ge0.\tag{3}
\]

If all three differences were nonzero, their signs would contradict
(3). If one vanishes, the associated vertices are identical because
the i indices are distinct; their q difference then vanishes. The
equations (2) propagate that equality to the other vertices. Thus
u=u', v=v', and w=w'. The image of (1) is exactly M_n.

This is a construction with n<=a, so its size alone is not an exponent
improvement. Its relevance here is that it supplies exact endpoint
maps with the boundary slack omitted by the failed stronger anchor
ansätze.

## Four endpoint vertices in A(8,8)

Take

\[
S=((0,7),(1,7),(6,0),(7,0)).\tag{4}
\]

Their physical charges i-q, shifted by seven, are 0,1,13,14. The
sixteen maps in (1) give exactly M4, including all 64 required terms
and no others. In particular, the target 13-to-1 matrix unit uses
F(6,1,7), and its reverse uses F(1,13,0). Both are boundary
coordinates. They produce the required nonzero diagonal trace
coefficient. Forcing all fully interior target units to vanish on
the boundary would lose this valid construction.

The charge +14 and -14 maps are the unique opposite physical corners
F(7,0,7) and F(0,14,0), as required by the endpoint equations.

## Eight endpoint vertices

A larger compatible partial target uses

\[
S=((0,7),(1,7),(2,7),(3,7),(4,0),(5,0),(6,0),(7,0)).\tag{5}
\]

It gives an exact M8 with charges 0,1,2,3,11,12,13,14. It contains
the four endpoint vertices in (4). The maps have 64 unit entries
per leg and the image has exactly 512 unit coefficients.

The saved export also places these vertices in the previously fixed
27-vertex charge profile, choosing the first occurrence of each
listed charge. All other rows of the 778-row M27 direct sum M7
format are zero. This is an exact partial target. It does not yet
satisfy endpoint pairings involving the remaining nineteen vertices,
and the small M7 block is absent. It is not asserted to coexist with
the separate fixed M12 direct sum M3 seed.

## Exact controls

The standard-library script `monotone_endpoint_seeds.py` checks four
formats, including complete enumeration of all 262,144 source terms
for each A88 example. It checks source-map injectivity, every resulting
coefficient against the corresponding matrix tensor, the source and
target charges, and the full-format embedding. The JSON file contains
all sparse maps and the endpoint obstruction-escaping coordinates.

Run from the repository root:

```
python -S research/ai/2026-10-20-anisotropic-constructions/monotone_endpoint_seeds.py
```

The proof and controls were produced in this generating session.
No external independent review, formalization, or priority is claimed.
