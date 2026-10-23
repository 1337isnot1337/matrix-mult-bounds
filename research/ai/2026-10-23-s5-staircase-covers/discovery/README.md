# Three unequal legs: discovery continuation

The standalone C++ integer enumeration completed all four r=1 block
words. Cost-sorted first and second thresholds, modulo their exchange,
leave an exactly minimized third threshold. The saved log reports no
improvement over the two-equal-leg minima. Pruning uses only nonnegative
remaining costs. It does not inspect r=2 or nonmonotone covers.

A separate Python implementation has completed and agrees on every
count, cost and retained witness. The [three-leg boundary](../three_leg_boundary.md)
records the finite completeness argument and literal small-support
controls. This continuation is registered only for r=1; the r=2 census
remains limited to two equal legs.

```sh
g++ -O3 -std=c++17 research/ai/2026-10-23-s5-staircase-covers/discovery/three_legs.cpp -o /tmp/s5-three-legs
/tmp/s5-three-legs
python research/ai/2026-10-23-s5-staircase-covers/discovery/three_legs.py --output results/local/s5-three-legs-python.json
```

The C++ program uses only standard-library integer arithmetic and is
optional discovery tooling, not a maintained verification dependency.
