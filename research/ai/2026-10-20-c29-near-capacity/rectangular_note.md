# Unequal targets close the one-source C29:C4 degree-sum route

October 20, 2026. AI-GROUP-C29-RECTANGULAR-010. Written proof, unreviewed.
No smaller matrix multiplication exponent follows.

## Statement

No single matrix target from C29:C4 through the injective-pair-map and
strict-vertex-potential construction passes the usual source degree-sum
gate at a positive exponent at most 9/4.

This extends the [size-ten obstruction](research_note.md), whose exact
three-point classification and reduction are reused here. The two additional
ordered targets are (9,9,11) and (9,10,10). The conclusion excludes no
general tensor degeneration, simultaneous extraction, or tensor-power
construction. It concerns the stated source cost as well as the stated
construction class.

## Complete one-source frontier

The source has four irreducibles of degree one and seven of degree four.
The free scalar action on the 28 nonzero additive dual characters gives
seven orbits of size four; the quotient C4 supplies the four linear
characters. The degree squares sum to 116. This uses the same standard
complex semidirect-product representation argument recorded in the group
source campaign.

Let a<=b<=c be target sizes. Pair injectivity gives bc<=116. The exact
degree-sum checker covers all 512 sorted shapes with a>=2 and bc<=116,
using integer-root rational intervals at 9/4. If a=1, the volume is at most
116 and cannot pass the gate, since
116^3 < (4+7*4^2)^4 = 116^4 and the source cost at 9/4 exceeds 116.

Every improving shape is screened with the earlier, written and unreviewed
[rank-locus theorem](../2026-10-20-group-potentials/rank_locus_proof.md):

```
116 >= bc + D(a-1),
D(r) = max sum_i k_i(2d_i-k_i),   sum_i d_i k_i <= r.
```

Only (9,9,11), (9,10,10), and (10,10,10) survive. The exact report is
`source-frontier.json`; it retains every improving shape and its rank-locus
decision. The last shape is already excluded in the stated coordinate
construction class by the size-ten proof.

Sorting is legitimate for this construction: cyclic family permutation
preserves the trace identity. Reversing family order inverts and reverses
the three pair labels, preserving support and injectivity; negating the
vertex potentials restores strict positivity. Thus all permutations of
the three sizes have equivalent construction status.

## Unequal fiber patterns

For either new target every family has a fiber of size at least three.
Normal-fiber unique sums and 3*3*4>29 force every fiber size to be at most
three. Each family has a three-point fiber. The earlier classification
therefore still forces every three-point fiber to be an arithmetic
progression and gives the same six ordered base-direction cases.

After independently moving a chosen largest fiber to scalar one, the size
patterns, including all permutations of the remaining positions, are:

| Family size | Unordered four-fiber patterns |
| --- | --- |
| 9 | (3,3,3,0), (3,3,2,1), (3,2,2,2) |
| 10 | (3,3,3,1), (3,3,2,2) |
| 11 | (3,3,3,2) |

`fiber_frontier.py --shape ...` enumerates every direction assignment in
the necessary domains, including separate directions in every short fiber.
An empty fiber contributes an empty mask. Its center is immaterial, so all
center values are allowed; this cannot reject a genuine offset assignment.
The complete cyclic packing checker accepts the zero mask's singleton
translation orbit.

All pair-quotient tests and normal-fiber constraints leave 392 configurations
for (9,10,10) and 48 for (9,9,11), across all six bases. Their cached packing
counts are respectively 99,648 and 214,292. These remain local configurations.

## Identity gluing rejects every local configuration

The earlier identity-quotient relation

```
v_ST + v_TU + v_US = 0 in F29^3
```

still holds. If a fiber is empty, give its unused offset an arbitrary value;
the telescoping relation remains true, while its empty mask imposes no
extra condition. Thus the relation remains necessary in the relaxed model.

`rectangular_gluing.py` computes every pair's full relative-translation list.
It joins the two shortest lists and tests the uniquely required third
vector for membership in the third complete list. This covers all possible
coherent triples without iterating impossible third-vector choices.
No coherent triple exists for any of the 440 local configurations. Together
with the complete direction filter, this excludes both new targets.

All three sorted frontier shapes are therefore excluded in the stated
construction class. Every other shape either fails the source gate or the
rank-locus necessary condition.

For completeness, failure of the 9/4 source gate also rules out passing
that same gate at a smaller positive exponent. For volume V>4^3, every
ratio d_i/V^(1/3) is less than one, so decreasing the exponent increases
their power sum. If V<=4^3, even one degree-four source block costs at least
V^(s/3) for s>0. This argument does not exclude an improved source-cost
algorithm or an extraction from powers.

## Reproduction

From the repository root, using Python 3.10 or later:

```sh
python research/ai/2026-10-20-c29-near-capacity/source_frontier.py \
  --output results/local/c29-source-frontier.json
python research/ai/2026-10-20-c29-near-capacity/fiber_frontier.py \
  --shape 9 10 10 --output results/local/c29-9-10-10-frontier.json
python research/ai/2026-10-20-c29-near-capacity/rectangular_gluing.py \
  --source results/local/c29-9-10-10-frontier.json \
  --output results/local/c29-9-10-10-gluing.json
```

Repeat the last two commands with shape 9 9 11. Committed full reports are
in `results/c29-near-capacity-2026-10-20/`; the dedicated rectangular test
replays both complete frontiers and their gluing checks. No optional solver
or new dependency is needed. No review or formalization is implied by tests.
