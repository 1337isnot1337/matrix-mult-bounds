# Full tensor objective and affine updates for unequal vertex charges

## Purpose and status

[parity_structure_unequal_objective.py](parity_structure_unequal_objective.py)
supports three different vertex-charge lists for each matrix multiplication
block. It also supports rectangular blocks, so its validation can detect
errors hidden by equal leg dimensions. The earlier common-profile objective
and affine solver remain unchanged.

This is optional numerical discovery infrastructure. It produces no exact
large-target witness and establishes no smaller exponent. Only the small
controls described below were run for this checkpoint. The large unequal
profiles considered while this code was written failed subsequent exact
screens, and no optimization was run on them.

The module requires NumPy at runtime. It adds no maintained dependency;
the repository's standard-library proof verifiers remain independent of it.
Its numerical controls are an optional test when NumPy is available and
are skipped when it is absent. Exact acceptance of a future construction
still requires a separate full coefficient certificate.

## Input conventions and complete objective

The constructor is

```python
problem = UnequalTorusDirectSumObjective(a, b, vertex_charges)
```

The input layout is `vertex_charges[vertex][block]`. On leg `i`, the target
matrix space is `Hom(V_(i+1), V_i)`, with vertex indices read modulo three.
The three lists can have unrelated multiplicities, orders and offsets.
For a rectangular block with vertex dimensions `(n0,n1,n2)`, the three
target leg dimensions are `(n0*n1,n1*n2,n2*n0)`.

Source columns retain the original A(a,b) ordering:

| Leg | Original source coordinate | Flattened column |
| --- | --- | --- |
| X | `(i,k,s)` | `(i*(a+b-1)+k)*b+s` |
| Y | `(j,p,u)` | `(j*a+p)*(a+b-1)+u` |
| Z | `(v,q,r)` | `(v*b+q)*a+r` |

The source weights are respectively `i+s-k`, `j+p-u` and `q+r-v`.
Target weights are row charge minus column charge. The public
`source_groups[leg][weight]` and `target_groups[leg][weight]` each retain
the correct leg-specific indices. `from_dense` rejects off-weight map
coefficients; `to_dense` reconstructs the complete maps.

All desired target coefficients have value one. The objective is

\[
 f(A,B,C)=\frac{\|T(A,B,C)-T_{\rm target}\|_F^2}
                    {2\sum_{\rm blocks}n_0n_1n_2}.
\]

The denominator is the positive norm of the complete target. Every
charge-conserving coefficient block is evaluated, including undesired
mixed-summand coefficients. Every other coefficient is identically zero
for maps admitted by `from_dense`. There are no charge-dependent residual
weights and no partial-target normalization.

The streaming contraction and complex adjoint are inherited from the frozen
[common-profile engine](parity_structure_torus_objective.py). The new
constructor independently builds the three target groupings, rectangular
matrix-unit support, target offsets and parameter layout. The inherited
contraction uses these block arrays without requiring equal target groups.

`pack` and `unpack` represent complex parameters as concatenated real and
imaginary parts. `objective(vector)` returns the complete objective and its
real gradient in that convention.

## Affine block interface

```python
solver = UnequalAffineTorusALS(
    problem,
    fixed_source_columns=[x_columns, y_columns, z_columns],
    fixed_target_rows=[x_rows, y_rows, z_rows],
)
solver.update_block(maps, leg=1, weight=2)
solver.update_leg(maps, leg=0, ridge=1e-8)
```

Both fixed-index arguments are optional and default to three empty lists.
Their entries are global source-column or target-row indices for the
specified leg. Different rows can be frozen on different legs. Free
coefficients at a given weight are all entries outside the fixed columns
and fixed rows. More general linear relations between free coefficients
are not imposed by this interface.

With the other two maps fixed, a complete weight block has the form `A*K`.
The solver streams all relevant third-grade blocks to accumulate

\[
 G=KK^*,\qquad B=T_{\rm target}K^*.
\]

The same Gram matrix serves every row of the active target block. Fixed
source-column contributions are subtracted before solving on the free
columns. The unregularized update uses a numerical Hermitian pseudoinverse.
With positive `ridge`, it instead minimizes the complete residual plus a
nonnegative squared distance from the old free block. The old point has
zero added penalty, so an exact solve cannot increase the unregularized
residual. Floating-point monotonicity and fixed-entry preservation are
checked in the numerical controls; they are not algebraic certificates.

`normal_equations` exposes the Gram matrix and target cross term for a
single leg and weight. `update_block` changes only that block;
`update_leg` updates all permitted blocks on the chosen leg.
`fixed_entries_unchanged` and `free_gradient_norm` use each leg's own row
indices and weight spaces.

## Sparse seed interoperability

```python
problem, maps, solver, metadata = load_sparse_seed(path)
```

This reads the unequal-profile export directly. Required fields are
`source_lengths`, `vertex_charges`, and either `partial_maps` or `maps`.
Each sparse entry is `[target_row, original_source_column, numerator]`.
`map_denominator` defaults to one. Optional `target_dimensions` are checked
against the actual three vertex lists. The loader rejects duplicate
coefficient entries, invalid indices and off-weight coefficients. It
does not rebuild a common charge list or silently identify vertex indices
on different legs. Metadata include the exact input file SHA-256.

The driver supports seed evaluation but deliberately runs no optimization
steps. Callers can use the block-update interface after selecting and
checking their precise affine family.

## Validation

The nonsquare control source is A(2,3), with 24 coordinates on each leg.
The target is `M(2,2,3) direct_sum M1`, with leg dimensions 5, 7 and 7.
Its three vertex lists are

```text
V0: [[0,0], [0]]
V1: [[0,0], [0]]
V2: [[0,-1,-2], [0]]
```

An integral monomial map gives the twelve desired coefficients of
`M(2,2,3)`, leaving the extra scalar map zero. The standard control has
squared residual one and positive normalization thirteen. The full dense
source contraction checks all 245 target coefficients, including those
outside the three conserving grade blocks.

Random complex maps, with a recorded deterministic seed, then test the
complete streamed objective against the independently assembled full
dense tensor. A central directional derivative tests the real/imaginary
gradient convention. Three separate affine solves, at weights 0, 1 and
-2 on the three different legs, are compared with full dense least
squares. The test uses different frozen source columns and target rows
on each leg and checks that every other map block remains unchanged.
Finally, regularized full-leg updates are checked for objective decrease
and fixed-entry preservation.

The recorded [numerical control report](parity_structure_unequal_objective_controls.json)
contains these observed discrepancies:

| Control | Absolute discrepancy |
| --- | ---: |
| Full dense versus streamed objective | `1.11e-16` |
| Complex directional gradient | `3.06e-11` |
| Largest full dense least-squares map difference | `7.69e-15` |
| Largest free gradient after a block solve | `3.60e-17` |

These are numerical validation results, not bounds on a prospective
large-target residual.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-anisotropic-constructions/parity_structure_unequal_objective.py
python -m unittest discover -s tests -p test_parity_structure_unequal_objective.py -v
```

The same test command with `python -S` skips the optional NumPy test and
does not introduce a new CI dependency. The engine remains a tool for
constructing candidate maps; the tensor identity must still be proved.
