# Mixed hyperplanes recover complete rank-one frame equations

The [written proof](proof.md), unreviewed, excludes every rank-one mixed
first pair with both effective dimensions at least six at the canonical
flags. It includes arbitrary complex subspaces, boundary graphs, later
coefficients and delayed unequal first orders. The necessary ordinary
first-rank sum with both mixed projections nonzero stays at most twelve;
only seven-by-five pairs remain on its rank-one threshold. The exponent
is still 9/4.

On the full 228-dimensional normal space, exact repeated two-by-two minors
show that a rank-at-most-one obstruction on either maximal seven-frame
has only its mixed column remaining. Any mixed hyperplane kills that
column and recovers all seven equations on that leg, without assuming
opposite-leg equations. Applying this twice leaves only the four common-
plane directions, so the earlier formal induction applies.

Every kernel substitution is polynomial and verified at every point of
the parameter chart; a separate endpoint and source reversal complete
coverage. The report also retains the conditioned calculation, nonzero
rank-one controls for boundary-only hyperplanes, and a mixed seven-by-five
control with twelve normal dimensions.

```sh
python research/ai/2026-10-21-rankone-mixed-hyperplanes/verify.py \
  --output results/local/rankone-mixed-hyperplanes.json
python -m unittest discover -s tests -p 'test_rankone_mixed_hyperplanes.py' -v
```

Finite tests do not formally verify the all-order proof. Source pins and
the distinction between adopted and new work are in `sources.json`.
