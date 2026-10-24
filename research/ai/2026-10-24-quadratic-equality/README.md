# Geometric quadratic equality spaces in odd characteristic

For every field K of characteristic different from two, the six-dimensional
linear families in the nine bidegree-(2,2) coefficients whose literal R_(3,3)
source rank is geometrically at most fourteen are exactly

    {M:Mv=0} and {M:v^t M=0}, for nonzero v in K^3.

The [proof](proof.md) excludes a six-space through an invertible coefficient
matrix using a tangent quadratic form of rank at least five. It supplies the
singular six-space classification and descent to K. It covers nonsemisimple
symmetric Gram blocks and characteristics three and seven, where the Hessian
rank can equal five. No diagonalization of the two-by-two block is used.

Claim `AI-ODD-QUADRATIC-EQUALITY-001` is **proof-written-unreviewed**.
Same-session auditing and exact arithmetic are corroboration, not independent
review or formalization. No compatible tensor target or exponent improvement
follows. Characteristic-two equality families remain open.

The geometric hypothesis means det R vanishes as a polynomial on the family.
Finite-ground-field point checks alone do not imply it. All source row and
column endpoints are fixed in the theorem. The determinant identity and cap
are inherited from the [pinned determinant package](../2026-10-23-quadratic-determinant/README.md).
Sources, their exact hashes and the original scratch hashes are in
[sources.json](sources.json). No new external theorem is imported.

From the repository root:

```sh
python research/ai/2026-10-24-quadratic-equality/verify.py
python -m unittest discover -s tests -p test_quadratic_equality.py -v
```

The verifier uses exact symbolic three-by-three determinant coefficients and
two-by-two/three-by-three Hessian identities. It retains five modular controls
from the scratch, including the characteristic-three/seven rank-five examples
and a nonsemisimple F5 block. They are finite implementation checks, not an
exhaustive census or the proof of a uniform rank bound. The saved report is
`results/quadratic-equality-2026-10-24/controls.json`.
