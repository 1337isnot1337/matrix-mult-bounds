# Retaining a full smaller convolution tensor beside M8

October 21, 2026. Exact rational construction, with every output
coefficient checked by integer arithmetic. No improved matrix
multiplication exponent is claimed.

\[
A(5,6)\longrightarrow M_8\oplus A(2,3).
\tag{1}
\]

The target has common leg dimension 64+24=88. It has 512 matrix-block
terms and 216 terms in the residual convolution tensor, for a total of
728. This retains the whole residual tensor that was compressed to M4
in [`parity_structure_a56.md`](parity_structure_a56.md).

## The two local slices

Keep that construction's bases

\[
U=(1,x^4),\quad V=(x-x^4,x^2,x^3,1+x^5),
\]

the eight dual product functionals R, and

\[
h_0=-e_0+e_5+e_8,\qquad h_1=-e_1-e_4+e_9.
\]

The functionals h annihilate U times V. On the remaining first short
space P_old=(x,x^2,x^3), their two pairing matrices against V are

\[
D_0=\begin{pmatrix}-1&0&0&0\\0&0&1&0\\0&1&0&1\end{pmatrix},
\qquad
D_1=\begin{pmatrix}0&0&-1&-1\\0&-1&0&0\\-1&0&0&0\end{pmatrix}.
\]

Set

\[
\begin{aligned}
P_0&=(x+x^2-x^3)/2,\\
P_1&=(-x-x^2-x^3)/2,\\
P_2&=(-x+x^2+x^3)/2,
\end{aligned}
\qquad
\begin{aligned}
Q_0&=x^3-1-x^5,\\
Q_1&=x-x^2-x^4,\\
Q_2&=x+x^3-x^4,\\
Q_3&=1-x^2+x^5.
\end{aligned}
\tag{2}
\]

Every Q is in span(V), and exact multiplication gives

\[
h_\lambda(P_\mu Q_\nu)
=\begin{cases}1,&\nu=\mu+\lambda,\\0,&\text{otherwise},\end{cases}
\quad 0\le\mu<3,\ 0\le\lambda<2,\ 0\le\nu<4.
\tag{3}
\]

This is the coefficient tensor for multiplying a polynomial of degree
below three by one of degree below two.

For an additional direct verification of the basis change, put

\[
Q_{\rm mix}=\begin{pmatrix}
0&0&1&-1\\1&-1&0&0\\1&0&1&0\\0&-1&0&1
\end{pmatrix},
\qquad
L=\frac12\begin{pmatrix}1&1&-1\\-1&-1&-1\\-1&1&1\end{pmatrix}.
\]

Then Q=Q_mix V and P=L P_old, with

\[
LD_0Q_{\rm mix}^{\mathsf T}=(I_3\ \ 0),\qquad
LD_1Q_{\rm mix}^{\mathsf T}=(0\ \ I_3).
\]

## Cyclic maps and the residual source convention

Label A(2,3) coordinates in the same lexicographic convention used for
every A(a,b) in this package:

\[
X'=(i,t,s)\in[2]\times[4]\times[3],\quad
Y'=(j,p,u)\in[3]\times[2]\times[4],\quad
Z'=(v,q,r)\in[4]\times[3]\times[2].
\]

The corresponding rows on the original A(5,6) source are

\[
\begin{aligned}
X'_{i,t,s}(I,T,S)&=P_s(I)h_i(T)Q_t(S),\\
Y'_{j,p,u}(J,P,U)&=Q_u(J)P_j(P)h_p(U),\\
Z'_{v,q,r}(V,Q,R)&=h_r(V)Q_v(Q)P_q(R).
\end{aligned}
\tag{4}
\]

The three local pairings (3) impose exactly t=p+q, u=r+s, and v=i+j.
Their coefficients are one, so (4) produces A(2,3) with the stated
orientation. Stacking these rows after the original M8 rows gives (1).

The mixed coefficients vanish for the same reason as in the M8 plus M4
construction. With one residual row, its long h pairs core U and V.
With two residual rows, one h pairs a core U with a residual Q, and
Q belongs to span(V). These factors vanish in every cyclic placement.

## Exact representation and replay

The three rational maps have shape (88,300). The first 64 rows are the
integral M8 maps. Every entry of the remaining 24 rows is 0, 1/2, or
-1/2. The saved numerator maps multiply those residual rows by two.
They have 768 nonzero entries each, all 1 or -1.

Applying the numerator maps to the 27,000 original source terms gives
M8 plus 8 times A(2,3), with all mixed coefficients exactly zero. The
verifier checks each resulting coefficient against the product of
its three row denominators. This verifies the rational maps without
floating-point arithmetic.

Files:

- `parity_structure_residual.py`: explicit bases, maps, and integer replay.
- `parity_structure_residual_certificate.json`: dimensions and exact checks.
- `parity_structure_residual_maps.npz`: A,B,C and x,y,z map arrays, exact integer numerator arrays, row denominators, and the local bases.

Run from the repository root:

```
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_residual.py
```

The NPZ A,B,C arrays use the exactly representable binary fractions
0 and plus or minus 1/2 on the residual rows. The separate numerator
arrays and integer denominator vector define the exact certificate.
