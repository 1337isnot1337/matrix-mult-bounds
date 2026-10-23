# An exact integer degeneration C(4,5) to 2-by-2 matrix multiplication

This is a constructive small-model result. It does not improve the matrix multiplication exponent. It supplies a finite Laurent witness for the adjacent model that the earlier ordinary C(4,6) control did not reach. Its coefficients are integers, and its leading coefficient identity is valid over every field.

## 1. Source and target conventions

Write

\[
C(4,5)=\sum_{a=0}^{3}\sum_{b=0}^{4} A_a B_{a+b} C_b.
\]

The source dimensions are `(4,8,5)`. Index each target leg by two binary indices:

\[
X_{is},\quad Y_{ij},\quad Z_{js},\qquad i,j,s\in\{0,1\}.
\]

The target is

\[
T=\sum_{i,j,s=0}^{1}X_{is}Y_{ij}Z_{js}.
\]

This is the tensor for multiplying `X` by the transpose of `Z`, with output paired against `Y`. It is the usual 2-by-2 matrix multiplication tensor after a transpose on one input and a relabeling of the output.

All two-index row orders are lexicographic: `00,01,10,11`.

## 2. Three explicit maps

The constant coefficient matrices are

\[
U=\begin{pmatrix}
1&1&1&1\\
1&0&1&1\\
1&1&0&1\\
0&1&0&1
\end{pmatrix},
\]

\[
V=\begin{pmatrix}
2&-1&0&0&0&0&0&0\\
-8&1&0&1&1&-1&0&0\\
-2&0&-1&1&0&0&0&0\\
-1&0&0&1&-1&0&0&1
\end{pmatrix},
\]

\[
W=\begin{pmatrix}
2&1&0&4&1\\
1&1&1&2&0\\
0&0&1&0&0\\
0&0&0&0&1
\end{pmatrix}.
\]

Use these integer row weights:

| Target row | U weight | V weight | W weight |
|---|---:|---:|---:|
| 00 | 0 | 0 | 0 |
| 01 | 4 | 2 | -4 |
| 10 | 1 | -1 | -2 |
| 11 | 5 | 1 | -6 |

For an indeterminate `t`, the actual three substitutions are

\[
A_a\longmapsto\sum_x t^{u_x}U_{xa}X_x,\qquad
B_k\longmapsto\sum_y t^{v_y}V_{yk}Y_y,\qquad
C_b\longmapsto\sum_z t^{w_z}W_{zb}Z_z.
\]

These are genuine source-resolved linear maps. There are no term-dependent output maps or independently chosen weights on source summands.

## 3. Finite coefficient proof

The coefficient of `X_x Y_y Z_z` in the transformed source is

\[
t^{u_x+v_y+w_z}
\sum_{a=0}^{3}\sum_{b=0}^{4}U_{xa}V_{y,a+b}W_{zb}.
\]

If `x=(i,s)`, `y=(i',j)`, and `z=(j',s')`, its Laurent degree is

\[
(i-i')+2(j-j')+4(s-s').
\]

Each difference belongs to `{-1,0,1}`. Thus degree zero occurs exactly on the eight target positions `i=i'`, `j=j'`, `s=s'`.

The companion verifier checks every one of the 64 coefficient positions using exact integer arithmetic. Each negative-degree coefficient is zero. Each of the eight degree-zero coefficients is one. There are 22 nonzero positive-degree terms, with degrees between one and seven. Their complete integer coefficient list is in the JSON witness.

Consequently the transformed tensor has the exact form

\[
T+tT_1+t^2T_2+\cdots+t^7T_7,
\]

with integer tensors `T_1,...,T_7`. This proves

\[
\boxed{C(4,5)\ \rightsquigarrow\ M_2}
\]

over every field. Reducing the integer equality in any characteristic preserves the constant target coefficient and the vanishing of all negative powers.

## 4. Equivalent polynomial implementation

For a polynomial variable `z`, form

\[
\begin{aligned}
F(z,t)={}&(1+z+z^2+z^3)X_{00}
+t^4(1+z^2+z^3)X_{01}\\
&+t(1+z+z^3)X_{10}
+t^5(z+z^3)X_{11},\\
G(z,t)={}&(2+z+4z^3+z^4)Z_{00}
+t^{-4}(1+z+z^2+2z^3)Z_{01}\\
&+t^{-2}z^2Z_{10}+t^{-6}z^4Z_{11}.
\end{aligned}
\]

Let `P_k` be the coefficient of `z^k` in `FG`. The four output forms, in row order, are

\[
\begin{aligned}
H_{00}&=2P_0-P_1,\\
H_{01}&=t^2(-8P_0+P_1+P_3+P_4-P_5),\\
H_{10}&=t^{-1}(-2P_0-P_2+P_3),\\
H_{11}&=t(-P_0+P_3-P_4+P_7).
\end{aligned}
\]

All negative Laurent powers cancel in these four outputs. Their constant terms are the four entries of `X Z^T`.

## 5. Discovery and verification status

An exact Boolean coefficient search first found a solution over the field with two elements. An independently implemented integer Jacobian calculation found a 36-by-36 minor with determinant exactly one. Its column choice fixes all entries of U. A digit-by-digit Hensel lift then stabilized at the displayed small integer matrices; direct integer substitution proves the result without using Hensel's lemma in the final argument.

The discovery code requires Z3. The final verifier requires only the Python standard library. A separate team agent independently replayed the finite-field seed and recovered another small integer witness by choosing different Jacobian columns. The primary agent and a second construction agent independently replayed the displayed integer witness. The primary agent accumulated the twenty original source monomials and also checked full ranks of all three maps. This is same-session AI verification, not an external proof review.

The row weights use several Laurent degrees. Setting t=1 in this witness retains its positive-degree error terms; that specialization is not asserted to equal matrix multiplication.

No smaller exponent follows from this small construction alone. Its immediate use is as a verified singular pilot, and as a construction template for the larger source-target searches.

## 6. Reproduction

From the repository root, run:

```bash
python research/ai/2026-10-21-singular-pilots/verify_c45.py
python -m unittest discover -s tests -p test_singular_pilots.py
```

The complete witness is retained in
[`c45_integer_witness.json`](../../../results/singular-pilots-2026-10-21/c45_integer_witness.json).
