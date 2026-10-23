# One-sided partial-unit regularity

**Disposition:** [superseded by stronger concurrent proofs](DISPOSITION.md).
This scoped derivation is retained on a closed unmerged branch.

The [written proof](proof.md) improves the regular unit-image threshold
for the canonical A4 to M(10,10,11) degeneration chart from 109 to 107.
It retains the hypotheses of a regular full-rank long map and a regular
source lift of the target identity. Every finite Laurent pole order is
covered. Unit-image rank at most 106, singular long-leg limits and polar
identity lifts remain open.

The changes are the one-sided target loss `nu-e` and the full-column
source kernel bound `dim(A)-mu_B+k`. The prior two-sided target loss was
`nu-2e` and its compressed source kernel bound used `q=k+e` instead of
`k=N-R`. At image rank 107 the new strict margins are 1, 3, 2.

Run from the repository root with the maintained dependencies:

```sh
python research/ai/2026-10-23-one-sided-unit-image/verify.py
python -m unittest discover -s tests -p test_one_sided_unit_image.py -v
```

`verify.py --write` regenerates the finite exact controls at
`results/one-sided-unit-image-2026-10-23/controls.json`. Verification checks
three pinned prior source files, five A4 rank cases, five genuine target
column-compression controls, five full-versus-compressed source kernel
controls, six sharp three-part source rank budgets and six Laurent product
controls distinguishing raw coefficients from regularized limits.

These are finite matrix checks supporting an unreviewed formal argument.
They do not enumerate tensor degenerations, formalize the all-order proof,
construct a matrix target, or establish a smaller exponent.
