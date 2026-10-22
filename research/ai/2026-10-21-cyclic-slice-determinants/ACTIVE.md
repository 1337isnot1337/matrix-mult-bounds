# Cyclic convolution source and regular unit charts

Question selected October 21, 2026: characterize a regular-unit singular
chart for A4 to M(10,10,11), and determine the available full-source slice
invariants, outside the owned leading-flag investigations.

Base: main f80ebf5. Branch: research/cyclic-slice-determinants-20261021.
Worktree: /tmp/matrix-cyclic-determinants.

Initial exact discovery: F(i,k,s)=1 when i+s=a-1 and k=a-1 gives an
invertible slice in sizes a=2,...,5. An elementary interval-block argument
proves its determinant is plus or minus one for every a>=1. For a=2,3,4,
one explicit pencil through that slice has squarefree determinant modulo
1009 and full degree. This rules out a repeated global determinant factor
in characteristic zero and therefore any nonconstant common divisor of
the full source's submaximal minors. It does not exclude tensor maps or
factor arguments after a restriction or a singular leading flag.

The unit-chart continuation proves that one regular full-rank long map
and a regular invertible source unit lift require pole order at least six
on the other long map. It allows arbitrary first-map poles and higher
regular coefficients. See unital_chart.md for every hypothesis; it does
not exclude singular unit lifts or long-leg limits that lose rank.

The completed source calibration gives an all-size integer proof and exact
standard-library Krylov/Bezout witnesses for three finite reducedness claims. The
finite-field discovery used optional NumPy; acceptance must not rely on it.
No independent review or exponent improvement is claimed.

Completed local evidence: four focused tests passed in 7.702 seconds,
for source calibrations, including full-rank normalized commutators, missing-family rejection and
false-formalization controls. Eighteen metadata tests and all five archive
replays passed. The source proof and verifier are in proof.md and certify.py; the unit
proof and finite rank controls are in unital_chart.md and unital_controls.py.

Existing S5 result: merged PR93. The separate F8 modular contribution is
PR96. Their validation histories are recorded in those pull requests.
