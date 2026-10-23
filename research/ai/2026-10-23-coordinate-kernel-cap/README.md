# A coordinate-kernel cap in the regular-leg frontier

The [written proof](proof.md) closes the sixteen mixed high-rank pairs
of the prior standalone regular-leg screen when both constant regular
maps have coordinate kernels in the canonical A4 bases. Higher jets,
output frame mixing and the third Laurent map are unrestricted. Any
such regular pair therefore has limiting ranks summing to at most192.
This is a condition on the leading kernels, with no assumption that the
higher series maps stay coordinate.

The certificate covers every8008 ten-coordinate biform subspace.
7744 have25 disjoint source edges. The other264 have24 matching edges
and a uniquely forced24-vertex cover, all on one side. None fits the
mixed candidates' deletion budgets, giving projected source rank at
least103 against the target ceilings102 and101.

This is a finite coordinate census and a **written, unreviewed**
all-order application. It does not classify arbitrary complex leading
kernels, construct a target or improve the exponent. Prior source and
saturation results keep their attribution and byte pins.

From the repository root:

```sh
python research/ai/2026-10-23-coordinate-kernel-cap/verify.py
python -m unittest discover -s tests -p test_coordinate_kernel_cap.py -v
```

The checker performs no matching search. Discovery can be regenerated
with `python research/ai/2026-10-23-coordinate-kernel-cap/discover.py`,
followed by verification. Witnesses are compressed in
`results/coordinate-kernel-cap-2026-10-23/matchings.json.gz`; the JSON
summary records exact scope and counts. Corrupted matchings, omitted
subsets, altered source pins and inflated claims must be rejected.

Claims: `EXP-COORDINATE-COVER-CENSUS-001` and
`AI-A4-COORDINATE-REGULAR-PAIR-002`. No new external theorem is imported.
