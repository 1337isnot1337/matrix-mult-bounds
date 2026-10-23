# Stacked-product continuation to unit-image rank105

The [written proof](proof.md) sharpens the prior rank107 exclusion by
combining two source blocks into one regularized product of rank at
most q. First-map poles then require source rank at most2q; rank-one
target parameters have limiting source rank at most n+2q. A rank-one
kernel bound replaces first-map injectivity, and coherent factors
propagate across target rulings even when some parameters have zero image.

For A4 to M(10,10,11), this excludes every finite Laurent order when one
long map is regular with rank110 limit, the source identity lift is
regular, and its unit image has rank at least105. This includes every
regular source unit of corank at most five. Retained rank104, singular
long-leg limits and polar units remain unresolved by this argument.

Claims `AI-CYCLIC-STACKED-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-RANK105-002` are written and unreviewed. No independent
review, formalization, tensor construction or exponent improvement.
The prior source theorems, frames and retraction lemma retain their
existing credits and exact byte pins. No new external theorem is imported.

```sh
python research/ai/2026-10-23-unit-image-stacked-rank/verify.py
python -m unittest discover -s tests -p 'test_unit_image_stacked_rank.py' -v
```

The finite controls include48 exact Laurent block families, three symbolic
rank-one matrix spaces, seven A4 image-rank cases and three dependency
pins. The block examples attain rank2q, including the strict rank104
boundary, but are not cyclic-source degeneration witnesses. The tests
separately inspect all binary2-by2 rank-one pencils. These controls do
not formalize arbitrary Laurent series.
