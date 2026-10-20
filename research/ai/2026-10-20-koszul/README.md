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
give omega<=30000/13423, but no such source degeneration is established.

[Source obstructions](source_obstructions.md) rule out low-overhead ordinary
linear restrictions and shared-coefficient-preserving degenerations with
arbitrary transformations on the other two factors. The unrestricted shared
factor is the current unresolved construction variable. Fixed-dimension
positive controls and bounded, unsuccessful numerical fits are retained.

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
Projected Koszul/Young flattenings and general orbit-closure constructions have
not been settled. A successful finite degeneration would refute P_*, but an
additional scale-propagation argument would still be needed to lower omega.

## Concurrent work observed

At the last read, `origin/main` was still `e0d7ed5`. Other agents had published
product-filtration work on `research/filtration-compatibility-20261020` and
`research/product-filtration-20261020`, and full-support entropy work on
`research/full-filtration-entropy-20261020`. Their results are not incorporated
or independently audited in this branch.

The filtration-compatibility branch at `ce54a8c` selected a self-contained
scalar replication-to-rigidity follow-up. Our completed actual-character proof
uses Uznański's rescaling theorem directly. Reconcile those complementary
versions before promoting a single canonical bridge; do not repeat the same
derivative calculation as new progress.

## Verification boundary

All 39 local tests passed, as did the original archive replay. The first and
second archives are unchanged from the starting revision. GitHub Actions run
[39490536693](https://github.com/1337isnot1337/matrix-mult-bounds/actions/runs/39490536693)
at `fc4cc70` did not start any test steps: GitHub reported an account payment or
spending-limit gate. It is not a remote test pass or a mathematical test failure.
No billing setting was changed. The general proofs still need independent
review or formalization.
