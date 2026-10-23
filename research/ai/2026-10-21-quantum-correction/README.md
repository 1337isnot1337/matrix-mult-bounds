# Exact screens for graded corrections of a prescribed Q(6,4) point

This package studies one fixed ordinary restriction of `Q(6,4)` to
format `(25,20,20)`. It proves two scoped obstructions:

1. No ordinary map preserving the stated integer grading, augmented by
   at most four homogeneous rank-one terms, gives `M(5,4,5)`.
2. Three specified assignments of six homogeneous rank-one terms are
   also excluded, by an exact noncommuting central slice space.

The second conclusion was obtained after four bounded numerical fits
failed. The complete fits are retained as discovery records. Neither
these obstructions nor the numerical residuals improve the matrix
multiplication exponent. General corrections, other subspaces, and
Laurent families remain outside these conclusions.

## 1. Exact source and grading

Use the maintained paired source

\[
Q(6,4)=\sum_{0\le p,q<6}\sum_{0\le y,v<4}
A_{pq}B_{y,q+v}C_{p+y,v}.
\]

Reverse the two convolution-output coordinates, giving the source
coordinate convention

\[
(p,q),\qquad(y,8-q-v),\qquad(8-p-y,v).
\]

All three source factors have dimension 36. The prescribed rational
Clebsch–Gordan maps use a primitive fourteenth root of unity. On the
first leg, retain the components labelled `k>=1` in degree pair `(5,5)`.
On each long leg, the degrees are `11,9,7,5`; retain positions `l=5,6`
from degree 11, positions `l=3,4,5,6` from degree 9, and every position
from degrees 7 and 5.

The valuation-minimal row reduction from the maintained near-full
quantum package gives regular maps with identity pivot submatrices.
Their specializations have ranks `25,20,20`. Write their contraction
with the constant source as `T0`. The complete exact maps, generic
rational rows, tensor coefficients, and valuations are preserved in
`results/quantum-correction-2026-10-21/N5-m4-family.json`.

`quantum.py` rebuilds the specialization directly through the maintained
exact local-map routines. `verify.py` checks all 576 original source
coefficient identities, each specialized local matrix, and the complete
416-term tensor. No numerical fit is used in that verification.

If a local row has original weight `k+l=w`, use centered integer weights

\[
2w-10\quad\text{on A},\qquad 2w-11\quad\text{on B and C}.
\]

Every tensor term has total weight zero. The target convention is

\[
M=\sum_{0\le i,j<5}\sum_{0\le k<4} a_{ij}b_{jk}c_{ki},
\]

with weights `2i-2j`, `2j-2k-1`, and `2k-2i+1`, respectively.
The source and target weight multiplicities agree in each factor.

An ordinary graded correction has the form

\[
(L_A\otimes L_B\otimes L_C)T_0
   +\sum_{s=1}^r u_s\otimes v_s\otimes w_s=M,
\tag{1}
\]

where each `L` preserves these weight spaces and each auxiliary factor
is homogeneous, with the three weights summing to zero. The matrices
are not assumed invertible at the outset. Each auxiliary term costs
at most one in border rank.

## 2. Four auxiliary terms cannot suffice

Every nonzero B slice or C slice of `M(5,4,5)` has matrix rank at least
5. If `r<=4` and `L_B` were singular, a nonzero functional annihilating
its image would turn (1) into a target B slice expressed by at most
four rank-one matrices. This is impossible. Thus `L_B` is invertible;
the same argument applies to `L_C`.

The A weight spaces have the following exact rank witnesses. A witness
rank is a lower bound on the maximum rank of its source weight space;
no claim of generic maximality is needed.

| A weight | Source weight dimension | Exact source witness rank | Maximum target slice rank |
|---:|---:|---:|---:|
| -8 | 1 | 6 | 4 |
| -6 | 2 | 9 | 8 |
| -4 | 3 | 12 | 12 |
| -2 | 4 | 16 | 16 |
| 0 | 5 | 20 | 20 |
| 2 | 4 | 16 | 16 |
| 4 | 3 | 12 | 12 |
| 6 | 2 | 9 | 8 |
| 8 | 1 | 6 | 4 |

The target maximum is `4(5-|w|/2)`: in weight `w`, the underlying
five-by-five matrix has entries on one diagonal of length
`5-|w|/2`.

At either extreme A weight, a nonzero scalar block of `L_A` gives a
rank-six matrix before the auxiliary correction. An extreme target
slice has rank four. Therefore at least two auxiliary terms must have
that A weight. If the scalar block of `L_A` is zero instead, all of the
rank-four target slice must be supplied by the auxiliary terms, so
at least four terms are required there. In both cases the lower bound
of two holds.

Hence four available terms are all spent on the two extreme weights,
with two terms at each. There are no auxiliary terms at weights
`-6` and `6`. Target conciseness on these two-dimensional A weight
spaces then forces their blocks of `L_A` to be invertible: a
functional annihilating a proper image would annihilate a nonzero
target slice. Invertible maps on all three relevant factors preserve
the rank-nine source witness at either weight. The target maximum
there is eight, a contradiction.

This proves the first assertion for all homogeneous assignments with
`r<=4`, including singular choices of the A blocks. It does not prove
an obstruction to arbitrary ungraded corrections or to singular
parameter-dependent families.

## 3. Three six-term assignments are also excluded

All three tested assignments contain the four triples

\[
(-8,3,5),\quad(-8,5,3),\quad(8,-3,-5),\quad(8,-5,-3).
\]

The remaining two triples are:

| Assignment | Fifth triple | Sixth triple |
|---:|---|---|
| 0 | `(-6,3,3)` | `(6,-3,-3)` |
| 1 | `(-6,1,5)` | `(6,-1,-5)` |
| 2 | `(-6,5,1)` | `(6,-5,-1)` |

For each assignment, every individual B weight and every individual
C weight receives at most two auxiliary terms. A singular block of
`L_B` would have a homogeneous annihilating functional. Its target
slice would then be a sum of at most two rank-one matrices, again
contradicting minimum rank five. Therefore the entire `L_B` is
invertible. The same reasoning gives invertibility of `L_C`.

No auxiliary term has A weight zero. Conciseness forces the
five-dimensional zero-weight block of `L_A` to be invertible.
Consequently the central source slice space would have to be
equivalent, under invertible left and right maps, to

\[
\{\operatorname{diag}(a_0,a_1,a_2,a_3,a_4)\otimes I_4\}.
\]

For any invertible anchor in that target space, all normalized slices
commute. This property is preserved by an invertible left-right
equivalence: if `S_i` maps to `U S_i V` and `H` maps to `U H V`, then
the normalized matrix becomes `U S_i H^{-1} U^{-1}`.

Index the five source zero-weight slices by source A coordinates
`10,11,12,13,14`. The exact matrix

\[
H=S_{10}+2S_{11}+5S_{12}+10S_{13}+17S_{14}
\]

has rank 20. Direct arithmetic in `Q(zeta_14)` gives

\[
\operatorname{rank}[S_{11}H^{-1},S_{12}H^{-1}]=14.
\]

In particular the commutator is nonzero. The finite certificate
records a nonzero entry as well as its exact rank. This excludes all
ordinary graded maps for each of the three specified assignments.
It does not exclude every six-term assignment.

## 4. Bounded discovery records

`discovery.py` fits arbitrary complex matrices in the permitted
weight blocks. It imposes no invertibility constraints. All 10,000
target coefficient positions, including the desired zero positions,
are included in every reported residual.

Each run allowed at most 1,200 alternating least-squares updates.
The map norm stopping rule was sampled every 100 updates: a run
stopped at the first reported checkpoint exceeding 100. This is a
sampled stopping rule, not a guarantee that intermediate norms stayed
below 100.

| Assignment | Seed | Updates completed | Best relative residual | Final largest map norm | Stop |
|---:|---:|---:|---:|---:|---|
| 0 | 202610431 | 1200 | 0.7451922012 | 44.5041 | Update limit |
| 0 | 202610432 | 600 | 0.7349295364 | 125.7321 | Sampled norm stop |
| 1 | 202610433 | 500 | 0.7430140228 | 101.5213 | Sampled norm stop |
| 2 | 202610434 | 1200 | 0.7572792077 | 6.9153 | Update limit |

Each checkpoint contains its full objective history, all graded maps,
the complete exact cyclotomic source maps, and the numerical composed
maps from the original 36-dimensional source factors. The long maps
tended toward singularity; none of these residuals is a candidate
identity or evidence of a degeneration. The exact obstruction in
Section 3 is independent of the optimizer behavior.

## 5. Reproduction and next construction question

From the repository root:

```sh
python research/ai/2026-10-21-quantum-correction/verify.py
python -m unittest discover -s tests -p 'test_quantum_correction.py'
```

One discovery run can be reproduced with:

```sh
OPENBLAS_NUM_THREADS=1 python research/ai/2026-10-21-quantum-correction/discovery.py \
  --family results/quantum-correction-2026-10-21/N5-m4-family.json \
  --assignment 0 --seed 202610431 --iterations 1200 \
  --output /tmp/q64-quantum-D6-replay.json
```

A broader constructive target omits the central A diagonal and the
two outermost diagonals on each side. For target `M(N,4,N)`, this
omits `N+6` A entries when `N>=3`; adding their standard rank-one
matrix multiplication terms costs at most `4N+24`. Thus a scalable
exact map on every remaining coefficient would suffice for the
separate correction-budget criterion. No such scalable map is
proved here.

The source-equivalence and Clebsch–Gordan conventions are inherited
from the maintained paired-quantum, narrow-quantum, and near-full
quantum packages. The rank-budget argument, commutator screen, and
finite experiments above are AI-derived deductions for this
prescribed point. Exact computational replay does not constitute
independent mathematical review.
