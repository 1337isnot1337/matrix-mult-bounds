# Two regular leg maps: a necessary rank frontier

The [written proof](proof.md) gives an all-order necessary condition for
the canonical A4 source to reach M(10,10,11). If both maps to the two
110-dimensional target legs are regular, their limiting ranks sum to at
most192. Their total rank loss is therefore at least28. The remaining
map may have arbitrary Laurent poles, and both regular maps may have
arbitrary higher jets and complex input mixing. No target unit is chosen.

The argument combines the prior source locus below twice minimum matrix
rank with the prior saturated target-support inequality. These older
results keep their attribution and byte pins in [sources.json](sources.json).
The new intermediate bound says that two-sided compression of total
defect below2a^2 hides at most a^2 source dimensions. At defect a^2
with both maps deficient, the sharp hidden dimension is at most one.
With one short and
one long regular target leg, the same tests leave exactly sixteen rank
pairs of total rank at least193; they are listed in the proof and report.

The results are **written and unreviewed**. Finite controls do not
formalize the arbitrary-complex-map or all-order statements. The lower
rank pairs, singular constructions outside these hypotheses and the
exponent goal remain open. No target or smaller exponent is established.

Reproduce from the repository root with the root requirements installed:

```sh
python research/ai/2026-10-23-regular-leg-frontier/verify.py
python -m unittest discover -s tests -p test_regular_leg_frontier.py -v
```

The [finite report](../../../results/regular-leg-frontier-2026-10-23/controls.json)
contains ten exact coordinate compressions, five rank-2a^2 boundary
controls, and an exhaustive screen of23532 integer rank pairs. The
compressions enumerate the original six source indices for a=2,...,6.
They attain both an a^2-dimensional hidden coherent space and a single
hidden minimum-rank source slice. The tests also reject altered source
pins, corruption of this evidence and inflated scope. Use `verify.py
--write` only to regenerate the report, then replay without that flag.

Claims: `AI-REGULAR-COMPRESSION-KERNEL-001` and
`AI-A4-REGULAR-LEG-FRONTIER-002`.

Concurrent PRs [113](https://github.com/1337isnot1337/matrix-mult-bounds/pull/113)
and [125](https://github.com/1337isnot1337/matrix-mult-bounds/pull/125)
study one-regular-leg obstructions and close some pairs that survive this
standalone screen. Their unreviewed proofs are separate and retain their
credit; the sixteen pairs here are not claimed as a global open frontier.
