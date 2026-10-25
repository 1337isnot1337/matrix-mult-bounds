# A common kernel for every singular characteristic-two section

Over every characteristic-two field, a two-dimensional coefficient pencil
with polynomial D=T4=0 has a common right or left kernel over that field.
The proof factors the homogeneous adjugate and uses exact Plucker identities
to exclude two moving linear kernels. No algebraic closure is needed.

Every characteristic-two attaining three-space therefore has a common
kernel in its intrinsic singular two-section. This reduces the remaining
geometric classification to the two non-evaluation kernel cases, without
claiming those cases are classified.

Claim `AI-CHAR2-SINGULAR-PENCIL-KERNEL-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) and [sources.json](sources.json). An exhaustive
GF2 census and a counterexample to pointwise vanishing support the proof;
they do not establish arbitrary-field scope or an exponent improvement.

```sh
python research/ai/2026-10-25-char2-singular-pencil/verify.py
python -m unittest discover -s tests -p 'test_char2_singular_pencil.py' -v
```

The saved report is `results/char2-singular-pencil-2026-10-25/controls.json`.
