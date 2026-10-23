# Leading flags after both long maps become singular

The [written proof](proof.md) gives necessary full-source A4 conditions
for the still-unconstructed M(10,10,11) target. Balance each long map by
its own minimum scalar valuation. Let their leading ranks be r_B,r_C
and set d=224-r_B-r_C. Then:

* d>=16. If16<=d<32, the leading first-map image has one fixed
  coherent middle factor and dimension at most16.
* At d=16, that image has dimension exactly one and is a minimum-rank
  source slice. The balanced first map must have pole order at least10.
  Arbitrary higher regular long-map coefficients are allowed.
* Exact controls satisfy the leading equation at every rank pair
  r_B+r_C=208 with99<=r_B,r_C<=109. Their constant outputs have rank12,
  and supply no target identity or completed degeneration.

Claims `AI-A4-LEADING-DEFECT-001` and `AI-A4-BOUNDARY-POLE-GAP-002`
are **written and unreviewed**. Pole orders at least10 at equality,
larger defects, the full target and an exponent below9/4 remain open.
This full-source flag problem is separate from the canonical conic jets.

The [registered question](QUESTION.md) records the branch selection.
The source minimum, minimum-rank classification, coherent-factor theorem
and PR113 obstruction retain [exact predecessor pins](sources.json) and
their original credit. The row/column intersection and bounded-pole
continuation are owner-directed OpenAI Codex work using the two credited
standard graph-descent facts in Stacks Tags02LS and0AB1. No historical
priority or independent mathematical review is claimed.

With the root requirements installed, run from the repository root:

```sh
python research/ai/2026-10-23-leading-defect/verify.py
python -m unittest discover -s tests -p test_leading_defect.py -v
```

The frozen report is `results/leading-defect-2026-10-23/controls.json`.
Eleven sparse long-map controls record deleted source coordinates and
coordinates restored at degree one. Every unspecified retained source
coordinate has coefficient one; the last two deleted coordinates remain
absent. The controls also check125440 literal source coefficients on ten
minimum-rank pencil fibers, two exact annihilator determinants, and ten
families of bilinear kernels with450 basis-pair intersections, plus
three coordinate-span controls for the nine-constraint boundary. They do
not formalize the arbitrary-series proof. Regenerate with `--write`,
then replay without that flag. Tests reject false completion, altered
pole bounds and corrupted predecessor pins.
