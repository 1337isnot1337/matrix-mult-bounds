# Simple poles in the fixed A22 compression chart

October 21, 2026. This note proves a restriction on Laurent families in
one explicit compression chart. It does not exclude arbitrary A22
degenerations or produce a smaller exponent.

## 1. The chart and its exact trace defect

Use the physical basis P in `parity_balancing_spin1.md`. All W(A22)
matrices whose top 3-by-3 block is A have the form

\[
J_u(A)=\begin{pmatrix}
A&u(A)\\
\ell(A)+u(A)^TQ&\operatorname{tr}A
\end{pmatrix},\qquad
Q=\begin{pmatrix}0&0&1/2\\0&1&0\\1/2&0&0\end{pmatrix},
\]

where u:Mat3 to C3 is arbitrary and

\[
\ell\!\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}
=(d-h/2,-a+i,b/2-f).
\]

Indeed, the kernel of the top-block map consists of
[[0,v],[v^T Q,0]], a three-dimensional space. This is the chart used in
`parity_balancing_compression.py`; it allows both off-diagonal blocks.

There can be different maps u_0,u_1,u_2 on the three legs. Write
t(A)=tr(A). Direct block multiplication gives

\[
\operatorname{tr}(J_{u_0}(A)J_{u_1}(B)J_{u_2}(C))
-\operatorname{tr}(ABC)
=t(A)t(B)t(C)+L(u)+\mathcal Q(u),\tag{1}
\]

where

\[
L(u)=\sum_{\rm cyc}\ell(A)\bigl(Bu_2(C)+t(C)u_1(B)\bigr),\tag{2}
\]

and

\[
\mathcal Q(u)=\sum_{\rm cyc}
u_0(A)^TQ\bigl(B+t(B)I\bigr)u_2(C).\tag{3}
\]

The cyclic sum simultaneously rotates (A,B,C) and the map indices.
Only the quadratic terms can be grouped as in (3), using symmetry of
Q. Grouping the linear terms with the same scalar factors would give
an incorrect formula. The verifier checks (1)-(3) on every trilinear
coefficient for three distinct integer parameter maps.

## 2. Statement

There is no family in this fixed chart of the form

\[
u_i(\epsilon)=\epsilon^{-1}f_i+g_i+O(\epsilon),\tag{4}
\]

with at least one f_i nonzero, whose contracted trace tensor has a
finite coefficientwise limit. In particular, no such family gives M3
as a limit.

The same proof applies to a single negative order epsilon^(-d) with
no other negative powers. Families with several negative orders,
families with moving physical bases, and arbitrary source maps are
outside this statement.

To prove it, let
\(B_f(g)=\mathcal Q(f+g)-\mathcal Q(f)-\mathcal Q(g)\).
A finite limit in (4) would require

\[
\mathcal Q(f)=0,\qquad B_f(g)+L(f)=0.\tag{5}
\]

We show these two equations cannot hold when f is nonzero.

## 3. Classifying the nonzero leading quadratic directions

Set r_i=rank(f_i) and U_i=image(f_i). If A is in ker(f_0), then
equation Q(f)=0 reduces to

\[
f_2(C)^TQ(A+t(A)I)f_1(B)=0.
\]

The linear map A to A+t(A)I is invertible on Mat3: it is the identity
on traceless matrices and multiplication by four on the scalar line.
Consequently the space of functionals

\[
A\longmapsto v^TQ(A+t(A)I)w,
\qquad v\in U_2,\ w\in U_1,
\]

has dimension r_1 r_2. Every such functional vanishes on ker(f_0),
so

\[
r_1r_2\le r_0,
\quad r_2r_0\le r_1,
\quad r_0r_1\le r_2.\tag{6}
\]

If all r_i are positive, multiplication yields r_0 r_1 r_2<=1, so
all three equal one. Exactly two positive ranks are impossible by
(6). Thus a nonzero quadratic direction has either one nonzero map
of arbitrary rank, or three maps of rank one.

In the latter case write f_i(A)=alpha_i(A)w_i with w_i nonzero, and
put

\[
\beta_{jk}(A)=w_j^TQ(A+t(A)I)w_k.
\]

All beta_jk are nonzero because the displayed map on Mat3 is
invertible. Dividing Q(f)=0 on the open set where the alpha_i do not
vanish gives a sum of one rational function of A, one of B, and one
of C equal to zero. Each function is therefore constant. Equivalently,
there are nonzero c_i such that

\[
f_0(A)=c_0\beta_{21}(A)w_0,\quad
f_1(B)=c_1\beta_{02}(B)w_1,\quad
f_2(C)=c_2\beta_{10}(C)w_2,
\tag{7}
\]

with c_0 c_1+c_1 c_2+c_2 c_0=0. Conversely these formulas do make
Q(f) identically zero.

## 4. A two-matrix obstruction for every nonzero vector

For every nonzero w in C3 there exist matrices A,B such that

\[
w^TQ(A+t(A)I)=0,\qquad (B+t(B)I)w=0,\tag{8}
\]

but

\[
E_w(A,B):=t(A)\ell(B)w-t(B)\ell(A)w\ne0.\tag{9}
\]

There are two normal forms. For the isotropic vector w=e_0, take

\[
A=\operatorname{diag}(2,0,-1),\qquad B=E_{21}.
\]

These satisfy (8), and E_w=-1/2. For the nonisotropic vector w=e_1,
take

\[
A=\operatorname{diag}(1,-1,1),\qquad
B=\operatorname{diag}(1,0,-1).
\]

Then (8) holds and E_w=-2. Matrix indices here are zero based.

For completeness, the covariance used to reduce to these normal
forms follows directly from the formula for ell. If
R^T Q R=Q and det R=1, then

\[
\ell(RAR^{-1})=\ell(A)R^{-1}.\tag{10}
\]

One way to see it is to write A^TQ-QA as the alternating form
\((v_1,v_2)\mapsto\det(v_1,v_2,z)\), where
z=(ell_3,ell_2/2,ell_1)^T and ell(A)^T=2Qz. Both the volume form
and Q are preserved by R, so z transforms to Rz and (10) follows.
Over C, the orthogonal Gram-Schmidt construction and an isotropic
pair completion show that, up to nonzero scaling, every nonzero
vector is taken to e_1 or e_0 by such an R. The orientation can be
adjusted in the complementary directions. Simultaneously conjugating
A and B transports (8)-(9), proving the assertion for every w.

## 5. Contradiction at the next Laurent order

First suppose only f_2 is nonzero. Choose C with w=f_2(C) nonzero,
and then choose A,B from (8)-(9). The two possible terms of B_f(g)
at this triple are

\[
g_0(A)^TQ(B+t(B)I)w
+w^TQ(A+t(A)I)g_1(B),
\]

and both vanish. The remaining linear term is

\[
L(f)(A,B,C)=\ell(A)Bw+t(A)\ell(B)w
=E_w(A,B)\ne0,
\]

contradicting (5). The other single-leg cases follow cyclically.

Now suppose all three leading maps have rank one and use (7).
Take w=w_2 and again choose A,B from (8)-(9). Formula (7) gives
f_0(A)=0 and f_1(B)=0 automatically. Choose C with beta_10(C)
nonzero. All terms of B_f(g) either contain one of those zero
leading values, or are the two terms just displayed multiplied by
c_2 beta_10(C). They vanish. On the other hand,

\[
L(f)(A,B,C)=c_2\beta_{10}(C)E_w(A,B)\ne0.
\]

This is the required contradiction in every case.

## 6. Controls and scope

The standard-library verifier `compression_simple_poles.py` checks
all 729 coefficients of the corrected defect formula, both normal
forms, transported normal forms under explicit rational Q-orthogonal
matrices, and complete quadratic cancellation for six distinct
rank-one leading families. It also checks the nonzero next-order
obstruction with unrelated constant maps g.

The mathematical proof is author checked and was checked by two other
agents in the generating session. There is no external independent
review or formalization. Discovery probes using exact rational
linear systems motivated the proof; their failure was not itself used
as a claim about all leading directions.

Run from the repository root:

```
python -S research/ai/2026-10-20-anisotropic-constructions/compression_simple_poles.py
```

No general degeneration exclusion or exponent improvement is claimed.
