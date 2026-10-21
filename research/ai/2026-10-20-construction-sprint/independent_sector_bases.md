# The growth criterion permits independent shared bases in each sector

October 21, 2026. Conditional construction criterion; no smaller exponent is
established here.

The canonical fat-point target is stronger than the target structure needed
by the [growth argument](../2026-10-20-concavity-equivalence/fatpoint_growth_route.md).
The blocks may use different invertible identifications of their shared
space. This observation changes the construction problem but does not supply
the missing unbounded family.

## A larger target class

Fix `m>=1`, put `D=m-1` and `N=m(m+1)/2`, and choose matrices
`H_p in GL_m(C)` for `p=0,...,D`. Define

\[
\widetilde T_m=\sum_{p=0}^{D}\sum_{a=0}^{p}\sum_{c=0}^{D-p}
\sum_{i=0}^{D}(H_p)_{i,a+c}
X_iY_{a,p-a}Z_{c,D-p-c}.
\]

The two nonshared spaces are split into matched, disjoint degree blocks.
The block indexed by `p` is `C(p+1,m-p)` with its output as the shared
factor, followed by the invertible map `H_p` on that factor. Its character
value is therefore unchanged. No common map on the whole shared factor is
asserted, and the full tensor need not be isomorphic to canonical `T_m`.

Every nonshared flattening has rank `N`: each convolution block is concise,
and its two nonshared spaces are disjoint from those of the other blocks.
The shared flattening has rank `m`, already witnessed by an endpoint block.
Tensoring with `B_X(k)` multiplies the nonshared flattening ranks by `k`.

## The same conditional inequality

Suppose actual degenerations exist along an unbounded sequence:

\[
C(a_m,B_m)\unrhd\widetilde T_m\otimes B_X(k_m),\qquad
\limsup\frac{a_m}{m}\le\sigma,\quad
\limsup\frac{B_m}{k_mN}\le\rho.
\]

Use exactly the character conventions of the linked growth argument. The
shared-leg entropy inequality is applied to the matched nonshared blocks.
Invariance under the invertible `H_p` leaves every block value unchanged, so
the resulting lower bound is again

\[
P(a_m,B_m)\ge k_m\sum_{u=1}^{m}P(u,m+1-u).
\]

More explicitly, let `p_h` be the dot-product exponent on character leg `h`
and put `t=(p_1+p_2+p_3)/3`. For each of the six orientations, the
shared-leg inequality uses power `1/p_h` on the blocks. Weighted Holder
with weights `p_h/(6t)` combines the six inequalities: each leg occurs
twice, so the weights sum to one. Its product inside each summed term is
exactly the symmetrized powered block profile. The factors from `B_X(k_m)`
give the common multiplier `k_m`. Thus no simultaneous shared change of
basis is needed in the symmetrization either. The relevant characters near
the exponent endpoint have positive `p_h`; if one were zero, the usual
rank bound `p_h<=1` would give total exponent at most two.

The full nonshared rank still forces `B_m>=k_mN`. All remaining steps of the
[source-aspect extension](shared_dimension_slack.md) concern only this
inequality, the source dimensions, and the homogeneous profile. They yield
the same conditional necessary inequality

\[
\rho\sigma^{d-1}d(d+1)2^d\ge8,\qquad d=1/t.
\]

Thus the same unbounded cost condition
`rho sigma^(1/3)<9/(7 cuberoot(2))` would force an exponent improvement.
The premise remains unconstructed. The rational exponents in the linked
criterion remain conditional consequences, not established bounds.

## What a certificate must establish

A proposed construction must cancel every negative Laurent coefficient and
every unwanted constant coefficient. Each retained degree block must be
identified with its stated convolution tensor by actual invertible maps.
Matching dimensions, flattening ranks, or a numerical fit alone do not give
that identification. In particular, the shared maps `H_p` must have full rank.

Natural degree weights, constant on the entire shared factor, permit these
independent maps. A grading that gives different weights to different shared
coordinates generally does not preserve a dense `H_p`; those are separate
search templates unless weight compatibility is proved.

This is an application of the existing character and shared-leg machinery,
whose external sources are attributed in the linked notes. The argument was
checked within the same AI research session; external review and formal
verification remain outstanding.

A second agent independently checked the six-orientation Holder weights,
the shared-output orientation, and both full nonshared flattening ranks.
