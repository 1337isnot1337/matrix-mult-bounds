# Unequal partial frames and the rank106 unit-image chart

The [written all-order proof](proof.md) excludes A4 to M(10,10,11) under
either of two sufficient partial-frame pairs:106/110 and107/109.
The first number is the dimension of a regular right frame for B;
the second is the dimension of regular selected columns of C. A target
identity upgrades the limiting rank of B after B and F become regular.
The full source's column-contraction rank then eliminates C poles.

For unit images, it suffices that `C H` has a regular rank-r_C limit and
`S C K` has a regular rank-r_B limit, with independent constant injections
H,K. The rest of C and the source-unit slice S may have poles.

In particular, for an entirely regular full-rank long map C and regular
unit lift, `rank(S(0) C(0))>=106` is impossible. Every unit of corank at
most four is included. This strengthens the earlier rank109 criterion.
Rank105 is outside these strict bounds; the theorem does not establish
that arbitrary degenerations possess the required frames.

The proofs are **written and unreviewed**. Source rank minima, ordinary
obstructions, and the predecessor partial-frame arguments retain their
credit and exact source pins. The rectangular pole argument and target
unit rank upgrade are owner-directed OpenAI Codex continuations. There
is no independent review, formalization, target construction or exponent
improvement.

```sh
python research/ai/2026-10-23-asymmetric-regular-frames/verify.py
python -m unittest discover -s tests -p test_asymmetric_regular_frames.py -v
```

Use root requirements and run from the repository root. The verifier
replays its predecessor controls and checks all12100 integer pairs in
the registered A4 range, finding nine sufficient pairs and two minimal
pairs. Four exact unit examples verify the rank upgrade while retaining
an unselected pole; eleven corank/alignment examples check the unit-image
rank floor. These examples do not assert the source contraction minima
and are not tensor degenerations to the target. Tests reject corrupted
pins, missing frontier pairs, falsely included equality cases and an
inflated rank105 exclusion. Finite arithmetic supports the written proof
without formalizing its Laurent quantifiers.

Claims: `AI-ASYMMETRIC-FRAME-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-106-002`.
