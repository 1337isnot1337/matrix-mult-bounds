# Exact integrable boundary shears

Written AI-assisted construction, unreviewed. No exponent improvement.

The [proof](proof.md) gives a two-parameter polynomial family of14-dimensional
source rowspaces. Both spaces move outside the common polynomial-plane
motions, while the entire112-by14-by14 contracted tensor stays fixed.
Every complex parameter is covered. The fixed tensor has first rank12.

Away from the origin, these spaces are each other's complete annihilators
on the100-dimensional source kernel. Their dimensions are exactly14;
explicit98-by98 determinants cover both nonzero-parameter charts. At the
origin the annihilator dimensions are16.

The family gives degree-two polynomial local maps with canonical four-row
leading flags, effective first ranks10,10, and two independent non-plane
normal derivatives. All five possible tensor coefficients are checked
exactly; every source-row correction can be zero. This is an all-order
integrable family, not just a compatible third jet.

The local maps have generic rank14 and their contracted first rank stays12.
They cannot reach the matrix target of dimensions100,110,110 on their own.
Higher-rank completions change the exact identity and remain open. The
example prevents extending the common-plane trap to every10-by10 first
pair without additional hypotheses.

```sh
python research/ai/2026-10-21-integrable-boundary-shears/verify.py --output-dir /tmp/boundary-shears
python -m unittest discover -s tests -p test_integrable_boundary_shears.py -v
```

Use root requirements.txt. Tests independently evaluate every source
coefficient using fixed index relations, replay all polynomial chart
minors without searching for them, reject a sign error, and verify every
coefficient of the degree-two maps. Canonical source data and prior normal
coordinates retain their credit in sources.json. Same-session exact checks
and CI provide no independent mathematical review or formalization.
