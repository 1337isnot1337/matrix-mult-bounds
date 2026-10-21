# Paired convolution sources: all-power Koszul ranks

AI-assisted research, October 20, 2026. **No exponent improvement or qualifying
matrix degeneration is constructed.** Written proofs are unreviewed.

For P_a=C(a,a)_(A,B,C) tensor C(a,a)_(A,C,B), put v=a^2 and
N=a(2a-1). The [all-power proof](all_koszul.md) gives, over every field,

    rank K_p(P_a)=N binom(v-1,p)+2(a-1)^2 binom(v-3,p-1).

The [matrix calculation](matrix_koszul.md) determines the comparison ranks
over C by the exterior Cauchy rule, Pieri rule and a Casimir operator. It
credits the kernel inclusion in Landsberg--Ottaviani (2015), Lemma 4.2;
no claim about historical priority or the subsequent literature is made.
These formulas exclude all 239 improving, dimension-compatible single
matrix targets for 2<=a<=13, modulo exchanging the two larger source legs.
Every exclusion has an exact integer rank witness in the saved frontier.
A second [cohomological matrix proof](matrix_euler.md) gives a short
alternating sum and proves the target ranks over every field. The complete
frontier through a=16 has 28 survivors, first appearing at a=14. They pass
this necessary test; none is an exhibited degeneration.

For a=4, an integer budget potential certifies the endpoint scoring ceiling
for every one-copy extraction to a direct sum of matrix blocks in each paired
factor. This method cannot force the finite profile gain needed for M106.
The ceiling concerns that factorwise extraction method; it does not exclude
joint extraction from the full six-factor source or its powers.

In particular, the initially selected P_6 -> M(6,10,6) target is now
excluded: at p=7 its Koszul rank exceeds the source rank by 1,456,180.
The earlier conditional 2.235 implication has an excluded premise. The
[first-kernel note](research_note.md) also excludes the full-capacity
matrix target in every size and a size-five matrix direct sum. None of
these obstructions closes joint extraction, larger formats or the separate
fat-point construction question. No singular coefficient construction is
supplied here.

## Reproduction

Use root requirements.txt. The coefficient and integer-budget routines use
only the standard library; exact slice-matrix controls additionally use SymPy.

```sh
python research/ai/2026-10-20-paired-sources/paired.py --output /tmp/paired-verification.json
python research/ai/2026-10-20-paired-sources/budgets.py --table /tmp/paired-budget.json.gz --output /tmp/paired-budget-verification.json
python research/ai/2026-10-20-paired-sources/all_ranks.py --maximum-a 16 --output /tmp/paired-frontier.json
python research/ai/2026-10-20-paired-sources/all_ranks.py --controls --output /tmp/paired-controls.json
python -m unittest discover -s tests -p test_paired_sources.py -v
```

The retained potential has 14,297 entries and 825,458 checked integer
transitions over all 267 admissible matrix shapes after the full-capacity
exclusion. All fourth-root decisions and threshold comparisons are exact.
The certificate checker tests upper inequalities without optimizing again.
The source controls verify every first-kernel vector and modular ranks at
a=2,...,6. There are also 16 independent higher-power source matrix controls
and 35 matrix-target controls. The tests check complete coverage of the
saved frontier and replay its strict witnesses; they need not repeat the
longer search for the first excluding power. The written arguments supply
the all-size conclusions. No random experiment or optional numerical
dependency is used for acceptance.

This work adopts the concurrent finite-amplitude ceiling and six-factor
profile implication from ../2026-10-20-koszul/finite_amplitude.md and its
Laurent coordinate-input screen from finite_target_screens.md. Those notes
credit OpenAI, Uznański and the group worker's earlier arguments. The paired
source kernels and the finite budget application are derived here. No prior
historical novelty or independent mathematical review is asserted.
