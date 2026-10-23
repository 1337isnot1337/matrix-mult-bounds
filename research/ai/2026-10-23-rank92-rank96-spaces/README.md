# Sharp source caps below ranks 92 and 96

For the canonical complex A4 source, the maximum dimension of a linear
space whose slices all have rank strictly below 92 is exactly 68.
Below 96 the maximum dimension is exactly 72. Explicit spaces attain
these dimensions and attain matrix ranks 91 and 95, respectively.
These spaces disprove the initially proposed smaller caps 64 and 68.

Read [proof.md](proof.md) for the source formula, credited order-ideal
reduction, short layer-size case splits, and fixed row-and-column covers.
[sources.json](sources.json) records exact prerequisite bytes.
[QUESTION.md](QUESTION.md) states the investigation and claim scope.

## Reproduce acceptance

From the repository root, using Python 3.10 or later:

    python -I -S research/ai/2026-10-23-rank92-rank96-spaces/verify.py
    python -m unittest discover -s tests -p 'test_rank92_rank96_spaces.py' -v

Acceptance uses only the Python standard library and integer arithmetic.
It reconstructs the literal matrices, checks 112 source factorizations,
replays eleven credited coherent minors and two new sharpness minors,
checks both fixed covers, and independently enumerates all 245,157
nonincreasing seven-layer size profiles. No random search is used for
acceptance. The profile census checks the written case split.

The saved report is
[controls.json](../../../results/rank92-rank96-spaces-2026-10-23/controls.json),
and the fixed witnesses are
[certificates.json](../../../results/rank92-rank96-spaces-2026-10-23/certificates.json).

## Optional discovery replay

    python research/ai/2026-10-23-rank92-rank96-spaces/discover.py --output results/local/rank92-rank96-spaces/rebuilt.json

Discovery copies the eleven credited coherent certificates and searches
at most 256 binary masks per sharpness space with seed zero reset for
each space. The stored rank-91 and rank-95 witnesses occur on attempts
2 and 5. Selected minors use highest-column elimination; acceptance
rebuilds coefficients from a different literal indexing loop and uses
lowest-column elimination on the specified square minors.

Both theorem thresholds are strict and the geometric reduction is in
characteristic zero. The support covers themselves work over any field.
There is no classification of all extremal spaces, target construction,
target-rank-pair theorem, or matrix multiplication exponent improvement.
