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
python research/ai/2026-10-23-monomial-projections/verify.py --alphabet-size 2 --max-sum 9 --output results/monomial-projections-2026-10-23/binary-sum9.json
python research/ai/2026-10-23-monomial-projections/verify.py --alphabet-size 3 --max-sum 8 --output results/monomial-projections-2026-10-23/ternary-sum8.json
```

All three ordered censuses are complete:

| Alphabet | a+b cutoff | Candidates | Strictly strengthened scores | Maximum ratio | Exact violations |
| --- | ---: | ---: | ---: | ---: | ---: |
| Binary | 8 | 1,623 | 581 | 1 | 0 |
| Binary | 9 | 4,197 | 1,817 | 1 | 0 |
| Ternary | 8 | 24,699 | 6,486 | 1 | 0 |

The scopes overlap and must not be added as distinct support counts.
All nine retained records (best, first improvement, worked example in each
report) replay after JSON serialization, and each ordered count agrees with
the independent formula. No strengthened score exceeds the source profile.
Four focused tests pass, including the exhaustive 64-support mask comparison,
the 190-candidate small census (35 strict gains), rejection of corrupted
terms/scores/masks and replay with the optimizer disabled.

Claims `AI-MONOMIAL-PROJECTION-OPT-001` and
`EXP-MONOMIAL-PROJECTION-CENSUS-001` separate the written, unreviewed finite
recurrence from the finite search outcome. Full regression and hosted CI
remain pending. No independent review, formalization or exponent improvement
is claimed.
