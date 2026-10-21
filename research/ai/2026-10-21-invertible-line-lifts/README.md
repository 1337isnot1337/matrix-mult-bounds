# Lifting the invertible mixed lines

Exact finite linear and polynomial calculations, unreviewed, October 21,
2026. The matrix-multiplication exponent remains unchanged.

For the retained invertible first-line seed, the target's required zero
projected third coefficient removes 32 of the 72 normal directions,
leaving **40**. This includes sixteen pure-B directions, sixteen pure-C
directions, and four common-plane motions. Their span has dimension 36;
we select four complementary coupled directions for construction work.
This is a vector-space decomposition, not a nonlinear gauge reduction.

The [calculation note](calculation.md) fixes a 36-direction ansatz using
the two pure spaces and the selected complement, with second new rows
set to zero. The existence of second leading-row and third new-row
corrections is exactly equivalent to sixteen quadratic equations. They
couple only the pure-B and pure-C parameters. Third leading-row equations
and later coefficients are separate conditions and remain to solve.

A retained compatible control has uncorrected first rank 13 at t=1,
so the correction problem includes growth beyond the rank-12 seed.
Neither compatibility nor this finite rank supplies the required
100-dimensional target slice space or 110-dimensional output legs.

```sh
python research/ai/2026-10-21-invertible-line-lifts/normal_space.py \
  --output results/local/invertible-normal-space.json
python research/ai/2026-10-21-invertible-line-lifts/quadratic.py \
  --output results/local/invertible-quadratic-compatibility.json
python -m unittest discover -s tests -p 'test_invertible_line_lifts.py' -v
```

The frozen reports retain complete bases and coefficient lists, not
sampled parameter assertions. Source pins are in `sources.json`.
These checks are from the generating session and do not provide
independent mathematical review or formalization.
