# Matched-window permutations require a quadratic Q(n,4) correction

**Result.** Independently permuting the `n` matched long-leg coordinates for each inner index still leaves target-minus-source correction flattening rank at least `(n-1)^2`, for every first-leg map and every `n`.

The proof uses the unique source coefficient for a target entry in the matched `(0,0)` block. Except when its preimage lies on one boundary row or column, it also contributes uniquely to the absent `(0,1)` block. Therefore the target/source slice-space intersection has dimension at most `2n-1`.

The exact rational replay exhausts every permutation profile at `n=1,2` and checks deterministic profiles through `n=5`. The all-size proof is in [`proof.md`](proof.md).

Other coordinate maps, general long-leg maps, independent review, Lean formalization and exponent improvement remain outside this claim.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-window-permutations/verify.py \
  --max-n 5 \
  --profiles 8 \
  --output results/q64-window-permutations-2026-10-23/verification.json
```
