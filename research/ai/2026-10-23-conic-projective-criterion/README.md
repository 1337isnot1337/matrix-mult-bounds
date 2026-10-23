# Complete projective conic normal-class criterion

The theorem closes all missing projective base charts of the affine conic
criterion. Over complex parameters and for a nonzero normal direction, some
second jet, a formal extension, and an exact polynomial extension exist
exactly when

\[
(a_1r-a_0s)(b_1r+b_0s)(s\lambda^3+r\mu^3)=0.
\]

At every base point, the leading ranks remain 14, 14 and 12. The complete
tangent is 68 boundary directions plus two normal directions. Source reversal
swaps both conic homogeneous coordinates and the two normal coordinates.

The three new residual strata have complete source-operator certificates.
Eight saved polynomial families cover the cubic factor, and seven exact
linear-branch checks cover both linear factors. The finite mixed families
have degrees one and two in the curve parameter. All polynomial identities
hold with the original coordinate kernel fixed.

## Reproduction

Install the root requirements and run from the repository root:

```bash
python research/ai/2026-10-23-conic-projective-criterion/construct.py
python research/ai/2026-10-23-conic-projective-criterion/verify.py
python -m unittest discover -s tests -p test_conic_projective_criterion.py -v
```

The verifier imports no curve constructor. It rebuilds the complete tangent
and curvature certificates from the pinned source model, checks every saved
map coefficient with a separate 4096-term contraction, and proves the exact
chart transition on the whole maps. The focused suite caches one complete
acceptance run and adds corruption, degree, parser and chart-coverage controls.

`proof.md` states the hypotheses and establishes the equivalence. `sources.json`
preserves the predecessor attribution and exact byte pins. Saved results and
timed validation receipts are in `results/conic-projective-criterion-2026-10-23`.

The theorem concerns existence for a normal class with a freely chosen
boundary velocity. It does not prescribe a complete first or higher jet,
construct a target tensor, or improve a matrix multiplication exponent.
