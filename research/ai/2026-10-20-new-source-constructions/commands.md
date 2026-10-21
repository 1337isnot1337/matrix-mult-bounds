# Reproduction commands

Run from the repository root. Exact verification needs the maintained SymPy
dependency. Optional discovery also uses NumPy, SciPy, or Z3 as indicated by
the imports; the recorded environment is in `runtime.json`.

## Exact structural controls

```sh
python research/ai/2026-10-20-new-source-constructions/torus_exact.py --structure-only --output results/new-source-constructions-2026-10-20/structure.json
python research/ai/2026-10-20-new-source-constructions/general_target_orbit.py --maximum-m 7 --output results/new-source-constructions-2026-10-20/general-structure.json
python -m unittest discover -s tests -p test_nonmonic_target_orbit.py -v
```

Twelve exact tests passed. They include 200 size-four target-orbit controls,
140 all-degree target-orbit controls, twelve original-source coefficient
replays over `F3` and `F4`, selected-minor and integer-relation checks, and
rejection of zero targets and dropped pivots. Finite controls support the
implementation; the all-degree mathematical proof is in
`uniform_normalization.md`.

The two added controls check sixteen symmetric polynomial-pairing inputs
and sixteen elimination inputs across the two fields, reconstructing all
121 original tensor coefficients in each case.

The chamber controls reproduce the predecessor's coefficient system exactly
and check all 115 new nonpositive entries at eight finite-field inputs.

## Weight chamber discovery

```sh
python research/ai/2026-10-20-new-source-constructions/chamber_search.py --seed 829191 --samples 20000 --bound 900 --beta 100 --output results/new-source-constructions-2026-10-20/chamber-search.json
python research/ai/2026-10-20-new-source-constructions/chamber_system.py --structure-only --output results/new-source-constructions-2026-10-20/chamber-structure.json
```

The recorded integer sample is not an exhaustive chamber enumeration.

## Finite discovery queries

```sh
python research/ai/2026-10-20-new-source-constructions/torus_exact.py --order 3 --seed 20261020 --timeout-ms 180000 --max-models 4 --output results/new-source-constructions-2026-10-20/pivot-torus-f3.json
python research/ai/2026-10-20-new-source-constructions/torus_exact.py --order 4 --seed 20261020 --timeout-ms 180000 --max-models 4 --output results/new-source-constructions-2026-10-20/pivot-torus-f4.json
python research/ai/2026-10-20-new-source-constructions/torus_scale_search.py --order 3 --seed 20261021 --timeout-ms 180000 --output results/new-source-constructions-2026-10-20/pivot-torus-cubic-f3.json
python research/ai/2026-10-20-new-source-constructions/torus_scale_search.py --order 4 --seed 20261021 --timeout-ms 180000 --output results/new-source-constructions-2026-10-20/pivot-torus-cubic-f4.json
```

All four completed with `unknown` and reason `timeout`. Runtime can change
the result of a time-limited discovery run. The saved query is a more precise
description of its finite mathematical scope. Its losslessly compressed
bytes are retained; its uncompressed SHA256 is in the associated report.

Two additional formulations have separate saved discovery records:

```sh
python research/ai/2026-10-20-new-source-constructions/symmetric_pairing.py --order 3 --seed 20261021 --timeout-ms 60000 --output results/new-source-constructions-2026-10-20/symmetric-pairing-f3.json
python research/ai/2026-10-20-new-source-constructions/symmetric_pairing.py --order 4 --seed 20261021 --timeout-ms 60000 --output results/new-source-constructions-2026-10-20/symmetric-pairing-f4.json
python research/ai/2026-10-20-new-source-constructions/eliminated_torus.py --order 3 --seed 20261021 --timeout-ms 120000 --output results/new-source-constructions-2026-10-20/eliminated-torus-f3.json
python research/ai/2026-10-20-new-source-constructions/eliminated_torus.py --order 4 --seed 20261021 --timeout-ms 120000 --output results/new-source-constructions-2026-10-20/eliminated-torus-f4.json
```

All four returned `unknown` at their stated budgets. Their additional
shared-residue restriction and verification scope are stated in
`finite_formulations.md`.

The compatible chamber has separate finite queries and an alternate solver
run on its saved F4 query:

```sh
python research/ai/2026-10-20-new-source-constructions/chamber_system.py --order 3 --seed 20261021 --timeout-ms 120000 --output results/new-source-constructions-2026-10-20/chamber-f3.json
python research/ai/2026-10-20-new-source-constructions/chamber_system.py --order 4 --seed 20261021 --timeout-ms 120000 --output results/new-source-constructions-2026-10-20/chamber-f4.json
python research/ai/2026-10-20-new-source-constructions/chamber_sls.py --query results/new-source-constructions-2026-10-20/chamber-f4.smt2.gz --structure results/new-source-constructions-2026-10-20/chamber-structure.json --order 4 --seed 20261021 --timeout-ms 120000 --output results/new-source-constructions-2026-10-20/chamber-sls-f4.json
python research/ai/2026-10-20-new-source-constructions/chamber_f2.py --seed 20261021 --timeout-ms 120000 --output results/new-source-constructions-2026-10-20/chamber-f2.json
```

## Numerical discovery

The first historical run used the preserved unnormalized program. Copy its
snapshot beside the current program so its original relative imports and
predecessor hashes resolve; remove that temporary copy after the run.

```sh
cp research/ai/2026-10-20-new-source-constructions/snapshots/pivot_torus_initial.py research/ai/2026-10-20-new-source-constructions/pivot_torus_initial_replay.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/pivot_torus_initial_replay.py --seed 20261020 --starts 3 --max-nfev 1200 --real --free-bound 3 --log-bound 1 --output results/new-source-constructions-2026-10-20/pivot-torus-real.json
rm research/ai/2026-10-20-new-source-constructions/pivot_torus_initial_replay.py
```

The remaining programs optimize residuals after target normalization.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/pivot_torus.py --seed 20261020 --starts 2 --max-nfev 2500 --real --free-bound 3 --log-bound 1 --input results/new-source-constructions-2026-10-20/pivot-torus-real.json --output results/new-source-constructions-2026-10-20/pivot-torus-normalized-real.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/pivot_torus.py --seed 20261020 --starts 1 --max-nfev 10000 --real --free-bound 10 --log-bound 3 --input results/new-source-constructions-2026-10-20/pivot-torus-normalized-real.json --output results/new-source-constructions-2026-10-20/pivot-torus-wide-real.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/full_pivot_torus.py --pure-shared --max-nfev 3000 --input results/new-source-constructions-2026-10-20/pivot-torus-wide-real.json --output results/new-source-constructions-2026-10-20/full-pure-shared-real.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/full_pivot_torus.py --complex --max-nfev 3000 --input results/new-source-constructions-2026-10-20/pivot-torus-wide-real.json --output results/new-source-constructions-2026-10-20/full-complex.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/anchored_search.py --index 3 --value 1 --max-nfev 3000 --input results/new-source-constructions-2026-10-20/full-complex.json --output results/new-source-constructions-2026-10-20/anchored-complex.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-new-source-constructions/chamber_numeric.py --seed 20261021 --max-nfev 2000 --input results/new-source-constructions-2026-10-20/full-complex.json --output results/new-source-constructions-2026-10-20/chamber-complex.json
```

The archived pure-power run is now a known-excluded diagnostic, as proved
in `search_outcomes.md`. Reproducing it is not a proposed research direction.
No numerical report is a construction certificate.
