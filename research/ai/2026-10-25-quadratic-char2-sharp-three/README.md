# Sharp characteristic-two quadratic dimension bound

Claim `AI-CHAR2-QUADRATIC-SHARP-THREE-001` is **proof-written-unreviewed**.

Over every field of characteristic two, the maximum dimension of a linear
coefficient family with geometric source rank at most fourteen and
coefficient determinant not identically zero is **three**. The upper bound
is proved here; the pinned universal three-plane supplies sharpness over the
ground field. This does not classify all attaining three-spaces. Outside
characteristic two, the existing interval remains [3,4].

[proof.md](proof.md) includes the singular-three-space classification,
its alternating exception, all three kernel orbits, both middle-kernel
rank cases, and the compression reductions. The adjugate identity excludes
the primitive alternating type. [sources.json](sources.json) preserves exact
published dependencies and discovery hashes; no scratch file is needed.

From the repository root with the maintained requirements installed:

```sh
python research/ai/2026-10-25-quadratic-char2-sharp-three/verify.py
python -m unittest discover -s tests -p 'test_quadratic_char2_sharp_three.py' -v
```

The saved exact output is
[controls.json](../../../results/quadratic-char2-sharp-three-2026-10-25/controls.json).
The verifier checks algebraic identities and obstruction coefficients.
It does not certify the geometric proof by computation. Tests retain the
rank-one three-space that invalidates an unconditional rank-two assumption,
check its separate extension obstruction, and reject missing adjugate and
quartic terms. The frozen earlier proofs and reports remain unchanged.

Same-session algebra auditing is not independent mathematical review.
No historical-priority claim, formalization, tensor target, or exponent
improvement is asserted. Next questions include the odd-characteristic
three-versus-four gap and classification of attaining three-spaces.
