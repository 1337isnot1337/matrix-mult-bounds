# External-seed continuation checkpoint

This is the October 23, 2026 continuation on
`research/flip-escape-20261023`, tracked by
[PR128](https://github.com/1337isnot1337/matrix-mult-bounds/pull/128).
The work started from main `1c04903` and integrated `fe602e4`.
The follow-up branch `research/gauged-batches-20261023` starts from
PR128's frozen head `a1a9b38`; its claims 008 and 009 are recorded below.
The external algorithm, source convention, and deletion viewpoint retain
the attribution and version pins in `sources.json`.

## Accepted exact witnesses and written implications

- The original rank-76 seed has a closed standard-flip component.
  Its 58 proportional-W classes remain isolated, and their scalar
  trace pairings prevent subset deletion by the physical stabilizer.
- Four and five simultaneous splits give explicit 76-term Laurent
  border seeds with 72 and 71 distinct U directions. Complete contraction
  checks all 10000 constant positions and every nonzero Laurent
  coefficient. The discarded terms share one contracting physical family.
- Weighted flat covers reject direct reuse of either seed in the
  specified termwise Q(6,4) evaluation-grid alignment.
- The later `2026-10-23-fixed-flip-components` package closes every
  finite standard-flip continuation of these two seeds for that grid.
  Each continuation retains 50 W directions requiring ten rank-four
  groups. The five-split component additionally has a positive trace
  obstruction to deleting any further nonempty subset, even allowing
  cancellation with the original discarded error.
- The broader `2026-10-23-gauged-splits` package gives six simultaneous
  deletions and a 76-term border seed with 70 U directions. Positive
  tensor valuations suffice even though two individual factor valuations
  are negative. Separate gauges after epsilon=t^3 make all discarded
  factors positive. A mixed trace equal to one proves that the prior
  common unscaled-arrow condition cannot accept this batch.
- The `2026-10-23-six-split-grid` package reconstructs its 52 isolated
  components and 47 permanent W directions. Those directions admit an
  explicit nine-group rational cover. Integer weights of total 144
  and flat cap 16 prove that nine is the minimum for the permanent subset.
- The `2026-10-23-six-split-mobile-obstruction` package enumerates all
  21649 possible saturated rational four-spaces in any nine-group cover.
  Their intersections with two mobile planes cannot span those planes.
  This closes the full specified termwise grid after finite standard
  flips or separate minimum-term refactorizations of the initial blocks.
- The `2026-10-23-large-gauged-batches` package gives ten and eleven
  simultaneous deletions with 66 and 65 distinct U directions. The
  eleven-split seed retains weight 214 against the prior U capacity 216.
  The ten-split seed has four exact cross-component span contacts. Neither
  property establishes a cross-component move or a grid map. Both full
  Laurent identities, including discarded errors, replay exactly.

These are written, unreviewed implications with finite exact input
certificates. Same-session audits are not independent mathematical
review. No smaller exponent, new rank record, complete target map,
maximum split-batch result, or general degeneration exclusion follows.

## Validation checkpoint

The earlier full regression in the source worktree completed 862 tests
in 1642.810 seconds, with three optional NumPy-dependent tests skipped.
All five archive replay jobs passed. PR128's integrated tree at `a1a9b38`
then passed 55 focused, research-metadata and archive-integrity tests,
including all five weighted-flat enumerations. The larger-batch follow-up
passed 32 focused, metadata and archive checks, including complete
saturated-flat enumeration. The full regression preceded the latest
packages; these counts are complementary checks, not a claim that all
862 tests ran at the final follow-up head. Hosted CI checks each submitted
head before merge. The protected archives are unchanged.

## Do not repeat

Unchanged random shared-factor walks of the original seed cannot leave
its certified component. Walks of the four-, five-, or six-split seed cannot
repair the specified termwise grid assignment. The five-split seed also
cannot yield further subset stabilizer deletion through those walks.
Tests that ignore the original positive Laurent remainder do not verify
a smaller border decomposition.

The discovery search's best five-split batch is an accepted witness,
not a proof that larger batches are impossible. Numerical LP objectives,
modular rejection filters, and bounded random searches are not acceptance
evidence by themselves.

## Next precise question

The answer to the first gauge-adjusted question is positive: the six-split
witness contracts six discarded terms under one physical transformation.
For term i, the sufficient valuation condition is

\[
\nu(U_i-U'_i)+\nu(V_i)+\nu(W_i)>0.
\]

The three minima may be redistributed by factor gauges with product one.
This is strictly more flexible than demanding that all unscaled arrows
raise one common descending image flag. The accepted larger batches now
leave two precise questions: whether their component flattening images
contain decomposable factors that permit actual cross-component changes,
and whether replacements on V or W permit useful new shared-factor flips.
The six-split full-cover question is closed in the continuation class
above, although its fixed-subset cover remains valid. Search candidate
bases and integer physical weights, and verify every successful rational
witness by full Laurent contraction. Screen the fixed W directions before
expensive flip searches. Other external decompositions remain open.

For any candidate, export the exact replacements, bases, weights and
factors. Check the complete tensor identity and source attribution, then
update the claim ledger and status together. A grid candidate also needs
simultaneous incidence conditions and actual source maps; passing one
weighted cover screen is insufficient.
