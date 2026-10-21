# Correction of sampled ridge-parameter histories

This is a correction of experiment metadata. It does not change any saved
tensor map, coefficient residual, norm, optimizer stopping point, or
mathematical status.

The ALS recorder in `q64_complete_flag_search.py` appended the mutable list
`ridges` directly to each history record. Subsequent mode updates changed
that same list. Consequently, the result written after the run repeated
the final three ridge parameters in earlier sampled records. The JSON
records printed during the run were serialized immediately and retained
the actual parameters at each sampled step.

The recorder now uses `ridges.copy()`. The historical values below were
restored from those original emitted records. No missing value was
inferred, and no optimizer was rerun to manufacture historical values.

## Exact reconstruction scope

All six published full-flag histories were compared against their
original emitted records, covering 161 retained snapshots. Every field
outside `ridge_parameters` agreed exactly.

| Published run | Retained snapshots | Corrected ridge snapshots |
|---|---:|---:|
| Refined, unrestricted | 2 | 0 |
| Lexicographic, unrestricted | 4 | 0 |
| Refined, norm bound 30 | 31 | 30 |
| Lexicographic, norm bound 30 | 31 | 30 |
| Lexicographic, parabolic gauge, norm bound 30 | 31 | 30 |
| Three-moment continuation | 62 | 0 |

Thus **90 sampled snapshots in three previously published artifacts**
were repaired. The two unrestricted runs predate ridge logging. The
moment optimizer does not use this ridge field. Their artifacts remain
byte-for-byte unchanged.

The two M1 moving-leading pilots also completed before this source fix.
Their histories contain 31 sampled snapshots each. Their 60 affected
ridge snapshots were restored before their first publication. These
two new artifacts are distinguished from the three corrected published
artifacts in the correction report.

At iteration zero the ridge list is `[null, null, null]`: no ALS mode
update has yet occurred. The final sampled ridge values already matched
the logs. The retained histories are sampled diagnostics, not a record
of every optimizer update. ALS snapshots occur every 50 iterations and
at the actual stopping point. The moment history uses its own recorded
acceptance schedule.

## Evidence and checks

`q64-ridge-emitted-records.json` preserves the parsed per-step stdout
records for all eight audited runs. Each group includes the filename and
SHA-256 identifier of the original complete stdout log. The stored
records are the audit input; the unretained summary text at the end of a
stdout log is not needed to restore the sampled ridge values.

`q64-ridge-metadata-correction.json` records before and after hashes for
the six published artifacts and the source change. It also records
canonical hashes of the map arrays and of the entire published payload
after removing only the ridge field and the added correction annotation.
Those canonical hashes agree before and after every correction. The
existing coefficient replay summary now refers to the three repaired
artifact hashes; its numerical results are unchanged.

The standard-library audit checks all 223 retained snapshots against the
stored stdout records, the artifact and map hashes, the unchanged
non-ridge published payloads, and the replay references:

```sh
python -S research/ai/2026-10-20-paired-direct-sums/q64_history_metadata_check.py
```

All experiments remain unsuccessful numerical searches. This metadata
correction establishes no new tensor restriction, degeneration, or
matrix multiplication exponent bound.
