# Exact cactus and ordinary rank of the canonical mixed target

Date: 2026-10-23. Owner-directed Codex work. Written proof with same-session
audits; no independent mathematical review or formalization is claimed.

## 1. Result and scope

Work over the complex numbers. Use the common first coefficient basis
`a_0,...,a_4` and disjoint second- and third-leg intervals for every block.
The literal block conventions are

\[
\begin{aligned}
\mathrm{Full}(a,b)&=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
 a_i\otimes b_j\otimes c_{i+j},\\
\mathrm{Mid}(a,b)&=\sum_{i=0}^{a-1}\sum_{k=0}^{b-1}
 a_i\otimes b_{i+k}\otimes c_k,\\
\mathrm{Out}(u,v)&=\sum_{j=0}^{u-1}\sum_{k=0}^{v-1}
 a_{j+k}\otimes b_j\otimes c_k,
 \qquad u+v-1=a.
\end{aligned}
\tag{1}
\]

Let

\[
T=7\mathrm{Full}(5,2)+10\mathrm{Full}(5,3)
 +4\mathrm{Out}(3,3)+2\mathrm{Out}(4,2)+6\mathrm{Mid}(5,2).
\tag{2}
\]

The additions share only the first leg. Thus `dim A=5`, `dim B=100`,
and `dim C=140`. The claim is

\[
\boxed{\operatorname{cr}(T)=\operatorname{sr}(T)
 =\operatorname{R}(T)=178.}
\tag{3}
\]

Here `cr` is cactus rank: the smallest length of a finite scheme on the
three-factor Segre variety whose projective linear span contains `[T]`.
The smoothable rank `sr` imposes that the finite scheme is smoothable.
Ordinary tensor rank `R` uses a reduced finite set. Consequently
`cr <= sr <= R`.

Equation (3) is proved directly. No rank-additivity theorem or conjecture
is assumed. It does **not** give border rank 178. In particular it does not
exclude a degeneration from `10 Full(5,10)`, whose border rank is 140.
If the target has border rank 140, then its smoothable rank exceeds its
border rank by 38; any such realization is wild in that precise sense.

The common first basis in (1) is part of the hypothesis. A global change
of any leg preserves the conclusion. Independent changes of the first
basis of different blocks are outside the equality claim (3). They still
obey the weaker cactus-rank lower bound 168, as explained in Section 5.

## 2. A low-rank curve gives a cactus-rank lower bound

**Lemma.** Let `U` belong to `A tensor B tensor C` and be concise in the
second and third legs, of dimensions `b` and `c`. Let
`X` be an irreducible, linearly nondegenerate projective subvariety of
`P(A*)`. Suppose every contraction `U(alpha)`, for `[alpha]` in `X`,
has ordinary matrix rank at most `s`. Then

\[
\operatorname{cr}(U)\ge b+c-s.
\tag{4}
\]

Linearly nondegenerate means that `X` is contained in no hyperplane of
`P(A*)`. The lemma also applies to a polynomially parametrized curve
whose image is contained in no hyperplane, by using its projective closure.

### From a finite Segre scheme to a finite algebra

Let `Z` be any finite scheme of length `r` in
`P(A) times P(B) times P(C)` with `[U]` in its Segre linear span.
Write `R=H^0(Z,O_Z)`. The scheme is affine and `dim_C R=r`.
Every line bundle on this finite scheme is trivial: its algebra is a
finite product of Artinian local algebras, and an invertible module is
free of rank one on each factor.

Choose trivializations of the restrictions of `O(1,0,0)`, `O(0,1,0)`,
and `O(0,0,1)`. Restriction of sections gives linear maps

\[
\tau_A:A^*\longrightarrow R,\qquad
\tau_B:B^*\longrightarrow R,\qquad
\tau_C:C^*\longrightarrow R.
\]

Under the product trivialization, the restriction map in multidegree
`(1,1,1)` sends `alpha tensor beta tensor gamma` to
`tau_A(alpha) tau_B(beta) tau_C(gamma)`.
The span assumption says that the trilinear functional `U` annihilates
the kernel of this restriction map. It therefore defines a functional
on its image. Extend that functional linearly to some `lambda:R -> C`.
Surjectivity of the restriction map is not required. We obtain

\[
U(\alpha,\beta,\gamma)
=\lambda\bigl(\tau_A(\alpha)\tau_B(\beta)\tau_C(\gamma)\bigr).
\tag{5}
\]

### Choosing a unit and a perfect pairing

For each closed support point `z` of `Z`, the condition that
`tau_A(alpha)` vanish at `z` is a proper hyperplane in `A*`. This uses
that the first projection of `z` is an actual point of `P(A)`.
Since `X` is irreducible and contained in no hyperplane, it is not contained
in the finite union of these hyperplanes. Choose `[alpha]` in `X` avoiding
them all. Then `tau_A(alpha)` is a unit of the finite algebra `R`.

Define

\[
J=\{x\in R:\lambda(xy)=0\text{ for every }y\in R\}.
\]

This is an ideal: if `x` is in `J`, then
`lambda((rx)y)=lambda(x(ry))=0`. Also `lambda(J)=0`, by taking `y=1`.
The quotient `Q=R/J`, of dimension `d <= r`, thus has the nondegenerate
bilinear pairing `(x,y) -> lambda(xy)`. Multiplying either argument by
the unit `u=tau_A(alpha)` preserves nondegeneracy.

The induced maps from `B*` and `C*` to `Q` are injective.
For example, if `tau_B(beta)` belongs to `J`, then (5) vanishes for
every `alpha,gamma`. Second-leg conciseness forces `beta=0`.
The third-leg argument is identical. Their images therefore have
dimensions `b` and `c` in the `d`-dimensional perfect-pairing space `Q`.

The restriction of a perfect pairing to subspaces of dimensions `b,c`
has rank at least `b+c-d`: the left kernel has dimension at most `d-c`.
Apply this to the unit-twisted pairing `(x,y) -> lambda(uxy)`. By (5),
its restriction is exactly the slice `U(alpha)`. Hence

\[
s\ge\operatorname{rank}U(\alpha)\ge b+c-d\ge b+c-r.
\]

This proves (4), since `Z` was arbitrary. It also proves the weaker
generic-slice bound `cr(U) >= b+c-max_alpha rank U(alpha)` by taking
`X=P(A*)`.

## 3. The common evaluation curve has slice rank 62

Consider the rational normal curve in the first dual space,

\[
\alpha(t)=a_0^*+t a_1^*+t^2a_2^*+t^3a_3^*+t^4a_4^*,
\qquad t\in\mathbb C.
\tag{6}
\]

It is contained in no hyperplane: a linear functional vanishing on (6)
would be a polynomial of degree at most four vanishing identically.
Equivalently, five distinct finite parameter values give an invertible
Vandermonde matrix. A finite union of support hyperplanes therefore
excludes only finitely many parameters in the proof of the lemma.

For a Full block, contraction by (6) is multiplication by the nonzero
polynomial `1+t z+...+t^4 z^4`. It has rank `b`; alternatively its first
`b` output coordinates give a triangular minor with diagonal entries one.
The Mid block is the transpose and also has rank `b`.
For a shared-output block the matrix entries are

\[
\alpha(t)_{j+k}=t^{j+k}=t^j t^k.
\]

This is the outer product `(1,t,...,t^(u-1))` and
`(1,t,...,t^(v-1))`, so its rank is exactly one.
The point at infinity has the same block ranks, although finite `t`
already suffices for the lemma.

All long-leg intervals are disjoint. Matrix rank therefore adds across
the blocks for this particular contraction, giving

\[
\operatorname{rank}T(\alpha(t))
=7\cdot2+10\cdot3+4\cdot1+2\cdot1+6\cdot2
=62.
\tag{7}
\]

Each individual block is concise in both long legs. This can be seen
directly from (1): distinct long-leg slice coefficients occur in distinct
basis coordinates or on distinct coefficient diagonals. Disjoint long-leg
intervals preserve conciseness in the sum. Thus the second and third
flattening ranks are 100 and 140, respectively. The verifier also
reconstructs these full flattenings from the literal coefficients.

Apply the lemma with `b=100,c=140,s=62`:

\[
\operatorname{cr}(T)\ge100+140-62=178.
\tag{8}
\]

For comparison, a generic first slice has rank 72, giving only the weaker
bound 168. At the explicit coefficient vector `(1,2,3,5,7)`, the
`Out(3,3)` Hankel determinant is one and every `Out(4,2)` block has rank
two, so 72 is attained. This comparison does not enter the sharper proof.

## 4. Interpolation gives the matching 178-term decomposition

For polynomial input lengths `u,v`, put `m=u+v-1`. Choose the `m`
distinct rational nodes `0,...,m-1`. Let

\[
e_u(t)=(1,t,\ldots,t^{u-1}),\qquad
L_t(z)=\prod_{\substack{0\le s<m\\s\ne t}}\frac{z-s}{t-s}.
\]

Write `ell_t` for the coefficient vector of `L_t` in the length-`m`
output space. Ordinary polynomial interpolation gives the tensor identity

\[
\mathrm{Full}(u,v)
=\sum_{t=0}^{m-1}e_u(t)\otimes e_v(t)\otimes\ell_t.
\tag{9}
\]

Permuting its factors gives the Mid and shared-output decompositions.
Every summand is rank one and has rational coefficients. Equation (9)
gives the following upper bound for (2):

| Block | Copies | Terms per copy | Total |
| --- | ---: | ---: | ---: |
| `Full(5,2)` | 7 | 6 | 42 |
| `Full(5,3)` | 10 | 7 | 70 |
| `Out(3,3)` | 4 | 5 | 20 |
| `Out(4,2)` | 2 | 5 | 10 |
| `Mid(5,2)` | 6 | 6 | 36 |
| All blocks | 29 | | 178 |

Thus `R(T) <=178`. Together with `cr <= sr <= R` and (8), this proves
(3). The same interpolation argument gives rank at most 140 for
`10 Full(5,10)`. Its third flattening has rank 140, so both its ordinary
rank and border rank are exactly 140.

The argument also proves a general canonical-block statement. For any
shared-first sum of the three block types in (1), with common first
dimension `a`, cactus, smoothable and ordinary ranks all equal the sum
of their interpolation lengths: `a+b-1` for Full and Mid, and `a` for
each shared-output block. On the common evaluation curve the slice ranks
are `b,b,1`, and the lower bound `dim B+dim C-s` is exactly that sum.
This is a consequence of the curve lemma, not an assumed additivity rule.

## 5. Border rank remains unresolved

Border rank is the least number of rank-one tensors in an approximating
family. A limit of their spans need not be the span of the limiting
finite scheme. That possible drop in span dimension is exactly why the
finite-scheme proof above cannot be applied to an arbitrary border
decomposition. Cactus rank is not a degeneration-monotone replacement
for border rank in this argument.

If every target block receives its own invertible first-leg identification,
the generic matrix rank of each block is unchanged. A generic first
covector simultaneously avoids the finitely many proper rank-drop loci,
so the maximum first-slice rank remains 72. The generic-slice form of the
lemma therefore still gives cactus rank at least 168 for every such target.
The common low-rank evaluation curve need not survive these independent
identifications, so the value 178 is not asserted in that broader scope.

Consequently the interval presently established for the target's border
rank remains `140 <= border rank(T) <=178`. The lower endpoint comes
only from third-leg conciseness. If the proposed source degeneration
exists, its border rank must be 140, while (3) forces smoothable and
cactus ranks to remain 178. No such degeneration or border decomposition
is constructed here, and no exponent improvement follows.

## 6. A small canonical sum already has a wild rank gap

The distinction is essential even within canonical Full/Mid sums.
Consider

\[
W=\mathrm{Full}(2,1)+\mathrm{Mid}(2,1)
=a_0b_0c_0+a_1b_0c_1+a_0b_1c_2+a_1b_2c_2,
\tag{10}
\]

in format `(2,3,3)`, with tensor product signs suppressed only in (10).
Its three ordinary flattening ranks are `(2,3,3)`. In the displayed
second- and third-leg bases, its first contraction is

\[
W(s a_0^*+t a_1^*)=
\begin{pmatrix}s&t&0\\0&0&s\\0&0&t\end{pmatrix}.
\tag{11}
\]

For every nonzero pair `(s,t)` this matrix has rank two: its first row
has a nonzero entry among the first two columns, and its third column
is nonzero in the last two rows. The curve lemma with `X=P(A*)` gives
`cr(W)>=3+3-2=4`. The four displayed monomials give `R(W)<=4`, so

\[
\operatorname{cr}(W)=\operatorname{sr}(W)=\operatorname{R}(W)=4.
\]

Nevertheless its border rank is three. Indeed, inside the space of all
complex `(2,3,3)` tensors, the matrix pencils `(M_0,M_1)` for which
`M_0` is invertible and `M_0^{-1}M_1` has three distinct eigenvalues form
a nonempty Zariski-open set. Nonemptiness follows from
`M_0=I_3, M_1=diag(0,1,2)`. Left and right basis changes transform any
such pencil to `(I_3,diag(lambda_1,lambda_2,lambda_3))`, with decomposition

\[
\sum_{j=1}^3 (a_0+\lambda_j a_1)\otimes b_j\otimes c_j.
\]

Thus a dense open set has rank three. Its closure is the entire tensor
space, so every tensor in this format has border rank at most three.
The third flattening of `W` supplies the matching lower bound.
Consequently `border rank(W)=3<cr(W)=4`.

This example supplies no degeneration for the `(5,100,140)` candidate.
It shows why a blanket assertion that canonical block sums cannot be
wild would be false.

## 7. Reproduction and provenance

Run from the repository root:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_cactus.py
python -m unittest discover -s tests -p 'test_mixed_longlegs_cactus.py' -v
```

The standard-library verifier pins the discovery input, independently
reconstructs both literal tensors, checks all three flattening ranks,
checks the evaluation slices at five distinct parameters and at infinity,
checks the explicit rank-72 slice, and reconstructs every coefficient of
the six required interpolation identities over the rational numbers.
It also exports their exact Lagrange coefficients and checks the toy
tensor's three flattenings and four slices. These are finite
convention and witness checks; the arbitrary-scheme lower bound is the
written proof in Section 2.

The finite-algebra description of scheme spans is standard. Relevant
primary references are Jelisiejew--Landsberg--Pal,
[*Concise tensors of minimal border rank*, arXiv:2205.05713v4,
Proposition 9.1](https://arxiv.org/pdf/2205.05713v4), for the equal-dimension
minimal-rank setting, and Jagiełła--Jelisiejew,
[*Unrestrictions and concise secant varieties*, arXiv:2604.24879v1,
Theorem 4.10 and Corollary 4.11](https://arxiv.org/html/2604.24879v1#S4.SS2),
for general finite-scheme spans and regular restrictions. Their hypotheses
and conclusions are not replaced by an assertion about border rank.
Section 2 supplies the required direction directly, including the
functional extension and quotient by the pairing radical.

The source rank and candidate were identified in the owner-directed
session. The curve bound, its canonical-block application and the exact
controls are local deductions using standard algebra and interpolation.
The parent and another research agent checked the finite-support and
pairing arguments in this same session. This is not external independent
review, a formal proof, or a claim of historical priority.
