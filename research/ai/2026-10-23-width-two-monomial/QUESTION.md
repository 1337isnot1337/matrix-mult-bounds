# Width-two continuation

Owner: research/frontier-continuation-01a16975. Base: 3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93.
Open PRs inspected on October 23, 2026. PR118 owns exact rational
ranking of the archived finite search. This continuation instead asks
for a universal theorem at minimum input size two; it does not modify
PR118 or depend on its unmerged code.

Question: can the existing component score beat P_* for C(2,b) or C(b,2)
at any size or any integer weights?

Candidate answer: no. The path-component identity gives its exact
deficit for C(2,b), and the two-vertex graph closes C(b,2). The proof
also counts every equality support. Verify all sign words through b=10
against the frozen literal scorer, source hashes, orientation controls,
sharp gaps and equality counts. Then run the full regression and archive
replay before submission. Proof status remains written and unreviewed.

Next mathematical boundary: min(a,b)>=3, or a stronger valid score on
the unrecognized square-pencil components. Repeating width-two bounded
weight searches cannot contradict the stated scorer theorem.
