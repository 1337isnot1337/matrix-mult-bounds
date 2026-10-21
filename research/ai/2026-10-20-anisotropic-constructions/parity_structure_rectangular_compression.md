# Direct rectangular physical compression: a numerical discovery chart

**Status:** a complete-coefficient search interface and one bounded trajectory
for the singular target `A(4,4) -> M(10,10,11)`. No restriction, degeneration,
or improved matrix-multiplication exponent is certified by that trajectory.
The separate integer `A(2,2) -> M2` control is exact.

This chart uses the full original source. It imposes no primary-torus grading,
retained small matrix core, or quotient-intertwining equation. The target gate
is recorded in `singular_support.md`; the ordinary slice-rank exclusions in
this package mean that a successful trajectory here must produce an actual
singular family, rather than a finite ordinary map.

## 1. Physical realization and complete target

Put `m=a+b-1`, `P=ab`, and `N=abm`. In the common source-coordinate convention,
the physical matrix of a source vector is

\[
 W(F)_{(i,q),(p,s)}=F_{i,p+q,s},
 \qquad 0\leq i,p<a,\quad 0\leq q,s<b.
\]

The source trilinear form is `tr(W(F_X) W(F_Y) W(F_Z))`. Expanding the trace
gives exactly the six-index source loop used by the other construction
certificates in this package. The numerical controls also compare this
physical contraction with that six-index loop directly.

For target vertex dimensions `(n0,n1,n2)`, leg `i` consists of the
`d_i=n_i n_(i+1)` matrix units of `Hom(V_(i+1),V_i)`. Every one of the
`d0*d1*d2` target coefficients is included. A target coefficient is one
precisely on a cyclic triple `(Eij,Ejk,Eki)`.

For `A(4,4) -> M(10,10,11)`, this means physical matrices of size 16, source
leg dimension 112, target dimensions `(100,110,110)`, and 1,210,000 checked
target coefficients. The target squared Frobenius norm is 1,100.

## 2. Exact internal compression equations

Choose three physical splittings with sections `T_i` and retractions `R_i`
satisfying `R_i T_i=I`. For every target matrix `A`, impose

\[
 R_i J_i(A)T_{i+1}=A,\qquad J_i(A)\in W.
 \tag{1}
\]

This equation only fixes the selected rectangular block. It does not require
`R_i J_i(A)=A R_(i+1)`. In particular, this is not an exact quotient chart.

Let `L_i` be the linear map taking source coefficients to the block in (1).
It has size `d_i x N`. Select an invertible `d_i x d_i` source-column
submatrix `L_P`; call the remaining columns `L_Q`. For arbitrary free
coefficients `U`, every lift is

\[
 C_P^{\mathsf T}=L_P^{-1}(I-L_QU^{\mathsf T}),\qquad C_Q=U.
 \tag{2}
\]

Here `C` is target-major: its rows are the source vectors for target units.
Equation (2) gives `L C^T=I` identically in exact arithmetic. The program
reports the floating point error in this identity at each checkpoint.

In the fixed-frame implementation, an SVD gives a particular right inverse
and an orthonormal kernel. In the moving implementation, a fixed source
pivot chart is used so that the derivative of the solve is explicit. Pivots
can be selected again by QR while preserving the current physical maps;
the reconstruction error is checked before continuation.

At the A44 target, the free dimensions per matrix unit are `(12,2,2)`.
There are 1,640 complex fiber parameters in total.

## 3. Moving the physical splitting

Starting from a unitary physical basis `G_i`, write `r_i=P-n_i` and introduce
arbitrary complex matrices `E_i` of size `n_i x r_i` and `F_i` of size
`r_i x n_i`. Use

\[
 \widetilde G_i
 =G_i\begin{pmatrix}I&E_i\\F_i&I+F_iE_i\end{pmatrix},
\quad
 T_i=G_i\begin{pmatrix}I\\F_i\end{pmatrix},
\quad
 R_i=(I+E_iF_i,\,-E_i)G_i^{-1}.
 \tag{3}
\]

The block matrix in (3) is a product of a lower and an upper unitriangular
matrix. Its inverse exists for every finite `E_i,F_i`, and `R_i T_i=I`
holds by direct multiplication. The entries and singular values may still
become unbounded along a trajectory.

These moving splittings add 350 complex parameters at the A44 target,
giving 1,990 complex parameters altogether. The reported physical-frame
singular values are diagnostics of this chart, not a degeneration certificate.
The source coefficient maps, their norms and their singular-value ratios
are recorded separately.

The gradient differentiates both the physical trace and the exact solve (2).
For example, if `G_P` is the coefficient gradient on pivot columns, then the
gradient with respect to the compression matrix is

\[
 G_L=-L_P^{-\ast}G_P^{\mathsf T}\overline C.
\]

This is obtained from `dC_P^T=-L_P^-1(dL)C^T`. The implementation then applies
the product rule to `L_i(F)=R_i W(F)T_(i+1)` and to (3). Complex derivatives
use the convention `df=Re <gradient,dparameter>`.

## 4. Actual target normalization

Write `I` for the complete contracted tensor and `T` for the standard target.
The raw loss is

\[
 \frac{\|I-T\|^2}{2\|T\|^2}.
\]

A raw residual can fall merely because an unrelated image becomes smaller.
The first moving-frame trajectory did this: its residual fell from about
686 to 5.28, while its correlation with `T` was only 0.0207.

The subsequent search therefore uses the complete-coefficient objective

\[
 \mathcal L(I)=\frac12\log
 \frac{\|I\|^2\|T\|^2}{|\langle T,I\rangle|^2}.
 \tag{4}
\]

No coefficient is omitted or given zero weight. For nonzero overlap, multiply
the first source map by `alpha=||T||^2/<T,I>`. The resulting actual tensor
`alpha I` has target coefficient mean exactly one. Its reported residual is

\[
 \frac{\|\alpha I-T\|}{\|T\|}
 =\sqrt{\rho^{-2}-1},\qquad
 \rho=\frac{|\langle T,I\rangle|}{\|T\|\|I\|}.
 \tag{5}
\]

The internal equations (1) refer to the maps before this explicitly recorded
first-leg scalar. This scalar is an ordinary allowed output map, and all
coefficients after scaling are still checked. The code rejects undefined
normalization. It also records the source coefficient norms after that
scalar, so that shrinking an internal map is not hidden.

For `c=<T,I>` and `q=||I||^2`, the image gradient of (4) is

\[
 I/q-T/\overline c.
\]

Analytic and complex finite-difference derivatives are compared separately
for fibers, moving splittings, and their combination, for both objectives.

## 5. An exact leg update for the normalized objective

Fix two legs and all physical splittings. Let `b` be the current complete
image, viewed as a matrix with one row per unit of the remaining target leg.
Let `D` be the common matrix of that leg's fiber directions. Images in this
affine chart have the form `b+UD`. Allowing one nonzero scalar gives the
linear span of `b` and those directions.

Project the standard target `T` orthogonally onto this linear span. This
maximizes correlation with `T`, and therefore minimizes (4) for the fixed
two legs. The projection is cheap because the row-wise design matrix has
only 12 or 2 columns at the A44 target.

Explicitly, remove from `b` and `T` their row-wise projections onto `D`,
leaving `b_perp,T_perp`. Then

\[
 s=\frac{\langle b_\perp,T_\perp\rangle}{\|b_\perp\|^2}.
\]

If `b_D,T_D` are the corresponding fitted row coefficients, the target
projection is `s b+(T_D-s b_D)D`. For nonzero `s`, division by `s` returns
to the internal chart (1). The program reports `s`. It stops this update
if `s` is numerically zero, since that boundary requires an explicit Laurent
construction rather than an unreported division.

## 6. Exact positive control and numerical controls

`parity_structure_compression_control.py` uses only the standard library.
It verifies an exact `A(2,2) -> M2` map with all three legs given, in common
source order, by

| Target row | Source coordinate |
|---|---|
| `E00` | `F(0,1,1)` |
| `E01` | `F(0,2,0)` |
| `E10` | `F(1,0,1)` |
| `E11` | `F(1,1,0)` |

The physical core uses vertices `(0,1)` and `(1,0)`. Every selected 2-by-2
top block is the required matrix unit. The complete 64-term source replay
gives exactly the eight matrix-product coefficients, with no extra term.
A nonzero-to-nonzero map-coefficient tamper is rejected. This is a positive
control, not a claim of a new matrix-multiplication algorithm.

The optional numerical controls use the nonsymmetric `A(2,3)` source and
`M(2,3,2)` target. They compare all 216 source terms and all 144 target
coefficients with a direct contraction. The largest recorded derivative
error is below `2e-10`; the direct coefficient discrepancy is below `3e-15`.
They also verify a monotone exact leg solve, preservation of the other
parameter blocks, preservation of physical splittings in the normalized
leg solve, the unchanged-map pivot refresh, and recovery of the exact M2
control with zero loss and zero gradient.

The focused unittest file has two standard-library tests and two optional
NumPy/SciPy tests. Under `python -S`, only the optional tests are skipped.

## 7. Recorded A44 trajectory

All entries below use the same initial physical-frame seed, `441011`.
They describe numerical search progress, not an upper bound on omega.

| Stage | Work | Raw relative residual | Target correlation | Positive-normalized residual |
|---|---:|---:|---:|---:|
| Fixed random frames | Initial evaluation | 2331.47 | Not used | Not used |
| Fixed frames | 12 alternating sweeps | 685.69 | Not used | Not used |
| Moving frames, raw objective | 80 iterations | 5.2823 | 0.020730 | 48.228 |
| Moving frames, objective (4) | 100 iterations | 4.5647 | 0.102976 | 9.6594 |
| Refreshed pivots, objective (4) | 4 leg sweeps and 100 iterations | Recorded in JSON | 0.180066 | 5.4627 |

The final stage took about 47 seconds. Its unscaled physical map norms were
66.13, 37.81, and 43.54; physical-frame smallest singular values were about
0.0646, 0.0291, and 0.0374. No coherent Laurent rate, cancellation identity,
or small residual was obtained. These data therefore give neither a
construction for the target nor an obstruction to it.

The next use of this checkpoint is to inspect the seven non-core terms in
the physical block-trace expansion, rather than to infer convergence from
the numerical sequence.

## 8. Files and replay

The complete dependency set is:

- `parity_structure_rectangular_compression.py`: fixed-frame elimination,
  complete tensor contraction, gradient and leg solve.
- `parity_structure_moving_compression.py`: imports that base module and adds
  exact moving splittings, implicit gradients, positive normalization,
  normalized leg projection and unchanged-map pivot refresh.
- `parity_structure_compression_control.py`: independent standard-library
  integer positive control.
- This note, the two numerical control JSON files, the A44 checkpoint JSON
  and NPZ files, and `tests/test_parity_structure_compression.py`.

Both numerical modules require NumPy and SciPy. The integer control and its
two tests do not. Example replay commands, from the repository root:

```sh
python -S -m unittest discover -s tests -p test_parity_structure_compression.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest discover -s tests -p test_parity_structure_compression.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-anisotropic-constructions/parity_structure_moving_compression.py --controls
```

NPZ checkpoints store source coefficient maps, the actual physical frames,
the base frame seed, source pivots, free-column choices, free origins and
scales, and all parameters. They are floating point discovery artifacts.
No external independent review of this new chart has been obtained.
