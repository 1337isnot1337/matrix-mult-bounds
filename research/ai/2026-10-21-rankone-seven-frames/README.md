# Uniform rank-one mixed seven-frames

The [written proof](proof.md), unreviewed, excludes maximal seven-by-seven
rank-one mixed first spaces at the canonical flags, with arbitrary graph
lifts, later coefficients and delayed unequal first-growth orders.
Only the four common-plane normal directions survive, uniformly over
all complex partner lines.

On the chart v=(a*b,b,a,1), a fixed 224-by-224 normal minor becomes the
identity plus a strictly triangular polynomial matrix after an invertible
constant row transformation. This is an all-parameter determinant identity.
The exceptional endpoint and source reversal cover the remaining lines.
The preserved full coefficient report includes the 332 polynomial entries,
triangular ordering, exact base and endpoint minors, and field/scope labels.

The necessary first-rank sum with both mixed projections nonzero is now
at most thirteen. This is a local constraint; the exponent stays 9/4.

```sh
python research/ai/2026-10-21-rankone-seven-frames/verify.py \
  --output results/local/rankone-seven-frames.json
python -m unittest discover -s tests -p 'test_rankone_seven_frames.py' -v
```

The tests also contract the full polynomial first pair in original cyclic
source coordinates, reject a wrong triangular ordering, and check that
deleting the mixed rows changes the normal problem. They do not formally
verify the separate all-order induction. Attribution is in `sources.json`.
