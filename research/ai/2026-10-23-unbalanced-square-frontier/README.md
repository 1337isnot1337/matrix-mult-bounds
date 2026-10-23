# Complete unbalanced ordinary square-sum frontier through dimension 1377

October 23, 2026. Owner-directed OpenAI Codex continuation. Written finite
application of prior unreviewed proofs; no independent mathematical review,
formalization, target construction or smaller exponent is claimed.

The previous Hankel application screened balanced A8 and A9 but left the
unbalanced source formats between dimensions 960 and 1377 undecided. This
package applies the same necessary conditions to **every** source A(a,b)
with 2<=a<=b and N=ab(a+b-1)<=1377, every target leg dimension 1<=D<=N,
and every square partition of D. There are 82 source formats and 52310
target dimensions. Twenty source formats have N>960.

All 70 source formats with N<1152 are excluded for an improving ordinary
square direct sum by the accumulated written gate proofs and exact finite
recurrence. The first necessary-test survivor is **A(8,9), N=1152**.
Only A(8,9) and A(9,9) survive through N=1377. The earlier balanced
A9 partition (32,6,3) retains its prior credit and open status.

| Source | N | Relaxed maximizing partition | Exact score upper numerator, denominator 10^6 | Critical score |
| --- | ---: | --- | ---: | ---: |
| A(7,10) | 1120 | (29,6,3,1,1,1) | 113971205203 | 117649 |
| A(8,9) | 1152 | (30,3,2,1,1) | 119724129494 | 117649 |
| A(8,10) | 1360 | (32,4,4) | 139773065248 | 140608 |
| A(9,9) | 1377 | (32,6,3) | 141065173366 | 140608 |

These are maxima of a relaxation, not realizable targets. In particular,
the simpler ordinary target A(8,9) -> M30 passes every implemented gate.
Its three leg dimensions are 900, the loss per long leg is252, and the
rank-one slice lift upper bound is534. The strongest eligible new Hankel
rank here is r=6; r=7 fails 5r<2(a+b). No extension beyond that strict
hypothesis is used. The M31 single target already fails the r=6 gate.

The exact inequalities

    180^9 > 49^12,
    180^5621 > 49^7500,
    4*5621 < 9*2500

certify the improving score and the **conditional** exponent bound
omega<=5621/2500=2.2484 if the ordinary M30 maps are constructed. The
existing character comparison is 180^omega<=49^3 under that premise.
The maps remain missing. No actual bound below9/4 follows from this screen.

## Exhaustive finite reduction

Use the prior [square-sum recurrence](../2026-10-20-anisotropic-constructions/square_sum_frontier.md)
and [Hankel application](../2026-10-21-hankel-pencil-degree/application.md),
including their original attribution and mathematical limitations.
For each source and dimension, retain exactly the existing minimum-rank,
rank-two equality, fixed-scheme, first-boundary and linear-annihilator
gates. The last gate excludes a size-n block only when, for some integer r,

    1<=r<min(a,b), 5r<2(a+b),
    n^2 > ab*max(r,max(1,floor((3r-a-b+4)/2))^2),
    n+2(N-D) < (r+1)ab.

All inequalities that were strict in the adopted theorem remain strict.
No square partitions are assumed balanced, irredundant or scalar-free.
One scalar and repeated scalars retain the prior separate rank gates.

For each allowed n, the old integer fourth-root routine supplies an exact
upper numerator for (6n)^(9/4) with denominator10^6. The unmodified
dimension-first unbounded knapsack covers all square partitions of D;
when at most one scalar is permitted, compare the nonscalar optima at
D and D-1. Unreachable dimensions are explicit nulls. The maximum over
all D is an upper bound on every ordinary square direct-sum score for
that source. Exclusion requires this upper bound to be strictly below
[3(a+b)-2]^3. A lower interval for the saved maximizing partition also
checks that neither passing classification results from interval rounding.

The source enumeration is complete: a>=10 already gives N>=1900 and
b>=26 gives N>=1404 for a>=2. The loops enumerate each remaining pair
until the monotone size bound fails. Exchanging a,b adds no new format.
The report stores an exact optimum upper numerator for every D, the
source maximum with a partition witness, all eligible new Hankel gates,
and the explicit conditional M30 comparison.

The tests independently enumerate the source rectangle, implement every
gate directly, and recompute all52310 dimension scores with an item-first
knapsack grouped by equal allowed-size sets. This differs from the
dimension-first generating recurrence. They also check the fourth-root
intervals, every saved maximum and partition, the passing classifications,
strict theorem boundaries, source pins and package hashes. Computation
certifies the finite application; it does not review the imported proofs.

## Reproduction and remaining questions

With root requirements.txt installed, from the repository root:

```sh
python research/ai/2026-10-23-unbalanced-square-frontier/verify.py --output results/unbalanced-square-frontier-2026-10-23/frontier.json
python -m unittest discover -s tests -p test_unbalanced_square_frontier.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

Investigate actual ordinary M30 maps for A(8,9), a stronger obstruction
valid in that format, or singular constructions outside the ordinary
screen. The A9 M32 equality question remains distinct. This package
does not cover a=1, rectangular direct sums, N>1377, source powers,
general singular degenerations or alternative score inequalities.
The original proofs, archives and historical frontier reports are unchanged.
