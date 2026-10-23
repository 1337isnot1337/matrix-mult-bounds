# Finer full-source S5 cube bounds

October 23, 2026. Claim `AI-S5-PEIRCE-COVERS-003` is a written,
AI-derived proof with exact finite certificates. It is unreviewed and
not formalized. No smaller matrix multiplication exponent is established.

## Result

For the full group trace tensors T_r of S5 x C2^r in characteristic two,

    SR(T_1^tensor(3)) <= 6638912,
    SR(T_2^tensor(3)) <= 41159136.

Every one-copy degeneration to a single M(a,b,c) therefore requires
abc<=2576 for r=1, or abc<=6415 for r=2. The r=2 result excludes five
more shapes left open by the preceding weighted cube bound:
(18,18,20), (17,18,21), (15,18,24), (18,19,19), and (17,19,20).
The four remaining shapes in that pinned frontier are
(16,16,25), (16,19,21), (14,19,24), and (16,20,20).
The r=1 frontier still has (13,13,15) and (13,14,14).

Over C these statements transfer only to the maintained coefficient-one
injective-coordinate/integer-potential constructions. General complex
cancellation identities, arbitrary source powers and target constructions
remain outside this result. No optimality of the new bounds is claimed.

## Actual source, not a leading limit

The earlier S5 block-filtration discovery saved an 88-vector candidate
basis of the principal block. We use those vectors as candidates, retaining
their provenance, and verify the source from scratch. A 32-vector
complement is obtained from the prior central idempotent: first choose
16 independent vectors from the projected radical, then extend through
the projected group basis. The resulting 120 binary vectors are exported.

The replay independently constructs S5 as the lexicographically ordered
permutations of five symbols, with multiplication p after q. It verifies
rank 120 of the exported change of basis. For every pair of basis vectors
it forms their group-algebra product, then pairs with every inverse basis
vector to evaluate the identity coefficient of xyz. Thus all 120^3=1728000
original source coefficients are checked exactly over F2.

There are 1198 principal terms and 6964 small-block terms, with no terms
crossing between the 88 and 32 coordinates. The small block's binary degree
histogram is 16+16t, and every nonzero triple has total degree at most one.
This is a verified tensor direct sum. We do not assume an isomorphism of
the small block with a matrix algebra over dual numbers.

The 88 principal coordinates have 19 retained type labels, whose counts
are (1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,16,16,16). The replay recovers all 52
unordered type triples of actual nonzero coefficients. Assign either of
the following integer degrees to the nineteen labels in that order:

    d_minus=(12,8,10,6,6,2,4,0,11,7,5,1,11,7,5,1,12,6,0),
    d_plus =(12,12,6,6,6,6,0,0,9,9,3,3,9,9,3,3,12,6,0).

For each assignment, every actual principal triple has total degree at
most 12. The replay checks this condition on all original coefficients;
it is not inferred from the old discovery support or a numerical solution.
The two one-leg degree polynomials are

    P_minus(t)=17+8t+t^2+t^4+8t^5+18t^6+8t^7+t^8+t^10+8t^11+17t^12,
    P_plus(t)=18+16t^3+20t^6+16t^9+18t^12.

All lower-degree terms of the source are retained. The refined degrees
need not be radical-ideal indices; their full-source support inequality
is exactly the property the finite slice cover requires.

As an additional verified witness, every principal coefficient meets the
type set {6,7,10,11,18}, which contains 26 coordinates. Its membership bit
can therefore give another support inequality. The selected bounds below
do not use this bit; no gain from it is claimed.

## Eight explicit word covers

In a cube block word with j principal factors, put k=3(r+1)-j. The
degree-one factors are the 3-j small blocks and the 3r central C2 factors.
For the latter use the full invertible basis (1,1+z). Its trace includes
the zero-degree term, and every supported triple has degree at most one.

Use P_minus for j=0,1,2 and P_plus for j=3. Give every degree-one factor
weight h. The one-leg polynomial is

    16^(3-j) P(t)^j (1+t^h)^k,

and every nonzero triple has total weighted degree at most 12j+kh. This
is the source support budget; it must not be replaced by the maximum
degree of a one-leg polynomial for other weight choices.

Choose cutoffs whose sum is 12j+kh-2. Any triple avoiding all three lower
degree sets would have total degree at least12j+kh+1, a contradiction.
Assign each coefficient to its first covering coordinate. This gives a
slice decomposition, whose cost is the sum of the three coordinate
counts. Summing over the eight block words uses no submultiplicativity
assumption about general slice rank.

| r | j | h | Cutoffs | Slices per word | Word multiplicity |
|---:|---:|---:|---|---:|---:|
| 1 | 0 | 1 | (1,1,2) | 147456 | 1 |
| 1 | 1 | 5 | (9,13,13) | 387328 | 3 |
| 1 | 2 | 5 | (14,14,14) | 945264 | 3 |
| 1 | 3 | 6 | (17,17,18) | 2493680 | 1 |
| 2 | 0 | 1 | (2,2,3) | 909312 | 1 |
| 2 | 1 | 5 | (14,18,18) | 2382848 | 3 |
| 2 | 2 | 5 | (19,19,19) | 5854752 | 3 |
| 2 | 3 | 6 | (23,23,24) | 15537024 | 1 |

The totals are 6638912 and 41159136. The producer multiplies integer
polynomials; the separate verifier instead enumerates ordered type tuples
and all binary degree choices with their full coordinate multiplicities.
It recomputes the source budget directly from the fully replayed support,
then checks every cutoff and total.

## Target implication and evidence limits

The [preceding S5 cube proof](../2026-10-23-s5-finite-covers/proof.md)
records the precise characteristic-two transfer, slice-rank closedness,
and cyclic three-copy argument. It retains the external bounded-rank
matrix-space theorem of Flanders/Meshulam, as stated in de Seguins Pazzis,
arXiv:1507.05375v2, Theorem 1.1, over an arbitrary field. That dimension
theorem yields the finite equality SR(M_m)=m^2. These external facts and
their prior local derivation are reused unchanged, with their credit.

Cyclic symmetry converts a proposed one-copy M(a,b,c) into a target
M(abc,abc,abc) of the source cube. Hence (abc)^2 is at most the appropriate
new bound. The integer square roots are 2576 and 6415. Target classification
is recomputed from the original complex rank-locus/Koszul frontier and
the preceding pinned cube bound. No test survivor is called a construction.

The old monotone staircase census used the coarser radical-degree
majorants. The new full-source degree assignments change that input, so
these smaller bounds do not contradict its finite-class minimum.

Discovery tested 5400 integer weight choices per block word, including
two common-cover bits. That finite search is not used to certify global
optimality. Acceptance depends on the exported full basis, actual source
coefficients, eight explicit covers and exact target comparisons.
All work here is owner-directed Codex work and has no independent
mathematical review or formalization.
