# Eleven- and ten-split border seeds

## Result and scope

**Claim:** `AI-EXTERNAL-LARGE-GAUGED-SPLIT-SEEDS-008`

**Status:** written-unreviewed

**Question:** Can positive valuations of discarded rank-one tensors produce
larger simultaneous replacement batches and invalidate the earlier
pairwise span-separation certificate?

Yes. This package gives two exact rational Laurent families with 76 surviving
rank-one terms and limit equal to the matrix multiplication tensor
`M(4,5,5)`.

| Certificate | Simultaneous replacements | Expanded exact terms | Surviving border terms | Distinct U directions | Nonzero coefficients at positive degrees |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eleven_certificate.json` | 11 | 87 | 76 | 65 | 414 |
| `ten_certificate.json` | 10 | 86 | 76 | 66 | 283 |

Every constant coefficient is checked: 100 prescribed ones and 9,900 zeros.
The surviving tensor has no nonzero coefficients at negative Laurent degrees.
Its positive-degree remainder is exactly the negative of the discarded tensor. The factors
themselves may have poles.

The eleven-split construction deletes weight 37 from the previously certified
original-U weight assignment. Its retained weight is 214, below that specific
nine-group capacity of 216. The ten-split construction has four nonzero
rational span intersections between distinct initial sharing components.
These are separate reasons to retain both witnesses.

Neither witness improves tensor rank, border rank, or the matrix
multiplication exponent. Neither supplies a complete `Q(6,4)` map. The
ten-split span intersections do not establish that a cross-component flip
or refactorization exists. No search optimum is claimed.

## Exact construction

Use the externally attributed integer rank-76 algorithm from
[`../2026-10-21-external-grid-seed/factors.json`](../2026-10-21-external-grid-seed/factors.json).
Its byte pin is
`bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3`.
Write

\[
M=\sum_{i=0}^{75}U_i\otimes V_i\otimes W_i,
\qquad
U_i\in\mathbb Q^{4\times5},\quad
V_i\in\mathbb Q^{5\times5},\quad
W_i\in\mathbb Q^{5\times4}.
\]

For a listed triple `(i,j,c)`, replace the surviving first factor `U_i`
by `c U_j`, using the original source direction. Retain the exact identity

\[
U_i\otimes V_i\otimes W_i
=cU_j\otimes V_i\otimes W_i
 +(U_i-cU_j)\otimes V_i\otimes W_i.
\]

The changed indices are distinct. None of the destination indices is changed
within its batch. Let `S` be the resulting 76-term tensor, and let `D` be the
sum of the new difference terms. Thus `M=S+D` exactly over the rationals.

### Eleven replacements

All indices are zero-based.

| Changed i | Destination j | c | Minimum factor valuations | Tensor valuation |
| ---: | ---: | ---: | --- | ---: |
| 12 | 24 | -1 | `(1,14,-14)` | 1 |
| 13 | 32 | -1 | `(0,15,-14)` | 1 |
| 16 | 3 | -1 | `(1,11,-11)` | 1 |
| 26 | 32 | 1 | `(0,0,1)` | 1 |
| 30 | 24 | -1 | `(1,13,-13)` | 1 |
| 47 | 52 | -1 | `(1,9,-3)` | 7 |
| 51 | 64 | -1 | `(-3,-4,11)` | 4 |
| 55 | 1 | -1 | `(-9,12,-2)` | 1 |
| 60 | 54 | -1 | `(2,-4,3)` | 1 |
| 63 | 34 | -1 | `(-1,-1,3)` | 1 |
| 73 | 52 | -1 | `(-1,9,-2)` | 6 |

### Ten replacements

| Changed i | Destination j | c | Minimum factor valuations | Tensor valuation |
| ---: | ---: | ---: | --- | ---: |
| 36 | 75 | -1 | `(-2,12,2)` | 12 |
| 46 | 44 | 1 | `(-14,13,2)` | 1 |
| 47 | 38 | 1 | `(-18,-5,24)` | 1 |
| 48 | 2 | -1 | `(-18,-5,24)` | 1 |
| 51 | 55 | -1 | `(-18,0,19)` | 1 |
| 57 | 16 | 1 | `(1,-5,5)` | 1 |
| 61 | 75 | -1 | `(-12,12,2)` | 2 |
| 62 | 56 | 1 | `(0,-1,2)` | 1 |
| 70 | 5 | 1 | `(-31,13,19)` | 1 |
| 73 | 38 | 1 | `(-18,0,19)` | 1 |

## Physical action and positive tensor valuations

The ten-split witness uses the three basis matrices from the earlier
[`split_certificate.json`](../2026-10-23-flip-escape/split_certificate.json).
The eleven-split witness uses those from
[`five_split_certificate.json`](../2026-10-23-flip-escape/five_split_certificate.json).
Their determinants are `(1,-1,1)` and `(1,1,-1)`, respectively. The complete
basis matrices and both source hashes are retained in the new certificates.
The new physical weights are independent of the old certificate weights:

| Variant | R weights | S weights | T weights |
| --- | --- | --- | --- |
| Eleven | `(0,1,3,11)` | `(0,2,4,4,1)` | `(0,14,13,13,15)` |
| Ten | `(0,-20,19,2)` | `(0,-12,0,-13,1)` | `(0,0,-5,0,0)` |

For the retained bases `B_R,B_S,B_T`, define

\[
R(\epsilon)=B_R\operatorname{diag}(\epsilon^{r_a}),\quad
P(\epsilon)=B_S\operatorname{diag}(\epsilon^{s_b}),\quad
T(\epsilon)=B_T\operatorname{diag}(\epsilon^{t_c}).
\]

We use `P` for the middle physical matrix to distinguish it from the surviving
tensor `S`. Apply the physical stabilizer action

\[
\Phi_\epsilon(U,V,W)
=(R^{-1}UP,\ P^{-1}VT,\ T^{-1}WR).
\]

Its action on the matrix multiplication tensor is the identity. This follows
directly by substituting elementary matrices and contracting each adjacent
matrix with its inverse. Consequently

\[
\Phi_\epsilon(S)=M-\Phi_\epsilon(D).
\]

For any transformed nonzero factor, its valuation is the smallest exponent
among its nonzero coordinates. A rank-one tensor product has valuation equal
to the sum of its three factor valuations: choose one nonzero minimum
coordinate in each factor, whose product is nonzero over the rationals.

Every row in the two replacement tables has strictly positive sum. Therefore
each discarded rank-one tensor tends to zero, and the finite sum does too.
It follows that

\[
\lim_{\epsilon\to0}\Phi_\epsilon(S)=M.
\]

This proves the two 76-term border decompositions. The displayed valuations
also explain why one must permit poles in individual factors. Positivity of
all three unscaled factor valuations is not required for tensor convergence.

### Optional factor gauges

A factor gauge consists of three nonzero scalar multipliers whose product is
one, so it preserves the entire rank-one tensor term. The certificates include
explicit gauges after the ramification `epsilon=t^3`. If a discarded term has
factor minima `(a,b,c)` with `a+b+c>0`, multiply its three factors by powers of
`t` with exponents

\[
(1-3a,\ 1-3b,\ 3a+3b-2).
\]

Their sum is zero. The new factor minima are
`(1,1,3(a+b+c)-2)`, all strictly positive. This changes neither the discarded
tensor nor the exact expanded identity. The replay checks every gauge sum
and each resulting positive minimum.

## What the two witnesses change

### Eleven: the old U-weight test no longer rejects this set of directions

The earlier
[`2026-10-23-grid-escape`](../2026-10-23-grid-escape/README.md) package assigns
weight four to 23 original U directions and weight three to all others. The
total is 251, and every rank-at-most-four flat has weight at most 24. Nine
such groups have capacity 216.

The eleven deleted indices contain four weight-four directions: `26,30,51,55`.
Their deleted weight is `3*11+4=37`, leaving `214`. Thus this particular
necessary bound gives no exclusion. This is an arithmetic consequence of
the earlier certified weight assignment; it is not a construction of nine
groups. The ten witness deletes weight 34 and retains weight 217, so that
same test still excludes its current U directions from nine such groups.

Both batches leave the original W factors unchanged. Therefore the earlier
original-W obstruction still excludes immediate termwise grid reuse of either
displayed seed. Further exact factor changes would be needed.

### Ten: exact intersections across initial sharing components

Form a graph on the 76 displayed surviving terms. Join two terms when their
factors are proportional on at least one leg. In the ten-split seed, one
connected component is

\[
B=\{2,38,39,47,48,51,52,55,73\}.
\]

Its leg span dimensions are `(5,9,5)`. The following relations use the
**surviving** constant factors, before the common physical action:

\[
\begin{aligned}
U_{19}&=U_{38}+U_{52},\\
U_{41}-U_{40}&=U_{38}-U_{51}+U_{52},\\
V_{26}&=-V_{39}-V_{51},\\
W_{58}&=-W_{38}+W_{51}.
\end{aligned}
\]

The respective other sharing components are `{19}`, `{40,41}`, `{26}` and
`{58,59}`. Each displayed common vector is nonzero. Exact row reduction gives
intersection dimension one in all four cases:

| Leg | B span dimension | Other component dimension | Combined span dimension |
| --- | ---: | ---: | ---: |
| U, with `{19}` | 5 | 1 | 5 |
| U, with `{40,41}` | 5 | 2 | 6 |
| V, with `{26}` | 9 | 1 | 9 |
| W, with `{58,59}` | 5 | 1 | 5 |

The earlier sufficient condition for permanent component isolation required
pairwise disjoint spans on all three legs. It does not hold here. The common
physical action is invertible for nonzero parameter, so these intersection
dimensions also persist over the Laurent field.

A span intersection alone does not supply the decomposable factors needed
for an exact refactorization. For example, the next constructive test for
`U19` is whether
`span{U_i tensor W_i : i in B}` contains a nonzero tensor of the form
`U19 tensor w`. This question remains outside the accepted claim here.

## Discovery and acceptance

Discovery used the previously enumerated 669 individually admissible
U-replacement candidates, fixed physical bases, and bounded mixed integer
linear programs. The physical weights were bounded by 20 in absolute value.
Each candidate had three auxiliary lower bounds for its factor valuations
and a binary inclusion indicator. A selected candidate required their sum
to be at least one. Source indices could be used once, and destination
indices had to remain unchanged.

The initial runs used a 40-second time limit. A small binary refinement at the
saved weights selected the eleven-split batch. `discovery.json` records the
two retained search outputs. Neither those bounds nor the solver's status
are used as mathematical acceptance criteria. The search has not proved a
maximum number of replacements or completeness of this ansatz.

Acceptance uses only Python's standard library. It byte-checks the external
seed and retained basis sources, regenerates every rational factor, checks
unimodularity, and contracts every Laurent coefficient. It also independently
counts the projective U directions and checks the four ten-split relations
and rational span dimensions. The saved intermediate exact identities have
86 or 87 terms; the border families have 76. At a nonzero parameter, the
76-term tensor generally differs from `M` by a nonzero error.

From the repository root:

```sh
python research/ai/2026-10-23-large-gauged-batches/verify.py --variant eleven
python research/ai/2026-10-23-large-gauged-batches/verify.py --variant ten
python -m unittest discover -s tests -p test_large_gauged_split_seeds.py -v
```

Six focused tests cover both complete exact replays, deterministic fixture
regeneration, gauges with poles, coefficient and valuation corruption,
schema/source/scope checks, the rational span contacts, and an independent
dense evaluation of the expanded identities at `epsilon=-2`. That evaluation
also confirms that the surviving tensor alone is not an exact decomposition
at the chosen nonzero parameter.

## Attribution

The rank-76 external seed is credited to Fawzi and collaborators, AlphaTensor,
Nature (2022), through the pinned conversion already retained by this project.
The physical bases come from the earlier local four- and five-split witnesses.
The larger batches, their new weights, the exact coefficient replay, and the
recorded span contacts are local AI-derived work.

The physical-stabilizer deletion viewpoint is discussed in Dumitriu et al.,
*Fast and Stable Arbitrary Precision Approximate Matrix Multiplication*,
[arXiv:2610.13905v1](https://arxiv.org/html/2610.13905v1), Theorems 2.1 and 2.2
and Section 2.3. The tensor-valuation and gauge arguments needed here are
proved directly above. Detailed source pins are in `sources.json`. No
historical priority, independent mathematical review, or exponent improvement
is asserted.
