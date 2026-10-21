# Complete-flag Q64 searches and gauge diagnostics

## Status and scope

This package records six completed, bounded numerical searches for a
monomial Laurent degeneration from `Q(6,4)` to `M(5,4,5)`. Every search has
auxiliary rank zero. None supplies an exact restriction, degeneration,
nonexistence result, or matrix multiplication exponent improvement.

The maps and complete run histories are saved in the six
`q64-flag-*-checkpoint.json` files. Every saved best point is replayed on
all 576 source terms and all 10,000 target coefficient positions by the
separate standard-library contraction in `q64_experiment_replay.py`.
Here “separate” describes the implementation; it does not mean external
mathematical review.

The exact controls establish only the stated grading and gauge identities.
The numerical optimizer and its controls require optional NumPy/SciPy.
The default tests require neither package and run under `python -S`.

## Tensor, grading, and exact acceptance equations

The source is

\[
 Q(6,4)=\sum_{p,q<6;\ y,v<4}
 A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

Source flattenings are `6*p+q`, `9*y+s`, and `4*z+v`.
The target is

\[
 M=\sum_{i,k<5;\ j<4}a_{i,k}b_{i,j}c_{j,k},
\]

with flattenings `5*i+k`, `4*i+j`, and `5*j+k`.
The row powers are

\[
 w_A(i,k)=-\alpha_i-\gamma_k,\quad
 w_B(i,j)=\alpha_i-\beta_j,\quad
 w_C(j,k)=\beta_j+\gamma_k.
\]

The lexicographic choice is `alpha_i=20*i`, `beta_j=5*j`,
`gamma_k=k`. The refined choice adds 1,000 to `alpha_4` and `gamma_4`.
Both choices have 4,950 negative coefficient positions, exactly 100
zero-degree positions, and 4,950 positive positions. The 100 zero-degree
positions are exactly the unit coefficients of the target.

For finite constant row maps, an exact certificate must set every negative
coefficient to zero and every zero-degree coefficient to the target value.
Positive powers are allowed. No approximate residual is substituted for
these equations.

Regroup the coefficients into a 100-by-100 operator with row
`(i_A,j_B,k_C)` and column `(i_B,j_C,k_A)`. The target becomes the identity.
The operator weight is

\[
 h(i,j,k)=-\alpha_i-\beta_j+\gamma_k.
\]

The middle sign is negative for the stated row-power convention.
All 100 weights are distinct, and each coefficient degree is the row
weight minus the column weight. Thus exact acceptance gives
`E=operator(T)-I` strictly triangular in weight order, so `E^100=0` and
every trace `Tr(E^k)` vanishes. These necessary operator identities do not
replace full coefficient verification. In particular, vanishing of the
first three traces does not establish nilpotence.

The general null-cone viewpoint was motivated by Dumitriu et al.,
[arXiv:2610.13905v1, Section 2.3](https://arxiv.org/html/2610.13905v1).
The finite grading identities above are checked directly here.

## Actual search budgets and outcomes

| Search | Actual accepted ALS updates / optimizer steps | Stop | Best relative required-coefficient residual |
|---|---:|---|---:|
| Refined flag, unrestricted linear solves | 50 | Map-norm guard exceeded | 0.0878082888 |
| Lexicographic flag, unrestricted linear solves | 150 | Map-norm guard exceeded | 0.0759618428 |
| Refined flag, map norm budget 30 | 1,500 | Iteration budget | 0.1168790860 |
| Lexicographic flag, map norm budget 30 | 1,500 | Iteration budget | 0.0044163113 |
| Lexicographic flag, parabolic gauge, map norm budget 30 | 1,500 | Iteration budget | 0.0030015236 |
| First three moment penalties, map norm radius 40 | 600 / 674 function evaluations | Iteration budget | 0.0030084718 at best combined objective |

Both unrestricted runs had a planned ceiling of 1,500 updates. They stopped
earlier when a recorded map norm exceeded 1,000. The recorded maxima at
those stops were approximately 2,813 and 1,687. Their positive coefficient
norms were approximately 296,000 and 145,000. Saved best points and final
iterates can differ; the complete histories preserve both distinctions.

The two finite norm budgets use a shared ridge parameter within each
linear subproblem. An eigendecomposition and scalar bisection solve its
Frobenius-ball trust region. Mode balancing preserves the represented
tensor. All three maps remain within norm 30, up to floating-point error.

The moment run minimizes

\[
 \|P_{\le0}(T-M)\|_F^2
 +|\operatorname{Tr}E|^2
 +0.1|\operatorname{Tr}E^2|^2
 +0.01|\operatorname{Tr}E^3|^2.
\]

Each map is parameterized as `40*Z/sqrt(1+||Z||_F^2)`, which enforces an
open norm ball. Analytic gradients include this parameterization.
Three directional finite-difference checks have maximum relative
discrepancy below `1.30e-7`.

The first three absolute traces fell from approximately
`(0.000938, 1.3864, 295.19)` to
`(2.15e-5, 9.58e-6, 1.40e-6)`.
The unnormalized negative coefficient norm remained `0.0300231`, the
constant error norm remained `0.00192412`, and the positive coefficient
norm remained about `1233.731`.
The operator spectral-radius diagnostic was about `22.52`; its fourth
trace had absolute value about `17325.85`. These are unresolved necessary
conditions, not a distance from the nilpotent variety. Eigenvalues can be
sensitive for these highly nonnormal matrices.

The numerical identifiers called seeds in the ALS files do not introduce
randomness when an initial checkpoint is supplied. These continuations
were initialized from the stated saved maps.

## Physical parabolic balancing

Use an upper triangular matrix `G` on the `i` index of `A` and `G^-T`
on the `i` index of `B`; similarly use upper triangular `H` on the `j`
index of `B`, and upper triangular `F` on the `k` index of `A`, with the
inverse transpose on each paired leg. The three physical factors preserve
the matrix multiplication tensor.

For increasing `alpha`, `beta`, and `gamma`, conjugating these gauges by
the grading has a regular invertible diagonal limit. Therefore they
preserve the exact acceptance set. Equivalently, the induced operator
similarity preserves the strict triangular error space. The residual norm
away from that zero set can change.

For a pair of map covariances `g` and `h` in the bilinear-dual convention,
the squared norm after a gauge depends on `X=G*G` through

\[
 \operatorname{Tr}(gX)+\operatorname{Tr}(hX^{-1}).
\]

Its positive minimizer satisfies `X g X=h`. The upper Cholesky factor of
`X` gives a permissible triangular gauge with the same pairwise norm
minimum. The numerical implementation floors small covariance eigenvalues;
the resulting invertible triangular gauge still preserves the exact zero
set. Repeated sweeps are a conditioning procedure, not a convergence proof
for the tensor search.

An exact integer control uses `Q(6,4) direct sum D_103`, with all native
Q columns zero: 100 naive matrix terms and three positive-degree errors.
Upper physical shears preserve all required coefficients. The three
opposite shear orientations create respectively 5, 4, and 3 required
errors. The scalar cost 103 is solely a verifier control and is not a
matrix multiplication improvement.

## Fixing the diagonal-gauge freedom

Let physical real log-diagonal parameters be `x_i`, `y_j`, `z_k`.
They scale the three map rows by

\[
 e^{x_i+z_k},\qquad e^{-x_i+y_j},\qquad e^{-y_j-z_k}.
\]

Fixing `z_4=0` removes the one-dimensional kernel and leaves 13 parameters.
Write the 65 row characters as `q_r` and the original squared row energies
as `e_r`. The normalization minimizes

\[
 F(s)=\sum_r e_r\exp(2q_r\cdot s).
\]

Assume every target row is nonzero. The characters span all 13 directions.
Their positive dependence follows by summing the character identity over
all target terms: each A row occurs four times, and each B/C row five
times. Hence `F` is coercive and strictly convex and has a unique minimum.
Its stationary equations are

\[
 \sum_r q_r\|N_r\|^2=0.
\]

They force the three complete map norms to be equal and make the norm
derivative vanish along every physical diagonal gauge, including the
Laurent grading. A Newton solve computes this representative.

For the final moment point, the relative grading derivative before
normalization is approximately `-0.03555`. The 13 normalized stationarity
residuals are below `5.4e-14` relative to total squared map norm.
The required residual changes from `0.00300847` to `0.00293465`, and the
three norms become `29.95985`. Thirty parabolic sweeps followed by diagonal
normalization give equal norms `28.85219` and residual `0.00363057`.
Thus a remaining diagonal rescaling does not account for most of the
observed residual. The coefficient errors and invariant failures remain.

The derivative of the normalization is available for future searches.
Let `D_r=exp(q_r.s)`, `N_r=D_r M_r`,
`K=sum_r ||N_r||^2 q_r q_r^T`, and let `G_r` be an output gradient under
the convention `df=2 Re sum <G_r,dN_r>`.
Define `b=sum_r q_r Re<G_r,N_r>` and solve `K eta=b`. The pulled-back
gradient is

\[
 D_r\bigl(G_r-(q_r\cdot\eta)N_r\bigr).
\]

This follows by differentiating the stationarity equations. The optional
control checks three directional derivatives (worst relative discrepancy
below `1.18e-7`), all 13 gauge tangents, uniqueness along a perturbed gauge
orbit, and the complete positive-error tensor control. The normalizer was
used for diagnostics here; no additional optimizer run using its pullback
is claimed.

## Reproduction

Run the exact maintained controls without site packages:

```sh
python -S -m unittest discover -s tests -p test_q64_full_flag_controls.py -v
```

Replay all six saved coefficient arrays using only the standard library:

```sh
python research/ai/2026-10-20-paired-direct-sums/q64_experiment_replay.py \
  results/paired-direct-sums-2026-10-20/q64-flag-*-checkpoint.json
```

The remaining commands require the optional discovery packages NumPy and
SciPy. They do not change root requirements.

```sh
python research/ai/2026-10-20-paired-direct-sums/q64_full_flag_diagnostics.py \
  results/paired-direct-sums-2026-10-20/q64-flag-*-checkpoint.json --gauges

python research/ai/2026-10-20-paired-direct-sums/q64_flag_moment_search.py \
  --initial results/paired-direct-sums-2026-10-20/q64-flag-parabolic-checkpoint.json \
  --check-gradient-only

python research/ai/2026-10-20-paired-direct-sums/q64_torus_gradient_control.py \
  results/paired-direct-sums-2026-10-20/q64-flag-moment-checkpoint.json
```

The next structural search is the distinct M1-leading chart supplied by
the paired-construction lane. No successful construction in that chart is
part of this package.
