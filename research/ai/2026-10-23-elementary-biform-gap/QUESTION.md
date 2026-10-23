# Elementary arbitrary-biform rank gap

October 23, 2026. Base main 3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93.
Owner-directed Codex work on research/elementary-biform-gap-01a1697a-d83f.

Question: can the existing block rank gap for every nonseparable complex
biform be proved without the vector-bundle splitting input used in
research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md?
The separate active PR171 treats exact two-monomial ranks; this question
concerns arbitrary biforms and does not duplicate its residue classification.

Candidate route: choose a smooth point on a mixed irreducible factor,
translate both variables, and scale to the lowest homogeneous term.
This should give a power of a linear form with two nonzero coefficients.
Prove a sufficient rank lower bound for that power directly using integer
minors. Verify the exact covariance of the maintained crossed coefficient
matrix under these affine changes before transferring a rank bound.

First checks: determine the complete ranks of those power matrices and
find characteristic-zero lower minors. A failed covariance, rank formula
or specialization implication must be recorded rather than assumed.
No theorem, dependency removal, matrix target or exponent gain was claimed
at the initial discovery checkpoint. The subsequent written argument and
exact acceptance are linked from README.md. Historical archives remain untouched.
