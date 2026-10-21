# A paired-source construction criterion with linear correction cost

October 21, 2026. Written, AI-derived conditional argument; no external
mathematical review or formalization. **The required source maps are
missing. No smaller matrix multiplication exponent is established.**

The purpose of this criterion is to broaden a construction search. It is
enough to recover almost all of a wide matrix target and repair a boundary
whose tensor border rank grows linearly. An isolated numerical fit does not
satisfy the unbounded-family premise.

## 1. Precise construction premise and consequence

Fix an integer b at least four. For unbounded positive integers n, suppose
there are complex tensors R_n of border rank at most Cn, with a constant C
independent of n, and genuine tensor degenerations

\[
Q_{n,b}\oplus R_n\ \unrhd\ M(n,b,n),\qquad
Q_{n,b}=\sum_{p,q<n}\sum_{y,v<b}A_{p,q}B_{y,q+v}C_{p+y,v}.
\tag{1}
\]

The source Q has format `(n^2,b(n+b-1),b(n+b-1))`. The additional tensor
is part of the source and its cost is explicit. The constant C may depend
on the fixed width b. The integer subsequence and every auxiliary tensor
are fixed constructions, independent of the tensor character used below.

**Conditional theorem.** Under (1), the matrix multiplication exponent
satisfies

\[
\omega\le\frac3{d_b},\qquad
d_b(6b)^{d_b}=12b^{3/2},
\tag{2}
\]

where the positive root is unique. For b=4 it lies strictly between 4/3
and 3/2. An exact integer certificate gives the conditional rational bound

\[
\boxed{\omega<\frac{30000}{13433}<2.2334.}
\tag{3}
\]

The root expression in (2) is approximately 2.233247 for b=4. This decimal
is a display value for the conditional implication, not an achieved
exponent. The stricter acceptance decision in (3) uses integer arithmetic.

The same theorem holds if the target in (1) is `M(l_n,b,r_n)` with
`l_n/n -> 1` and `r_n/n -> 1`. In particular, `M(n-c,b,n-c)` for a fixed
nonnegative integer c is sufficient. This version need not restore the
missing boundary at all.

## 2. Character notation and the cyclic comparison

Use the complex tensor-character framework of OpenAI's pinned 9/4 paper
and the normalization already maintained in this repository. For the
dot product missing leg i, write its character value as `k^(p_i)`, where
`0<=p_i<=1`. Put

\[
S=p_1+p_2+p_3,\qquad t=S/3,\qquad d=1/t=3/S.
\]

The detecting-character theorem converts an upper bound for every S into
the same upper bound for omega. Characters with S at most two already
satisfy (2), since the claimed right side is greater than two. We therefore
fix a character with S>2 for the remainder of the proof.

Let Q_i be the cyclic permutation whose two n-dimensional inputs share
leg i, and put `a_i(n)=lambda(Q_i)`. A convolution tensor C_ij(n,b) is an
ordinary restriction of an outer product: map the output coordinate
indexed by `(p,y)` to the coordinate indexed by `p+y`. Hence

\[
\lambda(C_{ij}(n,b))\le n^{p_j}b^{p_i},\qquad
a_i(n)\le n^{S-p_i}b^{2p_i}.
\tag{4}
\]

The paired tensor is exactly the product of C_ij and C_ik. Multiplying
over the three cyclic orientations uses each of the six oriented
convolution tensors once. In the existing symmetrized-profile notation,

\[
\prod_i a_i(n)=P(n,b)^{2S}.
\tag{5}
\]

The matrix target with the n-squared leg in position i has character
`n^(S-p_i)b^(p_i)`. The three cyclic target values therefore multiply to
`n^(2S)b^S`. Border rank bounds character values, so (1) gives

\[
\prod_{i=1}^3(a_i(n)+Cn)\ge n^{2S}b^S.
\tag{6}
\]

Each use of degeneration monotonicity is at one fixed n. No uniform
Laurent order or common parameter rate as n varies is assumed in this
character argument; every individual degeneration must still be proved.

## 3. Why a linear correction disappears in the cyclic product

Expand the left side of (6). The term without a correction is (5).
Since b is fixed, (4) bounds the other terms by constants times the
following powers of n:

| Term | Exponent | Positive gap below 2S |
|---|---:|---:|
| `Cn * a_i * a_j` | `1+2S-p_i-p_j` | `p_i+p_j-1` |
| `(Cn)^2 * a_i` | `2+S-p_i` | `S+p_i-2` |
| `(Cn)^3` | `3` | `2S-3` |

Every gap is positive: `p_i+p_j=S-p_k>=S-1>1`, `S+p_i>2`, and S>2.
Thus the entire sum of correction terms is `o(n^(2S))`, for this fixed
character. Dividing (6) by `n^(2S)` proves, along the unbounded construction
subsequence,

\[
\liminf\frac{P(n,b)}n\ge\sqrt b.
\tag{7}
\]

No numerical conditioning estimate is involved. An O(n-squared)
correction is not covered by this proof. More generally, a cost O(n^alpha)
works for a fixed character when alpha is smaller than all three pair
sums `p_i+p_j`; the linear budget is a uniform sufficient choice for
every S>2.

## 4. A general upper bound for the thin slope

The maintained scaling theorem, using Uznański's replication
degeneration, gives a symmetric, separately concave, degree-d homogeneous
profile F with `P(a,b)<=F(a,b)`. Its tripling inequality and the
two-sector source construction give

\[
F(b,4b)\ge3F(b,b),\qquad 2F(4b,b)\le(6b)^d.
\]

Consequently `F(b,b)<=(6b)^d/6`. The one-sided derivative argument from
symmetry and homogeneity gives

\[
\partial_1^+F(b,b)\le\frac{dF(b,b)}{2b}.
\]

Concavity bounds every value to the right by this supporting line. For
every n at least b,

\[
P(n,b)\le F(n,b)
\le\frac{(6b)^d}{6}\left(1+\frac{d(n-b)}{2b}\right).
\tag{8}
\]

Combining its limiting slope with (7) yields

\[
\sqrt b\le\frac{d(6b)^d}{12b},
\]

which is precisely the necessary inequality underlying (2). This step
does not assume endpoint rigidity, differentiability at the diagonal,
or equality of the six oriented finite-size profiles.

The function `d(6b)^d` is strictly increasing for positive d. At d=4/3
its value is smaller than `12b^(3/2)` exactly when `81b>256`, so b=4 is
the first integer width improved by this criterion. At d=3/2 the
inequality is reversed. Therefore `4/3<d_b<3/2` for every b at least four,
and (2) improves 9/4 if its construction premise is supplied.

For the rational certificate at b=4, set a=13433 and q=10000. The verifier
checks the exact integer inequality

\[
a^q24^a<(96q)^q.
\tag{9}
\]

Taking the positive q-th root says `(a/q)24^(a/q)<96`, and hence
`d_4>a/q`. This proves (3) without a floating-point root solver.

## 5. Boundary targets and useful construction budgets

For the near-full rectangular version, the cyclic target product is
`(l_n r_n b)^S`. After division by `n^(2S)`, its limit is again `b^S`,
so the same proof applies. More generally, limiting outer ratios alpha
and beta give the right side `12b^(3/2)*sqrt(alpha*beta)` in (2).

Alternatively, an explicit partial matrix tensor can be repaired by
adding each missing product as one rank-one source term:

- Removing the n diagonal first-leg entries costs bn such terms.
- Removing a fixed c rows and c columns costs `b(2cn-c^2)` terms.
- Any specified set of O(n) missing first-leg entries costs O(n) at
  fixed b.

These are explicit upper bounds for corrections, not claims that Q can
construct the remaining tensor. The coefficient controls in `verify.py`
check the restoration identities on small cases. A successful isolated
small map must still be extended to an unbounded sequence before this
theorem applies.

## Sources, scope, and replay

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [pinned revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf):
  character rules, dot products, symmetrization, and spectral conversion.
- Uznański, [arXiv:2610.10494v2](https://arxiv.org/html/2610.10494v2):
  replication and oriented scaling, as attributed in the maintained
  [homogeneous scaling proof](../2026-10-20-concavity-equivalence/homogeneous_rigidity.md).
- The same local scaling proof supplies `P<=F` and the one-sided diagonal
  derivative bound. The [two-sector note](../2026-10-20-truncated-algebras/two_sector_bound.md)
  supplies its all-size source inequality. These inputs precede this note.
- The linear correction estimate, resulting paired construction criterion,
  and integer root certificate are deductions in this generating session.
  A second agent checked the cyclic exponents and asymptotic error terms;
  this is a same-session check, not independent mathematical review.

```sh
python research/ai/2026-10-21-correction-budget/verify.py --output results/correction-budget-2026-10-21/certificate.json
python -m unittest discover -s tests -p test_correction_budget.py -v
```

The finite controls do not prove the missing maps, the unbounded-family
premise, or an achieved exponent improvement.
