# Branch consolidation

This maintenance branch gathers the work from 132 topic branch names. The initial
snapshot was taken at 2026-10-23 16:55:23 UTC. A subsequent pass incorporated thirty
new or updated heads, including three additional topic branches. The starting main
commit was `bd03b9dadba03b1089595f03ff7a091ee9e7ddbc`.

The [branch manifest](branches.json) records the exact source heads, their original
pull requests, and the archive tags that preserve them. There are 129 initial
tagged heads and thirty tagged updates. Source histories are also ancestors of the
consolidation branch. Original pull request draft status is retained in the
manifest as provenance; consolidation does not establish mathematical review.

## Content decisions

The source packages, tests, result files, and source records are combined in the
working tree. Shared Markdown sections and JSON records are reconciled explicitly.
Earlier packages remain available with their stated scope and limitations.

The combined ledger has 607 records. Five additional identifiers distinguish
independent records that previously shared an identifier. The
[claim decisions](claim_resolution.json) preserve each source record, its evidence
status, and any identifier or evidence-path change. The two initial historical
research archives remain byte-for-byte unchanged.

The [documentation decisions](docs_resolution.json) and [catch-up decisions](docs_catchup_resolution.json) preserve corrections and distinguish historical checkpoints from current scope. The [README decisions](readme_resolution.json) record the combined navigation and scoped Lean statement.

The [code decisions](code_resolution.json) record separate paths for the independent
rank-six and oblique-atlas implementations. Their tests and certificates remain
with their implementations. The [source decisions](reference_resolution.json)
retain all imported source identifiers. The
[restored-path record](restored_paths.json) identifies files restored after Git's
directory-rename inference incorrectly moved or removed them.

## Validation and merge policy

The required `CI` check retains the complete Python test matrix and historical
archive replay. It also requires the imported finite scalar-profile Lean lemma to
build. The earlier proposal for selective tests is retained in this directory as
an inactive file. It does not change the active workflow or create a schedule.

Local test results are recorded with the tested revision and exact coverage.
Passing these checks does not change a claim's mathematical review status. Changes
to main still require the repository's pull request and CI gates.

The [publication record](PUBLICATION.md) links exact revision-scoped test and
preservation receipts. The final inventory has 1,933 tests across 432 modules;
composite local coverage and two final metadata checks passed. The full final
local suite was not rerun as one uninterrupted run. Hosted CI remains required.

## Original branch recovery

Every archived branch head has a tag in the branch manifest. Fetch that tag from
the origin and create a branch at it to recover the exact original state. The
archive tags preserve versions that were superseded during conflict resolution,
as well as the versions selected for the combined working tree.

Source branches are retired only when their current head matches the archived,
integrated head. A concurrent push invalidates the deletion lease and keeps the
new work available for a later integration.
