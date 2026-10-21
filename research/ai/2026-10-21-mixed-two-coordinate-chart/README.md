# A two-coordinate graph chart

Claim `AI-MIXED-TWO-COORDINATE-STRATA-093` proves the exact normal rank
stratification for m+t*d0+h*d1 at a=b=1. A polynomial frame is complete
away from (0,0) and (1,1). A separate complete normal calculation and
target-rank elimination exclude the exceptional graph at (1,1).

The [written proof](proof.md) is unreviewed. The generic target incidence
on this chart remains open; no smaller exponent is established. The
[certificate](certificate.json) records exact witnesses, the
[report](../../../results/mixed-two-coordinate-chart-2026-10-21/report.json)
records replayed scope, and [sources](sources.json) pin the dependencies.

From the repository root with maintained dependencies installed:

```sh
python research/ai/2026-10-21-mixed-two-coordinate-chart/verify.py --output results/local/mixed-two-coordinate-chart.json
python -m unittest discover -s tests -p test_mixed_two_coordinate_chart.py -v
```

Singular was used for discovery only. The maintained replay verifies
the source coefficients, polynomial frame, matched minors, all complex
exceptional roots, and both complete target-normal elimination chains.

The subsequent [open-set theorem](../2026-10-21-generic-mixed-graphs/proof.md)
covers a nonempty open subset of this chart and extends to all six graph
coefficients and the partner parameter. Its exceptional complement remains
unclassified; the present rank-stratification and point certificates retain
their original scope.
