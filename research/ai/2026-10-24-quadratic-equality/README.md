# Geometric quadratic equality spaces over every field

For every field K, the six-dimensional
linear families in the nine bidegree-(2,2) coefficients whose literal R_(3,3)
source rank is geometrically at most fourteen are exactly

    {M:Mv=0} and {M:v^t M=0}, for nonzero v in K^3.

The [odd-characteristic proof](proof.md) excludes a six-space through an invertible coefficient
matrix using a tangent quadratic form of rank at least five. It supplies the
singular six-space classification and descent to K. It covers nonsemisimple
symmetric Gram blocks and characteristics three and seven, where the Hessian
rank can equal five. No diagonalization of the two-by-two block is used.

The [characteristic-two proof](characteristic-two.md) classifies singular
five-spaces, normalizes them using permitted binary changes, and excludes
noncompression extensions by explicit source determinants and a leading-term
factor argument. It does not divide by two or infer geometry from a finite
census. Its first quartic expansion omitted adfi; same-session audit caught
and corrected that term before publication, with a regression against the error.

Claims `AI-ODD-QUADRATIC-EQUALITY-001` and `AI-CHAR2-QUADRATIC-EQUALITY-002`
are **proof-written-unreviewed**.
Same-session auditing and exact arithmetic are corroboration, not independent
review or formalization. No compatible tensor target or exponent improvement
follows. Compatible three-leg maps, submaximal families and larger blocks
remain separate questions.

The geometric hypothesis means det R vanishes as a polynomial on the family.
Finite-ground-field point checks alone do not imply it. All source row and
column endpoints are fixed in the theorem. The determinant identity and cap
are inherited from the [pinned determinant package](../2026-10-23-quadratic-determinant/README.md).
Sources, their exact hashes and the original scratch hashes are in
[sources.json](sources.json). No new external theorem is imported.

From the repository root:

```sh
python research/ai/2026-10-24-quadratic-equality/verify.py
python research/ai/2026-10-24-quadratic-equality/verify_char2.py
python -m unittest discover -s tests -p 'test_quadratic_equality*.py' -v
```

The verifier uses exact symbolic three-by-three determinant coefficients and
two-by-two/three-by-three Hessian identities. It retains five modular controls
from the scratch, including the characteristic-three/seven rank-five examples
and a nonsemisimple F5 block. They are finite implementation checks, not an
exhaustive census or the proof of a uniform rank bound. The saved report is
`results/quadratic-equality-2026-10-24/controls.json`.

The characteristic-two verifier checks five polynomial identities against
literal 15-by-15 determinants over F2 polynomial rings. It also checks the
corrected highest homogeneous part and coefficient-gcd certificates, plus
the binary coefficient-action formulas. These are symbolic identities;
no enumeration of finite-field families is claimed. Its report is
`results/quadratic-equality-2026-10-24/char2-controls.json`.
