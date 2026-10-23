# The sharp A4 source dimension below rank 80 is 44

October 23, 2026. Claim `AI-A4-RANK80-SHARP-LINEAR-SPACE-001` is a
written proof with exact finite certificates. It is owner-directed
AI-derived work, without independent external mathematical review or
formalization.

## 1. Statement and prior inputs

Use the canonical cyclic A4 source, with parameter coefficients
F_(i,k,s), where 0<=i,s<=3 and 0<=k<=6. Its slice matrix is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),              (1)

where j,p,q,r range from zero to three, H,L range from zero to six,
and out-of-range parameters are zero. Its parameter space and both
matrix dimensions are 112.

**Theorem.** Among all complex linear parameter spaces V such that
rank M(F)<80 for every F in V, the maximum dimension is exactly 44.
An explicit 44-dimensional coordinate space has all slice ranks at
most 79 and contains a slice of rank 79.

The upper bound improves the preceding dimension-50 bound at the same
strict rank threshold. This note states no target-map rank consequence,
matrix-target construction, or matrix multiplication exponent bound.

The [canonical source](../2026-10-20-koszul/cyclic_finite_target.md),
[complex order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md),
and [coherent facts and layer constraints](../2026-10-23-torus-rank80/proof.md)
retain their original attribution. Their exact bytes are pinned in
`sources.json`. No new external structural theorem is imported.

The order-ideal reduction says that every bounded-rank complex source
space has a coordinate space of the same dimension and rank bound,
with support downward closed in the 4-by-7-by-4 box. Its proof uses
the literal rank-preserving lowering actions, distinct torus weights,
and a minimum Plucker-weight argument in the closed bounded-rank
Grassmann locus. We use it over C, not in characteristic two.

## 2. Necessary conditions for every remaining coordinate ideal

Define the 28-by-28 coherent block

    R(g)_((j,L),(H,r)) = g_(H-j,L-r).                     (2)

For a source supported at middle coordinate k, fixed reorderings give

    M(F)=H_k tensor R(g),     (H_k)_(p,q)=1_{p+q=k},
    rank H_k=(1,2,3,4,3,2,1)_k.                          (3)

Each coherent monomial has rank 16. The acceptance program rebuilds
all 4096 source terms and 256 coherent terms from their literal
products. It checks (3) on every one of the 112 parameter coordinates.

Represent a short downward ideal by four nonincreasing heights
h_0,...,h_3 in {0,...,4}; its coordinates are (i,s) with s<h_i.
The eleven coherent minors from the preceding rank-80 package are
copied with credit and replayed directly:

1. R(e_(0,1)+e_(1,0)) has a nonzero 20-by-20 minor.
2. Each of the seven short ideals of size nine has a slice with a
   nonzero 24-by-24 minor.
3. Each of the three short ideals of size thirteen has a slice with
   a nonzero 28-by-28 minor.

Every certificate is an integer zero-one coefficient choice and a
minor with odd determinant. The acceptance program enumerates all
seven and all three short ideals independently. Larger short ideals
contain one of the relevant size, by removing maximal points.

Write S_k for the short ideal in middle layer k, and n_k=|S_k|.
Downward closure gives S_0 containing S_1 containing ... containing
S_6. For every coordinate source space with all ranks below 80, the
following three conditions are necessary:

    (a) n_2<=12;
    (b) S_3 lies on one of the two short coordinate axes;
    (c) if S_5 is nonempty, then n_1<=8.                  (4)

For (a), a size-thirteen short ideal in S_2 supplies source rank at
least 3*28=84. For (b), containing both (0,1) and (1,0) supplies rank
at least 4*20=80. A downward ideal missing either point is contained
in the other axis, so n_3,...,n_6<=4.

For (c), the middle-1 blocks have row and column middle indices in
{0,1}; the middle-5 blocks have both indices in {2,3}. Their row and
column supports are disjoint. A middle-5 monomial therefore combines
with any middle-1 slice to give rank 32+2 rank R(g). The rank bound
forces rank R(g)<=23 throughout S_1. If n_1>=9, the second coherent
fact contradicts this. Both coefficients can be chosen independently
because the source space is coordinate. This proves all of (4).

## 3. The complete size-45 inventory and upper bound

Suppose a bounded-rank coordinate ideal has dimension at least 45.
Remove maximal points until its size is 45. The resulting ideal is
still downward closed, and its source space still has all ranks
below 80. It must satisfy (4).

There are exactly 1,709 such size-45 ideals. This is a complete finite
enumeration, not an enumeration of sampled shapes. Acceptance first
lists every nonincreasing profile (n_0,...,n_6) of total 45 with

    n_0<=16, n_2<=12, n_3<=4,
    n_5>0 implies n_1<=8.                               (5)

For each profile, it recursively fills all four short heights in each
layer, with the specified layer sum, nonincreasing heights, and
componentwise containment in the preceding layer. At layer three it
rejects precisely shapes containing both (0,1) and (1,0). All later
layers then lie on the same axis by containment. Every permitted
height has one recursive branch. The only capacity pruning compares
the remaining volume with a valid upper bound on remaining cells.
Thus no ideal satisfying (4)-(5) is omitted.

Discovery enumerates the same set in a separate way: it first forms
the seventy short Ferrers shapes, then walks nested chains of these
shapes with the total-volume and condition-(4) constraints. The two
inventories are compared by the acceptance record, which requires
each allowed shape exactly once.

For each of the 1,709 ideals, `certificates.json` supplies an integer
zero-one coefficient choice supported inside that ideal, 80 distinct
rows, and 80 distinct columns. The selected minor has determinant
one modulo two. Hence its integer determinant is odd and nonzero over
C, so that ideal contains a slice of rank at least 80.

The coefficient and minor masks use these index orders:

    source coefficients: (i,k,s) lexicographic;
    coherent coefficients: (i,s) lexicographic;
    source row(j,p,L)=(4j+p)*7+L;
    source column(H,q,r)=(4H+q)*4+r;
    coherent row(j,L)=7j+L;
    coherent column(H,r)=4H+r.                           (6)

Set bits select indices. Acceptance checks every support, every minor
dimension, and the determinant of each saved minor. It reconstructs
the original integer matrix before reducing modulo two. It does not
run discovery or use a random generator. Its fixed low-column
elimination differs from the highest-bit full-matrix pivots used for
discovery. The mod-two calculation only certifies nonzero integer
minors; it does not transfer the geometric reduction to that field.

These witnesses exclude every possible size-45 bounded-rank ideal.
Trimming and the credited order-ideal reduction give dim V<=44 for
every bounded-rank complex source space.

## 4. An explicit 44-dimensional space attaining the bound

Take every coefficient in middle layers zero and one, and in middle
layer two take precisely i<=2, with s arbitrary. Equivalently,

    S_0=S_1={0,1,2,3}^2,
    S_2={0,1,2} x {0,1,2,3},
    S_3=...=S_6=empty.                                  (7)

Its dimension is 16+16+12=44. All supported matrix entries lie in
the union of the following rows and columns:

| Selected vertices | Number |
| --- | ---: |
| Rows with p=0, all j,L | 28 |
| Rows with p=1 and j=3, all L | 7 |
| Columns with q=0 and H<=5, all r | 24 |
| Columns with q=1 and H<=4, all r | 20 |

To verify coverage directly, rows with p=0 are selected. For p=1,
only q=0 or q=1 can occur. If j=3, the row is selected. Otherwise
j<=2: at q=0 the layer is one and H=i+j<=3+2=5; at q=1 the layer
is two and H=i+j<=2+2=4. Both corresponding columns are selected.
For p=2 only q=0 can occur, and the layer-two restriction gives
H=i+j<=2+3=5. For p=3 there are no supported entries.

Any matrix supported on a union of 35 rows and 44 columns has rank
at most 35+44=79. Indeed, separate its entries in the selected rows;
the remainder is supported in the selected columns. The two summands
have ranks at most 35 and 44, and matrix rank is subadditive. This
argument holds over every field and requires no matching theorem.

The saved certificate also gives a slice inside (7) with an odd
79-by-79 minor. Thus its maximum rank is exactly 79. In particular,
the dimension-44 bound is attained, and a proposed dimension cap of
43 or less at this same strict rank threshold is false.

## 5. Exact coverage and limits

The standalone standard-library checker verifies 1,721 integer
minors: eleven credited coherent minors, 1,709 complete size-45
exclusion minors, and the rank-79 sharpness minor. It also checks
the literal source factorizations, the disjoint middle blocks, and
every source coefficient in the explicit support cover.

The strict threshold is essential. Taking i=0 or i=1 and all k,s
gives dimension 56 with at most 80 supported columns, since H=i+j<=4.
Thus changing rank<80 to rank<=80 would invalidate the dimension-44
claim. Acceptance checks this boundary support count directly.

Discovery tested smaller inventories only to locate the boundary.
The exact 44-dimensional construction makes further attempts to
lower this dimension cap at rank below 80 unnecessary. The theorem
does not classify all extremal spaces or determine caps at other
rank thresholds. The construction is a source parameter space, not
a complete matrix-target degeneration. No target-map rank-pair
application, exponent improvement, or external independent review
is included in this package.
