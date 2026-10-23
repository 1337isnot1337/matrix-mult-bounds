# Sharp A4 source dimensions below ranks 92 and 96

October 23, 2026. Claims AI-A4-RANK92-SHARP-LINEAR-SPACE-001 and
AI-A4-RANK96-SHARP-LINEAR-SPACE-001 are written proofs with exact finite
certificates. They have no independent external mathematical review or
formalization.

## 1. Statements and credited reduction

Write F for a parameter vector with coordinates F_(i,k,s), where
0 <= i,s <= 3 and 0 <= k <= 6. The canonical 112-by-112 A4 source slice is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r).             (1)

Here j,p,q,r run from zero to three, H,L run from zero to six, and an
out-of-range parameter coordinate is zero.

**Theorem 1.** The maximum dimension of a complex linear parameter space
V such that rank M(F) < 92 for every F in V is exactly 68.

**Theorem 2.** The corresponding maximum dimension with rank M(F) < 96
for every F in V is exactly 72.

The explicit spaces attaining these dimensions have maximum slice ranks
exactly 91 and 95, respectively. In particular, proposed dimension caps
64 below rank 92 and 68 below rank 96 are false.

The [canonical source](../2026-10-20-koszul/cyclic_finite_target.md),
[order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md),
[coherent minor facts](../2026-10-23-torus-rank80/proof.md), and
[preceding staircase construction](../2026-10-23-source-staircase-spaces/proof.md)
retain their credit and exact byte pins in the source record. No new
external structural theorem is imported.

The credited characteristic-zero reduction replaces any complex
bounded-rank linear parameter space by a coordinate order ideal of the
same dimension and rank bound. Its proof uses explicit rank-preserving
lowering actions and minimum Plucker weight in a closed Grassmannian
locus. An order ideal here is downward closed in all three indices.
Its seven short layers therefore satisfy

    S_0 contains S_1 contains ... contains S_6,
    n_k = |S_k|,   16 >= n_0 >= ... >= n_6 >= 0.          (2)

It suffices to bound the sum of the seven sizes in (2). The finite
modulo-two calculations below prove that specified integer determinants
are odd. They do not extend the geometric reduction to characteristic two.

## 2. Coherent ranks and independent middle layers

For a short parameter vector g define the 28-by-28 coherent matrix

    R(g)_((j,L),(H,r)) = g_(H-j,L-r).                     (3)

For F supported on middle layer k, fixed row and column reorderings give

    M(F) = H_k tensor R(g),    (H_k)_(p,q) = 1_(p+q=k),
    rank H_k = (1,2,3,4,3,2,1)_k.                       (4)

Define the credited lower bound

    rho(0) = 0,
    rho(n) = 16 for 1 <= n <= 4,
             20 for 5 <= n <= 8,
             24 for 9 <= n <= 12,
             28 for 13 <= n <= 16.                      (5)

Every short order ideal of size n contains a coefficient vector whose
coherent matrix has rank at least rho(n). A nonempty ideal contains
(0,0), whose monomial matrix has rank 16. An ideal of size at least five
cannot fit on one axis of length four, so contains (0,1) and (1,0).
Their sum has the credited odd 20-minor. By removing maximal points,
every larger ideal contains an ideal of any smaller desired size.
All seven size-nine ideals have credited odd 24-minors, and all three
size-thirteen ideals have credited odd 28-minors. The eleven nontrivial
small certificates are copied exactly with credit and replayed from (3).

The middle pairs (0,4), (1,5), and (2,6) have disjoint row supports and
disjoint column supports in the H matrices. Their ranks therefore add.
Two layer coefficient vectors can be chosen independently because the
source space is coordinate. If all source slices have rank strictly
below a threshold R, equations (4)-(5) imply

    (1,2,3,4,3,2,1)_k * rho(n_k) < R for every k,
    rho(n_0) + 3 rho(n_4) < R,
    2 rho(n_1) + 2 rho(n_5) < R,
    3 rho(n_2) + rho(n_6) < R.                           (6)

Each necessary inequality has its own coefficient witness. A simultaneous
maximizer of the different inequalities is neither used nor asserted.

## 3. The upper bound 68 below rank 92

Set R = 92. The pure middle-three inequality gives n_3 <= 8, since
4*rho(9) = 96. The two last pairs in (6) give

    n_1 >= 13 implies n_5 <= 4,   because 2*28+2*20 = 96,
    n_2 >= 13 implies n_6 = 0,    because 3*28+16 = 100,
    n_2 >= 9  implies n_6 <= 4,   because 3*24+20 = 92.   (7)

The following disjoint cases exhaust all possible profiles. All bounds
not explicitly in (7) follow from n_3 <= 8, nesting, or n_0 <= 16.

| Case | Componentwise upper bound for (n_0,...,n_6) | Total |
| --- | --- | ---: |
| n_2 >= 13 | (16,16,16,8,8,4,0) | 68 |
| n_2 <= 12 and n_1 >= 13 | (16,16,12,8,8,4,4) | 68 |
| n_1 <= 12 and 9 <= n_2 <= 12 | (16,12,12,8,8,8,4) | 68 |
| n_1 <= 12 and n_2 <= 8 | (16,12,8,8,8,8,8) | 68 |

Thus every bounded-rank coordinate ideal has dimension at most 68.
The credited geometric reduction gives the same bound for arbitrary
complex linear parameter spaces.

## 4. The upper bound 72 below rank 96

Set R = 96. The pure middle-three inequality again gives n_3 <= 8,
and the first two implications in (7) remain valid. Equality at 96
is excluded because the rank hypothesis is strict. The last implication
in (7) is not used at this threshold.

| Case | Componentwise upper bound for (n_0,...,n_6) | Total |
| --- | --- | ---: |
| n_2 >= 13 | (16,16,16,8,8,4,0) | 68 |
| n_2 <= 12 and n_1 >= 13 | (16,16,12,8,8,4,4) | 68 |
| n_1 <= 12 | (16,12,12,8,8,8,8) | 72 |

These cases are exhaustive. They prove dimension at most 72 for
coordinate ideals and hence for all complex bounded-rank spaces.

## 5. Enlarged staircase spaces attaining both bounds

For m = 2 or 3, let V_m be the coordinate space with all parameters
of the following three types, with s arbitrary:

    i < 2,          any k;
    i = 2,          k < m;
    i = 3,          k = 0.                              (8)

The types are disjoint, so dim V_m = 56+4m+4 = 60+4m. Relative to the
credited staircase with i < 2 and i = 2,k < m, the last type adds four
coordinates. A cover by rows and columns controls their rank cost.

Select the seven rows with (j,p)=(3,0) and arbitrary L. Select also
the columns with H <= 4, and the columns with H=5,q<m-1, in each case
with arbitrary remaining indices. There are

    7 selected rows and 80+4(m-1) selected columns,
    total 83+4m.                                        (9)

Every matrix entry allowed by (8) lies in this cover. Indeed (1) gives
H=i+j, k=p+q, and L=r+s. Entries with H <= 4 use a selected column.
If H=5 and i=2, then j=3 and p+q<m. Either q<m-1 and the column is
selected, or q=m-1 and p=0, so the row is selected. If H=5 and i=3,
then j=2 and p=q=0; the column is selected because m>=2. Finally,
H=6 forces i=j=3, and (8) forces p=q=0, so the row is selected.
No other H is possible.

Any matrix supported on r selected rows and c selected columns has
rank at most r+c: split off its selected rows, then the remaining
matrix is supported on the selected columns. Thus over every field

    rank M(F) <= 83+4m for every F in V_m.                (10)

At m=2 the dimension is 68 and the rank upper bound is 91<92. At m=3
the dimension is 72 and the rank upper bound is 95<96. This proves
sharpness in Theorems 1 and 2. Saved coefficient vectors in V_2 and
V_3 have odd 91-by-91 and 95-by-95 minors, respectively. Hence the
maximum slice ranks in these spaces are exactly 91 and 95.

The cover (9) is explicitly scoped to m=2,3. Substituting m=1 would
omit the H=5,q=0 columns required by i=3,j=2,k=0. Acceptance records
one such uncovered entry as a negative control; no m=1 rank bound
is asserted from this formula.

## 6. Exact acceptance and scope

The universal upper bounds are the written case splits in Sections 3-4,
using the credited geometric reduction and eleven coherent minors.
A supplementary independent enumeration checks all 245,157 nonincreasing
seven-layer size profiles against (6) and the displayed componentwise
case bounds. There are 119,381 admissible profiles at threshold 92;
their maximum volume is 68, with four maximizing profiles. At threshold
96 there are 121,481 admissible profiles, maximum volume 72, and one
maximizing profile. These counts check the case split; they are not
a substitute for it and do not classify actual extremal spaces.

Acceptance reconstructs the 4,096 literal source terms and the 256
coherent terms, checks all 112 basis factorizations (4), verifies
both row and column disjointness for the three middle pairs, replays
all thirteen saved odd minors, and checks every literal entry in the
two sharp spaces against the fixed covers. Discovery uses seeded
binary search only to select the two large minors. Acceptance uses
their saved integer coefficients and a separate pivot convention;
it performs no random search.

These theorems concern arbitrary complex source parameter spaces under
the two strict rank thresholds. They do not determine the corresponding
maximum dimensions at non-strict thresholds 92 or 96. The examples
refute the two smaller proposed source caps, while leaving other
possible compression-kernel constraints available. The package gives
no target-rank-pair consequence, no matrix-target construction, and
no improvement to the matrix multiplication exponent.
