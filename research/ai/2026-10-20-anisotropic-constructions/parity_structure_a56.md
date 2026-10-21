# Integral A(5,6) constructions: M8 plus M4, and M10

October 21, 2026. Both restrictions below are exact. Every coefficient
of their images was checked with Python integer arithmetic. They are
constructive controls and seeds, and do not establish an improved
matrix multiplication exponent.

\[
A(5,6)\longrightarrow M_8\oplus M_4,
\qquad A(5,6)\longrightarrow M_{10}.
\tag{1}
\]

The source has format 300 by 300 by 300 and 27,000 nonzero coefficients.
The direct-sum target has format 80 by 80 by 80 and 576 coefficients.
Its three restriction maps each have 216 nonzero entries, all equal to
1 or -1. The M10 maps have format 100 by 300, with 144 nonzero entries
on each leg, and their image has exactly 1,000 coefficients.

## Source and local multiplication

Use the source coordinates

\[
X=(i,p+q,s),\qquad Y=(j,p,r+s),\qquad Z=(i+j,q,r),
\]

with i,p,r<5 and j,q,s<6. Coordinate flattening is lexicographic in
each displayed tuple. A long coefficient functional acts on products
of a polynomial of degree below five and one of degree below six.
Let e_k denote extraction of the coefficient of x^k.

Take the two short bases

\[
U=(1,x^4),\qquad V=(x-x^4,x^2,x^3,1+x^5).
\tag{2}
\]

Their eight products are independent in the ten-dimensional space of
polynomials of degree below ten. In alpha-major order, a dual list is

\[
R=(e_1,e_2,e_3,e_0,-e_0+e_5,e_6,e_7,e_1+e_4).
\tag{3}
\]

The two complementary functionals are

\[
h_0=-e_0+e_5+e_8,\qquad h_1=-e_1-e_4+e_9.
\tag{4}
\]

Thus R_(alpha,beta)(U_(alpha')V_(beta')) is the Kronecker delta,
and h_0,h_1 annihilate every product U_alpha V_beta. More strongly,
the ten columns consisting of these eight products followed by x^8
and x^9 form an integral basis. Its inverse has rows (R,h_0,h_1).
Both inverse identities are checked exactly by the program.

Cycling the eight-dimensional outer-product identity gives M8. With
vertices I=(alpha_I,beta_I), J=(alpha_J,beta_J), K=(alpha_K,beta_K),
the rows of its maps are

\[
\begin{aligned}
X_{I,J}(i,t,s)&=U_{\alpha_I}(i)R_{\alpha_J,\beta_I}(t)V_{\beta_J}(s),\\
Y_{J,K}(j,p,u)&=V_{\beta_K}(j)U_{\alpha_J}(p)R_{\alpha_K,\beta_J}(u),\\
Z_{K,I}(v,q,r)&=R_{\alpha_I,\beta_K}(v)V_{\beta_I}(q)U_{\alpha_K}(r).
\end{aligned}
\tag{5}
\]

Rows are in the usual matrix order 8I+J, 8J+K, 8K+I.

## A four-vertex block from the complement

Set

\[
P=(x,x^2),\qquad
Q=(-x+x^4,-1-x^5,-1+x^3-x^5,-x^2).
\tag{6}
\]

The four Q vectors are in the span of V. Give them labels Q_(nu,kappa)
with nu,kappa in {0,1}, in that order. Direct multiplication gives

\[
h_\lambda(P_\mu Q_{\nu,\kappa})
=\delta_{\mu,\nu}\delta_{\lambda,\kappa}.
\tag{7}
\]

This is an outer product of two two-dimensional spaces, with its
four-dimensional factor on the second short coordinate. Its cyclic
product is M4. Label its vertices I=(a_I,b_I), J=(a_J,b_J), K=(a_K,b_K),
where both labels are in {0,1}. Its rows are

\[
\begin{aligned}
X'_{I,J}(i,t,s)&=P_{a_J}(i)h_{b_I}(t)Q_{a_I,b_J}(s),\\
Y'_{J,K}(j,p,u)&=Q_{a_J,b_K}(j)P_{a_K}(p)h_{b_J}(u),\\
Z'_{K,I}(v,q,r)&=h_{b_K}(v)Q_{a_K,b_I}(q)P_{a_I}(r).
\end{aligned}
\tag{8}
\]

These formulas directly yield the three pairwise matrix-index
equalities from (7), with coefficient one.

There are no mixed coefficients between (5) and (8). A coefficient
using one row from the M4 block and two rows from M8 has a local factor
h_lambda(U_alpha V_beta)=0. For a coefficient using two M4 rows and
one M8 row, one local edge pairs a core U with a new Q through h.
That factor is zero because Q lies in span(V). The same argument
applies to each cyclic placement. This proves the direct-sum assertion.

The saved direct-sum maps stack (5) above (8). Rows 0 through 63 are
the M8 block, and rows 64 through 79 are the M4 block. The verifier also
applies the maps to every one of the 27,000 original source terms and
checks the entire resulting coefficient dictionary against M8 plus M4.

## The integral M10 seed

Keep U=(1,x^4) and instead choose

\[
V_{10}=(1+x^5,x,x^2,x^3,x^4).
\]

Its ten products with U form an integral basis of the full long space.
An inverse in alpha-major order is

\[
R_{10}=(e_0,e_1,e_2,e_3,e_4-e_9,
        e_9,e_5-e_0,e_6,e_7,e_8).
\]

Formula (5), with five beta labels, therefore gives the exact M10
restriction. Both inverse identities and every output coefficient
are checked independently in the same replay.

## Saved artifacts and replay

- `parity_structure_a56.py` contains the bases, explicit maps, and exact replay.
- `parity_structure_a56_certificate.json` records the checks and all local bases.
- `parity_structure_a56_m8_m4_maps.npz` contains integer A,B,C arrays of shape (80,300), their x,y,z aliases, and the local bases.
- `parity_structure_a56_m10_maps.npz` contains integer A,B,C arrays of shape (100,300), their x,y,z aliases, and the M10 bases.

Run from the repository root:

```
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_a56.py
```

The maps use no numerical optimization, floating-point zero test,
coefficient tolerance, or externally supplied certificate. They are
valid ordinary restrictions; their existence does not supply the larger
target required by the exponent-comparison argument.
