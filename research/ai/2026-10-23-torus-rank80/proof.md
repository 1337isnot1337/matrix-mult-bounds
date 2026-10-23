# A4 source spaces below rank 80 and the balanced sum 144

October 23, 2026. Owner-directed AI-derived continuation over C. This
is a written proof with exact finite certificates. It is not formally
verified and has no independent external mathematical review. Neither
sharpness nor a matrix-target construction is claimed.

## 1. Statements and credited reduction

Use the same canonical cyclic A4 source as in the pinned source note:

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),                 (1)

where short indices i,j,p,q,r,s range from zero to three and long
indices H,L range from zero to six. Out-of-range coefficients are zero.
Its parameter space and both matrix dimensions are 112.

**Theorem 1.** If a complex linear parameter space V has rank M(F)<80
for every F in V, then dim V<=50.

**Theorem 2.** In every complete Laurent degeneration to the target
X tensor I_11 for X in Mat_10(C), independently scalar-balance the two
long maps to valuation zero, compensating by the inverse scalar product
on the first map. Their constant ranks b,c satisfy b+c<=144.

The dimension bound 50 and the rank-sum bound 144 are upper necessary
bounds. No example attaining either bound is supplied. The latter
requires a total target leading deficiency at least 220-144=76.

We use the preceding [order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md),
at the exact version in sources.json. It proves that every bounded-rank
complex source space has a coordinate space of the same dimension and
rank bound whose support is a downward order ideal in the full box

    0<=i,s<=3, 0<=k<=6.                                   (2)

The reduction uses literal rank-preserving lowering operators, distinct
torus weights, and a minimum Plucker-weight argument on the closed
bounded-rank Grassmann locus. Its characteristic-zero hypotheses apply
here. The same preceding package proves the necessary rank sum 160.

The source formula retains the credit of the
[cyclic finite-target note](../2026-10-20-koszul/cyclic_finite_target.md).
The [saturated target-support inequality](../2026-10-20-graded-quantum-flags/saturation.md)
is also a prior input. No new external structural theorem is imported.

## 2. Coherent blocks and three small finite facts

For a four-by-four coefficient array g, define the 28-by-28 coherent
block

    R(g)_((j,L),(H,r)) = g_(H-j,L-r).                       (3)

If the source F is supported at one middle coordinate k, with
F_(i,k,s)=g_(i,s), then fixed row and column reorderings give

    M(F) = H_k tensor R(g),
    (H_k)_(p,q) = 1 if p+q=k, and 0 otherwise.              (4)

The ranks of H_k are (1,2,3,4,3,2,1). Each monomial R(e_(i,s)) is a
partial permutation of rank 16. The verifier reconstructs all 4096
source terms and 256 coherent terms independently from their literal
products, then checks (4) on all 112 source coordinates.

A downward short-coordinate ideal is represented by a nonincreasing
height tuple h=(h_0,h_1,h_2,h_3), with 0<=h_i<=4. It contains exactly
the coordinates (i,s) with s<h_i. Its dimension is the sum of the
heights. Three finite facts will suffice.

**Fact A.** R(e_(0,1)+e_(1,0)) has a 20-by-20 minor with odd integer
determinant. Thus any short ideal containing both coordinates has an
R-slice of rank at least 20.

**Fact B.** Every short ideal of size nine has an R-slice with a
24-by-24 minor of odd integer determinant. All seven such shapes and
their coefficient-one witness supports are:

| Short-ideal heights | Witness support |
| --- | --- |
| (3,2,2,2) | {(0,2),(2,0)} |
| (3,3,2,1) | {(0,2),(2,0)} |
| (3,3,3,0) | {(0,0),(2,2)} |
| (4,2,2,1) | {(0,2),(2,0)} |
| (4,3,1,1) | {(0,2),(2,0)} |
| (4,3,2,0) | {(0,2),(2,0)} |
| (4,4,1,0) | {(0,2),(2,0)} |

It follows that a short ideal whose every R-slice has rank at most 23
has size at most eight. Indeed, any larger ideal contains one of size
nine, by repeatedly removing a maximal point. This is an ideal-specific
finite replay of the earlier coherent dimension-eight bound.

**Fact C.** Every short ideal of size thirteen has an R-slice of full
rank 28. The three shapes and witness supports are:

| Short-ideal heights | Witness support |
| --- | --- |
| (4,3,3,3) | {(0,3),(1,0),(3,1)} |
| (4,4,3,2) | {(0,1),(1,3),(3,0)} |
| (4,4,4,1) | {(0,1),(1,3),(3,0)} |

Each listed full determinant is odd. Thus a short ideal with every
R-slice of rank at most 26 has size at most twelve, again by trimming
a larger ideal to thirteen.

All source coefficients in these facts are literal integers zero or
one. Checking a minor determinant modulo two proves that the integer
determinant is odd and hence nonzero over C. It does not apply the
geometric order-ideal reduction in characteristic two. The saved
certificate contains the exact row and column masks for all eleven
coherent minors: one for Fact A, seven for Fact B, and three for Fact C.

## 3. Reduce all size-51 source ideals to 24 cases

Suppose a bounded-rank ideal from (2) has dimension at least 51. Remove
maximal points until it has exactly 51. The remaining ideal inherits
the strict rank bound. Write S_k for its short ideal at middle layer k,
and n_k for the size of S_k. Downward closure gives

    S_0 contains S_1 contains ... contains S_6;
    n_0>=n_1>=...>=n_6; sum_k n_k=51.                    (5)

First inspect the pure middle-3 subspace. By (4), its source slice
rank is four times its R-rank. Fact A therefore forbids S_3 from
containing both (0,1) and (1,0), since that would give source rank
at least 4*20=80.

A downward short ideal missing (0,1) lies on the s=0 axis: any point
with s>0 would force (0,1). An ideal missing (1,0) lies on the i=0
axis. Consequently S_3 is contained in one straight axis of length
four, and

    n_3,n_4,n_5,n_6<=4.                                  (6)

The pure middle-2 subspace has source rank three times its R-rank.
All its R-slices have rank at most 26 because source rank is below 80.
Fact C gives

    n_2<=12.                                             (7)

If S_5 is nonempty, choose one of its coordinates, whose R-slice has
rank 16. The k=1 source blocks have p,q in {0,1}; the k=5 blocks have
p,q in {2,3}. They have disjoint row and column supports. Thus for
every g supported in S_1, the sum of its middle-1 source slice and the
chosen middle-5 monomial has rank

    2 rank R(g) + 2*16.                                  (8)

Both summands can be chosen independently because the source space
is coordinate. The strict source rank bound forces rank R(g)<=23.
Fact B gives n_1<=8, and nesting also gives n_2<=8. Equations (6)-(7)
then imply

    sum n_k <= 16+8+8+4+4+4+4 = 48,

a contradiction. Therefore n_5=n_6=0.

If n_4=0, equations (6)-(7) instead give

    sum n_k <= 16+16+12+4 = 48,

also a contradiction. The only remaining regime is n_4>0, n_5=n_6=0.
Its componentwise maxima are

    (n_0,n_1,n_2,n_3,n_4) <= (16,16,12,4,4),             (9)

whose total is 52. To total 51, exactly one unit must be removed from
that maximum vector. Nesting rules out reducing n_0 alone or n_3
alone. Exactly three layer-size profiles remain:

    (16,16,12,4,3,0,0);
    (16,16,11,4,4,0,0);
    (16,15,12,4,4,0,0).                                  (10)

Each profile has n_3=4. By the axis conclusion following Fact A, S_3
must be either the full i-axis or the full s-axis. For each profile,
there are four compatible S_2 shapes for each of these two orientations.
All other layers are determined by their sizes and nesting. Hence
there are eight ideals per profile and 24 in total.

For completeness, this count is also obtained by a direct recursive
enumeration. Acceptance first enumerates all nonincreasing integer
layer sizes obeying (9), n_5=n_6=0, and total 51. It obtains exactly
(10). It then fills each four-entry height row under the previous
row, enforcing its volume and the exclusion of both coordinates from
Fact A in layer three. Every permitted height has one branch, with
only a valid remaining-capacity pruning rule. This lists all 24 ideals.
Discovery uses a separate Cartesian product over the seventy short
Ferrers shapes and the three displayed profiles.

## 4. Exclude the 24 remaining ideals

For each ideal in (10), certificates.json specifies a coefficient-one
subset of that ideal, 80 distinct matrix rows, and 80 distinct matrix
columns. The selected 80-by-80 integer minor has determinant one
modulo two. It is therefore nonzero over C and supplies a source
slice of rank at least 80 inside that ideal.

For source coefficient masks, index n is the position of (i,k,s) in
lexicographic order on the full 4-by-7-by-4 source box. For coherent
masks it is the position of (i,s) in lexicographic order on 4-by-4.
Row and column indices are

    source row(j,p,L)=(4j+p)*7+L;
    source column(H,q,r)=(4H+q)*4+r;
    coherent row(j,L)=7j+L;
    coherent column(H,r)=4H+r.                           (11)

Set bits select indices. Acceptance checks the complete inventories,
support containment, distinct minor indices, and invertibility of
each saved minor. It reconstructs the bases from the original literal
products; discovery used the matrix-entry formulas. Its elimination
uses fixed low-column pivots on the selected minor; discovery chose
highest-bit pivots in the full matrix. Acceptance never regenerates
the discovery coefficient choices.

These 24 witnesses contradict every remaining size-51 ideal. Together
with the preceding cases, they exclude every such ideal. Trimming
and the credited complex order-ideal reduction prove dim V<=50 for
an arbitrary bounded-rank complex source space. This proves Theorem 1.

The proof gives no extremal example of dimension 50. At source rank
80 itself, the rank-80 witnesses no longer contradict the hypothesis;
the strict threshold cannot be replaced by a weak one here.

## 5. The saturated target-support consequence

Let B_0,C_0 be the balanced leading long maps, of ranks b,c, and define
the constant cancellation kernel

    K={F:B_0 M(F) C_0=0}, h=dim K,
    delta=224-b-c.                                       (12)

Two-sided compression loses at most 224-b-c ranks, so every slice from
K has rank at most delta. Theorem 1 implies

    delta<80 => h<=50.                                   (13)

The credited saturated target-support inequality, repeated and proved
in the [preceding package](../2026-10-23-torus-order-ideal/proof.md), is

    h >= 100-floor(b/11)*floor(c/11).                     (14)

Its proof uses the saturated row lattice of the projected source.
It contains both the constant projected source space and the
100-dimensional target slice space {X tensor I_11}. Their intersection
has dimension at least 100-h. The joint row and column supports of
an intersection parameter space have dimensions at most floor(c/11)
and floor(b/11), respectively. This yields (14) even if the first map
has arbitrary Laurent poles. The coefficient order and all higher
coefficients of the long maps are unrestricted.

The preceding sum-160 theorem already excludes b+c>160. Suppose
145<=b+c<=160. Then 64<=delta<=79 and (13) gives h<=50. But

    floor(b/11)+floor(c/11)<=floor(160/11)=14,

so their integer product is at most 7*7=49. Equation (14) forces
h>=51, a contradiction. All sums above 144 are excluded, proving
Theorem 2. At b+c=144, delta=80 and (13) does not apply.

## 6. Coverage and limits

The exact replay checks all 4096 source terms, 256 coherent terms,
112 block factorizations, and disjoint middle-1/middle-5 supports.
It verifies all 35 integer minors, with complete seven-ideal,
three-ideal, and 24-ideal inventories. It screens all 12321 integer
rank pairs 0<=b,c<=110, including the previously proved high-sum
regimes. All 2926 pairs above 144 are excluded; 1096 pairs with sums
145 through 160 are newly excluded by this package.

The finite minors and the written reduction serve different roles.
The former establish explicit nonzero integer determinants. The latter
extends that finite exclusion to all complex linear source spaces.
These are computer-assisted written claims, with deliberate corruption
tests and internal agent cross-checks. They have no independent external
review or formal verification. Neither upper bound is claimed sharp.
No complete degeneration or improved matrix multiplication exponent
follows from these necessary conditions alone.
