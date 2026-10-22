# S5 block and Peirce filtrations

Question selected on October 21, 2026: does separating the modular blocks
and primitive-idempotent corners of F2[S5] strengthen the existing modular
slice-rank bound enough to exclude coordinate/potential constructions of
M(13,14,14) in S5 x C2, or the related central-extension targets?

Base: main 00d51337. Worktree: /tmp/matrix-s5-block-filtration.
Branch: research/s5-block-filtration-20261021.

Reuse the exact S5 group, binary representations, and certified radical
powers from ../2026-10-21-s5-split/ with their existing attribution. This
investigation is separate from the native-parity, commuting-trade, scalar-
repair and geometric boundary-chart work on other branches.

Intended output: exact binary block/corner certificates, a self-contained
counting argument for any improved bound, and an honest comparison with
the finite targets. Numerical optimization is discovery only. No source
degeneration, exponent improvement, optimal filtration, or independent
mathematical review is currently claimed.

Completed local result: proof.md and the exact central-idempotent certificate
give a modular upper bound below 389 for S5 x C2^2. It excludes the coordinate
M20 and M(19,20,21) targets despite their passing all the existing complex
rank-locus and full Koszul tests. The M19 and one-factor M(13,14,14) targets
remain open. Four focused tests passed in 19.616 seconds; broader checks and
the topic PR are still pending. All proofs remain written and unreviewed.

Discovery limits: the full Peirce trace-support optimization improved the
88-block estimate only slightly and supplied no extra target exclusion.
Uniform radical pilots for A5 and SL(2,5) also supplied no target exclusion.
These numerical pilots are retained as discovery data, not accepted proofs.

Environment: /tmp/matrix-entropy-venv/bin/python. Free disk at task start
was about 823 MB; avoid large dependencies and generated artifacts.
