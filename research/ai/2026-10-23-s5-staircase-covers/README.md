# Finite staircase boundary for S5 cube covers

The [finite completeness argument](proof.md) and census account for every
one of 891888 monotone first-leg staircases, with two equal legs and an
independently optimized third. All eight block-word minima equal the
weighted covers in PR111. This family cannot improve those cube bounds.

For r=1, the [three-unequal-leg continuation](three_leg_boundary.md)
also accounts for all 77392758 unordered first/second threshold pairs.
Separate Python and C++ enumerations agree on all four word minima,
which again give the cube bound6867542. Thus allowing three different
monotone thresholds on these bidegree majorants still cannot exclude
M(13,14,14). The r=2 three-unequal-leg case is not enumerated.

These are finite experiments. They do not establish arbitrary cover
optimality, independent mathematical review, a target construction or an
exponent improvement. Nonmonotone covers, finer source support, other
bases and source powers remain separate questions.

```sh
python research/ai/2026-10-23-s5-staircase-covers/staircases.py --output results/s5-staircase-covers-2026-10-23/census.json
python -m unittest discover -s tests -p test_s5_staircase_covers.py -v
```

The tests reproduce the complete census, verify every saved cover on its
bidegree support majorant, check the closed count of enumerated
staircases, and compare the reduction with literal exhaustive small
support and threshold enumeration.
