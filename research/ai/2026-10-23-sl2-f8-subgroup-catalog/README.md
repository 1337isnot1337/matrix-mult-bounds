# Complete SL(2,F8) subgroup cuts

The [written proof](proof.md) and exact certificate enumerate all386
subgroups in12 conjugacy classes, determine every averaging-ideal
dimension over C, and give all minimal full-coset cuts for the sixteen
saved SL(2,F8) coordinate/potential targets.

Two new minimal classes occur. Order14 dihedral subgroups have ideal
dimension308 and add1296 forbidden cosets on every target leg. Order6
subgroups have ideal dimension455 and add7056 cosets on ten of the48
legs. For M(18,18,25), the full minimal counts are3431,3431,2647.
A control vertex set passes the old8,9,18 filters and fails the new14 filter.

From the repository root:

```sh
python research/ai/2026-10-23-sl2-f8-subgroup-catalog/verify.py results/sl2-f8-subgroup-catalog-2026-10-23/certificate.json.gz
python -m unittest discover -s tests -p test_sl2_f8_subgroup_catalog.py -v
```

Regenerate discovery with the maintained root environment:

```sh
python research/ai/2026-10-23-sl2-f8-subgroup-catalog/catalog.py --output results/local/sl2-f8-subgroup-catalog.json.gz
```

Acceptance independently checks generator closure and extension
completeness, actual integer central projection identities and actual
nonzero coset minors modulo1009. It then checks minimality and coverage
for every saved target leg. Character data are used only in discovery.

The subgroup averaging lemma, exact source and earlier central-cover
catalog retain their credits in `sources.json`. The proof is written and
unreviewed. These are necessary conditions only; no improving target,
complete coordinate exclusion or exponent improvement is established.
