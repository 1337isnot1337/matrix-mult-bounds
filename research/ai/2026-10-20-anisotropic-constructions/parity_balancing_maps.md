# Numerical map search and target-vertex balancing

October 21, 2026. This file records numerical construction attempts and a
target-preserving gauge calculation. None of these runs found an exact
matrix multiplication restriction. No exponent improvement is claimed.

## Completed small-source searches

The initial question was whether complex mixed maps could extract M3, or
M3 direct sum M1 direct sum M1, from the parity110 face of A(2,2). These
targets have since been excluded by the
[pairwise-annihilator argument](parity_annihilator.md). The following
computations completed before that exclusion and are retained with
their actual scope.

| Target | Algorithm | Completed starts | Iterations per start | Best full relative error |
| --- | --- | ---: | ---: | ---: |
| M3 | Complex dense ALS | 16 | 1,000 | 0.46033987386131436 |
| M3 plus M1 plus M1 | Complex dense ALS | 16 | 1,000 | 0.5182005450485008 |
| M3 | Complex damped Gauss--Newton, warm ALS start | 1 | 150 | 0.459990669288956 |
| M3 plus M1 plus M1 | Complex damped Gauss--Newton, warm ALS start | 1 | 150 | 0.5179330294898563 |

Each reported residual includes every target coefficient: 729 for M3
and 1,331 for the direct sum. The parity source has 12 coordinates on
each leg and 48 nonzero coefficients. Seeds, trajectories, best maps
and control results are saved in the four result directories prefixed
`parity_balancing_small_` and `parity_balancing_gn_`.

For the small-source exclusion, shifted odd dimensions are all six.
At a D-dimensional direct sum target the annihilator argument requires
sum max(0,D-6) <= D. This excludes D=11. For the single M3 target D=9,
equality would require three nonzero annihilating matrix spaces with
total dimension at least nine. If r_X,r_Y,r_Z are their joint-image
dimensions, the defect in the rank bound is

\[
n^2-\sum_i r_i(n-r_{i+1})
=\frac{\prod_i(n-r_i)+\prod_i r_i}{n}.
\]

It is strictly positive when all three spaces are nonzero. Thus the
single M3 target is excluded as well. Failed numerical fitting is not
used as evidence for this theorem.

## A target-preserving balance operation

For the trace tensor of matrix multiplication, a vertex basis change P
acts on its two incident tensor legs as

\[
A\longmapsto P A,\qquad C\longmapsto C P^{-1}.
\]

Together with the identity on the third leg, these actions preserve
the exact target tensor. They can be applied independently at every
vertex and on every direct-sum block. In this statement A and C denote
the corresponding reshaped target-coordinate arrays of the source
maps; their remaining indices are included in the matrix products below.

Let G=A A^* be the outgoing vertex covariance and H=C^* C the incoming
one. For positive definite covariances, minimizing the sum of the two
incident map norms over positive P is equivalent to minimizing

\[
\operatorname{tr}(G X)+\operatorname{tr}(H X^{-1}),
\qquad X=P^*P>0.
\]

The stationary equation and its positive solution are

\[
X G X=H,\qquad
X=G^{-1/2}(G^{1/2}H G^{1/2})^{1/2}G^{-1/2}.
\]

Taking P=X^(1/2) balances the two transformed covariances. This gives
a genuine target gauge, without assuming that arbitrary restriction
maps may be made coisometric.

For an approximate image, a nonunitary target gauge changes the norm
of the residual, even though it preserves the exact target. The
implementation therefore regularizes small covariance eigenvalues,
bounds the eigenvalues of P, and accepts a gauge step only when the
full residual decreases. No gauge steps were accepted during the two
warm Gauss--Newton runs above. The operation was checked on a
deliberately unbalanced exact M2 control and left its residual zero.

## Gauss--Newton implementation and controls

[`parity_balancing_maps.py`](parity_balancing_maps.py) builds the full
complex holomorphic Jacobian of the three linear maps, solves damped
normal equations, and accepts only residual-decreasing steps. It
recomputes the full target tensor after each trial step. This routine
is explicitly limited to small Jacobians; it is not a large-target
matrix-free implementation.

An exact monomial A(2,2)-parity110 to M2 control has zero residual. The
Jacobian was checked along a complex direction against a central
finite difference, with relative discrepancy 2.293e-11. A gauge
transformation of an unbalanced version of the same control has zero
residual. These numerical controls check the implementation. They do
not turn the failed candidate fits into algebraic certificates.

## Full-source M14 seed search

The separate full-source experiment uses the
[integral mixed-basis M9 restriction](parity_structure.md), embedded in
the first nine vertices of M14. Its unperturbed image contains exactly
729 desired coefficients and no extra coefficient. Its relative target
residual is sqrt(2015/2744).

The full source is balanced by the existing binomial/Vandermonde
scaling. For example, its first-leg multiplier is

\[
\frac13\sqrt{\binom4i\binom4s/\binom8k}.
\]

The three cyclic copies give exact squared-coordinate marginals
1/225. The preconditioner replay checks all 675 equations with rational
arithmetic over all 15,625 source coefficients. This is a reproduction
of the previously recorded scaling, not a new theorem.

[`parity_balancing_full_search.py`](parity_balancing_full_search.py)
adds seeded noise to the original-coordinate M9 maps and then divides
the maps by the source scaling. This convention gives comparable
initial tensors regardless of preconditioning. The reports record the
core and scaling hashes, each start, and every retained residual.

The baseline uses two real and two complex starts with noise 0.3 and
60 ALS sweeps. A separate real continuation controls the observed
conditioning problem by imposing a decreasing singular-value floor
on the maps in original source coordinates, followed by ordinary ALS.
This is a discovery regularizer; it is not a restriction that may be
assumed without loss of generality. Its final objective is still the
unweighted error on all 7,529,536 coefficients of M14.

M14 alone is a useful possible construction component. It does not
satisfy the smaller-exponent gate by itself. The completed result
reports, rather than this description of the experiment, determine
its exact finished scope and best residuals.

## Reproduction

Run the exact balancing replays as described in
[`parity_balancing.md`](parity_balancing.md). Numerical experiments need
NumPy and SciPy. Set `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1` for
these small-matrix and sparse-contraction runs. The small ALS runs use
`dense_als.py` with `--a 2 --b 2 --source-mode parity110 --complex`,
the stated target, 16 starts and 1,000 iterations. Their seed ranges
are 202610211000--202610211015 and 202610212000--202610212015.

The Gauss--Newton runs use the corresponding best ALS arrays as
`--initial`, 150 iterations, and `--gauge-every 5`. The full M14 seed
search uses `parity_balancing_full_search.py`; its real and complex
seed ranges start at 202610214000 and 202610215000. All runs retain
floating-discovery status and keep `exact_witness_found` false.
