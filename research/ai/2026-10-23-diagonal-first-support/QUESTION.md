# Question and coordination

Base: support-capacity checkpoint
`7690348a792c5734d6f00d7fa7a9e6ce8dc37daa`, already containing main
`3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.
Branch: `research/diagonal-first-support-20261023`.

The coordinating parent assigned this follow-up to PR164. Does a
controlled diagonal of an otherwise mixed first map force substantial
ordinary repair, when the full product-map hypothesis is unavailable?

The result permits arbitrary long maps and arbitrary off-diagonal
bilinear changes that vanish on the diagonal. It imports the exact
source conventions, ordinary surjectivity and divisor-stratum bounds
from the preceding support-capacity proof, keeping those files pinned
and unchanged. The new steps are the Veronese intersection, common
factor-kernel exclusion, joint triangular deficiency budget and its
exact threshold split.

## Why the initial rank-only approach was insufficient

For c=1 and first residual e<r=n-1, the preceding proof makes both
long kernels sixteen-dimensional. On the residual annihilator W,
the dual first map is injective and satisfies

\[
\operatorname{rank}L(X)\le4\operatorname{rank}X+17.
\]

This follows from target slice rank \(4\operatorname{rank}X\),
at most 32 ranks lost by compression, and the native lower bound
\(\operatorname{rank}S_Y\ge\operatorname{rank}Y+15\).
The rank-one section therefore has coefficient rank at most21.

The shift-transpose control in the new proof is injective, has no
common matrix kernel or proper common image, and maps the entire
Segre to rank at most two. Thus these rank conditions alone do not
force the earlier fixed-product form. They do not supply the shared
long maps needed for an actual source-to-target identity.

Two checked classical results clarify the missing hypotheses. Marcus
and Moyls's [Theorem1](https://msp.org/pjm/1959/9-4/pjm-v9-n4-p17-s.pdf)
is a rank-one-preserving endomorphism theorem over an algebraically
closed field of characteristic zero; a rank-21 section does not meet
its assumptions. For a square matrix space of upper rank21, de Seguins
Pazzis's [Theorem1.7](https://arxiv.org/pdf/1507.05375v2) gives its
characteristic-zero compression conclusion at dimension at least
21n-40. The ruling spaces here have dimension at most n-1. The larger
space L(W) is not bounded in rank by21. Neither theorem is an input
to the new obstruction.

## Distinct scopes

- The preceding full product-first-map theorem controls all
  L(u tensor v)=H F(u)G(v). The new theorem controls only u=v and
  explicitly admits diagonal-vanishing perturbations.
- PR157's ordinary finite-bandwidth Toeplitz long maps with exceptional
  columns place restrictions on the long maps and allow an arbitrary
  first map. This package places its restriction on the first map's
  diagonal and permits arbitrary long maps. No result from PR157 is
  imported; the parent previously recorded its head `9e830aa`.
- The fixed-good-row frontier and oblique repair packages concern
  different explicit long-map hypotheses and constructions. They are
  not dependencies of this follow-up.
- The new result is ordinary only. The imported support-capacity
  theorem's broader Laurent scope does not extend the exact diagonal
  slice argument to Laurent maps.

The next construction question is an actual source-to-target identity
whose diagonal falls outside the displayed class, or one that accounts
for the permitted linear repair cost. No further constant optimization
is part of this checkpoint.
