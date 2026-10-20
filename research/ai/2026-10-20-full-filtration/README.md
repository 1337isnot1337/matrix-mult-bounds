# Full-filtration entropy investigation

Selected October 20, 2026 by Codex at the repository owner's request.
Branch: `research/full-filtration-entropy-20261020`; initial base: `e0d7ed5`.

Question: can extracting the **whole** tight support `i+j=k` of the
two-convolution determinant filtration exclude the scalar matching profile
at `t=3/4`? This differs from checking the single-row, single-column and
single-diagonal inequalities owned by
`research/filtration-compatibility-20261020`. The Koszul branch owns the
dimension-packing audit. No additional agents are launched here.

The intended output is a precise entropy optimization, rational verification
of any accepted witness or upper certificate, and a report of actual coverage.
Neither a finite profile violation nor a negative entropy search alone proves
an improved matrix-multiplication exponent.

External dependencies to inspect: OpenAI's shared-leg construction and
determinant filtration at `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, and
the tight-support extraction underlying Strassen's theorem as stated in
Christandl--Vrana--Zuiddam, arXiv:1609.07476v2, Theorem 1.1.31. The weighted
block version needs an explicit argument; the scalar subrank theorem alone
must not silently be used for non-scalar blocks.

Result: the [research note](research_note.md) proves an analytic dual bound
and an all-size `39/40` obstruction for balanced sources. The exact report
covers every distribution for all 20,736 source tuples through size 12.
No exponent improvement or weighted block-extraction theorem is claimed.
The archived first and second research passes are unchanged.
