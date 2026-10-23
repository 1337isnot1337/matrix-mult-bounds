# Publication and validation record

The replacement is [pull request #214](https://github.com/1337isnot1337/matrix-mult-bounds/pull/214).
It consolidates **136 topic branch names, 164 captured topic-source snapshots,
and 612 claim records**. The [branch manifest](branches.json) preserves exact
source heads, archive tags, original PR bodies, and draft states. Every captured
source history is an ancestor of the replacement. Original main was
`bd03b9dadba03b1089595f03ff7a091ee9e7ddbc`.

The concurrent integration correction at
`5d1441090e1c3c804d0ba0797a20ec303b5c08d5` is separately archived and incorporated
through a real merge. It is **not counted as another topic-source snapshot**.
The final merge to main remains subject to current hosted CI and discussion
gates. Consolidation and passing checks do not promote mathematical review or
establish an exponent improvement.

## Current content and preservation

The [preservation audit](preservation_report.json) records its exact audited
revision. It checks the original main plus all 164 topic heads, their verified
archive receipts, both historical research archives, every source-added path,
declared output hashes, all 39 conflict paths, claim provenance, and the 54
reference registry IDs. The [central resolution manifest](central_resolution_manifest.json)
records each deliberate reconciliation. Exact historical source variants remain
recoverable from their tags even when another version is selected for the active
tree. The [topic archive index](archive_verification_index.json) covers 164
snapshots; the [integration correction archive](integration_correction_archive.json)
has a separate receipt.

The [five-head continuation](NEXTWAVE.md) adds 40 package, proof, result and test
files with exact source bytes, plus five distinct unreviewed claims. Existing
executables, tests and dependencies were unchanged by those additions. Optional
discovery programs remain preserved and were not run as acceptance tests.

At tested commit `72f5c524fd72c894d4420067fd10206944bce405`, all 607 earlier claim
records were unchanged and five records were added. At corrected commit
`33a0f407b2071ed30433b2b1fbd8a577c50ea044`, **611 of those 612 records are unchanged**.
Only `AI-OBLIQUE-PAIRED-REPAIR-001.statement` changes: every first map satisfies
the residual-rank lower bound, and the supplied first map attains equality.
The [correction review](concurrent_oblique_claim_review.json) matches the unchanged
proof. All 612 evidence locations, status flags and other fields remain unchanged.
The [claim report](claim_resolution.json) retains every original source hash and
the exact before/after record. This narrow scope review does not change the
claim's written-unreviewed mathematical status.

The exact original concurrent audit files remain under `.5d144109.json` names.
The frozen next-wave [audit](preservation_report.72f5c524.json),
[manifest](central_resolution_manifest.nextwave-72f5c524.json), and
[claim report](claim_resolution.nextwave-72f5c524.json) retain their original
uncorrected checkpoint. The corrected content gate has its own
[audit](preservation_report.33a0f407.json),
[manifest](central_resolution_manifest.33a0f407.json), and
[claim report](claim_resolution.33a0f407.json). Earlier evidence is preserved in
the [159-snapshot publication record](PUBLICATION.159-a764cf16.md).

## Local validation with exact revision scopes

| Revision | Execution | Result |
| --- | --- | --- |
| `caf51fe67bed960cbe827d81174f914aeff6968c` | Complete 1,916-test baseline in four disjoint shards | 1,914 passed; two stale requirements-pin checks failed; no skips or errors |
| `e2baf1170cd1e6ce676fad00d4a4b3746148a3a4` | 29 focused checks covering repaired pins, added packages and repository/archive checks | All passed; both previously failing checks passed |
| `8a53354c23921b552703239aa1fdc62155a608fd` | 33 focused tests plus a standalone quadratic verifier | All passed in 28.255 seconds |
| `9354de63ff9ebb9a0b738d9a8cc88805636fa64d` | Final unbalanced package pin and relative-link checks | Both passed in 2.225 seconds |
| `72f5c524fd72c894d4420067fd10206944bce405` | 28 focused checks: all 17 added tests plus 11 repository/archive checks | All passed in 79.250 seconds; no failures, errors or skips |
| `33a0f407b2071ed30433b2b1fbd8a577c50ea044` | Corrected claim-ledger status and relative-link checks | Both passed in 2.257 seconds; no failures, errors or skips |

The latest [execution receipt](validation/nextwave-summary.json) and
[additive coverage receipt](validation/nextwave-coverage_union.json) establish
**1,950 tests across 437 modules**, with 17 additions and no removals relative to
the earlier 1,933-test inventory. Every new test passed. This is revision-aware
composite coverage: the final complete suite was listed, not rerun as one
uninterrupted local execution. The A4 acceptance includes its complete coordinate
census; the optional discovery script was not executed.

The [publication checks](validation/nextwave-publication-summary.json) and
[equivalence receipt](validation/nextwave-publication-equivalence.json) transfer
that coverage to the corrected tree. They prove exact preservation of 1,321
active code/configuration paths, 438 test files, every proof, witness and
dependency, all 23 protected archive files, and 73 earlier evidence/harness
files. The sole ledger difference is the source-authored statement correction;
all status flags remain unchanged. No census or inventory rerun was needed.
All validation checkouts remained unchanged during execution. Subsequent
packaging changes only this consolidation evidence directory.

The [strict pin repair](requirements-pin-repair.json) retains exact original
metadata and all 77 source/manifest checks. The required hosted `CI` gate still
runs the full Python matrix, archive replay and finite scalar-profile Lean build.
Local composite evidence does not replace current-head hosted CI.

## Completed cleanup and final captured sources

The [completed cleanup summary](completed_cleanup_summary.json) records **127
source branches deleted and verified, and 100 source PRs closed as superseded**.
The first phase deleted 117 branches and closed 91 PRs; the published159 phase
deleted ten more branches and closed nine more PRs. Four already-absent source
names were not counted as deletions. Superseded PR closures are not described as
individual merges.

The [final source inventory](final_five_inventory.json) captured five unchanged
topic heads plus main and consolidation. Their [full PR records](final_five_source_prs.json)
preserve PR213 and PR217 as ready, PR215 and PR216 as draft, and all original
bodies. No PR used one of the five topics as its base. The paired-rank-two topic
had no PR at capture. Publication and retirement of these five topics are
subsequent remote actions and are not claimed by this package.

Retirement requires the exact current source SHA, matching immutable archive,
source ancestry in the durable replacement, no open dependency and an explicit
deletion lease. A concurrent source push keeps the newer branch available.
Integrated-history tags preserve the full consolidation history even if the
eventual main merge is a squash.
