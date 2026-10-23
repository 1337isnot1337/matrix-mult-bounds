# Diagonal-shift correction obstruction

This package rules out one explicit set of maps from the paired source
`Q(n,4)` as a route to `M(n,4,n)` with a linear-border-rank auxiliary
correction. The correction's first-leg flattening has rank exactly `n^2`
for every positive integer `n`.

The proof projects two target inner-coordinate blocks and reduces each
diagonal block modulo two. See [proof.md](proof.md) for the all-size
argument and [QUESTION.md](QUESTION.md) for the precise scope.

The standard-library replay independently constructs the source image,
forms the correction, checks the projected block formula and verifies
full projected rank modulo two for `n=1,...,12`:

```sh
python -S research/ai/2026-10-23-q64-diagonal-shift/verify.py \
  --max-n 12 \
  --output results/q64-diagonal-shift-2026-10-23/verification.json
```

Claim `AI-Q64-DIAGONAL-SHIFT-CORRECTION-001` is written and unreviewed.
This is one restricted-map obstruction, not a general obstruction to
`Q(n,4)` constructions. It establishes no exponent improvement.
