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
