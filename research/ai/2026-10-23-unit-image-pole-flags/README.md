# Highest-pole flags at the remaining unit images

The [written proof](proof.md) narrows the regular-full-long-map,
regular-identity-lift chart left open by the one-sided unit theorem.
At A4 unit-image rank106 the first map must have a pole, whose leading
image has dimension at most four and belongs to one minimum-rank source
ruling. At image ranks102 through105, any first-map pole has a leading
image of dimension at most sixteen with one fixed rank-one Hankel factor.
Only the highest coefficient is constrained; lower poles remain open.

Run from the repository root with maintained dependencies:

```sh
python research/ai/2026-10-23-unit-image-pole-flags/verify.py
python -m unittest discover -s tests -p test_unit_image_pole_flags.py -v
```

`verify.py --write` regenerates
`results/unit-image-pole-flags-2026-10-23/controls.json`. The controls
reconstruct the original six-factor source, check24 minimum-rank slices
in eight four-dimensional rulings, exhibit ranks20 and32 when the
relevant fixed-factor conditions are broken, and retain a rank16 slice
with retained block rank4 at the rank106 boundary. This survivor does
not assert compatibility of the frames with a source unit trajectory.

The prior written source rank loci and Grothendieck's external splitting
theorem retain their credit and hypotheses in proof.md and sources.json.
The finite tests do not prove all formal coefficients, exclude the
remaining unit-image ranks, construct a target, or improve the exponent.
