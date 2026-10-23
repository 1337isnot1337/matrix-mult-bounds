# Complete bounded physical-subset search at a=24 through36

October 21, 2026. Verified finite computation using written, unreviewed
ordinary-map obstructions. No improved exponent.

For each balanced source A(a,a), 24<=a<=36, choose the smallest integer n
with216*n^3>(6*a-2)^4. Each matrix vertex is restricted to a multiplicity-
free subset of the physical irreducible dimensions1,3,...,2a-1, with at
most five summands and total dimension n. This is a precise bounded
ansatz, not all possible vertex representations or all target shapes.

The exhaustive capacity graphs contain4070 compatible unordered triples.
Of these,1211 contain the top irrep2a-1 at all three vertices and are
excluded by the existing shared-top-irrep polynomial obstruction. The
remaining2859 violate the ordinary invariant-slice rank inequality in
invariant_slice_pairing.md. No ordinary triple survives in this domain.
The source channel ranks used by the filter are recomputed exactly
modulo65519, and every used source invariant slice has full rank.

The first implementation used scalar Counter-based Clebsch-Gordan loops
and took1575.604 seconds. A second implementation precomputes the binary
Clebsch-Gordan interval array and sums it for each vertex pair using
int16 arrays. Every accumulator is at most25, so these are exact integer
operations, with an explicit overflow guard. It uses no floating point
for capacity decisions. The implementations agree on every source count,
every exclusion witness, and every rejected triple; a normalized digest
records that comparison. The complete second replay and its source
multiplicity test pass in47.922 seconds.

The full result is losslessly compressed; the readable summary contains
its uncompressed SHA256, the cross-implementation digest, and each source's
counts. Source certificate ranks and all invariant-slice witnesses are
included in the full result and recomputed by the verifier.

The new slice inequality is not a closed obstruction under arbitrary
singular limits. Consequently the2859 slice-rejected triples are not
claimed excluded as Laurent degenerations. Repeated irreps, more than
five summands, nonphysical vertex irreps, other sources and target shapes,
and symmetry-breaking maps are outside this search.
