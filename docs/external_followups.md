# External follow-up repositories

Review date: 2026-10-20. This is a source-level comparison, not a local Lean rebuild or a complete proof audit.

The subsequent [agent-board review](agent_board_review.md) adds the four
@fringewidth research reports, preserves their unverified status, and corrects
their proposed exact-rank search window using Massarenti-Raviolo's published bound.

## Sela Navot: all fields

Repository: https://github.com/selanavot/matrix-multiplication-all-fields

Inspected revision: `08481ef22bca7dc9ffba091083b7c1e81e537220`.

The README attributes the original numerical bound and complex proof to OpenAI. It describes an extension to arbitrary fields, including positive characteristic. The main modifications concern Fourier periods, interpolation nodes, and fixed-overhead descent from an algebraic closure.

The repository distinguishes exact coefficient rank from functional correctness over finite fields. That distinction matters because equality on finite-field inputs need not imply a formal polynomial identity.

The useful dependency for this project is the arithmetic-model and field-descent layer. A new tensor inequality must still reach the stated arithmetic exponent. The field extension itself does not reduce 9/4.

Source: [README at the inspected revision](https://github.com/selanavot/matrix-multiplication-all-fields/blob/08481ef22bca7dc9ffba091083b7c1e81e537220/README.md).

## Yang Zhou and Mingsheng Wang: arbitrary rings

Repository: https://github.com/Hugin-Hilbert/rectangular-matmul-rings

Inspected revision: `285f513384dee8f933d941ed5e8770ddfbdcaae2`.

The README credits the rectangular curve to Przemyslaw Uznanski. It describes integral constructions and circuits that apply uniformly to associative rings, including noncommutative and nonunital rings.

The reported curve is 2 for k<=1/2, and 1+k+1/(4k) for k>1/2. At k=1 it gives 9/4, not a smaller square exponent.

The useful dependency is the separation between integral tensor identities and arithmetic circuits. Its finite construction verifier is a prospective comparison target. It was not executed during this checkpoint.

Source: [README at the inspected revision](https://github.com/Hugin-Hilbert/rectangular-matmul-rings/blob/285f513384dee8f933d941ed5e8770ddfbdcaae2/README.md). README blob: `f9fc18814ac14dc41cfb5785b439b30f9a910d21`.

## Yuval Filmus: block identities

Repository: https://github.com/YuvalFilmus/matrix-multiplication-block-identities

Inspected revision: `8e38460c2c04617692a64a826b09e8995ac8717d`.

The README describes square and rectangular bounds over every field. It preserves formal polynomial correctness. It separately states the functional bounds without assuming equality of the two exponent definitions over finite fields.

The most direct research interface is the finite graph criterion in `identities_to_exponent`. I inspected its frozen Lean declaration, not its complete imported proof closure.

The statement requires nonzero tensors at graph vertices, certified shared-leg identities at edges, auxiliary matrix shapes, and nonnegative edge weights. It also requires a source border-rank bound r and a terminal whose symmetrization is a square matrix tensor of size d. Weighted balance inequalities constrain every nonterminal vertex.

Let L be the weighted terminal inflow in that theorem. Under its full hypotheses, with d>=2, r>=1, and L>1/d, the conclusion is

$$
\omega_F\le\frac{3\log r}{\log d+\log L}.
$$

A strict improvement on 9/4 follows when

$$
(dL)^3>r^4.
$$

For rational certificate data, this last comparison is exact. It is only the numerical endpoint. Tensor identities, rank bounds, and balance constraints remain necessary.

This is Filmus's external criterion, not a theorem discovered by this project. No qualifying graph certificate was constructed in this checkpoint.

Sources: [README](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/README.md) and [frozen theorem declaration](https://github.com/YuvalFilmus/matrix-multiplication-block-identities/blob/8e38460c2c04617692a64a826b09e8995ac8717d/BlockIdentities/Frozen/identities_to_exponent_v2.lean).

README blob: `06cab6441f44afd899d7e7586f3134abdf20ff71`.
Theorem blob: `6789991b21545636620548794c2e72205b8b3d6f`.

## Earlier scalar-profile work: Rohan Arun's repository

The [pinned draft](https://github.com/rohanarun/matrix-multiplication-sector-barrier/blob/0b09d3616da31d8750366747d7821d70ae6d1b90/proof.tex), Section 4,
contains the same least scalar profile used in AI-SCALAR-001:
H_u times (v+(u-1)/2), where H_u is the OpenAI product recurrence.
Its [introducing commit](https://github.com/rohanarun/matrix-multiplication-sector-barrier/commit/5a759558440672e69641547743bde3cf6d6ae50f)
is dated October 10, before our October 20 derivation. This is an
attribution overlap; the immutable local archive remains unchanged.
The external repository discloses AI generation and does not claim
independent review, a realizing tensor character, or an exponent gain.

Its [open PR #3](https://github.com/rohanarun/matrix-multiplication-sector-barrier/pull/3), inspected at
`651bb083f558d969eba106cb79a1a5d1f5289f12`, adds a leg-resolved
relaxation: the symmetric assignment P_min^(3/4) survives its six
oriented constraints. Its convexity proof concerns the listed scalar
inequalities; it does not construct tensor characters by interpolation.
We read Sections 4 and 5 and did not run the external test suite.

## Spectrum results used by concurrent research

Sakabe, Dogan and Walter's [Theorem 1.1, v1](https://arxiv.org/html/2601.21553v1)
identifies upper support and quantum functionals for complex tensors.
Alman, Li and Pratt's [v2, September 27](https://arxiv.org/html/2604.01386v2),
Corollary 8.10, classifies spectral points with one dot-product exponent
one as edge support functionals, over arbitrary fields. Neither statement
classifies the interior point (3/4,3/4,3/4).

The [concurrent PR #28](https://github.com/1337isnot1337/matrix-mult-bounds/pull/28)
already uses these results in its quantum-profile analysis. We inspected
the cited statements directly and retain their external attribution;
this literature update is not a proof audit or an interior-spectrum result.

## Attribution and limits

No external source tree was copied into this repository. The links and annotations preserve authorship and version information. Reported external verification remains attributed to the source projects.

This review prioritizes interfaces for further research. It does not independently verify the all-fields theorem, arbitrary-rings theorem, or block-identities formalization.
