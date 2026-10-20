# Verification and reproduction

## Evidence categories

A written proof is an argument for all parameters in its statement. A finite exact computation is evidence only for its enumerated domain. A symbolic identity establishes the identity, not every analytic step that uses it.

Independent review requires a reviewer who did not generate the argument, an identified commit, and a recorded scope. Lean verification requires a successful build of the relevant statement and its dependencies. A theorem-name match alone is insufficient.

The current local results have written arguments and finite reproduction. They have no independent review and no Lean build. External projects' reported builds are attributed to those projects.

## Recorded run

The initialization run used Python 3.13.5 and SymPy 1.14.0. Its exact payloads match all five archived reports. Timing and display-only floating values are excluded from payload comparison.

The replay first verifies all ten hashes in the original manifest. It runs programs in a temporary directory, rejects changed coverage or any reported violation, and verifies the archive again afterward.

```sh
python -m pip install -r research/ai/2026-10-20/requirements.txt
python -m unittest discover -s tests -v
python tools/replay.py --output results/local
```

The default timeout is 300 seconds per child process. The program makes no network requests. Its output directory is separate from the archive. Do not run with `-O` or `PYTHONOPTIMIZE`.

## Coverage

The scalar grid covers $1\le a,b\le128$. Replication covers $a,b\le32$ and $q\le8$. Four symbolic assertions supplement 73,856 grid assertions.

The filtration grid covers $1\le a,b,c,d\le12$. Its 20,736 source quadruples produce 353,664 matched-sector inequalities.

Binary weights lie in $\{0,1\}$, with minimum zero in each input, $2\le a\le b$, and $a+b\le11$. Ternary weights use $\{0,1,2\}$ and $a+b\le10$. These runs contain 12,976 and 209,692 candidates.

The random run contains 20,000 generated pairs, with lengths from 2 through 15 and entries from -8 through 8. Its seed is 20261020. These are candidate draws, not a claim of unique arrays or exhaustive coverage.

## Search limitations

Witness decisions compare exact `Fraction` values. The original monomial search chooses displayed best records using floating-point ratios. Those rankings are descriptive, not exact optimality certificates.

Sector recognition verifies convolution supports under the implemented coordinate orders and axis reversals. Other sectors receive only a single-slice dot-product lower bound. A failure to find a violation can reflect that weak estimate.

The search does not exhaust arbitrary weights, coordinate restrictions, basis changes, cancellations, or tensor powers. A finite violation of the model does not automatically improve the asymptotic exponent.

The Python tests do not validate the full shared-leg theorem, the external spectral framework, or every step in the determinant-filtration derivation. Those remain mathematical dependencies.

## Regression tests and continuous integration

The regression suite covers archive integrity, independent profile formulas, selected support invariants, exact recorded scores, and ledger consistency. The workflow runs those tests and the full replay. Its runtime status is separate from the local run recorded here.

## Product-filtration proof-chain checks

The maintained verifier checks the endpoint product bound, both Jensen bounds,
and domination of every label fiber, using exact rational arithmetic. Its six
regressions also check the necessary zero boundary, other normalized concave
profiles, and the elementary dot-product restriction in coefficients.

```sh
python research/ai/2026-10-20-concavity-equivalence/verify.py \
  --output results/concavity-equivalence-2026-10-20/verification.json
python -m unittest discover -s tests -p test_filtration.py -v
```

The recorded run uses Python 3.14.8. It covers 1,296 grid sources, 11,808
filtration inequalities and 5,184 intermediate bounds, plus six stress sources
with 4,860 inequalities. The [written proof](../research/ai/2026-10-20-concavity-equivalence/research_note.md)
establishes the all-size result; enumeration is not a replacement for its
argument. No independent review or Lean build is recorded.

The complete suite passed all 40 tests in the existing project virtual
environment (Python 3.14.8, SymPy 1.14.0). The five archived experiments also
replayed successfully and all ten manifest hashes matched before and after.
Receipts are under `results/concavity-equivalence-2026-10-20/`. The first system-Python
attempt failed because SymPy was absent; its test log is retained separately.
That dependency failure was resolved by using the existing virtual environment.

The follow-up analytic note has four exact symbolic/rational controls for an
actual flattening character, the critical shape, and the conditional fraction.
The initial control run compared two identical SymPy expressions structurally
and failed; the test now simplifies their difference before comparing to zero.
Both the initial failure and corrected result are retained. Those controls do
not prove the analytic limit, endpoint rigidity, or the uniform gain premise.

After the follow-up and path reconciliation, the full suite passed 44 tests
in the same virtual environment. The archived programs were not edited after
their successful replay; no redundant second full archive replay was run.

The all-degree fat-point follow-up adds three controls, bringing the passing
suite to 47 tests. Fifteen independent coefficient matrices (`a=1,...,5`,
every exterior degree) agree with the target rank formula. A symbolic integral
checks the lower envelope, and integer powers certify the conditional root
bound. These tests supply no convolution-source degeneration.

The following checkpoint passes 55 tests. It adds independent exact
homomorphism-kernel counts and two explicit graded coefficient controls,
including deliberate coefficient rejection. Numerical discovery scripts
additionally check their analytic Jacobian against finite differences; their
residuals are not used for mathematical acceptance.

The SL(2,7) source checkpoint passes 59 tests under the owned worktree's
virtual environment (Python 3.14.8, SymPy 1.14.0). Its three new controls derive
the complex block dimensions, check exact integer root intervals including
boundary cases, and reject a deliberately excessive source cost. The graded
verifier also rejects floating entries. The recorded transcript is
`results/sl2-seven-2026-10-20/tests.txt`.

```sh
.venv/bin/python research/ai/2026-10-20-sl2-seven/source_certificate.py \
  --output results/sl2-seven-2026-10-20/source-certificate.json
```

The source calculation uses exact SymPy arithmetic. Search discovery additionally
uses NumPy, SciPy and python-sat 1.9.dev17; accepted group potentials are checked
by the pinned integer-only verifier. No SAT timeout, floating fit, or source
cost certificate supplies the missing target degeneration.
