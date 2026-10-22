# Zero-or-three gap for balanced boundary projections

The [written proof](proof.md) proves the following complex matrix-space
statement: if `dim Z>=2` and Z contains no nonzero rank-one matrix, then
quotienting `Z tensor Mat2` by kernels of dimensions at most two on each
matrix leg leaves either zero first dimension or first dimension at least
three. The bound is sharp.

The rank-three case is an elementary quotient argument. The remaining
constant-rank-two pencils use the external classical complex Kronecker
canonical form, followed by explicit local gap arguments for its five
possible formats. The skew-pencil format has the stronger zero-or-four
gap. [sources.json](sources.json) states the exact imported theorem,
hypotheses, inspected source and fetched hash. Its proof is not rebuilt.

Within the actual 28-dimensional boundary-compatible normal family of the
preceding biform packages, projected first rank at most two now forces
complete cancellation. Its surviving normals therefore have the conic
shared factor already classified in PR94. The separate boundary
obstruction pair can still have ranks two/two outside that family; the
general 10-by10 first-boundary case remains open. Later compatibility,
full matrix slice space and an exponent improvement remain unproved.

Six focused tests replay five canonical-pencil certificates, seven
sharpness/hypothesis controls, all 651 rational lifts of binary kernels,
25 independent binary contractions and pinned local dependencies. The
registered discovery run completed all 423801 ordered binary kernel pairs
for the skew pencil; its only low-dimensional modular candidate replayed
as zero over Q. That finite screen is separate from the written proof.

The theorem is AI-assisted and unreviewed. No independent review,
formalization, historical priority or exponent below 9/4 is claimed.

```sh
python research/ai/2026-10-21-balanced-puncture-gap/verify.py --output results/balanced-puncture-gap-2026-10-21/controls.json
python research/ai/2026-10-21-balanced-puncture-gap/discover.py --output results/balanced-puncture-gap-2026-10-21/binary-kernels.json
python -m unittest discover -s tests -p test_balanced_puncture_gap.py -v
```

The exhaustive pilot is deterministic. Its saved elapsed time is a run
measurement and does not participate in acceptance or reproduction equality.
The exact histograms, kernel enumeration and rational replays do.
