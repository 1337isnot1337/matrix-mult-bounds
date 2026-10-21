# Numerical discovery and exact replay for Q(5,4) to M4

## Result and scope

A complex numerical search produced an ordinary-map candidate for
\(Q(5,4)\ge M(4,4,4)\). Its rowspaces suggested a polynomial-subspace
construction, from which a separate integer certificate was recovered.
The integer certificate passes a full coefficient contraction here.
This establishes the finite restriction; it does not improve the matrix
multiplication exponent.

The exact proof and maps are in
[outer_product_injection.md](../2026-10-20-paired-construction/outer_product_injection.md)
and [q54-exact.json](../2026-10-20-paired-construction/q54-exact.json).
That construction also proves \(Q(k+1,k)\ge M(k,4,k)\) for \(k\ge2\).
Its source width grows with k. It does not provide the fixed-width,
near-full family sought by the larger research program.

The saved numerical maps remain numerical evidence. They are not used
as coefficients of the exact certificate. The two contraction programs
were implemented separately within the same research session; no
external independent mathematical review or novelty claim is asserted.

## Coordinates and complete coefficient objective

The source tensor is

\[
Q(n,b)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{b-1}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

For this run, n=5 and b=4. The source coordinate indices are
\(5p+q\), \(8y+s\), and \(4z+v\), respectively. The target is

\[
M(4,4,4)=\sum_{i,j,k=0}^{3}a_{i,k}b_{i,j}c_{j,k},
\]

with coordinate indices \(4i+k\), \(4i+j\), and \(4j+k\).

| Quantity | Value |
|---|---:|
| Source dimensions | 25, 32, 32 |
| Source terms | 400 |
| Target dimensions | 16, 16, 16 |
| Target coefficient positions | 4,096 |
| Target nonzero coefficients | 64 |
| Complex map entries optimized | 1,424 |

Every reported residual uses all 4,096 target positions, including the
4,032 positions whose prescribed coefficient is zero. Relative error is
the Frobenius norm of the full tensor difference divided by 8, the
Frobenius norm of the target.

## Bounded numerical discovery

The successful run used complex ordinary maps, seed 202610321, NumPy
2.3.5, and SciPy 1.17.0. Alternating least squares updated each whole
linear map. Every ten iterations, transformations from the exact matrix
multiplication symmetry group balanced the three maps. These
transformations preserve the target tensor. Away from a solution, they
can change the residual norm, so only complete contractions after the
transformation were used for acceptance and checkpoint selection.

The first 3,000 alternating updates reached relative error
\(1.5282576144831268\times10^{-4}\). A continuation of 15,000 updates
reached \(2.4668015327022677\times10^{-12}\), with all three map
Frobenius norms approximately 5.960430492. The least-squares diagonal
regularizer was \(10^{-12}\). Two complex Newton corrections then gave
the saved candidate.

| Check | Relative coefficient error | Maximum absolute error |
|---|---:|---:|
| Before Newton corrections | 2.4668 × 10⁻¹² | 1.6430 × 10⁻¹² |
| After first correction | 1.0738 × 10⁻¹² | 7.7861 × 10⁻¹³ |
| After second correction, NumPy contraction | 4.7015 × 10⁻¹⁶ | 4.5459 × 10⁻¹⁶ |
| Saved-map replay, Python complex arithmetic | 8.4143 × 10⁻¹⁶ | 1.3345 × 10⁻¹⁵ |

The two final contractions use different summation orders. Their small
difference is consistent with floating-point arithmetic; neither is an
exact equality test. The final map norms are approximately
5.9604305754, 5.9604305770, and 5.9604305769.

The numerical artifact stores every real and imaginary map coefficient,
the coordinate conventions, iteration counts, Newton history, and these
norms. Adding one to a saved A-map coefficient raises the replayed
relative error to about 0.345885. A known integer Q(2,2) to M2
restriction and a deliberate sign error provide positive and negative
controls for the same contraction routine.

## Exact recovery and a separate integer check

The numerical A-map rowspace factored as a product of two
four-dimensional polynomial spaces. One long-leg rowspace also
factored through a two-dimensional inner polynomial space. This
suggested using the exact choices

\[
U=\langle t,t^2,t^3,1-t^4\rangle\subset P_4,
\qquad W=\langle1,t^3\rangle\subset P_3.
\]

Multiplication \(U\otimes W\to P_7\) is a unimodular isomorphism.
Its integer inverse provides two convolution restrictions, whose
product is M4. The linked proof states all three local maps and proves
the identity symbolically.

`q54_exact_replay.py` reads the saved integer maps without importing
their construction generator. It applies the native source formula
using Python integers and compares every output coefficient with the
standard target. All 4,096 positions agree exactly. The maps use only
0, 1, and −1, with 25, 20, and 20 nonzero entries. A deliberate sign
change produces four wrong coefficients. Because the successful
identity is integral, it remains valid over every field.

## Why the next target is different

This construction injects an outer polynomial space of dimension r
times an inner space of dimension two into a space of dimension
\(n+b-1\). Consequently it requires

\[
2r\le n+b-1.
\]

For source width b=4, the construction yields only
\(r\le\lfloor(n+3)/2\rfloor\). It reaches r=4 for n=5, exactly at
the dimension limit. The next proposed target,
\(Q(6,4)\ge M(5,4,5)\), violates that limit because 10 exceeds 9.
An exact witness there would therefore require additional structure.
No such witness is included in this package.

## Replay

Run from the repository root:

```bash
python research/ai/2026-10-20-paired-direct-sums/q54_numeric_replay.py \
  results/paired-direct-sums-2026-10-20/q54-m4-numerical-candidate.json
python research/ai/2026-10-20-paired-direct-sums/q54_exact_replay.py \
  research/ai/2026-10-20-paired-construction/q54-exact.json
```

Both programs require only the Python standard library. Stored outputs
are `q54-m4-numerical-replay.json` and `q54-exact-replay.json` under
`results/paired-direct-sums-2026-10-20/`. The integer replay also records
the SHA-256 digest of the exact certificate it checked.
