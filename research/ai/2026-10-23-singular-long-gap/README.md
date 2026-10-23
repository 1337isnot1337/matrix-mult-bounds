# Singular long-leg limits of rank at least106

The [written proof](proof.md) extends PR113's full-rank-long-leg exclusion
to regular limiting long maps of ranks106--109 for A4 to M(10,10,11).
It permits arbitrary finite poles in both other maps, including the
original source identity lift. Both scalar-balanced leading long-leg
ranks must therefore be at most105 in any remaining candidate.

The proof combines the prior regular rank-two kernel correction with the
source gap16-or-at-least20. Minimum-rank leading images give a map from
Mat10 to Mat4 taking rank-one matrices to rank at most one. A polynomial
factorization includes compression, transpose, fixed-row and fixed-column
cases. Each has an invertible matrix in its kernel, contradicting the
unit-image rank budget. Flanders's dimension inequality is imported only
for the degenerate fixed-row/column cases, with its complex hypotheses
and exact source in `sources.json`.

Claims `AI-SINGULAR-LONG-GAP-001` and `AI-A4-LONG-RANK106-002` are written
and unreviewed. No independent review, formalization, historical-priority
claim, target construction or exponent improvement is made. Rank105 is
the equality boundary for this minimum-rank-gap argument.

```sh
python research/ai/2026-10-23-singular-long-gap/verify.py
python -m unittest discover -s tests -p 'test_singular_long_gap.py' -v
```

Finite controls export53 exact invertible-kernel witnesses for compression
maps, including rank-deficient factors and the m=2a boundary; three
degenerate maps with exact invertible kernel witnesses; literal A4 source
ranks16 and20; six strict long-leg rank cases; and three local byte pins.
Acceptance directly verifies the exported witnesses. Seeded search is
used only to discover the three degenerate witnesses. These controls do
not formalize the arbitrary-series argument or supply degenerations.
