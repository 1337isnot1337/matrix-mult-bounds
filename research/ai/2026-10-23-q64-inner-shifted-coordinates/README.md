# Inner-index shifted long-leg maps still need a quadratic correction

**Result.** For the maps
`B_(y,s) -> b_(s-y,y)` and `C_(z,v) -> c_(v,z-v)`, with out-of-range
coordinates sent to zero, the target-minus-source correction has
first-leg flattening rank at least `n^2-2`, for every linear first-leg
map. Thus no `O(n)`-border-rank auxiliary tensor can repair this chart.

The proof uses the off-diagonal pairs `(y,v)=(1,0)` and `(0,1)` to force
the source functionals to vanish except at `(p,q)=(0,0)` and
`(n-1,n-1)`. The matched `(0,0)` block then shows any flattening kernel
vector is supported only on the two corresponding target coordinates,
so its dimension is at most two.

An exact rational replay checks the coefficient formulas and stacked
rank for six first-leg maps at `n=1,...,6`. This finite check validates
indexing; the all-size result is proved in [`proof.md`](proof.md).

This closes only this shifted-coordinate chart. Other long-leg maps,
general `Q(n,4)` restrictions, independent review, Lean formalization,
and exponent improvement are outside its scope.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-inner-shifted-coordinates/verify.py \
  --max-n 6 \
  --output results/q64-inner-shifted-coordinates-2026-10-23/verification.json
```
