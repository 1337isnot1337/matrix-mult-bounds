# Two larger targets fail the diagonal SL2 capacity test

October 21, 2026. Exact finite representation calculation, written and
unreviewed. These are restricted-ansatz exclusions, not exclusions of
the ordinary candidates themselves or of general degenerations.

The extended ordinary scan first encounters A(7,12) -> M(35,35,35),
with source leg1512, and also retains A(7,13) -> M(37,38,38). Under the
standard diagonal SL2 action, the source leg is

    V_(a-1) tensor V_(a+b-2) tensor V_(b-1),

where V_d has dimension d+1. This is the same physical Hankel action
used in the existing cyclic-equivariant and asymmetric-seed packages:
the middle Hankel factor is the highest symmetric-power summand. The
source contains only even highest weights. Its decomposition is obtained
by the standard Clebsch-Gordan rule V_i tensor V_j = sum V_k for
k=|i-j|,|i-j|+2,...,i+j. This representation theory is external standard
input; no priority is claimed for it.

For matrix-vertex representations U,V,W, an intertwining target-leg map
requires each of U tensor V*, V tensor W*, W tensor U* to embed in the
source representation. SL2 irreducibles are self-dual, so multiplicity
comparison is an exact necessary test. Since the source has only even
weights, each nonzero vertex representation must have pure parity, and
the three parities must agree. Each target here has an odd-dimensional
vertex, so the common parity must be even highest weight. Thus every
vertex representation is an unordered partition of its dimension into
odd irreducible dimensions; this is exhaustive for the stated ansatz.

For A(7,12), source multiplicities in highest weights 0,2,...,34 are

    1,2,3,4,5,6,7,7,7,7,7,7,6,5,4,3,2,1.

There are585 representations of dimension35. Only two unordered pairs
pass the multiplicity test:

    (1,13,21) with (9,11,15),
    (1,15,19) with (7,11,17).

The entries denote irreducible dimensions. These two disjoint edges
contain no triangle, so no triple U,V,W works. For A(7,13), the vertex
lists have760,864,864 members. The three ordered compatibility graphs
have58,80,58 edges, again with no compatible triple. The complete pair
lists and integer multiplicities are in the result JSON.

The obstruction also applies to degenerations through maps intertwining
these fixed matrix-vertex actions: a missing isotypic multiplicity cannot
be repaired by Laurent coefficients, and conciseness of the target
requires full leg rank. No symmetry reduction for unrestricted maps is
asserted. Both candidates remain open to symmetry-breaking constructions.
