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

The reports count 24,708 binary and 370,252 ternary candidates when complete.
Acceptance uses rational comparisons, an independent ordered-count formula,
and replay of every retained record. No full census result is asserted until
its report is present. The proof is written and unreviewed; the finite search
does not establish an all-weight obstruction or a smaller exponent.
