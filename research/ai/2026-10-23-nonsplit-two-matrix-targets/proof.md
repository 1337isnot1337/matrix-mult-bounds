# Fifth- through seventh-power checks of two-matrix targets for the nonsplit source

October 23, 2026. This is finite, owner-directed Codex research. The prior
two-matrix frontier is an input ledger; its earlier screen generators were
not retained. The exact power-five comparison checks all 144 rows, the
power-six comparison checks the 136 rows not excluded at power five, and
power seven checks the 126 rows left after power six. No
target is constructed, and no matrix-multiplication exponent improvement
is established. Source hashes and inherited proof statuses are in
`SOURCES.json`.

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

## Sixth-power source and target comparison

For six source factors, the same weighted block cover uses
`P(t)^j [16(1+t^h_j)]^(6-j)` with degree ceiling `D_j=8j+h_j(6-j)`.
The source cover generator searches integer weights `1<=h_j<=48` for each
row and chooses exact three-cutoff covers. The search range is a discovery
choice only; the certificate claims validity of the displayed cover, not
optimality among all weights. Its rows are:

| Principal factors `j` | Words | `h_j` | `D_j` | Cutoffs | Slices per word |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0 | 1 | 1 | 6 | 1, 1, 2 | 603,979,776 |
| 1 | 6 | 2 | 18 | 5, 5, 6 | 1,581,252,608 |
| 2 | 15 | 3 | 28 | 8, 9, 9 | 3,678,601,216 |
| 3 | 20 | 3 | 33 | 10, 10, 11 | 8,846,524,416 |
| 4 | 15 | 3 | 38 | 12, 12, 12 | 21,132,582,912 |
| 5 | 6 | 3 | 43 | 13, 14, 14 | 51,315,871,232 |
| 6 | 1 | unused | 48 | 15, 15, 16 | 124,081,743,648 |

As before, each row has cutoff sum `D_j-2`, so every degree triple with
total at most `D_j` is covered. After applying word multiplicities, the
verified bound is

    SR_F4(T_SL2F5^tensor(6)) <= 991,166,716,704.

The independent degree-class replay checks all `11^6 = 1,771,561` ordered
class tuples, all 64 block words, `120^6 = 2,985,984,000,000` coordinate
tuples with multiplicity, and 333,047 degree triples under the stated
cutoffs.

The sixth target power has 64 direct-sum matrix multiplication terms for
each orientation multiset. There are 462 multisets of six orientations from
the six permutations. Simultaneous reordering of the three output legs
partitions them into 83 exact orbits: 72 of size six, nine of size three,
one of size two and one fixed orbit. The verifier checks that these orbits
partition all 462 cases before scoring their representatives. Of the 136
power-five non-exclusions, ten now exceed the power-six source bound:

| Ledger row | Two matrix shapes | Target slice rank | Gap |
| ---: | --- | ---: | ---: |
| 78 | `M(2,3,5)`, `M(9,10,10)` | 1,000,752,840,000 | 9,586,123,296 |
| 79 | `M(2,3,5)`, `M(10,9,10)` | 995,858,550,000 | 4,691,833,296 |
| 83 | `M(2,3,6)`, `M(10,9,10)` | 1,013,406,391,296 | 22,239,674,592 |
| 86 | `M(2,3,7)`, `M(10,10,9)` | 999,649,773,936 | 8,483,057,232 |
| 87 | `M(2,3,8)`, `M(10,10,9)` | 1,015,462,086,336 | 24,295,369,632 |
| 95 | `M(2,4,4)`, `M(11,9,9)` | 1,008,949,613,377 | 17,782,896,673 |
| 120 | `M(3,4,6)`, `M(9,10,9)` | 1,012,242,942,288 | 21,076,225,584 |
| 121 | `M(3,4,6)`, `M(10,9,9)` | 1,003,081,686,768 | 11,914,970,064 |
| 127 | `M(3,6,7)`, `M(10,8,9)` | 1,021,165,849,800 | 29,999,133,096 |
| 131 | `M(4,4,7)`, `M(9,9,9)` | 1,003,324,305,217 | 12,157,588,513 |

The remaining 126 candidates are not excluded by this sixth-power check.
They are not shown to survive all degenerations or to be constructible.

## Seventh-power source and target comparison

For seven source factors, use `P(t)^j [16(1+t^h_j)]^(7-j)` with degree
ceiling `D_j=8j+h_j(7-j)`. The producer searches weights `1<=h_j<=48`
and selects explicit cutoff triples. This finite weight search is not a
global source-cover optimality claim.

| Principal factors `j` | Words | `h_j` | `D_j` | Cutoffs | Slices per word |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0 | 1 | 1 | 7 | 1, 2, 2 | 17,716,740,096 |
| 1 | 7 | 3 | 26 | 8, 8, 8 | 43,234,885,632 |
| 2 | 21 | 3 | 31 | 9, 10, 10 | 108,573,753,344 |
| 3 | 35 | 3 | 36 | 11, 11, 12 | 261,325,914,112 |
| 4 | 35 | 3 | 41 | 13, 13, 13 | 623,768,764,416 |
| 5 | 21 | 3 | 46 | 14, 15, 15 | 1,518,375,598,080 |
| 6 | 7 | 3 | 51 | 16, 16, 17 | 3,678,006,655,344 |
| 7 | 1 | unused | 56 | 18, 18, 18 | 8,860,016,290,395 |

Each cutoff sum is `D_j-2`. The full integer degree-class replay checks
`11^7 = 19,487,171` ordered class tuples, all 128 block words,
`120^7 = 358,318,080,000,000` coordinate tuples with multiplicity, and
607,328 degree triples under the cutoffs. After applying word
multiplicities, it gives

    SR_F4(T_SL2F5^tensor(7)) <= 100,070,673,945,707.

The seventh target power has 792 multisets of seven orientations. Their
common-leg symmetry orbits partition into 132 orbits, all of size six.
Among the 126 power-six non-exclusions, exactly one exceeds the source
bound:

| Ledger row | Two matrix shapes | Target slice rank | Gap |
| ---: | --- | ---: | ---: |
| 129 | `M(3,7,7)`, `M(11,8,8)` | 101,637,778,718,981 | 1,567,104,773,274 |

The other 125 candidates are not excluded by powers five, six or seven.
The largest of their seventh-power values is 98,192,715,899,136, at ledger
row 84 (`M(2,3,6)` and `M(10,10,9)`). It remains below the source bound by
1,877,958,046,571. This remains only a finite obstruction screen.

## Limits and reproduction

These are exact exclusions for 19 recorded candidates in the maintained
one-copy complex coefficient-one coordinate/potential class when the
existing characteristic-two good-reduction premise applies. They do not
regenerate the earlier pair orientation, Koszul, profile, or power-three
frontier; those are pinned discovery inputs. All two-matrix targets outside
that ledger, arbitrary complex mixing without good reduction, and the 125
candidates not excluded here remain open. There is no independent
mathematical review, formalization, target construction, or exponent gain.

From the repository root, regenerate and replay with Python 3.10 or later:

```sh
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power5.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power5-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/verification.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power6.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power6-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify_power6.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power6-verification.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/source_power7.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power7-source-cover.json
python research/ai/2026-10-23-nonsplit-two-matrix-targets/verify_power7.py \
  --output results/nonsplit-two-matrix-targets-2026-10-23/power7-verification.json
```
