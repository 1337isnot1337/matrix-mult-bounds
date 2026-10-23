# Nonsplit two-matrix targets: power-five screen

The fifth tensor power of the actual `SL(2,F5)` source has a verified
characteristic-two slice-rank upper bound of 9,874,344,844. Replaying the
exact direct-sum target slice ranks removes eight of the 144 two-matrix
candidates in the pinned earlier frontier. The other 136 are not excluded
by this comparison.

The [written derivation](proof.md) gives the exact source cover, target
formula, eight gaps, and limitations. `SOURCES.json` pins the candidate
ledger and inherited full-source verifier. The prior pair enumeration and
its earlier Koszul/profile screens are not regenerated here.

Run from the repository root with Python 3.10 or later:

```sh
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power5.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power5-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/verification.json
```

The verifier first checks every original source coefficient, independently
counts the five-power degree classes, and replays the power-three and
power-five exact target sums. No candidate degeneration or exponent
improvement is claimed; the finite conclusion retains the existing
one-copy coefficient-one good-reduction limitation and has no independent
review or formalization.
