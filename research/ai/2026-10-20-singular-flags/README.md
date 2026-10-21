# Polynomial flags and exact discovery calibration

This AI-assisted research checkpoint concerns constant matrices on all three
legs of C(m,B), followed by target-compatible diagonal parameter weights,
over C. **No exponent below 9/4 is proved.** The all-size argument is written
and unreviewed; neither its finite controls nor repository CI are independent
mathematical review.

The [normal-form argument](normal_form.md) uses a common GL(2) source change
and target row operations whose conjugates tend to the identity. It places
both inputs in decreasing polynomial-degree flags and the output functionals
in increasing monomial-pivot flags. An equal-degree coefficient then cannot
vanish. This excludes the entire earlier m=4,B=10 weight order
eta=(7,14,21,0), and a separated cone of orders unless B>=N+m-1.
The latter additive cost does not close the asymptotic construction route.
Arbitrary Laurent input mixing is outside the reduction.

[Masked residuals](masked_residuals.md) explains a target-stabilizer direction
along which a partial fitting objective approaches zero although the full
tensor error diverges. The exact source-family negative control checks every
coefficient over Q. A later complex pilot at beta=100,
eta=(0,201,403,607) passes the leading-pivot screen. Its smallest partial
residual is about 5.25e-8, but its full relative error is about 61501 at the
best parameter in the recorded interval. It is not an approximate certificate.

The concurrent Koszul/scaling work already excluded constant shared maps
with regular invertible limit, dominant degrees, and several other weight
regions. Its graded-route note already warns that partial residuals omit
positive-weight terms. These results are complementary and are not credited
as discoveries here. The generic Wronskian and binary-form equivariance
arguments are elementary and proved in the note; no historical novelty is
claimed for those ingredients.

## Reproduction

Use root requirements.txt for the exact controls. From the repository root:

```sh
python -m unittest discover -s tests -p test_singular_flags.py -v
python research/ai/2026-10-20-singular-flags/flag_obstruction.py
python research/ai/2026-10-20-singular-flags/gauge_control.py
```

The exact controls verify both GL(2) source actions, the full normal-form
reduction on known m=2,3,4 degenerations, equal-degree coefficient products,
the stated separated-cone cases through m=8, target diagonal stabilizer
dimensions through m=6, both fixed-basis SAT witnesses without a solver,
and hashes of all four retained exact fixed-basis queries. Those fixed-basis
queries give m=2 positive controls and m=4 UNSAT in two restricted models.
No checked proof trace of the UNSAT answers is claimed.

Optional numerical discovery uses requirements-numerical.txt. The retained
balanced complex pilot ran with system NumPy 1.26.4 / SciPy 1.11.4:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research/ai/2026-10-20-singular-flags/complex_projection.py --seed 3326965624427666133 --starts 3 --max-nfev 500 --beta 100 --eta 0,201,403,607 --output /tmp/complex-balanced-m4.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 research/ai/2026-10-20-singular-flags/full_error.py results/singular-flags-2026-10-20/complex-balanced-m4.json --output /tmp/complex-balanced-full-error.json
```

The original run drew its seed from os.urandom(8). Providing that seed replays
the selected starts, without asserting bitwise equivalence across platforms.
The full-error diagnostic minimizes a convex log-sum of squared coefficient
errors over log(epsilon) in [-10,0]; its result is a floating diagnostic only.
The source hashes in the original report pin the maintained pilot and imports.

Historical scripts in snapshots/ retain the exact discovery sources for the
earlier reports, including their original scratch paths and optional Z3
dependency. They are provenance snapshots, not portable entry points. Their
reports record seeds, coverage and solver limits. Maintained exact replay
uses exact_flags.py and does not import the snapshots or Z3. The manifest
hashes package and report files, excluding itself and Python caches.

## Remaining construction question

The balanced and nearby weight orders remain open after this leading-flag
test. Exact coefficient equations in the polynomial flag coordinates, or
genuinely Laurent input families, are the next construction questions. A
finite solution alone still requires an unbounded family, full overhead
accounting and a complete exponent implication.
