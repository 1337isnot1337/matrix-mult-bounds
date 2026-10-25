# Quadratic families containing invertible coefficient matrices

The [written proof](proof.md) shows that a linear family in the nine
bidegree-(2,2) coefficients with geometric literal R_(3,3) rank at most
fourteen has dimension at most **four** if it contains an invertible
coefficient matrix and the characteristic is different from two and three.
Thus every such family of dimension at least five has singular coefficients.
This refines the previously established cap six and its equality classification.

The proof uses the pinned tangent determinants to force a constant Gram
ratio. Unique factorization then makes the Frobenius norm a square of one
linear form. Orthogonality puts a determinant-gradient direction back inside
the family, where its first two determinant coefficients give a contradiction.
Characteristic seven is handled before division by seven. Characteristics
five and 151 pass the first coefficient condition but fail the second.

Claim `AI-QUADRATIC-INVERTIBLE-STRATUM-001` is **proof-written-unreviewed**.
The audit and arithmetic checks are from the generating session. They are
not independent review or formalization. No sharpness example, characteristic
two or three bound, compatible tensor map, or exponent improvement is claimed.
Finite-field rational point checks do not replace the geometric hypothesis.

The [source registry](sources.json) pins the merged determinant and equality
packages and the unpublished October 24 derivation. No new external theorem
is imported. From the repository root:

```sh
python research/ai/2026-10-25-quadratic-invertible-stratum/verify.py
python -m unittest discover -s tests -p 'test_quadratic_invertible_stratum.py' -v
```

The saved exact report is
`results/quadratic-invertible-stratum-2026-10-25/controls.json`.
Symbolic identities, two modular boundary controls, and direct determinant
curve tests corroborate the proof. They do not enumerate linear families.
The proof also records a necessary linear-form identity for future work in
characteristic three; it supplies no dimension bound there.
