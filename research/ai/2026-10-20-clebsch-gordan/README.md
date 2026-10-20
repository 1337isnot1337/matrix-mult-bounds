# Full recoupling coefficients and certified outer-weight searches

2026-10-20. AI-derived finite experiments and exact coefficient certificates;
no independent review, no Lean formalization, no exponent improvement.

The earlier fixed-label and full-leading-entropy investigations suppress all
blocks k>i+j. This package keeps them using the equivariant polarization lift

    u^(p+q-e) v^e -> sum_(f+g=e)
        binom(p,f) binom(q,g) / binom(p+q,e)
        * u^(p-f) v^f s^(q-g) w^g,

and multiplies by (uw-vs)^i at filtration order i, using degrees p-i,q-i
inside the lift. The diagonal substitution of each order-zero lift is its
displayed monomial; positive-order terms are in the determinant ideal.
The successive quotient argument proves these are bases. Polarization is
equivariant for the diagonal SL2 action, so these are the usual
Clebsch--Gordan components. This representation-theoretic description is
standard, not a historical novelty claim.

`cg_blocks.py` expands every input-basis product and solves the exact output
basis transformation in each homogeneous weight space. It records nonzero
blocks beyond the associated graded. A block is identified with a convolution
only after exact support comparison, axis permutation/reversal, and rational
diagonal-factor verification. Interior blocks use a dot-product restriction;
the strengthened run also checks interval-coordinate convolution restrictions.

For example, C(3,3)^2 has 14 nonzero recoupling blocks. The (0,0,2) block has
dimensions (5,5,5), is not itself a convolution, and has a certified C(3,3)
restriction. This improves its lower score from the coordinate dot bound 5
to the matching convolution value 56/9. The recorded restriction contains
its exact offsets, axes and rational factors.

`cg_search.py` searches normalized input-label weights and sets each output
weight to the negative of its minimum input weight. Every retained block is
an actual zero-weight block. It also permits every nonempty output-label
subset. Connected components on all three legs give full direct sums;
components on two legs give matched sectors sharing the remaining leg.
Each component is scored recursively. Unknown pieces use only proved
restrictions; no convolution value is assigned from dimension alone.

At t=3/4, all score decisions use integer intervals with scale 2^80. Sums on
a shared leg are ordinary sums. A full direct sum applies the 4/3 power to
a sum of 3/4 powers. Integer square/fourth/cube roots bound every such
operation. The report's lower bound comes with a specific expression tree;
its upper bound covers all component decompositions considered by the code.
No floating-point comparison is used for acceptance.

Completed coverage:

| Run | Sources | Distinct scored supports | Result |
| --- | ---: | ---: | --- |
| Binary input-label weights, grid 2..4 modulo source symmetries | 27 | 41,729 | No P_* violation; no ambiguous intervals |
| Ternary input-label weights, six listed sources | 6 | 99,110 | No P_* violation; no ambiguous intervals |
| Binary weights with stronger interval-coordinate restrictions, five sources | 5 | 24,505 | No P_* violation; no ambiguous intervals |

These counts overlap across runs. They are not counts of distinct tensor
isomorphism classes. The source symmetries used for the first run are
simultaneous exchange of the two tensor factors and simultaneous exchange
of the two input legs. They cover all 81 ordered tuples in {2,3,4}^4.
The original six-source binary pilot is retained separately.

The strongest pilot ratio is 23/25 at source C(2,2)^2, from the valid bound
P(2,2)^2 >= P(3,3)+P(3,1)+1. The ratio uses P_* as the comparison profile.
It does not contradict a source rank bound or prove an exponent improvement.

## Reproduction

```sh
python research/ai/2026-10-20-clebsch-gordan/cg_blocks.py
python research/ai/2026-10-20-clebsch-gordan/cg_search.py --alphabet 0,1,2 --output /tmp/full-cg-ternary.json
python research/ai/2026-10-20-clebsch-gordan/cg_search.py --strengthen --output /tmp/full-cg-strengthened.json
python -m unittest discover -s tests -p test_clebsch_gordan.py -v
```

The grid report records its explicit source list. Reproduce each list with
the `--sources` option. SymPy 1.14.0 is the only nonstandard dependency.
The original archive is unchanged. Tensor multiplication, character rules,
the growth recurrence and the external 9/4 theorem remain attributed to
OpenAI at commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. The matching
profile comes from the repository's first pass.

The search does not exhaust rational weights, changes of basis inside a
block, partitions into subblocks, tensor powers, or all character profiles.
The next active source family uses a smaller rank bound rather than simply
increasing this grid; see the truncated-algebra investigation.
