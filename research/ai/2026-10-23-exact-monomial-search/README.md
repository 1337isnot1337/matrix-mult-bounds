# Exact monomial support search

This maintained copy addresses the exact-ranking item in R6 of
docs/research_directions.md. The historical search remains unchanged.

## Method

For each integer weight pair, the search normalizes each array by subtracting
its own minimum. It preserves the two input leg roles: the first input index
is the shared axis used to group sectors, so swapping the arrays can change
the score. The output weights are the negatives of the minimum pair sums.

The report records the complete zero-weight support, its deterministic
connected-component partition, the exact block recognition (including axis
reversals), and rational source, target, and ratio scores. Every retained
leaderboard record is recomputed from its certificate before export. The
leaderboard compares Fraction values directly; floating-point values are not
used.

The certificate verifies this finite monomial relaxation. An unrecognized
sector receives only its valid single-slice lower bound. Neither a score nor a
support certificate supplies arbitrary basis changes or proves a matrix
multiplication exponent.

## Reproduction

Run from the repository root with Python 3.10 or later:

    python research/ai/2026-10-23-exact-monomial-search/search.py --mode binary --max-sum 11 --output results/exact-monomial-search-2026-10-23/binary.json
    python research/ai/2026-10-23-exact-monomial-search/search.py --mode ternary --max-sum 10 --output results/exact-monomial-search-2026-10-23/ternary.json
    python research/ai/2026-10-23-exact-monomial-search/search.py --mode random --samples 20000 --seed 20261020 --output results/exact-monomial-search-2026-10-23/random.json
    python -m unittest discover -s tests -p test_exact_monomial_search.py -v

The deterministic runs replay the three archived scopes:

| Mode | Parameters | Cases |
| --- | --- | ---: |
| Binary | Entries in {0,1}, min zero in each array, a+b <= 11 | 12,976 |
| Ternary | Entries in {0,1,2}, min zero in each array, a+b <= 10 | 209,692 |
| Random | 20,000 pairs, lengths 2 through 15, entries -8 through 8, seed 20261020 | 20,000 |

The exact reports are stored beside this package in
results/exact-monomial-search-2026-10-23/. Their source pin is recorded in
sources.json. This work changes the ranking and replay evidence, not the
mathematical scope of the historical finite experiment.

Across the three reports, the exact best ratio is 1. The best nontrivial
ratios are 1 for binary, 1 for ternary, and 21/22 for the seeded random run.

## Result status

All retained scores and support certificates are exact and replayable. The
search found no scored violation of the profile in the three recorded scopes.
This does not exhaust arbitrary integer weights, coordinate restrictions,
basis changes, cancellations, tensor powers, or stronger bounds on
unrecognized sectors. No improvement to omega is established.

The code, report, and proof status are AI-assisted and unreviewed. No
independent mathematical review or Lean formalization is claimed.
