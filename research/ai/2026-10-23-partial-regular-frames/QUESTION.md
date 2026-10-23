# Can partial regular frames force every Laurent map to be regular?

Predecessor: the partial-unit-image argument of PR105, developed at
`8168c3813dd7c57ab0b2a78084c19472425f3111`. It assumes an entirely regular
long map and regular target-unit lift.

New question: for the A4 target, do 109 regular independent columns of
the long map, together with 109 regular independent columns of its unit
image, suffice even when the other coefficients of both maps have poles?

Proposed mechanism: normalize the target unit, use the two partial source
frames to force the opposite long map to be regular, and then force the
first map to be regular using rank loss. Finally use the third source
leg's minimum contraction rank to eliminate poles in the remaining long
map. The new final step needs a fourth strict rank margin.

Intended output: a general regular-frame lemma with no target-unit
hypothesis, its unit-image corollary, exact controls and an explicit
escape boundary. Preserve PR105 as a separate reviewable predecessor.

The simultaneous existence of these frames is a hypothesis to verify,
not an automatic consequence of a degeneration. There is no full target
construction or exponent improvement. All work is owner-directed Codex.
