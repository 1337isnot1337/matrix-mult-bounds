# Paired-source shift-separation barrier

This package extends the rank-one channel-symbol factorization in [PR #157](https://github.com/1337isnot1337/matrix-mult-bounds/pull/157) to one long-leg map whose column coefficients vary with a finite family of scalar profiles. The predecessor is pinned by commit and source hash in [sources.json](sources.json). The all-field proof is in [proof.md](proof.md), with the precise task in [QUESTION.md](QUESTION.md).

For a profile `alpha_j`, form the matrix `Phi_j[q,v]=alpha_j(q+v)` on the interior source columns and the `m` middle coordinates. If the sum of these matrix ranks is less than `m`, the residual from any ordinary restriction `Q(n,m) -> M(n,m,n)` has flattening and border rank at least `g_B*g_C`, even with arbitrary mixing on the first leg. At fixed `m` and sublinear bandwidth/exception counts, this lower bound is `n^2-o(n^2)`.

The claim is proof-written and unreviewed. It excludes only this low shift-separation ordinary-map class. It does not settle arbitrary variable-coefficient maps or singular Laurent cancellations, and it establishes no smaller exponent.

## Reproduction

```sh
python -S research/ai/2026-10-23-paired-shift-separation/verify.py \
  --output results/paired-shift-separation-2026-10-23/verification.json
python -m unittest discover -s tests -p test_paired_shift_separation.py -v
```

The exact finite control uses `F_101`, a width-four instance with profile ranks `1` and `2`, and direct tensor reconstruction. It is a reproducibility check, not the proof of the all-size theorem.
