# Replication, the scaling limit, and rigidity at 9/4

October 20, 2026. AI-derived written argument by Codex at the owner's request.
Unreviewed and not Lean-formalized. No smaller exponent is established.

## Scope and relation to prior work

The second-pass draft assumed a homogeneous limit and differentiability at
the diagonal. This note derives the limit from the already stated scalar
replication and rank inequalities, and removes the differentiability assumption
from both the rigidity and curvature arguments.

Rescaling convolution profiles is **prior external work**: Uznański v2,
Lemma 4.1 and Appendix F, already constructs homogeneous limits of the oriented
profiles. The first-pass recurrence, the second-pass rigidity formula and its
curvature target are also prior local work. The result here is a self-contained
completion of the local analytic bridge, including the nonsmooth case. It is
not a new tensor construction, a new replication theorem, or an improvement
of OpenAI's exponent.

A later fetch also found the concurrent actual-character rigidity/curvature
note on the Koszul branch, observed at
[`30219d0`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/30219d0).
Its main rigidity and curvature conclusions overlap Sections 2-4 here; they
must not be counted as separate theorem advances. This note's additional
content is the direct scalar construction of the full limit in Section 1,
the exact flattening-character control, and the compactness consequence in
Section 5. This comparison is scope reconciliation, not independent review.

## 1. Hypotheses and existence of the full scaling limit

Let `P` be positive and symmetric on positive integer pairs, with `P(1,b)=b`
and separate discrete concavity on the positive axes. For a fixed real `d>0`,
assume for all positive integers `a,b,q` that

$$P(qa,qb)\ge q^dP(a,b),\qquad
P(a,b)\le(a+b-1)^d. \tag{R,U}$$

Also assume shifted tripling

$$P(a,3b+a-1)\ge3P(a,b). \tag{T}$$

For actual symmetrized tensor-character profiles, `d=1/t`. (U) and (T) are
from OpenAI. (R) follows from Uznański's replication degeneration and character
additivity; see the source section. Positivity and concavity imply monotonicity
on the whole positive axis, by the argument in the filtration note.

**Scaling theorem.** For all positive real `x,y`, the full limit

$$F(x,y)=\lim_{N\to\infty}
\frac{P(\lceil Nx\rceil,\lceil Ny\rceil)}{N^d} \tag{L}$$

exists and is finite and positive. It is continuous, symmetric, homogeneous
of degree `d`, separately concave, and coordinatewise nondecreasing. It obeys

$$F(x,y)\le(x+y)^d,\qquad F(x,3y+x)\ge3F(x,y). \tag{H}$$

For integer `a,b` there is the additional exact characterization

$$F(a,b)=\sup_{n\ge1}\frac{P(na,nb)}{n^d}\ge P(a,b). \tag{S}$$

**Proof on integer pairs.** Write `u_N=P(Na,Nb)/N^d`. It is bounded above
by `(a+b)^d`. Fix `n` and put `q=floor(N/n)`. For sufficiently large `N`,
monotonicity and replication give

$$P(Na,Nb)\ge P(qna,qnb)\ge q^dP(na,nb).$$

After division by `N^d` and passage to the lower limit,

$$\liminf_N u_N\ge\frac{P(na,nb)}{n^d}.$$

Take the supremum over `n`. Every `u_N` is at most that supremum, so the
lower and upper limits agree with it. This proves (S), positivity and the
integer-pair limit. Ordinary monotonicity of `u_N` was not assumed.

**Rational extension.** Taking subsequences gives
`F(ka,kb)=k^d F(a,b)` for integers `k>0`. Define the value at a positive
rational pair by division by a common denominator; this homogeneity makes it
well-defined. Monotonicity and symmetry pass to the limit. Discrete concavity,
applied at a common integer scale, gives every rational concavity inequality.
The upper bound is inherited from (U).

For rational `x=a/r,y=b/r` and `m=floor(N/r)`, the rounded inputs in (L)
are between `(ma,mb)` and `((m+1)a,(m+1)b)`. The integer-pair limit proves
(L) along **all** `N`, not only multiples of a denominator.

**Continuity and real extension.** Nearby positive rational pairs can be
squeezed coordinatewise between `(1-epsilon)(x,y)` and
`(1+epsilon)(x,y)`. Monotonicity and homogeneity bound their values between
`(1-epsilon)^d F(x,y)` and `(1+epsilon)^d F(x,y)`. Local boundedness then
gives continuity and a unique extension to positive reals. Rational bounds
from above and below squeeze the rounded sequence in (L) to that same value.
Homogeneity and separate concavity pass to the extension.

Finally, at integer scale,

$$P(Na,N(3b+a))\ge P(Na,3Nb+Na-1)\ge3P(Na,Nb).$$

Passing to limits and then to rational and real pairs proves (H). No passage
of derivatives or unproved regular-variation hypothesis is used.

## 2. The diagonal derivative bound without differentiability

Put `f(s)=F(1,s)` and `v=f(1)>0`. Finite concavity on the open interval
`(0,infinity)` supplies finite one-sided derivatives at 1. Denote them by

$$r=f'_+(1),\qquad l=f'_-(1).$$

Symmetry and homogeneity give the exact relation

$$f(s)=s^d f(1/s).$$

Expand it at `s=1-h`, using the right derivative at `1/(1-h)>1`. This gives

$$l=dv-r.$$

Concavity says `l>=r`. Consequently

$$r\le\frac d2v. \tag{D}$$

This is not an appeal to Euler's formula at a possibly nonsmooth point. For
example, `F(x,y)=min(x,y)` is symmetric, homogeneous and separately concave,
but has `l=1,r=0` at the diagonal. Differentiability must be proved if used.
That example does not satisfy tripling.

## 3. Critical rigidity, with its analytic hypotheses established

Tripling and the right tangent bound from concavity give

$$3v\le f(4)\le v+3r\le(1+3d/2)v.$$

Thus `d>=4/3`. If `d=4/3`, equality holds throughout. In particular
`r=l=2v/3`: differentiability at the diagonal is a **conclusion**.

The supporting line at 1 is

$$L(s)=\frac{2v}{3}\left(s+\frac12\right),\qquad f(s)\le L(s)\ (s\ge1).$$

The equality `f(4)=L(4)` forces `f=L` on `[1,4]` by concavity. More generally,
if `b>=1` has `f(b)=L(b)`, then tripling and the same upper line give

$$f(3b+1)\ge3f(b)=L(3b+1)\ge f(3b+1).$$

Iterating `b -> 3b+1` from `b=1` gives an unbounded sequence of equality
points. Concavity fills the intervals between them. Symmetry and homogeneity
then determine the entire positive quadrant:

$$\boxed{F(x,y)=K\min(x,y)^{1/3}
\left(\max(x,y)+\frac{\min(x,y)}2\right),\qquad K=\frac{2v}{3}>0.} \tag{C}$$

Therefore any actual character at `t=3/4`, using the cited replication
degeneration, necessarily has this limiting **shape**. There remains a free
positive amplitude `K`. This does not prove that such a character exists or
that its finite-size profile is the first-pass minimum.

## 4. A rigorous conditional improvement test

For the same scaling limit define its normalized curvature by

$$\delta(F)=\frac{2f(2)-f(1)-f(3)}{f(1)}\ge0.$$

Set `s_j=f(j+1)-f(j)`. Concavity and (D) give

$$s_1\le r\le dv/2,\qquad
s_2=s_1-\delta(F)v,\qquad s_3\le s_2.$$

Therefore

$$3v\le f(4)=v+s_1+s_2+s_3
\le(1+3d/2-2\delta(F))v,$$

which proves

$$\boxed{d\ge\frac43(1+\delta(F)).} \tag{Q}$$

If every relevant character's limit has `delta(F)>=delta_0>0`, with the same
positive constant, then `d=1/t` and the external spectral conversion imply

$$\boxed{\omega\le\frac9{4(1+\delta_0)}.}$$

For example `delta_0=1/1000` would give `2250/1001`, approximately
`2.24775224775`. **No positive delta_0 is proved here.** The improvement
criterion now needs only this substantive new tensor input; the scaling limit
and diagonal derivative argument are no longer additional unproved premises
under the displayed assumptions.

In particular, a finite-size strict concavity observation whose normalized
curvature tends to zero does not satisfy the premise.

An actual flattening-rank character provides an exact control. Its dot-product
parameters are `(0,1,1)` up to permutation, so `t=2/3,d=3/2`, and

$$P(a,b)=\sqrt{ab(a+b-1)},\qquad F(x,y)=\sqrt{xy(x+y)}.$$

Here `delta(F)=2 sqrt(3)-1-sqrt(6)>0` and is less than `1/8`, as (Q)
requires at `d=3/2`. This example verifies the normalization used in the test;
it is one character and cannot supply a gain for every character.

## 5. Why excluding equality can also suffice

One need not necessarily prove a numerical uniform curvature constant first.
The space of normalized tensor characters is compact in the topology of
pointwise evaluation: each nonzero tensor coordinate lies in the compact
interval `[1,rank(T)]`, and normalization, additivity, multiplicativity and
restriction monotonicity are closed conditions in their product. The zero
tensor has coordinate zero. This uses the ordinary product compactness theorem.

The objective

$$t(\lambda)=\frac{\log_2\lambda(B_X(2))+
\log_2\lambda(B_Y(2))+\log_2\lambda(B_Z(2))}{3}$$

is continuous and attains its maximum. OpenAI bounds it by `3/4`. Hence a proof
that **no character at that endpoint can exist** would force the maximum to be
strictly smaller and give an exponent strictly below `9/4` by the same spectral
conversion. This compactness observation supplies no numerical gap by itself.

Formula (C) narrows that exclusion problem: a new asymptotic tensor constraint
inconsistent with **every** amplitude `K>0` in (C) would exclude the endpoint.
Neither such a constraint nor the required character exclusion is proved here.
In particular, the two-source fixed-label families cannot do it, by the other
theorem in this pass.

## Sources and verification boundary

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [pinned revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf),
  Sections 2, 4 and 5: character rules, the rank bound, concavity, tripling, and
  conversion of bounds for all characters to the arithmetic exponent.
- Przemysław Uznański, *Rectangular matrix multiplication from polynomial
  products*, [arXiv:2610.10494v2](https://arxiv.org/html/2610.10494v2),
  October 11, 2026, Lemma 2.2 and Appendix E: `C(qa,qb)` degenerates to `q`
  independent copies of `C(a,b)`. Additivity gives a factor `q` in every
  character, hence `q^(1/t)` in the symmetrized profile. Lemma 4.1 and Appendix F
  already establish oriented rescaling. These prior results are attributed
  inputs, not local discoveries or independently rebuilt Lean proofs.
- [Second-pass local draft](../2026-10-20-session2/research_note.md),
  Sections 4-5: the earlier differentiable equality calculation and proposed
  curvature criterion. The archive is preserved unchanged.
- [All-size filtration proof](research_note.md): monotonicity lemma and the
  obstruction to using the stated fixed-label families for an improvement.

The all-size conclusions depend on the written analytic arguments above.
Finite checks cannot prove existence of a limit, compactness, or a uniform
curvature gain. No computational experiment is reported as verification of
those claims.

Four exact symbolic/rational regression controls check the flattening-character
scaling formula and curvature, the critical shape's derivatives and tripling
equality, and the conditional fraction. Run them with:

```sh
python -m unittest discover -s tests -p test_homogeneous.py -v
```
