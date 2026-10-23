# Complete validation coverage for the construction checkpoint

All 908 tests discovered at construction commit
`f802c00d04c3f64c7436b4c9d4da67b81a1834b8`, tree
`ca5f7ce98a9f306e71bb5f0270cfd5b39581a695`, passed with the exact combined
coverage recorded in [combined_report.json](combined_report.json).
This is combined coverage across the recorded runs, not one uninterrupted
run on a frozen final tree.

| Evidence component | Cases counted |
| --- | ---: |
| Completed unchanged baseline prefix | 448 |
| Final aggregation focused module | 11 |
| Remaining baseline shard 0 | 225 |
| Remaining baseline shard 1 | 224 |
| Exact union | 908 |

The original monolithic run completed 454 cases before it was deliberately
interrupted with exit code 130. Its six older aggregation cases are
excluded from the union and replaced by the final eleven-case module.
The one unfinished case is included in the remaining shards. Two completed
prefix cases printed progress between their test headers and unittest's
final `ok`; their complete success blocks are preserved and identified in
the receipt.

All 209 other test files and all 743 baseline implementation/test sources
are identical Git objects to the launch state. The full tracked-file
comparison appears in [plan.json](plan.json). Outside the aggregation
package and its test module, only `STATUS.md`, `PROVENANCE.md`, and the
claim ledger changed. The ledger's reader passed in a remaining shard on
the frozen construction checkpoint.

Each shard checked its discovered identifiers, assigned case set, clean
worktree, HEAD, and tree before and after execution. The receipt verifies
that its four counted case sets are pairwise disjoint and their union is
exactly the complete discovered suite. There were no failures, errors,
or skipped cases. All five archived replay reports also passed.

The complete prefix, focused, shard, and replay logs are retained here,
along with the exact harness, plan, outcomes, and SHA256 values. The
harness records this particular continuation and deliberately requires
its pinned checkpoint. To run the whole suite anew, use the standard
repository command `python -m unittest discover -s tests -v`.

These checks establish the recorded computational coverage. They do not
change the mathematical claims' written-and-unreviewed status.
