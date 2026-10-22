# Discovery limits

These deterministic pilots are separate from the accepted certificate.
They use the existing `/tmp/matrix-entropy-venv/bin/python` environment,
including optional NumPy 2.5.4 and SciPy 1.18.1. No floating-point result supplies a
target map, an exclusion, or a claim of an optimal filtration.

Run from this repository's root, in order:

```sh
python research/ai/2026-10-21-s5-block-filtration/discovery/peirce.py
python research/ai/2026-10-21-s5-block-filtration/discovery/optimize.py
python research/ai/2026-10-21-s5-block-filtration/discovery/support.py
python research/ai/2026-10-21-s5-block-filtration/discovery/covers.py
```

- `peirce.json` records nine mutually orthogonal binary idempotents summing
  to one and 41 nonzero corners, including their projected radical flags.
  These are discovery data. The maintained `blocks.py` verifier independently
  needs only its central idempotent and the full prior radical certificate.
- `optimizer.json` optimizes the coarser corner/Loewy support majorant with
  18 variables and 64 constraints. Its principal-block value is approximately
  78.524952. This is a numerical upper-bound candidate, not an optimum proof.
- `support.json` expands all 88^3 principal-block trace positions, finding
  1,198 nonzero entries. The 19 variable types give 52 distinct symmetric
  constraints. Numerical optimization gives approximately 78.457585. The
  resulting small change supplies no additional integer target exclusion
  in the reported frontier. The accepted theorem uses the simpler exact
  rational principal bound 78.5437 and does not rely on these data.
- `A5-radical.json` and `SL(2,5)-radical.json` save the alternate-source
  power-span pilots. The uniform all-algebra layer estimates are about
  59.759643 and 119.366441, respectively, and do not exclude their selected
  improving target gates. No independent replay of these alternate-source
  certificates is claimed. Blockwise or other filtrations there remain
  open questions.

Each numerical optimizer uses its script's recorded bounds, initial point,
tolerance and iteration limit, without a random seed. Saved weights can
vary with the SciPy version; they are not acceptance decisions. The accepted
block ranks and rational inequalities require only the root verification
dependencies and do not import these scripts.
