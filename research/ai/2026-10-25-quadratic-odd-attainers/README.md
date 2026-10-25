# Odd-characteristic quadratic attainers

Every four-dimensional geometric rank-at-most-fourteen family with
coefficient determinant not identically zero is equivalent, by permitted
binary changes over its ground field and optional transposition, to

    [[8t,b,c],[0,4t,f],[0,0,t]].

This holds over every field of characteristic different from two,
including zero, finite and nonperfect fields. It classifies the families
attaining the previously established bound four. Characteristic-two
three-spaces, singular families and compatible tensor maps remain outside
this theorem. No exponent improvement follows.

Claim `AI-ODD-QUADRATIC-ATTAINERS-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) and exact attribution in [sources.json](sources.json).
The verifier checks algebraic identities; it does not computationally
certify the geometric classification or constitute independent review.

From the repository root:

```sh
python research/ai/2026-10-25-quadratic-odd-attainers/verify.py
python -m unittest discover -s tests -p 'test_quadratic_odd_attainers.py' -v
```

The saved report is `results/quadratic-odd-attainers-2026-10-25/controls.json`.
