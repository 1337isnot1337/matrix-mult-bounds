# Concurrent research reviewed on October 20, 2026

These are other agents' contributions to the owner's repository, attributed
to their original commits. Reading a proof or a reported test result does not
constitute an independent formalization or a local replay. None reports a
smaller exponent. The public board reports remain separately attributed in
[the board review](agent_board_review.md).

| Source | Contribution and practical consequence | Review scope here |
| --- | --- | --- |
| [73b2d20](https://github.com/1337isnot1337/matrix-mult-bounds/commit/73b2d20), maintained at [b381178](https://github.com/1337isnot1337/matrix-mult-bounds/commit/b381178) | The fixed-row, fixed-column and fixed-diagonal product-filtration system is equivalent to separate concavity through zero for positive symmetric normalized profiles. This closes R2, including its boundary caveat. | Read the all-size endpoint-product/Jensen proof and converse; no separate replay of this branch's tests. |
| [b381178](https://github.com/1337isnot1337/matrix-mult-bounds/commit/b381178) | A direct scalar replication-to-limit argument, endpoint rigidity, and compactness consequence. This overlaps our actual-character bridge, which imports Uznański's rescaling theorem. | Read the branch's status and scope; detailed direct-scalar proof has not yet been audited here. Do not count the overlapping endpoint formula as another independent discovery. |
| [cf79709](https://github.com/1337isnot1337/matrix-mult-bounds/commit/cf79709) | The all-degree target and critical overhead threshold overlap our `292ba18`. Its limiting-slope estimate strengthens the conditional cost-one exponent to 125/56. We adopt that estimate with attribution and verify it under our single joint-sequence construction premise. | Read the complete growth proof and replayed the integer root certificate locally; the source degeneration remains unconstructed. |
| [e6d33e7](https://github.com/1337isnot1337/matrix-mult-bounds/commit/e6d33e7) | An entropy dual bounds every distribution in a specified optimistic score. Balanced sources have an all-size 39/40 gap; unequal sources through size 12 have exact certificates. A weighted tensor-valued extraction theorem is not claimed. | Read the general dual, balanced tail proof and finite-certificate boundary; branch tests have not been independently replayed here. |
| [89ebb78](https://github.com/1337isnot1337/matrix-mult-bounds/commit/89ebb78), [PR 2](https://github.com/1337isnot1337/matrix-mult-bounds/pull/2) | Affine-line integer-weight degenerations retain full direct sums across several filtration labels. The agent reports exact coefficient and whole-block matching certificates with no P_* violation in its finite search. | Read the squared-affine-line weight identity, domination of higher filtration terms, and Holder consequence; coefficient replay has not been independently run here. |

At [dcfc1ef](https://github.com/1337isnot1337/matrix-mult-bounds/commit/dcfc1ef)
the entropy agent published an exact SL2(5) group-potential search, a small
positive control, and scoped determinant obstructions. No target shape beating
9/4 succeeded; timeout and untraced solver outcomes remain unresolved.
The detailed group proof and its verifier have not been audited here.

At [b7cfb60](https://github.com/1337isnot1337/matrix-mult-bounds/commit/b7cfb60)
the product-filtration agent added off-leading Clebsch--Gordan coefficients,
small transvectant restrictions, and truncated-algebra source searches. Its
reported finite runs found no matching-profile violation. We read the active
queue and status; these new coefficient packages have not been replayed here.
Our branch retains the source-construction and source-obstruction task.
