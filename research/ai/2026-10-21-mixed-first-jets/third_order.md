# A third-order obstruction for the fixed mixed first spaces

Written proof, unreviewed, October 21, 2026. This closes a specified local
family; it does not improve the exponent or exclude other leading flags.

## Statement

Use the source and leading rows G from [the two-jet family](family.md).
Consider regular maps P,Q to the two 110-dimensional output legs, and an
arbitrary Laurent map on the first leg. Normalize the four leading rows
to G and remove G components from the first new rows by regular output
row operations. Suppose that the first new-row spaces are exactly the
fixed V_B,V_C in `seed.json`, of dimensions 14 and 6. Then the regular
limit cannot be M(10,10,11), whatever the higher coefficients.

The statement concerns these specified subspaces, not every pair of
dimensions 14 and 6. The two-jet certificate remains valid: the obstruction
uses a third coefficient and the target's minimum slice rank.

## 1. Normal first errors and their next corrections

Adopt the notation of the [moving-boundary proof](../2026-10-21-moving-boundary-flags/proof.md).
Write K_inf for its 64-dimensional annihilator, distinguishing it from
the 100-dimensional kernel of the leading first flattening. The boundary
spaces F_B,F_C have dimension 56, and

    T(K_inf,F_B,F_C)=0,
    ann T(K_inf,-,G)=F_B,  ann T(K_inf,G,-)=F_C.        (1)

Each nonzero first slice of the proposed target has matrix rank at least
11. Its slice space R has dimension 100, and the leading space W0 has
dimension 12. If L0 is the saturated limiting first-row space, then

    L0 = R direct-sum W0,    L0 intersect C0 = W0,     (2)

where C0 is the old cross, supported on the first four rows or columns.
Indeed L0 has dimension at most 112, every matrix in C0 has rank at most
8, and W0 is contained in L0 intersect C0.

For proposed normal variations D_B,D_C of the four leading rows, the
first equation on x in K_inf is

    T(x,D_B,G)+T(x,G,D_C)=T(y_x,G,G),                 (3)

with y_x uniquely supported on the twelve leading first coordinates A0.
The next off-diagonal equations require corrections b',c' satisfying

    T(x,b',G)+T(x,b,D_C)-T(y_x,b,G)=0,
    T(x,G,c')+T(x,D_B,c)-T(y_x,G,c)=0                 (4)

for every b in V_B and c in V_C. Equation (3) leaves 228 of the 448
normal parameters. Eliminating the correction rows in (4) gives 470
distinct equations of rank 212, hence a 16-dimensional normal space.
The sixteen directions of the frozen two-jet family are independent
solutions, and therefore span this entire space. `third_order.py`
reconstructs the equations from the source and verifies both inclusions
and the rank. The result allows arbitrary correction rows, rather than
assuming the particular corrections saved in the family.

## 2. A projected third coefficient independent of the correction choice

For a normal solution D, use the saved corrections b'_D,c'_D. Define
the 14-by-6 matrix, linearly in D and x, by

    J_D(x)[b,c] = T(x,b'_D,c)+T(x,b,c'_D)
                 -T(y_x,b,c),        x in K_inf.     (5)

This is the new-by-new part of the next regularized row. A different
solution b',c' of (4) differs by F_B,F_C, by (1). Since V_B is contained
in F_B and V_C in F_C, these differences contribute zero to (5).
Rows with zero first coefficient likewise have second corrections in
F_B,F_C and add no projected entries. Consequently (5) describes the
entire new-by-new block, padded by zeros to the full output dimensions.

Boundary components of D give zero in (3), so y_x=0; their terms in
(4) also vanish and their corrections can be taken zero. They make no
contribution to (5). Higher leading-row corrections affect the old
cross only. A second source-row correction multiplies a first tensor
coefficient whose new-by-new block is zero, so it also disappears under
this projection. These facts are the reason (5) is an obstruction for
arbitrary later maps, not merely for the displayed truncation.

If a regularized row has constant term M in L0 with projected block
J_D(x) of rank at most 2, then J_D(x)=0. To see this, write M=r+w using
(2). The difference between r and its new-by-new block is in C0, hence

    rank(r) <= rank(J_D(x))+8 <= 10.

The target's minimum rank forces r=0, so M belongs to W0 and its
projection is zero. This is the same rank-gap principle used in the
concurrent [no-second-growth theorem](../2026-10-21-second-jet-rank-one/rank_one.md),
applied here to a later coefficient and different source slices.

## 3. Two exact rank covers

Use source coordinate index (4*i+s)*7+z, and parameter coordinates
a0,...,a15 from the frozen family. The complete matrices (5) are
reconstructed by source contraction, with no sampled-parameter inference.

For source indices 36,37,39,40, only output row 13 of J_D(x) can be
nonzero. For 43,44,46,47, only row 12 can be nonzero. Thus all eight
matrices have rank at most 1 for every complex parameter value. Their
forced vanishing gives six independent linear equations, leaving ten
parameters.

On that ten-dimensional space, source indices 64,65 have support only
in output rows 9,11, and indices 71,72 only in rows 8,10. These four
matrices have rank at most 2 for every remaining parameter value.
Their forced vanishing gives six further independent equations.

The remaining four-dimensional parameter space has basis

    -e5+e12,  -e9+e13,  -e0-e7+e14,  -e2-e11+e15.    (6)

Substitution into the sixteen leading-row directions identifies its
image exactly with the common-plane tangent directions

    (D_B)_z = -e_(k,j,z), (D_C)_z = e_(j,k,z),
    j in {0,3}, k in {1,2}, z in {1,2,4,5}.           (7)

The certificate supplies rational ranks and nonzero modular minors.
The universal matrix-rank upper bounds follow from the explicit row
covers, so hold at special parameter values as well as generic ones.
All 64 projected source matrices vanish on (6), which is also checked.

## 4. Applying the same obstruction at every order

Use the formal graph chart of a plane U(t) of cubic forms from the
moving-boundary proof. It gives boundary spaces F_B(t),F_C(t) and a
regular rank-64 annihilator K_inf(t), with the exact identity

    T(K_inf(t),F_B(t),F_C(t))=0.                      (8)

Suppose every row is in these boundary spaces modulo t^N, N>=1.
Project the maps to those spaces and denote their errors by t^N D.
For a moving source row x(t) in K_inf(t), the coefficient of order N
is in the old cross. Equation (2) places it in W0; the annihilator
equalities force every new-row normal error to vanish. Only the four
leading rows on each side can have a normal error D at order N.

Subtract t^N y_x S(t), where S(t)=(1,P(t),Q(t))T. The coefficient of
order N+1 remains in the old cross, so (2) again places it in W0.
The off-diagonal equations are precisely (4) for the fixed first new
rows. Subtract the corresponding t^(N+1) z_x S(t) as well. Dividing by
t^(N+2) now gives a regular row of the generic first-row space, whose
constant term lies in L0.

Its new-by-new block is (5). Indeed the new rows have first coefficients
t b,t c and no normal error through order N; the first possible normal
corrections there are t^(N+1) b',t^(N+1) c'. At order N+2 their products
with the first rows give the first two terms of (5). The source-row
subtraction gives the last term. A product of two new-row errors starts
at order 2N+2>N+2. Higher terms of x(t), of the boundary maps, and of
the moving normal frame do not change this first new-by-new coefficient.
The t^(N+1) source-row subtraction starts at order N+3 in this block.

The two rank covers therefore force D to be a common-plane tangent.
Adjust the four graph coefficients of U at order N to absorb it.
Since all new rows have zero constant term, this adjustment preserves
their boundary membership modulo t^(N+1). The induction continues.

Thus all rows of P,Q lie in formal boundary spaces of rank 56.
Their generic flattening ranks are at most 56, and those ranks cannot
increase in a regular limit. This contradicts the two concise
110-dimensional target legs, completing the specified exclusion.

## Attribution and limits

The common-plane induction and its first two equations come from the
earlier moving-boundary package. The rank-gap argument adopts the
concurrent second-jet work. The new content is the complete normal space
for this fixed mixed seed, its correction-independent next projection,
and the two successive universal rank covers. Exact replays and CI are
generating-session verification, not independent review or formalization.
Other mixed subspaces, smaller or delayed first extensions, different
leading maps, and general tensor degenerations remain outside the claim.
