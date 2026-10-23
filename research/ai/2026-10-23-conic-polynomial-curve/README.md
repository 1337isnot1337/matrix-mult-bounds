# Polynomial all-order conic curve

Claim `AI-CONIC-POLYNOMIAL-CURVE-001` is a written, unreviewed result.
The [proof](proof.md) constructs full polynomial maps of degrees one and
three in the deformation parameter. Their complete literal source
contraction stays in the fixed twelve-dimensional first-source space.
The constant maps and first normal class `[1:d]` agree with PR107 for
every complex a,b,d at c=-d^3. The first boundary velocity changes.

The coefficient ring is Q[a,b,d], so there is no excluded d=0 fiber or
parameter denominator. Constant minors1,1,-1 certify leading ranks14,14
and formal first-source rank12 for every parameter specialization.
No full matrix target or exponent improvement is established.

The [all-order criterion](all_order_criterion.md), claim
`AI-CONIC-ALL-ORDER-CRITERION-002`, combines this construction with
PR101's complete two-jet necessity and exact linear-component curves.
For every affine complex base a,b,c and every nonzero projective normal
class `[lambda:mu]`, some representative extends to all orders if and
only if `(a-c)*(b+c)*(c*lambda^3+mu^3)=0`. Every allowed class has a
polynomial representative of degrees at most one and three. The
boundary velocity may be chosen; prescribed full jets are not classified.

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-conic-polynomial-curve/construct.py results/local/conic-polynomial-curve.json
python research/ai/2026-10-23-conic-polynomial-curve/verify.py results/conic-polynomial-curve-2026-10-23/polynomial-curve.json --output results/local/conic-polynomial-verification.json
python -m unittest discover -s tests -p 'test_conic_polynomial_curve.py' -v
```

`construct.py` contains the short rank-one formula. `verify.py` is a
separate acceptance program that reconstructs all 4096 source terms,
uses exact polynomial arithmetic, and checks every complete product
coefficient through degree four. Its highest-coefficient corruption
control rules out accepting only a three-jet. The exported witness,
verification report, source pins and focused-test report are retained.

For integration, the full supported gates remain:

```sh
python -m unittest discover -s tests -v
python tools/replay.py
```
