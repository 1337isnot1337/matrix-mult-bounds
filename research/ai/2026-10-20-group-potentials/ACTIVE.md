# Continued exponent campaign

Goal: prove a complete arithmetic exponent strictly below 9/4. The owner
requested sustained work without stopping at a partial checkpoint. The
active goal remains incomplete; no smaller exponent is established.

Current branch: research/normal-coset-koszul-20261020, from main 4289a7b.
Root checkout: /home/user/matrix-mult-bounds. A separate worktree at
/tmp/matrix-c29 owns PR #29, the complete unequal C29 coordinate-potential
frontier. Respect other workers' constructive-spectrum and SL2 source work.

Completed integrations: PR #21 variable-plane infrastructure; #22 fixed
cubic F8 parent orbit-hole obstruction; #24 fixed-base one-plane frontier;
#26 C29 size-ten classification and obstruction. Their fully incorporated
branches were removed after exact merged-tree verification. None proves
an exponent improvement. PR #29 extends the C29 obstruction to unequal
single targets in the stated construction and source-cost model.

Current structural result: the identity-quotient restriction to an abelian
normal subgroup has rank |H|. A classical three-slice Koszul inequality
requires 3 sum k_a^2 - number(k_a=1) <=2|H| for common-fiber square minima.
The new note in ../2026-10-20-normal-coset-koszul/ gives the proof, explicit
integer matrices and complete finite count checks. Written and unreviewed.

This closes ALL source448 size-nineteen targets with maximum fiber size
three, including variable planes and all offsets. Normal-fiber unique sums
also force every size-nineteen F2^6 fiber to have size at most four. With all
fibers >=2, exactly 1,566 count-pattern triples survive the new necessary
screen; they require four-point fibers in at least two families. Their
normal directions, offsets and strict potentials are unconstructed.
The same argument closes every source192 size-twelve coordinate target
and rules out source C31:C6 candidates having all fibers >=2.

Next precise construction question: source448 size nineteen with four-point
normal fibers. Test the surviving count patterns with full affine planes,
three-point triangles, and two-point short directions. Check local pair
packing before global offsets. A promising local pattern is not a witness;
accept only complete source support and exact integer potential verification.
Patterns with zero/one-point fibers and general changes of basis remain open.

Historical work and exact status:
- ../2026-10-20-full-filtration/: balanced optimistic entropy gap39/40;
  no weighted extraction theorem.
- rank_locus_proof.md: general complex group-degeneration necessary test;
  source SL2(5) to M10 remains open.
- octal_research.md: earlier direction, offset and parent searches with
  exact rejection circuits and honest timeout/untraced-UNSAT boundaries.
- ../2026-10-20-c29-near-capacity/: near-capacity normal classification and
  scoped coordinate-potential exclusions; general degeneration remains open.

Use /tmp/matrix-entropy-venv/bin/python. Exact maintained certificates need
only the standard library plus the root verification requirements. Optional
SAT/LP discovery packages are already installed. Four CPU cores; check disk
before large runs. Required CI now runs normally. Use topic PRs, wait for
current CI and resolve discussions, then merge and clean fully merged refs.
