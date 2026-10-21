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

## Conditioning checks

The first unrestricted warm L-BFGS run completed3000 iterations with final
relative error0.0183635703. The subsequent complex ALS run improved below
0.009. These are nonzero-residual numerical results.

A matrix-free Gauss-Newton implementation supplies both Jacobian products
and adjoint products. Its startup checks their adjoint identity and compares
the Jacobian to finite differences. A fixed tiny finite-difference step
suffered cancellation after block-normal preconditioning and failed the
check before optimization. The revised check uses Richardson cancellation:
for a cubic map, (4 D(h/2)-D(h))/3 removes the central-difference cubic term.
Three step sizes are reported. The preconditioned check errors were about
4.7e-11,4.7e-10,4.7e-9. No failed check was treated as successful verification.

The unpreconditioned Gauss-Newton run was stopped after slow progress. The
preconditioned run and ALS remain numerical exploration. Preconditioning
uses invertible fixed source-coordinate changes from each leg's initial
normal matrix; it does not change the polynomial equations.

`balance_target.py` applies target vertex changes of basis, which fix the
matrix multiplication tensor. Its positive control replays the exact
M(5,5,3) seed after balancing. On one approximate M(5,5,4) checkpoint,
the combined map norm dropped from51.17 to28.76, but relative error rose
from0.00642 to0.03769. The residual is not invariant under a nonunitary
change of basis. The transformed seed therefore requires fresh optimization;
its lower norm is not an improvement in construction accuracy. This also
shows why raw map norm growth alone cannot establish a singular limit.

## Sparse derivative checkpoint

The derivative has only135 complex entries per output coefficient:45 from
each leg. An explicit sparse derivative therefore replaces repeated physical
matrix contractions inside Krylov iterations. Its independent adjoint and
cubic Richardson checks pass before optimization. A100-evaluation run with
150 Krylov iterations per linear solve completed in202 seconds, improving
the relative residual to0.0024169483467. Its saved hexadecimal maps still
have nonzero residual and are not a restriction certificate.

The numerical infinitesimal-symmetry diagnostic considers source sl2^3
and traceless target vertex actions. The exact M(5,5,3) positive control has
three null directions; the enlarged approximate candidate has no numerical
null direction at the stated threshold. This does not exclude a different
symmetry or prove anything about a limiting map. The candidate's precise
input file hash is retained beside the diagnostic.

Source SL2^3 balancing, unlike target balancing, preserves the entire
computed output tensor. One numerical norm optimization checked that output
to relative drift below6e-14, but reduced the norm only slightly. It does not
prove a bounded or unbounded limit. The solver continues from the saved
sparse checkpoint with refreshed conditioning and a larger linear-solve
budget. Optional numerical dependencies are separate from exact verification.
