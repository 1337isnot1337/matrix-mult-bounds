# Higher conic jets

The [proof](proof.md) supplies two explicit finite incidence constructions:

- A fourth-order family for every complex a,b,d with d nonzero and c=-d^3.
  Its coefficients through order two equal PR107's mixed family.
- A tenth-order rational jet at a=1,b=2,d=1,c=-1, with the same prescribed
  coefficients through order two.

These are rank-twelve incidence jets of two fourteen-row maps. They
do not give an all-order curve, the full matrix target, or a smaller
matrix-multiplication exponent.

Run acceptance from the repository root with the maintained requirements:

```sh
python research/ai/2026-10-23-conic-higher-jets/verify.py results/conic-higher-jets-2026-10-23/rational-ten-jet.json
python research/ai/2026-10-23-conic-higher-jets/verify_symbolic.py results/conic-higher-jets-2026-10-23/mixed-fourth-family.json
python -m unittest discover -s tests -p test_conic_higher_jets.py -v
```

The rational verifier uses the Python standard library. The symbolic
verifier also uses the maintained SymPy version. Both contract the literal
4096-term source and do not call the discovery solver.

Discovery can be rerun separately:

```sh
python research/ai/2026-10-23-conic-higher-jets/discover_fourth.py --allow-third --symbolic --output results/local/conic-fourth-discovery.json
python research/ai/2026-10-23-conic-higher-jets/discover_higher.py --allow-third --through-order 10 --output results/local/conic-ten-discovery.json
```

The `--allow-third` flag in the generic continuation permits tangent
changes in the preceding coefficient, which is order n-1 at step n.
Intermediate witnesses are written beside the requested discovery output.
Positive acceptance depends on the exported maps, not on the reported
elimination dimensions. The failed fixed-third calculation is retained
as finite discovery evidence, with no universal nonexistence claim.
