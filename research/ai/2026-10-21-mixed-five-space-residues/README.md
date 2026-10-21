# A mixed five-space forces plane normals at one rank-one partner

At the partner point `u=v=(0,0,0,1)`, the full seven-dimensional B first
space and **any** complex mixed five-dimensional C first space force the
four common-plane normal directions. The [written proof](proof.md) is
unreviewed. It combines low-rank third slices, rank-two obstruction
minors, and the requirement that the C space have a nonzero mixed
projection. Source reversal also gives the point `u=v=(1,0,0,0)`.

The exact normal dimensions are

    88 -> 68 -> 54 -> 30 -> 18 -> 12 -> 4.

These are necessary reductions for a matrix-target lift, not a discovery
of a new target. This package does not cover every partner line. It does
not improve the exponent 9/4 or the global first-rank bounds.

The verifier reconstructs the source equations, proves that virtual C
correction errors factor through the C obstruction, exports all repeated
minor witnesses and small support covers, and compares the final kernel
with the four plane motions. Every calculation uses exact rational
arithmetic. No random sample is used for the universal five-space claim.

```sh
python research/ai/2026-10-21-mixed-five-space-residues/verify.py \
  --output results/local/mixed-five-space-residues.json
python -m unittest discover -s tests -p 'test_mixed_five_space_residues.py' -v
```

The report is in `results/mixed-five-space-residues-2026-10-21/report.json`.
Finite replay does not independently review the written all-order argument.
