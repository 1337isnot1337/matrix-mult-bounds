# Strict-exponent construction sprint

This continuation starts from main `75bf6a378f99c26c908bd9cd616e7e20bdf342ce`.
The requested goal is a proved complex arithmetic exponent below `9/4`.
The goal remains open. A conditional number is not an achieved exponent.

## Owned questions

- Unequal paired sources: obtain a smaller finite tensor target with a
  certified exponent implication, then seek the actual restriction or
  degeneration. See `../2026-10-20-unequal-paired/README.md`.
- Cyclic sources: decide whether the proposed `A(5,6)` square-sum target
  admits ordinary maps, then investigate singular maps outside that class.
  See `../2026-10-20-hankel-segre/README.md`.
- Singular shared-factor maps: investigate whether a varying shared basis
  can realize the fat-point growth target or whether a stronger invariant
  applies. This is a discovery question, not a claimed result.

Three research agents work on these disjoint questions while the parent
agent checks proofs, coordinates source updates, and commits results.
All remote changes use this topic branch and a pull request to `main`.
The external `9/4` theorem remains attributed to OpenAI. The local written
proofs are AI-derived; checks by another agent in this same session do not
constitute external mathematical review or Lean verification.

## First checkpoint

The higher-Hankel argument excludes the ordinary `A(5,6)` restriction to
`M16` direct sum `M4`. Its exact finite screen covers every square-sum
partition in 52 specified source formats with source leg dimension at most
800. The first source passing these necessary tests has dimension 784.
This says nothing decisive about singular degeneration of the earlier target.

The unequal paired-source formula supplies all first-leg Koszul ranks under
explicit source hypotheses. A selected target of first-leg dimension 120
passes those ranks and the finite exponent gate. Its numerical consequence
remains conditional on maps that have not been constructed.

At commit `b02aad1f865b7801e5b66554a41f9af346d8ae16`, all 305 regression
tests pass. All five archive replays pass, with respective coverage 73,856
profiles, 353,664 product-filtration cases, 12,976 binary words, 209,692
ternary words, and 20,000 random cases. The protected research archives are
unchanged. These are implementation and reproduction checks, not external
mathematical review.

## Second checkpoint

The unequal-source Koszul polynomial remains an upper bound without the
two equality-range hypotheses. The proof accounts for the extra spectral
sequence rows and the possible third differential. Independent finite
controls cover 303 characteristic-two maps and 12 odd-prime maps outside
the equality range. On the other convolution input leg, the bound excludes
`EPR2` tensor `C(25,29)` to `M(7,6,7)` under arbitrary degeneration.

The explicit singular shared family for every even `m=2s` passes all moving
shared catalecticant tests at the one-copy cost `B=N`. The exact finite
replay checks 648 rational block ranks, 28 source support counts, and 12
inverse coefficient identities. These shared maps do not by themselves
construct a tensor degeneration.

There is now a positive all-size construction for a specified projection:
`C(s+1,N)` degenerates to the evaluation projection of `T_m` at `s+1`
nodes. Polynomial residue levels give the exact identity
`mapped_source = projected_target + epsilon * error`. Its coefficient
replay at `m=4,6,8,10` checks 26,694 coefficients, including 4,345 required
zeros at negative exponents. The full target still lacks `s-1` shared
directions. In the proposed shared normalization, both nonshared maps
cannot be regular; genuinely Laurent behavior is needed.

The next construction question is how to lift the projected residue-level
maps to all shared directions, allowing additional Laurent terms or source
length `N+O(m)`. Such overhead would have asymptotic cost one. No lift has
been supplied and no numerical residual is accepted as a certificate.

## Third checkpoint

The first and second order matrix-rank conditions exclude the displayed
shared-map family at `B=N`, including its quadratic ramification. The
second-order result allows arbitrary first-order motion of the target and
arbitrary finite Laurent pole orders on both nonshared maps. Its key step
identifies an intersection of node image spaces, forcing the relevant
quadratic correction to vanish. The exact controls check the four sizes
`m=4,6,8,10`; a second agent checked the written intersection argument in
the same session. This remains externally unreviewed.

Consequently the constructive search prioritizes a few additional source
coordinates, beginning with `B=11,12` at `m=4`. Uniform overhead `O(m)`
would preserve the existing asymptotic implication. Completed floating
pilots still have nonzero residuals and supply no tensor certificate.

The integrated checkpoint `1bf04fac9bcb1a30360626423e9d150225bcf1b8`
passes the remote required CI, including regression jobs on Python 3.10
and 3.14 and archive replay on Python 3.13. All five local archive replays
also pass. A local full-suite attempt produced no completion record and is
not counted as a successful run. The new tangent controls pass separately.

## Fourth checkpoint

An explicit alternating-degree construction reaches the exact fixed-shared
lower bound for every size and every replication count. The previous
finite C(4,11) witness is cited as prior work. Its cost approaches 3/2, so
this sharp construction supplies a control and a boundary for the remaining
singular problem, not an exponent improvement.

The explicit exponential-jet algebra deformation supplies a positive
algebra-level construction. A Frobenius moment window is still missing,
and at size three that algebra-compatible model is provably too narrow.
The active continuation therefore allows two independent nonshared maps.
The ordinary EPR-convolution frontier is also complete in its stated grid,
with positive coefficient controls and no general singular exclusion.

The source-aspect extension permits a few more shared coordinates,
including a/m tending to one. This retains the existing cost-one
consequence and motivates dense rectangular shared maps. All numerical
exponent consequences still have an unconstructed asymptotic premise.

The isolated full regression run at `2fe0921` completed: 320 tests passed
in 149.142 seconds. Main `8722b36` was integrated in `ed23570` without
dropping any branch claims. New focused replays verify the algebra
coefficients, exact packing maps, ordinary frontier, and source-aspect
integer comparisons. Required CI and the archive checks remain merge gates.

The separate external-preprint audit is tracked in PR #40. Its finite
local identities do not certify the paper's claimed global construction
and are not adopted as a new exponent bound.

The integrated `902bf50` full run completed with 374 of 375 tests passing.
The only failure was the Markdown-link checker interpreting coefficient
extraction notation as a relative link. The notation is corrected without
changing the argument. All mathematical tests passed in that run, and
remote archive replay also passed. The corrected head still needs the
required current CI check before merge.
