# Ordinary rectangular targets of balanced cyclic sources

This finite report applies existing polynomial rank-locus and Hankel
symbol theorems. It establishes no new general rank theorem or exponent.

A later [rank-three saturation scan](../2026-10-21-rectangular-direct-sums/single_frontier.md)
closes the size-eight survivor described below. Across all balanced and
unbalanced sources through leg dimension1152, only A89 to M30 now survives
the maintained ordinary single-target gates. No maps are constructed.

Under the earlier gates alone, every potentially improving ordinary single matrix target is excluded
for balanced sources A_a through a=7. At a=8, source leg dimension960,
the sole sorted survivor of these gates is M(27,28,28), with target leg
dimensions756,784,756. Its maps are unconstructed. If supplied, the
existing spectral implication and the exact comparison

    4572288^191 > 46^765

would imply the conditional bound omega<=191/85<9/4. The premise remains
open. This is distinct from the existing M27 plus M7 direct-sum candidate.

The [finite application note](proof.md) records every theorem hypothesis
and all5139 improving sorted shapes for a=2,...,12:4192 are excluded and947
survive. These survivors are necessary-test outcomes, not constructions.
The [corner-minor note](corner_proof.md) gives a shorter rederivation of
the existing polynomial rank inequality, without claiming a new inequality
or independent mathematical review. Exact coordinate checks accompany it.

```sh
python research/ai/2026-10-21-rectangular-ordinary-frontier/verify.py --output /tmp/rectangular-frontier.json
python -m unittest discover -s tests -p test_rectangular_ordinary_frontier.py -v
```

The frontier code uses only exact integer comparisons. Tests independently
count complete candidate intervals, check every exclusion over all target
permutations, replay the conditional integer certificate, verify a direct
symbolic corner determinant, and reject corrupted witnesses.

Only balanced sources and single ordinary rectangular matrix blocks are
scanned. Unbalanced sources, direct sums, tensor powers and general
singular degenerations are outside this exclusion. The imported theorems
retain their written, unreviewed status and prior attribution.
