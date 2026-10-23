# One-slice speedups of the exact Q(5,4) seed

October 23, 2026. Owner-directed research, with same-session checks.
Written and unreviewed; no independent mathematical review, formalization,
or improvement of the matrix multiplication exponent is claimed.

The exact integer seed `Q(5,4) >= M(4,4,4)` satisfies the hypotheses of
the one-slice speedup in Alman and Li's
[*Asymptotic Rank Speedup Theorems, Revisited*, arXiv:2605.21738v1](https://arxiv.org/html/2605.21738v1#S5.SS3).
It gives the actual complex degenerations

\[
\boxed{
M(4^k,4^k,4^k)\oplus J_{\,8^k(2^k-1)^2}
\ \unlhd\ Q(5,4)^{\otimes k}\oplus J_{\,8^k}
\qquad(k\ge1),
}
\tag{1}
\]

where `J_s=M(1,s,1)` has format `(1,s,s)` and `U <=deg V`, written
\(U\unlhd V\), means that V degenerates to U. In particular,

\[
M(16,16,16)\oplus J_{576}
\ \unlhd\ Q(5,4)^{\otimes2}\oplus J_{64}.
\tag{2}
\]

This application supplies structured auxiliary terms, but its endpoint
inequalities do not exclude the existing feasible scalar profile. More
generally, the same conclusion holds for **one appended one-slice tensor
to a seed power and one-slice extraction**, for any choice of the slice.
The proof below gives a uniform ceiling, rather than a parameter search.
It does not exclude multiple-slice constructions, successive extractions,
other seeds, or constructions retaining additional tensor information.

## 1. Existing seed and orientations

Use the maintained coefficient conventions

\[
Q=Q(5,4)=\sum_{p,q=0}^4\sum_{y,v=0}^3
A_{p,q}\otimes B_{y,q+v}\otimes C_{p+y,v},
\tag{3}
\]

with format `(25,32,32)`, and

\[
T=M(4,4,4)=\sum_{i,h,j=0}^3
a_{i,h}\otimes b_{i,j}\otimes c_{j,h}.
\tag{4}
\]

The previous [integer construction](../2026-10-20-paired-construction/outer_product_injection.md)
provides maps \(L_A,L_B,L_C\) with `T=(L_A tensor L_B tensor L_C)Q`.
The verifier reads its saved [complete maps](../2026-10-20-paired-construction/q54-exact.json)
and rechecks all 4,096 target coefficients from the 400 source terms.
This is an imported local seed, not a new construction credited here.

The B map vanishes unless the native short coordinate y is 0 or 3.
On those 16 selected source coordinates it is a unimodular isomorphism.
The C map has the corresponding property for its native short coordinate
v in `{0,3}`. These facts follow from the seed's invertible convolution
dual and are checked directly on the saved matrices.

For the external one-slice statements, order the source modes as
`(B,C,A)`. The paper's one-slice tensor has its singleton in the third
mode. Returning to `(A,B,C)` gives exactly our `J_s`, with singleton A.
The two compressed dimensions in those statements are both 16.

## 2. A full source slice with compressed rank eight

Choose the A functional

\[
f=A_{0,0}^{*}+A_{4,4}^{*}.
\tag{5}
\]

Its B by C matrix is

\[
M_f=\sum_{\alpha=0}^1\sum_{y,v=0}^3
B_{y,4\alpha+v}\otimes C_{4\alpha+y,v}.
\tag{6}
\]

Every B coordinate occurs once, and every C coordinate occurs once.
Thus this is a 32 by 32 permutation matrix and its rank is 32.
After applying \(L_B,L_C\), only the eight terms with `y,v in {0,3}`
survive. Put

\[
x_{\alpha,y,v}=L_B(B_{y,4\alpha+v}),\qquad
z_{\alpha,y,v}=L_C(C_{4\alpha+y,v}).
\tag{7}
\]

The eight x vectors are independent, and so are the eight z vectors:
each set consists of distinct columns of its selected invertible long
map. Therefore

\[
(L_B\otimes L_C)M_f
=\sum_{\alpha=0}^1\sum_{y,v\in\{0,3\}}
x_{\alpha,y,v}\otimes z_{\alpha,y,v}
\quad\hbox{has rank }8.
\tag{8}
\]

Here is the exact cancellation needed by the speedup. Let X,Z be the
16 by 8 matrices with these columns. Adjoin `J_8` and extend the old maps
as

\[
\widetilde L_A=[L_A\mid0],\quad
\widetilde L_B=[L_B\mid X],\quad
\widetilde L_C=[L_C\mid Z],\quad
f'=[f\mid-1].
\tag{9}
\]

The extended maps still restrict the augmented source to T, because its
added A coordinate maps to zero. The raw `f'` slice is
`M_f direct sum (-I_8)`, of rank 40, and

\[
\widetilde L_B(M_f\oplus(-I_8))\widetilde L_C^{\mathsf T}
=L_BM_fL_C^{\mathsf T}-XZ^{\mathsf T}=0.
\tag{10}
\]

The verifier checks all 256 entries in (8) and all 256 entries in (10).
These ranks and identities use exact integer or rational arithmetic.

For contrast within this fixed construction, contracting Q by the two
old maps gives injective maps from each remaining source dual space:

| Remaining source leg | Source dimension | Two-map slice-space rank over Q | Kernel dimension |
| --- | ---: | ---: | ---: |
| A | 25 | 25 | 0 |
| B | 32 | 32 | 0 |
| C | 32 | 32 | 0 |

Thus the free-lunch theorem has no nonzero initial kernel slice for the
three **fixed seed maps** without augmentation. The same holds for their
tensor powers, because tensor products of injective linear maps remain
injective. This observation concerns those maps only.

## 3. Importing the speedup and taking powers

Alman--Li, v1, Proposition 5.4 starts from an arbitrary restriction
`T <= S` and a slice with raw rank q and compressed rank s. Appending
one `J_s` produces a kernel slice of raw rank `q+s`.
Proposition 5.3, through their Theorem 5.1, extracts a direct-sum
one-slice target of rank at least `q+s-n-m`, where n,m are the two
compressed target dimensions. One may restrict that extracted matrix
to any smaller nonnegative rank. Proposition 5.4 attributes the general
one-slice speedup to Strassen; the paper also explains its relation to
Coppersmith--Winograd's speedup. This package applies those results and
does not claim their mechanism as new.

Apply these statements directly to the ordinary restriction
`T^k <= Q^k`, with its tensor-product maps and functional `f^k`.
Matrix rank is multiplicative under tensor product, so (6)--(8) give

\[
q_k=32^k,\qquad s_k=8^k,\qquad n_k=m_k=16^k.
\tag{11}
\]

The guaranteed extracted rank is

\[
t_k=32^k+8^k-2\cdot16^k
=8^k(2^k-1)^2>0.
\tag{12}
\]

This proves (1) for every positive integer k. It uses the general-source
propositions, not the paper's later speedup statements specialized to a
diagonal source. Applying the propositions directly to the seed power
also avoids an additional isolation or iteration premise.

The actual degeneration in (1) follows from the cited theorem and the
exact seed hypotheses. A complete list of Laurent maps for it is not
provided or claimed to have been checked here. No unbounded family
`Q(n,4)` with nearly full outer target dimensions follows from (1): its
source is a power of a fixed tensor and its target inner dimension is
`4^k`. The formal-expression repair barrier is a different statement;
no formal-expression monotone is used in this actual construction.

## 4. A uniform endpoint ceiling for the stated route

Consider any one appended one-slice tensor to a seed power and one-slice
extraction in the preceding sense, yielding

\[
T^{\otimes k}\oplus J_t\unlhd Q_i^{\otimes k}\oplus J_s.
\tag{13}
\]

Here \(Q_i\) is any cyclic orientation, the slice choice is arbitrary,
and `s,t >= 0`; zero denotes the zero tensor. The raw slice of the
unaugmented source has rank `q <= 32^k`. The appended one-slice contributes
rank at most s. Since the extracted matrix is a restriction of that
augmented slice,

\[
t\le q+s\le32^k+s.
\tag{14}
\]

At a hypothetical endpoint character the three dot-product exponents
are all `3/4`. Set

\[
a_i=\lambda(Q_i),\qquad
\tau=\lambda(T)=4^{9/4}=16\sqrt2,\qquad
\mu=32^{3/4}.
\tag{15}
\]

Additivity, multiplicativity and degeneration monotonicity give

\[
a_i^k\ge\tau^k+t^{3/4}-s^{3/4}.
\tag{16}
\]

The function `x^(3/4)` is increasing and subadditive on nonnegative
numbers. Equation (14) therefore gives

\[
t^{3/4}-s^{3/4}
\le(q+s)^{3/4}-s^{3/4}
\le q^{3/4}\le\mu^k.
\tag{17}
\]

Consequently every numerical lower bound on `a_i` furnished by one
inequality (16) is at most

\[
\left(\tau^k+\mu^k\right)^{1/k}
\le\tau+\mu.
\tag{18}
\]

The last inequality follows by expanding `(tau+mu)^k`. If the right
side of (16) is negative, it provides no positive lower bound, which
also satisfies this ceiling. No optimization over f, s, t, or k can
invalidate (18) within the stated route.

## 5. Comparison with the existing symmetrized scalar profile

The [archived scalar theorem](../2026-10-20/research_note.md), Sections
1--2, imports positivity, symmetry, concavity and shifted tripling for
every actual symmetrized character profile, then proves its pointwise
lower bound `P >= P_*`. The
[external-route record](../../../docs/nine_fourths_route.md) records that
bridge. In this case

\[
h_4=\frac43\frac76\frac{10}{9}=\frac{140}{81},\qquad
P_*(5,4)=\frac{140}{81}\left(5+\frac32\right)
=\frac{910}{81}.
\tag{19}
\]

The [existing paired identity](../2026-10-21-correction-budget/critical_coefficient.md)
is

\[
a_1a_2a_3=P(5,4)^{9/2}.
\tag{20}
\]

Thus the established lower bound concerns the **geometric mean**
`(a_1 a_2 a_3)^(1/3) >= P_*^(3/2)`. It does not assert
`a_i=P^(3/2)` or `a_i>=P_*^(3/2)` for every orientation separately.

The following exact separation is sufficient:

\[
\tau+\mu<23+14=37
<\left(\frac{910}{81}\right)^{3/2}=:a_*.
\tag{21}
\]

All comparisons are decided by positive integer powers:

\[
512<23^2,\qquad32^3<14^4,\qquad
37^2\,81^3<910^3.
\tag{22}
\]

Hence the equal cyclic assignment `a_1=a_2=a_3=a_*` satisfies every
one-slice inequality covered by (13)--(18), for every k and every slice.
Its product is exactly the value prescribed by `P_*(5,4)` in (20).
The product lower bound obtained from those cyclic inequalities is also
weaker than the already established symmetrized-profile lower bound.

This proves that this family of additional scalar inequalities cannot
exclude the existing feasible endpoint scalar profile. It does **not**
construct an actual character realizing that profile, make actual
oriented character values equal, or show that every tensor inequality
is implied by the old scalar system. It also does not exclude a later
use of (1) in a construction containing other information.

## 6. Exact replay and evidence boundary

The standard-library verifier checks the saved seed completely, the
three initial kernel ranks over Q, both selected long-map determinants,
the permutation slice, its eight-term compressed factorization, the
appended cancellation, the k=1 and k=2 formula values, local source
hashes, and all strict integer comparisons in (22). The all-power and
uniform-ceiling claims are written proofs above, not finite searches.

```bash
python -S research/ai/2026-10-23-one-slice-seed-audit/verify.py
python -S -m unittest discover -s tests -p test_one_slice_seed_audit.py -v
```

`certificate.json` is the exact saved output. `sources.json` separates
the versioned external theorem, unchanged local seed, existing scalar
bridge, and this application. Same-session checks and passing tests do
not change the mathematical review status.
