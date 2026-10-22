# Split-cover finite cube exclusion

The full characteristic-two tensor of A5 x C2 has a third-power slice
cover of 973422. Cyclic symmetry and finite SR(M_m)=m^2 force abc<=986
for any single rectangular target M(a,b,c). This excludes one-copy
coefficient-one coordinate/potential M10 and M(9,10,11) constructions over C.
It does not exclude arbitrary complex degenerations or targets in the
nonsplit central covers. No exponent improvement is established.

Read [proof.md](proof.md) for the exact scope and the characteristic-free
target lower-bound argument. Claim `AI-SPLIT-COVER-CUBE-EXCLUSION-001` is
written and unreviewed. Flanders's bounded-rank matrix-space theorem is
external, cited through de Seguins Pazzis's arbitrary-field formulation.

From the repository root, with standard-library Python:

```sh
python research/ai/2026-10-21-central-cover-finite-slices/export_cover.py --output results/local/central-cover-cover.json
python research/ai/2026-10-21-central-cover-finite-slices/verify_cover.py results/central-cover-finite-slices-2026-10-21/cover-certificate.json --output results/local/central-cover-verification.json
python -m unittest discover -s tests -p test_central_cover_finite_slices.py -v
```

The polynomial producer and coordinate-counting verifier are separate.
The verifier reuses the preceding maintained F4 arithmetic primitives,
rechecks every full A5 coefficient and counts all 1728000 cube coordinates
on one leg. Acceptance uses no optional numerical package or optimizer.
Saved output and validation receipts are in
[`results/central-cover-finite-slices-2026-10-21/`](../../../results/central-cover-finite-slices-2026-10-21/).
