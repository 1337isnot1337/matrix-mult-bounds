# Validation of the arbitrary A4 compression theorem

The substantive theorem checkpoint is local commit
`c5d279f5181a4b9b48c44e9fcefe55b628d1de51`, tree
`bd724a8d4b805a1d7334279289cb5aa181573e19`.
The [machine-readable receipt](../../../results/a4-compression-algebra-2026-10-23/validation.json)
records the exact commands, hashes, test identifiers and source manifests.

## Fresh checks on that checkpoint

The independent literal-source acceptance passed all 2,809 grade-budget
pairs, 24 rational minor identities, nine coupled blocks, and two exact
coefficient determinants. All eight new acceptance/rejection tests
passed. All 18 repository checks passed. The checkpoint commit and tree
remained unchanged during these checks.

Separately, canonical sparse serialization of the independently rebuilt
46-matrix basis agrees exactly with the prior block-reduction basis:

    fc5fa7fa18a82913d47e5aab768bef31e3990a6020a9e227a22c94162ba27525

Another agent in the generating session read the complete verifier and
replayed its acceptance. Root and that agent also read the mathematical
proof, including the torus limit and shared-flag argument. These are
same-session checks, not independent mathematical review.

## Retained baseline plus the new delta

This is not a fresh complete regression run. The retained
[full baseline receipt](../../../results/conjugation-limit-2026-10-23/validation.json)
covers 905 tests at tree
`363271b34a2b82dd033b388d7b48d00f1e76d1f9`. Its interrupted prefix and
three disjoint shards have exact union coverage. One Markdown-link
check initially failed on an untracked scratch draft; its correction
and successful retry are explicitly retained in that receipt. There
are no unresolved baseline failures.

The new collector rechecked every retained log/artifact hash and the
disjoint 905-test union. All 742 Python files present at that baseline
are byte-identical at the theorem checkpoint. The intervening
[block-reduction receipt](../../../results/conjugation-limit-2026-10-23/block-validation.json)
and [escape-family receipt](../../../results/conjugation-limit-2026-10-23/escape-validation.json)
cover their later additions; every file hash recorded by those receipts
still matches. The seven changed baseline non-Python files are the
documented metadata, prior package README, and prior source manifest.
The new 18-check repository run covers the updated metadata.

Current discovery contains 916 tests: the retained 905, the three
previously checked block-reduction tests, and the eight new tests.
The new focused tests and metadata checks were rerun on the frozen
checkpoint; prior tests are not counted again as fresh execution.

All five archived replays passed in the retained baseline. The collector
verified all 20 archive/replay inputs, including both archive trees,
the replay driver and maintained requirements, byte-for-byte. Those
replays were reused and were not rerun for this additive theorem package.
A fresh complete hosted CI run remains required before merge.

The [collection script](../../../results/a4-compression-algebra-2026-10-23/validation/collect.py)
and its three fresh logs are retained beside the receipt. Its fixed-tree
guard intentionally requires the substantive theorem checkpoint; later
documentation/receipt commits are not represented as that same tree.
