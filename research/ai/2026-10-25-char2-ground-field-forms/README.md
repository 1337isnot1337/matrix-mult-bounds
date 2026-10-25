# Ground-field forms of characteristic-two quadratic attainers

The moving-eta locus over a perfect characteristic-two field K is classified
by the additive quotient K/{r^2+r}. Over each finite field it has exactly two
forms, with (q-1)^3 and (q-1)^2(q+1) invertible coefficient matrices.
A separate explicit construction gives nonsplit forms of P over arbitrary
characteristic-two fields and at least five inequivalent GF2 attainers.

Claims `AI-CHAR2-PERFECT-ETA-FORMS-001` and
`AI-CHAR2-NONSPLIT-P-FORMS-001` are **proof-written-unreviewed**.
See [proof.md](proof.md) and [sources.json](sources.json). This does not
exhaust P-forms or all GF2 attainers, or classify nonperfect-field forms.
No tensor map or matrix-multiplication exponent improvement is claimed.

From the repository root, without Python optimization:

```sh
python research/ai/2026-10-25-char2-ground-field-forms/verify.py
python -m unittest discover -s tests -p 'test_char2_ground_field_forms.py' -v
```

The saved report is `results/char2-ground-field-forms-2026-10-25/controls.json`.
It includes exact symbolic identities, 228696 weighted-action checks and
33824 determinant checks over GF2/GF4/GF8, and40 literal GF2 source ranks.
Finite coverage is separate from the written all-perfect-field proof.
