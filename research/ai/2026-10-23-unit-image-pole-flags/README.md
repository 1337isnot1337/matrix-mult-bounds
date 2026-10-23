# Highest-pole flags at the remaining unit images

**Disposition:** [superseded for the A4 frontier](DISPOSITION.md) by PR113.
The scoped proof and controls are retained on this closed branch.

The [written proof](proof.md) narrows the regular-full-long-map,
regular-identity-lift chart left open by the one-sided unit theorem.
At A4 unit-image rank106 the first map must have a pole, whose leading
image has dimension at most four and belongs to one minimum-rank source
ruling. The complete principal part has rank at least six, and its pole
order is at least two. No simple first-map pole is possible. The small-
principal-part argument uses at most four polar long-map terms and the
regular unit equation; it covers every Laurent order, while leaving
complete principal rank6 open. At image ranks102 through105, any first-map
pole has a leading image of dimension at most sixteen with one fixed
rank-one Hankel factor. Lower pole flags and a full target remain open.

Run from the repository root with maintained dependencies:

```sh
python research/ai/2026-10-23-unit-image-pole-flags/verify.py
python -m unittest discover -s tests -p test_unit_image_pole_flags.py -v
```

`verify.py --write` regenerates
`results/unit-image-pole-flags-2026-10-23/controls.json`. The controls
reconstruct the original six-factor source, check24 minimum-rank slices
in eight four-dimensional rulings, exhibit ranks20 and32 when the
relevant fixed-factor conditions are broken, verify four full row-contraction
factorizations, the strict principal-rank gap window and four sharp
unit/slice rank budgets, and retain a rank16 slice
with retained block rank4 at the rank106 boundary. This survivor does
not assert compatibility of the frames with a source unit trajectory.

The prior written source rank loci and Grothendieck's external splitting
theorem retain their credit and hypotheses in proof.md and sources.json.
The finite tests do not prove all formal coefficients, exclude the
remaining unit-image ranks, construct a target, or improve the exponent.

An abstract Gaussian control isolates one rank-one polar term whose raw
negative coefficients have ranks1,2,3. It prevents interpreting the formal
rank-one term as a rank-one assertion for every individual coefficient.
