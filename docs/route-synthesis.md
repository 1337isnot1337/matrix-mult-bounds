# Interfaces between the spectral, block-identity, and separation routes

Date: October 23, 2026. Local baseline: `1c04903c215f396150605c0778024e856ec0b0d4`.

This is a dependency map for research direction R5, not a reproof of the
external results. The local claims remain at their recorded status. In
particular, no result below improves the exponent past the external
`omega <= 9/4` bound.

## The three routes

| Route | Object that carries the argument | Bridge to an exponent bound | What must be supplied for a strict improvement |
| --- | --- | --- | --- |
| Spectral | One actual tensor character, its three dot-product exponents, and its six leg orientations. The 9/4 proof passes to a symmetrized profile on convolution tensors. | Character inequalities give concavity and shifted tripling; the discrete-growth lemma bounds the character parameter, and the detecting-character argument transfers that bound to matrix multiplication. | A constraint on actual characters beyond the scalar system. The local `P_*` profile satisfies that system, including the rank upper bound at `t=3/4`, but is not known to come from a character. |
| Block identities | A finite directed graph of nonzero tensors, exact shared-leg identities with matrix shapes, a source border-rank bound, nonnegative edge weights satisfying the vertex balances, and a terminal whose symmetrization is a square matrix tensor. | The pinned Filmus theorem bounds `formalOmega F` by `3 log(r)/(log(d)+log(L))`, where `r` is the source border-rank bound and `L` is weighted terminal inflow. | A graph certificate with all tensor identities and balances, plus `(dL)^3 > r^4`. The numerical inequality alone is insufficient. |
| Polynomial separation | A matched family `A_h` sharing one input space, with independent matched sectors on the other two spaces. | Lü's degeneration $A^{\oplus(M+n-1)}\rightsquigarrow\bigoplus_h(A_h\otimes B_X(n))$ gives a finite shared-leg inequality and, after tensor powers, the same asymptotic entropy inequality used by the spectral route. | This reduces the finite source-copy cost; by itself it does not change the asymptotic exponent. A separate character inequality or a block-identity certificate is still needed. |

The block-identity conditions above are the hypotheses exposed by the pinned
`identities_to_exponent` declaration: all vertex tensors are nonzero, every
edge carries its `SharedLegIdentity`, the terminal is symmetrized to `square d`,
the source has border rank at most `r`, and the weighted vertex inequalities
and `L > 1/d` hold. These are exact feasibility obligations, not consequences
of assigning a scalar value to each convolution size.

## What survives symmetrization

For an actual character, let `lambda_pi` be its six leg orientations,
`p_{pi,X}` the dot-product exponent of the common leg in orientation `pi`,
and

\[
t=(p_X+p_Y+p_Z)/3,\qquad
\mathcal P(T)=\left(\prod_{\pi\in S_3}\lambda_\pi(T)\right)^{1/(6t)}.
\]

For a matched sum `A = sum_h A_h` with shared leg `X`, the shared-leg entropy
inequality for one orientation is

\[
\lambda_\pi(A)\ \ge\
\exp\!\bigl(p_{\pi,X}H(q)\bigr)
\prod_h\lambda_\pi(A_h)^{q_h},
\qquad H(q)=-\sum_hq_h\log q_h.
\]

The finite-copy inequality behind it is

\[
(M+n-1)\lambda_\pi(A)\ge n^{p_{\pi,X}}\sum_{h=1}^M\lambda_\pi(A_h).
\]

Applying this to tensor powers with rational sector frequencies tending to
`q` gives the entropy inequality. Taking the geometric mean of the six
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
new local result. The missing information is a common *oriented* assignment of
all six values across several related tensors and decompositions.

Lü's improvement changes the finite copy count from `5M` to `2M-1` when
`n=M`; its asymptotic character inequality remains the same. Polynomial
separation thus improves the construction interface and its field
requirements, while the spectral route still supplies the same 9/4 endpoint.

## Candidate constraint and the next test

The next useful model is a finite joint oriented lift for a small
block-identity graph. At each graph vertex `v`, introduce six variables
`ell[pi,v]` for `log lambda_pi(A_v)` and one shared exponent vector
`(p_X,p_Y,p_Z)`. For each selected matched decomposition at a vertex and each
selected rational probability vector `q`, impose

\[
\ell_{\pi,v}\ge p_{\pi,X}H(q)+\sum_hq_h\ell_{\pi,A_h},
\]

using the same six variables whenever a tensor occurs in multiple
decompositions. For convolution vertices, impose the known scalar bounds and
the relation `(1/6) sum_pi ell[pi,v] = t log P(a,b)` when
`A_v = C(a,b)`. Retain the graph's exact
`SharedLegIdentity` maps, matrix shapes, border-rank bound, and weight balances
as separate certificate obligations. Take the geometric mean only after the
joint oriented constraints are imposed.

This is a candidate constraint system, not a proved new inequality on
`P(a,b)`. Its first test is whether a small graph can show that a scalar
profile compatible with `S1`-`S4` has no such oriented lift, or can certify
`(dL)^3 > r^4`. A finite infeasibility result for one profile would not by
itself improve the exponent: an improvement still needs to exclude all
critical characters and control characters approaching the critical value.
If neither happens, an equivalence or a counterexample would clarify why this
route adds no force. No character realizing `P_*`, joint infeasibility result,
qualifying graph, or exponent improvement is established here.

## Pinned sources and local interfaces

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  commit [`fd4aeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), especially the finite-separation proposition and shared-leg entropy inequality in Section 3, the discrete-growth lemma, and the detecting-character lemma. This is the external complex-field baseline.
- Yuval Filmus, *Matrix multiplication from block identities*, commit
  [`8e38460`](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/tree/8e38460c2c04617692a64a826b09e8995ac8717d), frozen declaration [`identities_to_exponent_v2.lean`](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Frozen/identities_to_exponent_v2.lean). The source-level interface was inspected; its imported proof closure was not rebuilt here.
- Houxi Lü, *Polynomial Separation of a Shared Tensor Leg and Matrix Multiplication in Arbitrary Characteristic*, [arXiv:2610.18914v1](https://arxiv.org/html/2610.18914v1), Proposition 2.1 and equations (3.1)-(3.3). Its field-size requirement and degeneration hypotheses are part of the statement.
- Local comparison points: [scalar profile and filtration note](../research/ai/2026-10-20/research_note.md), [direct-sum extraction](../research/ai/2026-10-20-affine-direct-sums/direct_sums.md), [fixed-label equivalence](../research/ai/2026-10-20-concavity-equivalence/research_note.md), and claim `AI-SCALAR-001` in [`research/claims.json`](../research/claims.json).
