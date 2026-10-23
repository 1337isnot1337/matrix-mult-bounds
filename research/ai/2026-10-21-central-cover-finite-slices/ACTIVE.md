# Active finite-power question

Base: canonical main `be66e0f3f14364afde6a56d055ce2c5a90dae754`
(merged PR #98). No overlapping open PR owns this question.

Question: does a finite tensor power of the full characteristic-two source
`A5 x C2` have slice rank below the corresponding `M10` power, despite the
asymptotic lower barrier in `AI-CENTRAL-COVER-SLICE-BARRIER-001`?

Intended output: an exact full-source support check, an independently
counted slice cover of its cube, and a proof of the resulting coordinate/
potential exclusion. The target's finite slice-rank lower bound must apply
in characteristic two. The complex semistability citation alone is not
used for that transfer.

The full-source verifier passes. It checks all 216000 coefficients and
counts 1728000 one-leg cube coordinates, giving SR<=973422. Cyclic
symmetry forces abc<=986 for any single rectangular target, excluding
M10 and M(9,10,11). All 831 local test IDs have successful results: 828
in the maintained environment and three optional numerical controls in
the existing discovery environment. The final five focused and 18
metadata tests pass. All five historical experiments replay, and all 18
tracked archive files are byte-identical to the canonical base. Receipts
are in `results/central-cover-finite-slices-2026-10-21/`.

Next: submit the focused PR through normal rules and wait for complete
current-head hosted CI. Merge acceptance does not confer math review.

The calculation does not give an upper bound for the nonsplit source
`SL(2,F5)` or its product with C2. Their degeneration to the split source
has the wrong direction for transferring this upper bound. No exponent
improvement or independent review is claimed.

Integration with canonical `39378de` preserves all 278 existing claims.
The combined inventory is 839 tests in 198 modules. All 31 focused
A5/cube/A4/metadata checks pass, including all eight newly added A4 tests.
The complete hosted suite on the final combined head is still required.
