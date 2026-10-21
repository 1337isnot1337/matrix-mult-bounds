# Sixteen adapted low-rank source slices on the full partner chart

For every compatible rank-one partner on the chart
`u=(ab,-a,-b,1)`, `v=(ab,b,a,1)`, and every leading normal satisfying the
complete B seven-frame equations, the sixteen source combinations

    e_(2,s,z) - a e_(1,s,z),  s=0,1,2,3; z=1,2,4,5

have projected third slices of rank at most one, modulo the C correction
obstruction. Their slices must vanish in a matrix-target lift. The
[written proof](proof.md) and exact polynomial report include every
complex a,b, with no sampling or excluded parameter values.

This extends the first step of the coordinate-partner elimination. It
does **not** extend its complete normal closure to every partner. General
mixed five-spaces and an exponent below9/4 remain open.

```sh
python research/ai/2026-10-21-mixed-five-space-uniform/verify.py \
  --output results/local/mixed-five-space-uniform.json
python -m unittest discover -s tests -p 'test_mixed_five_space_uniform.py' -v
```

The virtual tensor builder is shared with the point package. Its original
report remains unchanged and is replayed after this reuse change. The
uniform tensor's specialization at a=b=0 is also checked against the point
construction. The new report contains the uniform normal kernel,
constant-minor rowspace certificate, correction residual factorization,
adapted sources and full reduced coefficient tensor.
