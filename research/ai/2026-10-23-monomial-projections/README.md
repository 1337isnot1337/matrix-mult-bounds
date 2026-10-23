# Stronger scores through nonshared coordinate projections

The [finite recurrence](proof.md) computes the exact maximum of the existing
whole-convolution/slice-fallback component score over all y/z coordinate
projections of a fixed support. This strengthens an estimate on an old
degeneration. It does not claim optimality under general linear restrictions
or produce an exponent improvement. This branch depends on PR187's
recognition package, with its exact source pinned in `sources.json`.

At wx=(0,0,1), wy=(0,0,0), deleting the middle y coordinate raises the score
from 3 to 5, below P_*(3,3)=56/9. Two literal matching components give the
exported witness. Acceptance replays only the masks and support score and
never calls the optimizer. Direct enumeration of all pairs of masks checks
the optimum for all 64 subsets of a 2-by-3 additive support, including empty.

From the repository root:

```sh
python -m unittest discover -s tests -p test_monomial_projections.py -v
python research/ai/2026-10-23-monomial-projections/verify.py --alphabet-size 2 --max-sum 8 --output results/monomial-projections-2026-10-23/binary.json
```

The completed ordered binary census at a+b<=8 contains 1,623 candidates.
Coordinate projection strictly strengthens 581 scores. The maximum ratio
remains exactly one, with no exact violation. The three retained records
(best, first improvement, worked example) replay after JSON serialization.
Four focused tests pass, including the exhaustive 64-support mask comparison,
the 190-candidate small census (35 strict gains), rejection of corrupted
terms/scores/masks and replay with the optimizer disabled.

Claims `AI-MONOMIAL-PROJECTION-OPT-001` and
`EXP-MONOMIAL-PROJECTION-CENSUS-001` separate the written, unreviewed finite
recurrence from the finite search outcome. Full regression and hosted CI
remain pending. No independent review, formalization or exponent improvement
is claimed.
