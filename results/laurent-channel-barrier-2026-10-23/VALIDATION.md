# Validation of the Laurent channel barrier

The frozen proof checkpoint passes all 904 discovered tests and all five
archive replays. The tested full Git tree is
`799c5b8e07213790aa75db598a5bda0ee448fdcf`.

The local commit `13dfd91537a99ca9e0315e9181badc50d8cfd98d` and published
commit `b6cddb16c3ea03515d1708d6f651d14f8bb6994f` have that same tree.
Their commit identifiers differ because publication used different commit
metadata. The tracked tree did not change during validation.

The sequential regression process was deliberately interrupted with exit
code 130 after 547 completed successes. Only the 357 uncompleted test IDs
were resumed, in two module-grouped shards of 179 and 178 tests. Both
shards passed with exit code zero. Their exact, disjoint union with the
completed prefix equals all 904 discovered test IDs. No completed test
was repeated, and no test was skipped. This was not one uninterrupted
regression process.

Two successful prefix tests printed diagnostic output between their test
header and the final `ok`. Their complete logs and explicit IDs are
retained. The receipt's coverage count includes those two successes.

`validation.json` records the tree, commands, coverage, log hashes and
limits. `plan.json` lists every expected and assigned test ID;
`shard-0.json` and `shard-1.json` list the completed IDs. The historical
`remaining_tests.py` harness checks the frozen commit and tree at each
shard's start and finish. Logs were compressed with deterministic gzip
only after execution. The harness expects its original uncompressed
prefix log if its historical plan is reconstructed.

The archive replay completed before the regression interruption. Its
saved summary reports 73,856 profile checks, 353,664 product-filtration
inequalities, 12,976 binary cases, 209,692 ternary cases and 20,000 random
cases, with all exact payloads matching the archive. The ten credited
archive files and both immutable historical research directories remain
unchanged.

For a fresh verification of the published tree, the normal repository
commands are:

```sh
python -m unittest discover -s tests -v
python tools/replay.py
```

These checks validate finite implementation behavior and archive
reproduction. They do not replace the written quantified proof, establish
independent mathematical review, or improve the exponent.
