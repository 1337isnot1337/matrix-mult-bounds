# The full A4 chart with one regular long leg

The [written proof](proof.md) excludes a complete formal degeneration
A4 to M(10,10,11) whenever either long map is regular with rank110 limit.
The other two maps may have arbitrary finite Laurent poles. There is no
regularity or image-rank assumption on the original target-identity lift.
This strictly extends the previous rank109 partial-unit-image chart.

The general theorem uses a target unit and a spanning set of rank-rho
slices. A regular right inverse gives a kernel correction of rank at
most k=N-R. Its regular limit bounds each leading source generator
by rho+2k. The source minimum16 beats11+4 by one rank unit.

Both long maps must therefore have singular scalar-balanced leading
coefficients in any remaining A4 construction. Those cases, the full
target and any improvement below9/4 remain open. Claims
`AI-UNIT-KERNEL-LOW-RANK-001` and `AI-A4-ONE-REGULAR-LEG-002` are
**written and unreviewed**. CI does not change their mathematical status.

The [registered question](QUESTION.md) records the selected gap. Source
minimum-rank and predecessor Laurent arguments retain their credit and
[exact byte pins](sources.json). No new external theorem is imported;
all continuation work is owner-directed OpenAI Codex work.

With the root requirements installed, run from the repository root:

```sh
python research/ai/2026-10-23-one-regular-leg/verify.py
python -m unittest discover -s tests -p test_one_regular_leg.py -v
```

The frozen report is `results/one-regular-leg-2026-10-23/controls.json`.
It checks36 polar kernel projections with regular corrections, six
zero-rank limiting unit images, five scalar-balancing examples, nine
isolated rank budgets, all100 target matrix-unit generators, and one
literal rank16 source coordinate slice with a rank14 column compression.
These finite controls support the proof without formalizing its arbitrary
series. The tests also reject corrupt source pins and overstated scope.
Use `verify.py --write` only to regenerate the report, then replay without
that flag. The isolated rank-budget matrices do not claim to satisfy the
full tensor hypotheses or show optimality of the general theorem.

Concurrent [PR112](https://github.com/1337isnot1337/matrix-mult-bounds/pull/112)
also uses a regular right-inverse projection in its rank102 unit-image
argument. Its independent derivation and prior source credit remain
separate; no independent review is asserted here. This theorem uses
scalar balancing and spanning low-rank target generators to remove the
image-rank threshold. PR108's partial frames retain their separate scope.
