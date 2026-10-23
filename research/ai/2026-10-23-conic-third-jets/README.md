# Third-order lifts on the mixed cubic conic component

For every complex a,b,d with d nonzero and c=-d^3, PR101's specified
first jet admits an explicit rational third-order incidence lift after
changing its second coefficient. All coefficients belong to
Q[a,b,d,d^-1], with poles of order at most two in d.

An independent symbolic verifier reconstructs the original 4096-term
source and checks all 19600 moving-kernel coefficients at each of
orders one, two and three. Its leading minor determinants are 1,1,-1,
so both fourteen-row maps and the rank-twelve source contraction have
the required leading ranks everywhere on this chart. It imports no
discovery operator or predecessor tangent solver. The symbolic replay
uses SymPy from the root requirements.

The second universal backend, `verify_laurent.py`, uses only the Python
standard library. It represents coefficients as sparse Laurent polynomials
with rational coefficients and expands the three leading determinants
directly. It imports neither the SymPy verifier nor a discovery operator.
It checks the same chart, credited initial coefficients, second correction,
leading minors and incidence equations, and emits the same logical report.
The predecessor witness is checked against its credited SHA-256 pin.
The parser accepts bounded rational arithmetic in a,b,d, with division
only by nonzero rational monomials in d; it does not evaluate Python code.
Input budgets reject excessive syntax, powers and coefficient expansions.
This is an additional acceptance implementation, not a new mathematical
claim or independent mathematical review.

The earlier single rational point a=1,b=2,c=-1,d=1 retains its separate
standard-library verifier and corruption controls. These are local
rank-twelve incidence jets, not all-order curves or the full matrix
target. Claims `AI-CONIC-RATIONAL-THIRD-JET-001` and
`AI-CONIC-MIXED-THIRD-JET-002` are written and unreviewed. No exponent
improvement is established.

The [validation receipt](../../../results/conic-third-jets-2026-10-23/validation.json)
records the 850-test baseline, five historical replays and 34 combined
focused checks after integration of nonsplit main. Hosted CI must pass
the final combined head before merge.

Read [proof.md](proof.md), [QUESTION.md](QUESTION.md) and
[sources.json](sources.json). Discovery uses the credited PR101 tangent
operators. Acceptance uses the explicit maps and original-source
identities, without assuming completeness of those discovery systems.

From the repository root:

```sh
python research/ai/2026-10-23-conic-third-jets/verify_symbolic.py results/conic-third-jets-2026-10-23/mixed-family.json
python research/ai/2026-10-23-conic-third-jets/verify_laurent.py results/conic-third-jets-2026-10-23/mixed-family.json
python research/ai/2026-10-23-conic-third-jets/verify.py results/conic-third-jets-2026-10-23/third-jet-pilot.json
python -m unittest discover -s tests -p 'test_conic*third_jets.py' -v
```

Optional exact discovery can be repeated with `discover_symbolic.py`,
which writes to `results/local/mixed-conic-third-discovery.json`. The
earlier point search is `pilot.py --allow-second --output PATH`.

Next: handle the d=0 cubic fiber, then test fourth-order compatibility
with lower-jet freedoms. The finite point's current truncation has a
nonzero fourth Schur coefficient; that alone is not an obstruction to
adding higher coefficients.
