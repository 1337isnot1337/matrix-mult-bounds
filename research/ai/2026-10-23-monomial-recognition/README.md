# Whole-sector recognition and ordered monomial search

This owner-directed Codex continuation of R6 proves that arbitrary coordinate
permutations cannot reveal a whole convolution sector missed by the archived
sorted-index/reversal recognizer. See [proof.md](proof.md) for the exact
additive-label and coefficient-one hypotheses. General linear bases, proper
restrictions and stronger lower bounds on nonconvolution sectors remain open.

It also audits the missing input orientation in the archived finite binary
and ternary scopes. The component score shares the first input, so source
symmetry does not justify discarding a>b. PR118 retains the original finite
scope and supplies a separate maintained exact-ranking implementation; it is
credited but is not an executable dependency here.

Run from the repository root:

```sh
python research/ai/2026-10-23-monomial-recognition/verify.py --alphabet-size 2 --max-sum 11 --output results/monomial-recognition-2026-10-23/binary.json
python research/ai/2026-10-23-monomial-recognition/verify.py --alphabet-size 3 --max-sum 10 --output results/monomial-recognition-2026-10-23/ternary.json
python -m unittest discover -s tests -p test_monomial_recognition.py -v
```

Both reports are complete:

| Census | a+b cutoff | a<b | a=b | a>b | Total | Swapped unequal-dimension pairs with different scores |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Binary | 11 | 11,732 | 1,244 | 11,732 | 24,708 | 8,742 |
| Ternary | 10 | 160,560 | 49,132 | 160,560 | 370,252 | 118,604 |

The maximum ratio and maximum multicomponent ratio are exactly one in both
censuses; neither has an exact violation. These extend the original scopes
by 11,732 and 160,560 candidates respectively, without changing the score.
The alphabets overlap, so their totals are not a count of distinct supports.
Acceptance uses rational comparisons, an independent ordered-count formula,
and replay of every retained record. Six focused tests cover all 63 nonempty
2-by-3 supports against brute-force coordinate permutations, all 511 nonempty
3-by-3 supports against the archived recognizer, all output axes with shifted
and gapped labels, invalid supports, exact archived-score comparisons, the
51-candidate ordered control and corrupted-record rejection.

Claims `AI-ADDITIVE-SUPPORT-RECOGNITION-001` and
`EXP-ORDERED-MONOMIAL-CENSUS-001` distinguish the written, unreviewed proof
from the finite census. Neither establishes an all-weight obstruction or a
smaller exponent. Full local regression and archive replay logs are retained
outside the repository; their actual completion is recorded in the PR.
