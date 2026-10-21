# Bounded Q(6,4) extension searches

## Outcome and scope

Sixteen completed numerical searches tested
\(Q(6,4)\oplus D_r\) against \(M(5,4,5)\), where \(D_r\) is a
direct sum of exactly r rank-one scalar tensors. None supplied an exact
restriction or degeneration. None proves that the requested map is
impossible. No smaller matrix multiplication exponent follows from
these experiments.

All runs completed their stated budget of 3,000 alternating updates.
The package retains every map coefficient, seed, complete reported
iteration history, scalar cost, and coefficient objective. A separate
standard-library contraction replays all sixteen saved points.

The successful preceding finite construction is
[Q(5,4) to M4](q54_numeric_candidate.md). Its product-subspace method
requires twice the target outer dimension to be at most the source
convolution output dimension. For Q(6,4) and target outer dimension
five, this would require 10 to be at most 9. The present target was
chosen to test beyond that limitation.

## Source, target, and objective

The source is

\[
Q(6,4)=\sum_{p,q<6}\sum_{y,v<4}
A_{p,q}B_{y,q+v}C_{p+y,v},
\]

with dimensions (36,36,36) and 576 unit terms. Source coordinate
indices are \(6p+q\), \(9y+s\), and \(4z+v\). Each scalar summand
adds one coordinate to every leg and one independent unit term.

The target is

\[
M(5,4,5)=\sum_{i,k<5}\sum_{j<4}a_{i,k}b_{i,j}c_{j,k},
\]

with dimensions (25,20,20), 100 unit terms, and 10,000 coefficient
positions. Target indices are \(5i+k\), \(4i+j\), and \(5j+k\).
Ordinary-map residuals use all 10,000 positions, including every
off-support zero. Their relative normalization is the target's
Frobenius norm, which equals 10.

The scalar terms are jointly optimized with all three Q maps. They are
not silently omitted from the source cost. A finite successful fit with
fixed r would still need a separate family and exponent argument.

## Completed ordinary-map pilots

| Experiment | Scalar cost r | Best relative error |
|---|---:|---:|
| Exact Q54 embedding, perturbed | 0 | 0.4358898944 |
| Fresh complex initialization | 0 | 0.4358898944 |
| Long-map singular-value floor 0.15 | 0 | 0.4375150255 |
| Long-map singular-value floor 0.40 | 0 | 0.4365762898 |
| Long-map singular-value floor 0.70 | 0 | 0.4431346938 |
| Joint scalar fit, continued from the plateau | 1 | 0.4243212107 |
| Joint scalar fit, fresh initialization | 2 | 0.4124115222 |
| Joint scalar fit, continued from the plateau | 4 | 0.3873796618 |
| Joint scalar fit, fresh initialization | 4 | 0.3874414340 |
| First space divisible by u−v, first seed | 0 | 0.5430918788 |
| First space divisible by u−v, second seed | 0 | 0.5400168780 |
| First space divisible by u−v, with scalars | 4 | 0.5142995502 |

The two unconstrained ordinary runs approach
\(\sqrt{19}/10\). Their long-leg maps have numerical rank 18, and
their A-rowspaces numerically factor as products of two five-dimensional
spaces. The long rowspaces factor through two-dimensional inner spaces
and the full nine-dimensional convolution output. The resulting tensor
has squared norm and target inner product approximately 81. This
identifies the component found by these runs; it is not a classification
of all restrictions.

The singular-value floors were search heuristics intended to avoid
that component. They did not improve the residual. They do not prove
that full-rank maps are impossible.

The alternative first-map subspace was

\[
\{(u-v)Y(u,v):\deg_uY,\deg_vY\le4\}\subset P_5(u)\otimes P_5(v).
\]

Its dimension is 25. The change of basis from this space to the target
A leg was optimized freely. With scalar summands, the scalar source
coordinates were also permitted in the first map. Failure of these
three fits is confined to their finite numerical runs.

## Monomial Laurent chart

Four additional runs assigned powers to each target map row:

\[
\alpha_{ik}=-[i=4]-[k=4],\qquad
\beta_{ij}=[i=4],\qquad
\gamma_{jk}=[k=4].
\]

A saved map coefficient in row a is multiplied by
\(\varepsilon^{\alpha_a}\), and similarly on the other legs. Every
output position therefore has one specified total power. The search
forces all negative-power coefficients to zero and the complete
constant coefficient to equal M(5,4,5). Positive powers are allowed.

| Total power | Coefficient positions | Required value |
|---:|---:|---|
| −2 | 256 | Zero |
| −1 | 2,176 | Zero |
| 0 | 5,136 | Complete target tensor on this block |
| 1 | 2,176 | Unrestricted |
| 2 | 256 | Unrestricted |

Thus the objective includes 7,568 positions. All 10,000 target
positions are accounted for by their powers. An exact solution would
be a valid monomial Laurent degeneration. Approximate satisfaction of
these equations is not accepted as such a solution.

| Experiment | Scalar cost r | Best nonpositive-power relative error |
|---|---:|---:|
| Fresh Laurent initialization, first seed | 0 | 0.1074148828 |
| Fresh Laurent initialization, second seed | 0 | 0.1272374178 |
| Perturbed ordinary plateau initialization | 0 | 0.1035782433 |
| Fresh Laurent initialization with scalars | 4 | 0.1043001830 |

These runs allow every old source column to change. Their target gauge
transformations preserve the row powers: the two outer factors use
block sizes four and one, and the middle factor has no split. Generic
outer gauge mixing would not preserve this chart and is not used.
The map norms and positive-power coefficients grow substantially.
Their smaller masked residuals are not evidence of an exact limit.

## Operator diagnostic

Regroup the tensor coefficients as a 100 by 100 operator with row
\((i_A,j_B,k_C)\) and column \((i_B,j_C,k_A)\). The target becomes
the identity. If the chart were solved exactly, the error E would have
strictly positive weight for

\[
h(i,j,k)=-[i=4]+[k=4].
\]

There are only three weight levels, with dimensions 16, 68, and 16.
Consequently every product of three positive-weight blocks vanishes:
\(E^3=0\). This is a necessary condition for this prescribed chart.
Nilpotence by itself would not establish the chart or a degeneration
under the full matrix multiplication stabilizer.

At the four saved Laurent points, E instead has numerical spectral
radius between 1.23 and 1.83. The absolute trace of \(E^2\) ranges
from about 40 to 66. Their cube norms are also far from zero. These
diagnostics reinforce the failed coefficient tests; they are not
universal obstructions to the source tensor.

The broader idea of removing an error in the null cone of the matrix
multiplication stabilizer is discussed by Dumitriu, Holtz, Hsu, Liskij,
Moran, Schneider, Schwartz, and Yuan in
[Fast and Stable Arbitrary Precision Approximate Matrix Multiplication,
arXiv:2610.13905v1, Section 2.3](https://arxiv.org/html/2610.13905v1#S2.SS3).
The specific three-level power calculation above follows directly from
the displayed row weights. No external result is being claimed as new.

## Controls and replay coverage

`q64_experiment_replay.py` reconstructs the 576 native source terms
and every explicitly declared scalar term. It uses a separately
implemented standard-library contraction, retaining all target
positions. The maximum difference from the sixteen saved objective
values is below \(7\times10^{-16}\).

Its exact controls include the known Q(2,2) to M2 integer restriction,
a deliberate sign error, and a Laurent example with 101 explicitly
counted scalar terms. The latter consists of the 100 naive target
terms plus one positive-power error. The checker accepts its exact
limit, distinguishes it from an ordinary identity, and detects a
deliberately introduced negative-power term. This control is a test of
the verifier, not a research improvement.

The focused standard-library tests also verify that regrouping maps
the target to the identity, that a positive-weight error is nilpotent,
and that a reverse edge creates a non-nilpotent error. A separate,
explicitly optional NumPy control verifies that the permitted block
gauge preserves exact nonpositive coefficients to numerical precision.

Run from the repository root:

```bash
python research/ai/2026-10-20-paired-direct-sums/q64_experiment_replay.py \
  results/paired-direct-sums-2026-10-20/q64-*-checkpoint.json
python research/ai/2026-10-20-paired-direct-sums/q64_operator_diagnostics.py \
  results/paired-direct-sums-2026-10-20/q64-weighted*-checkpoint.json
python -m unittest discover -s tests -p test_q64_search_replay.py -v
python research/ai/2026-10-20-paired-direct-sums/q64_weighted_gauge_control.py
```

`q64-completed-searches.json` lists the sixteen experiments. Every
checkpoint includes the full history and all complex map entries.
`q64-warm-initial.json` preserves the perturbed initial embedding.
The five search programs and `rectangle_search_common.py` contain no
workspace-specific paths and use the maintained native source helper.
The discovery environment used NumPy 2.3.5. The complete coefficient
replay and the default exact tests require only the Python standard
library. Operator diagnostics, the optional gauge control, and
numerical searches use NumPy. Maintained dependencies are unchanged.

The separate exact statements about fixed boundary columns
belong to
[outer_product_boundary.md](../2026-10-20-paired-construction/outer_product_boundary.md).
Those scoped proofs should not be conflated with the failed numerical
searches recorded here.
