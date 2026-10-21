# Completed discovery runs and the pure-power limit

October 21, 2026. Numerical and finite-field discovery records. No qualifying
construction certificate was found in the runs listed below.

## Exact finite-field search

Four searches completed their 180-second budgets under Z3 4.15.4. Each
returned `unknown` with reason `timeout`, with no model. They cover two
different encodings over `F3` and `F4`:

| Encoding | Coefficient variables | Additional variables | Equations |
| --- | ---: | ---: | ---: |
| Target-orbit binomials | 125 | 0 | 101 zero coefficients and 2 binomials, plus 20 nonzero conditions |
| Explicit target scalars | 125 | 18 nonzero scalars | 121 cubic coefficient equations |

The saved queries permit inspection of the exact finite scope. They are
compressed losslessly as `*.smt2.gz`; the associated JSON gives the SHA256
of the uncompressed query. Neither timeout is an UNSAT result. Neither
finite encoding by itself proves complex existence or nonexistence.

## Numerical discovery

Every error in this table is the Euclidean norm from a separate evaluation
of all 121 normalized tensor coefficients of nonpositive parameter weight.
The twenty desired entries have been normalized to one. Errors are absolute,
not divided by the target norm.

| Report | Completed evaluations per start | Smallest normalized error |
| --- | --- | ---: |
| `pivot-torus-real.json` | 3 starts, 1200 each | `0.0010072923934` |
| `pivot-torus-normalized-real.json` | 2 starts, 2500 each | `0.0002322019688` |
| `pivot-torus-wide-real.json` | 1 continuation, 10000 | `0.00000209759194` |
| `full-pure-shared-real.json` | 1 continuation, 3000 | `0.00000112397468` |
| `full-complex.json` | 1 complex continuation, 3000 | `0.00000076054924` |
| `anchored-complex.json` | 1 fixed-coefficient branch, 1314 | `0.00003383063586` |

All but the final anchored run exhausted their specified evaluation budgets.
The anchored run stopped at the step-tolerance criterion. No exact point
or nonsingular interval certificate was recovered. The small last errors
coincide with near-singular Jacobians and must not be read as certified
distances to a solution set. The largest entries in the full transformed
tensor were approximately 146, 183, and 154 in the last three respective
runs. Tensor coefficients at positive weight are omitted from the objective;
for an exact coefficient solution they would vanish as the degeneration
parameter tends to zero, but a nonzero negative-weight error can instead
grow.

The initial `pivot-torus-real.json` run optimized unnormalized monic residuals.
Its separate normalized tensor check exposed the difference. The subsequent
program divides each coefficient residual by its target row-scaling product
before optimizing. This prevents small desired coefficients alone from
producing a misleading objective value. The first program is preserved
byte-for-byte in `snapshots/pivot_torus_initial.py` with its recorded SHA256.
Because of its original path-relative imports and hashes, place a temporary
copy beside `pivot_torus.py` when reproducing that historical run.

## The exact pure-power stratum is excluded

The broader numerical continuation drove the shared monic polynomials close
to

\[
G_p(t)=t^{D-p},\qquad D=m-1.
\]

This exact stratum is already excluded at the desired source cost by the
repository's [constant-shared-basis theorem](../2026-10-20-koszul/arbitrary_shared_basis.md).
Here is the reduction, which also explains why the numerical behavior does
not furnish a hidden exact construction.

For shared weights `gamma+beta*p`,

\[
\epsilon^{\gamma+\beta p}t^{D-p}
 =\epsilon^{\gamma+\beta D}(\epsilon^{-\beta}t)^{D-p}.
\]

The dilation `t -> epsilon^(-beta) t` is a source automorphism of polynomial
multiplication when applied on both inputs and contragrediently on the
output. Absorb it into the other two maps, and absorb the common scalar
into either map. The shared map then becomes the constant invertible
coordinate reversal. Arbitrary Laurent maps on the other legs remain
permitted. The existing theorem therefore applies and gives

\[
B\ge N+\lfloor D^2/4\rfloor-\lfloor D/2\rfloor.
\]

For `m=4`, `N=10`, this requires `B>=11`. Thus a `C(4,10)` solution cannot
have exactly these shared polynomials. Fixed nonzero leading row scalars
do not change the argument. The near-pure-power numerical run is retained
as a diagnostic; it is not a construction and will not be repeated in that
closed stratum.

A final explicitly different discovery branch fixes the coefficient of
`t` in `G_1(t)` to one, keeping it away from this exact stratum. Its scope
and completed outcome are recorded separately in `anchored-complex.json`.
It did not converge to zero residual. Its smallest row scale was about
`5.03e-12`, and its largest full tensor coefficient was about `4.01e16`;
this illustrates escape toward a poorly conditioned boundary, not a
finite construction. The independent normalized check is reported above
even though it is slightly larger than the internal optimization residual.
This restriction is useful for discovery; no assertion is made that it
covers every possible shared polynomial configuration.

## Acceptance requirements

A numerical candidate still needs exact coefficient equations and all open
conditions. A finite-field candidate still needs a checked lift, for example
the full-row-rank Hensel premise in the main README. Finally, a size-four
degeneration would require a complete growth construction before yielding
any new matrix multiplication exponent. None of these steps is supplied by
the floating residuals or time-limited searches above.
