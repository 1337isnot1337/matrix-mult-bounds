# Sharp Hankel index budgets in every degree

The [written proof](proof.md) constructs rectangular constant-rank Hankel
pencils attaining every integer equality in the annihilator degree budget.
Their complete polynomial kernels are explicit over every field.

At the A10 boundary it gives a 10-by-10 pencil of constant rank eight,
with primitive annihilator `z^8-t*z^4+t^2` and both minimal-index lists
equal to `(2,2)`. Thus the prior pencil-linearity argument needs its
strict inequality, even for constant projective rank. This does not
exclude or construct any of the remaining matrix targets or alter the
ordinary frontier. The exponent remains 9/4.

The [linear-extension theorem](extensions.md) then classifies every
linear Hankel space containing the prescribed pencil in characteristic
zero. There is a unique maximal one, of dimension 2epsilon. At A10 it
is exactly the four-space supported at moments 3,7,11,15, with source
ranks zero, four or eight. Thus this seed cannot be held inside a
linear Segre ruling of dimension greater than four.

The [question](QUESTION.md) records the scope. The earlier quadratic
control and the external index sum theorem keep their original credit.
The new family is written and unreviewed; finite exact checks are not
independent mathematical review or formalization.

With the root requirements installed, from the repository root:

```sh
python research/ai/2026-10-23-hankel-index-sharpness/verify.py --output results/hankel-index-sharpness-2026-10-23/controls.json
python research/ai/2026-10-23-hankel-index-sharpness/extensions.py --output results/hankel-index-sharpness-2026-10-23/extensions.json
python -m unittest discover -s tests -p test_hankel_index_sharpness.py -v
python -m unittest discover -s tests -p test_hankel_pencil_extensions.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The next question is whether other saturated quadratic pencils have
different maximal linear extensions, and the dimension of genuinely
bilinear Segre images at that boundary. The extension theorem does not
classify arbitrary quadratic pencils or establish their equivalence
under transformations preserving the Hankel source.
