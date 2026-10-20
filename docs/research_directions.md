# Research directions

These are proposed investigations, not claimed results. Each task has a concrete output and an explicit path to a downstream claim.

## R1: Review the local sharpness theorem

Status: open. Review the full all-integer proof, especially positivity of increments, the limiting slope, and the join at $a=b$. Distinguish the earlier recurrence from the local matching construction.

Deliver a proof review tied to a commit, a corrected proof, or a counterexample. A finite grid extension alone does not close this task. A Lean formalization is a separate deliverable, not a prerequisite for every discovery.

## R2: Decide compatibility with the product-filtration family

Status: resolved by written, unreviewed all-size proofs at `73b2d20` and
`712c91a`; see [the pinned review](concurrent_research.md) and the
[local concavity proof](../research/ai/2026-10-20-affine-direct-sums/research_note.md).
Every fixed-i, fixed-j and fixed-k family preserves P_* for all positive
integer parameters. The stronger equivalence result includes the necessary
zero-boundary concavity condition. The archived finite grid is unchanged.

The proof does not cover full direct sums with distinct labels on all three
legs. Such extractions and oriented character constraints remain candidates
for R3/R5. The next task must use additional tensor information; extending
the completed fixed-label grid cannot produce a smaller exponent.

## R3: Search outside identical single-source sectors

Status: open. The flattening obstruction closes only shorter single-convolution sources with identical targets and the stated shared leg.

Update, October 20: [closed Koszul rank formulas](../research/ai/2026-10-20-koszul/research_note.md)
reject all 85 saved second-pass packings, including the former optimum. Use
these necessary tests before trying to realize another packing. They do not
exclude all alternatives or establish sufficiency.

The [four-dimensional mixed family](../research/ai/2026-10-20-koszul/research_note.md#6-an-all-size-family-that-these-necessary-tests-do-not-exclude)
survives all three full-space Koszul families and beats P_* for k>=53. Its
canonical target has a border-rank certificate, while the coordinate-weight
source ansatz is excluded by B>=12k-1. Determine its degeneration status under
general basis changes. Passing the rank screens is not a construction; a finite
model refutation still needs a growth argument.

The [all-dimension extension](../research/ai/2026-10-20-koszul/all_dimension_targets.md)
supplies that growth argument for a specific unbounded sequence: realizing its
targets with source overhead below 2.04721048 percent would force omega<9/4.
No such sequence is constructed. The coordinate-weight ansatz has an all-size
50 percent asymptotic overhead obstruction; investigate general bases or a
different construction.

Investigate unequal sectors, tensor-product sources, or explicit basis changes. State all source and target leg dimensions. Certify the resulting coefficient identities or degeneration weights exactly. Account for any auxiliary tensor rather than cancelling it without justification.

The initial monomial search omits arbitrary basis changes and uses weak estimates for unrecognized sectors. Stronger block recognition is a concrete computational task. Record whether a new score comes from a new degeneration or from a stronger estimate on an old sector.

## R4: Establish a uniform gain or an alternative growth mechanism

Status: open. The target $P(a,4a-1)\ge(3+\eta)P(a,a)$ with a character-independent $\eta>0$ is sufficient for improvement. It is not necessary, and it is not proved.

The [completed analytic bridge](../research/ai/2026-10-20-koszul/scaling_rigidity.md)
now establishes the endpoint profile and the curvature implication for actual
characters without assuming continuous differentiability. A positive curvature
bound uniform over characters with t>=t0 for some t0<3/4 would suffice; proving
that bound remains the task.

A proposed solution must state its quantifiers and scale propagation. A single-size gain, a larger prefactor, or a character-dependent gain tending to zero does not establish the displayed uniform conclusion.

Deliver a proved gain, a rigorous obstruction to this particular gain, or another complete route from a tensor inequality to a smaller exponent.

## R5: Compare external formulations before duplicating work

Status: open synthesis task. Compare the spectral route, the block-identities route, and the polynomial-separation improvement. Identify precisely which constraints survive symmetrization and which information the scalar relaxation discards.

Deliver a dependency map with cited lemmas and a candidate constraint absent from the current local model. Do not describe an existing external lemma as a local discovery.

## R6: Make search results stronger and reusable

Status: open. Replace floating best-case ordering in a maintained search copy with exact rational ordering. Add canonical support certificates and replayable witnesses. Preserve the historical code unchanged.

A useful patch demonstrates an incorrect ranking, stronger certified block score, better search coverage, or lower computational cost at identical coverage. Report negative results with parameters and actual counts. Do not report unfinished runs as completed.

## Work selection

Read the current claim ledger, open issues, and active branches before selecting a task. Record the task and mathematical question before a long run. Prefer a question that can change a theorem, remove an assumption, or eliminate a specific search family.

Verification and discovery are separate activities. A new conjecture is useful when it has evidence and a testable consequence. Label it as a conjecture rather than withholding it or promoting it to a theorem.
