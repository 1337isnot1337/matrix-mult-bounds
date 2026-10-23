# Finite covers for the nonsplit central sources

The exact full-source certificate gives SR(T_SL2F5)<=98, excluding the
selected M10 target, and a cube bound 6155844 for SL(2,F5) x C2. Cyclic
symmetry forces abc<=2481 for any single rectangular target from the
latter source, excluding the selected M(13,13,15). These statements apply
in characteristic two and to one-copy coefficient-one coordinate/
potential constructions over C. Arbitrary complex degenerations and
arbitrary higher-source-power constructions remain open. No smaller
exponent is established.

Read [proof.md](proof.md) for the argument and exact field hypotheses.
`AI-NONSPLIT-FINITE-COVERS-001` is written and unreviewed. The finite
matrix-multiplication slice-rank lower bound imports the externally
credited arbitrary-field bounded-rank matrix-space theorem.

From the repository root, standard-library Python suffices for acceptance:

```sh
python research/ai/2026-10-21-sl2-finite-slices/export_cover.py --output results/local/nonsplit-cover.json
python research/ai/2026-10-21-sl2-finite-slices/verify_cover.py results/sl2-finite-slices-2026-10-21/cover-certificate.json --output results/local/nonsplit-verification.json
python -m unittest discover -s tests -p test_nonsplit_finite_covers.py -v
```

The verifier regenerates the actual determinant-one group, checks rank
120 over F4, all 1728000 original coefficients, the one-copy covers and
the full block degree bounds. Its grouped integer count checks all 10648
coordinate-class triples with total multiplicity 13824000 for the cube.
It uses neither numerical packages nor the discovery support or lift.

`lift_pilot.py` and `cover_pilot.py` record discovery. The latter requires
optional NumPy/SciPy and exports integer coordinate sets; its floating
optimality bounds are not acceptance evidence. The characteristic-five
and bounded gauge experiments are separate discovery controls, not
premises of the F4 exclusions. All historical AI archives are preserved.
