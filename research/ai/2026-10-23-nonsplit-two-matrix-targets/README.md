# Nonsplit two-matrix targets: fifth- through seventh-power screens

The fifth, sixth and seventh tensor powers of the actual `SL(2,F5)` source
have verified characteristic-two slice-rank upper bounds of 9,874,344,844,
991,166,716,704 and 100,070,673,945,707. Exact direct-sum target ranks
exclude eight of the 144 two-matrix candidates in the pinned earlier
frontier at power five, ten more at power six and one more at power seven.
The other 125 are not excluded by these comparisons.

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
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power6.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power6-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify_power6.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power6-verification.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power7.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power7-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify_power7.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power7-verification.json
```

The verifiers check every original source coefficient, independently count
the fifth-, sixth- and seventh-power degree classes, and replay the exact
target sums over the complete orientation orbits. The prior pair enumeration and its
Koszul/profile screens are not regenerated. No candidate degeneration or
exponent improvement is claimed; the finite exclusions retain the existing
one-copy coefficient-one good-reduction limitation and have no independent
review or formalization.
