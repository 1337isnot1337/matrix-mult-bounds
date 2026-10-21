# Leave the equivariant ansatz

The exact rectangular seed and its symmetry-class barriers motivate a
search with every coefficient of all three source maps free. No result in
this file certifies a new restriction or exponent improvement.

The first full-map L-BFGS experiment starts near the exact M(5,5,3) seed
embedded in M(5,5,4). It converges to relative error approximately0.5,
consistent with retaining only the original block. This numerical failure
is not used as an exclusion.

A second experiment imports the earlier three-quotient complex A33 to M5
numerical seed, preserving its provenance and recorded NPZ hash. Source
indices on B and C are permuted into the uniform physical-trace convention.
Before any cropping, its complete relative error is independently recovered
as0.1699480068188626. Cropping the third target vertex to its first four
coordinates gives initial relative error0.1260903260131934.

`unrestricted_search.py` optimizes the full complex coefficient maps using
an analytic gradient, with a directional finite-difference check before
optimization. `unrestricted_als.py` alternately solves the full linear least
squares problems on each leg. Both compute the entire output tensor, log
residuals and map norms, and save numerical maps only as discovery data.
The warm run and subsequent ALS are ongoing at this checkpoint.

Run with OPENBLAS_NUM_THREADS=1 to avoid unnecessary BLAS oversubscription.
Exact acceptance requires rational or algebraic maps and a complete original
source replay. Bounded-looking finite map norms do not prove convergence;
a residual tending to zero alone does not distinguish a restriction from
a degeneration.
