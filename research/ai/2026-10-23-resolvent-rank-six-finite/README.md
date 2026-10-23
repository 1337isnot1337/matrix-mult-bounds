# Fixed-resolvent rank-six locus

The rank-at-most-six locus in the maintained 112-dimensional fixed-resolvent
space is a 17-dimensional linear space. All its nonzero matrices have the
same six-dimensional image. Over an algebraically closed field, every pair
of rank109 long-map compressions loses at most one direction, and an explicit
integer compression attains that loss.

Claim `AI-RESOLVENT-RANK-SIX-FINITE-001` is written and unreviewed. This resolves
the rank-six classification question in PR139. It establishes no smaller
matrix-multiplication exponent or arbitrary singular-target exclusion.

`proof.md` gives the theorem, field hypotheses and complete argument.
`sources.json` pins the predecessor's definitions and credits.
`verify.py` independently reconstructs the outer source and checks 26 seven-
minor identities, five six-minor identities, the resulting common image,
and 111 unit pivots for the sharp compression. It uses only the standard
library and imports no discovery code.

From the repository root:

```sh
python -S research/ai/2026-10-23-resolvent-rank-six-finite/verify.py
python -m unittest discover -s tests -p test_resolvent_rank_six_finite.py -v
```

The exact certificate and report are in
`results/resolvent-rank-six-finite-2026-10-23/`. The full regression suite and
archive replay remain separate integration checks. Finite replay supports
the written proof; it is not independent mathematical review.
