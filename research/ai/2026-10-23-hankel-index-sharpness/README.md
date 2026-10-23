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

The [question](QUESTION.md) records the scope. The earlier quadratic
control and the external index sum theorem keep their original credit.
The new family is written and unreviewed; finite exact checks are not
independent mathematical review or formalization.

With the root requirements installed, from the repository root:

```sh
python research/ai/2026-10-23-hankel-index-sharpness/verify.py --output results/hankel-index-sharpness-2026-10-23/controls.json
python -m unittest discover -s tests -p test_hankel_index_sharpness.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The next question is the dimension of genuinely bilinear Segre images
with quadratic annihilator maps, rather than an extension of the
linear-annihilator premise by weakening its numerical hypothesis.
