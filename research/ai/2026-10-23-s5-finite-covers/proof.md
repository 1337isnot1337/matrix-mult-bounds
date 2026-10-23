# Finite weighted covers for S5 central sources

October 23, 2026. Claim `AI-S5-FINITE-COVERS-001` is a written,
AI-derived proof with exact finite certificates. It is unreviewed and
not formalized. No exponent improvement is established.

## Result and scope

Write T_r for the identity-coefficient group trace tensor of S5 x C2^r.
Over every characteristic-two field, the following finite bounds hold:

    SR(T_1^tensor(3)) <= 6867542,
    SR(T_2^tensor(3)) <= 42493572.

Consequently a degeneration of T_1 to a single M(a,b,c) requires abc<=2620,
and a degeneration of T_2 requires abc<=6518. This excludes M19 in the
second source: 19^6=47045881>42493572. It does not exclude M(13,14,14)
in the first source: 2548^2=6492304<6867542.

The same exclusions apply over C to the maintained injective-coordinate,
coefficient-one, integer-potential constructions, which reduce to
characteristic two with their intended coefficients unchanged. They do
not exclude arbitrary complex basis changes or cancellation identities.
The result concerns one-copy source constructions. No blanket exclusion
of arbitrary higher source powers or optimality of the covers is claimed.

## Certified algebra input

Adopt the exact radical and central-idempotent certificate of
[AI-S5-BLOCK-FILTRATION-001](../2026-10-21-s5-block-filtration/proof.md),
with its prior attribution. The new certificate pins its source bytes.
The old verifier is rerun, including all 28800 representation products,
24360 group-algebra products, centrality on all 120 elements, and the
projected radical ranks. This gives an algebra direct sum of dimensions
88 and 32, with multiplicative radical layer polynomials

    P(u)=17+9u+9u^2+18u^3+9u^4+9u^5+17u^6,
    Q(v)=16+16v.

A basis adapted to the radical powers of the first block has no nonzero
trace coefficient at total degree above six. In the second block the
corresponding bound is one. Indeed, the product belongs to the radical
power indexed by the sum of the three degrees, and that power is zero
above the specified maximum. Lower-degree terms are retained throughout.
Products involving both central blocks vanish.

For each central C2 factor use the invertible basis (1,epsilon), where
epsilon=1+z and epsilon^2=0. Its trace support includes (0,0,0), as well
as (1,0,0), (0,1,0), (0,0,1). Its total degree is at most one; it is not
replaced by a degeneration. These facts bound the actual full source.

## Finite cover for a block word

Expand the cube into its eight words in the two central blocks. A word
with j principal factors has k=3(r+1)-j degree-one factors: 3-j from the
small blocks and 3r from the central group factors. Its one-leg bidegree
polynomial is

    16^(3-j) P(u)^j (1+v)^k.

For every supported triple, the sum of its principal degrees is at most
6j and the sum of its degree-one degrees is at most k. Assign positive
integer weights s,h to these two degrees. Then the total weighted degree
of a nonzero triple is at most D=6js+kh.

Choose integer cutoffs c1,c2,c3>=-1 with sum at least D-2. Cover the
coordinates of leg i of weighted degree at most ci. If a supported triple
avoided all three sets, its total degree would be at least
c1+c2+c3+3>=D+1, a contradiction. Assign each tensor coefficient to its
first covering coordinate in a fixed order. This is an explicit slice
decomposition, costing the sum of the three covered coordinate counts.

If a_d is the coefficient of t^d in P(t^s)^j(1+t^h)^k, the cost per word
is therefore

    16^(3-j) sum_(i=1..3) sum_(d<=ci) a_d.

There are binomial(3,j) words of this type. Concatenate these decompositions;
no submultiplicativity assertion about slice rank is used.

| r | j | k | (s,h) | Cutoffs | Slices per word | Words |
|---:|---:|---:|---|---|---:|---:|
| 1 | 0 | 6 | (1,1) | (1,1,2) | 147456 | 1 |
| 1 | 1 | 5 | (2,5) | (9,13,13) | 397568 | 3 |
| 1 | 2 | 4 | (1,3) | (7,7,8) | 997536 | 3 |
| 1 | 3 | 3 | (1,3) | (8,8,9) | 2534774 | 1 |
| 2 | 0 | 9 | (1,1) | (2,2,3) | 909312 | 1 |
| 2 | 1 | 8 | (2,5) | (14,18,18) | 2440192 | 3 |
| 2 | 2 | 7 | (4,11) | (40,40,43) | 6165024 | 3 |
| 2 | 3 | 6 | (1,3) | (11,11,12) | 15768612 | 1 |

Summing the last two columns gives the asserted bounds. The weights were
discovered in the finite grid 1<=s,h<=12 with gcd(s,h)=1. Acceptance checks
only the exported covers; no global optimality is inferred from this grid.

## Target comparison

The [earlier finite-cover proof](../2026-10-21-central-cover-finite-slices/proof.md#4-finite-matrix-multiplication-slice-rank-in-characteristic-two)
derives SR(M_m)=m^2 over every field from the arbitrary-field matrix-space
bound in de Seguins Pazzis, arXiv:1507.05375v2, Theorem 1.1. We use its
dimension inequality for linear subspaces, retaining the credits to
Flanders and Meshulam. Section 1.1 allows an arbitrary field. This is an
external theorem, not a new local result.

For clarity, a p+q+s slice decomposition with p+q+s<m^2 would give a
matrix subspace U of dimension at least m^2-p, every element of which
has rank at most floor((q+s)/m). The external theorem implies
dim U<=m floor((q+s)/m)<=q+s, a contradiction. Expanding along one leg
gives the matching upper bound m^2.

After extension to an algebraic closure, bounded-slice-rank loci are
closed: for each possible allocation of slices to the three legs, use
the closed incidence condition over the product of the relevant
Grassmannians, then its proper projection. Linear maps also cannot
increase slice rank. These are the same hypotheses and argument used in
the earlier proof.

The group trace is cyclic. A degeneration T_r -> M(a,b,c) therefore gives
three cyclically rotated degenerations. Their tensor product is
T_r^tensor(3) -> M(abc,abc,abc). Hence (abc)^2 is at most the saved cube
bound. The integer square roots are 2620 and 6518, respectively.

## Exact frontier consequence and limits

Compare the existing, byte-pinned S5 block-filtration frontier, whose
complex rank-locus and full Koszul tests and external sources are reused
without change. Of its six surviving sorted shapes for r=1, four are
newly excluded in the coordinate/potential class. The remaining shapes are
(13,13,15) and (13,14,14).

Of its 45 surviving sorted shapes for r=2, 36 fail the new cube bound.
Two were already excluded by the prior asymptotic bound, so there are
34 additional exclusions. The nine remaining shapes are
(16,16,25), (18,18,20), (17,18,21), (15,18,24), (18,19,19),
(17,19,20), (16,19,21), (14,19,24), and (16,20,20).

All 38 new exclusions are listed in the certificate. None of the remaining
shapes is constructed. The verifier separately enumerates grouped one-leg
coordinates, preserving all multiplicities, and exhaustively tests the
bidegree support majorant against the cutoffs. This is independent code
replay by the generating session, not independent mathematical review.
