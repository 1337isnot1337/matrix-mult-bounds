# Quadratic-z middle-polynomial rank continuation

Research checkpoint: October 23, 2026. Source main snapshot `bd03b9dadba03b1089595f03ff7a091ee9e7ddbc`.

Selected question: for the maintained literal `R_(a,b)`, classify the rank of `alpha+z*v(x)+gamma*z^2` with nonzero constant outer coefficients over every field. This is a genuinely quadratic-in-z three-term recurrence, disjoint from PR209's affine-in-z classification, PR207's diagonal-polynomial Toeplitz family, and PR208's geometric diagonal subfamily. PR209 at `4247f42eeb305163d299f908144b5915d1c238c5` suggested the broader quadratic recurrence; the complete row-polynomial reduction used here explicitly credits that prior work.

Accepted result: the written all-field rank identity `ab+min(b,ceil(a/2)*d)+min(b,floor(a/2)*d)`, `d=deg v` (or zero for v=0). The proof parametrizes every polynomial solution by two central entries and establishes the exact maximum-degree filtration. Two finite exact acceptance backends agree. This is a one-slice formula, not an exponent claim. Claim `AI-QUADRATIC-Z-MIDDLE-RANK-001` is `proof-written-unreviewed`; `independent_review=false`, `lean_formalized=false`, `improves_omega=false`.

Reproduce from the repository root:

- `python -I research/ai/2026-10-23-quadratic-z-middle/verify.py` (580 exhaustive prime-field coefficient cases; 960 seeded cases; 135 degree-spectrum witnesses; 940 explicit polynomial null vectors in the spectrum cases; all pass).
- `python -I research/ai/2026-10-23-quadratic-z-middle/verify_charzero.py` (36 separately built characteristic-zero instances, with exact 105 rational null vectors and rank-lower certificates over F_1000003; all pass).
- `python -m unittest discover -s tests -p 'test_quadratic_z_middle_ranks.py' -v` (focused regression and deliberately invalid zero-matrix check).

The exact saved summary is `results/quadratic-z-middle-2026-10-23/validation.json`. The verifiers are independent implementations in the same generating session, not independent mathematical peer review. Project-wide regression, all five historical replays, and current-head hosted CI must be checked before merge. Do not assert them as completed without receipts.

Remaining mathematical bottleneck: classify degree-filtered polynomial solutions when the two outer coefficients are general nonconstant polynomials. Specifically, express the two minimal syzygy degrees in terms of polynomial matrix reduction, and find equal-degree triples with distinct exact ranks if coefficient degrees are insufficient. Source-to-matrix-target implications still require explicit compatible maps on all three legs and a rigorous exponent bridge. Avoid new claims based on finite rank tests alone.

Archived `research/ai/2026-10-20/` and `research/ai/2026-10-20-session2/` must stay byte-for-byte unchanged. Other research workers retain ownership of their respective active PRs.
