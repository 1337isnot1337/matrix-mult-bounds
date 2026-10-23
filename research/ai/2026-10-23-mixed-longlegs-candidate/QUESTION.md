# Closed candidate and precise next question

Over the complex numbers, the canonical source

\[
S=10\,\mathrm{Full}_{5,10}
\]

cannot degenerate to

\[
T=7\,\mathrm{Full}_{5,2}+10\,\mathrm{Full}_{5,3}
+4\,O_{3,3}+2\,O_{4,2}+6\,\mathrm{Mid}_{5,2}.
\]

The [global RNC proof](global_rnc_obstruction.md) covers arbitrary
independent invertible first identifications of every target block,
arbitrary poles and singular leading maps, and arbitrary long-leg mixing.
The source copies must share their canonical first identification.
Both endpoints have format(5,100,140). Their literal coefficients remain
fixed by discovery_input.json and verify.py.

Every ordinary Koszul degree on all three legs, both symmetric-power
families, the quantum/upper support bounds and the stated Schur family
pass. They do not detect the geometric obstruction. The canonical target
has ordinary, smoothable and cactus rank178, as proved in cactus_rank.md.
Its border rank remains unresolved: excluding this particular rank140
source orbit does not exclude the whole border-rank140 locus.

## Next question

Find a score-improving source-target proposal that escapes the finite
union of quartics in the first projection of rank-one third slices.
A width-one Full block has the whole first projective space as its
projection. Determine how many such blocks are required, then certify
whether a target with those blocks can satisfy dimension balance, the
shared-A Koszul inequalities and strict formal-score improvement.
Consider changing the source width or target structure if this format
cannot meet those requirements. Independent first identifications in
the source are also outside the current theorem and need separate work.

A surviving profile still requires actual Laurent maps or a complete
orbit-closure construction. A degeneration by itself would require a
further full algorithmic implication before any improved exponent claim.
The historical candidate question and its initial validation are pinned
at public commit79b23815c68cef6c013d4ba54ae37d4d068ae712.
