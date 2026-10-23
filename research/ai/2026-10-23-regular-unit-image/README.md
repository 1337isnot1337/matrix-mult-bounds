# Partial regular unit images in the A4 Laurent problem

The [written proof](proof.md) excludes A4 to M(10,10,11) at every finite
Laurent order when one long map C is regular with full-rank limit, the
lift of the target identity is regular, and `rank(S(0) C(0))>=109`.
The limiting source-unit slice S(0) may be singular. In particular this
includes every such unit of corank at most one, extending the previous
invertible-unit chart.

The general result first forces both remaining maps to be regular under
three explicit source/target rank margins. It selects independent unit
columns, completes independent source row and column frames, and varies
the target left inverse. Recovering the entire long map needs only e+1
left inverses when e target directions were dropped. The existing
ordinary A4 rank obstruction then supplies the contradiction.

The proof is **written and unreviewed**. There is no general singular-map
exclusion, independent review, formalization, matrix construction or
smaller exponent. Rank-108 unit images, singular long-leg limits and polar
unit lifts remain open. This is a full-source Laurent argument, separate
from the fourteen-row conic incidence problem.

Read [the registered question](QUESTION.md) and [predecessor pins](sources.json).
All work was prepared with OpenAI Codex under the owner's direction. The
previous source rank minimum, ordinary obstruction and normalized Laurent
lemma retain their original credit. No additional external theorem is used.

From the repository root with root requirements installed:

```sh
python research/ai/2026-10-23-regular-unit-image/verify.py
python -m unittest discover -s tests -p test_regular_unit_image.py -v
```

The verifier checks sixteen projection-recovery families, eight sharp
rank-budget matrices, four regularized-product controls, four singular
unit examples and three A4 rank-margin cases. The singular examples show
why a single compressed projection can hide a pole if the other source
hypotheses are absent. The regularized-product examples distinguish a
leading coefficient of a regularized product from a raw constant
coefficient with uncancelled poles. Tests reject corrupted predecessor
pins, a false rank-108 exclusion, altered recovery data and an inflated
proof status or exponent claim.

The controls use exact rational/symbolic arithmetic. They check the finite
linear algebra supporting the proof; they do not formalize its all-order
quantifiers. The frozen report is
`results/regular-unit-image-2026-10-23/controls.json`. Regeneration with
`verify.py --write` must be followed by replay without that flag.

Claims: `AI-PARTIAL-UNIT-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-EXCLUSION-002`.

Local regression at `8168c3813dd7c57ab0b2a78084c19472425f3111`
completed849 tests:846 passed and3 optional controls skipped. All five
historical archive replays passed. The dated result directory contains
the exact commit/tree receipt and compressed logs. This evidence does
not change the mathematical review status; hosted CI checks the final
PR head separately.

Concurrent [PR103](https://github.com/1337isnot1337/matrix-mult-bounds/pull/103)
studies a fixed square-zero resolvent with a rank16 limiting unit and
constant compression. Its open-locus obstruction is separate from this
rank109 unit-image criterion and retains its own credit.
