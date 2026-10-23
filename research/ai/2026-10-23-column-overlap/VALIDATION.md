# Validation of the column-overlap checkpoint

The mathematical checkpoint is local commit
`b0ccaa3fbacf86f9a330cd8bb25149fd748ad36e`, tree
`bd8908108844b3ea4e212204bbed15d54668d89a`. Its published equivalent is
`f8fdcd314d7a0740ebc36e70e76b348b8fa33935` in PR 215.

The [machine-readable receipt](../../../results/column-overlap-2026-10-23/validation/report.json)
records an exact union of passing evidence for all **903** tests in this
tree. This is retained baseline coverage plus fresh affected checks.
It is not a fresh complete regression run.

## Fresh acceptance

All six column-overlap tests pass. They replay the complete exact report,
check the full-channel sharpness example, test disconnected components
and the necessary saturation allowance, and reject a damaged integer map.
The source pins and written, unreviewed claim status also pass.

A separate invocation of the standard-library verifier reproduces the
retained report byte-for-byte. It covers seven complete cases, 4,277
target coefficient positions, and 23,722 source-slice coefficient
positions across the two specified exact evaluations. The formal controls
also expand the Laurent coefficients and check complete pole cancellation.
These finite checks support the proof; they do not replace its all-size
argument or establish an improved exponent.

All 18 shared repository, profile, and support tests pass on this checkpoint.
The exact
[focused log](../../../results/column-overlap-2026-10-23/validation/focused.log)
and [metadata log](../../../results/column-overlap-2026-10-23/validation/metadata.log)
are retained. A final link-only check covers this validation note and its
README pointer after they were added.

## Retained baseline and exact coverage

The earlier A4 checkpoint `6db05f5592b2f252ebc718cfececd5625a44aed5`, tree
`363271b34a2b82dd033b388d7b48d00f1e76d1f9`, has a retained complete
905-test evidence union. Its [immutable receipt](https://github.com/1337isnot1337/matrix-mult-bounds/blob/798cf02ffc87e59c7b33dab9866b7b777779e733/results/conjugation-limit-2026-10-23/validation.json)
was added after those checks. The fetched receipt matches the retained
local bytes exactly. Its raw test logs, machine-readable shard results,
inventory, and replay log all match their recorded SHA-256 hashes.

That baseline contains the same 897 main tests and eight A4-specific
tests absent from this branch. The eight A4 tests are excluded. The 18
shared repository, profile, and support tests are replaced with their fresh
results. The remaining 879 unchanged tests have passing entries in the
retained raw logs, including three tests whose progress messages split the
test header from its final `ok`. The raw-log results agree with the saved
shard results.

The current evidence is therefore a disjoint union:

| Evidence | Unique test IDs |
| --- | ---: |
| Unchanged baseline tests with retained passing logs | 879 |
| Fresh repository, profile, and support checks | 18 |
| Fresh column-overlap tests | 6 |
| Complete current inventory | **903** |

The [coverage record](../../../results/column-overlap-2026-10-23/validation/coverage.json)
lists every contributing ID and the eight excluded A4 IDs. There are no
missing IDs or overlaps among the three contributing parts. Repeated
focused checks and the final link check do not increase the count.

## Byte identity and historical replays

The [source audit](../../../results/column-overlap-2026-10-23/validation/source-identity.json)
compares main `bd03b9d`, the tested A4 baseline, and this checkpoint.
All 739 original Python files and all 209 original test modules have
identical Git blob identities. The same holds for 2,972 common files
after excluding five shared documentation/claim paths. This branch
changes four of those paths; the older baseline also changed the
research-directions document. Fresh metadata tests cover the current
documentation and ledger.

Both protected archive trees, the dependency file, the replay runner,
and the sharding runner are unchanged. The prior receipt records all
five historical experiments passing. Those expensive replays were not
repeated for this additive package. Current-head hosted `CI` remains a
separate merge requirement.

## Corrections and limits

The historical baseline initially failed one Markdown-link check because
an untracked scratch draft had invalid relative links. Its receipt retains
that failure and the successful correction. This branch's fresh link test
passes.

During development of the new verifier, the wrong-sign rejection guard
also ran on a positive control whose residual was zero. The guard was
restricted to nonzero residuals before the accepted checkpoint. No
mathematical map or theorem changed. All final controls and the damaged-map
test pass.

The proof, verifier, source pins, witness report, and focused test module
were unchanged during these checks. This receipt records same-session
validation. It does not change the claim to independently reviewed or
formalized, and it does not claim a smaller matrix multiplication exponent.
