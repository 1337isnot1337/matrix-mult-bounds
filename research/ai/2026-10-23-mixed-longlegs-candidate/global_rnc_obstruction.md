# A rational-normal-curve obstruction to the mixed target

Date: 2026-10-23. Written proof with same-session mathematical audits.
The coordinating and theory agents independently developed the curve argument;
the coordinating and frontier agents supplied the catalecticant inequality.
This is a written proof using the standard geometric results identified below.
It is not a formal proof or an external independent review.

## 1. Statement and exact scope

Work over the complex numbers. In a common first basis `a_0,...,a_4`, put

\[
S=10\operatorname{Full}(5,10),
\]

with separate second and third spaces for the ten copies. The tensor
`Full(a,b)` has coefficients

\[
\operatorname{Full}(a,b)=
\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}a_i\otimes b_j\otimes c_{i+j}.
\tag{1}
\]

Let `T` be any tensor obtained from

\[
7\operatorname{Full}(5,2)+10\operatorname{Full}(5,3)
+4\operatorname{Out}(3,3)+2\operatorname{Out}(4,2)
+6\operatorname{Mid}(5,2)
\tag{2}
\]

by independent invertible changes of the first basis of its 29 blocks.
The blocks retain disjoint second and third intervals. Here

\[
\begin{aligned}
\operatorname{Mid}(a,b)&=\sum_{i,k}a_i\otimes b_{i+k}\otimes c_k,\\
\operatorname{Out}(u,v)&=\sum_{j,k}a_{j+k}\otimes b_j\otimes c_k,
\qquad u+v-1=5.
\end{aligned}
\tag{3}
\]

Both source and target have format `(5,100,140)` and are concise in
the third factor.

**Theorem.** There is no Laurent degeneration from `S` to any such `T`.
Equivalently, `T` is outside the closure of the
`GL(A) times GL(B) times GL(C)` orbit of `S`.

The source's common binary-form identification is a hypothesis. Independent
first changes of different source copies are not covered. The theorem allows
arbitrary mixing and poles on the long factors and arbitrary singular leading
first maps in the initially proposed degeneration. The argument replaces any
such proposed degeneration by an equivalent one with a regular invertible
first map, then contradicts the catalecticant inequality.

This rules out this source-target degeneration. It does not show that the
target's border rank exceeds 140: the closure of one rank-140 orbit can be
strictly smaller than the entire border-rank-140 locus. No exponent improvement
is claimed.

## 2. First projections of rank-one third slices

For a third-concise tensor `U`, define its third slice space and incidence by

\[
R_U=\operatorname{im}(U_C:C^*\longrightarrow A\otimes B),\qquad
Z_U=\{([a],[b]):a\otimes b\in R_U\}.
\tag{4}
\]

The first projection is a subset of `P(A)`. It is distinct from the
low-rank curve in `P(A*)` used for the earlier cactus-rank bound.
Let

\[
\Gamma=\{[s^4:s^3t:s^2t^2:st^3:t^4]:[s:t]\in\mathbb P^1\}
\subset\mathbb P(A).
\tag{5}
\]

### Rank-one Hankel matrices

A third slice of `Full(a,b)` is the `a`-by-`b` Hankel matrix
`(lambda_(i+j))`. Assume `a,b>=2`. If it has rank one, write it as
`u v^T`. Adjacent equal entries give

\[
u_i v_{j+1}=u_{i+1}v_j
\quad(0\le i<a-1,\ 0\le j<b-1).
\tag{6}
\]

If `v_0` is nonzero, the equations with `j=0` give
`u_(i+1)=r u_i`, where `r=v_1/v_0`. Necessarily `u_0` is nonzero.
The equations with `i=0` then give `v_(j+1)=r v_j`. Thus the first
factor is `[1:r:...:r^(a-1)]`.

If `v_0=0`, let `j_0>0` be its first nonzero position. Taking
`j=j_0-1` in (6) forces `u_0=...=u_(a-2)=0`. The last coordinate of
`u` is therefore nonzero. Taking `i=a-2` then forces
`v_0=...=v_(b-2)=0`. This is the point at infinity of the same curve.
Conversely, every such point occurs as a rank-one Hankel slice.

Consequently, the first projection of `Z_Full(5,b)` is exactly `Gamma`
whenever `b>=2`. After a first identification `g`, it is exactly
`g Gamma`.

### The other blocks contribute no rank-one third slices

For a nonzero third covector `gamma`, put
`q(z)=sum_k gamma_k z^k`.
In a Mid block, the rows of its third slice are the coefficient vectors
of `q(z),z q(z),...,z^(a-1)q(z)`. They are independent, so every
nonzero third slice has rank `a`.

In an `Out(u,v)` block, its columns are the coefficient vectors of
`q(z),z q(z),...,z^(u-1)q(z)`. They are independent, so every nonzero
third slice has rank `u`. These ranks persist after any invertible
first identification.

Thus the relevant minimum ranks are 5 for Mid, 3 for `Out(3,3)`, and
4 for `Out(4,2)`. None has a nonzero rank-one third slice.

For the target, the decomposition `B=direct sum B_j` gives
`R_T=direct sum R_(T_j)` inside `A tensor (direct sum B_j)`.
If `a tensor b` belongs to this space, its projection to each summand is
`a tensor b_j`. Whenever `b_j` is nonzero, it is a rank-one third slice
of that block. Hence only Full blocks can occur. The converse follows by
using a rank-one slice of one Full block alone. We have proved

\[
\pi_A(Z_T)=\bigcup_{j\text{ a Full block}}g_j\Gamma.
\tag{7}
\]

There are at most 17 distinct curves in this finite union. Each is a
smooth rational normal quartic, of Hilbert polynomial `4n+1`.

The source supplies a rank-one slice over every point of `Gamma`: in
one source block, the third covector with coefficients
`s^13,s^12 t,...,t^13` produces the product of the length-5 and
length-10 evaluation vectors. We will only need this inclusion, not a
classification of the source's full rank-one locus.

## 3. Proper incidence forces a smooth curve limit

Suppose a degeneration exists. After allowing a finite change of parameter,
write `R=C[[t]]`, `K=C((t))`, and

\[
U(t)=(a(t)\otimes b(t)\otimes c(t))S\in
(A\otimes B\otimes C)\otimes R,
\qquad U(0)=T,
\tag{8}
\]

where all three maps are invertible over `K`. Their entries may have poles.
There is no assumption that the first map has a nonsingular leading term.

Third conciseness of `T` means that `U_C(t)` has a 140-by-140 minor that
is a unit of `R`. Its image therefore is a rank-140 direct summand

\[
\mathcal R\subset(A\otimes B)\otimes R.
\tag{9}
\]

Its special fiber is `R_T`, and its generic fiber is
`(a(t) tensor b(t))R_S`, because `c(t)` is invertible over `K`.

Define the closed relative incidence

\[
\mathcal Z=\{([u],[v]):u\otimes v\in\mathcal R\}
\subset\mathbb P(A)_R\times_R\mathbb P(B)_R.
\tag{10}
\]

It is closed because the tautological product line maps to zero in the
locally free quotient by `mathcal R`. Its first projection is projective,
and hence has closed image. Projective properness and the closed-image
property are the standard facts in Stacks tags
[01WC](https://stacks.math.columbia.edu/tag/01WC) and
[01W0](https://stacks.math.columbia.edu/tag/01W0).

The generic image contains the entire curve

\[
\Gamma_K'=a(t)\Gamma_K.
\]

Let `mathcal Gamma` be its flat projective closure, and let `Gamma_0`
be the special fiber. This flat closure can be constructed by intersecting
the generic homogeneous ideal with `R[x_0,...,x_4]`. The quotient is
torsion free over `R`, so it is flat; each finite graded piece is free.
Its special fiber has the same Hilbert polynomial `4n+1`.
The flatness implication is Stacks
[0539](https://stacks.math.columbia.edu/tag/0539); finite freeness is
[0AUW](https://stacks.math.columbia.edu/tag/0AUW).

Equivalently, `mathcal Gamma` is the family obtained by extending the
generic point to the projective Hilbert scheme of polynomial `4n+1`.
This parameter space is the standard Hilbert-scheme construction of
Grothendieck, Theorem 3.2 and its Hilbert specialization after Proposition
3.8 in [Bourbaki Expose 221](https://www.numdam.org/item/SB_1960-1961__6__249_0.pdf).

Because the image of (10) is closed and contains `Gamma_K'`, it contains
the support of its closure, including the support of `Gamma_0`.
Taking the special fiber and using (7) gives

\[
|\Gamma_0|\subseteq\bigcup_j g_j\Gamma.
\tag{11}
\]

This uses properness of the rank-one incidence, not flatness of its
projection. No claim that formation of a scheme-theoretic image commutes
with specialization is needed.

### Degree and Hilbert polynomial eliminate every singular alternative

The polynomial `4n+1` implies that `Gamma_0` is one-dimensional and has
degree four. Every one-dimensional irreducible component of its support
lies in one curve of the finite union (11). It must equal that curve,
because a proper closed subset of an irreducible curve is zero-dimensional.
Each possible component has degree four. Additivity of the leading
Hilbert coefficient with its positive generic multiplicities implies
that exactly one such component occurs, with multiplicity one.
Call it `Gamma'`.

There is a surjection of structure sheaves

\[
\mathcal O_{\Gamma_0}\longrightarrow\mathcal O_{\Gamma'}.
\]

Its kernel has finite support: the two sheaves agree at the generic
point of the unique curve. This kernel accounts for any embedded
nilpotents and any isolated points. Both structure sheaves have Hilbert
polynomial `4n+1`, so its Hilbert polynomial is zero. A sheaf with finite
support has constant Hilbert polynomial equal to its nonnegative length;
it follows that the kernel is zero. Therefore

\[
\Gamma_0=\Gamma'=g_j\Gamma
\quad\text{as schemes, for some Full block }j.
\tag{12}
\]

In particular the flat curve limit is a smooth rational normal quartic.

## 4. Normalize the first map by the source's binary-form symmetry

Let `G=PGL(A)`, and let `H` be the stabilizer of `Gamma`.
Restriction to the curve identifies `H` with `PGL(2)` acting by the
degree-four Veronese representation. Indeed, an automorphism of
`Gamma` is an automorphism of `P^1`; it acts on the complete degree-four
linear system. Conversely, an ambient projective transformation that
is the identity on `Gamma` is the identity, since five curve points
span `P(A)` and a sixth completes a projective frame.

The orbit `O=G/H` is the locally closed orbit of `Gamma` in its Hilbert
scheme. Its orbit map `G -> O` is smooth and surjective. For these
standard orbit statements and the smoothness implication from smooth
stabilizer, see Milne, *Algebraic Groups* (2017), Propositions 7.4,
7.12, 7.15, and 7.17 in the [author's book](https://www.jmilne.org/math/Books/iAG2017.pdf).
Proposition 7.17 supplies existence of the quotient and its immersion
into the Hilbert scheme.
Here `H=PGL(2)` is smooth over `C`.

By (12), both fibers of the arc classifying `mathcal Gamma` lie in `O`.
The arc therefore factors through `O`. To spell out the scheme issue,
an open subset of the Hilbert scheme in which `O` is closed contains
both points of `Spec R`; the ideal of that closed orbit pulls back to
zero because it is zero over `K` and `R` is a domain.

Choose a constant projective transformation carrying `Gamma` to
`Gamma'`. Smoothness of the orbit map lifts this point successively
over `R/(t^n)` to a compatible lift of the whole arc. This is the
infinitesimal lifting criterion in Stacks
[02H6](https://stacks.math.columbia.edu/tag/02H6).
Taking the inverse limit in an affine neighborhood produces a lift
`h(t)` over `R`. Since every line bundle over the local ring `R` is
trivial, choose a matrix representative

\[
h(t)\in\operatorname{GL}(A,R),\qquad
h(t)\Gamma= a(t)\Gamma\quad\text{over }K.
\tag{13}
\]

Thus `r(t)=h(t)^(-1)a(t)` belongs, projectively, to the stabilizer of
`Gamma` over `K`. Its projective action is induced by an invertible
linear substitution in two variables. Choose a lift in `GL(2,K)`;
any scalar discrepancy in `GL(A,K)` can be absorbed in a long factor.
One can also allow a finite field extension here without affecting
the degeneration argument.

### Why this stabilizer is absorbable on the long factors

The coefficient tensor (1) is the tensor of multiplication of binary
forms of degrees `a-1` and `b-1`. The same substitution in the two
variables acts covariantly on their product. Consequently, for any
representative `r` of a projective transformation preserving `Gamma`,
there are invertible maps `p_r,q_r` on the long factors such that

\[
(r\otimes p_r\otimes q_r)S=S.
\tag{14}
\]

This can also be checked without choosing binomial conventions. For
one Full block, its third slice space is spanned by the products
`v_4(s,t) tensor v_9(s,t)`. Apply the same projective substitution to
both evaluation vectors. Their span is preserved, and the third
flattening is an isomorphism onto this span. It supplies the unique
compensating invertible map of the third factor. Use that same pair
of long actions on all ten source copies. A scalar multiplying `r`
is compensated by the inverse scalar on one long factor.

More explicitly, define `R_d(k)` by

\[
R_d(k)v_d(s,t)=v_d(k(s,t)),\qquad
v_d(s,t)=(s^d,s^{d-1}t,\ldots,t^d)^{\mathsf T}.
\]

Let `Delta:C* -> A tensor B` be the third flattening of one source
block. The coefficient convention (1) gives
`Delta v_13=v_4 tensor v_9`. Evaluation vectors span each coefficient
space, so the polynomial identity implies

\[
(R_4(k)\otimes R_9(k))\Delta=\Delta R_{13}(k),
\qquad
(R_4(k)\otimes R_9(k)\otimes R_{13}(k)^{-\mathsf T})
\operatorname{Full}(5,10)=\operatorname{Full}(5,10).
\tag{14a}
\]

If `r=lambda R_4(k)`, take `p_r` to be ten copies of `R_9(k)` and
`q_r` to be ten copies of `lambda^(-1)R_13(k)^(-T)`.
This gives (14) with the literal basis, including its scalar and dual
conventions. It requires no choice of a fourth root of `lambda`.

Substitute `a=h r` and (14) into (8). The identical tensor family is

\[
U(t)=\bigl(h(t)\otimes b(t)p_r(t)^{-1}
\otimes c(t)q_r(t)^{-1}\bigr)S.
\tag{15}
\]

The new first map is regular with invertible constant term. The new
long maps may have arbitrary poles, which are permitted. This proves
the required normalization; it was not a choice assumed at the start.

## 5. The catalecticant contradiction

For `U=sum_i a_i tensor U_i`, define

\[
H(U)=(U_{r+s})_{0\le r,s\le2}:
\mathbb C^3\otimes B^*\longrightarrow\mathbb C^3\otimes C.
\tag{16}
\]

The companion
[catalecticant proof](catalecticant_chart.md)
establishes

\[
\operatorname{rank}H(S)=120,
\qquad \operatorname{rank}H(gT)\ge130
\quad(g\in\operatorname{GL}(A)).
\tag{17}
\]

For clarity, these inequalities do not assert that `H` rank is invariant
under the first general linear group. Their inputs are the following
universal block bounds, valid after every independent first identification.

| Block | Copies | Lower bound per block | Contribution |
| --- | ---: | ---: | ---: |
| Full(5,2) | 7 | 4 | 28 |
| Full(5,3) | 10 | 5 | 50 |
| Out(3,3) | 4 | 5 | 20 |
| Out(4,2) | 2 | 4 | 8 |
| Mid(5,2) | 6 | 4 | 24 |
| Total | | | 130 |

For Full, the map (16) has no nonzero decomposable kernel, so the
Segre dimension bound gives rank at least `b+2`; Mid follows by
transposition. For Out, a nonzero vector in the three-dimensional
auxiliary space gives a map `A -> C^3` with two-dimensional kernel.
The image obtained by fixing a nonzero third covector in an `Out(u,v)`
block has dimension `u>=3`, so the transposed catalecticant has no
nonzero decomposable kernel. Its rank is at least `v+2`.
For a canonical Full block, (16) has rank exactly `b+2`; the ten
source blocks therefore contribute `10(10+2)=120`.

Set `b'=b p_r^(-1)` and `c'=c q_r^(-1)`. Equation (15) and the regular
inverse of `h(t)` give the regular family

\[
Q(t)=(I\otimes b'(t)\otimes c'(t))S
=(h(t)^{-1}\otimes I\otimes I)U(t),
\quad Q(0)=h(0)^{-1}T.
\tag{18}
\]

On the generic fiber, long-factor covariance of `H` implies
`rank H(Q(t))<=120`. Thus every minor of size 121 vanishes identically.
Since `Q(t)` is regular, its special fiber has `H` rank at most 120.
But `h(0)` is invertible, and the target bound in (17) gives rank at
least 130. This contradiction proves the theorem.

## 6. Orbit closure, limitations, and verification boundary

The Laurent formulation covers the orbit-closure formulation over `C`.
One may take a curve through a proposed boundary point with its generic
point in the orbit, normalize it, and complete at that point. A generic
lift to the general linear group exists after a finite field extension:
the nonempty fiber of the orbit map has a closed point over a finite
extension. A finite extension of `C((t))` is another complex Laurent
series field after a change of parameter. The preceding proof permits
that change and yields the same contradiction.

The argument specifically requires a target whose rank-one third-slice
first projection is contained in a finite union of smooth quartic
rational normal curves. If this projection contains lower-degree
curves or a higher-dimensional component, the degree-four flat limit
may be singular or nonreduced, and Section 3 does not apply. A target
Full block of width one would give all of `P(A)` and break this
hypothesis. Loss of third conciseness also breaks the subbundle argument.

The calculation reports already associated with the frozen candidate
and catalecticant package verify its literal coefficient conventions,
third-flattening rank 140, and the rank totals 120 and 130. They do not
verify the arbitrary-arc normalization. That step is the written
geometric argument in Sections 2–4, with its imported properness,
Hilbert parameter-space, homogeneous-orbit, and smooth-lifting facts
listed explicitly above. No numerical search is used as a substitute
for that argument.

All prior checkpoints should remain unchanged. The earlier candidate
screens are still correct as statements about those particular tests;
the present result supplies a different obstruction to the proposed
degeneration. The cactus-rank result remains valid and, by itself,
still does not determine border rank.


## 7. Exact convention controls

Run from the repository root:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_global_rnc.py
python -m unittest discover -s tests -p 'test_mixed_global_rnc.py' -v
```

The standard-library verifier checks shear, swap, diagonal and mixed binary
substitutions in the literal coefficient bases. Its 8,400 exact rational
coefficient equalities include the inverse-transpose third action and a
nontrivial scalar compensation. It also checks 15 rank-one Hankel slices,
six noncurve Full slices, 42 nonzero Mid/Out slices, all six relevant
third-flattening ranks, and a width-one boundary example.

These checks protect coefficient and dual conventions. They do not verify
properness, formal lifting, or the arbitrary-arc theorem. The proof of
those steps is above, with imported geometric ingredients recorded in
[global_rnc_sources.json](global_rnc_sources.json). The derivative history
and frozen hashes are in
[global_rnc_integration.md](global_rnc_integration.md) and
[global_rnc_manifest.json](global_rnc_manifest.json).
