# Graded cyclic-source construction attempts

October 20, 2026. AI-derived finite experiments and fixed-map certificates;
unreviewed. **No new matrix degeneration or exponent bound is established.**
This continues the exact [A2 to M(2,3,4) construction](../2026-10-20-cyclic-mixed-map/README.md),
claim AI-CYCLIC-MIXED-RESTRICTION-046. The new experiment is
EXP-CYCLIC-GRADED-PILOTS-049.

## Exact fixed-map obstruction

Truncate the integer M(2,3,4) witness to the first three values of k. The
result is M(2,3,3), with maps A0,B0,C0 of shapes 6x12,9x12,6x12. Extend
the i vertex from two to three values. Give the new i value weight +1,
the old ones weight zero, and use the target-preserving weights

    alpha(i,j)=u_i+v_j, beta(j,k)=-v_j+w_k, gamma(k,i)=-w_k-u_i.

With v=w=0, every new C row has degree -1. It must lie in the common
kernel V_C of contractions with A0 and B0, or a negative coefficient
survives. The 54x12 matrix V_C has rank 10 and kernel basis

    (-1,0,0,0,0,0,1,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,1,0,0,0).

Three new C rows cannot be independent in this two-dimensional space.
Conciseness of M(3,3,3) requires independent rows, so this fixed extension
fails. Reversing the sign of u_new requires three new A rows in V_A,
the common kernel of B0 and C0. Here V_A has rank 12 and zero kernel.

The earlier rational M(2,3,3) witness has zero kernel in both directions.
The saved certificate gives nonzero maximal minors and complete nullspace
bases for all four matrices. The checker reconstructs the matrices from
the two retained exact witnesses, verifies each minor and all kernel
equations, and checks independence. The integer-derived minors have
determinant 1; those two obstructions also hold over every field. The
rational witness calculation is stated over C.

These results keep the old maps fixed. They do not exclude changing those
maps, using other weight patterns, higher Laurent terms, or general
degenerations A2 to M3. The positive M(2,3,4) identity remains valid.

## Completed numerical pilots

Constant dense 9x12 maps were fitted with target-vertex weights of the
displayed form. The equations impose exact M3 coefficients at degree zero
and zero coefficients at negative degree; positive-degree coefficients are
omitted. Only an exact solution would certify this degeneration class.

Two runs each completed 16 real starts, seeds 202610380 through 202610395,
500 alternating least-squares sweeps each. The first four starts use
u=(0,1,3), v=(0,2,6), w=(0,4,12). Later starts sample three distinct
values in [-5,5] for each vertex. Noise scales .03,.1,.3,1 repeat in order;
the base point is the integer witness truncated and embedded in M3.
The second run additionally balances the target's diagonal stabilizer
after each sweep, with at most 30 coordinate sweeps per balancing call.

| Run | Best masked relative residual | Exact certificate |
| --- | ---: | --- |
| Equalized map norms | 0.006498427056481416 | None |
| Additional diagonal stabilizer balancing | 0.0205536333452965 | None |

Levenberg-Marquardt refinement of both retained best iterates used an
analytic Jacobian, eight quadratic diagonal moment equations, and 1000
function evaluations each. The final masked residuals were
0.019433266634971393 and 0.014661938591845714. The latter had map norms
about 7600 and a largest unweighted coefficient about 8.30e8. Moment
residuals also remained nonzero. These are completed unsuccessful pilots,
not exclusion proofs. Reports and four actual saved iterates are retained
in `results/cyclic-singular-search-2026-10-20/`.

The numerical Jacobian control uses a scale-dependent finite-difference
step and a relative error threshold 1e-6. An initial absolute-error check
was inappropriate at the large second initialization and aborted before
optimization; the corrected check and both refinements were rerun. No
floating residual is used by the exact certificate checker.

## Why the masked loss is insufficient

This repeats and makes explicit for the present target the warning already
recorded by the [singular-flags worker](../2026-10-20-singular-flags/masked_residuals.md).
For M2 set u=(0,1),v=(0,2),w=(0,4). The coordinate terms at (0,0,1) and
(2,0,0) have degrees -1 and +1. Add both terms to M2 and apply the gauge
R to these weights. The target terms remain unchanged; the negative
coefficient becomes 1/R while the omitted positive coefficient becomes R.
The masked loss tends to zero although the full squared error is
R^2+R^-2 >= 2. This diagnostic example does not assert that its tensor
has no degeneration by some other maps. Balancing is a useful numerical
control, not a compactness theorem or an acceptance certificate.

## Reproduction

From the repository root, using the maintained requirements:

```sh
python research/ai/2026-10-20-cyclic-singular-search/verify.py
python -m unittest discover -s tests -p test_cyclic_singular_search.py -v
```

Optional discovery scripts require NumPy and SciPy (the completed run used
2.5.4 and 1.18.1). They write only to ignored `results/local/`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-cyclic-singular-search/discovery/weighted_cyclic_m3.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-cyclic-singular-search/discovery/weighted_cyclic_m3_balanced.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-cyclic-singular-search/discovery/refine_weighted_cyclic_m3.py
```

These discovery runs are not CI acceptance checks. Numerical trajectories
can vary across library and BLAS versions. There is no historical priority,
independent mathematical review or formalization claim.
