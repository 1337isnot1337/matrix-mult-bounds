# Neighboring inner-index shifted charts need quadratic corrections

**Result.** For either choice `epsilon_B,epsilon_C in {0,1}`, use
`B_(y,s) -> b_(s-epsilon_B*y,y)` and
`C_(z,v) -> c_(v,z-epsilon_C*v)`, sending out-of-range coordinates to
zero. For every linear first-leg map, the target-minus-source correction
has first-leg flattening rank at least
`n^2-1-epsilon_B*epsilon_C` for `n>=2`; in particular, the rank is at
least `n^2-2`. No auxiliary tensor of border rank `O(n)` can repair any
of these four charts.

The proof uses cross blocks `(1,0)` and `(0,1)` to kill all but at most
`1+epsilon_B*epsilon_C` source functionals. The matched `(0,0)` block
then confines the flattening kernel to the same number of target
coordinates.

An exact rational replay checks the coefficient formulas and projected
ranks for all four shift pairs, six first-leg maps, and `n=1,...,6`.
This replay checks indexing; the all-size result is proved in
[`proof.md`](proof.md).

Other long-leg maps, general `Q(n,4)` restrictions, independent review,
Lean formalization and exponent improvement are outside this result.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-inner-shifted-coordinates/verify.py \
  --max-n 6 \
  --output results/q64-inner-shifted-coordinates-2026-10-23/verification.json
```
