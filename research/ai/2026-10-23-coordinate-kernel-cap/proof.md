# Coordinate leading kernels close the mixed high-rank pairs

October 23, 2026. Owner-directed OpenAI Codex work. Written and
unreviewed over C. No independent review, formalization or exponent gain.

## 1. Precise coordinate condition

Use the canonical cyclic source A4, with leg dimension112, and the
unconstructed target M(10,10,11), with legs100,110,110. Two selected
outgoing tensor-leg maps are regular; their constant maps have coordinate
kernels in the canonical source bases. They can mix the surviving
coordinates in their output frames and have arbitrary higher jets.
The remaining map is arbitrary Laurent. When working in the dual slice
convention, use the transpose map on the corresponding regular leg.

The prior regular-leg frontier excludes limiting rank sums above192
for a long/long pair. For a short/long pair it leaves only

    (100,q), 100<=q<=107;    (p,110), 90<=p<=97,          (1)

among sums above192. This is that standalone necessary screen; other
concurrent one-regular-leg obstructions retain their separate credit.
We close all sixteen pairs (1) under the coordinate-kernel condition.
Consequently any two regular maps with coordinate limiting kernels
have ranks summing to at most192. Scalar balancing gives the same
condition for the selected maps' individual leading coefficients in
an arbitrary Laurent presentation, provided their leading kernels
satisfy the stated coordinate condition.

## 2. Hidden coordinates reduce to one coherent endpoint

Write the two constant maps, after independent output frame changes,
as coordinate projections P,Q. Their kernel coordinate counts in (1)
are either

    (12,112-q),  5<=112-q<=12,
    (112-p,2),  15<=112-p<=22.                          (2)

The total defect is at most24, strictly below32. Let W be the kernel
of the projected first-source slice map. Distinct first coordinates of
the literal source have disjoint matrix supports, so W is a coordinate
subspace: it is spanned by exactly the source coordinates whose entire
support was deleted. No cancellation between different coordinates
is possible for these constant coordinate projections.

The adopted below-twice-minimum classification puts every nonzero
element of W in g tensor h, with one fixed scalar rank-one Hankel h
for the whole space. A coordinate vector h=e_k has Hankel rank

    1,2,3,4,3,2,1  for k=0,...,6.

Thus any nonzero coordinate kernel W uses only k=0 or only k=6.
The literal reversal of all six convolution indices exchanges these
two endpoints and preserves the complete source support; the verifier
checks all4096 terms. It therefore suffices to work at k=0, where the
source first coordinates are the sixteen cells g_(i,z), 0<=i,z<4.

The active slice matrix R(g) has rows(j,L), 0<=j<4, 0<=L<7, and
columns(H,r), 0<=H<7, 0<=r<4. Cell(i,z) contributes the sixteen edges

    row(j,r+z) -- column(j+i,r), 0<=j,r<4.              (3)

Deleted coordinates outside these active28-row and28-column sets do
not help cover (3). Their deletion counts inside the sets are bounded
by (2).

## 3. Exhaustive finite matching certificate

For each of the C(16,10)=8008 ten-cell subsets, form the bipartite
graph (3) of all their coefficients. A vertex cover is necessary to
delete every coefficient of those ten cells. The exported witnesses
prove the following finite statement:

* For7744 subsets there are25 disjoint source edges, so every vertex
  cover uses at least25 coordinates.
* Each of the other264 subsets has24 disjoint source edges. Any cover
  of size24 is unique and uses24 vertices all on one side:132 subsets
  require the left side, and132 require the right side.

This statement is computationally exhaustive over the specified finite
coordinate family. No assertion about arbitrary complex subspaces
follows from it. It needs no imported vertex-cover theorem: disjoint
edges give the elementary lower bound, and the unique-cover certificate
is checked directly as follows.

A size24 cover must choose exactly one endpoint of each matched edge
and no unmatched vertex. Let x_i=1 select the left endpoint of matched
edge i, and x_i=0 its right endpoint. Every unmatched left vertex forces
the right endpoint of each neighbor to be selected; unmatched right
vertices similarly force left choices. An edge from matched left i to
matched right j imposes x_j=1 => x_i=1. Propagating these implications,
including their contrapositives, forces all24 choices. Every witness
forces all left or all right choices; the verifier also checks that
this forced set covers every edge. Therefore no other size24 cover
exists. A smaller cover is impossible by the24 matching edges.

Every budget pair (2) has total at most24 and each individual budget
at most22. It can realize neither a25-vertex cover nor a24-vertex
cover confined to one side. Hence no ten first coordinates can be
hidden and

    dim W<=9,   projected source rank rho>=103.        (4)

The constant maps may have arbitrary output frames because their
coordinate kernels alone determine which source subspaces survive.

## 4. Target support gives the contradiction

Apply the prior saturated matrix-space support inequality, with the
remaining110-dimensional target leg as the slice parameter and shared
matrix dimension10:

    rho <= 2+floor(p/10)*floor(q/10).                   (5)

For (100,q) in (1), its right side is102. For (p,110), it is101.
Both contradict (4). The saturation theorem permits arbitrary higher
jets of the two regular maps and every finite Laurent pole order on
the remaining map, so those operations cannot evade this coordinate
leading-kernel obstruction.

## 5. Evidence and limits

The matching discovery program and certificate checker are separate.
The checker contains no matching search. It checks every matching edge
against the literal source graph, disjoint endpoints, complete ordered
coverage of all8008 ten-subsets and every unique-cover implication.
It independently reconstructs all16 coefficient graphs from the
original six-index source and verifies endpoint reversal. The exported
compressed certificate contains every witness and has a pinned digest.

The existing cyclic source, low-rank classification, saturated support
condition and dense regular-leg frontier retain their original credit
with exact byte pins in sources.json. The finite coordinate matching
census and its all-order application are local continuations, without
a historical priority claim or any new external theorem. The proof is
written and unreviewed, and the finite certificate is not a formalization
or independent mathematical review. Arbitrary noncoordinate leading
kernels, smaller rank pairs and the full target remain open to this
argument. The exponent remains9/4.

The subsequent [torus reduction](torus_reduction.md) transfers the
coordinate compression bound to arbitrary complex kernels. It supplies
a separate written dense continuation; the finite graph census itself
retains precisely its coordinate scope.
