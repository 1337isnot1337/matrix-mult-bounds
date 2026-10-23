# Sharp A4 source dimensions below ranks 84 and 88

The [proof](proof.md) establishes sharp maximum dimensions 56 and 60
for complex linear A4 source spaces whose slices all have rank strictly
below 84 and 88, respectively. The upper bounds use the prior
order-ideal reduction, eleven small coherent minors, three disjoint
middle-layer pairs, and exhaustive written cases.

Explicit staircase spaces attain dimensions 56 and 60 with maximum
slice ranks 80 and 84. The exported odd minors certify attainment.
All claims remain written and unreviewed externally.

From the repository root, run the standard-library acceptance program
and focused tests:

    python -I -S research/ai/2026-10-23-rank84-rank88-spaces/verify.py
    python -m unittest discover -s tests -p 'test_rank84_rank88_spaces.py' -v

Discovery is separate and requires an explicit output path:

    python research/ai/2026-10-23-rank84-rank88-spaces/discover.py --output results/local/rank84-rank88-candidate.json

The finite profile census checks the complete written case split.
The universal claim over complex spaces also uses the pinned
characteristic-zero geometric reduction. Mod-two arithmetic certifies
nonzero integer minors and does not replace that reduction.

The [question](QUESTION.md) and source record delimit the investigation.
There is no matrix-target construction, exponent improvement,
independent external review, or formalization.
