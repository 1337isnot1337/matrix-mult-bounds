# Cartan block flattenings and a quantum quotient target

October 20, 2026. EXP-CYCLIC-BLOCK-FLATTENINGS-054 and
AI-CYCLIC-ROOT-MODULES-053. Finite exact screens and a written representation
calculation, unreviewed. **No exponent improvement is established.**

The selected family from [the size-five frontier](../2026-10-20-cyclic-equivariant/a5.md)
is A3 to M(6,6,7), A4 to M(10,10,11), and A5 to M(14,14,15), with the
specified matrix-vertex Cartan characters. A necessary restriction on every
individual weight block is easy to miss when fitting the full maps. This
package checks those blocks with Koszul flattenings and records a
[root-of-unity realization](root_quotient.md) of the formal vertex character.
Neither supplies the missing simultaneous maps.

## Block conventions and exact rank directions

Use source coordinates A=(i,k,s), B=(j,p,L), C=(H,q,r), with terms at
k=p+q, L=r+s, H=i+j. Their Cartan weights are k-i-s, L-j-p, H-q-r.
Every term has total weight zero. Two additional integer grades are

    A: (i,k), B: (j,-p), C: (-H,-q).

Their sums vanish as well, checked on every coefficient. Fix a triple
(alpha,beta,gamma) of Cartan weights. The source block is an integer
0/1 tensor with dimensions (m,b,c). A weight-preserving degeneration
would restrict to a degeneration on this block.

For p=0,...,m-1, its Koszul map is

    Lambda^p A tensor B* -> Lambda^(p+1) A tensor C.

The two residual grades decompose its rows and columns into independent
blocks. If d_w and e_w are their dimensions, its rational rank is at most
sum_w min(d_w,e_w). The exterior-weight multiplicities are computed by
an exact subset-count recurrence. This is an upper bound, not a claim
that every grade block has maximal rank.

For selected powers we additionally construct the actual integer map
modulo two. Its rank there is a lower bound for its rational rank.
Thus a modular source rank at least the exact target rank certifies that
this rank comparison does not exclude the target over C. A small modular
rank would not by itself be a complex obstruction.

For target vertices with multiplicities U_i,V_j,W_k, the block is the
direct sum of M(U_i,V_(i+alpha),W_(i+alpha+beta)) over all valid i.
We use the [maintained matrix Koszul formula](../2026-10-20-paired-sources/all_ranks.py)
with first-leg padding to the source dimension. For a direct sum,
the B/C spaces separate, so these padded ranks add. The source's target
weight spaces can have unused rows in an individual block; the padding
is essential. Independent small controls build the original matrix tensor
coefficient by coefficient before partitioning its weights.

## Completed coverage

| a | All-power grading comparisons | Actual modular rank comparisons |
| --- | ---: | ---: |
| 3 | 1017 | 555 |
| 4 | 3672 | 1308 |
| 5 | 9675 | 2061 |
| Total | 14364 | 3924 |

Every nonempty target block and all three cyclic first-leg choices are
included. Every allowed exterior power is covered by the grading bound.
The modular powers are 0 through 2 when available, additionally power 3
when its domain dimension is at most 10000; for first-leg dimension at
most ten, they are 0 through floor((m-1)/2).

Every grading upper bound is at least its target rank. Every computed
modular source rank is also at least its target rank. Therefore none of
these completed comparisons excludes the candidate. The remaining grading
comparisons may still conceal rank defects; no maximal-rank assertion is
made. Joint blocks, other flattenings, other characters, and the actual
simultaneous coefficient equations remain untested here.

The compressed JSON records every comparison and the exact target shapes.
No floating arithmetic, external numerical solver, or inferred zero is
used. Earlier scratch sweeps are superseded by this combined retained
coverage; repeated comparisons are not counted as separate results.

## Reproduction

```sh
python research/ai/2026-10-20-cyclic-weight-blocks/blocks.py --output results/local/weight-blocks.json.gz
python research/ai/2026-10-20-cyclic-weight-blocks/root_quotient.py
python -m unittest discover -s tests -p test_cyclic_weight_blocks.py -v
```

Use the root requirements. The quantum arithmetic and the exact matrix
Koszul formula are adopted from the other worker's maintained packages;
this package contributes their specified block application and target
quotient calculation. Their checks and these checks are not independent
mathematical review. General degenerations remain open.
