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

## The full oriented profile laws still admit the critical shape

The pinned [continuous oriented-profile completion theorem](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Rectangular/OrientedProfileCompletion.lean)
adds bounds, homogeneity, input-swap symmetry, monotonicity, powered
concavity, and the powered three-sector row with its side-swapped middle
orientation. These rows also admit the critical shape. At the symmetric
weight vector `w_X=w_Y=w_Z=3/4`, set all six profiles equal to

\[
Q(x,y)^{3/4},\qquad
Q(x,y)=\min(x,y)^{1/3}\left(\max(x,y)+\frac{\min(x,y)}2\right).
\]

This profile is positive, symmetric, homogeneous of degree one, and
coordinatewise increasing. If `m=min(x,y)` and `M=max(x,y)`, then
`Q(x,y)^(3/4)/m=(M/m+1/2)^(3/4)` lies between `1` and `M/m+1`; hence
`m<=Q(x,y)^(3/4)<=x+y`. Its powered profile is exactly `Q`. For fixed `x`,
`Q(x,y)=xy^(1/3)+y^(4/3)/2` when `y<=x`, with
`d^2Q/dy^2=(2/9)y^(-5/3)(y-x)<=0`; for `y>=x` it is affine, with matching
first derivatives at `y=x`. Thus the powered concavity row holds. Because all
orientations agree, the tripling row
reduces to `3Q(1,s)<=Q(1,3s+1)`. It is equality for `s>=1`; for `0<s<=1`,
putting `z=s^(1/3)` gives
`Q(1,3s+1)-3Q(1,s)=(3/2)(1-z)^3(1+z)>=0`.

This is a feasible point of the continuous profile-law system, not a tensor
character or a supporting-vector construction. It matches the necessary
critical limiting profile in the
[endpoint rigidity note](../research/ai/2026-10-20-critical-character-extension/README.md)
at amplitude one. Therefore adding the pinned powered profile rows alone
still does not exclude the `9/4` endpoint. A new constraint on actual
characters or tensor maps is needed; the screen is tracked as
`AI-R5-ORIENTED-PROFILE-SCREEN-001`.

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

At Filmus's pinned commit, neighboring-length, square-tripling, and
general-tripling modules provide actual `SharedLegIdentity` records. Write
`C(r,b)` for the
convolution tensor, and write `x(C(r,b))` for a positive value assignment
satisfying their induced inequalities. In the exponent theorem,
`x(A)=normalizedValueAtOmega(A)`. For `r>=1` and `b>=2`, the neighbor identity
has source
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

The rectangular provider gives the general split
`C(r,3s+r-1) -> 3 C(r,s)` for positive `r,s`; its supported three-sector sum
has the same shared first leg and reversed, permuted middle block. The pinned
`generalTriplingSharedIdentity` theorem packages it with source and output
shapes of volume `1`.
The replication provider gives `C(mr,ms) -> m C(r,s)` for positive `m,r,s`
over an infinite field. Its direct-sum sectors can be labeled on the two
private legs and zero-padded on the common first-leg space, again with scalar
shapes. The algebraic closure used by the exponent theorem is infinite, so
this field hypothesis is available there. The generic supported-sum helper
packages replication as a shared-leg row; this wrapper is written here but
was not formalized in this repository. The resulting rows are

\[
x(C(r,3s+r-1))\geq3x(C(r,s)),\qquad
x(C(mr,ms))\geq m x(C(r,s)).
\]

The pinned [componentwise restriction theorem](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Rectangular/OrientedConvolutionProfiles.lean)
gives another one-child row.
For \(r\leq R\) and \(s\leq S\), selecting initial coordinates on all three
legs restricts \(C(R,S)\) to \(C(r,s)\). Scalar padding packages this as a
shared-leg identity with one child; this wrapper is written here but was not
locally formalized:

\[
x(C(R,S))\geq x(C(r,s)).
\]

The same pinned module gives an input-swap isomorphism \(C(r,s) \cong C(s,r)\),
so their scalar vertex values are equal. The boundary symmetry used by the row
certificate is a special case.

The pinned source proves the neighbor and square-tripling degenerations and
the independent block identifications needed by `SharedLegIdentity`. It also
gives source border-rank at most `u+v-1` for every `C(u,v)` over an infinite
field, and formalizes `symmetrize(C(2,1)) \cong M(2,2,2)`. More generally,
`C(q,1)` has coefficient `1` exactly when its two `Fin q` indices agree.
After identifying each symmetrized leg with a pair of `Fin q` indices, its
coefficient is

\[
\delta_{x_1,z_2}\delta_{z_1,y_2}\delta_{y_1,x_2},
\]

the matrix multiplication tensor `M(q,q,q)`. This extends the terminal
isomorphism to every `q>=2` by a direct coordinate check; the pinned Lean
source formalizes only `q=2`, and this general check is not formalized here.

It still cannot meet the strict graph threshold using only these convolution
edge rows: componentwise restriction, neighbor, general tripling, replication,
and input-swap symmetry.
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

and for `b>=r` the neighbor row is equality. The input-swap symmetry follows
from symmetry of `P_*`, and
`P_*(r,4r-1)=3P_*(r,r)`. The profile's shifted tripling inequality gives
`P_*(r,3s+r-1)>=3P_*(r,s)`. Its replication inequality gives
`P_*(mr,ms)^3>=m^4P_*(r,s)^3`, which implies
`P_*(mr,ms)>=mP_*(r,s)` because `P_*>0` and `m>=1`. The formula is also
monotone in each coordinate: for fixed `a` and `b<a`,
`P_*(a,b+1)-P_*(a,b)=h_b(a+2b)/(3b)>0`; for `b>=a`, the increment is
`h_a>0`. By symmetry it is monotone in the first argument. Consequently, for
any nonnegative edge weights satisfying the certificate balances with source
`C(u,v)` and terminal `C(q,1)`, summing each row against this positive
potential gives `qL<=P_*(u,v)`, since `P_*(q,1)=q`. For the diagonal source
`C(a,a)` and terminal `C(2,1)`, this specializes to the inflow cap

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

For \(a\geq4\), \(h_a^3\leq \mathrm e(a-1)\) follows from
\(\log(1+u)\leq u\) and the harmonic-number bound
\(H_n\leq1+\log n\). Using \(2a-1\geq7a/4\) and \(3a-1\leq3a\)
then bounds the ratio by \(864\mathrm e/2401\). The elementary
\(\mathrm e<11/4\) gives \(864\mathrm e/2401<2376/2401<1\). At `a=2,3`
the ratios are respectively `1000/2187` and `175616/455625`.

This diagonal estimate also controls every rectangular source `C(u,v)`.
Let `m=min(u,v)` and `n=max(u,v)`. When `m=1`, `P_*(u,v)=n=u+v-1`,
so `P_*(u,v)^3/(u+v-1)^4=1/n<=1`. When `m>=2`, regard `n` as real and set

\[
F(n)=\frac{h_m^3(n+(m-1)/2)^3}{(n+m-1)^4}.
\]

For `n>=m`,
`d(log F)/dn=(m-1-n)/((n+(m-1)/2)(n+m-1))<0`. Hence
`F(n)<=F(m)=(2L_m)^3/(2m-1)^4<1` by the diagonal estimate above. Therefore
`P_*(u,v)^3<=(u+v-1)^4` for all positive `u,v`, with equality only when
`u=v=1`. For any thin terminal `C(q,1)` with `q>=2`,
`(qL)^3<=P_*(u,v)^3<=(u+v-1)^4`, so these graph rows never pass the strict
improvement criterion for any rectangular source.

The pinned row certificate attains `L_a`, so this is the optimal inflow for
the diagonal source `C(a,a)` and terminal `C(2,1)`. The product has the
asymptotic

\[
h_a=\frac{\Gamma(a+1/3)}{\Gamma(4/3)\Gamma(a)}
  \sim\frac{a^{1/3}}{\Gamma(4/3)},\qquad
L_a\sim\frac{3}{4\Gamma(4/3)}a^{4/3}.
\]

Thus the diagonal-source exponent bounds tend to `9/4` but do not pass the
strict criterion. More generally, the current restriction/neighbor/general-
tripling/replication/input-swap row family cannot give a strict improvement
from any rectangular source `C(u,v)` to a thin terminal `C(q,1)` with `q>=2`.
The input-swap isomorphism gives the same barrier for `C(1,q)`. Other terminal
families, additional exact identities, and constraints beyond this scalar
edge system remain open. This written, unreviewed conditional result is
tracked as
`AI-R5-CONVOLUTION-GRAPH-BARRIER-001`.

## Pinned sources and local interfaces

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  commit [`fd4aeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), especially the finite-separation proposition and shared-leg entropy inequality in Section 3, the discrete-growth lemma, and the detecting-character lemma. This is the external complex-field baseline.
- Yuval Filmus, *Matrix multiplication from block identities*, commit
  [`8e38460`](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/tree/8e38460c2c04617692a64a826b09e8995ac8717d), frozen declaration [`identities_to_exponent_v2.lean`](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Frozen/identities_to_exponent_v2.lean). The source-level interface was inspected; its imported proof closure was not rebuilt here.
- The same pinned Filmus commit's [shared convolution identities](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/ConvolutionSharedIdentities.lean), [neighbor degeneration](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Providers/ConvolutionNeighbor.lean), [tripling degeneration](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Providers/ConvolutionTripling.lean), [convolution potential](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Square/ConvolutionPotentialBound.lean), [yield formula](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Square/Yield.lean), [border-rank bound](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/ConvolutionRankBound.lean), and [terminal isomorphism](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/ConvolutionTerminal.lean). Provider hypotheses include `b>=2` or `r>=2`; the border-rank result assumes an infinite field.
- The same commit's [general-tripling shared-leg identity](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/OrientedConvolutionIdentities.lean), [generic supported-sum identity](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Tensor/SharedSumIdentity.lean), [general tripling provider](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Rectangular/Providers/ConvolutionGeneralTripling.lean), and [replication provider](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Rectangular/Providers/ConvolutionReplication.lean) supply these rows and their source degenerations. Replication assumes an infinite field, satisfied after passage to the algebraic closure. The replication and restriction wrappers described above are written here from the pinned source results but were not formalized in this repository.
- The same commit's [shared-leg value inequality](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Providers/SharedLegValue.lean) converts each exact identity and its matrix volumes into the value rows above.
- Houxi Lü, *Polynomial Separation of a Shared Tensor Leg and Matrix Multiplication in Arbitrary Characteristic*, [arXiv:2610.18914v1](https://arxiv.org/html/2610.18914v1), Proposition 2.1 and equations (3.1)-(3.3). Its field-size requirement and degeneration hypotheses are part of the statement.
- Local comparison points: [scalar profile and filtration note](../research/ai/2026-10-20/research_note.md), [direct-sum extraction](../research/ai/2026-10-20-affine-direct-sums/direct_sums.md), [fixed-label equivalence](../research/ai/2026-10-20-concavity-equivalence/research_note.md), and claims `AI-SCALAR-001` and `AI-REPLICATION-003` in [`research/claims.json`](../research/claims.json).
