# Research checkpoint and handoff

This branch starts at `e0d7ed5` and contains three mathematical checkpoints:

- `d5303b8`: general convolution Koszul ranks and rejection of the 85 archived
  candidate packings.
- `5d831b4`: attributed agent-board review and the Massarenti-Raviolo correction
  to the finite exact-rank search window.
- `fc4cc70`: a mixed target surviving full-space Koszul tests, its explicit
  border-rank certificate, the restricted monomial obstruction, and actual
  rescaled-profile rigidity without a C1 assumption.

The [research note](research_note.md), [analytic bridge](scaling_rigidity.md),
[claim ledger](claims.json), and [verification record](../../../results/koszul-2026-10-20/verification.json)
give the precise results and limitations. The exponent remains 9/4.

The continuation adds [all-dimension mixed targets](all_dimension_targets.md):
explicit border-rank certificates, survival of all full-space Koszul tests,
an all-size coordinate-weight obstruction, and a quantitative implication
from an **unconstructed** convolution degeneration. Less than 2.04721048 percent
asymptotic source overhead would suffice. Zero overhead would conditionally
give omega<=125/56, but no such source degeneration is established.
The stronger limiting-slope bound is adopted from the concurrent `cf79709`
proof, with the overlap and joint-sequence quantifiers reconciled in the note.

[Source obstructions](source_obstructions.md) rule out low-overhead ordinary
linear restrictions and shared-coefficient-preserving degenerations with
arbitrary transformations on the other two factors. The unrestricted shared
factor is the current unresolved construction variable. Fixed-dimension
positive controls and bounded, unsuccessful numerical fits are retained.
The shared-factor polynomial-matrix lemma rules out further progress from
projected shared Koszul or linear equivariant Young/Pieri tests of that form.

The [orthogonal-polynomial audit](orthogonal_bases.md) gives an all-size
obstruction for degree-ordered coordinate degenerations in those bases.
For Chebyshev bases with arbitrary shared permutations, an exact necessary
two-row enumeration excludes nonidentity orders through m=38; independent
small enumeration and exact normalized witnesses validate the implementation.
The finite range is explicit and the general shared-factor problem remains open.

The subsequent [arbitrary shared-basis proof](arbitrary_shared_basis.md)
extends the catalecticant obstruction to every constant invertible shared
basis, by bounding the derivative spaces of a biform with invertible
coefficient matrix. This also excludes the concurrent constant-G graded
ansatz at low overhead. Its nonsingular-block extension and explicit slice
cover also exclude two regions of mixed shared/nonshared weights. Genuinely
singular shared maps and intermediate weight slopes remain the gap.
The [intermediate-weight slice covers](intermediate_weights.md) quantify a
further range of slopes and exclude the replicated m=4 balanced-direction
target for k>=2. They leave the single-copy case and the growing-m balanced
route open; no construction or exponent improvement follows.

The [finite amplitude target](finite_amplitude.md) combines existing
tripling and two-sector constructions into 6P(a,a)<=(6a-2)^(1/t). A new
universal 13/12 gain at C(4,4), if proved near the endpoint, would give
omega<=2.249 by an exact integer certificate. That gain is unproved.
A dimension screen excludes one matrix-product extraction method at a=2,3.
The separate [permutation pilot](permutation_probe.md) retains 11 unsuccessful
floating fits at direction (5,2), with no construction or exclusion claim.

## Next mathematical question

Continuation selected after fetching the other research branches on October 20:
extend the four-block target to all shared dimensions m, determine an explicit
source-overhead threshold that would contradict the actual critical profile,
and investigate the required degeneration. This stays separate from the other
agents' product-filtration and scalar-rescaling tasks. The threshold is a
conditional construction target, not an achieved exponent improvement.

The finite precursor is to determine whether C(4,10k) can degenerate to the canonical four-block target
T tensor B_X(k) for some k>=53 using general changes of basis. The target's
border rank is 10k and all full-space Koszul tests pass, while coordinate
selection and diagonal weights require source length at least 12k-1 and fail.
The projected shared Koszul and linear equivariant shared flattenings above
cannot reject this target. General orbit-closure constructions remain
unsettled. A successful finite degeneration would refute P_*, but an
additional scale-propagation argument would still be needed to lower omega.

## Concurrent work observed

At the last read, `origin/main` was still `e0d7ed5`. The pinned
[concurrent review](../../../docs/concurrent_research.md) records which other
workers' arguments were read and which were adopted, including the stronger
limiting-slope estimate and the minimum-slice restriction obstruction.

## Verification boundary

The latest local regression has 63 passing tests, including exact rotated
catalecticant and basis checks; the original archive replay previously passed. The first and
second archives are unchanged from the starting revision. GitHub Actions run
[39490536693](https://github.com/1337isnot1337/matrix-mult-bounds/actions/runs/39490536693)
at `fc4cc70` did not start any test steps: GitHub reported an account payment or
spending-limit gate. It is not a remote test pass or a mathematical test failure.
No billing setting was changed. The general proofs still need independent
review or formalization.

The earlier CI limitation has since cleared: hosted replay run
[39504501053](https://github.com/1337isnot1337/matrix-mult-bounds/actions/runs/39504501053)
passed at the exact head `8e0a766`. This is artifact verification, not theorem
review. The historical failed-to-start run remains recorded accurately above.
