# Unequal F8 target continuation

Branch: research/f8-unequal-graphs-20261020. Refreshed through main48bd72d.
Goal: an actual arithmetic exponent below 9/4; still incomplete.

PR #31 closes every balanced size-nineteen coordinate-potential target in
F8^2:C7. General complex degenerations and smaller unequal targets remain
open. The exact source-degree/rank-locus pilot leaves 26 sorted shapes;
in particular (16,16,26) passes those necessary tests. No target is constructed.

The higher seven-slice bound now excludes all (16,16,26) count patterns:
520710 class pairs have minimum maximum weight345, so the third-family
average is8970/7>1280. The proof and exact standard-library replay are
in research_note.md and pair_averaging.py. This is written and unreviewed.

Current precise question: can the surviving (16,20,21) count pattern in
count-survivor-16-20-21.json be lifted to actual vertex families and a
strict potential? Two nonlinear graph pilots found no construction:
generic is untraced UNSAT, dual timed out. Their base frames and graph
ansatz are restricted; neither report is a nonexistence proof. A small
(4,4,3) positive control is fully verified and does not pass the degree gate.

Keep general rank inequalities attributed to their classical sources.
Do not restart the closed balanced size-nineteen search. Preserve the
archived research paths and use the existing root requirements for checks.
