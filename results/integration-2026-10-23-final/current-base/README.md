# Incremental validation on the updated topic heads

This is a separate incremental receipt for commit
`b1f2345829f4982d632f3eb58d4639171ca675a5`, tree
`5441a0c0ed7bf5bedad032844162ce281d1439bc`.

The snapshot merges these exact updated topic heads:

- PR129: `35ac38d72dc42327899da29b1af355e494545356`.
- PR136: `14c4da35f059b94d25402a7870d81e05ede307c1`.
- Both include main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.

The [preceding full receipt](../validation.json) records 924 passing tests,
zero skips, and all five exact historical replays on its identified frozen
snapshot. Its receipt commit is `844857b`. The updated snapshot changes only
five existing coordination files and adds the standalone resolvent package.
Every existing executable file and test module is unchanged; the complete
path comparison is in [changed-paths.json](changed-paths.json).

On the updated snapshot, all five new resolvent tests passed in 0.143 seconds.
All nine repository-metadata and archive-integrity checks passed in 0.076
seconds. There were zero skips, failures, or errors. Both protected archives
remain byte-identical to the prior run and reference commit `fe602e418`.

[coverage.json](coverage.json) records 929 discovered test IDs in 214 modules:
all 924 earlier IDs and exactly five new resolvent IDs. The complete 929-test
suite was not rerun. This receipt combines the prior full gate with the
authorized incremental checks; it does not claim a single full-suite run on
the updated snapshot. The claim ledger contains 304 unique IDs and equals
the exact object union of the two updated topic heads.

[validation.json](validation.json) records commands, times, component hashes,
the exact prior receipt hash, and compressed-log hashes. Later work in
PR155 and PR156 is outside both receipts. Hosted CI, external mathematical
review, formal verification, and exponent improvements are not claimed.
