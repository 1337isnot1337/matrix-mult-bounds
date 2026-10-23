# Paired-repair validation checkpoints

These receipts separate complete frozen-checkpoint runs from later integration
checks. Every accepted run has a complete unittest result and no skipped tests.

## Accepted coverage

| Checkpoint | Scope | Result |
| --- | --- | --- |
| `53fed21130a5c46a9c2336a8d196ea0547c2cbfb` | Ordinary maps and nineteen scalar repairs | 871 tests in 204 modules; all five archive replays |
| `b6c38513b33c4de2b1ddee4b22525adb74dbc291` | Polynomial border repair and exact ordinary core rank seven | 884 tests in 206 modules; all five archive replays |
| `aeafc7b944425f2f8d0118ea6cf7f520724eb251` | Full-residual rank proof, long-map frontier and main integration | 63 incremental tests; no failures, errors or skips |
| `2c1e026b5f1a0d86b3515f558b26cf39b667d65f` | Equalizer border-rank lower bound twelve | 35 incremental tests; no failures, errors or skips |

The [ordinary receipt](ordinary-checkpoint/validation.json) and
[border receipt](border-checkpoint/validation.json) record each disjoint group,
all test identifiers, Python and SymPy versions, compressed logs and hashes.
The archive summaries record equality of all five saved exact payloads.

The [integration receipt](integration.json) concerns the tree after merging
main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93` and the two focused follow-ups.
It includes all nineteen added tests: seven full-residual rank tests, seven
long-map frontier tests and five incoming resolvent tests. It also reruns
twenty-six related construction tests and eighteen repository checks.

All 728 Python files from the 884-test checkpoint remain byte-identical.
Only six Python files were added, and they match their source commits.
The combined discovery inventory is 903 tests in 209 modules. This inventory
is not a fresh execution of all 903 tests. Both archives are unchanged
against the full-suite checkpoint and its original main baseline `fe602e4`.
All claim objects from both mathematical branches and incoming main were
retained at integration.

The later [equalizer receipt](equalizer-followup.json) records seven new
tests, seven existing full-residual tests, eighteen repository checks and
three archive-integrity checks. Its standalone standard-library certificate
replay also passed. This follow-up adds only two Python files; all 734
previous Python files remain byte-identical. The combined inventory is now
910 tests in 210 modules, without a fresh full-suite execution. Its new
lower-bound claim and the forward-facing ordinary-rank cross-reference
update the border interval to twelve through eighteen. Pinned historical
proofs and certificates retain their earlier, weaker interval.

## Reproduction

Use the repository's supported environment, with Python optimization disabled.
The completed local runs used Python 3.12.14, SymPy 1.14.0 and thread limits
`OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`.

At the indicated frozen commit, run the complete suite and archive replay:

```sh
python -m unittest discover -s tests -v
python tools/replay.py
```

The four-way execution uses `tools/test_shard.py --shard-index I --shard-count 4`
for each `I=0,1,2,3`. Each receipt retains its complete, disjoint test inventory.
The exact incremental command and test identifiers are in `integration.json`
and its compressed discovery record.

## Excluded attempts

The border checkpoint retains two initial diagnostic group runs that ended
with exit code 139 and no complete unittest footer. Their cause is unknown.
Fresh complete runs without periodic stack dumping passed the entire groups.
The incomplete attempts contribute no accepted test coverage.

An initial integration run reported 63 successful tests, but its persisted
log stopped before the final result. That discrepancy is retained with cause
unknown and contributes no accepted coverage. A fresh 63-test run wrote its
complete in-memory log after execution; its saved bytes, hash and final footer
agree. The integration receipt identifies the accepted and excluded records.

## Limits

Current-head hosted CI remains the merge gate. Local test success and
coordinated proof checks do not establish independent mathematical review.
These receipts do not change the claims' written-and-unreviewed status or
establish an improved matrix multiplication exponent.
