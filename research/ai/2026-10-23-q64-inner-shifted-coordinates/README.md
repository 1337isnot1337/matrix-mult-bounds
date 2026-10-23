# All inner-index proportional long-leg shifts need quadratic correction

**Result.** For every `n`, choose any integers
`0<=k_B(n),k_C(n)<n` and map
`B_(y,s) -> b_(s-k_B*y,y)` and
`C_(z,v) -> c_(v,z-k_C*v)`, sending out-of-range target coordinates to
zero. For every linear first-leg map, the target-minus-source correction
has first-leg flattening rank at least `n^2/2` for every `n>=4`.
Consequently this entire multiplier family cannot use an auxiliary
correction of border rank `O(n)`.

The proof has two cases. If either `2*k_B>n+1` or `2*k_C>n+1`, the
matched inner slice `j=2` receives no source contribution and gives full
rank `n^2`. Otherwise the two off-diagonal blocks give rank at least
`n^2-1-k_B*k_C`, which is at least `n^2/2` for `n>=4`.

The exact rational replay checks every multiplier pair `0<=k_B,k_C<n`
for `n=1,...,6` and six first-leg maps. It checks coefficient formulas
and the stated rank bounds; the proof in [`proof.md`](proof.md) supplies
the all-size argument.

Other long-leg maps, general `Q(n,4)` restrictions, independent review,
Lean formalization and exponent improvement remain outside this claim.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-inner-shifted-coordinates/verify.py \
  --max-n 6 \
  --output results/q64-inner-shifted-coordinates-2026-10-23/verification.json
```
