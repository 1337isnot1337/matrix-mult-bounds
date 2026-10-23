# Paired long-leg checkpoint

Objective: determine the long-leg Koszul obstruction for the 28 remaining
paired single-matrix formats through a16, then construct a surviving
target or identify a stronger obstruction. The exponent goal is open.

Completed: the written all-field injectivity interval 0<=p<=a(a-1),
and full row rank for N-a<=p<=N, with the proof in proof.md. Exact coefficient and integer-kernel evidence
is in results/paired-bundle-injectivity-2026-10-23/. Six focused and18 metadata
tests pass on Python3.12 with the pinned maintained dependencies.
All five archive replays passed on the pre-isolation proof head. The first
full-suite run was stopped during branch isolation; it is not a complete
validation. Final integrated regression evidence will be recorded separately.

Next mathematical step: the intermediate-degree kernel bundle R_p(D). Its
successive line-bundle degrees are p+a-1-a*k for k>=a, with multiplicities
from the Hankel kernel and wedge^(p-k)Q. At p=a(a-1)+1 the largest degree
is zero. Filtration extension maps can obstruct lifting those sections;
counting the associated graded sections is not an exact kernel formula.
Compute or control these connecting maps before asserting higher ranks.

Discovery boundaries: a two-weight dimension bound need not be sharp;
at a2,p3 it is74 while the exact complex rank is70. Finite mod2 and
mod1009 pilots agree at a3,p7,...,11, but agreement of two modular lower
bounds is not a complex upper bound. A restriction to a direct sum of
a Hankel tensors gives an all-degree source lower bound; together with
the injectivity theorem it does not settle any new degree beyond the
proved interval for the 28 maintained survivors. Do not infer that those
degrees pass. These pilots are discovery, not additional theorem claims.

Worktree: /tmp/matrix-paired-bundle-01a168f9.
Branch: research/paired-bundle-01a168f9.
No independent review or formalization. Preserve the separate active
central-cover, singular-unit and boundary-incidence investigations.
