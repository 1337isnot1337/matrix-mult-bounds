# Full coefficient search for a small paired degeneration

## Question and status

Does

\[
 P_3\unrhd M(1,3,3)\oplus M(3,3,2)
\]

admit a first-order degeneration that preserves the specified Cartan grading?
This is a smaller homologous construction problem for the unconstructed
`P10` target in `README.md`. Its source format is `(9,15,15)` and its target
format is `(9,12,15)`.

**No such construction was found.** Four finite alternating least-squares
runs and two bounded nonlinear least-squares runs all finished with nonzero
tensor residuals. These experiments neither prove nor disprove the
degeneration. The exact identities used to calibrate the verifier concern
different, smaller targets.

The `a=3` target passes all first-leg Koszul tests implemented in
`frontier.py`. The source minimum nonzero first-slice rank is nine. An
ordinary restriction can lose at most three ranks on the second leg and
none on the third leg, whereas the target has first slices of rank three.
Because its first leg uses all nine dimensions, an ordinary restriction is
therefore excluded by the adopted minimum-slice-rank argument. A successful
map must be genuinely singular.

## Exact grading and ansatz

The source coordinates and tensor follow `README.md`:

\[
 P_a=\sum_{p,q,y,v=0}^{a-1}A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

Source weights are

\[
 w(A_{p,q})=p+q,\qquad w(B_{y,j})=y+2a-2-j,\qquad
 w(C_{z,v})=2a-2-z+v.
\]

Every source term has total weight `4a−4`. For a matrix block, choose lists
`alpha`, `beta`, `gamma` and give its coordinates weights

\[
 w(a_{i,k})=\alpha_i+\gamma_k,\quad
 w(b_{i,j})=\beta_j-\alpha_i,\quad
 w(c_{j,k})=4a-4-\beta_j-\gamma_k.
\]

The two `a=3` allocations are

| Block | alpha | beta | gamma |
|---|---|---|---|
| `M(1,3,3)` | `[0]` | `[2,4,5]` | `[0,1,2]` |
| `M(3,3,2)` | `[0,1,2]` | `[2,4,6]` | `[1,2]` |

The target uses no more coordinates than the source in any weight space.
Each factor map preserves weights. There are 85 coefficients in one set of
three graded maps, so the two coefficient levels below have 170 parameters.

The Laurent model is

\[
 \varepsilon^{-1}(L_A+\varepsilon H_A)\otimes
 (L_B+\varepsilon H_B)\otimes(L_C+\varepsilon H_C)\;P_3.
\]

Writing `T_d` for its coefficient before division by `epsilon`, the complete
equations are

\[
 T_0=(L_A\otimes L_B\otimes L_C)P_3=0,
\]

\[
 T_1=(H_A\otimes L_B\otimes L_C+
 L_A\otimes H_B\otimes L_C+L_A\otimes L_B\otimes H_C)P_3
 =M(1,3,3)\oplus M(3,3,2).
\]

All 234 coordinates of each degree that are allowed by the grading are
checked, including coordinates outside the target support. Coordinates of
other total weights vanish identically under the imposed grading. Positive
powers after division by `epsilon` are unrestricted. The 468 coefficient
equations have not been solved exactly.

## Exact positive and negative controls

`exact_jet_coefficients` in `laurent_search.py` contracts every source term,
every target coordinate, and every choice of coefficient levels over the
rationals. It computes all degrees zero through three before the common
division by `epsilon`.

For the diagonal tensor `D2`, the standard elementary identity

\[
 \varepsilon^{-1}\big((e_0+\varepsilon e_1)^{\otimes3}
 -e_0^{\otimes3}\big)
\]

has the three-term `W` tensor as constant coefficient. The checker verifies
all eight coordinates of each degree, with nonzero coefficient counts
`[0,3,3,1]`. Changing the coefficient of the second diagonal summand from
`−1` to `−2` leaves the desired constant coefficient unchanged but introduces
a pole. The negative control explicitly detects that failure.

The separately maintained integer construction
`paired-construction/exact_p2.py` supplies `P2 -> M(2,2,2)`. Embedding its
maps as `L_A=0`, `H_A=A`, `L_B=B`, `H_B=0`, `L_C=C`, `H_C=0` gives a regular
instance of this Laurent model. All 64 target coordinates at each degree
are checked, and the nonzero counts are `[0,8,0,0]`. This control includes
the four off-support cancellations in that construction.

These checks validate coefficient accounting. They do not supply the
missing `a=3` or `a=10` degeneration. The exact controls are part of
`tests/test_paired_direct_sums.py` and require no numerical dependency.

## Completed alternating least-squares scope

The first method updates both coefficient levels of one factor/weight
space by a linear least-squares solve. Every tensor coefficient equation
enters the objective. Each global leading map is renormalized to Frobenius
norm one by an epsilon reparameterization that leaves `T1` unchanged and
rescales `T0` by a nonzero scalar. This prevents epsilon rescaling alone
from making the leading residual small, but does not bound the derivative
maps.

Four seeds `202610200` through `202610203` completed 300 iterations each with
ridge `1e−8`. The target has squared Frobenius norm 27. The combined relative
error is `sqrt(norm(T0)^2+norm(T1−target)^2)/sqrt(27)`.

| Seed | Final leading norm | Final target relative error | Best recorded combined relative error |
|---|---:|---:|---:|
| `202610200` | `0.0408571` | `0.243238` | `0.243365` |
| `202610201` | `0.0946565` | `0.176044` | `0.176984` |
| `202610202` | `0.128809` | `0.276052` | `0.277163` |
| `202610203` | `0.106214` | `0.0723873` | `0.0742920` |

The last row's best checkpoint occurred before its final iteration; its
final combined error is `0.0752180`. Derivative-map Frobenius norms grew
into the hundreds or thousands. The saved JSON reports contain every
recorded residual and map norm. These outcomes are failed searches, not
approximate construction certificates.

## Completed bounded refinement scope

`laurent_refine.py` uses SciPy nonlinear least squares with an analytic
Jacobian for the same complete 468 coefficient equations. It adds six
explicit gauge equations:

\[
 \|L_k\|_F^2=1,\qquad\langle L_k,H_k\rangle=0
 \quad(k=A,B,C).
\]

At an exact solution with three nonzero leading maps, these equations may
be imposed by epsilon reparameterization, scalar factor rescaling, and
adding a scalar multiple of `L_k` to `H_k`. The latter operation changes
`T1` only by a scalar multiple of `T0`. An exact solution with a zero leading
map would be an ordinary restriction, already excluded for this target.

The searches use real coefficients bounded in absolute value by ten.
Neither this coefficient bound nor the restriction to real, grading
preserving, first-order maps covers all possible degenerations. Gauge
residuals are reported separately and are never counted as tensor error.

Two runs completed their budgets of 300 function evaluations. One used an
independent random start (`202610210`); the other projected and clipped the
best saved fourth ALS start (`202610211`). Projection and clipping can
change the tensor coefficients away from an exact solution; the initial
residuals are recorded after those operations.

| Start | Final coefficient relative error | Largest coefficient error | Largest gauge error |
|---|---:|---:|---:|
| Independent random | `0.0842467` | `0.163190` | `0.0534475` |
| ALS checkpoint | `0.208823` | `0.242617` | `0.234280` |

Both runs reached the coefficient bound and the function-evaluation
budget. The analytic Jacobian was checked by a central directional
difference over all 474 equations at an independent point; the largest
discrepancy was `1.13e−11` with step `1e−5`. This is a numerical implementation
check, not exact verification of a proposed degeneration.

## Reproduction and evidence

Pure rational controls and the exact frontier controls:

```sh
python -m unittest discover -s tests -p test_paired_direct_sums.py -v
```

Numerical discovery additionally uses NumPy and SciPy. The bounded runs
record NumPy `2.3.5` and SciPy `1.17.0`. These are optional discovery
dependencies; exact verification does not require them. A representative
first-stage run is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/laurent_search.py --a 3 --seed 202610203 --iterations 300 --ridge 1e-8 --report-every 50 --checkpoint /tmp/paired-a3-als.json --output /tmp/paired-a3-als-report.json
```

The bounded independent start and controls are:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/laurent_refine.py --seed 202610210 --evaluations 300 --bound 10 --checkpoint /tmp/paired-a3-bounded.json --output /tmp/paired-a3-bounded-report.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/laurent_refine.py --controls --output /tmp/paired-laurent-controls.json
```

Passing `--start /tmp/paired-a3-als.json --seed 202610211` selects the recorded
warm-start procedure. JSON checkpoint files preserve the same binary64
values as the original local NumPy archives. The reports and exact control
results are in `results/paired-direct-sums-2026-10-20/`.

The grading helper is adopted from
`paired-construction/graded_search.py`. The finite first-leg rank formulas
and the source minimum-slice-rank bound are adopted through the local
dependencies recorded in `sources.json`. This package contributes the
small target allocation, Laurent coefficient objective and exact controls,
bounded refinement implementation, and the finite failed-search record.

**No smaller matrix multiplication exponent is established by these
experiments.**
