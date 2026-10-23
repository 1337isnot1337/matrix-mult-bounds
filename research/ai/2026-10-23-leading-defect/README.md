# An all-order defect gap for the two singular A4 long maps

The [written proof](proof.md) excludes every A4 to M(10,10,11) formal
candidate whose two scalar-balanced long-map leading ranks sum to more
than204. Equivalently, their total source defect d must be at least20.
Every finite pole order is covered. No assumption is made on the lift
of a target identity.

For20<=d<=27 the leading first-map coefficient has linear-map rank
between10 and16, and its image has one fixed coherent middle Hankel
factor. For28<=d<=31, the coherent factor and upper bound16 still hold.
Defects at least20, the full target and an exponent below9/4 remain open.

The numerical204 corollary is subsumed by the separate written176
bound in [PR129](https://github.com/1337isnot1337/matrix-mult-bounds/pull/129),
if that package is accepted. This package retains a general invertible
leading-kernel lemma for square matrix targets and an alternative A4
argument;204 is not the strongest proposed frontier. See the comparison
and exact peer commit in proof.md. No peer replay or independent review
is claimed here.

The new argument uses an invertible target parameter in the kernel of
the leading first map. The regular right-inverse correction then forces
every leading source slice to have rank at most2+min(q_B,q_C). Flanders's
bounded-rank dimension theorem and the prior source gap above rank16
supply the contradiction for d<20. Both external inputs and predecessor
credit are explicit in the [source record](sources.json).

Claims `AI-A4-LEADING-DEFECT-001` and
`AI-A4-INVERTIBLE-LEADING-KERNEL-002` are **written and unreviewed**.
This is a necessary full-source reduction, separate from the conic jets.
All continuation work is owner-directed OpenAI Codex work, without
independent mathematical review, formalization or a priority claim.

With the root requirements installed, run from the repository root:

```sh
python research/ai/2026-10-23-leading-defect/verify.py
python -m unittest discover -s tests -p test_leading_defect.py -v
```

The frozen report is `results/leading-defect-2026-10-23/controls.json`.
Eleven sparse long-map examples have total leading defect16 and satisfy
the leading negative equation. Their constant output has rank12 and
cannot extend to a target, by the all-order proof. Deleted coordinates
and those restored at degree one encode the maps exactly; every other
retained coordinate has coefficient one. The invertible trace-kernel
parameter exposes a correction-rank violation in every example.

Two exact literal source controls check all25088 source coefficients
and ranks16 and20. Nine dimension controls record the strict Flanders
margin and singular-kernel equality examples. Twelve synthetic matrix
sources verify116 complete Laurent basis identities with an invertible
leading-kernel parameter. Their minimum source rank is one; they calibrate
the general lemma without satisfying the A4 source hypotheses. These controls do
not formalize arbitrary series. Regenerate with `--write`, then replay
without it. Tests reject false completion, changed rank bounds and
corrupted source pins or external-source attribution.
