# Unequal vertex charges and an exact partial tensor

## Scope

The preserved width-13 candidate assigns different integer charges to the three
27-dimensional vertex spaces of `M27`. Each vertex space of the other
matrix block, `M7`, has one coordinate at each charge from 0 through 6.
The full ordinary grading-preserving target is now excluded by the
iterated homogeneous-slice Newton pruning described below. The exported
maps still give an exact embedded
`M12 direct_sum M3` partial tensor, with all other coefficients zero.
They have rank 153 on each leg; a full-target map would require rank 778.
No smaller matrix multiplication exponent follows from this package.
These profiles are historical controls, not live targets for a fit.

The profiles at charges 0 through 14 are

| Vertex space | Multiplicities |
| --- | --- |
| `V0` | `(1,1,2,2,2,3,2,2,2,2,2,2,2,2,0)` |
| `V1` | `(1,2,1,2,2,2,2,2,3,2,2,2,2,2,0)` |
| `V2` | `(1,2,2,2,2,2,3,2,2,2,2,1,2,2,0)` |

Every list has 27 entries after expansion. The target legs, in order,
are `V0 tensor V1*`, `V1 tensor V2*`, and `V2 tensor V0*`. Consequently,
their weight multiplicities are cross-correlations, rather than the
autocorrelation of one shared list. All three zero-weight target spaces
have dimension 60. No target coordinate has weight 14 or -14.

## Exact dimension and endpoint checks

If `m_i(q)` denotes the large-block multiplicity on vertex space `i`
and `n_i(q)` the small-block multiplicity, the target dimension on leg
`i` at weight `w` is

\[
 D_i(w)=\sum_q m_i(q+w)m_{i+1}(q)
       +\sum_q n_i(q+w)n_{i+1}(q),
 \qquad i\pmod3.
\]

The source weights are `i+s-k` in the common coordinate order
`F(i,k,s)`. Counting all 960 coordinates gives, at nonnegative weights,

\[
 (64,63,61,58,54,49,43,36,28,21,15,10,6,3,1).
\]

The checker recomputes all 87 signed target dimensions from the actual
three pairs of charge lists. It tests every capacity inequality
`D_i(w) <= N(w)`. It also applies the separately proved
[zero-weight minimum-slice bound](parity_structure_zero_grade_rank.md):
the uniform small block supplies a rank-one zero-weight target slice,
so every cyclic pair of zero-weight dimensions must have sum at most
121. The present sums are all 120.

For historical candidates that use the unique source extreme weights,
the checker records the endpoint degree-13 Sylvester condition. If
all vertex spaces have one coordinate at charges 0 and 14, let
`l_i=m_i(1)` and `h_i=m_i(13)`. The source pair matrix has determinant
`a^3`, and the extreme products force `a` to be nonzero at the tested
target input. Restricting a nonsingular three-by-three bilinear form
to subspaces of dimensions `d,e` leaves rank at least `d+e-3`.
Thus the necessary inequalities are

\[
 h_i+l_{i-1}+l_{i+1}\le3,
 \qquad
 l_i+h_{i-1}+h_{i+1}\le3.
\]

The current width-13 candidate has no weight-14 target units, so that
extreme-input argument does not apply. Passing any of these tests is
only a necessary condition. The elementary screen routine explicitly
records that it has not exhausted all possible obstructions. Its passing
result must be read together with the subsequent global exclusion.

## Later exclusion of the entire homogeneous-map family

The separate implementation
`parity_balancing_newton_pruning_audit.py` replays a stronger argument
that does not depend on these particular charge lists. Let `K` be a
common retained coordinate set containing the images of all three
maps. A target matrix-unit slice has rank at most 27. Since each map
is injective, its lifted slice in the coordinate-restricted source has
rank at most

\[
 R=27+2(|K|-778).
\]

The full source torus preserves every coordinate restriction. Within
one original weight, it induces arbitrary linear weights in `(i,s)`.
If a lifted homogeneous slice has a nonzero coefficient outside the
convex hull of the coordinates whose individual slice ranks are at
most `R`, an exposing torus weight and a secondary tie-break give a
coordinate-slice degeneration of rank greater than `R`. This is
impossible. Remove all such coordinates and repeat with the smaller
source and its updated codimension.

The independent replay enumerates the full source support, verifies
that coordinate slices on all three legs are partial permutation
matrices, recomputes their ranks in each retained support, and builds
each convex hull with a separate monotone-chain implementation. It gives

| Available coordinates | Lift rank bound | Retained coordinates |
| ---: | ---: | ---: |
| 960 | 391 | 922 |
| 922 | 315 | 834 |
| 834 | 139 | 468 |

The final dimension is smaller than 778, contradicting injectivity.
Thus no ordinary restriction in which every target matrix unit maps
homogeneously for the specified source torus can realize this full
target. This includes all the unequal profiles recorded here.
Ungraded restrictions and arbitrary degenerations are outside the
argument. The independent report is
`results/anisotropic-constructions-2026-10-20/parity_balancing_newton_pruning_audit.json`.
The partial-tensor verifier does not itself rerun this separate proof.

## The actual partial source maps

The construction reuses the exact monomial core from
[the common-profile seed](parity_structure_torus_seed.md), but embeds
its vertices separately in each of the three target vertex spaces.
Let

\[
 U=(0,1,6,7),\qquad V=(0,2,4),
\]

and index the twelve core vertices by pairs `(alpha,beta)` with
`0 <= alpha < 4`, `0 <= beta < 3`. The core matrix unit from
`(alpha,beta)` to `(gamma,delta)` selects the common source coordinate

\[
 F\bigl(U_\alpha,U_\gamma+V_\beta,V_\delta\bigr).
\]

Its weight is `(U_alpha-V_beta)-(U_gamma-V_delta)`. Add 6 to all these
vertex charges. They become the twelve distinct charges 2 through 13,
which exist in each current vertex list. For each list, the embedding
chooses its first vertex of the required charge. A common shift does
not change any matrix-unit weight.

The disjoint `M3` block uses

\[
 F(7-i,14-j,7),\qquad 0\le i,j<3.
\]

Its vertex charges are `2,1,0`, inside each seven-dimensional target
vertex space. The source tensor is

\[
 \sum_{i,p,r,j,q,s=0}^7
 X_{i,p+q,s}Y_{j,p,r+s}Z_{i+j,q,r}.
\]

The exported maps use the original coordinate orders on all three
legs. Their rows use the unequal target vertex embeddings: an edge
on leg `i` joins the selected vertex in `V_i` to the selected vertex
in `V_(i+1)`.

The standard-library verifier enumerates all 262,144 source terms.
The exact output contains precisely the 1,755 terms of
`M12 direct_sum M3`. Equality of the complete coefficient dictionaries
also checks every mixed or unwanted coefficient. Every map selects
153 distinct source columns into 153 distinct target rows, which
proves its stated rank. Every selected coefficient is an integer.
The squared relative residual against the complete target is exactly
`18271 / 20026`; this is a partial seed, not a near solution.

## Preserved failed neighbor-hole profile

The earlier file
`results/anisotropic-constructions-2026-10-20/parity_balancing_unequal_neighbor_hole_partial.json`
preserves a different exact partial tensor. Its full-target profile is
excluded. Its `X(+13)` and `Y(-13)` dimensions are two and three.
At the high endpoint, the source pair form is nonsingular, so the
restricted bilinear slice has rank two; the required target slice has
rank one. This is a direct rank contradiction even though that profile
passed the earlier dimension and weighted-flattening screens.

The partial tensor in that historical file remains exact. The verifier
recomputes both its tensor identity and its failed necessary screen;
it does not turn a correct partial construction into a full-target
claim. The more recent width-14 profiles discussed during exploration
also fail the later high-weight endpoint tests and are not live targets.

## Replay

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_unequal_profiles.py
python -S -m unittest discover -s tests -p test_parity_balancing_unequal_profiles.py -v
```

The generator writes
`results/anisotropic-constructions-2026-10-20/parity_balancing_unequal_profiles.json`.
Its optional `--npz PATH` argument exports the same actual maps as dense
NumPy arrays `A`, `B`, and `C`, each of shape `778 x 960`.
The exact JSON certificate and standard-library replay are authoritative.
The pruning argument and the separate replay were checked by a second
agent in this generating session; there has been no external independent
review or formalization.
