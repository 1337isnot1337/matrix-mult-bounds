# Isotropic lift of shared-leg entropy constraints

Date: October 23, 2026. Research direction: R5.

This note studies a candidate finite joint oriented-lift model for
[research direction R5](research_directions.md#r5-compare-external-formulations-before-duplicating-work).
It establishes an exact equivalence for the entropy constraints defined
below. It does not construct a tensor character or a block-identity graph
certificate.

## Constraint model

Use the convention 0 log 0 = 0.

Fix `t > 0` and a finite set of vertices `V`. A scalar assignment is a real
number `s_v` at each vertex. For each selected matched decomposition `D` of a
vertex `v` into vertices `u_1,...,u_M`, and each probability vector
`q=(q_1,...,q_M)`, let `L(D)` be its shared leg, which may be any of `X`, `Y`,
or `Z`. The scalar model imposes

\[
s_v \ge H(q)+\sum_{h=1}^M q_h s_{u_h},\qquad
H(q)=-\sum_{h=1}^M q_h\log q_h.
\]

The joint oriented model assigns numbers `ell_{pi,v}` for the six leg
permutations `pi` and a shared exponent vector `(p_X,p_Y,p_Z)` with
`p_X+p_Y+p_Z=3t`. For each decomposition `D`, the permutation `pi` determines
the exponent `p_{pi,L(D)}` of its shared leg. It imposes

\[
\ell_{\pi,v}\ge p_{\pi,L(D)}H(q)+\sum_{h=1}^M q_h\ell_{\pi,u_h},
\qquad
\frac{1}{6}\sum_{\pi\in S_3}\ell_{\pi,v}=t s_v.
\]

The model in this note contains these entropy inequalities and mean
normalizations only. It does not impose extra orientation-specific bounds on
individual `ell_{pi,v}` or on the individual `p` coordinates.

## Exact projection theorem

For any fixed finite list of matched decompositions, a scalar assignment
`(s_v)` satisfies all scalar inequalities if and only if it has a feasible
joint oriented lift under the constraints above.

**Joint lift implies scalar feasibility.** Average an oriented inequality over
all six permutations. For any selected shared leg `L(D)`, each coordinate of
`(p_X,p_Y,p_Z)` occurs twice as `p_{pi,L(D)}`, so

\[
\frac{1}{6}\sum_{\pi\in S_3}p_{\pi,L(D)}
=\frac{p_X+p_Y+p_Z}{3}=t.
\]

The mean normalizations then give

\[
t s_v\ge tH(q)+t\sum_hq_hs_{u_h}.
\]

Dividing by `t` yields the scalar inequality.

**Scalar feasibility implies joint lift.** Set

\[
p_X=p_Y=p_Z=t,\qquad \ell_{\pi,v}=t s_v
\quad\text{for every }\pi,v.
\]

Every orientation and every selected shared leg now has `p_{pi,L(D)}=t`, and
each oriented inequality is the corresponding scalar inequality multiplied
by `t`. The mean normalization holds with equality. Thus this is a feasible
joint lift, even when the graph mixes decompositions sharing different legs.

## Consequence and scope

Within this constraint model, requiring one common set of six oriented values
across multiple decompositions, even when those decompositions share different
legs, does not strengthen the scalar entropy system:
the projection of its feasible assignments onto `(s_v)` is exactly the
scalar feasible set. In particular, a finite graph encoded only by these
constraints cannot reject a scalar profile that satisfies the same selected
scalar inequalities by asking whether that profile has an oriented lift.

For a convolution vertex `v=C(a,b)`, setting `s_v=log P(a,b)` makes the mean
normalization exactly
`(1/6) sum_pi ell_{pi,v}=t log P(a,b)`. The statement therefore applies to
any candidate scalar profile on the graph whenever it satisfies every
matched-decomposition inequality selected for that graph. It does not assert
that `P_*` satisfies arbitrary matched-decomposition inequalities.

The equivalence does not include the separate obligations for exact
`SharedLegIdentity` maps, matrix shapes, source border rank, terminal
symmetrization, or edge-weight balances in a block-identity certificate.
Nor does it rule out a stronger model that constrains individual orientation
values using additional spectral facts, fixes a non-isotropic exponent vector,
or links orientation values across tensors in a way absent from the model
above. No actual character, qualifying graph, smaller exponent, or
independent review is established.
