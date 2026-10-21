# Three-shift formula for the A(2,b) residual

October 21, 2026. This is a simplification of the exact residual in
[the all-size triangular lift](parity_balancing_triangular.md), with
the correction retained. It is not a new exponent bound.

## Explicit formula

Let b>=2. In the notation of that construction, the quotient matrices
A have size b+1 and the kernel matrices K(A) have size b-1. Change
the kernel basis by the invertible anti-diagonal matrix

\[
T_{b-2-v,v}=(-1)^v\binom{b-2}{v},\qquad 0\le v\le b-2.
\]

Then \(\widehat K(A)=TK(A)T^{-1}\) satisfies

\[
\boxed{\quad
\widehat K(A)_{ij}=
\frac{(b-i)(b-i-1)}b A_{ij}
+\frac{2(i+1)(b-i-1)}b A_{i+1,j+1}
+\frac{(i+1)(i+2)}b A_{i+2,j+2},
\quad 0\le i,j\le b-2.
\quad}
\tag{1}
\]

Equivalently, the coefficient of \(A_{i+s,j+s}\) is

\[
(b-1)\frac{\binom{b-2}{i}\binom2s}{\binom b{i+s}},
\qquad s=0,1,2.
\tag{2}
\]

Thus the correction is explicitly
\(\operatorname{tr}(\widehat K(A)\widehat K(B)\widehat K(C))\).
It still requires an M_(b-1) source for the displayed cancellation.
For b=2, (1) reduces to the scalar \(\operatorname{tr}A\).

## Derivation from two-by-two binomial blocks

Write d=b-1, \(C_h=\binom dh\), taking binomial coefficients outside
0,...,d to be zero. For a fixed last coordinate s, the central block
of the defining equation \(\pi J(A)=A\pi\) is

\[
\begin{pmatrix}C_h&-C_{h+1}\\-C_{h-1}&C_h\end{pmatrix}
\begin{pmatrix}F_{0,h,s}\\F_{1,h+1,s}\end{pmatrix}
=(-1)^{s-h}C_s
\begin{pmatrix}A_{d-h,d-s}\\A_{d-h+1,d-s+1}\end{pmatrix},
\qquad 0\le h\le d.
\tag{3}
\]

Its determinant is

\[
\Delta_h=C_h^2-C_{h-1}C_{h+1}
=\frac{(d+1)C_h^2}{(h+1)(d-h+1)}>0.
\tag{4}
\]

In particular,

\[
F_{0,h,s}=
\frac{(-1)^{s-h}C_s}{\Delta_h}
\bigl(C_hA_{d-h,d-s}+C_{h+1}A_{d-h+1,d-s+1}\bigr).
\tag{5}
\]

The kernel basis from the all-size construction is

\[
Qe_v=\frac{d-v}{d}e_{0,v}+\frac{v+1}{d}e_{1,v+1}.
\]

Comparing row (0,q) in \(J(A)Q=QK(A)\) therefore gives

\[
K(A)_{qv}=\frac{d-v}{d-q}F_{0,q,v}
+\frac{v+1}{d-q}F_{0,q+1,v+1},
\qquad 0\le q,v\le d-1.
\tag{6}
\]

Put i=d-1-q and j=d-1-v. The change of basis multiplies (6) by
\((-1)^{q-v}\binom{d-1}{q}/\binom{d-1}{v}\). Its signs cancel
those in (5). Use

\[
(d-v)\binom dv=(v+1)\binom d{v+1}
=d\binom{d-1}{v}.
\]

The coefficients of the three remaining entries, in increasing
order of their shifts, are

\[
\frac{d\binom{d-1}{q}}{d-q}
\left(
\frac{C_{q+1}}{\Delta_{q+1}},\quad
\frac{C_q}{\Delta_q}+\frac{C_{q+2}}{\Delta_{q+1}},\quad
\frac{C_{q+1}}{\Delta_q}
\right).
\]

Substitution of (4) reduces them to (2), and hence (1). The indices
q and q+1 in this derivation range from 0 through d, so all boundary
cases are included without using an undefined binomial block.

## Two useful normalizations

Vandermonde's identity applied to (2) gives, for every A,

\[
\operatorname{tr}\widehat K(A)=(b-1)\operatorname{tr}A,
\qquad
\widehat K(I_{b+1})=(b+1)I_{b-1}.
\tag{7}
\]

There is also a three-term positive matrix representation over the
real numbers. Let \(D_m=\operatorname{diag}\sqrt{\binom m0},\ldots,
\sqrt{\binom mm}\), and set
\(A_o=D_b^{-1}AD_b\) and
\(K_o=D_{b-2}^{-1}\widehat K(A)D_{b-2}\). Define the
(b-1)-by-(b+1) matrices

\[
(L_s)_{i,i+s}=\sqrt{
\frac{\binom{b-2}{i}\binom2s}{\binom b{i+s}}},
\qquad s=0,1,2,
\]

with all other entries zero. Equation (2) implies directly that

\[
K_o=(b-1)\sum_{s=0}^2 L_s A_o L_s^{\mathsf T}.
\tag{8}
\]

This formula may help with structured cancellation searches. It does
not make the cubic correction vanish.

## Exact controls and scope

`parity_balancing_a2_residual.py` implements (1) with standard-library
rational arithmetic. Its optional comparison imports the separate
SymPy binomial-block generator. The saved report checks every target
matrix unit for b=2,3,4,5, including the complete quotient and kernel
identities from that generator. The proof above establishes (1) for
every b>=2; those finite checks verify the implementation.

The source identity remains

\[
A(2,b)\oplus M_{b-1}\longrightarrow M_{b+1}.
\]

Review status: author-checked derivation and exact finite replay in
this generating session; no external independent review or
formalization is claimed.
