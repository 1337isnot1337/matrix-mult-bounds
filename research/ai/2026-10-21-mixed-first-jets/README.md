# A sixteen-parameter family of mixed second-order jets

Exact polynomial certificate, October 21, 2026. This is a partial formal
construction, not a matrix-multiplication target or exponent improvement.

The first-extension quotient ranks are **14 and 6**, attaining the mixed
rank-sum boundary in the adopted second-jet theorem. Sixteen independent
leading-row directions admit complete second-order corrections, for every
combination of their parameters. The [identity and scope](family.md)
specify what is verified and what remains to construct.

`seed.json` supplies the first rows and directions. `construct.py` rebuilds
the second derivatives and first-leg corrections by rational linear solves.
The separate `verify.py` contracts the 4096-term source and checks every
coefficient through order two, including all 136 quadratic parameter
monomials. This covers 171 complete identities on 100 first rows and
18-by-10 active output coordinates, without sampling parameters.

The frozen family and report are in `results/mixed-first-jets-2026-10-21/`.
From the repository root:

```sh
python research/ai/2026-10-21-mixed-first-jets/construct.py \
  --output results/local/reconstructed-mixed-twojet.json
python research/ai/2026-10-21-mixed-first-jets/verify.py \
  --output results/local/mixed-twojet-report.json
python -m unittest discover -s tests -p 'test_mixed_first_jets.py' -v
```

Tests independently evaluate a nontrivial parameter choice using the
original cyclic source coordinates and reject a changed second derivative.
Another test retains a nonzero third coefficient, preventing second-order
acceptance from being mistaken for an all-order identity. These are
generating-session checks, not independent review or formalization.

Next: construct higher coefficients, including unused output rows, and
determine whether the saturated first-row space can contain the matrix
target. The other worker's full boundary-spanning family remains a separate
investigation; this package uses mixed first rows.
