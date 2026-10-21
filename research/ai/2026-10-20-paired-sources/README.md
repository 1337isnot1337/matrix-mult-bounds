# Paired convolution sources and a finite size-six target

AI-assisted research, October 20, 2026. **No exponent improvement or qualifying
matrix degeneration is constructed.** Written proofs are unreviewed.

The [research note](research_note.md) proves an exact first Koszul kernel
of dimension 3a-2 for the paired source
P_a=C(a,a)_(A,B,C) tensor C(a,a)_(A,C,B). It excludes the full-capacity
matrix target M(a,2a-1,a) under arbitrary complex degeneration. It also
excludes the size-five direct sum M(4,9,4)+M(3,3,3), whose conditional
spectral implication would otherwise beat 9/4. These are algebraic
source obstructions, not finite solver negatives.

For a=4, an integer budget potential certifies the endpoint scoring ceiling
for every one-copy extraction to a direct sum of matrix blocks in each paired
factor. This method cannot force the finite profile gain needed for M106.
The ceiling concerns that factorwise extraction method; it does not exclude
joint extraction from the full six-factor source or its powers.

The next open finite target is P_6 -> M(6,10,6), in formats (36,66,66)
to (36,60,60). It would imply omega<=2.235, by the existing convolution
ceiling and an exact integer comparison. Ordinary restrictions and the
adopted coordinate-input models are excluded. The first Koszul tests leave
the target open; higher recorded grading bounds are only coarse necessary
tests. A genuine singular coefficient construction remains missing.

## Reproduction

Use root requirements.txt. The coefficient and integer-budget routines use
only the standard library; exact slice-matrix controls additionally use SymPy.

```sh
python research/ai/2026-10-20-paired-sources/paired.py --output /tmp/paired-verification.json
python research/ai/2026-10-20-paired-sources/budgets.py --table /tmp/paired-budget.json.gz --output /tmp/paired-budget-verification.json
python -m unittest discover -s tests -p test_paired_sources.py -v
```

The retained potential has 14,297 entries and 825,458 checked integer
transitions over all 267 admissible matrix shapes after the full-capacity
exclusion. All fourth-root decisions and threshold comparisons are exact.
The certificate checker tests upper inequalities without optimizing again.
The source controls verify every kernel vector and modular ranks at a=2,...,6;
the written argument supplies the all-size conclusion. No random experiment
or optional numerical dependency is used for acceptance.

This work adopts the concurrent finite-amplitude ceiling and six-factor
profile implication from ../2026-10-20-koszul/finite_amplitude.md and its
Laurent coordinate-input screen from finite_target_screens.md. Those notes
credit OpenAI, Uznański and the group worker's earlier arguments. The paired
source kernel and the finite budget application are derived here. No prior
historical novelty or independent mathematical review is asserted.
