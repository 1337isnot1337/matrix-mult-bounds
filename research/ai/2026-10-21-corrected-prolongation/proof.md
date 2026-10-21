# Complete second jets with full boundary first frames

Written proof with exact rational and polynomial certificates, unreviewed,
October 21, 2026. This constructs finite-order local-map data. It does not
construct a matrix tensor limit or establish an exponent improvement.

## Fixed frames and the first equation

Adopt the canonical source, four covectors G, leading source indices A0,
and kernel coordinates K from PR45, now on main. The leading first space
W0 has dimension 12. Split the canonical extension bases as boundary D_B,D_C
of dimension 16 plus four mixed covectors. Each D contains G.

Use 110 output rows on each regular leg. Put G in rows 0,...,3 at order 0,
and put the sixteen D_B,D_C covectors in rows 4,...,19 at order 1. All other
outside-leading rows have zero first coefficient. The four leading rows
at order 1 are unknown P1_top,Q1_top, with 896 scalar entries.

The first partial space remains W0 precisely when their canonical 400 by 896
coupled matrix vanishes on these entries. Its rank 364 and nullspace basis N
of dimension 532 are adopted and replayed from the canonical package.
Outside first rows already obey the extension constraint. There is a unique
linear first-row correction Y on K, supported on A0, with

    S1_K = Y S0_A0.

It is computed using a fixed invertible12 by 12 column minor of S0_A0.
The code verifies this equality in all 16 leading output coordinates.

## Corrected off-diagonal second equations

For a new B row b1 in D_B, the complete second residue has off-diagonal
coefficient

    T(K,b2,G)+T(K,b1,Q1_top)-T(Y(K),b1,G).

It must vanish. The analogous expression holds for a new C row. The
last term is the first-row correction; omitting it gives a different
and incomplete system.

The map b2 ->T(K,b2,G) has rank 92 in 400 coordinates, so its cokernel
has dimension 308. Projecting the right side to that cokernel gives308
linear equations on the 532 first parameters for each of sixteen rows,
on each side. The resulting9856 by 532 matrix has rank 360. Its nonzero
360 by 360 minor certifies the lower bound. A 172-column nullspace basis
annihilates the full system and has a nonzero172 by 172 minor. Thus the
allowable leading first coefficients form exactly a 172-dimensional space.

The frozen basis has312 nonzero rational entries as an896 by 172 matrix.
Projecting onto the coefficients outside the fixed56-dimensional boundary
spaces has rank 28, certified above and below. Thus a first-order departure
from those spaces survives the complete off-diagonal second equations.
The statement is about this fixed boundary-frame family, not the maximal
sixteen-dimensional effective extensions on both sides excluded in PR46.

## The leading second block has no additional obstruction

Let theta denote all 172 parameters. The residual leading4 by 4 block of
the full second coefficient, after the first-row correction, is

    R(theta)=T(K,P1_top,Q1_top)-Y(theta) S1_A0,top(theta).

Project it to the four annihilator coordinates of W0. The leading P2_top,
Q2_top variables enter through the same rank 364 coupled matrix as before.
Its left cokernel has dimension 36. Therefore the complete additional
obstructions are36 homogeneous quadratic polynomials in theta.

Every one of those polynomials is identically zero over Q. The code
constructs the full expressions before coefficient collection; it does
not test only coordinate axes or random parameter values. This is an
exact polynomial identity for all complex theta.

Consequently every theta admits second coefficients: apply fixed rational
right inverses on the rank 92 images to choose the sixteen new b2,c2 rows,
and a fixed right inverse on the rank 364 image to choose P2_top,Q2_top.
All other second rows may be zero. These choices are linear, respectively
quadratic, in theta. The outside-by-outside block is already zero on K
because T(K,D_B,D_C)=0. All four output blocks have now been included.
There is a second correction Z, supported on A0, such that

    S2_K - Y S1_A0 = Z S0_A0.                           (1)

Thus this is a polynomial family of complete compatible second jets.
It satisfies the necessary W2=W0 constraint proved in PR47. It supplies
no evidence that those jets lift through every later order.

## Explicit coefficient witnesses

The report stores two rational assignments and all of their P0,P1,P2,
Q0,Q1,Q2 entries. It also stores Y and Z. One assignment uses parameter 24;
the other uses parameters 24,25,100,164 with weights1,2,-1,1. The latter has
nonzero leading second coefficients and a nonzero Z, so it exercises the
quadratic cross terms and second correction.

For each assignment, all first and second coefficients are contracted
from the original4096 source terms. The identities S1_K=Y S0_A0 and (1)
are checked in every one of the 20 by 20 active output positions. The other
ninety output rows have zero coefficients through order 2, so all remaining
positions in the 110 by 110 tensor are identically zero by construction.
A separate fixed-index formula in the tests reconstructs every active
coefficient on all 112 first indices independently.

The regular first-leg change with K rows

    e_K - t Y e_A0 - t^2 Z e_A0

and unchanged A0 rows has determinant1. All 100 corrected K rows start at
order at least3. This is a finite-order statement, not a matrix tensor.

If desired, add t^3[I110 0] to both regular leg maps. The selected square
minor then has highest-degree coefficient 1, so the maps are generically
surjective. This preserves the verified second jets, but asserts none of
the subsequent matrix-limit conditions. A complete construction still
requires those conditions, an actual full Laurent first-leg map and the
complete target coefficient identity.
