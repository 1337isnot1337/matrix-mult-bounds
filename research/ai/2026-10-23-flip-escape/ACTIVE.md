# External-seed continuation checkpoint

This is the October 23, 2026 continuation on
`research/flip-escape-20261023`, tracked by
[PR128](https://github.com/1337isnot1337/matrix-mult-bounds/pull/128).
The work started from main `1c04903` and integrated `fe602e4`.
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

These are written, unreviewed implications with finite exact input
certificates. Same-session audits are not independent mathematical
review. No smaller exponent, new rank record, complete target map,
maximum split-batch result, or general degeneration exclusion follows.

## Do not repeat

Unchanged random shared-factor walks of the original seed cannot leave
its certified component. Walks of either accepted split seed cannot
repair the specified termwise grid assignment. The five-split seed also
cannot yield further subset stabilizer deletion through those walks.
Tests that ignore the original positive Laurent remainder do not verify
a smaller border decomposition.

The discovery search's best five-split batch is an accepted witness,
not a proof that larger batches are impossible. Numerical LP objectives,
modular rejection filters, and bounded random searches are not acceptance
evidence by themselves.

## Next precise question

Can a common physical transformation delete more useful terms when
separate factor gauges are allowed for each discarded tensor? For term i,
the sufficient valuation condition is

\[
\nu(U_i-U'_i)+\nu(V_i)+\nu(W_i)>0.
\]

The three minima may be redistributed by factor gauges with product one.
This is more flexible than demanding that all unscaled arrows raise one
common descending image flag. Search candidate bases and integer physical
weights, and verify any successful rational witness by full Laurent
contraction. Larger sets of changed W components should be screened
before expensive flip searches. Other split legs and other external
decompositions are additional open routes.

For any candidate, export the exact replacements, bases, weights and
factors. Check the complete tensor identity and source attribution, then
update the claim ledger and status together. A grid candidate also needs
simultaneous incidence conditions and actual source maps; passing one
weighted cover screen is insufficient.
