# Uniform mixed-axis normal reduction

Claim `AI-MIXED-AXIS-REDUCTION-091` is written and unreviewed. At b=1 and
for every complex a and nonzero t, a C first space containing m+t*d0
opposite the full B seven-frame has a complete32-dimensional initial
normal kernel. After four plane directions are removed, exact projection
minors force every target-admissible normal into a10-dimensional family.
That family remains unresolved; no full axis exclusion or exponent gain
is claimed.

The certificate uses a rank minor t^18, a complete Laurent kernel,
stable row combinations, and two rounds of square minors. Every pivot
division is by a nonzero rational multiple of a t power. This retains
all exceptional a values without numerical sampling.

From the repository root with the root requirements:

```sh
python research/ai/2026-10-21-mixed-axis-family/verify.py --output results/local/mixed-axis-family.json
python -m unittest discover -s tests -p test_mixed_axis_family.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

`certificate.json` stores replay witnesses, not discovery-cache paths.
The maintained verifier reconstructs its source matrices. See
[proof.md](proof.md), [QUESTION.md](QUESTION.md), and [sources.json](sources.json).
