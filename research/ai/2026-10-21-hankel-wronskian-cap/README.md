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

Two further written refinements are included: [scalar-Hankel saturation at
the dimension equality](boundary_saturation.md), and the [one-dimensional
loss in proper crossed-rank sections](proper_sections.md). The latter closes
an ordinary A12 block configuration at384>383. The [finite application](application.md)
imports and credits the concurrent higher-input-rank and bundle bounds;
its balanced comparison is not a claim to replace the full all-source frontier.

The rational witness generator takes any r+1 independent moment vectors,
finds a rank-greater-than-r integer combination, and exports a nonzero
original Hankel minor. It tries at most(r+1)(a+b-2-r)+1 integer shears.
This gives exact witnesses rather than a numerical rank test.

From the repository root with requirements.txt installed:

```sh
python research/ai/2026-10-21-hankel-wronskian-cap/verify.py --output results/hankel-wronskian-cap-2026-10-21/controls.json
python research/ai/2026-10-21-hankel-wronskian-cap/geometry.py --output results/hankel-wronskian-cap-2026-10-21/geometry.json
python research/ai/2026-10-21-hankel-wronskian-cap/application.py --rectangular-output results/hankel-wronskian-cap-2026-10-21/rectangular.json --square-output results/hankel-wronskian-cap-2026-10-21/squares.json
python -m unittest discover -s tests -p 'test_hankel_*.py' -v
python -m unittest discover -s tests -v
python tools/replay.py
```

To export a witness, pass `--basis-input input.json --output witness.json`.
The input has integer fields a,b,r and a list of r+1 rational moment rows:

```json
{"a":3,"b":4,"r":2,"basis":[[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,0,1]]}
```

Rational entries may be integers or fraction strings. The generator checks
basis dimensions and independence. It is implemented for rational inputs;
the all-field claim rests on the proof. The six focused tests pass, covering
4356 direct antidiagonal determinants,375 distinct-degree Wronskians, the
shear/translation identities, sharp spaces and exported witnesses. The full
repository regression ran608 tests in844.203 seconds:605 passed and3 optional
tests skipped. All five protected archive replays passed. The first combined
Hankel run caught an invalid test expectation (13 dimensions in a24-dimensional
ambient space); the fixture was corrected to25, and the full run includes
that correction. The original failure log and its targeted resolution remain
in the result directory. These checks do not supply independent proof review.
