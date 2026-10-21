# How much source-weight mixing the ordinary target requires

## Result and scope

Consider an ordinary restriction

\[
 A(8,8)\longrightarrow M_{27}\oplus M_7.
\]

Every target leg has dimension `778`. Fix a matrix-unit basis on each
leg, and use the source weight

\[
 \operatorname{wt}F(i,k,s)=i+s-k.
 \tag{1}
\]

**On at least two target legs, at least 19 matrix-unit images must each
have nonzero components in three or more distinct source weights.**
The weights need not be consecutive, and the allowed pair of weights
for any remaining image may depend on that individual matrix unit.
No target charge profile or equivariance assumption is made here.

This extends the homogeneous-image exclusion in
[`torus_support_peeling.md`](torus_support_peeling.md). In particular,
mixing only two source weights per matrix unit on two legs cannot
produce the target, even when the third map is unrestricted. Leaving
two legs unrestricted does not give a contradiction from the present
calculation. General ungraded maps and arbitrary singular degenerations
remain open in this work.

The companion construction is an exact change of basis of the known
smaller restriction `A(8,8) -> M12 direct_sum M3`. Its three maps each
have 36 images with three source weights, and it uses cancellations
between positive and negative weight offsets. It is a positive control
for those cancellations, not a new larger matrix target or a smaller
matrix multiplication exponent.

The mixed-grading proof was checked by another agent in this generating
session. The primary homogeneous proof also has a separate exact replay.
There has been no external independent review or formalization.

## Separate masks and inherited injectivity

Use the common source coordinates and tensor

\[
 F(i,k,s),\quad 0\leq i,s<8,\quad 0\leq k<15,
 \qquad
 S=\sum_{i,p,r,j,q,s=0}^{7}
 X_{i,p+q,s}Y_{p,r+s,j}Z_{r,i+j,q}.
 \tag{2}
\]

Let `K_X,K_Y,K_Z` be possibly different sets of source coordinates
known to contain the three actual parameter-map images. Restrict (2)
to their spans and call the resulting tensor `S_K`.

Suppose the three parameter-map domains have dimensions `d_X,d_Y,d_Z`
and the maps are injective. If a domain basis vector `e` on leg `i`
has target slice rank at most `r`, deleting the complementary row and
column spaces gives

\[
 \operatorname{rank}S_K(J_i(e))
 \leq r+\sum_{j\ne i}(|K_j|-d_j)=:R_i.
 \tag{3}
\]

The full target is concise, so all three hypothetical full parameter
maps are injective. Later we restrict two target legs to the span of
selected matrix units. **Those restricted parameter maps remain
injective because they are restrictions of the hypothetical full
injective maps.** The restricted target tensor need not itself be
concise. Conciseness of that restricted tensor is not used. Its
matrix-unit slice ranks can only decrease, so `r=27` remains valid.

Every coordinate slice of (2) is a partial permutation matrix. That
property survives every separate coordinate restriction. Thus its
rank is exactly the number of source terms through that coordinate
whose other two coordinates remain in their respective masks. The
replay checks all three pair projections of all `8^6=262144` source
terms before using these counts. Separate masks require separate
rank arrays; equality of the arrays is not assumed.

## Why two weights can still be separated

The weights (1) sum to zero on every source term. Their diagonal torus
therefore preserves `S`, every coordinate mask, and the rank of a slice
up to invertible row and column transformations. If

\[
 F=F_u+F_v,\qquad u<v,
\]

then a normalized torus limit isolates `F_u`; reversing the torus
isolates `F_v`. Specialization cannot increase matrix rank, so

\[
 \operatorname{rank}S_K(F_u),\quad
 \operatorname{rank}S_K(F_v)
 \leq\operatorname{rank}S_K(F).
 \tag{4}
\]

This uses ordinary matrix rank over a Laurent rational-function field,
followed by specialization. It does not assume a numerical limit of a
putative algorithm. With three weights, the middle component need not
be a torus limit; (4) cannot simply be asserted for it.

There is also a three-parameter diagonal source torus. In common
coordinates its leg weights can be written

\[
\begin{aligned}
 d_X(i,k,s)&=a i+b k+c s,\\
 d_Y(i,k,s)&=-b i-c k+a s,\\
 d_Z(i,k,s)&=c i-a k-b s.
\end{aligned}
\tag{5}
\]

Their sum on every term of (2) is zero. On a fixed primary weight,
`k=i+s-w`, this torus realizes every linear functional on `(i,s)`
on each leg. It exposes each vertex of the Newton polygon of a
homogeneous slice. The rank of every exposed coordinate slice is
at most the rank of that slice.

Consequently, for a selected leg whose basis images have at most two
weights, both components of every image lie in the weightwise convex
hulls of

\[
 \{F(i,k,s)\in K_i:
      \operatorname{rank}S_K(F(i,k,s))\leq R_i\}.
 \tag{6}
\]

All coefficients outside these hulls vanish. Linearity places the
whole selected domain image in the new mask. Unselected masks are
left unchanged. Equation (3) then applies with the smaller masks,
so the rank budget and hulls can be recomputed.

## Exact separate-mask calculations

The companion code generates all source terms and uses integer
monotone-chain convex hulls. It imports the separate source/hull
implementation in `parity_balancing_newton_pruning_audit.py`, not the
primary peeling implementation. The certificate contains every removed
coordinate and the SHA-256 digest of every resulting mask.

With all three domain dimensions equal to `778`, the results are:

| Selected legs with at most two weights per image | Successive mask dimensions | Result of this screen |
| --- | --- | --- |
| One | `(960,960,960) -> (922,960,960)` | Stable; no exclusion |
| Two | `(960,960,960) -> (922,922,960) -> (834,834,960) -> (724,724,960)` | Excluded: `724<778` |
| Three | `(960,960,960) -> (922,922,922) -> (834,834,834) -> (468,468,468)` | Excluded: `468<778` |

The selected-leg rank budgets in the two-leg case are `391,353,265`.
Cyclic symmetry makes this apply to any pair of legs.

Using the full three-dimensional coordinate Newton hull on an
unrestricted leg does not improve these particular rounds. Its mask
remains the whole box `[0,7] x [0,14] x [0,7]`. The eight box corners
have full-source coordinate-slice rank `64`, which cannot increase
under restriction. All applicable unrestricted-leg budgets before
the recorded contradiction are at least `139`. The eight corners
are therefore admissible, and their hull is already the whole box.

For the quantitative statement, suppose two legs each have at least
`760` matrix-unit images using at most two weights. Keep any `760`
such units on each leg and all `778` units on the third leg. The
inherited injectivity discussed above permits (3) with domain
dimensions `(760,760,778)`. The exact rounds are

| Selected-leg mask size before | Rank budget on each selected leg | Size after |
| ---: | ---: | ---: |
| 960 | 409 | 922 |
| 922 | 371 | 884 |
| 884 | 333 | 834 |
| 834 | 283 | 756 |

The third mask stays `960`. The final `756<760` contradicts
injectivity. Hence at most one leg can have `760` or more such images.
At least two legs each have at most `759`, and therefore at least
`778-759=19` images with three or more weights.

The `759`-row control stops at `(922,922,960)` and does not give a
contradiction. This establishes a limit of this particular count
screen, not sharpness of the necessary condition for actual maps.

## A globally one-sided weight band does not suffice

Give target vertex spaces arbitrary integer charges, so the target
tensor is supported on triples whose leg weights sum to zero.
Suppose every matrix unit of target weight `w` maps only to source
weights `w+d` with `d>=0`, on all three legs. For a target triple of
total weight zero, a source contribution requires `d_X+d_Y+d_Z=0`.
All three offsets must therefore be zero.

The grade-preserving parts of the three maps alone reproduce every
target coefficient of total weight zero. They vanish on all other
triples by source grading, as does the target. They would thus give
the forbidden homogeneous restriction. The same argument applies
when every offset is nonpositive, or after consistent leg shifts
whose sum is zero. A useful ordinary construction must escape this
global one-sided condition as well as the two-weight count bound.

## Exact balanced three-weight construction on the smaller target

The stored positive control starts with the existing exact monomial
restriction `A(8,8) -> M12 direct_sum M3`. Its twelve large-block
vertices are `(alpha,beta)` with

\[
 U=(0,1,6,7),\qquad V=(0,2,4),
 \qquad q_{\alpha,\beta}=U_\alpha-V_\beta.
\]

In common coordinates the image of the large-block matrix unit is

\[
 J(E_{(\alpha,\beta),(\gamma,\delta)})
 =F(U_\alpha,U_\gamma+V_\beta,V_\delta).
 \tag{7}
\]

The three small-block vertices have charges `0,-1,-2`; their unit
images are `F(7-i,14-j,7)`. Each leg uses the same common formula,
with the original source coordinate orders exported explicitly.

The large-block charges are the twelve distinct integers `-4,...,7`.
Pair consecutive charges as

\[
 (-4,-3),\ (-2,-1),\ (0,1),\ (2,3),\ (4,5),\ (6,7).
\]

Let `N` contain one vertex matrix unit for each pair. Orient the
first three from higher to lower charge and the last three from
lower to higher charge. The pairs are disjoint, so `N^2=0`.
Put `G=I+N`, with `G^{-1}=I-N`, and replace every large-block leg map by

\[
 J'(A)=J(GAG^{-1}).
 \tag{8}
\]

Simultaneous conjugation preserves `tr(ABC)`, so (8) preserves the
exact target. Expanding

\[
 GE_{ij}G^{-1}=E_{ij}+NE_{ij}-E_{ij}N-NE_{ij}N
\]

gives at most four source coordinates and at most three consecutive
source weights per image. The actual exported maps have the following
counts on each leg:

| Distinct source weights in an image | Number of matrix-unit images |
| ---: | ---: |
| 1 | 45 |
| 2 | 72 |
| 3 | 36 |

Each map has `333` integer nonzero entries and rank `153`. The rank
verifier explicitly applies the inverse target conjugation and
recovers all `153` distinct monomial rows of (7) and the small block.
The full replay enumerates all `262144` source terms and recovers
exactly the `12^3+3^3=1755` target terms, with every other coefficient
zero. It does not infer this identity from the construction label.

The actual source-minus-target offsets include `-2,-1,0,1,2`.
Deleting every off-grade coefficient from these stored maps changes
`648` tensor coefficients, each by magnitude one, for squared error
`648`. Thus both signs participate in the exact fixed-basis identity.
The conjugation can of course be reversed: this remains a change of
basis of the smaller known construction. It does not certify the
much larger `M27 direct_sum M7` target.

## Reproduction

Run from the repository root:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_mixed_grading.py
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_three_weight_seed.py
python -S -m unittest discover -s tests -p 'test_parity_balancing_mixed_grading.py'
```

Both scripts use only the Python standard library. The mixed-grading
JSON records recomputed masks for all five controls. The seed JSON
contains the complete three actual sparse maps, the vertex change of
basis, and the recomputed full tensor report. Tests reject changed
nonzero map coefficients and all-zero maps, and recompute the maps'
weight support and ranks instead of trusting stored report fields.
