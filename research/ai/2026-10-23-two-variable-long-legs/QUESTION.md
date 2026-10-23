# Both long maps variable: bounded profile repair barrier

Base: main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.
Owner-directed OpenAI Codex research, October 23, 2026.

Question: for ordinary maps of the paired source Q(n,m), does a common
B shift-window span of dimension r, together with a C coefficient-profile
span of dimension s and r*s<m, force quadratic first-residual rank even
when both long maps vary with their source column?

Planned output: a self-contained all-field proof, independently expanded
finite coefficient controls, explicit residual flattenings, strict-boundary
and corrupted-evidence tests, exact source pins and a claim ledger entry.
The first-leg map remains arbitrary. Exceptional columns may be nonlocal.

Consequence sought: exclude subquadratic auxiliary repair in this broader
ordinary-map class. This cannot exclude Laurent cancellation or arbitrary
full-profile maps, and cannot itself improve the matrix exponent.

Concurrency checked: all open PRs through #178 and no open non-PR issues.
PR #173 treats one variable leg with the other Toeplitz; PR #172 treats
one profile-separated leg with the other Toeplitz. The proposed extension
retains their common Laurent-symbol idea and adds a profile expansion on
the second leg. Neither pending PR is treated as merged or independently
reviewed. Their method credit and immutable commits will be recorded.

Checkpoint: written proof and six finite coefficient/flattening controls pass.
An exact width-four control attains full symbol rank at the strict boundary.
Focused regression, full regression and required hosted CI are pending.
Next: carry the contraction argument to near-full target outer dimensions,
the form used in the maintained linear-correction criterion.
