# Fixed long-leg coordinate maps require a quadratic correction

**Result.** Fix the coordinate maps
`B_(y,s) -> b_(s,y)` and `C_(z,v) -> c_(v,z)` from `Q(n,4)` to
`M(n,4,n)`, sending indices outside the target to zero. For every linear
map on the first leg, the target-minus-source correction has first-leg
flattening rank exactly `n^2`. Consequently, no auxiliary tensor of
border rank `O(n)` can complete this fixed long-leg chart.

The proof projects to the coefficients of `b_(s,0)c_(0,z)` and
`b_(s,1)c_(1,z)`. Their source terms come from the same first-leg source
coordinate at adjacent positions. A kernel vector must therefore be
constant along each diagonal, and the boundary rows force every diagonal
to vanish. No assumption on the first-leg map is needed.

The exact standard-library replay checks the coefficient identities and
the stacked projected rank for six rational first-leg maps, at
`n=1,...,6`. This is an indexing control; the all-size proof is in
[`proof.md`](proof.md).

The result leaves open changing either long-leg map or the source family.
It does not establish an exponent improvement. The written proof is
unreviewed and has no Lean formalization.

Reproduce with:

```bash
python -S research/ai/2026-10-23-q64-coordinate-long-legs/verify.py \
  --max-n 6 \
  --output results/q64-coordinate-long-legs-2026-10-23/verification.json
```
