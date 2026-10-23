# A 68-dimensional source space below rank 96

This small checkpoint records an explicit counterexample to the
proposed universal A4 source-space cap 57 below rank 96. The space
has 68 independent source coordinates and only 92 supported matrix
columns. Every slice therefore has rank at most 92.

The proof gives a whole family at every source size: d full short
coordinate layers, followed by m middle layers of the next short
coordinate. Its dimension is a[d(2a-1)+m], and its joint column support
has size a^2(a+d-1)+a min(m,a).

Run the exact standard-library controls from the repository root:

```sh
python research/ai/2026-10-23-source-staircase-spaces/verify.py
python -m unittest discover -s tests -p 'test_source_staircase_spaces.py' -v
```

The checker covers all 140 parameter triples for a=2,...,6 and replays
the saved A4 counterexample directly from the literal source. It
proves the finite support counts; the written argument proves the
all-size construction.

Proposed claim: `AI-CYCLIC-SOURCE-STAIRCASE-SPACES-001`.

This defeats the particular rank-96 cap premise proposed for a
sum-128 continuation. It does not block smaller threshold refinements
or arguments using the structure of actual compression kernels.
No rank ceiling is claimed attained, and no target or exponent bound
is improved. The claim remains written and externally unreviewed.
