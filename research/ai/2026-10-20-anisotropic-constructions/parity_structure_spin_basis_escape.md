# An exact change of local source basis escapes the fixed compression identity

Claim **AI-SPIN-BASIS-ESCAPE-126**, October 21, 2026.
This is an exact control for a larger construction family. It does not
construct M9 or establish a matrix multiplication exponent bound.

## 1. What the control establishes

[Claim 124](spin_fiber_closure.md) closes arbitrary scalar weights and
Laurent weights on the prescribed raw columns of one fixed local spin
map. Its two-digit outputs satisfy the linear identity

\[
C(0,1,39)-C(30,31,39)+C(30,31,69)=0.                 \tag{1}
\]

The construction here changes the local source basis **before** those
columns are compressed. The resulting three coefficients are exactly
1, 2, and 7. Their combination in (1) is 6. Thus the enlarged family
is not contained in the hyperplane proved for the fixed family.
The corresponding M9 coefficients are 0, 1, and 0, so this particular
output is not M9 either.

This is a concrete distinction between two map families. It does not
invalidate claim 124 or imply that the larger family contains a desired
matrix tensor or a degeneration to one.

## 2. Exact local maps

Use the common source-coordinate order

\[
F(i,m,s),\qquad \operatorname{col}(i,m,s)=(3i+m)2+s,
\]

where i,s are binary and m ranges from 0 to 2. The local source is

\[
\sum_{i,p,r,j,q,s\in\{0,1\}}
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
\]

Let J be the denominator-two, 9-by-12 map from
[claim 118](spin_fiber_compression.md). Its three copies give

\[
T_{A(2,2)}(J,J,J)=M_3+
 \operatorname{tr}(X)\operatorname{tr}(Y)\operatorname{tr}(Z).       \tag{2}
\]

For g with entries a,b,c,d, use the polynomial multiplication action

\[
H(g)=\begin{pmatrix}
a^2&ab&b^2\\
2ac&ad+bc&2bd\\
c^2&cd&d^2
\end{pmatrix}.
\]

The three short-pair changes and their inverse dual long changes preserve
the cyclic convolution tensor. On source leg ell the action is

\[
S_\ell=g_{\ell+2}\otimes H(g_\ell)^{-\mathsf T}
                 \otimes g_{\ell+1},
\]

with indices taken modulo three. Here S acts on the source variable
vector. The new target-major local map is
J S_ell^T. This follows directly by applying polynomial multiplication
to both short factors on each of the three convolution edges.

Choose the integral matrices

\[
g_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
g_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix},\qquad
g_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

All three determinants equal one. The changed local maps have denominator
two and respectively 44, 44, and 34 nonzero integer numerators. The
verifier reconstructs these maps using exact rational matrix inversion.
It also checks every one of the 729 output coefficients of (2) by
enumerating the 64 original source terms. In particular, the preserved
local identity is checked without relying only on the symmetry argument.

## 3. Two-digit compression and the escape

Use the changed maps in the low digit and the original J in the high
digit. Map each raw source column pair to

\[
(i_0,m_0,s_0;i_1,m_1,s_1)
\longmapsto(i_0+2i_1,m_0+2m_1,s_0+2s_1).
\]

All raw column weights are one. The resulting source is A(4,4), with
column index (7i+m)4+s. The output vertices are numbered with the low
ternary digit first. Target matrix-unit row numbers are 9I+J on X,
9J+K on Y, and 9K+I on Z.

The saved three 81-by-112 maps have denominator four and respectively
704, 704, and 544 nonzero integer numerators. Complete enumeration of
the 4096 original A(4,4) terms gives the following selected coefficients.

| Output row triple | Integer numerator | Denominator | Coefficient |
|---|---:|---:|---:|
| (0, 1, 39) | 64 | 64 | 1 |
| (30, 31, 39) | 128 | 64 | 2 |
| (30, 31, 69) | 448 | 64 | 7 |

Hence the combination in (1) is 1-2+7=6. Only these three full-source
coefficients are needed for the asserted escape. No complete M9 identity
is asserted for the changed compressed maps.

## 4. Reproducible finite discovery, kept separate from the exact claim

The optional `parity_structure_spin_basis_compression.py` evaluates all
81^3 output coefficients and an analytic parameter gradient. It contains
two real local charts: independent SL2 changes on the three convolution
edges of each digit, and independently moving local cyclic quotient
kernels. The latter chart changes the local scalar correction as well.
Both may also use 432 independently weighted raw columns and an optimal
overall output scalar. Finite differences checked the implemented
gradients at the saved initial probes.

Three bounded runs stopped without a matrix tensor witness. The reported
relative residual is the Frobenius error against the full unit M9 tensor,
divided by its norm 27. These are numerical discovery measurements.

| Saved run | Parameters | Iterations | Best relative residual |
|---|---:|---:|---:|
| Source changes, seed183 | 18 | 30 | 6.2056451174 |
| Source changes and weights, seed184 | 450 | 100 | 0.8428307649 |
| Quotient changes and weights, seed185 | 450 | 100 | 0.8347559814 |

The second run developed large map norms; the third retained moderate
norms but still had substantial error. Neither supplies a coherent
Laurent family or an exact identity. The JSON records include parameters,
full residuals, map norms, singular values, and gradient controls.

An additional finite-field discovery record fixes the two compressed
Y/Z maps, either original or changed as in Section 2, and frees the whole
first source map. It checks only the eight common prefix outer-vertex
sets of sizes 9 down to 2, with middle dimension 9. All sixteen prescribed
systems are inconsistent over the field with 65521 elements. This finite
screen is not used to claim a general rational or singular obstruction,
and it does not allow either retained map to vary.

## 5. Exact replay and acceptance scope

`parity_structure_spin_basis_escape_witness.json` stores the source-basis
matrices, all three local maps, all three compressed maps, and the
selected coefficient claims. The standard-library verifier reconstructs
the maps, checks the full local identity, then enumerates the original
larger source for the three selected coefficients. The focused tests
also reject a nonzero-to-nonzero map edit and a false hyperplane claim.

~~~sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_basis_escape.py
python -S -m unittest discover -s tests -p 'test_parity_structure_spin_basis_escape.py' -v
~~~

The optional finite runs can be reproduced with NumPy and SciPy:

~~~sh
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_basis_compression.py --seed 183 --steps 30
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_basis_compression.py --seed 184 --steps 100 --raw-weights --fit-scale
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_basis_compression.py --seed 185 --steps 100 --raw-weights --fit-scale --quotient-kernels
~~~

The exact claim has no optional dependency. A second agent in this generating session checked the multiplication
action, inverse-dual convention, and exact replay. This note records the
construction and its checked scope, with no external independent review
or historical priority claim.
