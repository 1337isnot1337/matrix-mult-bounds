# Singular leading long maps and the minimum-rank gap

October23,2026. Branch `research/singular-long-gap-20261023`.
Base: PR113 at `08ac3e983e270cf3df4e26d960ceb16415f7ef31`.

PR113 closes every scalar-balanced long-leg limit of rank110, without
unit-lift assumptions. PRs110 and119 are closed checkpoints subsumed
for that target. PR108's partial frames and PR112's regular unit-image
bound have different explicit hypotheses. Conic, asymmetric boundary,
Hankel and group-source work retain their current ownership.

Question: does the full-source minimum-rank gap exclude a regular long
map whose limiting rank is106,107,108 or109, with arbitrary Laurent
poles in both other maps and no original unit-lift assumption?

Proposed route: scalar-balance F to be regular with F_0 nonzero. The
credited right-inverse correction has regular limiting rank at most2.
With a corank-s long-leg limit, every rank-one parameter has a source
lift of rank at most15+s. For s<=4, the existing gap16-or-at-least20
forces a minimum-rank slice. Coherent-factor propagation and a polynomial
rank-one-preserver factorization should then force ker F_0 to contain
an invertible target matrix, contradicting the unit-image rank budget.

Prove all factorization cases, including degenerate image spaces, before
claim registration. Give exact invertible-kernel witnesses and the s=5
strict-boundary failure. The target and exponent remain unconstructed.
