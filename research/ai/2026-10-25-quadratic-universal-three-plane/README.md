# An invertible quadratic three-plane over every field

The [proof](proof.md) gives M(x,y,z)=[[x,x,0],[0,y,0],[0,z,z]]. Its coefficient
determinant is xyz; its full quadratic source determinant vanishes identically.
A symbolic14-minor is -x^6*y^3*z^5, so every invertible coefficient point has
source rank exactly fourteen in every characteristic. The basepoint minor
is -1, giving an integer certificate without exceptional primes or a
field-extension assumption.

The proof also shows this particular three-plane is inclusion maximal in
every characteristic: it has no fourth direction preserving geometric source
rank at most fourteen. This scoped result does not exclude other four-spaces.

This raises the lower bound on the maximum dimension among geometric
rank-at-most-fourteen families containing invertible coefficient points to
three. Together with the pinned previous upper bounds the interval is [3,4]
outside characteristic two and [3,5] in characteristic two. Dimension-four
sharpness and the characteristic-two upper bound remain open. Singular
six-dimensional families still exist.

Claim `AI-QUADRATIC-UNIVERSAL-THREE-PLANE-001` is **proof-written-unreviewed**.
Exact polynomial identities, same-session audit and CI are not independent
review or formalization. No compatible tensor map or exponent improvement
is established. The [source record](sources.json) retains exact dependencies,
discovery pins and the corrected initial integer-sign mistake.

From the repository root:

```sh
python research/ai/2026-10-25-quadratic-universal-three-plane/verify.py
python -m unittest discover -s tests -p 'test_quadratic_universal_three_plane.py' -v
```

The retained report is
`results/quadratic-universal-three-plane-2026-10-25/controls.json`.
