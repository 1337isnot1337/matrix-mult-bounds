# A fifth-power check of two-matrix targets for the nonsplit source

October 23, 2026. This is finite, owner-directed Codex research. The prior
two-matrix frontier is an input ledger; its earlier screen generators were
not retained. This note proves only the exact power-five source comparison
for the 144 candidates in that ledger. No target is constructed, and no
matrix-multiplication exponent improvement is established. Source hashes
and inherited proof statuses are in `SOURCES.json`.

## Exact source upper bound

Use the degree labels of the full 120-dimensional `F4` basis for the actual
`SL(2,F5)` source. The inherited dense verifier checks the complete source
trace tensor, all `120^3 = 1,728,000` coefficients, both block degree
bounds, and the absence of cross-block terms. The degree polynomial of the
88-dimensional principal block is

    P(t) = 9 + 8t + 10t^2 + 8t^3 + 18t^4 + 8t^5
           + 10t^6 + 8t^7 + 9t^8,

and the other 32 basis vectors have polynomial `16(1+t)`.

For a word with `j` principal factors among five tensor factors, weight each
degree in the 32-dimensional block by `h_j`. The resulting one-leg
polynomial is

    P(t)^j [16(1+t^h_j)]^(5-j),

with degree ceiling `D_j = 8j + h_j(5-j)`. If the three grouped tensor
legs have cutoffs `c_1,c_2,c_3` with `c_1+c_2+c_3 >= D_j-2`, every source
term is covered: a term avoiding all three cutoff sets would have degree
at least `(c_1+1)+(c_2+1)+(c_3+1) >= D_j+1`.

The exact integer cover is:

| Principal factors `j` | Words | `h_j` | `D_j` | Cutoffs | Slices per word |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0 | 1 | 1 | 5 | 1, 1, 1 | 18,874,368 |
| 1 | 5 | 4 | 24 | 7, 7, 8 | 51,904,512 |
| 2 | 10 | 3 | 25 | 7, 8, 8 | 127,193,088 |
| 3 | 10 | 3 | 30 | 9, 9, 10 | 300,936,960 |
| 4 | 5 | 3 | 35 | 11, 11, 11 | 715,663,968 |
| 5 | 1 | unused | 40 | 12, 13, 13 | 1,736,327,596 |

Multiplying each per-word count by its word multiplicity gives

    SR_F4(T_SL2F5^tensor(5)) <= 9,874,344,844.

The producer convolves integer degree histograms. A separate verifier
counts all `11^5 = 161,051` ordered tuples of one-leg degree classes, checks
the 32 block words, and accounts for all `120^5 = 24,883,200,000`
coordinate tuples with multiplicity. It verifies every degree triple under
the six stated cutoffs. This is a finite upper bound, not a source-cost
optimality claim or an asymptotic estimate.

## Exact slice rank of the fifth target power

Write the two-component target as

    U = M(a_0,b_0,c_0) direct_sum M(a_1,b_1,c_1).

Its fifth tensor power expands as the direct sum over all 32 words
`epsilon in {0,1}^5`. For a word `epsilon`, the corresponding summand is

    M(A,B,C),  A=product_i a_(epsilon_i),
                   B=product_i b_(epsilon_i),
                   C=product_i c_(epsilon_i).

Each factor may independently use any of the six leg permutations supplied
by cyclicity and group inversion. Given such an orientation list
`sigma_1,...,sigma_5`, replace the factor dimensions by
`(a_(epsilon_i), b_(epsilon_i), c_(epsilon_i))` under `sigma_i`. The exact
slice rank is then

    sum_(epsilon in {0,1}^5) min(A*B, B*C, C*A).

This follows from the exact finite-field slice rank of a rectangular matrix
multiplication tensor and Gowers's direct-sum additivity theorem over every
field. A one-copy coefficient-one degeneration with the stated good
reduction would tensor to each such target, so any one of these exact
target ranks above the source upper bound is a contradiction.

The score is unchanged if all three output legs are reordered together.
Thus the 252 multisets of five orientations from the six permutations fall
into 42 orbits of size six. `target_power.py` checks that orbit count and
computes all 32 direct-sum terms with exact integer arithmetic for each
representative. Power-three values are independently cross-checked against
all 144 values in the prior candidate ledger.

Of the 144 candidates retained by that earlier ledger, eight have fifth
power target slice rank strictly above 9,874,344,844:

| Ledger row | Two matrix shapes | Target slice rank | Gap |
| ---: | --- | ---: | ---: |
| 96 | `M(2,4,5)`, `M(11,9,9)` | 10,017,148,547 | 142,803,703 |
| 115 | `M(3,4,5)`, `M(9,9,10)` | 9,943,165,125 | 68,820,281 |
| 122 | `M(3,4,7)`, `M(10,9,9)` | 10,016,741,556 | 142,396,712 |
| 134 | `M(4,5,6)`, `M(9,10,8)` | 10,204,224,000 | 329,879,156 |
| 135 | `M(4,5,6)`, `M(10,9,8)` | 10,129,221,120 | 254,876,276 |
| 138 | `M(4,6,7)`, `M(9,9,8)` | 10,043,781,120 | 169,436,276 |
| 142 | `M(5,7,8)`, `M(9,8,7)` | 10,120,529,531 | 246,184,687 |
| 143 | `M(6,6,9)`, `M(8,8,7)` | 9,879,256,960 | 4,912,116 |

The candidates are recorded in their original leg order; the orientation
maximization includes all permutations. The other 136 candidates are only
not excluded by this power-five comparison. They are not shown to survive
every possible degeneration or to be constructible.

## Limits and reproduction

This is an exact exclusion for eight recorded candidates in the maintained
one-copy complex coefficient-one coordinate/potential class when the
existing characteristic-two good-reduction premise applies. It does not
regenerate the earlier pair orientation, Koszul, profile, or power-three
frontier; those are pinned discovery inputs. All two-matrix targets outside
that ledger, arbitrary complex mixing without good reduction, and targets
that pass the five-power screen remain open. There is no independent
mathematical review, formalization, target construction, or exponent gain.

From the repository root, regenerate and replay with Python 3.10 or later:

```sh
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power5.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power5-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/verification.json
```
