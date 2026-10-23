# Filtered-bundle screen of the paired long-leg targets

This package makes an exact finite comparison for the 28 saved short-leg
survivors at `a=14,15,16`. It uses the associated-graded kernel-section
bound in the written proof at [PR #169](https://github.com/1337isnot1337/matrix-mult-bounds/pull/169), pinned to head
`a629c557d3ee155cbd1c8c2f97ce3d367a115475`. That all-size proof is still
unreviewed and unmerged, so the comparison is conditional on it.

For `N=a(2a-1)`, the pinned proof gives

```text
U(a,p) = sum_{k=a}^{2a-1} a*(C(2a-1,k)-C(2a-1,k+1))
         * C((a-1)(2a-1),p-k) * max(p+(a-1)-a*k+1,0)
rank K_p >= max(0, a^2*C(N,p)-U(a,p)).
```

We compare this source-rank lower bound with both exact padded matrix-target
long-leg ranks from the pinned `all_ranks.py`, over every degree in the
intermediate ranges left by PR #169's endpoint theorems. For every saved
target, both target ranks are at most the source lower bound throughout:

| `a` | Saved targets | Intermediate degrees checked | Degrees safe for every target and both legs |
| ---: | ---: | ---: | ---: |
| 14 | 5 | 183–363 | 183–209 |
| 15 | 11 | 211–419 | 211–241 |
| 16 | 12 | 241–479 | 241–274 |

Thus these first degree windows cannot give another long-leg rank exclusion
for the 28 saved formats, assuming the pinned bundle proof. Individual
targets can have wider safe windows; the exact per-shape intervals are in
`results/paired-long-leg-target-screen-2026-10-23/certificate.json`.

The remaining degrees are undecided by this comparison. A target rank above
the source lower bound is inconclusive: it does not show that the actual
source rank is smaller. The finite screen is not an exact source-rank
formula, an independent proof review, a degeneration, or an exponent
improvement.

Reproduce from the repository root:

```sh
python research/ai/2026-10-23-paired-long-leg-target-screen/verify.py --output results/paired-long-leg-target-screen-2026-10-23/certificate.json
python research/ai/2026-10-23-paired-long-leg-target-screen/verify.py --verify results/paired-long-leg-target-screen-2026-10-23/certificate.json
python -m unittest discover -s tests -p 'test_paired_long_leg_target_screen.py' -v
```

All combinatorial and target-rank arithmetic is exact. The verification pins
the local frontier and target-rank implementation; `sources.json` records
the separate, unmerged proof dependency.
