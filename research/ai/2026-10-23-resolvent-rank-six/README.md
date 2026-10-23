# Fixed-resolvent rank-six locus

The [written proof](proof.md) classifies the full rank-at-most-seven locus
of W: a 17-dimensional linear space, with every nonzero element of rank
six and one fixed six-dimensional image. Rank seven is absent. Over
algebraically closed fields, rank109 compression factors lose at most one
direction, giving sharp compressed dimension 111.

This is a continuation of `AI-RESOLVENT-SHARP-MINRANK-001` with exact source
pins, not a matrix target or an exponent improvement. All claims remain
written and unreviewed.

From the repository root:

```sh
python -S research/ai/2026-10-23-resolvent-rank-six/verify.py
python -m unittest discover -s tests -p test_resolvent_rank_six.py -v
python -m unittest discover -s tests -p test_resolvent_minrank.py -v
```

Acceptance reconstructs the literal source without importing the discovery
program. It checks 26 eight-by-eight triangular-minor identities, all unit
substitutions, the exact residual parameter basis, and its common image.
The predecessor supplies the all-field lower bound six. Focused tests
include independent source reconstruction, corrupted certificates, exact
rational rank-six and rank-eight controls, and a compression killing
exactly one direction of the 17-dimensional locus.

`discovery/triangular_minors.py` searches for candidate minors. Its output
is not trusted by acceptance. The universal argument uses polynomial
identities rather than finite sampling. See `claims.json` and
`sources.json` for scope and provenance.
