# Narrow-source coefficient and compression searches

## Source and completed ordinary-map pilot

Define the narrower paired convolution tensor

\[
Q_{n,b}=\sum_{\substack{0\le p,q<n\\0\le y,v<b}}
A_{p,q}B_{y,q+v}C_{p+y,v},
\]

of format `(n²,b(n+b−1),b(n+b−1))`. This is
`C(n,b)_(A,B,C) tensor C(n,b)_(A,C,B)` in the same convolution convention
as the paired source. The ordinary target in this pilot is `M(n,b,n)`,
with coefficient convention

\[
\sum_{i,k=0}^{n-1}\sum_{j=0}^{b-1}a_{i,k}b_{i,j}c_{j,k}.
\]

**No restriction `Q_(3,2) -> M(3,2,3)` was found.** This is a construction
question, and the failed experiments below prove no nonexistence result.
Even that small target, if constructed, would not by itself establish a
smaller matrix multiplication exponent.

`narrow_source_search.py` fits unrestricted real constant maps. Its full
coefficient objective includes every target coordinate, including those
outside the matrix support. For `n=3,b=2`, there are 177 map parameters,
36 source terms, 18 target terms, and 324 target coefficient positions.

Eight deterministic seeds completed 1,000 alternating least-squares
iterations each with ridge `1e−12`. Residuals were recorded every 200
iterations, and the best recorded maps were saved as JSON.

| Seed | Best recorded relative coefficient error |
|---:|---:|
| `202610230` | `0.471449` |
| `202610231` | `0.375885` |
| `202610232` | `0.375884` |
| `202610233` | `0.375886` |
| `202610234` | `0.372213` |
| `202610235` | `0.375885` |
| `202610236` | `0.372211` |
| `202610237` | `0.471583` |

The same fitting code, with `n=2,b=2` and seed `202610229`, reached relative
error `2.49e−12` on the known positive case. Its exact rational verifier
separately expands the integer `P2=Q_(2,2) -> M(2,2,2)` maps from
`paired-construction/exact_p2.py`. All 16 source terms and 64 target
positions are checked, including the off-support cancellations. A sign
corruption is explicitly rejected. The numerical fit is not the proof of
that known identity.

## Compression kernels and an exact algebra criterion

The coefficient search was followed by a distinct method that optimizes
the two compression kernels directly. For `Q_(3,2)`, source second and
third dimensions are eight, while target dimensions are six. A chart of
each two-dimensional kernel has 12 coordinates, giving 24 parameters in
total. The chart uses identity blocks on the retained coordinates and
variable blocks on the two omitted coordinates. It does not cover every
possible kernel.

After compression, let `S_i` be the nine `6`-by-`6` first-slice matrices.
Choose the fixed diagonal first-space combination

\[
S_0=\sum_{p=0}^{2}S_{p,p}
\]

as an anchor. When `S0` is invertible, set `R_i=S_i S0^(-1)`. The numerical
objective orthonormalizes the span of the vectorized `R_i`, forms all 81
products of its nine basis matrices, and measures their components
outside that span. This is 2,916 scalar product-coordinate equations in
the real search. It removes arbitrary first-space basis choices from the
optimization.

Closure alone does not identify a matrix multiplication tensor. The exact
acceptance criterion implemented in `kernel_algebra_search.py` requires:

1. The normalized slice span has dimension nine.
2. Every one of its 81 basis products lies exactly in that span.
3. Its center has dimension one.
4. The trace form `(X,Y) -> Tr_6(XY)` is nondegenerate on the span.

All four tests use rational arithmetic when given rational matrices.
Closure is checked at every matrix coordinate after solving for product
coordinates from an invertible minor. No test is limited to a proposed
support.

Here is the acceptance implication over the complex numbers. The anchor
ensures that the span contains the identity, so closure makes it a unital
algebra `R` inside `Mat6`. Its Jacobson radical `J` is a nilpotent ideal.
For `X in J` and `Y in R`, the product `XY` lies in `J` and is nilpotent,
so its matrix trace is zero. Nondegeneracy of the trace form therefore
forces `J=0`. The standard structure theorem for finite-dimensional
semisimple complex algebras, together with center dimension one, makes
`R` a single full matrix algebra. Dimension nine identifies it with
`Mat3(C)`. Its six-dimensional representation consists of two copies of
the standard three-dimensional module. Rank nine identifies the original
first space with this algebra, and the resulting basis changes give the
tensor `M(3,2,3)`.

This standard algebra argument was independently checked by the concurrent
mathematical worker. It is an acceptance criterion, not a claim that a
compression meeting it was found. A genuine result would require exact
compression data and the induced basis maps, or an exact certificate for
the complete algebra-to-tensor implication. The original target has 324
tensor coefficients; a proposed map must account for all of them.

Exact controls verify the criterion on the actual `M(3,2,3)` slice space.
They also reject two distinct false positives: a closed commutative algebra
with center dimension four, and the upper triangular `2`-by-`2` algebra,
whose center has dimension one but whose trace form is degenerate. The
latter control checks that closure and a small center cannot substitute
for the semisimplicity test.

## Failed low-error kernel searches

Four real starts, seeds `202610240` through `202610243`, each had a budget
of 400 function evaluations. Their coordinates were bounded by ten.
All runs terminated, but their small closure errors came with nearly
singular anchors:

| Seed | Function evaluations | Closure residual norm | Anchor condition number |
|---:|---:|---:|---:|
| `202610240` | 129 | `0.00679052` | `1.31e10` |
| `202610241` | 43 | `0.0000296761` | `3.97e11` |
| `202610242` | 46 | `0.000992434` | `5.34e10` |
| `202610243` | 44 | `0.00000457408` | `1.84e9` |

The commutant spectra also failed to show the required four-dimensional
kernel. These points were rejected. A small closure error after an
ill-conditioned normalization is not evidence of an exact matrix tensor.

The known `Q_(2,2)` positive case behaved differently: it reached closure
error `1.56e−14` in nine evaluations, with anchor condition number `4.12`
and four numerical commutant zero modes. This is a numerical method
calibration; the exact positive identity remains the separately verified
integer map.

## Condition and spectrum penalties

A second set of runs retained every closure equation and added seven
residual components:

- Logarithmic penalties when anchor or normalized-span condition number
  exceeds 100.
- The second, third, and fourth smallest singular values of the
  commutator map for an orthonormal slice basis. The first singular value
  vanishes because scalar matrices commute with everything.
- A penalty when the fifth commutator singular value is below `0.01`.
- A penalty when the smallest trace-form singular value is below `0.01`.

These are soft penalties, and their final violations are reported
separately from closure errors. They do not constitute exact spectral
certificates. The hard coordinate bound remains ten.

The same four real starts completed with the following results:

| Seed | Function evaluations | Closure residual norm | Anchor condition number |
|---:|---:|---:|---:|
| `202610240` | 225 | `0.595229` | `111.51` |
| `202610241` | 400 | `0.408800` | `111.88` |
| `202610242` | 203 | `0.582642` | `105.75` |
| `202610243` | 291 | `0.359826` | `106.30` |

None gave a candidate for rational reconstruction. The `Q_(2,2)` positive
calibration with these extra penalties reached closure error `6.97e−16`
in ten evaluations, anchor condition number `5.90`, and the required
four numerical commutant zero modes.

All reports are explicit discovery records. Neither solver termination
nor the exact verification of the controls advances the matrix
multiplication exponent.

## Complex kernel extension

Two further starts allowed complex compression coordinates, represented
by 48 real variables. The bound of ten applies separately to each real
and imaginary part. Complex span projections use the Hermitian inner
product, while matrix multiplication, commutators, and the algebra trace
form remain complex bilinear operations. The full complex closure
objective contributes 5,832 real residual components, in addition to the
same seven condition and spectrum penalties.

Both seeds `202610250` and `202610251` completed all 400 function
evaluations. Their closure residual norms were `0.394012` and `0.305934`,
and their anchor condition numbers were `111.01` and `104.93`. Neither
produced a matrix-algebra candidate. The independent complex `Q_(2,2)`
calibration, seed `202610249`, reached closure error `8.11e−16` in eleven
evaluations, with anchor condition number `7.55` and four numerical
commutant zero modes. These positive numerical controls supplement the
exact coefficient and algebra checks; they do not supply new tensor maps.

The complex extension is reproduced by adding `--complex --stabilized`
to the kernel command below and selecting the corresponding seed.

## Reproduction

Pure rational controls are included in the focused standard-library tests:

```sh
python -m unittest discover -s tests -p test_paired_direct_sums.py -v
```

Representative numerical runs, with optional NumPy and SciPy dependencies:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/narrow_source_search.py --n 3 --b 2 --seed 202610230 --iterations 1000 --report-every 200 --checkpoint /tmp/narrow-q3.json --output /tmp/narrow-q3-report.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/kernel_algebra_search.py --n 3 --seed 202610240 --evaluations 400 --checkpoint /tmp/kernel-q3.json --output /tmp/kernel-q3-report.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-paired-direct-sums/kernel_algebra_search.py --n 3 --seed 202610240 --evaluations 400 --stabilized --checkpoint /tmp/kernel-q3-conditioned.json --output /tmp/kernel-q3-conditioned-report.json
```

The source and target coordinate generators, complete rational coefficient
checker, exact algebra checker, discovery code, reports, and JSON
checkpoints are maintained together. Numerical runs used NumPy `2.3.5`
and SciPy `1.17.0`; exact tests need neither package.
