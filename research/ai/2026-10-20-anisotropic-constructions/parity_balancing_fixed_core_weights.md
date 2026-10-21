# A graded dimension test for keeping a matrix core fixed

## Result and scope

Let a graded source tensor have third-leg dimension `N_w` at weight w.
Fix two maps for a specified matrix multiplication core inside the
desired target. Contracting those two core maps defines a linear map
`Phi_w` from the source's third-leg weight space to bilinear forms on
the two core legs. Write `r_w=rank(Phi_w)`, and let `c_w` be the number
of third-leg core matrix units at that weight.

Every concise graded extension to a target with third-leg dimensions
`D_w` must satisfy

\[
 \boxed{D_w\le N_w-r_w+c_w.}
\]

This is a condition on **keeping those two core maps fixed**. It does
not exclude a larger restriction obtained by moving the core maps,
changing the torus profile, or using a degeneration. The test applies
with any cyclic choice of the two fixed legs.

For the specified A(8,8) to M27 plus M7 torus profile, the source has
64 coordinates at weight zero and the target needs 60. Several exact
small matrix restrictions fail this extension test even when the sum
of the dimensions passes a weaker, ungraded test:

| Specified exact core | Total pair rank | Ungraded target-leg bound | Pair rank at weight zero | Target weight-zero bound |
| --- | ---: | ---: | ---: | ---: |
| Endpoint M2 | 6 | 958 | 4 | 62 |
| Endpoint M4 | 44 | 932 | 10 | 58 |
| Monotone M6 | 138 | 858 | 18 | 52 |
| M6 with repeated short indices | 192 | 804 | 28 | 42 |
| Monotone M8 | 312 | 712 | 28 | 44 |

The endpoint M2 passes all of these necessary weight inequalities; no
extension is asserted. The listed M4, both M6 controls and M8 fail.
The M4 also fails at weights +12 and -12, where its extension bound is
4 while the target requires 5. M8 already fails the ungraded bound,
since the full target-leg dimension is 778.

The M4 conclusion means that the exact initial M4 row maps in an
endpoint seed cannot all remain fixed on two legs while constructing
the stated torus target. Free coefficients in its target rows must
be allowed to move. Separately, the particular first boundary choices
also have additional slice obstructions; this dimension test does not
claim that moving only the free columns repairs those boundaries.

All table entries are exact integer support counts. The root worker
obtained the M4, monotone M6 and M8 counts separately, and the generating
worker obtained the same graded failures before exchanging the full
tables. These results were checked by a second agent in this generating
session; no external independent review or formalization has occurred.
No exponent improvement is established.

## Proof of the general inequality

Let `A_0` and `B_0` denote the two target core-leg spaces. Keeping their
source maps fixed defines

\[
 \Phi_w:C^{\mathrm{source}}_w\longrightarrow A_0^*\otimes B_0^*.
\]

Suppose a complete target restriction exists, and let `J_w` be its
third-leg lift. A concise target forces `J_w` to be injective: a vector
in its kernel would annihilate the target tensor on that leg.
Consequently the image `U_w=J_w(C^{\mathrm{target}}_w)` has dimension
`D_w`.

In a matrix multiplication tensor, fixing the first two variables to
matrix units supported on the chosen core vertices gives a bilinear
form that depends only on the third matrix unit with both vertices in
that core. Every such third unit occurs, and these forms are linearly
independent. Variables in the other target vertices or direct-sum
blocks give zero. Therefore

\[
 \dim\Phi_w(U_w)=c_w.
\]

Rank-nullity on `U_w`, followed by inclusion in the source kernel,
gives

\[
\begin{aligned}
 D_w
 &=\dim(U_w\cap\ker\Phi_w)+\dim\Phi_w(U_w)\\
 &\le (N_w-r_w)+c_w.
\end{aligned}
\]

Summing over weights yields the ungraded bound
`D <= N-r+n^2` for an M_n core. A failure at one weight can be much
stronger than this sum. The proof requires the two specified core
subspaces and maps, not a fixed completion of any remaining target
row. In particular the third core map may vary.

## Why the rank is a coordinate count for these controls

Use common source coordinates

\[
 W(F)_{(i,q),(p,s)}=F_{i,p+q,s}
\]

for A(a,b), with `0 <= i,p < a` and `0 <= q,s < b`. Given two common
source coordinates `X=(i,k,s)` and `Y=(p,u,j)`, there is at most one
third source coordinate:

\[
 q=k-p,\qquad r=u-s,\qquad Z=(r,i+j,q).
\]

It occurs with coefficient one exactly when `0 <= q < b` and
`0 <= r < a`. Thus a pair of monomial core selectors induces either
the zero functional or one coordinate functional on the third source
leg. The rank is exactly the number of distinct resulting third-leg
coordinates. Partitioning that set by `weight(i,k,s)=i+s-k` gives each
`r_w` without Gaussian elimination, approximation or a field-dependent
rank assumption.

For a list of physical vertices `S={(i_u,q_u)}`, each tested core uses

\[
 E_{uv}\longmapsto F(i_u,q_u+i_v,q_v).
\]

The following lists give all five controls. The last two coordinate
lists use the same 8 by 8 physical space as the others:

| Core | Physical vertices, in core matrix order |
| --- | --- |
| Endpoint M2 | `(0,7), (7,0)` |
| Endpoint M4 | `(0,7), (1,7), (6,0), (7,0)` |
| Monotone M6 | `(0,7), (1,7), (2,7), (5,0), (6,0), (7,0)` |
| M6 with repeated short indices | `(0,7), (1,7), (0,5), (7,2), (6,0), (7,0)` |
| Monotone M8 | `(0,7), (1,7), (2,7), (3,7), (4,0), (5,0), (6,0), (7,0)` |

The monotone controls are related to `monotone_endpoint_seeds.md`.
The repeated-index M6 is a separate exact coordinate construction;
it is verified directly and does not rely on the distinct-first-index
hypothesis in that note. Its 216 matrix multiplication terms are exact.
Its full fixed core nevertheless fails the graded extension bound.

## Certificate and replay

`parity_balancing_fixed_core_weights.py` and the corresponding results
JSON contain all source maps, core vertex embeddings and supported
third-leg coordinates for every weight. The checker validates actual
sparse maps and their torus weights. It then computes the unique-third-
coordinate formula for every core pair and compares the entire core
tensor with M_n. A second contraction enumerates all 262,144 A(8,8)
source terms and checks the same result independently.

The complete exported cases account for every one of the `n^6` target
coefficients, including zero coefficients. Recorded rank or exclusion
metadata is not used to recompute the answer. The M2 case provides a
control in which no exclusion is returned.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_fixed_core_weights.py
python -S -m unittest discover -s tests -p test_parity_balancing_fixed_core_weights.py -v
```

The result is saved at
`results/anisotropic-constructions-2026-10-20/parity_balancing_fixed_core_weights.json`.

The next construction must permit the relevant core lifts or boundary
channels to change. These tests do not exclude an M6 tensor identity
with different, mixed source maps or a compatible larger restriction
that moves all three core maps.
