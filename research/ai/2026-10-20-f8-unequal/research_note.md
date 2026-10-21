# Unequal F8 normal-coset bounds and nonlinear graph experiments

October 21, 2026. AI-GROUP-F8-UNEQUAL-014 and EXP-GROUP-F8-GRAPHS-015.
Written proof with finite certificates, unreviewed. No exponent improvement.

## 1. Result and scope

Let G have a normal subgroup H isomorphic to C2^6 and quotient C7. There
are no vertex families of sizes at least (16,16,26), in any order, giving
a matrix target through injective pair maps and strict vertex potentials.
This concerns the same construction frame as the
[balanced size-nineteen theorem](../2026-10-20-normal-coset-koszul/rectangular_note.md).
It includes empty fibers, nonlinear four-point fibers, all directions and
all offsets. General complex tensor degenerations are outside this proof.

The new calculation uses explicit five- and seven-slice Koszul maps and
cyclic averaging. The maps and their border-rank interpretation are
classical; see Landsberg and Ottaviani, *New Lower Bounds for the Border
Rank of Matrix Multiplication*, Theory of Computing 11 (2015),
[article and paper](https://theoryofcomputing.org/articles/v011a011/).
The local contribution is the stated finite pencils and the unequal
normal-coset application. No new general tensor-rank inequality is claimed.

## 2. Higher rectangular Koszul bound

Write a,b,c for the three normal-fiber count arrays in quotient order C7.
Restrict all three group-tensor legs to H. As in the earlier proof, the
target is the direct sum of blocks M(a_i,b_i,c_i), while the restricted
source has complex rank |H|=64 by Fourier transformation. Independent
right translations of the three vertex families allow independent cyclic
shifts of their arrays, preserving all pair maps and potential conditions.

For d=2p+1 integer matrices X_t of size a by b, form the map

```
K_p(X): wedge^p C^d tensor C^b -> wedge^(p+1) C^d tensor C^a
        w tensor v |-> sum_t (e_t wedge w) tensor X_t v.
```

For a decomposable tensor this map has rank at most binomial(2p,p):
wedge multiplication by one nonzero vector has that rank, and the
remaining matrix factor has rank at most one. Therefore border rank r
implies Koszul rank at most r*binomial(2p,p). This remains valid after a
linear map on the first leg, and under degeneration because matrix-rank
upper bounds are closed polynomial conditions.

One M(a,b,c) block is c copies of this pencil on the remaining legs.
The first-leg projections can be chosen separately on each direct-sum
block. Thus certified ranks r_p(a,b) imply the necessary inequality

```
sum_i c_i r_p(a_i,b_i) <= 64*binomial(2p,p),                 (1)
```

for all cyclic alignments and all cyclic choices of the first leg.
The zero row and column of each rank table are zero. Exact modular ranks
of explicit integer matrices are lower bounds over C: a nonzero minor
modulo the prime101 is a nonzero integer minor. No generic-rank or
maximality claim is needed.

The certified nonzero tables, indexed by a,b=1,...,4, are

```
p=2, d=5, rank-one divisor6:
  6  9 10 10
  9 16 20 20
 10 20 30 30
 10 20 30 40

p=3, d=7, rank-one divisor20:
 20 30 34 35
 30 52 65 70
 34 65 90 105
 35 70 105 140
```

All32 pencils, their coefficients, dimensions, deterministic discovery
seeds and exact modular ranks are in
`results/f8-unequal-2026-10-20/koszul-pencils.json`. The verifier rebuilds
every matrix, validates integer coefficients and redoes Gaussian
elimination. Tests also compare full-first-space cases with an independent
existing padded Koszul formula, check the decomposable rank divisor, and
check the c-column repetition.

## 3. Complete (16,16,26) exclusion

Restrict to exactly16,16,26 vertices. Each family has a normal fiber with
at least three vertices since each total exceeds14. The earlier normal
unique-sum lemma then bounds every fiber by four: three-point subsets
of two other fibers have independent two-dimensional difference spaces;
their sum is a four-dimensional subspace of F2^6, and the remaining
fiber meets each of its four cosets at most once. This also applies to
non-affine four-point fibers.

There are7140 arrays in {0,...,4}^7 of total16, forming1020 cyclic classes.
The verifier constructs the classes and independently checks coverage by
the coefficient of x^16 in (1+x+...+x^4)^7. None has a shorter orbit,
because16 is not divisible by7.

For every unordered pair of these classes, including repeated classes,
the exact table above satisfies

```
max_s sum_i r_3(a_i,b_(i+s)) >= 345.                        (2)
```

All520710 pairs and their seven relative alignments are recomputed.
The receipt gives a complete histogram and a pair attaining345; the
minimum is345, not350. These are lower ranks of the displayed pencils,
so this statement does not assert a sharp tensor rank.

Fix an alignment satisfying(2). Averaging the third array, of total26,
over its seven shifts gives

```
average_t sum_i c_(i+t) r_3(a_i,b_i) >= 26*345/7 = 8970/7
                                             > 1280 = 64*20.
```

Some alignment violates(1). This proves the stated construction exclusion.
Restriction to smaller vertex subfamilies proves the version with larger
side sizes. This is a written, unreviewed proof with a complete finite
certificate, not an independently reviewed or formalized theorem.

## 4. Remaining unequal frontier and actual experiments

The maintained source-frontier script checks all4811 sorted integer
shapes with a>=2 and b*c<=448. The exact source-degree gate is

```
(a*b*c)^(3/4) > 7 + 9*7^(9/4).
```

It holds for59 shapes; the existing general complex rank-locus bound
leaves26. Their twelve componentwise minimal shapes are recorded in
`source-frontier.json`. This uses the existing source degrees and
rank-locus proof without changing their status. The present theorem
closes one of those minimal shapes in the stated coordinate construction
frame. The balanced theorem closes another. Neither excludes arbitrary
complex degenerations of the group algebra.

The counts

```
S = (0,0,0,4,4,4,4)
T = (0,4,4,0,4,4,4)
U = (3,3,3,3,3,3,3)
```

have totals(16,20,21). Independent replay of every cyclic alignment and
all three first-leg choices gives maximum certified ranks108,360,1260
for p=1,2,3, below source ceilings128,384,1280. All pair-capacity sums
are at most64. These counts survive only necessary tests. No directions,
offsets, pair maps or potential have been constructed for them.

The optional native-parity search rotates these counts independently to
place nonempty fibers at the identity, fixes one of two complementary
base frames, and allows each later fiber to be a graph over its own
two coordinates. The four-point graph values are independent, allowing
non-affine fibers; all offsets are explicit. This graph parameterization
and its two base frames do not cover all possible vertex families.
Its Boolean encoding is audited on a triangular nonlinear normal control;
that control fails pair injectivity, which is recorded explicitly.

Actual reports:

| Report | Completed outcome | Exact target witnesses |
| --- | --- | --- |
| graph-16-20-21-generic.json | solver-reported UNSAT in56.25s, no proof trace | 0 |
| graph-16-20-21-dual.json | time limit, elapsed214.35s including encoding and cooperative solver overrun | 0 |
| graph-control.json | exact full-support (4,4,3) positive control | 1 control only |

The positive control has48 intended terms and no unwanted terms, checked
again by the independent integer full-support verifier. It is far below
the exponent gate. The search reports do not prove nonexistence, and no
result here improves the arithmetic exponent9/4.

## 5. Reproduction

From the repository root, with its maintained verification dependencies:

```sh
python research/ai/2026-10-20-f8-unequal/koszul_tables.py --output results/local/f8-pencils.json
python research/ai/2026-10-20-f8-unequal/pair_averaging.py results/f8-unequal-2026-10-20/koszul-pencils.json --output results/local/f8-pair-averaging.json
python research/ai/2026-10-20-f8-unequal/f8_source_frontier.py --output results/local/f8-source-frontier.json
python -m unittest discover -s tests -p test_f8_unequal.py -v
```

Discovery additionally needs optional python-sat, pycryptosat5.17.0,
NumPy and SciPy; CI does not import these modules. To repeat a bounded
experiment, use `graph_search.py --base generic --seconds 180 --max-models 50
--output results/local/f8-generic.json`, replacing generic by dual for the
other frame, or adding `--control` for the small positive control. Actual
solver timings and timeout outcomes need not repeat. Acceptance always
requires full-support exact verification; UNSAT without a checked trace
remains an experiment.
