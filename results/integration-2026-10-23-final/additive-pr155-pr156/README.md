# Additive integration gate for frozen PR155 and PR156

This checkpoint passed **25 newly added tests** and **9 repository/archive checks**,
with zero skips, failures or errors, on commit `7cf5d0a04d6fed4fb99f4cba6077294ef3aba860`
(tree `d67869e10e83496ccbfd5d7789efb8c301cab765`). It discovers **954 tests in 218 modules**.
All 929 test IDs from the preceding checkpoint are retained, with exactly 25 additions.
This is an additive validation record; it does not claim a full 954-test run.

## Frozen components and merge scope

- Starting receipt commit: `3cd88ded9aa1990ab1647f9c4afc579f02b67362`.
- PR155: `72ef0788b6847af5e8105047c806c26c537c18ed`; staircase, strict-rank-37 and sharp-rank-80 source packages.
- PR156: `9e27c8d97dd6fd6fd29c4432e07619b48cd71953`; prescribed-third-jet obstruction and exceptional exact curves.
- First merge: `4abd5e33ec7d553d056194805b73fd4ea2a6e8d7`; the second merge is the tested commit above.

Only five coordination metadata files changed relative to the previously validated
snapshot `b1f2345829f4982d632f3eb58d4639171ca675a5`. Every existing executable and test file remains byte
unchanged. The four new test modules contain 18 source-space tests and 7 conic tests.
The new research/result files match their frozen component commits byte for byte.
All 308 claim objects are unique and equal the exact union of the three parent ledgers.
Additive conflict resolution preserved all nonduplicate sections and claim lines;
no frozen research proof or verifier was changed.

## Evidence reused without rerunning unchanged tests

The [full baseline](../validation.json) records 924 passing tests in four shards
and five complete historical archive replays on
`dabda4091b7ccc7f25cce5c7a5c001cf66a3241e`. The
[current-base increment](../current-base/validation.json) records five added
resolvent tests plus nine metadata/archive checks on `b1f2345829f4982d632f3eb58d4639171ca675a5`,
bringing discovered coverage to 929. Both prior receipts and every artifact hash
were rechecked before this additive gate. Their original timing and scope remain
unchanged. The current checkpoint adds the 25 tests listed in `coverage.json`.

## Exact artifacts and limits

`validation.json` records commands, runtime, times, component SHAs, and hashes.
The two `.log.gz` files preserve the complete raw unittest streams losslessly;
both compressed and uncompressed hashes are recorded. `coverage.json` lists every
test ID. `changed-paths.json`, `frozen-components.json`, and `claim-union.json`
record the additive scope. `archive-integrity.json` compares all 18 protected
files directly with `fe602e418743f37a7cfa54d788b64aaf8a9d6095` before and after testing.

The ongoing every-pair-rank and projective conic criterion packages are excluded.
This receipt is an internal integration check, not hosted CI, independent external
mathematical review, formalization, or an exponent improvement. Research claims
retain their written-unreviewed status.
