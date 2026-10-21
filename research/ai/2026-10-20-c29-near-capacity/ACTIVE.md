# C29 near-capacity construction question

Source main: fc2eadb (refreshed after PR #24 and the SL2(7) merge). Branch: research/c29-near-capacity-20261020.

Question: classify three three-point subsets of C29 with an injective sum
map, then use the exact classification before fitting a (10,10,10)
coordinate-potential target in C29:C4.

Reason: the abelian-coset bound forces every normal fiber of such a target
to have at most three points. Each family has either sizes (3,3,2,2) or
(3,3,3,1). Its largest normal-fiber triples therefore sum injectively to
27 of 29 elements. This near-capacity condition may sharply restrict their
directions before offset discovery.

An exploratory computation found five first-set affine templates and six
ordered normalized sum triples, all arithmetic progressions. Rebuild this
with a separate exhaustive checker before using it as a claim.

No exponent improvement or group-level construction is established.
Separate PR #24 records the fixed-base F8 single-plane experiment; other
workers own the cyclic-source and SL2(7) investigations.

Completed: independent normal classification agrees; all six size-ten
bases leave twelve local configurations and all fail identity gluing.
The separate affine-system solver also rejects all twelve. Written proof
and reports are in this package. General degeneration remains open.

Next construction question: the exact degree-sum and rank-locus frontier
for source C29:C4 leaves (9,9,11), (9,10,10), and (10,10,10). Only the last
is closed in the stated coordinate-potential class by this package.
