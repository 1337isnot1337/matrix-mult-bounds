# Streaming full torus objective

October 21, 2026. This is a numerical discovery evaluator for the historical
A(8,8) to M27 plus M7 torus construction. It evaluates the complete tensor
residual within the exact torus ansatz. It assumes no quotient,
fixed-border lift, or row/column factorization. No optimization run or
target witness is claimed by this package. The later
[support-peeling proof](torus_support_peeling.md) excludes this full target
within the ordinary graded ansatz. The evaluator is retained for its
small controls and as the base of the unequal-profile implementation.

## What is evaluated

The source charges are those of `parity_structure_torus_seed.md`:
i+s−k on the first leg and its two cyclic reorderings. A target edge
has its row-vertex charge minus its column-vertex charge. Each map
preserves that charge exactly. Source and target tensors therefore
vanish identically whenever their three charges do not sum to zero.

The evaluator checks all coefficients in every conserving charge
block. For the supplied 27-plus-7 profile, there are 631 such blocks,
containing 20,308,848 target coefficients. The full unblocked array
would contain 470,910,952 coefficients. The code stores the 262,144
source support terms sparsely and forms one dense source block at a
time. The largest source block has 262,144 entries. It does not allocate
the full source or target cube.

The objective is

\[
f(A,B,C)=\frac{\|S(A,B,C)-(M_{27}\oplus M_7)\|_F^2}
                   {2(27^3+7^3)}.
\]

The denominator is the fixed positive integer 20,026. No weights are
discarded or downweighted. There is no target-dependent normalization
that a fit can reduce independently of the tensor error. All mixed
coefficients between the two target matrix blocks are included and
required to vanish.

## Interface

Instantiate the evaluator with the source lengths and the common
vertex-charge lists for the target blocks:

```python
problem = TorusDirectSumObjective(8, 8, witness['full_target_vertex_charges'])
maps = problem.from_dense([A, B, C])
report, gradient = problem.evaluate(maps, gradient=True)
```

Each `maps[leg][weight]` is a target-major matrix whose rows use
`problem.target_groups[weight]` and whose columns use
`problem.source_groups[leg][weight]`. Both are ordered lists of the
original tensor indices. `from_dense` rejects maps with nonzero entries
between distinct charge spaces. The returned gradient uses exactly
the same block layout and is the gradient of the half squared relative
residual with respect to the complex map coefficients.

An external exact parametrization may construct these map blocks and
apply its own chain rule to the returned gradients. In particular,
the evaluator does not impose the discarded full-border anchor ansatz.
True extreme-slice equations can instead be incorporated by a flexible
map parametrization.

The optional flat interface packs the real and imaginary parts of all
114,666 complex map coefficients:

```python
vector = problem.pack(maps)
value, derivative = problem.objective(vector)
```

`problem.unpack(vector)` reverses the packing. The derivative is with
respect to that real vector and can be passed to a numerical optimizer.
No generic large-target optimization is launched by the module.

## Adjoint and controls

Within each charge block, the forward operation contracts the source
successively with the first, second, and third maps. The adjoint walks
back through those same operations, conjugating the two unvaried maps
for complex parameters. Intermediates are discarded before the next
charge block.

The small A(2,2) control uses the exact extreme-charge M2 maps and a
zero extra scalar block. Its squared residual is exactly 1 and its
positive normalization is 9. A separate direct dense contraction of
all original small-source terms agrees with the streamed objective.
A random complex derivative direction checks the analytic adjoint;
the recorded error is approximately 9.5e-11.

The full-format M12 plus M3 seed gives exactly the expected squared
residual 18,271 with normalization 20,026. Its gradient is zero: an exact
matrix subtarget with the other vertex rows zero is a stationary point
of the full least-squares objective. A growth attempt therefore needs
new directions, a controlled perturbation, or additional exact anchor
data; simply running a first-order method from the unperturbed seed
does not add missing vertices.

The replay data are in `parity_structure_torus_objective_controls.json`.
NumPy is a discovery dependency. These numerical controls complement
the separate standard-library exact seed certificate and do not claim
an exact full-target construction.
