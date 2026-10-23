# One-slice seed audit: complete local regression

The full regression was run on the frozen commit
`42360e9816d5755a07a6da6fa607b92865a0be6b`, tree
`6dbaa9335ef6603fce09dbf07dda6c98ad1561b8`.
All **864 tests in 203 modules** completed successfully, with zero
failures, errors or skips. All five archive replays matched their saved
exact payloads. The two archived research directories are unchanged.

The [validation receipt](validation.json) includes hashes of the compressed
logs and their uncompressed contents. The [coverage manifest](coverage.json.gz)
lists every test ID and demonstrates disjoint, complete group coverage.

| Accepted group | Tests | Retained log |
|---|---:|---|
| 0, original complete run | 229 | [group-0.log.gz](group-0.log.gz) |
| 1, complete retry without asynchronous stack dumping | 206 | [group-1.log.gz](group-1.log.gz) |
| 2, complete fresh rerun | 239 | [group-2.log.gz](group-2.log.gz) |
| 3, original complete run | 190 | [group-3.log.gz](group-3.log.gz) |

Each accepted log has its complete unittest footer and `OK` result.
Complete result/status records are retained separately. The coordinating
parent also observed tool exit zero for the final group-one retry.

## Incomplete attempts retained and excluded

The original group-one and group-two commands each exited zero but
produced no complete unittest footer. A group-one diagnostic retry with
asynchronous stack dumping exited 139 and also lacked a complete result.
Their logs, last saved status records, and the diagnostic stack output
are retained. Their causes are unknown, and none contributes to the
864-test total. The stack-dumping option is an observed configuration,
not a diagnosis of the exit cause. The original aggregate run summary
is retained with its unsuccessful status.

No test or verification code was changed to obtain the completed reruns.
This record concerns exactly the frozen commit above. A later main
integration and its incremental checks have their own receipt and are
not represented as another full-suite run.

The complete commands use Python 3.12.14 and SymPy 1.14.0 with the
thread limits recorded in the receipt:

```sh
python tools/test_shard.py --shard-index 0 --shard-count 4
python tools/test_shard.py --shard-index 1 --shard-count 4
python tools/test_shard.py --shard-index 2 --shard-count 4
python tools/test_shard.py --shard-index 3 --shard-count 4
python tools/replay.py
```

This is execution evidence, not independent mathematical review or an
exponent improvement. Current-head hosted CI remains a separate gate.
