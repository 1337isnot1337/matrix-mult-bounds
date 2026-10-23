# An explicit curvilinear smoothing and the missing Krylov condition

October 20, 2026. AI-derived written construction, externally unreviewed.
The algebra smoothing below is explicit. The extra functional condition
needed for a convolution-source tensor degeneration is **not constructed**.
No matrix multiplication exponent improvement follows from this note.

## 1. A rational smoothing with no existence theorem required

Put `D=m-1`, `N=m(m+1)/2`, and work in the curvilinear algebra

\[
C_N=\mathbb Q[t]/(t^N).
\]

Let

\[
f(t)=t,\qquad g(t)=\sum_{k=1}^{N-1}\frac{t^k}{k!}.
\]

**Proposition.** The `N` elements

\[
b_{a,b}=f(t)^a g(t)^b,\qquad a+b\le D, \tag{1}
\]

form a rational basis of `C_N`.

Here and below exponential notation refers only to its truncated formal
power series, so the construction involves rational numbers exclusively.
To prove the proposition, the binomial expansion changes (1) by an invertible
triangular matrix into the family

\[
t^a\exp(bt),\qquad 0\le b\le D,\quad 0\le a\le D-b.
\]

These functions are a fundamental solution set of the constant-coefficient
differential equation

\[
\prod_{b=0}^{D}(\partial_t-b)^{D-b+1}F=0, \tag{2}
\]

whose order is `N`. Their independence follows by successively applying
the factors in (2) to isolate a nonzero polynomial times one exponential.
A solution whose first `N` Taylor coefficients vanish is identically zero,
by the coefficient recurrence of the monic order-`N` equation. Thus their
`N`-jet matrix is invertible. This is also the usual confluent Vandermonde
argument, supplied here to fix its characteristic-zero hypotheses.

Write multiplication in the basis (1) as

\[
b_\alpha b_\beta=\sum_\gamma c_{\alpha\beta}^{\gamma}b_\gamma.
\]

On the vector space with basis `e_(a,b)`, transport this multiplication
through `e_(a,b) -> epsilon^(a+b)b_(a,b)`. The structure constants become

\[
\mu_\epsilon(e_\alpha,e_\beta)
=\sum_\gamma c_{\alpha\beta}^{\gamma}
 \epsilon^{|\alpha|+|\beta|-|\gamma|}e_\gamma. \tag{3}
\]

If `|alpha|+|beta|<=D`, the product is exactly the corresponding basis
element, so its coefficient has exponent zero. Otherwise every exponent
in (3) is positive, because `|gamma|<=D`. Thus (3) is a polynomial family
of associative unital algebras, with generic fiber `C_N` and special fiber

\[
B_m=\mathbb Q[x,y]/(x,y)^m. \tag{4}
\]

This proves the required algebra-level smoothing directly. It does not
choose the short shared leg of a convolution tensor.

The determinant of the scaling part has valuation

\[
\sum_{d=0}^{D}d(d+1)=\frac{m(m^2-1)}3.
\]

The classical density of the curvilinear stratum motivates this question.
The author version of Bayer, Chen and Jiang, *Brill--Noether theory of
Hilbert schemes of points on surfaces*, Example 2.5 and Remark 2.6,
[pages 3--4](https://webhomes.maths.ed.ac.uk/~abayer/Hilbn-Brill-Noether.pdf),
states it for the punctual Hilbert scheme of `k[[x,y]]` and cites Briancon,
Theorem V.3.2 and Corollary V.3.3, and Iarrobino, Section 5. Briancon's
original publication is
[Inventiones 41 (1977), 45--89](https://doi.org/10.1007/BF01390164).
The proof of (1)--(4) does not depend on that external density theorem.

## 2. The exact additional condition for this algebra route

Let `A` be a free rank-`N` algebra over `Q[[epsilon]]`, with special fiber
`B_m` and generic fiber a curvilinear algebra. The construction above is
one explicit choice. Write `W_0` for the `m`-dimensional subspace of
`B_m^*` consisting of the homogeneous degree-`D` coefficient functionals.
The tensor obtained by evaluating multiplication against this subspace
is exactly `T_m`.

The following is a **sufficient condition**, not a statement supplied by
curvilinear smoothability:

1. Choose a generator `tau_epsilon` of the generic algebra, so its first
   `N` powers form a basis, and a functional `ell_epsilon` for which
   `(a,b) -> ell_epsilon(ab)` is nondegenerate.
2. Form the rank-`m` Krylov subspace of its dual module

   \[
   W_\epsilon=\operatorname{span}\{
   \ell_\epsilon,\tau_\epsilon^*\ell_\epsilon,\ldots,
   (\tau_\epsilon^*)^D\ell_\epsilon\},\qquad
   (\tau^*\ell)(a)=\ell(\tau a). \tag{5}
   \]

3. Require that its saturated limit inside `A^*` is exactly `W_0`.
   Equivalently, after a possibly singular change of the `m` shared basis
   vectors, it must admit a regular basis converging to the degree-`D`
   coefficient functionals.

If these conditions hold, they give an explicit `C(m,N)` degeneration to
`T_m`. Indeed, in the basis `1,tau,...,tau^(N-1)`, the two nonshared maps
send a target input `a` to its coefficient vector and a target input `b`
to the functional vector

\[
(\ell(b),\ell(\tau b),\ldots,\ell(\tau^{N+D-1}b)).
\]

The shared slice with index `i` evaluates `ell(tau^i ab)`, exactly as in
`C(m,N)`. The regular basis of (5), together with the regular multiplication
of `A`, makes the limiting tensor `T_m`. Laurent coefficients in these
maps are allowed. This proves the implication from the stated condition;
it does not prove that such a generator and functional exist.

For this algebra-compatible realization, (5) is precisely the requirement
that the chosen functionals form a consecutive moment window. General
convolution degenerations need not arise from this same algebra-compatible
construction, so failure of this route would not exclude them.

## 3. A finite exact form of the missing condition

In any regular basis of `A`, form the `N`-by-`m` matrix `K(epsilon)` whose
columns are the functionals in (5). Clear a common Laurent power from its
Pluecker vector. The condition in Section 2 is equivalent to requiring
that the resulting leading exterior product be a nonzero multiple of
the wedge of the `m` degree-`D` coordinate functionals.

Thus a proposed explicit smoothing, generator and functional can be tested
by exact valuations of maximal minors. At `m=4,N=10` there are only
`binom(10,4)=210` such minors. The desired top-degree minor must attain the
strictly smallest valuation, and all other minors must have larger valuation.
This is a concrete acceptance condition for a supplied Laurent candidate.
No candidate meeting it is supplied here.

One necessary diagnostic follows without computing all minors. Let `L_0`
be the subspace of elements of degree at most `D-1`, of codimension `m`.
If a regular, nonconstant limiting generator `tau_0` exists, the Krylov
prefix condition forces the boundary map

\[
L_0\longrightarrow B_m/L_0,\qquad a\longmapsto\tau_0a\bmod L_0
\]

to have rank at most one. The reason is that the annihilator of (5), in a
Frobenius coordinate, is a unit multiple of a consecutive polynomial
prefix, whose span grows by at most one under multiplication by `tau`.
More explicitly, subtract the scalar part of the generic generator, which
does not change its Krylov span, and write
`ell(a)=coeff_(tau^(N-1))(u a)` for a unit `u`. The annihilator is then
`u^(-1)span(1,tau,...,tau^(N-m-1))`. This rank inequality survives a regular
limit of the generator and the saturated annihilator subspace.

Subtract the scalar part of `tau_0`, and let its first nonzero homogeneous
part have degree `e`. Multiplication of this part by all degree-`D-e`
binary forms has rank `D-e+1`, since a nonzero polynomial is not a zero
divisor before truncation in degree `D`. Therefore `e>=D`. Such a regular
nonconstant limiting generator must lie in the socle. Generators with
poles, or further valuation cancellations, remain possible and are exactly
the cases that need investigation.

## 4. Why this algebra-compatible method is too restrictive at m=3

There is a useful small calibration. Let `C=K[t]/(t^6)`, and suppose
`1,x,y,x^2,xy,y^2` is a basis. Its degree-below-two subspace is
`L=span(1,x,y)`. It cannot be the annihilator of a fixed three-term
Frobenius Krylov window.

To see this, take a generator coordinate `tau`. Every Frobenius functional
has the form `ell(a)=coeff_(tau^5)(u a)` for a unit `u`. The annihilator of
`ell,tau^*ell,(tau^*)^2ell` is then `u^(-1)span(1,tau,tau^2)`.
If it equalled `L`, the three polynomials `u,ux,uy` would all have degree
at most two. Their six pairwise products lie in the five-dimensional
space of polynomials of degree at most four. Multiplication by the unit
`u^2` would give a dependence among `1,x,y,x^2,xy,y^2`, a contradiction.

The repository already has an actual `C(3,6)` degeneration to `T_3`.
There is no contradiction: the fixed algebra-compatible window is a
stricter method.

In fact, the same obstruction excludes **varying** algebra-compatible
windows at length six. In every generic fiber their annihilator `L_epsilon`
satisfies

\[
\dim\operatorname{span}(L_\epsilon L_\epsilon)\le5,
\]

because it is a unit multiple of a three-term polynomial prefix. The
multiplication map is regular in an algebra smoothing. After taking the
saturated limit of `L_epsilon`, the rank of its square cannot increase.
But `span(L_0L_0)=B_3` has dimension six. Thus the sufficient method in
Section 2 cannot capture the known `C(3,6)` tensor degeneration, even
with varying generators and shared normalization. A broader module model
with two independent nonshared maps is necessary to include that control.

## 5. Explicit dual coordinates and a rejected natural generator

The smoothing also gives exact coordinates for the desired functionals.
Define

\[
Q(z)=\prod_{b=0}^{D-1}(z-b)^{D-b},\qquad \deg Q=N-m.
\]

The functionals on `C_N` that annihilate every `b_(a,b)` of degree below
`D` are exactly

\[
a(t)\longmapsto[p(\partial_t)a(t)]_{t=0},
\qquad p(z)\in Q(z)\operatorname{span}(1,z,\ldots,z^D). \tag{6}
\]

Indeed, the same triangular binomial transformation as before identifies
the lower-degree span with
`t^a exp(bt)`, where `0<=b<=D-1` and `0<=a<=D-1-b`.
Evaluation gives

\[
[p(\partial_t)(t^a\exp(bt))]_{t=0}=p^{(a)}(b),
\]

so precisely the root multiplicities in `Q` are required. The dimensions
then give equality. Formula (6) is a convenient exact representation of
the target dual space. It is **not** already a convolution moment window:
multiplication by `t` on the dual sends `p(z)` to `p'(z)`, whereas the
displayed basis changes by multiplication by `z`.

A natural unit generator is

\[
\tau(t)=\frac{\exp(t)-1}{t}
 =1+\frac t2+\frac{t^2}{6}+\cdots \pmod {t^N}.
\]

Its linear coefficient is nonzero, so it generates `C_N`. Set `ell` to
be the coefficient functional dual to `g^D` in the basis (1). For `a>=i`,

\[
\tau^i b_{a,b}=b_{a-i,b+i},
\]

which gives the desired homogeneous shift in the interior. However, the
cases `a<i` introduce extra terms. The exact verifier records these
boundary contributions for every size `m=2,...,6`. At `m=4`, the matrix
of moments `ell(tau^i b_(a,b))` on the six lower-degree inputs has rank
three, and its entry on input `1`, moment `i=1`, is
`-19/1632960`. Therefore this constant generator and functional do not
supply the required window. This rejection does not cover Laurent
deformations of the generator, functional, or the two independent maps.

## 6. Verification and next construction target

`verify_smoothing.py` checks the rational basis matrices, expands every
ordered pair product in that basis, and checks the complete special-fiber
multiplication table for the selected sizes. It exports the exact `m=4`
basis and inverse, the exact functionals (6), and the rejected ratio
candidate. These are certificates for the algebra smoothing and the
stated finite controls only. The run at `m=2,...,6` checks 811 ordered pair
products and 13,879 transported structure coefficients, as well as 265
dual-space coefficients and 125 interior ratio identities. Its report is
`results/singular-shared-normalization-2026-10-20/smoothing.json`.

The next target is a Laurent generator and functional satisfying (5), or
its version with an ambient cyclic algebra of length `B=N+O(m)` and an
`N`-dimensional target subspace. Additional ambient dimensions could absorb
the boundary terms without changing the asymptotic source ratio. The
`m=3` obstruction also motivates allowing two independent nonshared maps,
without requiring them to come from the same algebra multiplication.
No such extension is currently constructed.
