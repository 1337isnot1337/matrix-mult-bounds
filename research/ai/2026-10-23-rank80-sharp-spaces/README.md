# Sharp source dimension 44 below rank 80

The [proof](proof.md) determines the exact maximum dimension of a
complex A4 source space whose every slice has rank below 80: it is 44.
This improves the earlier upper bound 50. Claim
`AI-A4-RANK80-SHARP-LINEAR-SPACE-001` remains written and unreviewed
externally, with no formalization.

The upper bound reduces arbitrary complex spaces to coordinate ideals.
Exactly 1,709 size-45 ideals survive the prior coherent-block constraints;
each has an exported integer slice with a nonzero 80-by-80 minor. The
lower bound uses full middle layers zero and one plus twelve coordinates
in layer two. A fixed cover by 35 rows and 44 columns bounds every slice
in this 44-dimensional space by rank 79. An exported rank-79 minor
attains that rank.

## Reproduce

From the repository root, with Python 3.10 or later:

```sh
python -I -S research/ai/2026-10-23-rank80-sharp-spaces/verify.py
python -m unittest discover -s tests -p 'test_rank80_sharp_spaces.py' -v
```

Acceptance uses only the standard library. It checks the source hashes,
all 1,721 saved minors, complete ideal coverage, and the sharpness cover.
It does not import discovery or regenerate random choices.

To regenerate candidate data and then verify it:

```sh
python research/ai/2026-10-23-rank80-sharp-spaces/discover.py --output results/local/rank80-sharp-spaces-candidate.json
```

Discovery uses a bounded stream of binary candidates, reset with seed
zero for each ideal. The saved witnesses required at most seven choices
per size-45 ideal. A discovery file is not accepted until the separate
verifier checks its exact support and minors.

The [source record](sources.json) credits the prior order-ideal theorem
and coherent certificates. The earlier rank-80 proof and its inputs are
unchanged. This package contains no target-map rank-pair application,
complete target construction, or new exponent bound.
