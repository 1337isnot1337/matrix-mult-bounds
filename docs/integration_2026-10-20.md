# Main integration checkpoint

The owner requested frequent integration into main and cleanup of completed
branches and pull requests. This checkpoint combines these immutable heads:

| Lane | Included head | Main content |
| --- | --- | --- |
| Scalar and filtration compatibility | `0f56494` | Concavity equivalence, endpoint rigidity, conditional fat-point route, exact restriction barrier, SL(2,7) source cost and central quotient lemma |
| Koszul and source constructions | `8e0a766` | All-degree target certificates, source obstructions, constant-shared-basis argument |
| Product filtration and recoupling | `20734a9` | Affine direct sums, full recoupling blocks, scalar subrank certificates, mixed-coordinate capacity bound |
| Entropy and group potentials | `6afff6c` | Exact entropy duals, group source/frontier certificates, rank-locus and finite-field obstructions, normalized searches |

The product lane was also merged through PR 2 at `93f8f8a` while this
integration was being checked. That main commit is included as an ancestor.
Overlapping fixed-label and rigidity arguments retain their attribution and
are not counted as separate independent discoveries or reviews. Historical
experiment counts and validation receipts remain tied to their original runs.

Validation on the combined source tree passed 160 unit tests under Python
3.14.8 and SymPy 1.14.0. All five original experiments replayed with matching
exact payloads; all ten manifest hashes passed before and after. Both dated
historical research directories are byte-for-byte unchanged from `e0d7ed5`.
The latest 30 finite-group reports were additionally replayed after import.
Their sparse integer cuts are checked; solver UNSAT statements have no checked
proof traces. Receipts are in `results/integration-2026-10-20/`.

These checks do not constitute independent mathematical review, a Lean build,
or an exponent improvement. The stated conditional exponents still lack their
required tensor constructions. The bound below 9/4 remains the active goal.

Active worker branches remain available for ongoing research. A branch should
be removed only when its work is included and it is no longer an active worker
checkout or publication target. Pull requests whose heads are included in
main can be closed as merged; unmerged work must be preserved. The temporary
integration branch itself does not need a remote branch or pull request.

## Quantitative capacity follow-up

The capacity branch integrates main `a83bc24` into its exact checkpoint
`e1ec7b1`, preserving all 39 claim records. The historical filtration entry
retains main's attribution to both overlapping all-size arguments. The
status additions are combined, with no archived research changes. All 164
combined tests pass locally under the pinned SymPy 1.14.0 environment; the
log is `results/mixed-restrictions-2026-10-20/combined-tests-164.txt`.

The new written, unreviewed asymptotic coordinate-input capacity bound is
`3/2-sqrt(3)/4`; it is not a smaller matrix exponent. Its claim ID is
AI-MIXED-ASYM-CAPACITY-001 and its exact scope is recorded in the linked
mixed-restrictions package. The next construction still requires singular,
nondiagonal shared behavior beyond the closed coordinate-input family.

The central-projection follow-up integrates `a0b602f` with the current PR
workflow. It passes all 170 combined tests in the existing Python 3.14.8
environment containing only the maintained SymPy/mpmath dependencies and
replays all 1,394 parity circuits without optional search packages. These
receipts are `central-projection-tests.txt` and `central-projection-replay.json`
under the integration results directory. This finite search reduction adds
no tensor witness or exponent improvement.

## Follow-up graded-obstruction integration

The Koszul worker then integrated main at `a83bc24` with its newer proof
checkpoint `635bf48` and PR #1 head `3898d54`. This adds the nonsingular-block
extension and the two graded-weight-region obstructions. All 162 tests pass
on the combined tree; the only merge conflicts were in `STATUS.md` and
`docs/research_directions.md`, and both source packages' conclusions and
attributions were retained. The historical archive bytes remain unchanged.
The full baseline replay also passed on the Koszul source before integration;
the prior four-lane replay receipt above remains intact. Exact receipts for
the update are `graded-update-tests.txt` and `graded-update-summary.json` in
the same results directory. No theorem status or exponent was promoted.

The next update integrates protected-workflow main `6cfa5a9` and the latest
source-obstruction work. All 169 combined tests pass; the distinct report is
`results/mixed-restrictions-2026-10-20/combined-tests-169.txt`. Both historical
archives remain unchanged. The capacity PR follows the newly required CI
and squash-merge policy; no rule bypass or direct main push is used.

The capacity branch subsequently integrates main `424dd92` and its exact
projected-group/central-lift certificates. All 174 combined tests pass in
`results/mixed-restrictions-2026-10-20/combined-tests-after-424dd92.txt`.
All 40 claim records are preserved. The capacity claim is placed beside its
related earlier claim, avoiding a collision with future appended group
records. No proof status changes and neither archive changes.
