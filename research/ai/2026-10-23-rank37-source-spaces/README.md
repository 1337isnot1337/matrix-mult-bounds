# A sharp source-space cap of sixteen below rank 37

Every complex linear space of canonical A4 source slices whose matrix
ranks are all below 37 has dimension at most sixteen. The full middle-0
coordinate plane attains dimension sixteen and has every rank at most28.

The proof uses the preceding order-ideal reduction. A middle-2 monomial
excludes higher middle layers; a coherent20-minor forces middle1 onto
one short axis. Exactly thirteen size17 ideals remain, and each saved
witness has an odd integer37-minor.

From the repository root, run the exact standard-library acceptance:

```sh
python research/ai/2026-10-23-rank37-source-spaces/verify.py
python -m unittest discover -s tests -p 'test_rank37_source_spaces.py' -v
```

Optional discovery reproduction into a separate scratch artifact:

```sh
python research/ai/2026-10-23-rank37-source-spaces/discover.py --output /tmp/rank37-source-certificates.json
```

Acceptance independently reconstructs the literal source, enumerates
all thirteen ideals, and checks the frozen minors. It does not use
the discovery random choices as evidence. The exact coverage also
includes 112 block factorizations and the sixteen-dimensional witness.

Proposed claim: `AI-A4-RANK37-LINEAR-SPACE-001`.

This is a written, externally unreviewed theorem with exact finite
evidence. No threshold40 statement, mixed target-leg consequence,
target degeneration, formalization, or exponent improvement is claimed.
