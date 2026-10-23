# A weighted screen for split replacements of the rank-76 seed

Any termwise candidate preserving all 58 original third-factor
directions on a long leg in the specified target-leg alignment needs
at least ten rank-four groups. The Q(6,4) evaluation grid supplies only
nine. Therefore a construction based on this seed
must change the third-factor direction set; merging first-factor
directions alone cannot make the termwise assignment work. Shared-first-
factor flips after a split can change some third factors. The later
[fixed-component certificate](../2026-10-23-fixed-flip-components/README.md)
closes that continuation for the two explicit split seeds: 50 permanent
third-factor directions still require ten groups. Other split seeds
and operations outside those components remain open.

The four simultaneous split replacements found in the companion
`2026-10-23-flip-escape` investigation leave 72 distinct first-factor
directions. They escape the previous *count* of 76 directions against a
72-direction upper bound. They still fail a stronger termwise grid test:
their remaining directions have weight 238, while nine rank-four groups
can cover weight at most 216.

The screen also sets a concrete target for further split searches. A
scheme that only replaces original first factors by other original first
factors must delete weight at least 35. It needs at least nine distinct
direction deletions; nine suffice for this necessary inequality only if
at least eight come from the distinguished set below. Passing the screen
does not construct the source maps or even a grid cover.

This is a finite exact computation and a written implication for the
specified termwise model. It does not exclude general maps from Q(6,4),
new replacement directions, or singular constructions outside that model.
It gives no new matrix multiplication algorithm or exponent.

## The unchanged third factor already needs ten groups

Normalize each of the 76 original `w` vectors by its first nonzero entry
and deduplicate in first-occurrence order. This gives 58 integral
projective directions, with 40 singleton classes and 18 double classes.
The verifier reconstructs these classes from the pinned external data;
no separate list of factor arrays is introduced.

In that class order, assign the following nonnegative integer weights:

```
4,3,3,2,3,3,2,2,4,1,2,1,4,4,4,4,4,4,0,4,
4,4,0,4,4,4,2,4,4,4,4,2,0,4,0,0,4,4,1,4,
0,2,2,1,2,2,2,3,2,2,1,3,2,1,4,3,0,2.
```

Their total is 149. The exhaustive replay checks all
\(\binom{58}{4}=424,270\) four-subsets over F_101, of which 423,231
are independent. Every resulting four-flat has total weight at most 16.
The full source span has dimension 20, so every smaller flat extends to
one of these. Reduction of integer minors, as detailed below, transfers
the bound to complex rank-at-most-four sets. The nonnegative weights
also make this statement valid when some directions have weight zero.

Thus any nine rank-four groups cover weight at most 144, below 149:

\[
\boxed{\text{Covering all original third-factor directions requires
at least }\lceil149/16\rceil=10\text{ groups.}}
\]

This conclusion allows arbitrary changes of the first two factors and
arbitrary common invertible changes and individual nonzero rescalings of
the third factors. It also applies over a characteristic-zero Laurent
field. It only requires that every original third-factor direction is
still represented by a nonzero term. In particular, it excludes all
first-factor-only replacements that retain the original third factors.
It does not exclude the later flips that change those factors.

The weights were found using a numerical linear-programming discovery
step and rounded down to the displayed integers. Acceptance uses only
these integers and the exhaustive finite-field replay in
`w_enumeration.json`; it does not trust an optimizer objective or require
SciPy. A rational rank-four equality witness is checked independently.

## Source and weights

We reuse the 76 integer first-factor vectors `u` of the externally credited
AlphaTensor M(4,5,5) algorithm, byte-pinned at
[`../2026-10-21-external-grid-seed/factors.json`](../2026-10-21-external-grid-seed/factors.json).
The original package records the Fawzi et al. Nature (2022) attribution,
the Lille catalogue, Perminov's conversion commit, the upstream notice,
the full tensor convention, and its exact coefficient replay. None of
those external results is new work here. Its interpolation argument also
supplies the rank-four grouping condition used below.

All indices are zero based. Give weight four to the directions indexed by

```
17, 20, 26, 29, 30, 34, 35, 38, 39, 40, 41, 44,
46, 51, 55, 59, 61, 64, 67, 70, 72, 74, 75.
```

Give weight three to every other direction. Write E for this set of 23
indices and w for the weight function. The total weight is

\[
\sum_{i=0}^{75}w_i=3\cdot76+23=251.
\]

The set E was selected during exploratory flat enumeration. The accepted
bound does not assume that discovery calculation. The new exhaustive
replay checks the stated weights directly against every four-dimensional
span.

## Complete finite-field certificate

The C99 program `weighted_flats.c` examines all
\(\binom{76}{4}=1,282,975\) four-subsets over F_101. For each independent
subset it computes the full rank-four span, tests membership of every
one of the 76 vectors, and sums their weights. There are 1,280,087
independent four-subsets. The largest weight found is 24, attained by a
rational rank-four flat as checked separately by `verify.py`.

The following table gives the largest number e of E-directions found in
a flat containing k original directions. The full basis-weighted
histogram and witness are in `enumeration.json`.

| k | Maximum e | Maximum weight 3k + e |
| ---: | ---: | ---: |
| 4 | 4 | 16 |
| 5 | 4 | 19 |
| 6 | 4 | 22 |
| 7 | 3 | 24 |
| 8 | 0 | 24 |

The vectors span dimension 20 over F_101, so every smaller span extends
to one of the enumerated four-dimensional spans. Weights are positive;
the cap therefore applies to every rank-at-most-four set.

Suppose a subset of the integer vectors has rank at most four over C.
All of its five-minors vanish as integers, so they vanish modulo 101.
Its reduced vectors lie in a rank-at-most-four finite-field span, and
the exhaustive bound gives total weight at most 24. All 76 reductions
are nonzero and pairwise nonproportional, as checked separately, so this
argument counts their distinct projective directions correctly. Thus

\[
\boxed{\text{Every complex rank-at-most-four set of original directions
has weight at most 24.}}
\]

The same statement holds over any characteristic-zero field extension,
including a Laurent-series field: the rank of a rational matrix does
not change on extending its field. A common invertible change of basis
and individual nonzero rescalings preserve every rank and projective
incidence in this configuration.

## Consequence for the Q(6,4) evaluation grid

In the specified leg alignment, interpolation represents Q(6,4) by a
9-by-9 grid. For fixed second node, one long-leg factor lies in a space
of dimension at most four. Consequently any termwise assignment of an
algorithm to this grid covers all of its distinct directions on that
leg by nine rank-at-most-four groups. This necessary condition survives
arbitrary linear source maps and invertible target changes of basis.
See the original seed package for the three evaluation factors and
the target-leg alignment.

Let D be the original directions absent after replacements, and suppose
every remaining direction is one of the original 76. Subadditivity of
the weight of a union gives the necessary condition

\[
251-\sum_{i\in D}w_i\le9\cdot24=216.
\]

Writing \(r=|D|\) and \(e=|D\cap E|\), every such candidate must satisfy

\[
\boxed{3r+e\ge35.}
\]

In particular, r<=8 is impossible. With r=9 one needs e>=8; with r=10,
e>=5; with r=11, e>=2. These are only necessary bounds; no sufficiency or
optimality is claimed.

For the four-split construction the substitutions are

\[
u_0\mapsto-u_{18},\quad u_{17}\mapsto u_8,\quad
u_{48}\mapsto-u_2,\quad u_{56}\mapsto-u_{22}.
\]

All four destination directions remain present. The deleted set is
D={0,17,48,56}, whose weight is 13. Its 72 remaining directions have
weight 238>216, so this particular seed cannot be assigned termwise to
the grid. The common physical Laurent transformations used in that
construction preserve this exclusion over C((epsilon)). This says
nothing against the validity of that border decomposition; it only
rejects the proposed termwise reuse through this source grid.

## Reproduction and scope

From the repository root:

```sh
python research/ai/2026-10-23-grid-escape/verify.py
python research/ai/2026-10-23-grid-escape/verify.py --enumerate
python -m unittest discover -s tests -p 'test_weighted_grid_escape.py' -v
```

The first command validates source identity, the stored runs' counters,
both rational extremal witnesses, the source spans, projective
distinctness, and the four-split application. It explicitly reports that
it has not rerun the exhaustive searches. The second compiles the C99
program in a temporary directory and repeats every four-subset for both
legs, comparing the entire outputs with the retained reports. The tests
also run that full replay
when a C compiler is available; otherwise only that test is skipped.

The `deletion_screen` function scores proposed deleted sets for use in
construction search. It reports a failed necessary condition separately
from a constructed grid, which it never asserts. The finite computation,
proof, and replay are same-session AI-derived work. They have no
independent mathematical review or formalization.
