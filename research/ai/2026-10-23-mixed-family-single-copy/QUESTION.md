# Single-copy pilot for the mixed-sector degeneration

Selected October 23, 2026 from `origin/main` at `1c04903`. The current issue
and pull-request list and local worktrees were checked; none has this
single-copy question. This is a finite pilot for R3, not a new exponent claim.

## Exact question

Work over `C`. Let the convolution source be

\[
C(4,10)=\sum_{i=0}^{3}\sum_{j=0}^{9}X_iY_jZ_{i+j},
\]

of format `(4,10,13)`. Let

\[
T_4=\sum_{a+b+c+d=3}X_{a+c}Y_{a,b}Z_{c,d},
\]

where each of `Y` and `Z` has the ten coordinates indexed by
`a+b<=3` or `c+d<=3`. This is the `k=1` member of the four-sector family in
`research_note.md`, and has format `(4,10,10)`.

Determine whether there are Laurent-polynomial families of linear maps

\[
A_\epsilon:\mathbb C^4\to\mathbb C^4,\quad
B_\epsilon:\mathbb C^{10}\to\mathbb C^{10},\quad
C_\epsilon:\mathbb C^{13}\to\mathbb C^{10},
\]

of full required rank for generic nonzero `epsilon`, for which
`(A_epsilon tensor B_epsilon tensor C_epsilon) C(4,10)` has a finite limit
equal to `T_4`, up to fixed invertible changes of target bases. A positive
answer needs an exact identity and limit certificate. A negative answer needs
a polynomial or geometric obstruction covering every such family.

## Existing boundary

- The target has border rank exactly `10`; the source dimensions and target
  coefficient identity are retained in `all_dimension_targets.md`.
- An ordinary restriction is impossible by
  `source_obstructions.md`, whose slice-rank bound requires source length at
  least `13` here.
- Coordinate selection with diagonal weights is impossible: the saved
  interval argument requires length at least `11` for `m=4,k=1`.
- Shared-leg Koszul tests and all three full-space Koszul families pass.
  Existing structured shared-factor flattenings also cannot separate a
  target of border rank `10` from this source.
- These statements do not exclude singular shared-map degenerations with
  general changes on the other legs. A result for `k=1` alone would not prove
  the unbounded `k>=53` premise or improve `omega`.

## First calculation

Construct the four exact source and target slice matrices in a fixed recorded
coordinate order. Compute the target's exact rank strata in `P^3`, including
the determinantal ideals, and compare their scheme data with the source
family after arbitrary three-dimensional quotients of its long leg. Use this
as a discovery route only: any claimed obstruction must be invariant under
the full family of allowed changes and must survive orbit closure.

Record exact equations, matrix ranks, and failed approaches. Do not promote a
finite numerical fit or a rank-pattern mismatch to a border-degeneration
obstruction.
