# Arbitrary mixed hyperplanes of rank-one seven-frames

The [written proof](proof.md), unreviewed, excludes rank-one mixed first
dimensions seven and six in either order, including all complex mixed
hyperplanes and boundary graph lifts. The necessary ordinary first-rank
sum with both mixed projections nonzero is now at most twelve. The
exponent stays 9/4.

Conditioning on the complete first seven-frame leaves 88 normal parameters.
Exact repeated two-by-two minors show that a rank-at-most-one obstruction
on the opposite seven-frame has only its mixed column remaining. A
six-dimensional first space with a mixed component kills that column.
The normal directions are then exactly the four common-plane motions,
and the earlier formal induction applies at arbitrary shifted orders.

Every kernel substitution is polynomial and verified uniformly on the
parameter chart. The report includes full triangular-minor and kernel
witnesses, the exceptional endpoint, nonzero rank-one controls for the
excluded boundary-only hypothesis, and a mixed seven-by-five control
with twelve normal dimensions.

```sh
python research/ai/2026-10-21-rankone-mixed-hyperplanes/verify.py \
  --output results/local/rankone-mixed-hyperplanes.json
python -m unittest discover -s tests -p 'test_rankone_mixed_hyperplanes.py' -v
```

The finite tests do not formally verify the all-order proof. Source pins
and the distinction between adopted and new work are in `sources.json`.
