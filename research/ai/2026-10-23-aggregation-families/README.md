# Exact aggregation of 29 and 106 independent products

The [written proof](proof.md) and exported witnesses give these exact
rank bounds for every positive integer n over every characteristic-zero
field. Write x=n+1.

| Independent products | Matrix dimension | Rank upper bound | Improvement over cited external family |
| ---: | --- | --- | --- |
| [29](witness_29.json) | n^3 by n^3 | x^9+9x^8+36x^7+3x^6 | Smaller certified cost per output than 28 products, for every n>=1 |
| [106](witness_106.json) | n^4 by n^4 | x^12+12x^11+66x^10+139x^9+5x^8 | Smaller certified cost per output than 105 products, for every n>=7 |

A separate set-based verifier checks all 24,389 and 1,191,016 ordered
mixed triples, respectively, and every required correction subset.
The source aggregation mechanism and comparison families are credited
to Solomonik and Blaeser, arXiv:2610.26563v2, in
[sources.json](sources.json). The new finite families were found locally.
No optimal rank or historical priority is claimed.

These are positive tensor constructions with complete uniform costs.
They do not improve omega below 9/4. An exact [size gate](cost_floor.md)
shows that no balanced conflict-free family with N<=10 can cross that
threshold while charging the complete (n+1)^(3N) leading aggregate.
This concerns a displayed upper-bound certificate; it is not a lower
bound on tensor rank. N>=11 is necessary for this particular cost model,
not sufficient. No polynomial-source restriction, independent
mathematical review, or formalization is supplied.

## Exact acceptance

From the repository root:

```sh
python research/ai/2026-10-23-aggregation-families/verify.py
python research/ai/2026-10-23-aggregation-families/verify.py research/ai/2026-10-23-aggregation-families/witness_106.json
python research/ai/2026-10-23-aggregation-families/evaluate.py
python research/ai/2026-10-23-aggregation-families/evaluate_binary.py
python -m unittest discover -s tests -p test_aggregation_families.py -v
```

The verifier enforces the versioned external source SHA256, recomputes
every mixed triple and correction subset, and verifies exact polynomial
identities for both cost comparisons. For 106 products it certifies the
n>=7 threshold by positive coefficients after the integer shift x=8+u.
It preserves the stronger all-positive-n comparison for 29 products.

The evaluators are implementation controls, separate from the uniform
proof. One F101 assignment to the 29 independent 8-by-8 products checks
all 159,651 rank-one contributions. One F2 assignment to the 106
independent 16-by-16 products checks all 9,323,181 rank-one positions by
exact byte-packed arithmetic; 117 correction aggregates are nonzero.
Each corrected scalar value equals the independently evaluated target
under that assignment. Neither evaluation claims to check all possible
input coefficients. Mathematical acceptance is the complete finite
combinatorial certificate plus the written all-n coordinate identity.

All maintained acceptance tools use only the Python standard library.
Tests enforce the advertised product counts, reject altered source
bytes, remove a required correction, and understate a cost. Saved reports
record their exact scopes. `validation.json` and the complete
[validation receipts](validation/README.md) account for all 909 discovered
tests through the cost-gate refinement. They distinguish the preserved
baseline successes, final focused tests, and recorded remaining shards.

## Optional discovery reproduction

The constructive local search uses C++17 with no external libraries.
First export the credited external seeds in its mask format:

```sh
python research/ai/2026-10-23-aggregation-families/verify.py --export-seed results/local/aggregation-search/ex28.masks
python research/ai/2026-10-23-aggregation-families/verify.py research/ai/2026-10-23-aggregation-families/witness_106.json --export-seed results/local/aggregation-search/ex105.masks
c++ -O3 -std=c++17 research/ai/2026-10-23-aggregation-families/search.cpp -o results/local/aggregation-search/search
results/local/aggregation-search/search results/local/aggregation-search/ex28.masks conflict 300000 20261023 results/local/aggregation-search/reproduced-29.masks
results/local/aggregation-search/search results/local/aggregation-search/ex105.masks conflict 20000 20261031 results/local/aggregation-search/reproduced-106.masks
```

The first run found 29 products at iteration 8,312 and completed 300,000
iterations. The second found 106 at iteration 17,022 and completed 20,000.
The discovery reports record the exact inputs, code hash, and seeds.
C++ standard-library shuffle implementations can change the search
trajectory; acceptance of the saved witnesses is portable.

The unsuccessful 30-product and correction-free 39-product attempts
are recorded separately in [search_followups](search_followups/README.md).
Those bounded runs are not nonexistence or optimality proofs. A numerical
MILP solver proposed candidates only; its statuses are never mathematical
acceptance premises. No discovery search need be repeated to verify the
two successful constructions.

`QUESTION.md` preserves the initial research question. The earlier
shared-input partial-transpose construction is distinct and retains
its source credit and obstruction scope.
