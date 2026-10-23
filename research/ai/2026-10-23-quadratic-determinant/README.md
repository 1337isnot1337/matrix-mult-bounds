# The quadratic source determinant and its two factors

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
limits the first alternative to dimension six. Thus any family of
dimension at least seven must lie in the degree-twelve locus and
contain an invertible coefficient matrix over the algebraic closure
(over the original field too if it is infinite).

Over Q, the package also proves the sharp dimension-six bound for
source-rank-at-most-fourteen linear families. Three explicit integer
polynomials span a rational three-space all of whose nonzero members
have source rank fifteen: clearing denominators and reducing modulo
two brings each to the merged seven-point binary certificate. Dimension
intersection then gives the bound, and a fixed-factor six-space attains
it. This rational result does not require a new binary census.

The general-field reduction does not prove a geometric rank-fourteen
dimension-six bound over arbitrary fields, irreducibility of the degree-twelve
factor, or a classification of its linear spaces. The geometric
hypothesis cannot be replaced by unexamined finite-field point tests.
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

From the repository root, with the root requirements installed,
reproduce the report and nine focused tests:

```bash
python research/ai/2026-10-23-quadratic-determinant/verify.py
python -m unittest discover -s tests -p 'test_quadratic_determinant.py'
```

[sources.json](sources.json) pins the original literal source, the
merged geometric-rank conventions and dimension references, the
classical orthogonal-group background, and the scratch discovery
records, including the inherited seven-point certificate used for the
rational bound. The proof does not depend on torsion, Mazur's theorem, or an
unmerged attainment package.
