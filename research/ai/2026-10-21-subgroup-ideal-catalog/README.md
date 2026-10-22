# Complete subgroup-ideal catalog

The three active central-cover targets now have complete finite
subgroup-ideal catalogs: 455 subgroups in 65 conjugacy classes, with
exact integer upper-rank certificates and matching modular lower ranks.
The [proof and scope](proof.md) retain credit for the existing
subgroup-averaging lemma and source tables.

For PSL(2,5) x C2 to M10, noncyclic order-four and order-six subgroups
add 550 minimal forbidden cosets per leg beyond central pairs and
order-five cosets. The other two selected sources have no additional
minimal cuts from this method. These results constrain coordinate maps
with strict vertex potentials. They do not exclude the selected targets
under arbitrary complex maps or establish an exponent below 9/4.

From the repository root, using the maintained requirements:

```sh
python research/ai/2026-10-21-subgroup-ideal-catalog/subgroup_catalog.py \
  --output results/local/subgroup-catalog.json.gz
python research/ai/2026-10-21-subgroup-ideal-catalog/verify_catalog.py \
  results/subgroup-ideal-catalog-2026-10-21/catalog.json.gz
python -m unittest discover -s tests -p test_subgroup_ideal_catalog.py -v
```

The deterministic gzip certificate includes the full subgroup lists,
generation witnesses, all conjugacy classes, all integer annihilators and
the exact inclusion-minimal cuts. Verification checks closure and complete
one-generator extensions independently of the enumeration's traversal.
The tests also compare with all 256 subsets of C2 cubed and reject an
omitted subgroup, a corrupted rank witness and an omitted minimal cut.

The search is optional and additionally requires the existing discovery
dependencies `python-sat` and `scipy`; certificate replay and the regression
tests do not require either. The run used the existing discovery environment
at `/home/cinna/matrix-mult-filtration-20261020/.venv`, rather than changing
the maintained requirements.

```sh
python research/ai/2026-10-21-subgroup-ideal-catalog/search.py --control \
  --output results/local/subgroup-catalog-control.json
python research/ai/2026-10-21-subgroup-ideal-catalog/search.py \
  --reuse-report results/subgroup-ideal-2026-10-21/split-target10.json \
  --seconds 600 --output results/local/subgroup-catalog-target10.json
python research/ai/2026-10-20-sl2-five-native-parity/verify.py \
  results/local/subgroup-catalog-target10.json
```

The weighted 3-by-3 control passes. The new 600-second target run ended
at its time limit after 34 model events, with 32 exported exact parity
contradictions and no pair-injective lift. Every exported contradiction
replays; the two other events learned conditional rows. This is a bounded
discovery result, not a target exclusion or a measured search speedup.
All 794 current test IDs have successful results: 360 completed in the
initial sequential run, followed by 434 tests partitioned across four
processes at module boundaries. Three optional numerical controls skipped
in the maintained environment also passed in the existing discovery
environment. The compressed logs, complete inventory and disjoint
assignment reconciliation are saved in
`results/subgroup-ideal-catalog-2026-10-21/regression-evidence.json.gz`.
The five historical experiments replay successfully and all 18 tracked
historical archive files match the base byte for byte.

An initial focused test expected the preceding running checkpoint's 30
parity contradictions. Its assertion was corrected to the terminal count
32, with the failed log retained; the production certificate was unchanged.
The mathematical claims remain written and unreviewed or finite
experiments, as specified in the claim ledger.
