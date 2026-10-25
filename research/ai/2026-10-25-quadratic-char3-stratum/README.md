# Invertible quadratic families in every odd characteristic

The [characteristic-three proof](proof.md) completes the dimension-four upper
bound for geometric rank-at-most-fourteen families in the complete quadratic
R_(3,3) block that contain an invertible coefficient matrix. Together with
the pinned prior result, the bound now holds over **every field of
characteristic different from two**, including characteristic zero.

The new proof uses the two-dimensional radical of the tangent form to force
the direction NQ² into a hypothetical five-space. The integral linear form
from the prior package then makes a cubic determinant coefficient vanish,
forcing a constant Gram ratio. The Frobenius-gradient argument gives the
contradiction. It does not claim tangent rank seven in characteristic three.

An [explicit two-plane](two-plane.md), defined over any odd-characteristic
field containing a square root of -1, has invertible coefficient points and
geometric source rank at most fourteen. A 14-by-14 integer minor equal to16
certifies exact source rank fourteen at its integer basepoint. Over an
algebraically closed field of characteristic different from two, the maximum
dimension among families containing an invertible coefficient matrix is
therefore between **two and four**, inclusive. Sharpness remains
open; this is not an exponent improvement or a compatible tensor construction.

Claims `AI-CHAR3-QUADRATIC-INVERTIBLE-001` and
`AI-QUADRATIC-INVERTIBLE-TWO-PLANE-002` are **proof-written-unreviewed**.
Same-session audit, exact arithmetic and CI do not establish independent review
or formalization. The geometric hypothesis cannot be replaced by checking
only the points of a finite ground field. The two-plane's field-of-definition
qualification does not restrict the upper-bound theorem.

Exact dependencies and discovery inputs are pinned in [sources.json](sources.json).
No new external theorem is imported. From the repository root:

```sh
python research/ai/2026-10-25-quadratic-char3-stratum/verify.py
python -m unittest discover -s tests -p 'test_quadratic_char3_stratum.py' -v
```

The saved report is `results/quadratic-char3-stratum-2026-10-25/controls.json`.
It contains symbolic reductions modulo three, two tangent-rank controls,
Gaussian-integer coefficient identities and the complete basepoint minor.
The full linear-family dimension argument remains a written proof.
