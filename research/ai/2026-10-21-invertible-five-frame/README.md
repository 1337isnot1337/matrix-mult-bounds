# The invertible first lines have no output-growth escape

The [written proof](proof.md), unreviewed, excludes every compatible
invertible mixed-line first pair at the canonical four-row flags. It
includes arbitrary boundary graphs, arbitrary later maps, and unequal
positive first-growth orders. It does not improve the exponent.

The key is that a five-row/five-column cross has matrix rank at most ten,
below the target's minimum nonzero slice rank eleven. The both-mixed
classification makes each opposite five-frame's annihilator exactly the
original five-frame. Formal row elimination then prevents every further
output row, regardless of the leading rows' higher normal variations.

For the rational seed, `verify.py` exports exact rank-107 certificates
for both 500-by-112 annihilator maps. A separate retained cubic curve
shows that the preceding rank-13 linear truncation can be corrected
through degree three. Its first particular second correction had a
cubic obstruction, but the 264 homogeneous second-row freedoms have a
rank-13 action on that obstruction space and can cancel this residual.
This finite control does not yield an all-order lift or a matrix target.

```sh
python research/ai/2026-10-21-invertible-five-frame/verify.py \
  --output results/local/invertible-five-frame.json
python research/ai/2026-10-21-invertible-five-frame/construct.py \
  --output results/local/invertible-cubic-control.json
python -m unittest discover -s tests -p 'test_invertible_five_frame.py' -v
```

The tests replay the cubic control in both canonical and original cyclic
source coordinates and reject a changed nonzero source correction.
Finite checks do not formally verify the all-order argument. Sources,
earlier generating heads, and attribution are recorded in `sources.json`.
