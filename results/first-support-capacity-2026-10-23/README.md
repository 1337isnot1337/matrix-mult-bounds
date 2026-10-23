# First-support capacity validation

All **871 tests across 204 modules** passed at the frozen research
checkpoint below, with no failures, errors or skips. All five archive
replays reproduced their saved exact payloads.

- Tested commit: `66c463682c899f3d6cffa5f5f438812bf0981fd4`.
- Tested tree: `931dfcffdf98fce09201d88569953457ebdd362c`.
- Python: 3.12.14. SymPy: 1.14.0.
- `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS`: `1`.
- Machine-readable record: [validation.json](validation.json).

## Complete test groups

The saved coverage lists are disjoint and together contain every test
identifier discovered at the tested commit. Each retained log has its
complete unittest result footer and a matching successful status record.

| Group | Tests passed | Unittest seconds | Log | Status |
|---|---:|---:|---|---|
| 0 | 214 | 405.497 | [Log](group-0.log.gz) | [Status](group-0-status.json.gz) |
| 1 | 206 | 399.780 | [Log](group-1.log.gz) | [Status](group-1-status.json.gz) |
| 2 | 224 | 412.227 | [Log](group-2.log.gz) | [Status](group-2-status.json.gz) |
| 3 | 227 | 282.780 | [Log](group-3.log.gz) | [Status](group-3-status.json.gz) |

The [coverage record](coverage.json.gz) retains all test identifiers,
the tested commit and tree, and the dependency versions. Compressed and
uncompressed evidence hashes are recorded in `validation.json`.

The repository shard runner reproduces each group, with `i` from zero
through three:

```sh
python tools/test_shard.py --shard-index i --shard-count 4
```

## Archive replay

The [replay summary](archive-replay.json) records five exact matches:
profile checks, product-filtration checks, binary search, ternary search
and random search. The [replay log](archive-replay.log.gz) is retained.
The replay checked ten archived source files and all five saved report
payloads. Both archive directories have an empty Git diff from
`fe602e418743f37a7cfa54d788b64aaf8a9d6095` to the tested checkpoint.

## Scope

This receipt records the completed suite at the stated commit. The
eighteen repository metadata checks were run again after packaging the
receipt and updating the status text; that smaller check is recorded in
[metadata-check.json](metadata-check.json). No Python file was changed
after the full regression. No newer main-branch changes were merged
during this receipt checkpoint.

The tests do not establish independent mathematical review or an
improved matrix multiplication exponent. The two new claims remain
`proof-written-unreviewed`. Hosted CI at the final commit is a separate
gate.
