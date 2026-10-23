# Rank-gap continuation of the long-leg obstruction

This additive checkpoint imports the previously established complex A4
slice-rank gap: a nonzero source slice has rank 16 or at least 20.
It preserves the simpler minimum-locus-only proofs and their original
finite reports in this package.

Two new written arguments give necessary conditions for a Laurent
degeneration A4 to M(10,10,11):

- [The individual-leg extension](gap_extension.md) excludes any regular
  long map whose limit has rank at least 106. It proves the needed
  rank-one-preserver classification directly, including degenerate maps.
- [The normalized rank-sum extension](rank_sum_gap.md) requires
  r_B+r_C<=204 after independent scalar valuation normalization of the
  long maps. This argument needs only the classification of linear spaces
  in the minimum-slice locus.

Thus a remaining scalar-normalized chart must have both long leading
ranks at most 105 and their sum at most 204. These are necessary conditions;
the notes do not construct a chart on the boundary or exclude every
degeneration. Singular changes of basis are not treated as preserving
these leading ranks. No improved matrix-multiplication exponent is claimed.

The rank-gap proof imports Grothendieck's splitting theorem for vector
bundles on the complex projective line. This extra dependency, its source
version, the predecessor proof bytes, and the concurrent PR113 kernel
argument are recorded in [gap_sources.json](gap_sources.json). All claims
remain `proof-written-unreviewed`; same-session agent checks are not an
independent mathematical review or formalization.

## Reproduce the finite controls

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-long-leg-rank-obstruction/verify_gap.py
python -m unittest discover -s tests -p test_long_leg_rank_gap.py -v
```

To regenerate the report, run the verifier with `--write`. The exact
report is `results/long-leg-rank-gap-2026-10-23/controls.json`.

Coverage consists of 32 factored or transposed-preserver kernel units,
two arbitrary fixed-factor kernel units, literal source blocks of ranks
16, 20, 24 and 28, and all 12,100 nonzero integer leading-rank pairs.
Seeds are 106204 for factored maps and 410 for fixed-factor maps. All
matrix calculations use exact SymPy arithmetic.

Two negative controls distinguish claims the proofs do not make. A
rank-one preserver can have a full 16-dimensional Mat4 image, and a
Mat10-to-Mat6 rank-one preserver can have an entirely singular kernel.
The first prevents replacing the individual-leg preserver argument with
the smaller linear-minimum-locus argument; the second checks the role
of the output dimensions. These finite examples check algebra and sharp
boundaries. They do not prove the universally quantified preserver
classification, the source rank gap, or the Laurent obstruction.

Proposed claim-ledger entries are in [claims_gap.json](claims_gap.json).
