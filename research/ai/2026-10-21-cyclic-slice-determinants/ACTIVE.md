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

The unit-chart continuation proves an all-order exclusion when one long
map is regular with full-rank limit and a target identity lifts regularly
to an invertible source slice. All other maps may have arbitrary Laurent
poles. A regularized rank-two product gives the stronger source pole
ceiling6; no finite pole-order cap is needed. See unital_chart.md. Singular
unit lifts and rank-deficient long-leg limits remain open.

The completed source calibration gives an all-size integer proof and exact
standard-library Krylov/Bezout witnesses for three finite reducedness claims. The
finite-field discovery used optional NumPy; acceptance must not rely on it.
No independent review or exponent improvement is claimed.

Completed local evidence: four focused tests passed in 7.702 seconds,
for source calibrations, including full-rank normalized commutators, missing-family rejection and
false-formalization controls. Eighteen metadata tests and all five archive
replays passed. The source proof and verifier are in proof.md and certify.py; the unit
proof and finite rank controls are in unital_chart.md and unital_controls.py.

Current integrated validation: eight focused tests passed after importing
the entire discovered suite (4.145 seconds), and 18 metadata checks passed.
The earlier 811-test collection passed in 2165.154 seconds before the all-order
unit extension and the final main integration; it is not exact-head evidence
for those additions. Current-head CI and coverage belong in the topic PR.

Existing S5 result: merged PR93. The separate F8 modular contribution is
PR96. Their validation histories are recorded in those pull requests.
