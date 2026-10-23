# A sharp global cap for singular source spaces

Every complex linear subspace of the full A4 source whose every matrix
slice is singular has dimension at most96. A96-dimensional zero-row
kernel attains the bound. Thus every97-dimensional source subspace
contains an invertible slice. Read the [written proof](proof.md).

The proof packs sixteen disjoint supports carrying unimodular source
slices. A diagonal action with112 distinct source weights preserves
matrix rank. It degenerates an arbitrary complex all-singular subspace
to a coordinate subspace of the same dimension. The packing forces at
least sixteen missing coordinates. This covers arbitrary dense complex
subspaces; the finite witnesses alone do not supply that quantifier.

For the A4 to M(10,10,11) problem, if the first lift F is regular and
the other long map has109 regular independent selected columns, its
leading source image must be entirely singular and have dimension<=96.
Otherwise a generic invertible target matrix has a regular invertible
source-unit lift, contradicting the partial-frame theorem. No injectivity
of F(0) is assumed. Sharpness of the source cap does not establish a
target degeneration attaining leading rank96.

The proof is **written and unreviewed**. It imports no new external
theorem. The maintained source convention and earlier minimum-rank,
unit and partial-frame proofs retain their credit and exact pins.
The new packing, diagonal proof and leading-rank consequence are
owner-directed OpenAI Codex work. No independent review, formalization,
target construction or exponent improvement is claimed.

```sh
python research/ai/2026-10-23-source-singular-space-cap/verify.py
python -m unittest discover -s tests -p test_source_singular_space_cap.py -v
```

Use root requirements from the repository root. The verifier checks all
sixteen112-square unit matrices modulo1009, independently proves their
unimodularity by four exact28-square integer determinants and full
Kronecker entry comparison, checks4096 source weight identities and the
sharp zero-row kernel. The tests compare all200704 unit-matrix entries
to the pinned maintained source and reject forged units, weights, caps,
source pins and exponent claims. These are exact finite checks of the
proof data, not a formalization of the all-subspace or Laurent arguments.

Claims: `AI-SOURCE-SINGULAR-CAP-001` and
`AI-A4-FIRST-LEADING-RANK-002`.
