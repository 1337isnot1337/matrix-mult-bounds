# Direct-product source and search normalization

Written, unreviewed and not Lean formalized. No target degeneration or smaller
matrix multiplication exponent is constructed.

The group table is the direct product of determinant-one 2x2 matrices over F5
with addition modulo two. It has 240 elements. Rational class sums and CRT
central idempotents derive the nine complex degrees of SL(2,5), using the same
exact method as the SL(2,7) source certificate. The first trial central element
is not cyclic for p=5; coefficients 1,2,4,...,256 give a cyclic generator.
The recorded determinant, factorization and idempotents verify that choice.
The original p=7 generator and its complete certificate remain unchanged.

Irreducibles of a finite direct product over C are tensor products. C2 has
two one-dimensional irreducibles, so each degree of SL(2,5) occurs twice.
The squares sum to 240. Integer root intervals give

    sum d_i^(2247/1000) < (13*13*15)^(749/1000).

The source upper numerator is 3,448,338,926,674 and the target lower numerator
is 3,544,700,077,791, both over 10^10. The existing group algebra/tensor-power
argument therefore gives omega < 2247/1000 **if** the target degeneration
exists. The source calculation alone is insufficient.

The concurrent rank-locus screen gives 217<=240, so it does not exclude this
target. This is only a necessary test. The external ordinary-TPP bound in
BCGPU ITCS 2023 Theorem 3.2 also does not exclude it: n(G)=2 and
`2*(2535-240)^2 < 240^3`. These statements do not provide a construction.

The center has four elements, three of order two. Each other-pair
count is greater than 120. By the central-involution lemma no selected set
can contain a pair differing by any nonidentity central element. Thus a
selected set uses at most one point from each of the 60 central orbits.
The presence variables and their cardinality constraints express exactly
this necessary restriction; they are additional to the pinned base SAT model.

Four explicit generators give an order-48 subgroup H, checked by closure.
Every set of size 13,13,15 has at least three points in some right coset of H.
Independently translate a chosen point in each such fiber to identity. The
whole fiber moves into H. Right quotient sets, cyclic group equations and
vertex-potential conditions are preserved. This justifies the three minimum
fiber constraints. The subgroup contains the whole center, so its quotient
uses twelve central orbits, also checked exactly.

The integer-only accepted-witness verifier is unchanged from the pinned
concurrent implementation. A small known SL(2,5) control embeds with C2
coordinate zero and checks acceptance in the product table. It does not
establish the selected target or an asymptotic family. Timed-out search and
untraced SAT outcomes are not nonexistence proofs.
