# Exact aggregation of 29 independent products

The [written proof](proof.md) and [exported witness](witness_29.json) give

\[
R\bigl(M(n^3,n^3,n^3)^{\oplus29}\bigr)
\le (n+1)^9+9(n+1)^8+36(n+1)^7+3(n+1)^6
\]

for every positive integer n over every characteristic-zero field.
The independent set-based verifier checks all 24,389 ordered triples.
This raises the attained exact nine-coordinate comparison family from
28 to 29 products and strictly lowers its bound per output for every n.
The underlying aggregation method is credited to the external sources
in [sources.json](sources.json); the new family was found locally.

An exact weighted AM-GM certificate shows that the displayed budget
cannot reach the exponent 9/4 through direct asymptotic-sum substitution
at any local dimension. This is a statement about that cost formula,
not a tensor-rank lower bound. It supplies a positive independent-product construction with a
complete cost, not a restriction from the repository's polynomial
source. No optimality, historical priority, independent review, or
formalization is claimed.

## Exact acceptance

From the repository root:

```sh
python research/ai/2026-10-23-aggregation-families/verify.py
python research/ai/2026-10-23-aggregation-families/evaluate.py
python -m unittest discover -s tests -p test_aggregation_families.py -v
```

The verifier enforces the versioned baseline SHA256 and recomputes
every mixed triple, every correction subset,
and the exact positive-coefficient comparison with the attributed
external baseline. The evaluator separately constructs the rational
centered dual maps modulo 101 and sums all 159,651 rank-one terms at
n=2 for a full seeded assignment of matrix entries. Its answer equals
the independently evaluated target. This finite evaluation is a
control; the uniform proof is the argument in proof.md.

The acceptance and control reports are checked in. Dependencies are
only the Python standard library. Tests deliberately remove a required
correction, duplicate a product, understate a cost, and alter the external
source bytes to check rejection. They also require exactly 29 products.

## Optional discovery reproduction

Discovery uses C++17, with no external libraries. First export the
credited 28-product seed in the mask format consumed by the search:

```sh
python research/ai/2026-10-23-aggregation-families/verify.py --export-seed results/local/aggregation-search/ex28.masks
c++ -O3 -std=c++17 research/ai/2026-10-23-aggregation-families/search.cpp -o results/local/aggregation-search/search
results/local/aggregation-search/search results/local/aggregation-search/ex28.masks conflict 300000 20261023 results/local/aggregation-search/reproduced-29.masks
```

The recorded run found 29 products at iteration 8,312 and completed
300,000 local destroy-and-rebuild iterations without a larger family.
`discovery_report.json` records its parameters. This coverage is not
exhaustive and proves no upper bound. Search need not be repeated to
verify the construction. C++ standard-library shuffle implementation
choices can affect the exact search trajectory; acceptance is portable.

`QUESTION.md` preserves the initial investigation and states the gap
between improving a finite aggregation family and improving omega.
The earlier local shared-input partial-transpose construction is a
different investigation and retains its prior credit.
