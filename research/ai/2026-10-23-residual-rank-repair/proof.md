# Finite and asymptotic repair gates from residual support ranks

October 23, 2026. Owner-directed Codex work. Written conditional proofs,
without independent mathematical review or formalization. **No paired
construction satisfying either improvement gate is supplied. No smaller
matrix multiplication exponent is established.**

The earlier correction criteria bound the auxiliary tensor by its border
rank. Here its three flattening ranks can give a smaller character bound.
This yields a finite stopping criterion and a larger quantified repair
class. It is a deduction from existing source estimates, not a new source
degeneration or a claim of historical priority.

## 1. Source, target, and construction premise

Work over the complex numbers. Use the maintained paired source

\[
Q(n,b)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{b-1}
A_{pq}\otimes B_{y,q+v}\otimes C_{p+y,v},
\]

with format `(n^2,b(n+b-1),b(n+b-1))`. The target is

\[
M(l,h,r)=\sum_{i<l,\alpha<h,j<r}
a_{ij}\otimes b_{i\alpha}\otimes c_{\alpha j},
\]

with format `(lr,lh,hr)`. The first target leg is the output leg.

For a tensor E, let `(r_A,r_B,r_C)` be its flattening ranks and set

\[
D(E)=\min\{r_A r_B,r_A r_C,r_B r_C\}.
\tag{1}
\]

Certified upper bounds for the three ranks can be used in (1). Ambient
dimensions alone are also valid, but can be much weaker. Every rank must
belong to the actual residual tensor. A small numerical residual norm
does not provide such a rank certificate.

The finite construction premise is a genuine degeneration

\[
Q(n,b)\oplus E\unrhd M(l,h,r).
\tag{2}
\]

An exact coefficient identity `(local maps) Q = M-E` suffices: use E as
the added summand and sum its three target spaces with those of M-E.
More generally, if Q degenerates to M-E, direct-sum monotonicity followed
by those summation maps proves (2). All coefficients, including unwanted
ones and negative Laurent powers, must be checked. E is an actual tensor
in the premise, not a formal subtraction in a semiring.

## 2. An elementary outer-product envelope

After restricting to its concise support, E belongs to
`C^(r_A) tensor C^(r_B) tensor C^(r_C)`. It is a restriction of the outer
product tensor with dimensions `(r_A,r_B,r_A*r_B)`: map its output basis
vector indexed by `(i,j)` to the corresponding E coefficient vector in
the third factor. Repeating with the other two pairs gives three such
restrictions. This is valid over any field.

In the notation of the previous correction-budget note, p_i is the
character exponent of a dot product missing leg i. At a hypothetical
endpoint character `p_1+p_2+p_3=9/4`, the previously proved rigidity
forces every p_i to equal 3/4. Consequently

\[
\lambda(E)\le D(E)^{3/4}.
\tag{3}
\]

The same bound applies to every cyclic permutation of E. It is not a
bound on scalar border rank. It is a bound on endpoint character values,
used only inside the contradiction argument below.

If E is supplied as a sum of tensors E_j in common target spaces, then
E is a restriction of their direct sum. Thus one may replace the right
side of (3) by `sum_j D(E_j)^(3/4)`. A certified scalar border-rank bound
can be used instead for any individual piece when it is smaller.

## 3. A shifted finite source estimate

Fix b and write `f(n)=P(n,b)` for the existing symmetrized character
profile. At an endpoint character, the earlier thin-slope argument gives

\[
\limsup_{N\to\infty}\frac{f(N)}N
\le L_b:=\frac23(6b)^{1/3}.
\tag{4}
\]

The exact shifted-tripling inequality is

\[
f(3n+b-1)\ge3f(n).
\tag{5}
\]

Put `c=(b-1)/2` and `n_k=3^k(n+c)-c`. Each n_k is an integer because
3^k-1 is even. Iterating (5) and applying (4) gives

\[
f(n)\le\frac{f(n_k)}{3^k}
=\frac{f(n_k)}{n_k}\frac{n_k}{3^k}
\quad\Longrightarrow\quad
\boxed{P(n,b)\le L_b\left(n+\frac{b-1}{2}\right)
=\frac{(6b)^{1/3}}3(2n+b-1).}
\tag{6}
\]

This holds for all positive integers n,b, even when n<b, since n_k
eventually exceeds b. It improves by one the `2n+b` factor obtained
directly from the earlier homogeneous tangent estimate. Only the existing
tripling inequality and limiting slope enter this finite refinement.

## 4. One finite repaired target can exclude the endpoint

**Finite gate.** Suppose (2) is constructed for one set of positive
integer dimensions. If

\[
\boxed{(lhr)^{3/4}
>D(E)^{3/4}+\frac13\sqrt{2b(2n+b-1)^3},}
\tag{7}
\]

then `omega_C<9/4`. For several supplied residual pieces, replace the
single repair cost in (7) by their sum from Section 2.

**Proof.** Suppose an endpoint character exists. Let a_i be its value
on the cyclic source whose n-squared leg occupies position i. The prior
paired-source product identity and (6) give

\[
\prod_{i=1}^3a_i=P(n,b)^{9/2}\le U^{9/2},
\qquad U=\frac{(6b)^{1/3}}3(2n+b-1).
\tag{8}
\]

Every cyclic target has value `T=(lhr)^(3/4)`. Applying (2) in each
orientation and using (3) gives

\[
a_i\ge T-D(E)^{3/4}.
\tag{9}
\]

By (7), this common lower bound is positive and strictly greater than

\[
U^{3/2}=\frac13\sqrt{2b(2n+b-1)^3}.
\]

Multiplying (9) contradicts (8). This uses the product of the three
source values. It does not bound each a_i by a symmetrized profile.

The matrix-spectrum sum attains its maximum omega. Excluding every
endpoint character, together with the external bound omega<=9/4,
therefore gives omega<9/4. Compact attainment is the same external input
already used by the critical-coefficient note; it is stated in
Alman--Li, arXiv:2605.21738v1, Proposition 4.2.

An unbounded family is unnecessary for this strict finite implication.
The proof does not give a numerical value below 9/4 from the strict
inequality alone. Failure of (7) is only failure of this sufficient gate;
it is not an obstruction to the proposed tensor degeneration.

### Smallest full targets for this finite paired gate

For E=0 and the full equal-width target M(n,b,n), (7) is equivalent to
the integer comparison

\[
81bn^6>4(2n+b-1)^6.
\tag{9a}
\]

Among all positive integer n,b passing (9a), the minimum of the largest
source leg `max(n^2,b(n+b-1))` is 441. Only `(n,b)=(21,8)` and `(21,9)`
attain it, giving source formats `(441,224,224)` and `(441,261,261)`.
Their respective target formats are `(441,168,168)` and `(441,189,189)`.
Both allow only D=0 under this gate.

This finite census gives a global minimum for the stated objective:
the largest source leg is at least both n-squared and b-squared.
Any value below 441 therefore forces `n,b<=20`. The complete 400-pair
check rejects every smaller format. The complete 441-pair check through
`n,b<=21` leaves exactly the two minimizers above. For b<=3 one can
also reject the gate directly from `81b<256` and
`(2n+b-1)^6>=(2n)^6`.

The next n=22 permits nonzero residual pair products:

| b | Source format | Target format | Largest accepted D |
|---:|---|---|---:|
| 7 | (484,196,196) | (484,154,154) | 4 |
| 8 | (484,232,232) | (484,176,176) | 9 |
| 9 | (484,270,270) | (484,198,198) | 10 |

These minima concern only this paired-source criterion. The repository
already contains other conditional targets with smaller formats, including
the 112-dimensional cyclic A4 source. No global minimality among tensor
constructions is claimed, and none of these new benchmark maps is supplied.

### Exact numerical targets for width four

With no residual, `Q(n,4) -> M(n,4,n)` first satisfies this gate at n=38.
For `Q(n,4) -> M(n-1,4,n-1)`, the first n is 64. These are unconstructed
finite targets, not successful maps.

The table gives the largest integer D accepted by (7) for a single
residual and target `M(n-1,4,n-1)`. Its last column assumes both long
residual ranks are at most `4(n-1)` and records a sufficient first rank.

| Source n | Largest accepted D | Sufficient first residual rank |
|---:|---:|---:|
| 64 | 0 | 0 |
| 100 | 230 | 0 |
| 200 | 2,121 | 2 |
| 500 | 18,393 | 9 |
| 1,000 | 80,775 | 20 |
| 10,000 | 8,739,465 | 218 |

For example, a single exact identity from Q(200,4) to M(199,4,199)
with residual ranks at most `(2,796,796)` would suffice. The crude
scalar-rank bound from these dimensions is 1592. The new endpoint cost
is at most `1592^(3/4)`, which fits the finite gate. No such identity
is supplied here.

## 5. Quantified repair rates with a sublinear first support

Fix an integer b>=4 and `0<=gamma<1`. Suppose one unbounded sequence
of genuine complex degenerations has

\[
Q(n,b)\oplus E_n\unrhd M(l_n,b,r_n),
\qquad l_n/n\to1,\quad r_n/n\to1,
\tag{10}
\]

and the residual flattening ranks satisfy

\[
r_A(E_n)=O(n^\gamma),\qquad
r_B(E_n)=O(n),\qquad r_C(E_n)=O(n).
\tag{11}
\]

A is the n-squared/output leg in (10). All maps, the integer sequence,
and rank bounds are fixed independently of the tensor character.
Every individual degeneration must be proved; there is no assumption
of uniform Laurent order as n varies.

Let `d_b` be the unique positive root

\[
d_b(6b)^{d_b}=12b^{3/2},\qquad B_b=3/d_b.
\]

**Quantified gate.** Under (10)--(11),

\[
\boxed{\omega\le
\max\left\{B_b,\ \frac94-\frac{(1-\gamma)^2}{4}\right\}.}
\tag{12}
\]

**Proof.** Fix a character, write `S=sum p_i` and `delta=9/4-S`, and
suppose S exceeds both terms on the right of (12). Then S>2 and
`sqrt(delta)<(1-gamma)/2`. In orientation i the outer-product bounds
using the first residual factor and either long factor give

\[
\lambda(E_{n,i})
\le O\!\left(n^{p_i+\gamma\min\{p_j,p_k\}}\right),
\quad\{i,j,k\}=\{1,2,3\}.
\tag{13}
\]

The source is O(n^(S-p_i)) and the target is Theta(n^(S-p_i)) in this
orientation.
Using `min(p_j,p_k)<=(S-p_i)/2`, the gap between this exponent and
the residual exponent is at least

\[
(1-\gamma/2)S-(2-\gamma/2)p_i.
\tag{14}
\]

The previous one-coordinate localization bound says
`p_i<=3/4-delta+sqrt(delta)`. Substituting it in (14) gives

\[
\begin{aligned}
\text{gap}&\ge
\delta-\frac{4-\gamma}{2}\sqrt\delta+\frac34(1-\gamma)\\
&=\left(\sqrt\delta-\frac{1-\gamma}{2}\right)
  \left(\sqrt\delta-\frac32\right)>0.
\end{aligned}
\tag{15}
\]

Thus each cyclic correction is `o(n^(S-p_i))`. The source bound
`a_i(n)<=b^(2p_i)n^(S-p_i)` controls all seven correction terms when
the three target inequalities are multiplied. After division by
`n^(2S)`, they disappear, giving

\[
\liminf\frac{P(n,b)}n\ge\sqrt b.
\]

For d=3/S, the earlier slope theorem gives the opposing upper bound
`d(6b)^d/(12b)`. It is strictly below sqrt(b) when S>B_b. This
contradiction proves (12) through the existing character detection.

At gamma=7/10, the localization term is 891/400=2.2275. The earlier
integer certificate `B_4<30000/13433<2.2334` therefore supplies the
same strict rational consequence under (10)--(11). The elementary
scalar-rank estimate for such residuals is only O(n^(17/10)), outside
the older subcritical scalar-rank budget. At gamma=3/4 and 9/10,
(12) instead gives 143/64=2.234375 and899/400=2.2475 respectively.
Every number in this paragraph remains conditional on the missing maps.

### A qualitative product budget

The same endpoint argument permits

\[
\limsup\frac{D(E_n)}{n^2}
<\left((\rho\sigma h)^{3/4}-\frac43\sqrt b\right)^{4/3},
\tag{16}
\]

for targets with `l_n/n->rho>0`, `r_n/n->sigma>0`, provided the inner
parenthesis is positive. Indeed, divide the finite gate costs by
n^(3/2) and use strictness. For width four and near-full outer dimensions,
the right side is `(2 sqrt(2)-8/3)^(4/3)`, approximately 0.088138.
The decimal is descriptive. In particular, `D(E_n)=o(n^2)` suffices
for a strict qualitative improvement. No premise in this paragraph is
claimed to have been constructed.

## 6. Existing construction control, evidence, and limits

The pinned integer restriction `Q(5,4) -> M(4,4,4)` supplies a concrete
control. Embed its target as a principal corner of M(5,4,5). The missing
36 scalar products give a residual with exact ranks `(9,20,20)`, hence
D=180. The repaired identity exists, but it fails (7), as expected.
This control does not give a new restriction or exponent result.

The verifier uses exact integer roots and rational outward intervals
for every acceptance decision. It checks each budget and its next
integer, the first no-residual thresholds, literal outer-product
identities, and the existing corner residual's ranks. It also checks
510 exact instances of the localization factorization. Tests include
rank corruption and equality controls. These checks support the written
proofs; they do not certify the missing paired maps or formalize the
universal character arguments.

The separate `separate_replay.py` was written by another agent in this
session and imports no acceptance helper. It uses integer square roots
to recheck the finite minimum, full-target budgets, and 5100 rational
localization identities. Its code independence is not independent
mathematical review.

```sh
python research/ai/2026-10-23-residual-rank-repair/verify.py --output results/local/residual-rank-gates.json
python research/ai/2026-10-23-residual-rank-repair/separate_replay.py
python -m unittest discover -s tests -p test_residual_rank_repair.py -v
```

`sources.json` pins the prior source estimates, rigidity proof, finite
amplitude discussion, and integer seed. The external character framework
and 9/4 theorem retain OpenAI's credit; oriented rescaling retains
Uznański's credit. Compact attainment retains Strassen's framework and
the cited Alman--Li statement. The outer-product argument is elementary
and is not claimed as a historical novelty. The finite shifted-tripling
refinement was identified and the new gap was checked by another agent
in this generating session. That is not independent mathematical review.
