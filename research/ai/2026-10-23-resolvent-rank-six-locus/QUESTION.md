# Rank-six locus of the fixed-resolvent limit space

October 23, 2026. Discovery in progress; no new theorem claimed here.

Base: main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.
This continues the open structural question in `docs/research_directions.md`
and the merged `AI-RESOLVENT-SHARP-MINRANK-001` package (PR139).
It does not repeat the Sections 1–4 proof audit in PR163.

Question: classify all rank-six matrices in the 112-dimensional limiting
space W and determine their compatible rank109 compression kernels.

Initial exact row reduction finds rank six for every monomial Q(e_i0),
0<=i<=3. After the invertible left change K, these four matrices have
the same six potentially nonzero rows. This suggests a common-image
linear family. Whether it exhausts the rank-six locus is open.

Intended output: a written proof with an exported integer certificate,
an acceptance verifier separate from discovery, and explicit sharpness
and compression examples. Work over every field where justified; keep
the separate Laurent applications over C and their hypotheses explicit.

No smaller exponent, general singular-degeneration exclusion, independent
review, or formalization follows from the initial calculation.
