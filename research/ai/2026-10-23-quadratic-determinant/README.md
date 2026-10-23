# The quadratic determinant and sharp geometric dimension bound

Over every field of characteristic different from two, a linear
family of the complete quadratic biform block with geometric source
rank at most fourteen has dimension at most six, and six is attainable.
The geometric hypothesis means that the rank cap holds after extension
to an algebraic closure. Over infinite fields, a cap on every rational
point suffices; over finite fields that replacement is not asserted.

For the complete fifteen-by-fifteen crossed source R(M) associated to
a three-by-three biform coefficient matrix M, this package proves the
integer polynomial identity

    2048 det R(M) = det(M) det(2 adj(H)-tr(adj(H)) I),
    H=M^t J M J,     J=[[0,0,-2],[0,1,0],[-2,0,0]].

The [proof](proof.md) fixes the literal source ordering, derives a
dense three-parameter normal form, and verifies its two symbolic
parity-block determinants. Polynomiality then extends the identity
to every coefficient matrix and every characteristic. In characteristic
two the cleared identity becomes vacuous; the rank criterion requires
characteristic different from two.

For a linear family with geometric source rank at most fourteen, one
factor must vanish identically on the whole family: either the cubic
coefficient determinant or the degree-twelve invariant factor. An
elementary rederivation of the classical singular-matrix-space bound
limits the first alternative to dimension six. The second alternative
is excluded for larger spaces by an explicit local quadratic argument:
at any invertible coefficient member, three tangent directions carry
a nondegenerate ternary quadratic form. A seven-dimensional linear
family would force a two-dimensional totally isotropic subspace there,
which is impossible. [Theorem D and Section 8](proof.md) prove this
in every odd characteristic, including three, using formal coefficient
expansions rather than an analytic argument.

Over Q, the package also proves the sharp dimension-six bound for
source-rank-at-most-fourteen linear families. Three explicit integer
polynomials span a rational three-space all of whose nonzero members
have source rank fifteen: clearing denominators and reducing modulo
two brings each to the merged seven-point binary certificate. Dimension
intersection then gives the bound, and a fixed-factor six-space attains
it. This rational result does not require a new binary census.

The geometric dimension bound over arbitrary fields of characteristic
two remains unresolved here. The package also does not establish
irreducibility of the degree-twelve factor or classify all spaces
attaining dimension six. The geometric hypothesis cannot be replaced
by unexamined finite-field point tests.
No matrix-multiplication exponent improvement is claimed. The proof is
written and unreviewed; same-session checking is not independent review
or formalization, and no historical-priority claim is made.

The companion [verifier](verify.py) and saved
[report](../../../results/quadratic-determinant-2026-10-23/controls.json)
cover 29 exact rational coefficient matrices (five named and 24 seeded),
three additional rational controls from the explicit full-rank three-space,
18 odd-prime reductions, one characteristic-two boundary, and the exact
eight-by-eight and seven-by-seven parity blocks in three variables.
The 29 rational inputs replay the prior scratch controls rather than
constituting new discovery cases. The verifier imports no earlier
implementation and does not expand a general nine-variable determinant.
Five local curvature certificates (two over Q, one each over F3,F5,F7)
independently check 45 ordinary directional derivatives and 30
skew-direction second derivatives. The F5 example has a nontrivial
Jordan block, so this control also checks the absence of a
diagonalizability requirement.
These arithmetic controls supplement the written proofs. The full-suite
receipt at commit 5ea78f5 predates the addition of Theorem D and remains
a pre-extension baseline, not a validation receipt for the extended
proof.

From the repository root, with the root requirements installed,
reproduce the report and twelve focused tests:

```bash
python research/ai/2026-10-23-quadratic-determinant/verify.py
python -m unittest discover -s tests -p 'test_quadratic_determinant.py'
```

[sources.json](sources.json) pins the original literal source, the
merged geometric-rank conventions and dimension references, the
classical orthogonal-group background, and the scratch discovery
records, including the inherited seven-point certificate used for the
rational bound. The local quadratic argument imports no additional
structural theorem. The proof does not depend on torsion, Mazur's
theorem, or an unmerged attainment package.
