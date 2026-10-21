# C29 one-source route checkpoint

Branch: research/c29-rectangular-20261020. Source main: 094fed4.
PR #26 integrated the size-ten proof, and its branch was removed after
verifying the exact merged tree. The present followup extends to unequal shapes.

Current result: the injective-pair-map construction with strict vertex
potentials cannot pass the usual C29:C4 one-source degree-sum gate at any
positive exponent <=9/4. This written argument is unreviewed. General
complex degenerations, extraction from powers, and a better source cost
remain outside its scope. The arithmetic exponent has not improved.

Evidence: rectangular_note.md, source_frontier.py, fiber_frontier.py,
rectangular_gluing.py, and results/c29-near-capacity-2026-10-20/.
All 512 sorted shapes are screened. The only three rank-locus survivors
are (9,9,11), (9,10,10), and (10,10,10); all three now fail within the
stated construction class. Unequal cases cover 48+392 local configurations.
The four focused rectangular tests passed with complete frontier replay.

Next distinct construction route: leave this source and construction class.
A separate abelian-normal-coset Koszul proof is being prepared for the F8
variable-plane family; do not repeat that search without inspecting its status.
