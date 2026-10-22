# Cyclic source calibration and the regular-unit obstruction

The [all-order unit-chart proof](unital_chart.md) excludes A4 to M(10,10,11)
when one long map is regular with full-rank limit and a target identity has
a regular source lift with invertible limiting slice. The other maps can
have arbitrary finite Laurent poles. The two hypotheses are retained:
general singular A4 maps and the exponent question remain open.

The [source-calibration proof](proof.md) gives an explicit unimodular slice
for every A_a over every field. At sizes two through four, exact Krylov and
Bezout witnesses prove the full slice determinant reduced over C, and
normalized commutators attain full rank. These calibrations alone exclude
no matrix target. All written arguments remain unreviewed externally.

Run the two exact verifiers from the repository root:

```sh
python research/ai/2026-10-21-cyclic-slice-determinants/certify.py --verify results/cyclic-slice-determinants-2026-10-21/certificate.json
python research/ai/2026-10-21-cyclic-slice-determinants/unital_controls.py --verify results/cyclic-slice-determinants-2026-10-21/unital-controls.json
```

The root requirements suffice. The finite rank controls distinguish a raw
constant coefficient of a singular Laurent product from a genuine
regularized limit. Only the latter inherits the product rank bound. The
controls are not a formalization or a certificate of the complete all-order
proof. No smaller matrix multiplication exponent is claimed.
