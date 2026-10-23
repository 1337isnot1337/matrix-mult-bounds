# Arbitrary per-index shifts on both Q(n,4) long legs require quadratic correction

**Result.** For arbitrary size-dependent integers `beta_0,...,beta_3` and `gamma_0,...,gamma_3`, use
`B_(y,s) -> b_(s-beta_y,y)` and `C_(z,v) -> c_(v,z-gamma_v)`, with zero padding. For every linear first-leg map, the target-minus-source correction has first-leg flattening rank at least `n(n-1)/2` for every `n`.

The proof reduces the best possible first-leg map to the dimension of the intersection between the target matrix-multiplication slice space and the source two-long-leg image. A small adjacent C-shift forces most intersection coefficients to vanish through unique off-diagonal monomials. If all adjacent C-shifts are large, the four matched blocks have a common support of at most `ceil(n/2)` coordinates in one matrix direction.

The exact rational replay checks deterministic arbitrary-shift profiles and the exact source/target subspace ranks through `n=5`. The proof in [`proof.md`](proof.md) gives the all-size argument.

Other long-leg maps, general `Q(n,4)` restrictions, independent review, Lean formalization and exponent improvement remain outside this claim.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-arbitrary-inner-shifts/verify.py \
  --max-n 5 \
  --profiles 8 \
  --output results/q64-arbitrary-inner-shifts-2026-10-23/verification.json
```
