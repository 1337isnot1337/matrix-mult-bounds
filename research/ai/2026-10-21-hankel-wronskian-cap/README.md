# Uniform Hankel-space caps and exact witnesses

A linear space of a-by-b Hankel matrices of rank at most r has dimension
at most r over every characteristic-zero field, when0<=r<min(a,b).
The [written proof](proof.md) uses an explicit binomial shear and a
Wronskian determinant. It is unreviewed. No historical priority, matrix
tensor construction, or exponent improvement is claimed.

This supplies the cap uniformly, without requiring a coordinate-subspace
certificate search for each new format. The earlier torus proofs and
certificate arrays remain valid and unchanged. The concurrent rectangular
worker's higher-ruling and saturation arguments retain their credit.
A cap on linear spaces is not a cap of r on a whole Segre image.

The rational witness generator takes any r+1 independent moment vectors,
finds a rank-greater-than-r integer combination, and exports a nonzero
original Hankel minor. It tries at most(r+1)(a+b-2-r)+1 integer shears.
This gives exact witnesses rather than a numerical rank test.

From the repository root with requirements.txt installed:

```sh
python research/ai/2026-10-21-hankel-wronskian-cap/verify.py --output results/hankel-wronskian-cap-2026-10-21/controls.json
python -m unittest discover -s tests -p test_hankel_wronskian_cap.py -v
```

To export a witness, pass `--basis-input input.json --output witness.json`.
The input has integer keys a,b,r and a list of r+1 rational moment rows:

```json
{"a":3,"b":4,"r":2,"basis":[[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,0,1]]}
```

Rational entries may be integers or fraction strings. The generator checks
basis dimensions and independence. It is implemented for rational inputs;
the all-field claim rests on the proof. The six focused tests pass, covering
4356 direct antidiagonal determinants,375 distinct-degree Wronskians, the
shear/translation identities, sharp spaces and exported witnesses. Full
repository regression is still required before this branch's merge request.
