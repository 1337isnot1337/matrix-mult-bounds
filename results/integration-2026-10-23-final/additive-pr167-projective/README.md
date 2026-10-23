# Additive integration gate for frozen PR167 and the projective criterion

This checkpoint passed **26 newly added tests** and **9 repository/archive checks**,
with zero skips, failures or errors, on commit `19187753696e3f9d86daffdf78c01a168a1cf3b5`
(tree `ee47ff0a53cb2ea186bcd47ecc6187f0a4fc465d`). It discovers **980 tests in 222 modules**.
All 954 test IDs from the preceding checkpoint are retained, with exactly 26 additions.
This is an additive validation record; it does not claim a full 980-test run.

## Frozen components and merge scope

- Starting receipt commit: `03538eab2f573f72ef8283b24741c785ce86c9ee`.
- PR167: `16a13196c3ac501e9e80adfdb7dade0041fc6a36`; all-pair 144, sharp source caps at 84/88, and all-pair 136.
- Projective criterion: `a7d37918fe19918700a3d5c5d9fad6df69cc7852`; complete conic normal-class existence.
- First merge: `a59b0ae18fda1ee61c537a1ae2f4efc17d99f493`; the second merge is the tested commit above.

Only five coordination metadata files changed relative to the previously validated
snapshot `7cf5d0a04d6fed4fb99f4cba6077294ef3aba860`. Every existing executable, test, proof, operator,
and research result remains byte unchanged. The four new test modules contain
19 rank-package tests and seven projective tests. All 45 new research,
result and test files match their frozen component commits byte for byte.

The ledger contains all 313 unique claim IDs from the exact parent union. One
incoming parent updates only the limitations field of the earlier affine conic
criterion to identify it as the prerequisite of the separate projective theorem.
`claim-union.json` preserves the old and new text; every other claim field matches
its parent object. The affine scope and prescribed-jet limits are retained.
Conflict resolution also reconciles outdated open-chart coordination notes with
the new completed chart theorem. No frozen research file was changed.

## Evidence reused without rerunning unchanged tests

The [full baseline](../validation.json) records 924 passing tests in four shards
and five complete historical archive replays on `dabda4091b7ccc7f25cce5c7a5c001cf66a3241e`.
The [current-base increment](../current-base/validation.json) adds five resolvent
tests and nine repository/archive checks on `b1f2345829f4982d632f3eb58d4639171ca675a5`.
The [preceding additive increment](../additive-pr155-pr156/validation.json) adds
25 tests and nine repository/archive checks on `7cf5d0a04d6fed4fb99f4cba6077294ef3aba860`, bringing
discovered coverage to 954. All three prior receipts and every artifact hash were
rechecked. Their timing and scope remain unchanged. This gate adds only the 26
tests listed in `coverage.json` and reruns the nine repository/archive checks.

## Exact artifacts and limits

`validation.json` records commands, runtime, times, component SHAs, and hashes.
The two `.log.gz` files preserve complete raw unittest streams losslessly;
both compressed and uncompressed hashes are recorded. `coverage.json` lists every
test ID. `changed-paths.json`, `frozen-components.json`, and `claim-union.json`
record the additive scope. `archive-integrity.json` compares all 18 protected
files directly with `fe602e418743f37a7cfa54d788b64aaf8a9d6095` before and after testing.

The ongoing rank-92/rank-96 source package and any later target consequences are
excluded. This receipt is an internal integration check, not hosted CI, independent
external mathematical review, formalization, or an exponent improvement. Research
claims retain their written-unreviewed status.
