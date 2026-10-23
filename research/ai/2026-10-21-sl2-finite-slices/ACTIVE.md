# Actual nonsplit finite-power question

Base `d833eb0`, owned worktree and branch. Open PRs and main refreshed
October 23, 2026; no overlap with the separate conic, F8, boundary,
rectangular or spin investigations. Split-cover PR100 is merged.

Question: can an exact basis of the actual SL(2,F5) tensor, rather than a
degeneration toward A5 x C2, give a useful finite-power slice cover?

First discovery pass: lift the preceding A5 F4 idempotents through the
square-zero central augmentation ideal, lift each basis vector into its
actual Peirce corner, and compute the full nonsplit trace support.
Unverified earlier radical data may guide discovery but is not an
acceptance premise. Any numerical or bounded negative result remains
scoped to the tested basis/weights. No new exclusion is presumed.

Independent standard-library replay confirms a 98-slice full nonsplit
cover and the extra-C2 cube bound 6155844<6426225, giving target volume
<=2481. The retained full regression logs show 844 tests completed,
with three optional skips, and five passing archive replays. A fresh
October 23 replay passes all five focused tests, including corruption
controls. Proof and claim ledger remain written and unreviewed.
Current-commit regression and hosted CI will be recorded before merge.
No exponent improvement.
