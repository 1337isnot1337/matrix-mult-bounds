# Maximal first extensions and moving polynomial boundaries

Written proof and exact finite certificates, unreviewed, October 21, 2026.
No matrix-multiplication exponent improvement is established.

The [first-extension package](../2026-10-21-quantum-extension-spaces/README.md)
left open variations moving the leading rows outside fixed boundary spaces.
The [proof here](proof.md) handles those variations when the new first rows
span the full 16-dimensional quotient E_B/G and E_C/G on both sides.
At every order, the maps are forced into boundary spaces associated with
a moving two-dimensional plane of cubic forms. Their generic ranks are
at most 56, excluding the target M(10,10,11).

The key exact linear lemma leaves only four normal directions. They are
precisely the common polynomial plane's four tangent directions. The
certificate consists of ranks 220 and 224 and four explicit kernel vectors;
no floating-point inference is used in the proof.

A construction with these leading flags must therefore have first quotient
rank at most 15 on at least one side. Delayed first growth, such rank-deficient
jets, other leading flags, and leading-rank loss remain open. Neither an
arbitrary-degeneration exclusion nor an exponent improvement is claimed.

Reproduce from the repository root:

```sh
python research/ai/2026-10-21-moving-boundary-flags/normal_directions.py \
  --output results/local/moving-boundary-normal-certificates.json
python -m unittest discover -s tests -p 'test_moving_boundary_flags.py' -v
```

This package adopts the first-extension and partial-saturation results
identified in `sources.json`. Its generating session's exact checks do
not constitute external independent review or formalization.
