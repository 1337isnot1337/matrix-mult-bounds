# Second-order graded Laurent pilot

This experiment continues the small construction question in
`laurent_search.md`:

\[
P_3\unrhd M(1,3,3)\oplus M(3,3,2).
\]

**The two completed second-order searches did not find a degeneration.**
Both produced nonzero pole coefficients. A smaller error in the desired
target coefficient does not compensate for those poles.

## Model

Keep the source coordinates, target allocation, and Cartan grading from
the first-order experiment. Replace each factor by a degree-two map:

\[
\varepsilon^{-2}
(L_A+\varepsilon H_A+\varepsilon^2J_A)\otimes
(L_B+\varepsilon H_B+\varepsilon^2J_B)\otimes
(L_C+\varepsilon H_C+\varepsilon^2J_C)\;P_3.
\]

Every tensor coordinate allowed by the grading is included in each
coefficient equation. Degrees zero and one before division by epsilon must
vanish, and degree two must equal the complete target tensor. The equations
include all off-support positions. The other total-weight coordinates
vanish identically under the grading.

There are 255 real parameters, 702 coefficient equations, and nine gauge
equations:

\[
\|L_k\|_F^2=1,\qquad
\langle L_k,H_k\rangle=\langle L_k,J_k\rangle=0
\quad(k=A,B,C).
\]

For a true order-two solution with nonzero leading factor maps, norms can
be fixed by scalar factor rescaling and an epsilon reparameterization. The
orthogonality conditions can then be imposed by multiplying each factor
by a scalar power series with constant term one. Because the lower tensor
coefficients vanish, these scalar power series do not change the target
coefficient. Their terms above order two do not enter any checked equation.
This explains the gauges at an exact solution. During initialization,
projecting approximate coefficients can change the tensor, and the code
records its residual after initialization.

Coefficients are bounded in absolute value by ten. The search is therefore
limited to bounded, real, grading-preserving jets of this order. Numerical
failure does not exclude other coefficients, orders, gradings, or complex
degenerations.

## Controls

The exact rational coefficient checker uses the full identity

\[
\frac{(e_0+\varepsilon e_1)^{\otimes3}
      +(e_0-\varepsilon e_1)^{\otimes3}-2e_0^{\otimes3}}
 {2\varepsilon^2}
= e_1\otimes e_1\otimes e_0
 +e_1\otimes e_0\otimes e_1
 +e_0\otimes e_1\otimes e_1.
\]

The three diagonal source terms are assigned explicit rational factor
maps. Every coordinate of degrees zero through six is checked. The
nonzero coefficient counts are `[0,0,3,0,0,0,0]`. Changing only the constant
coefficient of the third diagonal summand introduces a pole without
changing the desired degree-two coefficient; the negative control detects
it.

The analytic Jacobian for the numerical model was independently checked
by a central directional difference over all 711 equations at a random
point. The largest discrepancy was `1.76e−11` at step `1e−5`. This checks
numerical indexing and differentiation, not a proposed target identity.

## Completed scope and outcomes

Two starts each completed 250 function evaluations with NumPy `2.3.5` and
SciPy `1.17.0`:

| Start | Seed | Pole coefficient norms | Target relative error | Full coefficient relative error |
|---|---:|---|---:|---:|
| Independent random | `202610220` | `0.0302242`, `0.309438` | `0.0346902` | `0.0691636` |
| Perturbed lift of bounded first-order checkpoint | `202610221` | `0.125262`, `0.212220` | `0.0345328` | `0.0586659` |

The full coefficient relative error is the square root of the sum of all
three coefficient-error squared norms, divided by the target Frobenius
norm `sqrt(27)`. The respective largest gauge errors were `0.00618159` and
`0.0103050`, and the largest absolute tensor-coordinate errors were
`0.0860921` and `0.0886324`. Both runs approached the coefficient bound and
stopped at the function-evaluation budget.

The lifted start substitutes the first-order derivative into degree two,
then adds a small seeded degree-one perturbation. Without that perturbation,
the degree-one variables would start at a symmetric stationary subspace of
the target-coefficient objective. Projection and clipping follow, with the
resulting initial residual explicitly recorded.

The reports, controls, and final JSON checkpoints are named
`higher-jet-*.json` in `results/paired-direct-sums-2026-10-20/`. They are
failed numerical construction attempts. They prove neither the existence
nor the impossibility of the target degeneration and give no improvement
of the matrix multiplication exponent.

## Reproduction

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/higher_jet_search.py --controls --output /tmp/higher-jet-controls.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/higher_jet_search.py --seed 202610220 --evaluations 250 --bound 10 --checkpoint /tmp/higher-jet-seed0.json --output /tmp/higher-jet-seed0-report.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/higher_jet_search.py --seed 202610221 --evaluations 250 --bound 10 --start results/paired-direct-sums-2026-10-20/laurent-bounded-a3-seed0-checkpoint.json --checkpoint /tmp/higher-jet-seed1.json --output /tmp/higher-jet-seed1-report.json
```

`higher_jet_search.py` adopts the grading helper through
`laurent_search.py`. It computes all coefficient contractions and their
derivatives explicitly; no external numerical residual is treated as a
tensor identity.
