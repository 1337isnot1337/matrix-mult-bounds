# Sharp dimension sixteen for A4 source spaces below rank 37

October 23, 2026. Owner-directed AI-derived work over C. This is a
written proof with exact finite certificates, not a formalized proof
or independent external review. It makes no target-rank consequence.

## 1. Statement and reduction

For the canonical cyclic A4 source, use

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),             (1)

with short indices in {0,1,2,3}, long indices H,L in {0,...,6}, and
out-of-range coefficients zero. Its source space has coordinates
F_(i,k,s), with 0<=i,s<=3 and 0<=k<=6.

**Theorem.** Every complex linear parameter space V with rank M(F)<37
for every F in V has dimension at most sixteen. The dimension bound
is sharp. In particular, the same conclusion holds below rank 36.

We use the proved, byte-pinned
[order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md): V has
a coordinate limiting space of the same dimension and rank bound
whose support is downward closed in (i,k,s). That reduction uses the
literal lowering operators and a minimum Plucker-weight argument
over C. The source itself retains the credit of the
[cyclic finite-target note](../2026-10-20-koszul/cyclic_finite_target.md).

A monomial source slice has rank 16 times (1,2,3,4,3,2,1)_k. Thus a
downward ideal with any coordinate at k>=2 contains a middle-2
monomial of rank 48, contradicting rank below 37. The ideal lies
entirely in layers k=0,1.

For a short coefficient array g, define the 28-by-28 coherent block

    R(g)_((j,L),(H,r))=g_(H-j,L-r).                       (2)

The pure middle-k source matrix is, after fixed reorderings,
H_k tensor R(g), where (H_k)_(p,q)=1 when p+q=k. In particular the
middle-1 source rank is twice the R-rank. Its R-slices therefore have
rank at most eighteen under the theorem's hypothesis.

The coherent slice R(e_(0,1)+e_(1,0)) has an integer 20-minor with
odd determinant, as used in the preceding
[rank-80 package](../2026-10-23-torus-rank80/proof.md). We export and
replay that minor again here. A downward short ideal containing both
coordinates would give a middle-1 source slice of rank at least forty.
Hence the layer-1 short ideal misses at least one coordinate. Missing
(0,1) forces it onto the s=0 axis; missing (1,0) forces it onto the
i=0 axis. Its size is at most four.

## 2. Exactly thirteen ideals need a witness

If the source ideal has at least seventeen points, remove maximal
points until seventeen remain. This preserves downward closure and
the rank bound. Write S_0,S_1 for its nested short ideals and n_0,n_1
for their sizes. Then n_0+n_1=17, n_0<=16, and 1<=n_1<=4. The top
ideal S_1 is a straight axis segment.

Represent a short ideal by its nonincreasing four-entry height tuple,
with each height between zero and four. The complete inventory is:

| Size n_1 | Size n_0 | Bottom short shapes | Axis choices | Nested ideals |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 16 | 1 | 1 | 1 |
| 2 | 15 | 1 | 2 | 2 |
| 3 | 14 | 2 | 2 | 4 |
| 4 | 13 | 3 | 2 | 6 |

All indicated axis segments lie in every corresponding bottom shape.
The two axis descriptions coincide at length one, which is why the
first row has only one choice. Thus there are thirteen ideals total.

The acceptance program independently fills the eight heights of the
two layers recursively. At each step a height is bounded by its
previous neighbor in the same row and the corresponding previous-
layer height. It retains total size seventeen and excludes a top
layer containing both (0,1),(1,0). Every permissible height array has
one branch, and its only extra pruning uses the valid remaining
capacity of four per unfilled cell. This recovers the counts 1,2,4,6.
Discovery instead uses Cartesian products of the short Ferrers shapes
with the two axis segments.

## 3. Exact rank-37 witnesses and sharpness

For each ideal, certificates.json stores a coefficient-one subset,
thirty-seven matrix rows, and thirty-seven matrix columns. Each of
these thirteen integer minors has determinant one modulo two.
Consequently its determinant is odd and nonzero over C. Each ideal
contains a source slice of rank at least thirty-seven, contradicting
the strict rank hypothesis.

Source coefficient masks use lexicographic (i,k,s) order on the full
4-by-7-by-4 source box; coherent masks use lexicographic (i,s) order.
The source matrix indices are

    row(j,p,L)=(4j+p)*7+L;
    column(H,q,r)=(4H+q)*4+r.

For the coherent block use row(j,L)=7j+L and column(H,r)=4H+r.
Set bits select indices. Acceptance reconstructs the original literal
source, checks support containment, exact minor dimensions, and the
complete inventory, then uses low-column elimination on the selected
minors. Discovery used direct coefficient formulas and highest-bit
pivots on full matrices. The acceptance step does not rerun its
coefficient choices. The characteristic-two computations certify only
integer determinants; the geometric reduction remains over C.

No size-seventeen ideal survives. Trimming and the credited reduction
prove the dimension upper bound for every complex V.

For sharpness, take all sixteen coordinates (i,0,s). Their matrices
have nonzero entries only in the p=q=0 coherent block, with at most
twenty-eight nonzero rows. Every slice has rank at most 28, below 37.
This gives a valid sixteen-dimensional space and proves sharpness.

## 4. Scope and controls

The checker covers all 4096 literal source terms, 256 coherent terms,
112 monomial slice ranks and block factorizations, the coherent
20-minor, all thirteen source37-minors, and the sharpness plane.
It rejects missing or duplicate ideals, incorrect supports, altered
minor dimensions, singular minors, changed source pins, and inflated
scope.

The threshold is strictly below 37. This package does not extend the
theorem to rank 37 or to a threshold of forty. It claims sharpness
only for the source-space dimension sixteen in the stated range.
Applications to mixed target-leg pairs require a separate complete
argument and are not asserted here. No target construction, balanced
rank-sum bound, formalization, or exponent improvement is claimed.
