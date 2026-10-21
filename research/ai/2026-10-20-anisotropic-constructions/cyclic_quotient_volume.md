# The volume of an exact cyclic physical quotient

October 21, 2026. This is a written algebraic proof with exact finite
controls. The proof was checked by two other agents in the generating
session. No external independent review, formalization, or priority
claim is made.

The statement concerns exact quotient equations in the physical trace
model of A(a,b). It allows three unrelated quotient spaces and arbitrary
linear lifts. It does not concern arbitrary restrictions, compression
maps with both off-diagonal blocks nonzero, or arbitrary degenerations.

## 1. Statement

Work over any field. Put q=ab and x=a+b-1, with a,b positive. The
physical matrix subspace for the cyclic convolution source is

\[
\mathcal W=\{W(F): W(F)_{(i,j),(p,s)}=F(i,p+j,s)\}
\subseteq\operatorname{End}(\mathbb F^a\otimes\mathbb F^b),
\]

where i,p range from 0 to a-1 and j,s from 0 to b-1. Its cyclic trace
tensor is A(a,b), in the coordinate orders in
`parity_balancing_spin1.md` and `parity_balancing_triangular.md`.

Let M_0,M_1,M_2 be nonzero vector spaces of dimensions m_0,m_1,m_2.
Suppose there are surjective maps

\[
\pi_t:\mathbb F^a\otimes\mathbb F^b\longrightarrow M_t
\]

such that, for every A in Hom(M_(t+1),M_t), there is J_t(A) in W with

\[
\pi_t J_t(A)=A\pi_{t+1}.\tag{1}
\]

Subscripts are cyclic. The lifts need not be assumed linear for the
necessary condition below. Then

\[
\boxed{m_0m_1m_2\le x^3.}\tag{2}
\]

In particular, an exact cyclic quotient with square target M_m has
m<=a+b-1. Over the rational numbers, the bound is attained by the triangular
construction at m=a+b-1. Its nonzero residual tensor remains a separate issue.

## 2. Short row supports

Write pi_(t,j):F^a to M_t for the jth column block of pi_t. Define

\[
R_t=\sum_{j=0}^{b-1}\operatorname{rowspace}(\pi_{t,j})
\subseteq(\mathbb F^a)^*,\qquad \rho_t=\dim R_t.
\]

Each rho_t is positive because pi_t is surjective onto a nonzero
space. For a fixed input block s, the corresponding block of pi_t W(F)
is the map F^a to M_t with pth column

\[
\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
\pi_t(e_i\otimes e_j)F(i,p+j,s).\tag{3}
\]

As F varies, these blocks form one space L_t contained in
Hom(F^a,M_t). The same space occurs for every s: the entries F(i,k,s)
are free, and the formula has no other dependence on s.

For each fixed long coordinate k, the vector (F(i,k,s))_i matters in
(3) only through its class in F^a/R_t^perp. Indeed, every row of every
pi_(t,j) lies in R_t. There are x long coordinates, so

\[
\dim L_t\le x\rho_t.\tag{4}
\]

This is a bound on the actual common block image, and does not require
a common basis for the three quotient spaces or any assumption that
their kernels agree.

## 3. All target left actions fill the required block space

For a fixed s, condition (1) implies

\[
\{A\pi_{t+1,s}:A\in\operatorname{Hom}(M_{t+1},M_t)\}
\subseteq L_t.
\]

The space on the left is precisely
M_t tensor rowspace(pi_(t+1,s)). To see equality, any linear map from
the image of pi_(t+1,s) into M_t extends to M_(t+1). Summing over s
inside the same space L_t gives

\[
M_t\otimes R_{t+1}\subseteq L_t.
\]

Combining this inclusion with (4) proves the three inequalities

\[
\boxed{m_t\rho_{t+1}\le x\rho_t.}\tag{5}
\]

Their product is (2), after cancelling the positive product of the
rho_t. In the square case one may also select an index with minimal
rho_t and read m<=x directly from its inequality.

## 4. Consequence for the finite exponent comparison

An exact quotient lift has a residual trace tensor on the three
kernels. Suppose, even more favorably, that this residual could be
cancelled at no cost. The matrix volume v=m_0m_1m_2 would still obey
v<=x^3. To improve the critical exponent 9/4 through this single matrix
target, the finite comparison requires

\[
216v>(3x+1)^4.\tag{6}
\]

For x>=3, however,

\[
\frac{216v}{(3x+1)^4}
\le\frac{216x^3}{(3x+1)^4}
\le\frac{216\cdot3^3}{10^4}
=\frac{729}{1250}<1.\tag{7}
\]

The middle expression decreases for x>1, since its logarithmic
derivative is 3(1-x)/(x(3x+1)). Thus free cancellation of an exact
quotient residual would still be insufficient in this particular
finite comparison. This sharpens the necessary dimension information
used in `quotient_score_barrier.md`; its more relaxed score calculation
remains valid as written.

For A(8,8), this says m<=15. It excludes an exact 27-vertex quotient
regardless of quotient bases or kernels. It does not exclude the
currently missing ordinary restriction A(8,8) to M27 direct sum M7,
which could use maps not satisfying (1).

The argument also applies over a field of rational or Laurent
functions, when (1) holds exactly there and all quotient dimensions
are fixed. It does not imply that an arbitrary singular family can be
put in this exact quotient form.

## 5. Exact finite controls

`cyclic_quotient_volume.py` uses only the Python standard library.
It checks the block formula against direct physical matrix
multiplication, computes short row supports, and checks the sharp
triangular projections in seven formats up to A(8,8). The latter
block images attain the upper bound a(a+b-1): a modular nonzero minor,
together with the proved rational upper bound, certifies their
rational ranks exactly. The prime used for these rank certificates
is recorded in the report.

Three coordinate quotient examples above the long dimension are
also checked over the rational numbers. They fail the common-block
inclusion, as predicted. These finite checks exercise the coordinate
directions and the sharpness examples; they are not a substitute for
the proof for arbitrary quotient maps.

Run from the repository root:

```
python -S research/ai/2026-10-20-anisotropic-constructions/cyclic_quotient_volume.py
```

No improved matrix multiplication exponent is claimed.
