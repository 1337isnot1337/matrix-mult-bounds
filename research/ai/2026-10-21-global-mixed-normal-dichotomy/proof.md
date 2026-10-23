# A uniform normal dichotomy for all mixed graphs at a=b=1

Written proof, unreviewed, October21,2026. Claim
`AI-GLOBAL-MIXED-NORMAL-DICHOTOMY-096`. This necessary-condition reduction
does not exclude a new complete target or improve the exponent.

Adopt the canonical A4 leading flags, partner a=b=1 and full B maximal
seven-frame. Let the actual C first space be any five-space containing
m+sum h_j*d_j, with arbitrary h in C^6 and boundary four-space. Adopt
the complete88-dimensional normal equations and four planes of088--094.

**Result.** Every necessary normal, modulo the four planes, belongs to
the union of two fixed linear spaces of dimensions54 and36. The first
is the kernel of ten stable boundary rows. The second is the complete
zero-projection kernel. In particular, the rank-at-most-one projection
alternative forces projection zero for every graph h.

## 1. Define both spaces before choosing a graph

Reconstruct Z0,...,Z6, the seven312-by88 source blocks. Choose the
specified constant88-by84 complement J to the four planes. Retain094's
56 source rows, concatenate all seven blocks horizontally, and take the
complete rational coefficient-row basis. This gives56 rows with seven
C columns, linear in d in C^84, without graph parameters.

In the six boundary columns write S(d)=(E0,O0,E1,O1,E2,O2) and set
Q(d)=(O0-E0,O1-E1,O2-E2). The coefficient-row kernel of this projection
gives ten combinations W(d) in its kernel. Here W denotes their three
stable boundary columns; their mixed column remains unrestricted.
Their complete linear coefficient kernel has dimension54. The complete
coefficient kernel of Q has dimension36. Exact rational row reduction
checks both statements.

All selected rows annihilate the actual C five-space, so rank S<=2.
Since the rows W are combinations of S in the projection kernel,

    rank S >= rank Q + rank W.

Thus W=0 or rank Q<=1. The first case lies in the54-dimensional family.

## 2. Exact square identities for the rank-one branch

Saved triangular two-minors of Q are nonzero rational multiples of
squares of linear forms. Their complete kernels give84->52->48.
On the resulting frame P, the projection coefficient map has rank12.
Twelve independent coefficient columns define a46-by3 matrix T(x),
linear in twelve active variables. An exact rational matrix C satisfies

    Q(P*u)=T(C*u).

The verifier checks all coefficients, retaining the36 inactive directions.
The certificate gives68 actual two-minors f_i of T and eight independent
linear forms L_j with exact rational identities

    L_j(x)^2 = sum_i a_ji*f_i(x),       j=1,...,8.

These are checked over Q in all78 quadratic monomials. Rank Q<=1 makes
all f_i zero, hence all L_j zero over C. The complete kernel of L*C
reduces48 coordinates to40. A radical calculation suggested the forms
during discovery; no claim about that algorithm enters the proof.

## 3. The actual mixed row forces projection zero

Let P40 be the84-by40 resulting frame and N=J*P40. The actual row gives

    M(h)*N*u=0,       M(h)=Z6+sum h_j*Zj.

The source partition splits these40 coordinates into two groups of20.
The residual projection coefficient map has rank four, two in each group.
Let B_g be a complete two-row basis of its coefficient map on group g.
Retain25 specified mixed-equation rows in that group, obtaining a25-by20
polynomial matrix A_g(h). The saved2-by25 matrices U_g(h) have degree at
most one and satisfy the exact polynomial identities

    U_g(h)*A_g(h)=B_g,       g=0,1.

The checker reconstructs A_g from all original Z blocks and N, checks
every coefficient over Q[h0,...,h5], verifies both20-coordinate groups
cover all40 coordinates, and recomputes the complete row bases B_g.
No graph-dependent determinant is inverted and no exceptional h is
removed. The actual mixed equations therefore imply B_g*u_g=0 and Q=0.

The resulting complete kernel has dimension36 and equals the original
zero-projection kernel, checked by combined exact column rank. This
proves the dichotomy for all six graph parameters at a=b=1.

## 4. Scope

Adding back planes gives dimensions58 and40 in the original normal
space. This union is a necessary enclosure, not a set of constructed
maps. Further mixed-row, source-rank and higher-order conditions remain.
Other partners and leading flags are outside the claim. Previous point
and open-set exclusions retain their own scope. The written proof has
no independent mathematical review or formalization.
