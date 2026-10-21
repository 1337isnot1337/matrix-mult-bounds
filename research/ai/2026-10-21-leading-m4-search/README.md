# Numerical search for an M4 leading point with a larger source kernel

**Status: finite search history, with no exact low-rank certificate and no
new exponent bound.** This package preserves 39 terminal floating-point
points, their full maps, their available parameter vectors, the diagnostic
stage traces, and discovery-code snapshots. It includes a separate native
coefficient contraction that does not import the search implementations.

The seven batches explored leading points for a possible Laurent extension

\[
Q_{6,4}\unrhd M(5,4,5),\qquad
Q_{n,m}=\sum_{p,q<n}\sum_{y,v<m}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

Their immediate goal was an ordinary restriction of `Q(6,4)` to `M(4,4,4)`
whose map on the **unrestricted source A leg** has rank at most 27. No
batch produced an exact witness for that condition. A failed numerical
search excludes no tensor restriction or degeneration.

## Why the rank threshold is 27

Let `B0,C0` have output supported on the old 16 coordinates of each long
target leg. Applying them to the source, while retaining all 36 source A
coordinates, gives

\[
S_0=(\mathrm{id}_A\otimes B_0\otimes C_0)Q_{6,4}
\in A_{36}\otimes B_{16}\otimes C_{16}.
\]

Write `r` for the dimension of its A-slice space. A final `M(5,4,5)` has
25 A slices, of which exactly 16 are supported in the old `16 by 16`
long-leg block. It therefore needs nine independent directions outside
that block. The saturated source slice space has dimension at most 36,
contains the limiting leading space, and must contain those nine new
directions. Thus `r+9 <= 36`, or `r <= 27`, is necessary for this
particular extension setup. This is the dimension gate proved in
[outer_product_boundary.md](../2026-10-20-paired-construction/outer_product_boundary.md).

The previously certified `Q(5,4) -> M(4,4,4)` maps, embedded in `Q(6,4)`,
have pre-A rank 36. This motivates changing the long leading maps before
searching higher Laurent coefficients.

## Archived batches

The residual is `||T - M4||_F / 8`. The rank-tail diagnostic is
`(sigma_28^2 + ... + sigma_36^2)^(1/2)` for the `36 by 256` pre-A matrix.
The latter depends on basis and scale, so values from different gauges
are not directly comparable. Coefficient residuals below come from the
standard-library replay; singular-value tails come from the saved search
records, with a separate optional SVD replay. The two minima in each row
can occur at different terminal points.

| Batch | Terminal points | Smallest coefficient residual | Smallest absolute rank tail |
|---|---:|---:|---:|
| Unconstrained, relative tail, historical gradient | 3 | 3.4816573e-4 | 0.77585661 |
| Unconstrained, absolute tail, historical gradient | 3 | 6.3044551e-5 | 0.09777517 |
| Unconstrained, corrected absolute-tail continuation | 3 | 2.4487084e-6 | 0.09523019 |
| Identity-preserving annihilator family | 12 | 1.9004001e-15 | 1.91371270 |
| Mixed middle space, without middle Gram penalty | 2 | 3.5209233e-16 | 0.62738947 |
| Mixed middle space, with middle Gram penalty | 12 | 9.6626137e-17 | 1.27966729 |
| Moving outer and middle spaces | 4 | 6.5159399e-15 | 0.60786080 |

In the last four batches, the formulas preserve the M4 identity
algebraically when the selected product minors are invertible. Their
small floating-point coefficient residuals confirm the formula replay;
they do **not** certify the desired low pre-A rank. The residual in the
corrected unconstrained batch is also not zero.

Balanced mixed-middle seeds 0, 4, and 8 start at the same structured
point. Consequently, its 12 labeled trials contain ten distinct initial
states. The moving-space batch continues four earlier fixed-space
points. The batches are not 39 independent random restarts.

### Unconstrained maps and the corrected derivative

The first three batches vary three complex `16 by 36` maps. They use the
full coefficient error, an SVD rank-tail objective, entrywise bounds,
and a norm-cap penalty. For a real coordinate vector representing a
complex map, the penalty is

\[
\phi(M)=\frac{\rho}{2}
\max\{0,\|M\|_F^2/64-1\}^2.
\]

On its active branch the gradient is

\[
\nabla\phi(M)=\frac{2\rho}{64}
(\|M\|_F^2/64-1)M.
\]

The two oldest discovery scripts omitted the factor 2. Their initial
finite-difference checks were below the cap and did not exercise this
branch. Those scripts and terminal points are retained as historical
records with this error explicitly marked. This does not affect replay
of their saved maps, but their optimization trajectories are not runs
of the stated objective gradient.

The corrected continuation starts from the three absolute-tail terminal
points. It runs three stages, with rank weights `0.1, 0.01, 0.001`, up to
1,800 L-BFGS-B iterations each. Before optimization, it checks a random
direction at 1.2 times the starting map, where the norm penalty is
active. All three derivative errors were below `8e-10`. The separate
scalar penalty control in `replay.py` detects the historical derivative
and accepts the corrected one. No certificate was obtained after the
correction.

### Families that preserve the leading M4 identity

The starting point is polynomial multiplication. Here `P_d` denotes
polynomials of degree at most `d`.

The annihilator batch fixes four-dimensional spaces `U,V` in `P5` and
two-dimensional spaces `Y,W` in `P3`. The two product spaces `U Y` and
`V W` have dimension eight inside the nine-dimensional `P8`. Dual
product maps give M4. Free long-map terms in the one-dimensional product
annihilators preserve that tensor identity, including the simultaneous
cross term. There are 96 complex free coefficients. All 12 complete
terminal maps and the four defining spaces are saved.

The mixed-middle batches allow a four-dimensional space

\[
H\subset P_3\otimes W,
\]

which need not factor as `Y tensor W`. They choose left inverses for

\[
V\otimes W\longrightarrow P_8,\qquad
U\otimes H\longrightarrow P_8\otimes W.
\]

The first map has an eight-dimensional domain and one unused output
dimension; the second has a sixteen-dimensional domain and two unused
output dimensions. With product-dual rows `LB` and `LC`, the maps are

\[
\begin{aligned}
A_{p,q}\mapsto\sum_{i,h}U_h(p)V_i(q)a_{i,h},\\
B_{y,s}\mapsto\sum_{i,j,b}H_j(y,b)LB_{i,b;s}\,b_{i,j},\\
C_{z,v}\mapsto\sum_{h,j,b}LC_{h,j;z,b}W_b(v)c_{j,h}.
\end{aligned}
\]

Contracting the two product-dual identities gives M4. This is the
same contraction used in the exact mixed-middle construction, with the
outer spaces now allowed to have degree five. The obstruction in
[mixed_middle_boundary.md](../2026-10-20-paired-construction/mixed_middle_boundary.md)
requires outer spaces in `P4` and does not exclude this `P5` family.

The fixed-space batches vary 72 complex parameters: 32 coefficients for
`H`, 32 for the second dual's free output complement, and eight for the
first dual's free output complement. The balanced batch also penalizes
`||H H* - I||_F^2`. The moving-space batch varies `U,V,W` as well, for
128 complex parameters. It uses fixed invertible-minor charts for both
left inverses and Gram penalties for the moving spaces. Complete
terminal parameter vectors and pivot orders are saved.

## Finite coordinate pilot

The archive also includes a separate C++ enumeration of an additive
single-coordinate embedding ansatz. It scanned 956 normalized middle
coordinate sets and 405,817 admissible outer-coordinate pairs. It found
six valid M4 embeddings, all with all 36 source A coordinates present
in the pre-A support. Only the best-support record and source code were
retained; the enumeration did not retain every rejected coordinate set.
This narrow ansatz provides no obstruction for dense linear maps.

## Contents, replay, and limits

Run from the repository root:

```bash
python -S research/ai/2026-10-21-leading-m4-search/replay.py
python -S -m unittest discover -s tests -p 'test_leading_m4_search_replay.py'
```

`results/leading-m4-search-2026-10-21/search-history.json.gz` contains
checksummed original text records. Each terminal point includes all
three complex maps. Structured families also include their terminal
parameters, pivot orders, and fixed spaces as applicable. Available
diagnostic stage traces are included. Intermediate optimizer iterates
and intermediate full maps were not retained.

The discovery sources are preserved for provenance. Some retain their
original absolute scratch paths. The archived mixed-middle source is
the later balanced version; the two unbalanced pilots ran before the
middle Gram penalty was added. Their maps remain directly replayable.
The supported portable verification entry point is `replay.py`.

To extract the historical source and point files without executing them:

```bash
python research/ai/2026-10-21-leading-m4-search/replay.py --extract /tmp/leading-m4-history
```

The default replay uses only the Python standard library. It uses the
literal native source indices, sums all 576 source terms, and checks all
4,096 target coefficients for each of the 39 terminal points. Its stored
result is `verification.json`. It also
replays the earlier integer Q54 certificate after embedding it into
Q64, and detects a deliberate sign error at four coefficient positions.
No optimization generator or NumPy module is imported by these checks.
The default result labels the saved singular values as archived
diagnostics; it does not reverify them.

The optional `--svd` flag imports NumPy lazily and recomputes the numerical
singular values. It is outside the required verification dependency set
and is not run by the default tests. Its separately recorded result is
`verification-svd.json`:

```bash
python research/ai/2026-10-21-leading-m4-search/replay.py --svd
```

These are same-session verification controls. They are not external
review. Floating-point singular values prove neither a low-rank
construction nor an exact exclusion. This package supplies reproducible
negative search evidence and identifies the derivative correction; it
does not change the exponent ledger.
