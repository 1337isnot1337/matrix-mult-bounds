# Two ordinary A(8,9) targets excluded by rank-three inputs

The [written, unreviewed proof](proof.md) excludes ordinary complex
restrictions from A(8,9) to M(28,31,31) and M(29,30,31). It combines:

- a dimension budget for arbitrary linear projections of rank-at-most-k
  matrices, derived using the classical Borel fixed-point theorem;
- a codimension-two bound for every large linear section of the
  rank-seven8-by9 Hankel variety;
- the previously credited polynomial source-rank inequality and
  coefficient injection.

For either target, all rank-three parameter matrices must give Hankel
symbols of rank at most seven. The source coefficient injection requires
an image of dimension at least13 and at most16. Its rank-three image
would have codimension at least two, requiring dimension at least20 by
the projection budget. These inequalities contradict each other.

This is a structural exclusion, not a finite extension of the prior
linear-annihilator theorem beyond its hypotheses. The [PR138 inventory](https://github.com/1337isnot1337/matrix-mult-bounds/pull/138)
records the three preceding single-rectangular necessary-test survivors;
this argument excludes its two nonsquare formats. That inventory's
historical report is unchanged. The ordinary M30 target remains open:
its rank-two input constraint is compatible with the new dimension budget.
General singular maps and the exponent below9/4 also remain open.

The exact controls cover all7338 integer partitions of sizes0 through24
and22014 rank/diagram cases, all697 coordinate sections omitting at most
three moment coordinates, eight two-point/nonreduced moment families
including both projective endpoints, a seven-distinct-root conormal
control, four projection Jacobians, and both target rank budgets.
The tests independently differentiate the actual bilinear projection
maps and compute tangent annihilator intersections. The general geometric
proof is not formalized by these finite controls.

Owner-directed OpenAI Codex work. Borel's theorem, Milne's exposition,
the classical Hankel description and all earlier source proofs retain
their attribution. No historical priority, independent mathematical
review, construction or improved exponent is claimed. Exact source
versions and hashes are in sources.json; the package manifest excludes
itself and root coordination files.

With root requirements.txt installed, from the repository root:

```sh
python research/ai/2026-10-23-rank-three-hankel/verify.py --output results/rank-three-hankel-2026-10-23/controls.json
python -m unittest discover -s tests -p test_rank_three_hankel.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The next mathematical question is the rank-two image in the remaining
M30 case. The sharp3-by4 rank-two projection control has image
codimension two at dimension12. Thus applying the new budget unchanged
cannot exclude its possible13-through16-dimensional symbol images.
