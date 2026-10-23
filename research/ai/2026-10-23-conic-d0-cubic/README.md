# d=0 cubic-conic fiber

The PR101 two-jet at `c=d=0` already extends to an exact polynomial curve
for every complex `a,b`:

```text
B(t) = B0 + t*B1 + t^2*B2
C(t) = C0 + t*C1
```

The only new `B2` entries are the eight listed in [the proof](proof.md);
`C2=0`. The literal source contraction has zero kernel block at every
power of `t`, with no moving source-row correction. This closes the `d=0`
fiber for this fixed first jet. It does not settle the generic `d!=0`
all-order problem or the full matrix target.

The discovery elimination includes all seventy second-tangent fields, but
the independent acceptance verifier relies only on the explicit maps and
the original source identities.

Run the verifier and focused test from the repository root:

```sh
python research/ai/2026-10-23-conic-d0-cubic/verify.py
python -m unittest discover -s tests -p 'test_conic_d0_exact_curve.py' -v
```

See [QUESTION.md](QUESTION.md), [proof.md](proof.md), and the exact matrices
in `results/conic-d0-cubic-2026-10-23/exact-curve.json`.
