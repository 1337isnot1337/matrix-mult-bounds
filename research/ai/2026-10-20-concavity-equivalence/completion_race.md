# Longer finite completion recipes

Selected source: OpenAI, *Complex Matrix Multiplication Below 2.258 and
Rectangular Bounds*, September 24, 2026, Sections 10-12, especially 12.3.
The primary PDF was downloaded and its text inspected. Its construction and
recurrences are external work, not local discoveries.

The base-rank-three conditional counts are `(2,2,1)`, and the base-rank-two
counts are `(1,1,1)`. A completion of size m at center i sends

`d_i -> d_i^m` and `d_j -> (d_i+d_j)^m-d_i^m` for each other j.

After termination, keep two colors. If N is their total count and b is the
product of the completion sizes, the externally proved uniform-leaf witness
gives exponent at most `3 b log(R)/log(N)`, where R is the base rank.
It beats 9/4 exactly when `N^3 > R^(4b)`.

This investigation extends the published finite list by a bounded beam search.
Floating log counts are discovery data only; a proposed improvement requires
integer replay and an exact power comparison, plus checking the external
recipe hypotheses. No smaller exponent is presently claimed.

The first completed beam used sizes 2,3, depth 15 and width 4,000. Its best
descriptive values were approximately 2.28345385 from rank two and 2.26511039
from rank three. Neither beats 9/4. Temporary detailed beam files were not
available after continuation, so no new exact recipe bound is reported.
The published Section 12.3 five-step recipe was separately replayed in integers:
it has b=72 and the exact quoted terminal count
2995461856366867388223311649574852466276480577.

Primary source:
[pinned manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf).
The source commit was obtained from the GitHub file history. The local review
covered the construction description and Sections 10-12, not a fresh Lean build.
