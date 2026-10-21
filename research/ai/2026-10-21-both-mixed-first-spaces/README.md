# Simultaneous mixed first spaces

The [written proof](proof.md) classifies the two nonzero mixed projections
as lines, while allowing arbitrary boundary graph corrections. Rank-one
mixed lines have a unique partner relation and first quotient ranks at
most 7 on each side. Invertible mixed lines have first quotient ranks
exactly 1 on each side. The necessary rank sum is therefore at most 14
when both mixed projections are nonzero.

This is an unreviewed local obstruction, not a smaller exponent. Exact
7-by-7 and 1-by-1 compatible first spaces are retained as positive controls.
Their complete polynomial maps still have first rank twelve and do not
realize the matrix target. The invertible-line stratum leaves 72 normal
directions before the further lifting equations; those remain to solve.

The verifier checks the two mixed-boundary matrix actions, symbolic partner
identities on charts covering every nonzero complex rank-one matrix, and
all coefficients of both positive controls. Tests use a separate source
coordinate convention and reject a changed boundary graph.

```sh
python research/ai/2026-10-21-both-mixed-first-spaces/verify.py \
  --output results/local/both-mixed-first-report.json
python -m unittest discover -s tests -p 'test_both_mixed_first_spaces.py' -v
```

Source pins and inspection limits are recorded in `sources.json`.
Generating-session checks and CI do not constitute independent review
or formalization.
