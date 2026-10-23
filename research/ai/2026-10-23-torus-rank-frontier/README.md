# A balanced A4 long-rank sum of at most 176

The [written proof](proof.md) establishes two necessary bounds over C:

- Every linear space of A4 source parameters whose slices all have
  matrix rank below 48 has vector dimension at most 24.
- In every A4 to M(10,10,11) Laurent degeneration, independently balance
  both long maps to valuation zero. Their constant ranks must sum to
  at most 176, a total loss of at least 44 from the target dimensions.

The first assertion concerns arbitrary complex subspaces. A rank-preserving
torus moves each such subspace to a coordinate limit without changing its
dimension. Exact block restrictions and the prior eight-pair rank-24
certificate then give the bound. The dimension-24 upper bound is not
claimed sharp.

The second assertion allows every finite Laurent pole order and arbitrary
higher jets. It combines the source bound with the credited saturated
target-support inequality. It strengthens PR122's sum bound of 192.
No maps realizing a surviving pair, complete matrix target, or exponent
improvement are supplied. Both claims remain written and unreviewed.

Run from the repository root with Python 3.10 or later:

```sh
python research/ai/2026-10-23-torus-rank-frontier/verify.py
python -m unittest discover -s tests -p test_torus_rank_frontier.py -v
```

The verifier uses only the Python standard library. It independently
replays the literal six-index source, eight saved rank-24 minors, all
768 prohibited middle-pair controls, the Kronecker block multiplicities,
and all 12,321 integer long-rank pairs. Its frozen evidence is
`results/torus-rank-frontier-2026-10-23/controls.json`. Use `--write` only
to regenerate the evidence before replay. Source versions and credit
are in [sources.json](sources.json).

Proposed claims: `AI-A4-RANK48-LINEAR-SPACE-001` and
`AI-A4-BALANCED-LONG-SUM176-002`.
