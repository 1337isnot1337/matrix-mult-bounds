# Finite affine partner chart

Claim `AI-AFFINE-PARTNER-CHART-100`, written and unreviewed.

The [proof](proof.md) closes the b=0 boundary in the canonical leading-flag,
full-seven versus arbitrary mixed-five class. With099 and087 it covers
every finite pair(a,b). The two projective endpoints and other first-space
or leading-flag classes remain outside this result. The exponent is9/4.

Run from the repository root:

```sh
python research/ai/2026-10-21-affine-partner-chart/verify.py --output results/affine-partner-chart-2026-10-21/report.json
python -m unittest discover -s tests -p 'test_affine_partner_chart.py' -v
```

The verifier reconstructs the complete rational fiber at(1,0), both source
families, all four cubic blocks, the source torus, and the existing corner
closure. The b-nonzero part adopts099; its verifier is not rerun here.
Exact replay and CI do not establish independent mathematical review.
