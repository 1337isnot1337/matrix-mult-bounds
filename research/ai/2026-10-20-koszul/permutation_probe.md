# Intermediate-weight permutation pilot

October 20, 2026. Bounded floating discovery only. No exact certificate,
construction-class exclusion, or smaller exponent is established.

After the slice covers closed the replicated balanced direction, this pilot
tested m=4,B=10 and (alpha,beta)=(5,2). It used general dense real P,Q and
11 fixed nonaffine shared permutations. Source coefficient reflection pairs
the 24 permutations; retain the 12 with first image 0 or 1, and omit the
affine identity already covered by the fixed-coefficient obstruction.
This is a bounded set of starting points, not an exhaustive nonlinear search.

The program imports the concurrent worker's `problem` and analytic Jacobian
from `graded_shared_discovery.py`; that implementation is credited, not
reimplemented or counted as independent verification. Each run used 600
function evaluations, with seeds 202610200 through 202610210 in lexicographic
permutation order. All runs reached that budget. NumPy 2.5.4 and SciPy 1.18.1
ran with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.

All 11 final P,Q,G arrays and diagnostics are retained under
`results/koszul-2026-10-20/intermediate-permutations/`. The smallest partial
coefficient residual was about 1.34e-5, at shared order (0,2,1,3). Its P
matrix had smallest singular value about 1.38e-4. None supplied exact
rational matrices satisfying the coefficient conditions.

The full tensor was separately evaluated at 300 geometrically spaced epsilon
values from 0.05 to 1, for every retained fit. The smallest relative full
tensor error in this grid was about 3.078, also at (0,2,1,3). This is a finite
diagnostic, not minimization over every positive epsilon or a mathematical
lower bound. In particular the small partial residual did not demonstrate
a tensor degeneration.

The existing exact m=2 and m=3 positive controls also pass the rational
verifier with the new (5,2) weights. This checks the convention in a setting
with known certificates; it does not validate a floating m=4 candidate.

Reproduce discovery in an environment with the stated optional dependencies:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-koszul/permutation_probe.py
```

New runs write to ignored `results/local/intermediate-permutations/`.
Replay the retained full-tensor diagnostics without rerunning optimization:

```sh
python research/ai/2026-10-20-koszul/permutation_diagnostics.py results/koszul-2026-10-20/intermediate-permutations
```

Do not repeat these unchanged fits as new progress. The selected next route
is the finite spectral inequality in `finite_amplitude.md`; the general
singular source-degeneration problem remains open.
