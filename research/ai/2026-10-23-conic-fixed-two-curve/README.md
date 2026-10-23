# Exact conic curve with the prescribed full two-jet

Claim `AI-CONIC-FIXED-TWO-CURVE-001` is written and unreviewed.
For every complex a,b,d with d nonzero and c=-d^3, the [proof](proof.md)
extends all six prescribed PR107 map coefficients through order two,
and its supplied kernel corrections Y1=Y2=0, to an exact polynomial
curve. B has degree eight and C degree nine in the deformation parameter.

Every coefficient belongs to Q[a,b,d,d^-1], with pole orders at most
five and six. The complete source contraction has a fixed kernel at
every order, and constant minors1,1,-1 certify formal ranks14,14,12.
The d=0 fiber is outside this mixed-chart witness. No prescribed third
jet, complete matrix target or exponent improvement is claimed.

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-conic-fixed-two-curve/construct.py results/local/conic-fixed-two-curve.json
python research/ai/2026-10-23-conic-fixed-two-curve/verify.py results/conic-fixed-two-curve-2026-10-23/polynomial-curve.json --output results/local/conic-fixed-two-verification.json
python -m unittest discover -s tests -p 'test_conic_fixed_two_curve.py' -v
```

The independent acceptance program reconstructs the literal source and
checks all eighteen possible product orders. Sparse exact arithmetic
and retaining every relevant K contribution keep this complete check
small enough for routine regression. The tests cache one full positive
replay and use inexpensive targeted corruption controls thereafter.

Exact timings and focused coverage are recorded in the validation
receipt. Full repository regression, historical replay and current-head
hosted CI remain the separate integration gates.
