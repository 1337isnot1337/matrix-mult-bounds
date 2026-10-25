# Characteristic-two attainers with a common evaluation kernel

Over an algebraically closed field of characteristic two, every attaining
three-space whose singular section has a common evaluation-conic kernel
(or left kernel) is equivalent to one of the two known universal planes:

    [[t,x,0],[0,t,x],[0,y,0]],
    [[x,x,0],[0,y,0],[0,z,z]].

The two normalized first-column charts are classified over their ground
field, using explicit shears. Arbitrary ground-field forms and families
outside this evaluation-kernel locus remain open.

Claim `AI-CHAR2-EVALUATION-KERNEL-ATTAINERS-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) and [sources.json](sources.json). Exact coefficient
checks and same-session auditing do not establish independent review or
an exponent improvement.

From the repository root:

```sh
python research/ai/2026-10-25-char2-evaluation-kernel/verify.py
python -m unittest discover -s tests -p 'test_char2_evaluation_kernel.py' -v
```

Report: `results/char2-evaluation-kernel-2026-10-25/controls.json`.
