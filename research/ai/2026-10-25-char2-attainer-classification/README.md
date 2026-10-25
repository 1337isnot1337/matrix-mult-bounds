# Exactly three geometric characteristic-two quadratic attainers

Over an algebraically closed field of characteristic two, every
three-dimensional coefficient family with nonzero coefficient determinant
and geometric full-source rank at most fourteen is equivalent to exactly
one of the previously published families P, N and V, under permitted binary
changes and optional transpose.

The proof combines the common-kernel pencil lemma and evaluation-kernel
classification with a complete moving-eta normalization and mixed-kernel
exclusion. Claim `AI-CHAR2-QUADRATIC-ATTAINERS-001` is
**proof-written-unreviewed**. See [proof.md](proof.md) and [sources.json](sources.json).

This is a geometric classification. A GF2 example is equivalent to V only
after field extension; arbitrary ground-field forms remain unclassified.
No compatible tensor map or matrix-multiplication exponent improvement follows.

From the repository root:

```sh
python research/ai/2026-10-25-char2-attainer-classification/verify.py
python -m unittest discover -s tests -p 'test_char2_attainer_classification.py' -v
```

The saved report is `results/char2-attainer-classification-2026-10-25/controls.json`.
