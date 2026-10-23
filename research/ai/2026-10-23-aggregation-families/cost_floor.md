# A size gate for the displayed aggregation budgets

October 23, 2026. Owner-directed OpenAI Codex work. Written and unreviewed.

The new finite families improve the stated comparison budgets. A separate
calculation shows why increasing those small families alone cannot reach
the repository's exponent target. This note concerns the cost certificate
that charges every term of the main centered aggregate. It is **not** a
lower bound for the rank of the resulting tensor, or for matrix multiplication.

## Model

Take a conflict-free family of p ordered, balanced tripartitions
`(U_i,V_i,W_i)` of a set with 3N coordinates, each part having size N.
Its displayed centered-aggregation budget has the form

\[
 B(n)=(n+1)^{3N}+\sum_{k\ge1}c_k(n+1)^{3N-k},\qquad c_k\ge0.
\]

It supplies p independent copies of `M(n^N,n^N,n^N)`. This is the model
used in the accompanying proof and in Sections 5.6 and 8.2 of
[Solomonik–Bläser, arXiv:2610.26563v2](https://arxiv.org/html/2610.26563v2).
The aggregation framework and the asymptotic sum theorem are prior work.

For n>1 the direct asymptotic-sum substitution gives the exponent bound

\[
 \frac{\log(B(n)/p)}{N\log n}.
\]

To certify a value at most 9/4 through this particular budget, one needs
`B(n) <= p*n^(9N/4)`.

## A counting bound for the number of products

First, no two selected products can have the same U part. If `U_i=U_j`
with i different from j, the mixed choice `(U_i,V_j,W_j)` is an
off-diagonal complete tripartition. That contradicts conflict-freeness.
The same argument applies to the V and W parts. Write

\[
 C={3N\choose N},\qquad D={2N\choose N}.
\]

Consider the tripartite hypergraph whose three vertex classes are copies
of all N-subsets of the coordinate set. An edge is a complete ordered
tripartition. The hypergraph has CD edges, and every vertex belongs to
exactly D edges: after fixing one part, either remaining part may be any
N-subset of its 2N-coordinate complement.

The selected U, V and W parts give p vertices in each class. They induce
exactly p edges. There are p diagonal edges, and conflict-freeness excludes
every other edge among the selected vertices. Deleting the other
3(C-p) vertices removes exactly CD-p edges. Counting incidences at deleted
vertices can count a removed edge more than once, so

\[
 CD-p\le 3(C-p)D.
\]

Rearranging gives the stronger product bound

\[
 p\le P_N:=\left\lfloor\frac{2CD}{3D-1}\right\rfloor.       \tag{1}
\]

This argument needs the induced-edge condition, not just distinct parts.
For example, on three coordinates the three cyclic tripartitions have
distinct parts in every class but have unwanted mixed edges. The bound
is sharp at N=1: two suitable tripartitions form a conflict-free family.
No sharpness is claimed for larger N.

## The leading cost floor

Weighted arithmetic–geometric mean, applied to
`n/3, n/3, n/3, 1`, gives

\[
 n+1\ge 4(n/3)^{3/4}.
\]

Consequently, for every real n>0,

\[
 \frac{B(n)}{n^{9N/4}}
 \ge \frac{(n+1)^{3N}}{n^{9N/4}}
 \ge \frac{4^{3N}}{3^{9N/4}}.                              \tag{2}
\]

Equality in the last inequality occurs at n=3. This estimate already
ignores every correction cost, so removing corrections cannot overcome
it while the leading aggregate is charged as above.

## Exact finite comparison

For each N from 1 through 10 the following strict integer inequality holds:

\[
 P_N^{4}\,3^{9N}<4^{12N}.                                 \tag{3}
\]

Combining (1)–(3) proves `B(n) > p*n^(9N/4)` for every n>0.
Hence **no balanced conflict-free family with N<=10 can certify an
exponent at most 9/4 by this displayed aggregation budget**.

The last column below is the smallest integer exceeding the real cost
floor in (2); it is computed using integer comparisons, not rounded logs.

| N | Product cap from the induced-edge count | Necessary products to exceed the leading cost floor |
| ---: | ---: | ---: |
| 1 | 2 | 6 |
| 2 | 10 | 30 |
| 3 | 56 | 158 |
| 4 | 331 | 853 |
| 5 | 2,004 | 4,606 |
| 6 | 12,380 | 24,886 |
| 7 | 77,527 | 134,463 |
| 8 | 490,326 | 726,537 |
| 9 | 3,124,571 | 3,925,676 |
| 10 | 20,030,046 | 21,211,507 |
| 11 | 129,024,540 | 114,611,623 |

The N=11 row is included to show the limit of this particular argument.
It does not construct a family of that size or account for its corrections.
It proves only that N>=11 is necessary for this budget to pass the gate;
it does not prove sufficiency. In particular, both the N=3 and N=4
constructions in this package are below the gate regardless of the
remaining local search budget.

The earlier version used only p<=C and excluded N<=7. The induced-edge
count extends the certified range without a numerical optimization or an
assumption about the minimum correction cost.

## Reproduction and scope

`cost_floor.json` contains the exact integer sides of (3), their
differences and the integer thresholds. The core check uses only Python's
standard library:

```python
from math import comb

for N in range(1, 12):
    C, D = comb(3*N, N), comb(2*N, N)
    cap = (2*C*D) // (3*D-1)
    assert (cap**4 * 3**(9*N) < 4**(12*N)) == (N <= 10)
```

This leaves open algorithms that lower the main-aggregate cost, exploit
other tensor identities, use different target shapes, or introduce a new
source construction. It also leaves open a better rank decomposition of
these same tensors. The displayed upper bound failing the gate is not a
lower bound on their actual rank. Same-session checks are not independent
mathematical review or formalization.
