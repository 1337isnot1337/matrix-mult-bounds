# Fixed leading maps, a free corner kernel, and a partial corner target

These two completed bounded experiments produced no exact tensor map.
The first retains the exact endpoint M1 leading point while allowing its
corner kernel to move. The second asks the reduced endpoint corner for
M4 with its four diagonal A coordinates omitted. Both use zero auxiliary
scalar summands. Neither experiment proves nonexistence or improves the
matrix multiplication exponent.

## Fixed M1 lead with a free corner kernel

The source is

\[
Q(6,4)=\sum_{p,q<6;\ y,v<4}A_{p,q}B_{y,q+v}C_{p+y,v},
\]

with source indices `6*p+q`, `9*y+s`, and `4*z+v`. The target is
M(5,4,5), with coordinates `5*i+k`, `4*i+j`, and `5*j+k`.
The row powers are

\[
w_A=-[i>0]-[k>0],\qquad w_B=[i>0],\qquad w_C=[k>0].
\]

The [previous exact leading-point calculation](q64_m1_leading_history.md)
provides the endpoint old B and C rows. They give a rank-four leading
map \(H_0\), with

\[
K_0=\ker(f\otimes f),\qquad f(X)=(X_1,X_0+X_4),\qquad \dim K_0=32.
\]

This pilot holds those eight old long-map rows fixed. It also holds
the target A00 row fixed to source A11. All 24 other A rows are
parameterized in an orthonormal basis of K0; all 16 new rows of each
long map remain free. In particular, the 16 corner A rows are not
confined to the previously excluded subspace P tensor P.

The initialization uses the embedded exact Q(5,4) to M4 maps, extends
the first-map product space by t5, and perturbs the new long rows.
Seed 202610453, a Frobenius norm bound 30 on each complete map, and
1,500 ALS updates were prescribed. The per-update least-squares bounds
subtract the norms of the fixed rows from the available squared budget.
No target gauge or global mode balancing is applied during this fit,
because the leading rows must stay fixed. All 7,568 nonpositive
coefficient positions are required; all 10,000 positions are retained
in the saved-map replay. There are 576 source terms and 100 target terms.

The run completed all 1,500 updates, and its best sampled point was
its final point:

| Saved-point quantity | Value |
|---|---:|
| Required Frobenius error divided by 10 | 0.031212190729 |
| Negative coefficient norm | 0.297437424552 |
| Constant coefficient error norm | 0.094610060169 |
| Unrestricted positive coefficient norm | 421.540588021 |
| Each complete map norm | 30 |
| Smallest A singular value | 0.000393113761 |
| Non-old A rows times H0, Frobenius norm | 8.4e-17 |

The leading rows agree entry for entry with the integer seed. Thus this
run avoids the leading-rank drift of the earlier moving-leading pilots.
It still fails the coefficient equations and the corner compatibility
diagnostics below.

### Corner subspace diagnostics

Let H1 be the first-order cross map, with both old/new long-leg blocks
included. Sixteen independent corner A rows must lie in its kernel
inside K0. Thus rank(H1 restricted to K0) must be at most 16 in this
monomial chart. The saved singular-value tail after 16 is 0.7062929.

The 16 saved corner rows have smallest singular value 0.0521143.
Replacing them with an orthonormal basis of their row space changes
their first-jet residual norm from 0.2974374 to 2.7780718. This separates
the corner subspace test from the scale of its coefficient rows.

There is another necessary condition involving only a proposed corner
subspace L and the fixed old long maps. Define

\[
F_B(L)_{s,(u,j)}=\sum_{a,t} L_{u,a}(C_0)_{j,t}Q_{a,s,t},
\qquad
F_C(L)_{t,(u,j)}=\sum_{a,s} L_{u,a}(B_0)_{j,s}Q_{a,s,t}.
\]

All four old B rows annihilate F_B because L lies in K0. All 16 new
B rows must also annihilate it, to cancel the corner poles. The complete
B map must have rank 20: a rank-deficient map would make every member
of the Laurent family have deficient B flattening rank, a closed
condition incompatible with the target. Consequently rank(F_B) must
be at most 36 minus 20, or 16. The same argument applies to F_C.

At the saved orthonormal corner, both constraint matrices have numerical
rank 32 at relative threshold 1e-8. Their singular-value tails after
16 are 0.6830984 and 1.0087255. Singular values are numerical
diagnostics, not exact rank certificates; these values do not support
accepting the saved point as a compatible corner.

### Gauge diagnosis with the lead preserved

The physical diagonal subgroup with x0=z0=0 and middle factor equal
to the identity preserves every fixed leading row. It acts by

\[
a_{i,k}\mapsto e^{x_i+z_k}a_{i,k},\quad
b_{i,j}\mapsto e^{-x_i}b_{i,j},\quad
c_{j,k}\mapsto e^{-z_k}c_{j,k}.
\]

It includes the direction that suppresses negative powers and enlarges
positive powers. We minimized total squared map norm over these eight
real parameters as a diagnostic. This was not another optimization of
the tensor equations. The combined norm decreases from 51.9615 to
50.1547, and the required relative coefficient error becomes 0.0381814.
The resulting map norms are 35.3176, 26.8655, and 23.3753; this orbit
representative is not asserted to satisfy the original separate norm
budgets. The relative derivative along the prescribed grading decreases
from 0.3288345 to 4.6e-17. All fixed rows remain unchanged.

A separate known-gauge control starts from a prescribed diagonal
transform of the saved maps. Normalizing both inputs gives the same
representative to relative error 1.8e-13. This checks the numerical
gauge implementation; it provides no new degeneration.

## Reduced endpoint corner to diagonal-deleted M4

The source is the exact
[reduced endpoint corner R](../2026-10-20-paired-construction/m1_endpoint_corner.md),
of format 16 by 18 by 18 with 90 integer terms. Its native A basis is
P tensor P, where P is spanned by 1-t4, t2, t3, and t5.
The ordinary target retains the twelve A coordinates (i,k) with
i unequal to k, while keeping all sixteen B and sixteen C coordinates:

\[
\sum_{i,k<4,\ i\ne k}\ \sum_{j<4}a_{i,k}b_{i,j}c_{j,k}.
\]

There are 48 target terms and 3,072 coefficient positions. This is a
different target from full M4, which R cannot produce even by
degeneration under the separately proved corner obstruction.

The initialization uses the rational right inverse of the endpoint
product matrix that splits its duplicate pair (P1,w1) and (P3,w0)
equally. The interior source directions receive a small complex
perturbation, as do the endpoint columns. The A map initially selects
the twelve corresponding source A coordinates with the transpose
convention recorded by the replay. All three maps then vary freely.

Seed 202610454, a norm budget 20 per map, and 1,500 ALS updates were
prescribed. The target gauge consists of diagonal physical outer
factors and an unrestricted middle GL4 factor. Both preserve this
partial target. Every coefficient position enters the objective.

The run completed the full budget. Its best point was the final point,
with full relative coefficient error 0.356062746872, normalized by
the target norm sqrt(48). The maximum coefficient error is
0.763410435212. Each map norm is 9.30799349.

The complete singular spectra show one very small singular value on
each long map, approximately 3.6e-10 and 8.5e-11. At relative threshold
1e-8, both long maps and both long tensor flattenings have numerical
rank 15. There is no rank-14 claim. If a long flattening had exact rank
15, the target's sixteen equal singular values sqrt(3) would give a
relative error floor 0.25 for that flattening alone. Small computed
singular values do not prove exact rank, and this conditional floor
does not explain the entire observed residual or exclude other maps.

## Preservation, controls, and reproduction

Each saved checkpoint contains every complex map coefficient, the
complete 31-record sampled history, the actual 1,500-update stop,
and explicit zero auxiliary cost. The retained histories were compared
with all 62 original emitted JSON records; every field matched.
The mutable-ridge metadata error corrected in the previous checkpoint
does not occur in these pilots. Both maintained wrappers regenerated
their original initial map arrays entry for entry in the recorded
runtime; no optimization updates were repeated for this control.

The standard-library saved-map replays recover both reported errors
to less than 3e-16 absolute difference. A separately implemented exact
control restricts R to M(3,4,3) by retaining three independent endpoint
outer directions. It checks all 1,296 integer coefficient positions,
and detects a deliberately introduced sign error at four positions.
This smaller restriction is a calibration, not an exponent improvement.

```sh
python -S -m unittest discover -s tests -p test_reduced_corner_replay.py -v
python -S research/ai/2026-10-20-paired-direct-sums/q64_experiment_replay.py \
  results/paired-direct-sums-2026-10-20/q64-m1-fixed-leading-checkpoint.json
python -S research/ai/2026-10-20-paired-direct-sums/reduced_corner_replay.py \
  results/paired-direct-sums-2026-10-20/reduced-corner-offdiagonal-checkpoint.json
```

Optional NumPy diagnostics and discovery:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q64_m1_fixed_lead_diagnostics.py \
  results/paired-direct-sums-2026-10-20/q64-m1-fixed-leading-checkpoint.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/reduced_corner_diagnostics.py \
  results/paired-direct-sums-2026-10-20/reduced-corner-offdiagonal-checkpoint.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q64_m1_fixed_lead_search.py \
  --seed 202610453 --iterations 1500 --norm-budget 30 --prefix /tmp/q64-m1-fixed
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/reduced_corner_offdiagonal_search.py \
  --seed 202610454 --iterations 1500 --norm-budget 20 --prefix /tmp/reduced-corner
```

Different linear algebra runtimes can produce different numerical
trajectories. The saved coefficients and complete replays are the
record of the two completed finite experiments. No further identical
start is included in this package.
