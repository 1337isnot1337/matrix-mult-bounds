# A projected two-bit spin1 lift and its exact carry defect

This is a small source-compression control. It changes the bitwise lift
by projecting its physical matrices into the Hankel source `A(4,4)`.
The resulting maps are injective, but their trace tensor is not the
desired tensor. Two exact coefficient equations exclude the entire
six-parameter projection family described below.

This result does not exclude other projections, changes of the local
spin1 maps, auxiliary corrections, or general source compressions.
It establishes no matrix multiplication exponent improvement.

## The projection family

The [spin1 witness](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin1/scalar_witness.json)
gives a map from the 9 matrix variables to the 12 source coordinates
of `A(2,2)`, with denominator two, whose image tensor is

\[
 S=M_3+\rho,\qquad \rho(A,B,C)=\operatorname{tr}(A)
 \operatorname{tr}(B)\operatorname{tr}(C).
\]

Take two tensor copies of this map. Combine each pair of binary short
indices by `i=i0+2*i1` and `s=s0+2*s1`. A pair of middle trits has
integer middle index `k=k0+2*k1`. All middle fibers are singletons
except the following two:

| Integer index | Base trits | Alternate trits | New coordinate |
| ---: | --- | --- | --- |
| 2 | `(0,1)` | `(2,0)` | `(1-alpha)*base + alpha*alternate` |
| 4 | `(2,1)` | `(0,2)` | `(1-beta)*base + beta*alternate` |

Use the same two parameters at every pair of short indices on a leg,
and allow independent parameters on the three legs. There are thus
six parameters. The resulting maps have 81 rows and 112 source
columns, with denominator four. Their source image has coefficients
with common denominator 64 and degree at most one in the parameters
belonging to each leg.

At `alpha=beta=1/3` on all legs, this is the physical-entry average
over each Hankel fiber: the base trits occur twice among the physical
row/column pairs, while the alternate trits occur once. Exact rational
elimination gives map rank 81 on every leg. Full contraction over
all 4,096 source terms gives 22,039 nonzero image coefficients. The
difference from `M9` has 21,949 nonzero coefficients, and its slice
at the second input `I9` has rank 75. Thus the correction has tensor
flattening rank at least 75.

The large correction includes the original spin1 trace defects. To
test the new carry error separately, compare the image with `S tensor
S`, rather than with `M9` alone.

## Two incompatible carry equations

Number a target matrix unit `E_IJ` by `9*I+J`, with
`I=i0+3*i1` and `J=j0+3*j1`. Direct contraction of the original
`A(4,4)` source gives the following coefficients:

| Target rows on `(X,Y,Z)` | Projected coefficient | Coefficient in `S tensor S` | Required condition |
| --- | --- | ---: | --- |
| `(9,0,61)` | `1-alpha_X` | 1 | `alpha_X=0` |
| `(12,50,39)` | `2-2*alpha_X` | 0 | `alpha_X=1` |

Neither expression involves any other parameter. Over characteristic
zero, or any field in which two is invertible, they cannot both have
their required values. The projected family therefore cannot even
preserve the original two-copy spin1 tensor. This assertion concerns
only the displayed six-parameter family.

The verifier reconstructs these two coefficients independently of
the full-polynomial aggregation: it selects the specified target
rows, loops over every original source term, and collects the exact
parameter monomials. The comparison coefficients are computed from
the matrix-unit multiplication rule and the three trace functionals.
No numerical solve or Gröbner basis is required for the exclusion.

## Reproduction

The [saved report](../../../results/anisotropic-constructions-2026-10-20/bitwise-hankel-projection.json)
also records seven rational projection choices. All calculations use
the Python standard library. The maps depend on the saved spin1
witness, whose full coefficient identity was checked separately.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/bitwise_hankel_projection.py
python -S -m unittest discover -s tests -p test_bitwise_hankel_projection.py
```

The coefficient checks have been generated and replayed in this
session. They have not received external independent review.
