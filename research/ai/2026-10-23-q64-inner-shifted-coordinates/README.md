# Fixed inner-index shift multipliers still need quadratic correction

**Result.** Fix nonnegative integers `k_B,k_C` and use
`B_(y,s) -> b_(s-k_B*y,y)` and
`C_(z,v) -> c_(v,z-k_C*v)`, with out-of-range target coordinates sent
to zero. For every linear first-leg map, if `n>max(k_B,k_C)`, the
target-minus-source correction has first-leg flattening rank at least
`n^2-1-k_B*k_C`. For fixed `k_B,k_C`, this grows quadratically, so the
chart cannot use an `O(n)`-border-rank auxiliary correction.

The proof uses the `(1,0)` and `(0,1)` inner-coordinate blocks to force
all but at most `1+k_B*k_C` source functionals to vanish. The matched
`(0,0)` block confines any flattening kernel to those target coordinates.

The exact rational replay checks all four pairs `k_B,k_C in {0,1}`, six
first-leg maps, and `n=1,...,6`. These finite checks validate indexing;
the proof in [`proof.md`](proof.md) handles every fixed nonnegative pair.

Other long-leg maps whose shifts are not fixed multiples of the inner
indices, general `Q(n,4)` restrictions, independent review, Lean
formalization and exponent improvement remain outside this claim.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-inner-shifted-coordinates/verify.py \
  --max-n 6 \
  --output results/q64-inner-shifted-coordinates-2026-10-23/verification.json
```
