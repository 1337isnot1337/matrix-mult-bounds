# The inner-index shifted long-leg chart has a near-terminal frontier

**Result.** For each `n`, choose any integers
`0<=k_B(n),k_C(n)<n` and use
`B_(y,s) -> b_(s-k_B*y,y)` and
`C_(z,v) -> c_(v,z-k_C*v)`, zeroing out-of-range target coordinates.
For every linear first-leg map, the target-minus-source correction has
first-leg flattening rank at least
`n^2-1-k_B*k_C`.

Consequently, an `O(n)`-border-rank auxiliary correction in this chart
requires `k_B*k_C >= n^2-O(n)`. Since both multipliers are at most
`n-1`, this forces `k_B=n-O(1)` and `k_C=n-O(1)`. The proof therefore
excludes all shift sequences where either multiplier stays more than a
bounded distance below `n`; the near-terminal pair remains open.

The exact rational replay checks four pairs `k_B,k_C in {0,1}`, six
first-leg maps, and `n=1,...,6`. Those cases check indexing; the proof in
[`proof.md`](proof.md) covers arbitrary size-dependent multipliers.

Other long-leg maps, general `Q(n,4)` restrictions, independent review,
Lean formalization and exponent improvement are outside this claim.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-inner-shifted-coordinates/verify.py \
  --max-n 6 \
  --output results/q64-inner-shifted-coordinates-2026-10-23/verification.json
```
