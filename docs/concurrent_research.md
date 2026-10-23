# Concurrent research reviewed on October 20, 2026

## October23: remove the A4 unit-lift hypotheses

At main `1c04903`, the new `research/a4-one-regular-leg-20261023` question
continues PR105 while preserving the separate PR103 resolvent, PR104
asymmetric-boundary and PR107 conic investigations. The complete proof is
in `research/ai/2026-10-23-one-regular-leg/proof.md`: a regular right-inverse
kernel correction excludes the full target whenever either long map has
a regular rank110 limit, without assumptions on the original unit lift.
Next: address candidates whose scalar-balanced leading long maps are both
singular. The result is written and unreviewed; no smaller exponent.

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

Additional source-pinned review on October 20:

- [`d2d505c`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/d2d505c)
  strengthens the canonical target's ordinary-restriction overhead from
  asymptotically 50 percent to 100 percent, by using its minimum nonzero slice
  rank km instead of the maximum. We read the proof and adopt it with exact
  slice controls in `source_obstructions.md`. Its separate fixed-shared
  homomorphism obstruction is weaker than our catalecticant bound, as that
  branch explicitly records. Its finite Chebyshev search overlaps our basis
  choice; our orthogonal-basis proof and center enumeration are distinct.
  That branch's search tests were not replayed here.
- [`f6f307c`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/f6f307c)
  proves the two-sector inequality 2P(a,b)<=(a+2b-1)^(1/t). Combining this
  with critical-profile rigidity gives the nonempty amplitude interval
  1/Gamma(4/3)<=K<=(16/9)^(1/3). We read the explicit weights, all-size
  matching-profile compatibility factorization and amplitude optimization;
  this narrows a necessary interval without excluding a critical character.
- [`75f453b`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/75f453b)
  gives a projective rank-locus obstruction to general complex degenerations
  from semisimple algebra tensors. We read the dimension and closed-incidence
  proof. It excludes SL2(5) targets (9,9,12) and (9,10,11); only (10,10,10)
  survives that branch's finite dimension/source-cost screen. This supersedes
  the earlier list of three open shapes, without constructing the survivor.
- [`4abb9e4`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/4abb9e4)
  excludes injective triple sums of three four-point sets in F3^4, using
  affine dimension and an explicit Fourier-moment inequality. We read the
  argument, including its 1232>1088 contradiction. Its consequence concerns
  coordinate-potential constructions with such an abelian subgroup, not all
  tensor degenerations. The group search certificates were not replayed here.

These are other workers' written, unreviewed results. Reading an argument and
checking its displayed arithmetic is not independent formal verification.

**Scope correction for the constant-G graded task.** Our subsequent
[`arbitrary_shared_basis.md`](../research/ai/2026-10-20-koszul/arbitrary_shared_basis.md)
proves that the target catalecticant rank lower bound survives every constant
invertible shared GL(m) change. It closes the low-overhead constant-G ansatz
in `d2d505c`, not only the earlier G=I ansatz. The next search must permit a
singular shared map. This is a new written argument, not a replay or a claim
of failure of the other worker's optimizer implementation.

The same note now proves a nonsingular-block extension and two graded-weight
obstructions. The dominant-degree region alpha>(m-1)*abs(beta), including
our ten retained exploratory fits, is excluded. An X_0-slice support cover
also excludes 0<alpha<=beta at low overhead; at m=4 it needs B>=12 and
therefore rejects the worker's (1,1) and (1,2) runs at B=10. The (1,-1)
direction recorded in `0108d62` remains outside these arguments. Its partial
residual is not an exact certificate. These are analytic scope updates, not
new numerical search claims.

The subsequent [intermediate-weight covers](../research/ai/2026-10-20-koszul/intermediate_weights.md)
give a sharper scope update for (1,-1), equivalently (2,1): at m=4 they
require B>=12k-3. Thus the replicated B=10k target is excluded for k>=2,
although the worker's single-copy fit remains outside this exclusion.
The all-dimension normalized bound tends to one in this direction and does
not close the growing-family premise. The new tests independently check the
support covers and small bipartite matchings; they are not exponent evidence.
