# Research directions

These are proposed investigations, not claimed results. Each task has a concrete output and an explicit path to a downstream claim.

## R1: Review the local sharpness theorem

Status: open. Review the full all-integer proof, especially positivity of increments, the limiting slope, and the join at $a=b$. Distinguish the earlier recurrence from the local matching construction.

Deliver a proof review tied to a commit, a corrected proof, or a counterexample. A finite grid extension alone does not close this task. A Lean formalization is a separate deliverable, not a prerequisite for every discovery.

## R2: Decide compatibility with the product-filtration family

Status: settled for the three stated two-source, fixed-label families by
[AI-FILTRATION-007](../research/ai/2026-10-20-concavity-equivalence/research_note.md).
They are equivalent to separate concavity including the zero boundary for
positive, symmetric, edge-normalized profiles. The matching profile satisfies
them at all positive integer sizes. Actual character profiles already have
the boundary from the elementary `P(a,b)<=ab` restriction.

Further work must retain information absent from these families, for example
extracting several label fibers together. A new constraint must force stronger
growth for every relevant character before it can affect $\omega$.

The concurrent proof at `712c91a` supplies another compatibility argument;
see [the pinned comparison](concurrent_research.md) and its
[local proof](../research/ai/2026-10-20-affine-direct-sums/research_note.md).
Extending the completed fixed-label grid cannot produce a smaller exponent.

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

The [completed scaling and rigidity argument](../research/ai/2026-10-20-concavity-equivalence/homogeneous_rigidity.md)
now supplies the earlier curvature draft's analytic bridge from replication,
rank and concavity. No differentiability assumption is needed. An endpoint
character must have limiting shape
`K min(x,y)^(1/3)(max(x,y)+min(x,y)/2)` for some `K>0`.
Find a new asymptotic tensor constraint excluding every such amplitude, or
prove a positive normalized curvature gain. Neither is currently proved.

The [actual-character bridge](../research/ai/2026-10-20-koszul/scaling_rigidity.md)
supplies an overlapping proof with the external rescaling theorem.


A proposed solution must state its quantifiers and scale propagation. A single-size gain, a larger prefactor, or a character-dependent gain tending to zero does not establish the displayed uniform conclusion.

Deliver a proved gain, a rigorous obstruction to this particular gain, or another complete route from a tensor inequality to a smaller exponent.

The [finite amplitude route](../research/ai/2026-10-20-koszul/finite_amplitude.md)
selects S_4 to M106 as a sufficient, unconstructed degeneration. Its
[necessary tests](../research/ai/2026-10-20-koszul/finite_target_screens.md)
pass all singleton quantum functionals but exclude coordinate inputs even
with arbitrary Laurent output. The next question is a construction with
actual input mixing or a necessary test that covers such mixing. The
all-power coordinate matrix-extraction method is also excluded at a=5 by
an entropy refinement; repeating that class at these diagonals cannot
supply the finite gain.

A [smaller sufficient target](../research/ai/2026-10-20-koszul/cyclic_finite_target.md)
is A_4 to M(10,10,11), where A_4 has leg dimension 112. The minimum-slice-rank
proof excludes all constant linear maps, so a construction needs a singular
limit as well as input mixing. The later
[polynomial rank-locus theorem](../research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
closes all four ordinary A5 targets that passed the old minimum-only
screen. The [updated balanced rectangular frontier](../research/ai/2026-10-21-rectangular-ordinary-frontier/proof.md)
uses the existing higher Hankel gates and excludes every improving ordinary
single matrix shape through a=7. At a=8, M(27,28,28) is the sole sorted
necessary-test survivor; its maps remain missing. Singular A4 constructions
remain open.

## R5: Compare external formulations before duplicating work

Status: open synthesis task. Compare the spectral route, the block-identities route, and the polynomial-separation improvement. Identify precisely which constraints survive symmetrization and which information the scalar relaxation discards.

Deliver a dependency map with cited lemmas and a candidate constraint absent from the current local model. Do not describe an existing external lemma as a local discovery.

## R6: Make search results stronger and reusable

Status: open. Replace floating best-case ordering in a maintained search copy with exact rational ordering. Add canonical support certificates and replayable witnesses. Preserve the historical code unchanged.

A useful patch demonstrates an incorrect ranking, stronger certified block score, better search coverage, or lower computational cost at identical coverage. Report negative results with parameters and actual counts. Do not report unfinished runs as completed.

## R7: Whole-filtration entropy beyond the balanced obstruction

Owned on `research/full-filtration-entropy-20261020`. The [new note](../research/ai/2026-10-20-full-filtration/research_note.md)
defines the optimistic full-support entropy score and proves an all-size
`39/40` upper bound for balanced sources. Exact certificates cover every
distribution at every unequal-source tuple through size 12.

The next precise question is whether its explicit upper bound `U(a,b,c,d)`
never exceeds `P_*(a,b)P_*(c,d)` for arbitrary positive lengths, or even has the
same `39/40` factor when all four lengths exceed one. This is a conjecture,
not an all-size consequence of the grid. A weighted block-extraction theorem
also requires its own proof; the scalar subrank formula is insufficient by itself.

## Work selection

The product worker's [paired-source calculation](../research/ai/2026-10-20-paired-sources/research_note.md)
now includes an [all-power rank formula](../research/ai/2026-10-20-paired-sources/all_koszul.md).
It excludes the initially selected P_6 to M(6,10,6) target at power seven.
The complete finite frontier through a=13 excludes all 239 improving,
dimension-compatible single matrix shapes modulo B/C exchange. Do not fit
those closed targets. Larger paired matrix targets, joint extraction from
paired factors, and genuinely varying recoupling bases remain construction
questions. Passing a necessary rank test would not supply a degeneration. The new
[quantum recoupling question](../research/ai/2026-10-20-quantum-recoupling/QUESTION.md)
uses genuinely varying bases near a root of unity. Its regular initial
maps have insufficient size; tensor-level cancellations remain to be found.
The [leading-flag follow-up](../research/ai/2026-10-20-graded-quantum-flags/QUESTION.md)
now closes several prescribed root flags even with arbitrary higher jets.
Changing the first-leg jet cutoff does not escape those proofs. Different
leading flags and weight-breaking projections remain construction questions.

The active fat-point construction question is quantified in the
[all-degree growth route](../research/ai/2026-10-20-concavity-equivalence/fatpoint_growth_route.md).
It requires a genuine convolution-source degeneration at cost below
`9/(7*2^(1/3))`; no such construction is supplied. New linear bases and
matrix-space degenerations are open. The finite rank screens do not decide it.
The [finite-group construction campaign](../research/ai/2026-10-20-group-potentials/README.md)
is owned on `research/full-filtration-entropy-20261020`. Rank-locus dimensions
exclude two previously reported SL(2,5) targets under general degeneration;
only (10,10,10) survives the finite degree-sum/rank-locus frontier. Constructing
that degeneration would give a smaller exponent, but no witness exists here.
Affine-group searches use exact abelian-coset and normal-table constraints.
Avoid repeating the earlier unnormalized searches without a new reason.

The [semisimple full-space continuation](../research/ai/2026-10-21-semisimple-koszul/proof.md)
supplies a new exact SL(2,F8) source and screens every improving integer
format. The selected M(18,18,25) target passes all stated necessary tests
and would imply2.245 if constructed. Its first full-D18-subgroup pilot
timed out without a pair model. The next construction must improve that
search or change its frame; repeating the same bounded run is not new
mathematical progress. This is distinct from the active SL(2,5) native
parity work. General complex F8 degenerations also retain21 possible
formats after the new full-space Koszul exclusions.

Read the current claim ledger, open issues, and active branches before selecting a task. Record the task and mathematical question before a long run. Prefer a question that can change a theorem, remove an assumption, or eliminate a specific search family.

Verification and discovery are separate activities. A new conjecture is useful when it has evidence and a testable consequence. Label it as a conjecture rather than withholding it or promoting it to a theorem.
