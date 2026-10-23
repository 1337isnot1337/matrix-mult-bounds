# Interfaces between the spectral, block-identity, and separation routes

Date: October 23, 2026. Local baseline: `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.

This is a dependency map for research direction R5, not a reproof of the
external results. The local claims remain at their recorded status. In
particular, no result below improves the exponent past the external
`omega <= 9/4` bound.

## The three routes

| Route | Object that carries the argument | Bridge to an exponent bound | What must be supplied for a strict improvement |
| --- | --- | --- | --- |
| Spectral | One actual tensor character, its three dot-product exponents, and its six leg orientations. The 9/4 proof passes to a symmetrized profile on convolution tensors. | Character inequalities give concavity and shifted tripling; the discrete-growth lemma bounds the character parameter, and the detecting-character argument transfers that bound to matrix multiplication. | A constraint on actual characters beyond the scalar system. The local `P_*` profile satisfies that system, including the rank upper bound at `t=3/4`, but is not known to come from a character. |
| Block identities | A finite directed graph of nonzero tensors, exact shared-leg identities with matrix shapes, a source border-rank bound, nonnegative edge weights satisfying the vertex balances, and a terminal whose symmetrization is a square matrix tensor. | The pinned Filmus theorem bounds `formalOmega F` by `3 log(r)/(log(d)+log(L))`, where `r` is the source border-rank bound and `L` is weighted terminal inflow. | A graph certificate with all tensor identities and balances, plus `(dL)^3 > r^4`. The numerical inequality alone is insufficient. |
| Polynomial separation | A matched family `A_h` sharing one input space, with independent matched sectors on the other two spaces. | Over a field with at least `M+n-1` distinct elements, Lü's degeneration $A^{\oplus(M+n-1)}\rightsquigarrow\bigoplus_h(A_h\otimes B_X(n))$ reduces the finite source-copy cost; after tensor powers it gives the same asymptotic shared-leg entropy inequality. | The copy-count reduction alone does not change the asymptotic exponent. A separate character inequality or a block-identity certificate is still needed. |

The block-identity theorem is stated over a field `F`, with finite tensors over
its algebraic closure. Its pinned `identities_to_exponent` declaration
requires nonzero tensors at every vertex; distinct source and terminal vertices
`s` and `t`; no edge leaving `t`; exact `SharedLegIdentity` maps with source
and output matrix shapes on every edge; a symmetrized terminal isomorphic to
`square d` for `d>=2`; and a source tensor of border rank at most `r` for
`r>=1`. For edge weights `mu_e>=0`, write `sigma(e)` for the parent, `w(e,i)`
for child `i`, and `D(e)`, `Dout(e,i)` for the corresponding shapes. The
nonterminal balance condition is

\[
\sum_{e:\sigma(e)=v}\operatorname{vol}(D(e))\mu_e
-\sum_{e,i:w(e,i)=v}\operatorname{vol}(Dout(e,i))\mu_e
\leq \mathbf 1_{v=s}\qquad(v\ne t).
\]

The terminal inflow is
`L = sum_{e,i:w(e,i)=t} vol(Dout(e,i)) mu_e` and must satisfy `L>1/d`.
These are exact feasibility obligations, not consequences of assigning a
scalar value to each convolution size.

## What survives symmetrization

For an actual character, let `lambda_pi` be its six leg orientations,
`p_{pi,X}` the dot-product exponent of the common leg in orientation `pi`,
and

\[
t=(p_X+p_Y+p_Z)/3,\qquad
\mathcal P(T)=\left(\prod_{\pi\in S_3}\lambda_\pi(T)\right)^{1/(6t)}.
\]

For a matched sum `A = sum_h A_h` with shared leg `X`, pairwise disjoint
coordinate spaces on the other two legs, and no unmatched cross terms, the
shared-leg entropy inequality for one orientation is

\[
\lambda_\pi(A)\ \ge\
\exp\!\bigl(p_{\pi,X}H(q)\bigr)
\prod_h\lambda_\pi(A_h)^{q_h},
\qquad H(q)=-\sum_hq_h\log q_h.
\]

Applying the finite-separation proposition to tensor powers with rational
sector frequencies tending to `q` gives the entropy inequality. Taking the
geometric mean of the six
oriented inequalities preserves the statement: each leg appears as the
shared leg in two orientations, so `(1/6) sum_pi p_{pi,X} = t`. Therefore

\[
\mathcal P(A)\ \ge\
\exp(H(q))\prod_h\mathcal P(A_h)^{q_h}.
\]

This is a constraint on actual characters and arbitrary matched families.
The scalar array `P(a,b)` records only `mathcal P(C(a,b))`; it has no entries
for general `A` or its sectors. The local tripling inequality is one special
case. The product-filtration and direct-sum notes already use restricted
families of these constructions, so the entropy inequality itself is not a
new local result. A proposed common assignment of all six oriented values is
not stronger at the entropy-only level; the exact projection result below
identifies the additional tensor data a successful route must retain.

OpenAI's finite-separation proposition uses `5M` copies for `M` matched
sectors. Lü proves the replacement
`A^{\oplus(M+n-1)} \rightsquigarrow \bigoplus_h(A_h\otimes B_X(n))` when
the field has at least `M+n-1` distinct elements. For an infinite-field
character, this gives

\[
(M+n-1)\lambda(A)\geq n^{p_X}\sum_{h=1}^M\lambda(A_h).
\]

Taking `n=M` lowers the count to `2M-1`; the asymptotic character entropy
inequality remains the same. Polynomial separation thus improves the finite
construction interface and its field requirements, while the spectral route
still supplies the same 9/4 endpoint.

## Candidate constraint after the entropy-only test

At each graph vertex `v`, the finite oriented model assigns six values
`ell[pi,v]` and uses a common exponent vector `(p_X,p_Y,p_Z)`. Write
`s_v=(1/(6t)) sum_pi ell[pi,v]`; for a convolution vertex this is
`log P(a,b)`. For a selected matched decomposition `D` with shared leg
`L(D)` and probability vector `q`, it imposes

\[
\ell_{\pi,v}\geq p_{\pi,L(D)}H(q)+\sum_hq_h\ell_{\pi,A_h},
\qquad \frac16\sum_{\pi}\ell_{\pi,v}=t s_v.
\]

The [exact projection theorem](oriented-lift-relaxation.md) shows that these
entropy constraints alone add no scalar restriction, even when a finite graph
mixes decompositions sharing different legs. Averaging any lift gives the
scalar inequalities. Conversely, any scalar-feasible assignment lifts by
setting all orientations equal and choosing `p_X=p_Y=p_Z=t`. Thus a search
for scalar-profile infeasibility in this entropy-only lift is already decided:
it cannot exclude a profile that satisfies the same selected scalar
inequalities.

The candidate absent from the scalar profile model is a qualifying
block-identity certificate. It needs nonzero vertex tensors, every exact
`SharedLegIdentity` and matrix shape, a source border-rank bound `r`,
nonnegative edge weights satisfying the nonterminal balance inequalities,
and a terminal whose symmetrization is the square matrix tensor of size `d`.
If `L` is the weighted terminal inflow, the pinned Filmus theorem assumes
`L>1/d` and gives

\[
\operatorname{formalOmega}(F)\leq
\frac{3\log r}{\log d+\log L}.
\]

Since `dL>1`, this gives a strict improvement on `9/4` exactly when
`(dL)^3>r^4`. The exact Filmus convolution graph below does not meet that
threshold. The next research task is to add certified tensor identities that
escape its scalar edge barrier, or derive another tensor-level constraint that
excludes the critical spectral behavior. No exponent improvement is claimed.

## Exact Filmus convolution graph and its scalar barrier

At Filmus's pinned commit, the neighboring-length and tripling providers do
instantiate actual `SharedLegIdentity` records. Write `C(r,b)` for the
convolution tensor. For `r>=1` and `b>=2`, the neighbor identity has source
shape `(1,1,2)` (volume `2`) and two children `C(r,b+1)` and `C(r,b-1)`,
each with output shape `(1,1,1)` (volume `1`). Its value inequality is

\[
2x(C(r,b))\geq x(C(r,b+1))+x(C(r,b-1)).
\]

For `r>=2`, the tripling identity has source `C(r,4r-1)`, source and output
shapes of volume `1`, and three children isomorphic to `C(r,r)`. Its middle
child uses the `xzy` output permutation, which preserves the reversal in the
source declaration. It gives

\[
x(C(r,4r-1))\geq 3x(C(r,r)).
\]

These are not just formal sector sums: the pinned provider proves the source
degenerations and the independent block identifications needed by
`SharedLegIdentity`. The same pinned source gives the boundary symmetry
`x(C(r,r-1))=x(C(r-1,r))`, a source border-rank bound `2a-1` for `C(a,a)`
over an infinite field, and
`symmetrize(C(2,1)) \cong M(2,2,2)`. Thus the family supplies an explicit
graph from `C(a,a)` to the terminal `C(2,1)`.

It still cannot meet the strict graph threshold using only these edge rows.
Let

\[
h_1=1,\qquad h_{a+1}=\left(1+\frac{1}{3a}\right)h_a,
\qquad P_*(a,b)=h_{\min(a,b)}
  \left(\max(a,b)+\frac{\min(a,b)-1}{2}\right).
\]

This is the positive potential already recorded in the
[scalar-profile note](../research/ai/2026-10-20/research_note.md). It obeys
the graph rows: for `2<=b<=r`,

\[
2P_*(r,b)-P_*(r,b-1)-P_*(r,b+1)
 =\frac{2h_b(r-b)}{3b(3b-2)}\geq0,
\]

and for `b>=r` the neighbor row is equality. The boundary symmetry follows
from symmetry of `P_*`, and
`P_*(r,4r-1)=3P_*(r,r)`. Consequently, any nonnegative weighted combination
of just these graph rows, with source `C(a,a)` and terminal `C(2,1)`, has
terminal inflow at most: multiply each row by its edge weight and sum, then
apply the certificate balances to this positive potential. The resulting cap is

\[
\frac{P_*(a,a)}{P_*(2,1)}
 =L_a=\frac{3a-1}{4}\prod_{j=1}^{a-1}
  \left(1+\frac{1}{3j}\right).
\]

Here `P_*` is a feasible potential for the edge inequalities, not an
assertion that it is an actual tensor value. In particular, it bounds what
the selected graph rows alone can certify. For every `a>=2`, this ratio is
strictly below the required threshold:

\[
\frac{(2L_a)^3}{(2a-1)^4}
 =\frac{(3a-1)^3h_a^3}{8(2a-1)^4}<1.
\]

For `a>=4`, `h_a^3<=e(a-1)`, `2a-1>=7a/4`, and `3a-1<=3a` bound the ratio
by `864e/2401 < 2376/2401 < 1`; `a=2,3` follow by direct substitution.
The pinned row certificate attains `L_a`, so this is the optimal inflow for
this fixed edge system. The product has the asymptotic

\[
h_a=\frac{\Gamma(a+1/3)}{\Gamma(4/3)\Gamma(a)}
  \sim\frac{a^{1/3}}{\Gamma(4/3)},\qquad
L_a\sim\frac{3}{4\Gamma(4/3)}a^{4/3}.
\]

Thus the resulting exponent bounds tend to `9/4` but do not pass the strict
criterion. This rules out the current
neighbor/tripling/boundary row family as a strict-improvement certificate
with these endpoints. It does not rule out additional exact identities,
different endpoints, or a constraint beyond this scalar edge system. This
written, unreviewed conditional result is tracked as
`AI-R5-CONVOLUTION-GRAPH-BARRIER-001`.

## Pinned sources and local interfaces

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  commit [`fd4aeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), especially the finite-separation proposition and shared-leg entropy inequality in Section 3, the discrete-growth lemma, and the detecting-character lemma. This is the external complex-field baseline.
- Yuval Filmus, *Matrix multiplication from block identities*, commit
  [`8e38460`](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/tree/8e38460c2c04617692a64a826b09e8995ac8717d), frozen declaration [`identities_to_exponent_v2.lean`](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Frozen/identities_to_exponent_v2.lean). The source-level interface was inspected; its imported proof closure was not rebuilt here.
- The same pinned Filmus commit's [shared convolution identities](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/ConvolutionSharedIdentities.lean), [neighbor degeneration](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Providers/ConvolutionNeighbor.lean), [tripling degeneration](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Providers/ConvolutionTripling.lean), [convolution potential](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Square/ConvolutionPotentialBound.lean), [yield formula](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Square/Yield.lean), [border-rank bound](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/ConvolutionRankBound.lean), and [terminal isomorphism](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/ConvolutionTerminal.lean). Provider hypotheses include `b>=2` or `r>=2`; the border-rank result assumes an infinite field.
- The same commit's [shared-leg value inequality](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Providers/SharedLegValue.lean) converts each exact identity and its matrix volumes into the value rows above.
- Houxi Lü, *Polynomial Separation of a Shared Tensor Leg and Matrix Multiplication in Arbitrary Characteristic*, [arXiv:2610.18914v1](https://arxiv.org/html/2610.18914v1), Proposition 2.1 and equations (3.1)-(3.3). Its field-size requirement and degeneration hypotheses are part of the statement.
- Local comparison points: [scalar profile and filtration note](../research/ai/2026-10-20/research_note.md), [direct-sum extraction](../research/ai/2026-10-20-affine-direct-sums/direct_sums.md), [fixed-label equivalence](../research/ai/2026-10-20-concavity-equivalence/research_note.md), and claim `AI-SCALAR-001` in [`research/claims.json`](../research/claims.json).
