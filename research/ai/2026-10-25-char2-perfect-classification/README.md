# Perfect-field characteristic-two attainers

For every perfect field K of characteristic two, the three-dimensional
attainers for the literal complete quadratic source have classes

    (K/AS(K))_P disjoint-union {N} disjoint-union (K/AS(K))_V,
    AS(K)={z^2+z:z in K}.

Thus every finite field of characteristic two has exactly five classes.
The P-form classification holds over every characteristic-two field.
The N uniqueness and inherited V classification here require perfection.

Claims `AI-CHAR2-P-FORMS-001` and `AI-CHAR2-PERFECT-ATTAINERS-001` are
**proof-written-unreviewed**. See [proof.md](proof.md) for polynomial rank
hypotheses, permitted actions, explicit representatives and the descent
argument. [sources.json](sources.json) pins the earlier proofs and preserved
discovery, including an incorrect k substitution and its correction.

From the repository root:

```sh
python -B research/ai/2026-10-25-char2-perfect-classification/verify.py
python -B -m unittest discover -s tests -p test_char2_perfect_classification.py -v
python -B -m unittest discover -s tests -v
python -B tools/replay.py
```

The first command reproduces
[the exact report](../../../results/char2-perfect-classification-2026-10-25/controls.json).
It checks twenty source pins, pre-normalization restrictions, full chart
coefficients, every normalization and AS-shift identity, middle-column
covariance and the square-chart N shear. Seven tests include damaged
substitution, matrix, action, quartic and source-pin controls.

No new finite census is asserted. The exact-five corollary follows from
the written classification and the two-element AS quotient over finite
fields. Computation does not certify the geometric rank-transfer or descent
arguments. Author self-audit is not independent review. Nonperfect N/V
forms, a compatible three-leg tensor map, formalization, historical
priority and an exponent improvement remain outside these claims.
