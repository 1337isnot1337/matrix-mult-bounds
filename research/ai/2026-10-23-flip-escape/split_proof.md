# Four splits and a common contracting physical transformation

**Claim `AI-EXTERNAL-SPLIT-BORDER-SEED-002`. Written proof, unreviewed.**

The [five-split continuation](five_split.md) supplies a second witness
by the same argument. This note preserves the original four-split data.

There is an explicit rank-76 border decomposition of M(4,5,5) with 72
distinct first-leg factor directions over the rational Laurent field.
It comes from four splits of the pinned external exact rank-76 algorithm,
followed by deletion of the four new terms under one physical stabilizer
transformation. Every coefficient of the Laurent identity is checked
exactly in `verify_split.py`.

This is a different border seed, with the same upper bound 76 as the
external exact algorithm. It is not a rank record or a Q(6,4) map.
In particular, 72 distinct directions alone do not establish the required
nine rank-at-most-four groups. The accompanying weighted-incidence
investigation excludes this particular seed from that termwise grid
assignment as well.

## 1. Exact splits

Use zero-based indices and the matrices U_i, V_i, W_i of the external
seed. For each row in the following table, replace its U_i factor by
c U_j and introduce one discarded term with first factor U_i-c U_j.
Both terms keep V_i and W_i.

| Changed index i | Retained direction j | Coefficient c |
| ---: | ---: | ---: |
| 0 | 18 | -1 |
| 17 | 8 | 1 |
| 48 | 2 | -1 |
| 56 | 22 | -1 |

The identity

\[
U_i\otimes V_i\otimes W_i
=(cU_j)\otimes V_i\otimes W_i
 +(U_i-cU_j)\otimes V_i\otimes W_i
\]

increases the exact term count from 76 to 80. Let S be the sum of the
76 surviving terms and D the sum of the four discarded terms. Then

\[
M(4,5,5)=S+D.
\]

The selected indices i and j are disjoint, so each replacement duplicates
a direction still present elsewhere. The original 76 U directions are
distinct. The surviving list therefore has exactly 72 directions.

## 2. Joint nilpotence through image flags

Write each discarded term as (A_a,B_a,C_a), with maps

\[
A_a:\mathbb Q^5\longrightarrow\mathbb Q^4,\qquad
B_a:\mathbb Q^5\longrightarrow\mathbb Q^5,\qquad
C_a:\mathbb Q^4\longrightarrow\mathbb Q^5.
\]

Start with full spaces R_0, S_0, T_0 of dimensions 4,5,5. Define

\[
R_{k+1}=\sum_a A_a S_k,\quad
S_{k+1}=\sum_a B_a T_k,\quad
T_{k+1}=\sum_a C_a R_k.
\]

These sequences are descending. Exact rational elimination gives:

| k | dim R_k | dim S_k | dim T_k |
| ---: | ---: | ---: | ---: |
| 0 | 4 | 5 | 5 |
| 1 | 4 | 4 | 3 |
| 2 | 3 | 3 | 3 |
| 3 | 2 | 3 | 3 |
| 4 | 2 | 3 | 1 |
| 5 | 2 | 1 | 1 |
| 6 | 1 | 1 | 1 |
| 7 | 1 | 1 | 0 |
| 8 | 1 | 0 | 0 |
| 9 | 0 | 0 | 0 |

In particular every mixed composable path of nine discarded arrows is
zero. This is stronger than checking each individual product A_a B_a C_a
for nilpotence: it includes interactions between different discarded
terms.

Choose a basis adapted to each descending flag. Assign weight -k to
a vector first added when extending the chosen basis of the (k+1)-st
space to that of the k-th space. Each arrow takes depth k into depth
at least k+1. Thus, after the corresponding physical diagonal scaling,
each nonzero arrow coefficient has positive valuation.

## 3. Explicit bases and weights

One exact choice is

\[
B_R=\begin{pmatrix}
0&0&0&-1\\
1&1&0&0\\
0&0&1&0\\
1&0&0&0
\end{pmatrix},\qquad
B_S=\begin{pmatrix}
0&0&0&0&1\\
0&1&-1&1&0\\
0&0&-1&0&0\\
0&-1&0&0&0\\
-1&0&-1&0&0
\end{pmatrix},
\]

\[
B_T=\begin{pmatrix}
0&0&0&1&0\\
0&1&0&0&0\\
-1&0&0&0&0\\
0&0&0&0&1\\
0&0&1&0&0
\end{pmatrix}.
\]

Their determinants are 1,-1,1. The column weights are

\[
r=(-8,-5,-2,-1),\quad
s=(-7,-4,-4,-1,0),\quad
t=(-6,-3,-3,0,0).
\]

Set

\[
R(\epsilon)=B_R\operatorname{diag}(\epsilon^r),\quad
S(\epsilon)=B_S\operatorname{diag}(\epsilon^s),\quad
T(\epsilon)=B_T\operatorname{diag}(\epsilon^t).
\]

Apply the physical action

\[
U\mapsto R^{-1}US,\quad
V\mapsto S^{-1}VT,\quad
W\mapsto T^{-1}WR.
\]

For example, an entry of B_R^{-1} U B_S in row a and column b gains
exponent s_b-r_a. All entries of each of the three factors of every
discarded term have exponent at least one. Their rank-one tensor
products consequently have exponent at least three.

The physical action fixes the matrix multiplication tensor. Applying it
to the exact split identity gives

\[
S(\epsilon)=M(4,5,5)-D(\epsilon),\qquad
D(\epsilon)\in \epsilon^3\mathbb Q[\epsilon]^{20\times25\times20}.
\]

Hence the 76 surviving Laurent rank-one terms have limit M(4,5,5).
Individual surviving factors may have poles; the complete tensor has
none. This distinction is essential for the border claim.

The bases are unimodular and the source coefficients are integers.
The displayed formal identity therefore has integer Laurent
coefficients. The direct coefficient verification, rather than a small
floating-point residual or a condition estimate, is the acceptance
criterion.

## 4. Complete coefficient replay

`split_certificate.json` exports all 76 surviving terms and all four
discarded terms. Every sparse factor entry is a triple
`[flat_coordinate, rational_coefficient, Laurent_exponent]`. Each factor
coordinate contains at most one monomial. The flattening convention is
the same as the external seed: row-major sizes 4-by-5, 5-by-5 and 5-by-4.

The verifier first checks the source byte pin, regenerates the exact
image flag, and checks the basis and inverse identities. It then
reconstructs every stored factor from the split and physical matrices.
Finally it contracts the exported factors, collecting every tensor
coordinate and every Laurent degree before removing zero coefficients.
The result has:

* no negative-degree coefficient;
* exactly the 100 required unit coefficients at degree zero, with the
  other 9900 tensor positions zero;
* 51 positive-degree coefficients, equal to the negative of the complete
  discarded tensor.

| Degree | Nonzero tensor coefficients |
| ---: | ---: |
| 0 | 100 |
| 3 | 5 |
| 4 | 2 |
| 6 | 9 |
| 7 | 7 |
| 9 | 12 |
| 10 | 7 |
| 12 | 6 |
| 13 | 2 |
| 15 | 1 |

The discarded remainder is nonzero. In particular the surviving terms
before taking the limit are an approximate tensor family, not an exact
76-term decomposition of M(4,5,5) at a generic nonzero epsilon. Future
flips may preserve this family, but must keep its remainder in their
coefficient accounting.

## 5. Consequence and remaining question

The split operation escapes the hypotheses of the closed-component
proof. After deletion, the surviving representation has new shared-U
directions. They permit further refactorizations that the original
exact seed did not permit. The first-leg direction count remains 72
under the common invertible physical action over Q(epsilon).

This count only removes the earlier 76-greater-than-72 pigeonhole
contradiction. It supplies neither nine rank-at-most-four groups nor
the simultaneous second-leg and evaluation-node compatibility needed
for Q(6,4). The stronger weighted-flat test for the retained old
directions excludes the present four-split seed. Further splits or
flips changing the factor directions require new exact certificates.

The construction follows the nilpotent-factor deletion approach in
[Dumitriu et al., arXiv:2610.13905v1, Theorems 2.1 and 2.2](https://arxiv.org/html/2610.13905v1).
The specific four splits, common rational flag, unimodular bases, and
complete Laurent certificate are local work. The external AlphaTensor
algorithm retains its original attribution. No general invariant-theory
theorem, historical novelty, independent review, rank record, or exponent
improvement is claimed.
