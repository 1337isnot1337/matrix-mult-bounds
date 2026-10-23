# Final integration validation: 924 tests and historical replay

This receipt records the completed local gate for the exact frozen commit
`dabda4091b7ccc7f25cce5c7a5c001cf66a3241e`, tree
`7e1e9dc8a4a0ed8513e4dd14d29e194128c122d5`.

The snapshot merges PR136 commit
`f687963f4c69e58a3f39f651874b3b9b4c9f42fb` and PR129 commit
`0e43a999897eb8e003ed9ba7f7b0b9657a73c805` into the preceding integration
checkpoint `c3264dec240c25cacae62c48e58141fdd5cfb8bd`.
The five conflicts were additive coordination records. Resolution preserved
every nonduplicate section and the exact parent claim objects, giving 303
unique claim IDs. No pinned research file was changed to resolve a conflict.

## Completed gate

Python 3.12.14, SymPy 1.14.0, NumPy 2.3.5, and SciPy 1.17.0 were available.
`PYTHONPATH` was `/workspace/scratch/814d3d40fe43/mathdeps`; Python optimization
was disabled. Full commands and environment settings are in
[validation.json](validation.json).

| Shard index | Tests passed | Modules | unittest seconds | Skips |
| --- | ---: | ---: | ---: | ---: |
| 0 | 265 | 54 | 338.393 | 0 |
| 1 | 192 | 53 | 531.864 | 0 |
| 2 | 240 | 53 | 544.842 | 0 |
| 3 | 227 | 53 | 491.093 | 0 |
| Total | 924 | 213 | — | 0 |

All four shards passed with zero failures, errors, expected failures, or
unexpected successes. Discovery assigned every test and module exactly once;
[coverage.json](coverage.json) records all 924 test IDs. This is 28 tests more
than the preceding 896-test integration checkpoint. Elapsed wall time,
including coverage discovery and archive checks, was 552.356 seconds.

Each shard ran with:

```sh
python tools/test_shard.py --shard-index INDEX --shard-count 4
```

The complete original replay ran alongside the shards:

```sh
python tools/replay.py --output results/integration-2026-10-23-final/archive-replay
```

All five exact replay payloads matched the original records: 73,856 scalar
grid checks, 353,664 product-filtration inequalities, 12,976 binary candidates,
209,692 ternary candidates, and 20,000 seeded random candidates.

The 11 tracked files in `research/ai/2026-10-20/` and seven tracked files in
`research/ai/2026-10-20-session2/` remained byte-identical to commit
`fe602e418743f37a7cfa54d788b64aaf8a9d6095` before and after the run.
[archive-integrity.json](archive-integrity.json) records every file hash.
All test and replay logs are retained as gzip files; the receipt records
hashes of both compressed and uncompressed logs and every evidence artifact.

This is a local integration gate for the exact snapshot above. It does not
report hosted CI, external mathematical review, a formal proof build, a new
theorem, or an exponent improvement.
