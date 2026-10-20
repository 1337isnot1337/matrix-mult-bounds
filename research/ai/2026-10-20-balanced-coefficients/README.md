# Balanced coefficient equations and a Hensel certificate route

AI-assisted research, October 20, 2026. **No degeneration or exponent below
9/4 is proved here.** All written arguments are unreviewed. This package
continues the polynomial-flag investigation merged through PR #13.

The [exact elimination](elimination.md) replaces the 125 coefficients of a
restricted monic flag ansatz by 57 parameters satisfying 53 integer
polynomial equations, of degree at most 12. The 68 eliminated coefficients
are polynomial recurrences with integer coefficients, since the pivot
matrices are unimodular. The reduction applies over every field. Fixing all
pivots to one is an additional ansatz, not a general normalization theorem.

A solution over a finite field, together with a full-row-rank formal
Jacobian, would establish a characteristic-zero solution by multivariable
Hensel lifting and the Nullstellensatz. This is a sufficient acceptance
method using standard theorems, not a new lifting theorem. No qualifying
certificate has been obtained. Small-field solver failures and partial
numerical residuals provide no complex nonexistence result.

## Evidence and reproduction

Use root requirements.txt for the exact maintained controls:

```sh
python research/ai/2026-10-20-balanced-coefficients/coefficient_system.py
python -m unittest discover -s tests -p test_balanced_coefficients.py -v
```

The tests check all pivot inverses exactly, compare the reconstructed
constraints with independent direct multiplication, recover independently
specified monic maps, and replay finite-field equation evaluations. The
finite-field discovery modules import Z3 only in their command entry point.

Optional discovery uses the preceding package's numerical requirements or
z3-solver 4.15.3.0, with reports in results/balanced-coefficients-2026-10-20/:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research/ai/2026-10-20-balanced-coefficients/monic_projection.py --seed 9990128424963620090 --output /tmp/monic-m4.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research/ai/2026-10-20-balanced-coefficients/polynomial_pilot.py --seed 15718638889553417934 --input results/balanced-coefficients-2026-10-20/monic-m4.json --output /tmp/polynomial-m4.json
python research/ai/2026-10-20-balanced-coefficients/finite_field.py --prime 3 --output /tmp/field-three.json
python research/ai/2026-10-20-balanced-coefficients/field_four.py --output /tmp/field-four.json
```

Both numerical runs originally drew the saved seeds from os.urandom(8).
The monic pilot completed four starts with 600 evaluations each. Its smallest
masked residual was about 1.23e-8, but its full relative error exceeded
2.7 million at the best parameter in the recorded interval. The polynomial
pilot completed three starts with 800 evaluations each. Its two fresh starts
ended at condition norms about 0.0159 and 0.0315, with no exact solution.
The warm start exposed severe amplification after enforcing the eliminated
equations exactly. None of these numbers is an acceptance certificate.

The F2 solver returned UNSAT in the stated finite ansatz; no checked proof
trace is supplied. The F3 run returned unknown at its 120-second budget.
The F5 and F4 runs also returned unknown at their 120-second budgets. Exact
queries and source hashes are retained. snapshots/finite_field_f2.py pins
the original F2 entry point before the prime-field encoding was changed.
The maintained verifier does not import the snapshot.

The open construction question includes nonmonic pivots and arbitrary
Laurent input matrices. Even an exact size-four solution would need a
complete growth implication or an unbounded family before improving omega.
