# High A4 source caps and the full-short long-rank bound 20

The [written proof](proof.md) determines sharp maximum source-space
dimensions 84, 88, 92 and 96 below the strict slice-rank thresholds
100, 104, 108 and 112. Credited staircase spaces attain these dimensions;
four new exact minors certify their maximum ranks 96, 100, 104 and 108.

For complete complex Laurent A4-to-M(10,10,11) presentations with
individually balanced short leading rank 100, both long leading ranks
are at most 20. In fact each positive long rank lies in {1,...,12,20}.
The numerical endpoint (100,20,20) does not construct a target.

## Reproduction

Run from the repository root with Python 3.10 or later:

```sh
python research/ai/2026-10-23-high-rank-source-caps/verify.py
python -m unittest discover -s tests -p 'test_high_rank_source_caps.py' -v
```

Both commands use only the Python standard library. The frozen input
versions and code attribution are in [sources.json](sources.json).
To reproduce the separate witness-selection step and regenerate its
report, run:

```sh
python research/ai/2026-10-23-high-rank-source-caps/discover.py --output results/high-rank-source-caps-2026-10-23/certificates.json
python research/ai/2026-10-23-high-rank-source-caps/verify.py --write-report
```

The [certificates](../../../results/high-rank-source-caps-2026-10-23/certificates.json)
contain eleven unchanged credited coherent witnesses and four new source
minors. The [report](../../../results/high-rank-source-caps-2026-10-23/controls.json)
records all literal-source controls, layer-case counts, sharpness checks,
strict endpoints and all 102 one-leg target decisions. The complete
10,404-case full-short pair check retains 196 of the preceding 841
triples, excluding 645 additional numerical possibilities.

The proof retains the order-ideal reduction and all-order saturated
target-support hypotheses. This branch follows frozen PR176 and does
not import the concurrent rank-91 refinement. All five claims remain
written and unreviewed, with no formalization, external independent
review, target construction or exponent improvement.
