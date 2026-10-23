# Exact conic curve with the prescribed full first jet

Claim `AI-CONIC-FIXED-FIRST-CURVE-001` is written and unreviewed.
For every complex a,b,d at c=-d^3, the [proof](proof.md) supplies cubic
polynomial maps preserving PR107's full constant and first coefficients.
The complete source contraction stays in the fixed rank-twelve source
space; the map ranks are fourteen over the formal parameter ring.

All coefficients belong to Q[a,b,d], with no parameter denominator.
This includes d=0 and the linear-component intersections. The second
coefficients change. No full matrix target or exponent gain is claimed.

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-conic-fixed-first-curve/construct.py results/local/conic-fixed-first-curve.json
python research/ai/2026-10-23-conic-fixed-first-curve/verify.py results/conic-fixed-first-curve-2026-10-23/polynomial-curve.json --output results/local/conic-fixed-first-verification.json
python -m unittest discover -s tests -p 'test_conic_fixed_first_curve.py' -v
```

The verifier contracts the complete literal source product through
degree six and compares the full credited first jet. The construction
and verification programs share no gauge formula. Reused polynomial
arithmetic and source helpers retain their exact byte pins and credit.
Full repository regression, historical replay and hosted CI remain the
integration gates; focused validation is recorded separately.
