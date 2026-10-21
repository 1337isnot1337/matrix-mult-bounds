# Changed first jets at the four quantum root flags

Written local proof and exact finite linear algebra, unreviewed, October 21,
2026. No degeneration to the matrix target or exponent improvement is proved.

The prescribed quantum parameter curves are already excluded by the
[concurrent first-jet investigation](https://github.com/1337isnot1337/matrix-mult-bounds/pull/41).
This package uses its partial saturated space W1 and investigates **changed
first derivatives** at the same leading maps. It does not repeat the search
along those curves. The inspected source is pinned in `sources.json`.

The [proof](proof.md) gives a minimum-matrix-rank consequence of saturation.
For the target M(10,10,11), the fixed leading maps force dim W1=12. The exact
first-derivative solution space has dimension 4772 for two 110-row maps:

- each of the 106 new rows on each leg belongs to an explicit space of
  dimension 20;
- the eight leading rows satisfy a coupled system of rank 364 in 896
  variables, leaving 532 parameters;
- the bilinear next coefficient on the kernel has first flattening rank
  25 and every matrix slice has rank at most eight. This is one component
  of the second coefficient, not a bound on the complete second jet.

These results hold over Q, with the leading maps normalized exactly over
Q(zeta_6). They apply over C. Constant final projections that preserve the
two four-dimensional leading images can be folded into the regular maps.
Rank-reducing projections and other leading flags are outside the explicit
classification. No assertion about all higher jets follows.

Run from the repository root:

```sh
python research/ai/2026-10-21-quantum-extension-spaces/extensions.py \
  --output results/local/quantum-extension-certificates.json
python -m unittest discover -s tests -p 'test_quantum_extension_spaces.py' -v
```

The frozen report is in `results/quantum-extension-spaces-2026-10-21/`.
Ranks use rational row reduction and independently replayable nonzero
minors modulo 786433. The modular minors certify lower bounds over Q;
the exact nullspaces and rational reductions supply the upper bounds.

## Next construction question

Can any point of this linear first-jet space be lifted to regular P(t),Q(t)
whose saturated 112-dimensional rowspace contains M(10,10,11)? The first
remaining coefficient has contributions from P2 Q0, P1 Q1 and P0 Q2.
Changing only the P1 Q1 term or optimizing a truncated residual is not a
complete answer. A positive result must supply all local maps and verify
the full Laurent limit and the existing exponent implication.
