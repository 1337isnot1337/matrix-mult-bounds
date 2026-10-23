# Balanced leading-rank total 202

Claim `AI-A4-LEADING-RANK-SUM202-001` proves necessary conditions for
every complete complex Laurent A4 to M(10,10,11) presentation:

- The three individually balanced leading ranks have total at most 202.
- If the short rank is 100, both long ranks are at most 28.
- The exact additional mixed and long floor constraints hold on pair
  sums 129 through 136, retaining the prior every-pair bound of 136.

See [proof.md](proof.md) for the all-order hypotheses, short contradictions,
and the distinction between arithmetic endpoints and target constructions.
[sources.json](sources.json) pins the unchanged every-pair 136 and 144
proofs and the new sharp source-space proof below ranks 92 and 96.

## Reproduction

Run from the repository root with Python 3.10 or later:

```sh
python research/ai/2026-10-23-leading-rank202/verify.py
python -m unittest discover -s tests -p 'test_leading_rank202.py' -v
python -m unittest discover -s tests -p 'test_rank92_rank96_spaces.py' -v
```

The target verifier uses only the standard library. To regenerate its
complete saved arithmetic evidence, use the verifier's `--write` flag.
This writes only the new result directory.

## Evidence format

[controls.json](../../../results/leading-rank202-2026-10-23/controls.json)
records all counts, endpoint checks, floor-quotient lists, source pins,
and the exact claim scope.
[census.json.gz](../../../results/leading-rank202-2026-10-23/census.json.gz)
contains the prior-survival and new-survival masks for all 20,706 pairs
and all 1,050,804 triples. Each hexadecimal string encodes bytes. Bit k
of byte j records case 8*j+k. Cases are in lexicographic rank order,
with the last coordinate varying fastest, starting at zero. The shapes
are [101,102], [102,102], and [101,102,102]. Unused final bits are zero.
Acceptance reconstructs every bit and compares the complete records.

The two new source caps remove 817 additional pairs and 62,478 additional
triples. The unique screened total maximum is (70,66,66); the unique
full-short total maximum is (100,28,28). These are numerical controls,
not constructed Laurent presentations. No sharp target bound, improved
exponent, formalization, or independent external review is claimed.
