# Publication and validation record

The replacement is [pull request #214](https://github.com/1337isnot1337/matrix-mult-bounds/pull/214).

The earlier publication baseline incorporated 147 captured source snapshots from
132 topic branch names. The eight-head catch-up extends this to 155 captured
source snapshots and 607 claim records; the topic-name count remains 132.
The sections below retain the earlier audit and test results at their exact
revisions. The new source decisions are in [postvalidation_source_resolution.json](postvalidation_source_resolution.json)
and the ledger decisions are in [claim_postvalidation.json](claim_postvalidation.json). The starting main commit is
`bd03b9dadba03b1089595f03ff7a091ee9e7ddbc`. The exact source heads and recovery tags
are recorded in [branches.json](branches.json). The 102 open source pull requests
at the last complete inventory, including their original bodies and draft flags,
are preserved in [source-prs-before-retirement.json](source-prs-before-retirement.json).
That inventory contained 61 draft and 41 ready pull requests.

## Final closure capture and tested coverage

Four additional source heads advanced during source retirement. Their exact
histories and recovery tags bring the manifest to 159 captured snapshots from
the same 132 topic names. The ledger remains unchanged at 607 records. The
[closure source decisions](closure_source_resolution.json) retain all executable,
test, workflow and dependency inputs at the passing eight-head revision. The
authored changes clarify Laurent degrees and historical A9 gate scope; the
unbalanced package manifest updates only the corrected README digest.

The [eight-head focused receipt](validation/postvalidation-summary.json) records
33 passing unit tests plus the standalone quadratic verifier on
`8a53354c23921b552703239aa1fdc62155a608fd`, with no skips, failures, errors or
tracked changes. The [coverage receipt](validation/postvalidation-coverage.json)
lists 1,933 tests across 432 modules. It records ten additions, no removals, and
passing coverage of every addition. The prior 1,923-test composite and the new
focused run cover that inventory. This is revision-aware composite evidence,
not an uninterrupted rerun of the complete final suite. All 23 checked archive
files and earlier validation receipts remained unchanged.

## Preservation of the publication baseline

The [preservation audit](preservation_report.json) passed with zero errors on
`901a6b61f2525d124485e925c74c18098faf7100`. It checked all 148 distinct captured
heads, including original main, as ancestors; all 147 verified archive tag
receipts; all 18 historical archive files in exact bytes and mode; and the
representation of 2,168 source-added paths and 2,210 original blob variants.

All 39 provisional conflict paths have explicit decisions in the
[central resolution manifest](central_resolution_manifest.json), with 300 final
output hashes checked. The baseline claim ledger contains all 599 original unique claim
identifiers and five aliases distinguishing independent collisions, for 604
records. Evidence and review flags retain their source values. All 54 reference
registry identifiers remain present.

This audit establishes preservation and traceability. It does not establish
independent mathematical review or a smaller matrix-multiplication exponent.

## Local test evidence before the eight-head catch-up

The [full baseline receipt](validation/baseline-summary.json) records 1,916 unique
tests across 429 modules on `caf51fe67bed960cbe827d81174f914aeff6968c`, using
Python 3.12.14. The four shards completed without skips. There were 1,914 passes
and two failures: the asymmetric-boundary and conic-second-jets source-pin tests
still expected the old root requirements file before NumPy was added.

The [pin repair](requirements-pin-repair.json) refreshes eight maintained JSON
metadata files, including downstream manifest hashes, while retaining all 77
strict hash checks and the original metadata copies. It changes no mathematical
implementation, proof, witness, claim, or test bytes.

The [focused final receipt](validation/focused-summary.json) records 29 passing
tests on `e2baf1170cd1e6ce676fad00d4a4b3746148a3a4`: both repaired checks, their
downstream pin checks, all 14 aggregation and quadratic-z tests, and 11 repository
and historical-archive checks. That inventory contains 1,923 tests across
430 modules; all seven additions are included in the focused run.

All five historical experiments replayed successfully. Both validation trees
remained unchanged during their runs, and the historical archive hashes matched
before and after. The longest full-suite shard took 1,062.598 seconds.

These are a full baseline run and focused final reruns, with exact revision and
test-ID receipts. They are not one uninterrupted full-suite pass at the final
publication head. The [publication comparison](publication_equivalence.json)
records that the later receipt merges changed only documentation, provenance,
and historical Laurent validation receipts. Packaging of that publication baseline added audit and validation metadata only.
The eight-head catch-up includes additional proofs, acceptance code, tests and
scoped claim updates; it requires its separately recorded frozen-head checks.

The auxiliary Lean build was not run locally. The required hosted `CI` check
retains the complete Python 3.10 and 3.14 test matrix, archive replay on Python
3.13, and the finite scalar-profile Lean build. Main is updated only after the
repository's current-base, CI, and discussion gates pass.

## Retirement and recovery

The replacement pull request supersedes only source pull requests whose live
head is an exact incorporated version. Branch deletion additionally requires
the matching archive tag, source ancestry in the replacement, no open head or
base dependency, and an explicit exact-SHA deletion lease. New, advanced,
protected, or foreign refs are retained.

All original snapshots remain recoverable through their recorded archive tags.
A separate `archive/consolidation-20261023-165523/integrated/` tag preserves the
complete consolidated merge history when the replacement is squash-merged.
Source pull requests are closed as superseded; they are not reported as
individually merged. Retirement outcomes are recorded separately after the
remote operations complete.
