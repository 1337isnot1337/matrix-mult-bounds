# Full-right-inverse Laurent regularity

The [written, unreviewed proof](proof.md) gives a general Laurent
regularity theorem without a low-rank-spanning target hypothesis.
Its A4 application excludes the canonical A4 to
M(10,10,11) degeneration whenever one long map C is regular with rank110
limit, the target identity has a regular source lift, and its limiting
image S(0) C(0) has rank at least102. It includes source units of corank
at most eight. PR105's rank109 theorem is preserved as a predecessor.

After normalizing the unit equation, T=S C is a regular right inverse
of the possibly polar B. The projector I-T B has rank two over C((t)).
Regularizing its product with a source slice first excludes every pole
in F. The unit-image rank then makes F(0) injective, and the full-column
row-contraction dimension bound excludes poles in B. The existing
ordinary slice-rank contradiction finishes the A4 application.

This is a source-grounded extension at every finite Laurent pole order,
separate from the local fourteen-row conic jets and PR103's fixed
resolvent. No independent review, formalization, arbitrary degeneration
exclusion, matrix construction or smaller exponent is claimed. Image
rank101, singular long-leg limits and polar unit lifts remain outside
the exclusion. First-map regularity alone needs no unit-image rank bound.

See [the question](QUESTION.md) and [predecessor pins](sources.json).
Concurrent [PR113](https://github.com/1337isnot1337/matrix-mult-bounds/pull/113)
at08ac3e9 uses low-rank target generators with the same right-inverse
mechanism to exclude every A4 chart with one regular full-rank long map,
including arbitrary original unit lifts. It subsumes this package's A4
corollary. The rank101 equality above is a boundary of this general
criterion, not a remaining A4 frontier. Its proof was inspected after
this package's first commit c34ffcd; no independent review is claimed.
PR125 and PR142 separately address singular long-map limits.

Reproduce finite controls and five focused tests:

```sh
python research/ai/2026-10-23-regular-unit-projector/verify.py
python -m unittest discover -s tests -p test_regular_unit_projector.py -v
```

The exact controls and focused tests pass. All five historical archive
replays pass. Full local regression and final-head hosted CI remain in
progress. These checks support finite linear algebra and do not formalize
the universal proof or establish independent mathematical review.
