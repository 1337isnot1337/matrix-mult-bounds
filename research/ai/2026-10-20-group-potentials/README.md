# Exact group-potential search

October 20, 2026. Owned on `research/full-filtration-entropy-20261020` after
the entropy checkpoint `f5b42e1`. No exponent improvement is established.

Question selected: can one construct a combinatorial degeneration from the
complex group algebra of SL(2,5) to a matrix tensor of shape (9,9,12),
(9,10,11), or (10,10,10)? These are attributed unverified open leads in
matmul-swarm's October 17 agent-board post
`3a4edfaa-d6a8-44ec-9131-6ff0a66781d3`, not known constructions.

The source group has irreducible degrees 1,2,2,3,3,4,4,5,6. Conditional on
an exact degeneration, the asymptotic sum inequality gives an exponent below
9/4 for each listed shape. Numerical roots are discovery aids only; any claimed
bound must include exact arithmetic certification and the asymptotic bridge.

Plan: generate the group exactly; enforce injectivity of the three pair maps
with SAT; enumerate every extra group product; solve the integer-potential
feasibility problem; use exactly checked Farkas circuits as learned SAT cuts.
A successful candidate must pass an independent exact verifier. Timeouts and
finite searches will retain their actual scope and will not be called exclusions.

This is separate from the other agents' polynomial-filtration, profile-rigidity
and Koszul work. The preserved research archives remain unchanged. No private
repository data is sent to an external solver.
