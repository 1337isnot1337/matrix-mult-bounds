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

Focused checks pass for both packages. Complete regression and archive replay
will be recorded before the pull request is marked ready. The protected
research archives are unchanged.
