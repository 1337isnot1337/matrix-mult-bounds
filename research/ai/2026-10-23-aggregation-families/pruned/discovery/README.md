# Bounded discovery, separate from exact acceptance

These are completed finite experiments on the externally credited
general22 family. None is an optimality or characteristic-zero
nonexistence proof. The exact source and all-n position acceptance is
in [the parent verifier](../verify.py), which does not import these
discovery programs.

## Smaller dimension profiles

`explore.py` tried 10,000 mutation steps at each base n=2,3,4,7,11.
A profile specifies coordinate dimensions in {1,n}; full profiles were
disallowed so that the previous full-target hypothesis was removed.
Both centered active maps use the same smaller support. Every proposed
budget was counted as an integer, but the search objective divided by
a floating-point estimate of the volume mass. That objective only
guided discovery. The saved profiles are accepted separately by exact
counting and rational fourth-root intervals.

The report [dimension_profiles.json](dimension_profiles.json) records
all seeds, attempted step counts, successive improvements, final profiles,
budgets, and observed times. Each run completed; there is no claim of
exhaustive coverage or optimality. The featured n=3 profile is used as
one fixed all-n witness in the parent proof. Its selection base does
not limit the proof's dimension range.

From the repository root:

```sh
mkdir -p results/local/pruned-grid
python research/ai/2026-10-23-aggregation-families/pruned/discovery/explore.py
```

This writes a new discovery report under `results/local/pruned-grid/`.
It does not replace the accepted witness or the retained report.

## Separate centering rows

`split_auxiliary.py` uses E=[I;-1;0], D=[I;0;-1] on n+2 positions.
It treats ordinary coordinates as permutation orbits, and gives each
main or correction orbit its own scalar coefficient. For every mixed
triple of nonpositive grade, local coefficient functions are expanded
into these exact patterns:

- `O`: the ordinary equality tensor;
- `A`, `B`: the separate first or second extra row;
- `E`, `D`: the ordinary sum minus the relevant extra row;
- `R`: a replicated coordinate, with coefficients `(n,1,1)`.

For n>=2, the pairwise equality and all-ones functions are independent,
so they are constrained separately where both occur. The 2,279 distinct
pattern constraints cover all nonpositive mixed grades. Positive mixed
grades vanish in the formal parameter limit.

At each of n=2,3,4, row elimination is performed over the prime field
with modulus 1,000,003. The no-correction systems are inconsistent in
that field. With the supplied correction family the program exports
the actual modular coefficients and independently rechecks all 2,279
zero residuals and the unit diagonal coefficient. Its inexpensive-column
pivot ordering is a heuristic for cost, not an optimizer.

| n | No-correction modular system | Budget of corrected modular candidate | Original external complete-grid budget |
| ---: | --- | ---: | ---: |
| 2 | Inconsistent | 5,734 | 3,159 |
| 3 | Inconsistent | 24,420 | 13,312 |
| 4 | Inconsistent | 74,862 | 41,875 |

The candidate weights and all observed counts are retained in
[split_auxiliary.json](split_auxiliary.json). No characteristic-zero
lifting, all-n formula, finite-precision guarantee or optimality is
claimed for those candidates. In particular, modular inconsistency is
not promoted to a rational nonexistence result.

```sh
python research/ai/2026-10-23-aggregation-families/pruned/discovery/split_auxiliary.py
```

The original normalized source transcription in `explore.py` was checked
against the subsequently downloaded, hash-pinned ancillary bytes. Code
and report hashes, environment, seeds and scopes are retained in
[metadata.json](metadata.json). Neither experiment supplied an ingredient
that improves the direct 9/4 cost. No larger profile or orbit search is
part of this checkpoint.
