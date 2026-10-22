# Balanced punctures of the third biform core

The [written proof](proof.md) classifies **complete** cancellation after
deleting two dimensions from each twelve-dimensional boundary leg.
It does not establish an improving matrix multiplication degeneration.

- The complete auxiliary matrix action forces both quotient kernels to
  be products of a base line with the auxiliary two-dimensional space.
- In the biform multiplication kernel, every such cancellation space
  has dimension at most three. Dimension at least two forces a common
  factor of bidegree (1,1).
- On every projective chart, the actual normal core admits a non-plane
  cancellation precisely when `g=(r*x0+s*x1)*(r*y0-s*y1)`, with
  `[r:s]` arbitrary in P1. The two residual linear forms are arbitrary,
  and every non-plane normal fiber is exactly two-dimensional. Sixteen
  disjoint cases with constant unit minors and explicit residual identities
  certify the conclusion, including every projective boundary point.

The source tensor, flags and biform factorization are inherited from the
[earlier package](../2026-10-21-biform-third-core/proof.md). Their exact
dependencies are pinned in [sources.json](sources.json). The previous
integrable shear is retained as a separate positive construction; the
new affine family here is a family of third-block cancellations.

Claims: `AI-BIFORM-BALANCED-KERNEL-001`,
`AI-BIFORM-AFFINE-INCIDENCE-002`, `EXP-BIFORM-BALANCED-CONTROLS-003`,
`AI-BIFORM-PROJECTIVE-INCIDENCE-004`.
All proofs are AI-assisted, written and unreviewed. No priority,
independent review, formalization, or exponent improvement is claimed.

Reproduce from the repository root with its maintained dependencies:

```sh
python research/ai/2026-10-21-biform-balanced-puncture/verify.py --output-dir results/biform-balanced-puncture-2026-10-21
python research/ai/2026-10-21-biform-balanced-puncture/projective.py --output results/biform-balanced-puncture-2026-10-21/projective.json
python -m unittest discover -s tests -p test_biform_balanced_puncture.py -v
python -m unittest discover -s tests -p test_biform_projective_puncture.py -v
```

Nine focused tests replay the polynomial certificates against all actual core
coefficients, verify the reverse ideal identities, reject altered
certificates, independently multiply the biforms, and cover all 36 fixed
monomial line pairs. That finite coordinate control is separate from
the arbitrary-kernel theorem and all-parameter projective classification.

Open: projected first ranks one and two; later
coefficient compatibility; full-rank source maps; the required matrix
slice space; and an actual bound below 9/4.
