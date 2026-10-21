# Fixed-parent orbit obstruction

Question: Can arbitrary vertex deletions of the 56-point cubic F8 parent
produce a single strict-coordinate-potential matrix target passing the 9/4
degree-sum gate, including rectangular shapes?

Answer: No, under the written hypotheses. The orbit of an explicit eight-vertex
positive circuit gives a seven-cycle hole inequality. Integer optimization
bounds every such volume by 92,928. The proof is written and unreviewed.

Source main: `843ad78`. Branch: `research/octal-parent-orbit-barrier-20261020`.
The separate variable-plane continuation is PR #21; it uses a different source
and lies outside this obstruction.

Evidence: `parent_barrier.py`, `research_note.md`, and
`results/octal-parent-barrier-2026-10-20/certificate.json`.
The checker covers 10,752 circuits, 43,008 group support relations,
4,782,969 hole cycles, and 185,193 hole-total triples. It uses only the
standard library. No claim of general degeneration nonexistence is made.

Next construction question: leave this parent. Independent fiber directions
in F8^2:C7 remain open; a timed-out discovery query is not an exclusion.
The current best exponent remains 9/4.
