# Sharp A4 source dimensions below ranks 84 and 88

October 23, 2026. Claims AI-A4-RANK84-SHARP-LINEAR-SPACE-001 and
AI-A4-RANK88-SHARP-LINEAR-SPACE-001 are written proofs with exact finite
certificates, without independent external mathematical review or
formalization.

## 1. Statements and credited reduction

Let F have coordinates F_(i,k,s), with 0 <= i,s <= 3 and 0 <= k <= 6.
The canonical 112-by-112 A4 source slice is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),             (1)

where j,p,q,r range from zero to three, H,L from zero to six, and
out-of-range coefficients are zero.

**Theorem 1.** The maximum dimension of a complex linear parameter
space V such that rank M(F) < 84 for every F in V is exactly 56.

**Theorem 2.** The corresponding maximum dimension with rank M(F) < 88
for every F in V is exactly 60.

The explicit spaces attaining dimensions 56 and 60 have maximum slice
ranks exactly 80 and 84, respectively.

The [canonical source](../2026-10-20-koszul/cyclic_finite_target.md),
[characteristic-zero order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md),
[coherent minor facts](../2026-10-23-torus-rank80/proof.md), and
[staircase spaces](../2026-10-23-source-staircase-spaces/proof.md)
retain their prior attribution and exact byte pins in the source record.
No new external structural theorem is imported.

The credited reduction replaces any complex bounded-rank linear source
space by a coordinate order ideal of the same dimension and rank bound.
It uses three explicit rank-preserving lowering actions and a minimum
Plucker-weight argument in a closed Grassmannian locus. Thus it suffices
to consider nested short ideals

    S_0 contains S_1 contains ... contains S_6,
    n_k = |S_k|,   16 >= n_0 >= ... >= n_6 >= 0.         (2)

The finite mod-two computations below certify odd integer determinants.
They do not transfer the geometric reduction to characteristic two.

## 2. Small coherent bounds and disjoint middle pairs

For a short coefficient vector g define

    R(g)_((j,L),(H,r)) = g_(H-j,L-r).                    (3)

For a coefficient vector supported in middle layer k, fixed row and
column reorderings give

    M(F) = H_k tensor R(g),    (H_k)_(p,q) = 1_(p+q=k),
    rank H_k = (1,2,3,4,3,2,1)_k.                      (4)

Set

    rho(0) = 0,
    rho(n) = 16 for 1 <= n <= 4,
             20 for 5 <= n <= 8,
             24 for 9 <= n <= 12,
             28 for 13 <= n <= 16.                     (5)

Every short order ideal of size n contains a coefficient vector whose
coherent matrix has rank at least rho(n). For positive n its monomial
at (0,0) already has rank 16. A short ideal of size at least five cannot
lie on one coordinate axis, since each axis has length four. Hence it
contains both (0,1) and (1,0), whose sum has the credited odd 20-minor.
Every ideal of size at least nine contains a size-nine ideal after
removing maximal points; all seven such ideals have credited odd
24-minors. The same argument uses the three size-thirteen ideals and
their odd 28-minors. These eleven small certificates are copied with
credit and replayed directly from (3).

The middle-index supports of H_0 and H_4 are {0} and {1,2,3};
those of H_1 and H_5 are {0,1} and {2,3};
those of H_2 and H_6 are {0,1,2} and {3}. The sets are disjoint on
both the row and column sides. Coefficients in two layers can be
chosen independently because the source space is coordinate.
Consequently, if all source ranks are strictly below R, then

    (1,2,3,4,3,2,1)_k * rho(n_k) < R for every k,
    rho(n_0) + 3 rho(n_4) < R,
    2 rho(n_1) + 2 rho(n_5) < R,
    3 rho(n_2) + rho(n_6) < R.                          (6)

For each inequality a source vector supported on the indicated layer
or pair attains at least its left-hand side. There is no assertion
that one vector simultaneously realizes every inequality. None is
needed to derive the necessary conditions (6).

## 3. The sharp upper bound 56 for rank below 84

Set R = 84. The pure middle-two and middle-three inequalities imply

    n_2 <= 12,   n_3 <= 8.                             (7)

The three disjoint pairs imply

    n_0 >= 9  implies n_4 <= 4,
    n_5 > 0   implies n_1 <= 12,
    n_6 > 0   implies n_2 <= 8.                        (8)

For example, n_0 >= 9 and n_4 >= 5 would give
rho(n_0) + 3 rho(n_4) >= 24 + 3*20 = 84.
The other two implications follow from
2*28 + 2*16 = 88 >= 84 and 3*24 + 16 = 88 >= 84.

If n_0 <= 8, all seven layers have size at most eight, giving total
dimension at most 56. Otherwise n_0 >= 9 and (8) gives n_4 <= 4.
The following cases exhaust the last two layers:

| Case | Upper bounds for the seven layer sizes | Total |
| --- | --- | ---: |
| n_5 = 0 | (16,16,12,8,4,0,0) | 56 |
| n_5 > 0 and n_6 = 0 | (16,12,12,8,4,4,0) | 56 |
| n_6 > 0 | (16,12,8,8,4,4,4) | 56 |

Nesting supplies every bound not explicitly in (7)-(8). This proves
dimension at most 56 for coordinate ideals, hence for every complex
bounded-rank space by the credited reduction.

## 4. The sharp upper bound 60 for rank below 88

Set R = 88. The pure middle-three inequality gives n_3 <= 8.
The three pair inequalities give

    n_0 >= 13 implies n_4 <= 4,
    n_5 > 0   implies n_1 <= 12,
    n_6 > 0   implies n_2 <= 8,
    n_5 >= 5  implies n_1 <= 8.                        (9)

Indeed the excluded lower bounds are, in the same order,
28+3*20 = 88, 2*28+2*16 = 88, 3*24+16 = 88, and
2*24+2*20 = 88.

First suppose n_0 >= 13. Then n_4 <= 4, and nesting plus (9) gives:

| Case | Upper bounds for the seven layer sizes | Total |
| --- | --- | ---: |
| n_5 = 0 | (16,16,16,8,4,0,0) | 60 |
| n_5 > 0 and n_6 = 0 | (16,12,12,8,4,4,0) | 56 |
| n_6 > 0 | (16,12,8,8,4,4,4) | 56 |

Now suppose n_0 <= 12. If n_5 >= 5, (9) gives n_1 <= 8;
all six layers after layer zero then have size at most eight.
This bounds the total by 12+6*8 = 60. Otherwise n_5 <= 4:

| Case | Upper bounds for the seven layer sizes | Total |
| --- | --- | ---: |
| n_6 = 0 | (12,12,12,8,8,4,0) | 56 |
| n_6 > 0 | (12,12,8,8,8,4,4) | 56 |

These cases are exhaustive, so the coordinate dimension is at most 60.
The credited reduction proves the bound for arbitrary complex spaces.

## 5. Explicit spaces attaining both bounds

For m = 0 or 1 take every source coordinate with i < 2, together
with coordinates having i = 2 and k < m. The short index s is arbitrary.
This is the credited staircase family at a = 4, d = 2.
Its dimension is 56+4m.

For i < 2, equation (1) implies H = i+j <= 4. These coordinates use
only the 80 columns with H <= 4. The additional coordinates when
m = 1 have k = 0, so p = q = 0. They can add only the four columns
with H = 5, q = 0 and arbitrary r. Thus every source matrix in the
two spaces has rank at most 80 and 84, respectively.

Both upper bounds are strictly below the required thresholds, so
dimensions 56 and 60 are attained. The saved coefficient vectors
also have odd 80-by-80 and 84-by-84 minors. Thus the maximum slice
ranks inside these examples are exactly 80 and 84.

The strict thresholds are essential. The 60-dimensional example
already invalidates a cap of 56 when rank <= 84 is allowed. The
staircase at m = 2 has dimension 64 and at most 88 supported columns,
invalidating a cap of 60 when rank <= 88 is allowed.

## 6. Acceptance and scope

The proof of each dimension upper bound is the exhaustive case split
above, combined with the credited geometric reduction and eleven
small coherent minors. A supplementary finite check independently
enumerates all 245,157 nonincreasing seven-layer size profiles:
51,553 satisfy (6) at strict rank 84, with maximum volume 56 and four
maximizing profiles; 59,809 satisfy them at strict rank 88, with
maximum volume 60 and two maximizing profiles. These counts are
controls for the case split, not a replacement for the proof.

Acceptance reconstructs the literal source and coherent matrices,
checks every basis factorization (4), verifies disjoint supports on
both sides of all three pairs, and replays all thirteen saved odd
integer minors. It checks the complete supported-column sets for
both sharp examples and the weak-rank-88 boundary example.

These theorems do not classify all extremal source spaces. Their
sharpness examples are source parameter spaces, not matrix-target
degenerations. Any target rank-pair consequence must separately use
the applicable saturated target-support inequality. No improved
matrix multiplication exponent or external review is claimed.
