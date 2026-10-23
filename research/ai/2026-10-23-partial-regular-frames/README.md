# Partial regular frames in the full Laurent target problem

The [written proof](proof.md) shows that A4 cannot degenerate to
M(10,10,11) if it has partial regular source frames of dimension109
as specified below. All other map coefficients may have finite poles.
This strengthens the separate PR105 regular-unit-image argument.

In a unit-free formulation, suppose constant 110-by109 injections H,J
and regular 112-by109 matrices V,U satisfy `C H=V`, `B U=J`, with U(0)
and V(0) of rank109. The complete source contraction minima and target
dimensions force B, then F, then C to be regular. The existing ordinary
rank contradiction12>11 rules out the target.

For a target identity, write S for its source slice. It suffices instead
that `C H` and `S C H` are regular with rank109 limits for some constant
H. The rest of C and S may have poles. The unit equation provides the
partial right inverse after regular target normalization.

These partial frames are **hypotheses**. Their existence for arbitrary
degenerations is unproved. The written result is unreviewed and supplies
no matrix construction or exponent improvement. Rank108 remains outside
the strict dimension argument. The proof credits the original source
rank minimum and the predecessor Laurent and projection lemmas; the new
column-contraction step and frame formulation are owner-directed Codex work.

```sh
python research/ai/2026-10-23-partial-regular-frames/verify.py
python -m unittest discover -s tests -p test_partial_regular_frames.py -v
```

Run from the root with its requirements installed. The verifier replays
the predecessor controls, four independent-target-frame examples, twelve
polar unit/long-map examples, twelve column-kernel examples and three A4
rank margins. The polar examples satisfy the frame and unit identities
without the strong source rank hypotheses, so they illustrate the weaker
chart assumptions and are not target constructions. The column-kernel
examples attain the dimension bound and show why equality gives no
contradiction. Tests reject corrupted pins, erased poles, an accidental
identification of the two target frames and a false rank108 exclusion.

Finite controls do not formalize the all-order proof. Claims:
`AI-PARTIAL-FRAME-REGULARITY-001`, `AI-A4-PARTIAL-FRAME-EXCLUSION-002`.
