# An exact scalar extension of the full A(2,2) source

October 21, 2026. This note gives an ordinary restriction over the
rational numbers:

\[
A(2,2)\oplus\langle1\rangle\longrightarrow M_3.
\]

The extra scalar summand is essential to this particular formula.
On the original source, the constructed image is exactly

\[
\operatorname{tr}(ABC)+\operatorname{tr}(A)
\operatorname{tr}(B)\operatorname{tr}(C).
\]

This is a complete small construction, not a smaller exponent bound or
a restriction from the original source to M3. The previously obtained
full diagonal-SL2 obstruction to A(2,2) to M3 does not apply to this
extended source. The proof below uses a rational triangular matrix
identity and does not depend on the symbolic discovery calculation.

## 1. The source as a restricted trace tensor

The full source has coefficient one at

\[
X=(i,p+q,s),\quad Y=(j,p,r+s),\quad Z=(i+j,q,r),
\qquad i,j,p,q,r,s\in\{0,1\}.
\]

Use a common order for a source functional on each leg:

\[
F_X(i,k,s),\quad F_Y(p,k,j),\quad F_Z(r,k,q),
\qquad k\in\{0,1,2\}.
\]

Associate a four-by-four matrix to such a functional by

\[
W(F)_{(i,q),(p,s)}=F(i,p+q,s),
\]

with rows and columns in the lexicographic order of pairs in
\(\{0,1\}^2\). This map is injective. Its image is the
12-dimensional space W of matrices whose two middle binary indices
are symmetric. Directly expanding a matrix trace gives

\[
\begin{aligned}
\operatorname{tr}(W(F_X)W(F_Y)W(F_Z))
={}&\sum_{i,j,p,q,r,s}
F_X(i,p+q,s)\\[-2pt]
&\hspace{12mm}\cdot F_Y(p,r+s,j)F_Z(r,i+j,q).
\end{aligned}
\]

This is exactly the contraction with A(2,2), with the cyclic coordinate
orders just specified. No term is omitted, and every coefficient is one.

## 2. A triangular embedding with a trace correction

For a three-by-three matrix

\[
A=\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix},
\]

define the linear map into four-by-four matrices

\[
J(A)=
\begin{pmatrix}
e+i&2d-h/2&b/2&a\\
b/2&a&c&-b/2\\
h/2&g&i&-h/2\\
i&-h/2&b/2-2f&a+e
\end{pmatrix}.
\]

The paired entries in the preceding definition of W agree, so every
J(A) belongs to W. Let

\[
P=\begin{pmatrix}
0&1&0&1\\
1&0&0&0\\
0&0&1&0\\
0&-1&0&1
\end{pmatrix}.
\]

This matrix is invertible over the rationals. Multiplication gives

\[
P^{-1}J(A)P=
\begin{pmatrix}
a&b&c&0\\
d&e&f&0\\
g&h&i&0\\
d-h/2&-a+i&b/2-f&a+e+i
\end{pmatrix}
=\begin{pmatrix}A&0\\\ell(A)&\operatorname{tr}(A)\end{pmatrix}.
\]

Products of these matrices remain lower triangular in the displayed
three-plus-one block decomposition. Taking the trace of a product of
three therefore proves

\[
\operatorname{tr}(J(A)J(B)J(C))
=\operatorname{tr}(ABC)
+\operatorname{tr}(A)\operatorname{tr}(B)\operatorname{tr}(C).
\tag{1}
\]

The same argument gives, for every positive word length r,

\[
\operatorname{tr}\!\left(\prod_{t=1}^r J(A_t)\right)
=\operatorname{tr}\!\left(\prod_{t=1}^r A_t\right)
+\prod_{t=1}^r\operatorname{tr}(A_t).
\]

Together with Section 1, equation (1) is the asserted restriction of
the original full source to a rank-one perturbation of M3.

## 3. The extra scalar and the complete maps

Append a thirteenth coordinate on every source leg, and one source term
on the triple of appended coordinates. Send its coordinate to
\(-\operatorname{tr}(A)\), \(-\operatorname{tr}(B)\), and
\(-\operatorname{tr}(C)\) on the three legs. The product is the negative
of the extra term in (1). The full image is consequently M3 exactly.

Here is the common source functional F corresponding to J(A), ordered
by \((i\cdot3+k)\cdot2+s\):

\[
\left(
e+i,\ 2d-h/2,\ b/2,\ a,\ c,\ -b/2,
h/2,\ g,\ i,\ -h/2,\ b/2-2f,\ a+e
\right).
\]

Apply this formula on X directly. On the Y leg, convert the original
coordinate (j,p,k) to the common order (p,k,j). On Z, convert (k,q,r)
to (r,k,q). The final scalar coordinate maps to \(-a-e-i\) on every
leg. These formulas specify all entries of the three nine-by-thirteen
restriction matrices. Every entry has denominator dividing two.

The machine-readable certificate contains the entire matrices as
integer numerators with common denominator two. Target rows have
orders 3I+J, 3J+K, and 3K+I. Original source orders are

\[
(i\cdot3+p+q)\cdot2+s,\qquad
(j\cdot2+p)\cdot3+r+s,\qquad
((i+j)\cdot2+q)\cdot2+r.
\]

All indices are zero based. Source coordinate 12 is the scalar summand.

## 4. Exact verification and discovery record

The pure-Python verifier reconstructs all 64 original source points and
the one appended scalar point. It accumulates transformed coefficients
with Python integers, clears the denominator cubed, and compares all
729 coefficients with the standard M3 tensor. It finds precisely the
27 required nonzero coefficients. A separate replay omits the scalar
point and checks all coefficients of (1).

The derivation script also checks the triangular identity on each of
the nine matrix units. Its W-trace control compares a full contraction
against direct four-by-four trace multiplication, with integer maps.
These checks support the explicit proof; they are not numerical fits.

The construction was discovered inside the diagonal-SL2 intertwiner
space. The physical four-dimensional module is
\(\mathfrak{sl}_2\oplus\mathbf1\), and W has irreducible decomposition
\(V_4\oplus2V_2\oplus V_0\). The target leg End(V2) has one copy
each of V0, V2, and V4. An exact intertwiner basis therefore has four
parameters, ordered by target degrees (0,2,2,4). For the basis saved by
the script, the rational choice is

\[
(u_0,u_1,u_2,u_3)=(1/3,1/4,-1/2,-1/12).
\]

The cyclically equal coefficient system with a scalar correction has
the reduced Gröbner basis

\[
1728u_3^3+1,\quad u_1^2-9u_3^2,\quad
u_0+4u_3,\quad u_2-6u_3,\quad \mathrm{scalar}+1.
\]

Removing the scalar correction makes this particular system
inconsistent, as expected from the existing stronger equivariant
obstruction. The explicit J and P formulas provide the construction
without needing to trust the Gröbner-basis computation.

## 5. Reproduction and scope

From the repository root, the exact certificate replay requires only
the Python standard library:

```sh
python research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin1_verify.py results/anisotropic-constructions-2026-10-20/parity_balancing_spin1/scalar_witness.json
```

The optional discovery and regeneration script uses NumPy and SymPy:

```sh
python research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin1.py --groebner --output results/anisotropic-constructions-2026-10-20/parity_balancing_spin1
```

The result directory contains `scalar_witness.json`, the same maps in
`scalar_witness.npz`, the original-source maps in `defect_maps.npz`,
the four intertwiners and coefficient tensor in `coefficient_core.npz`,
and the exact discovery report. The certificate explicitly records
that the source includes a scalar summand and that no exponent
improvement has been established.

Review status: author-checked proof and exact replay in this generating
session; no external independent review or formalization is claimed.

## 6. An ordinary full-source A(2,3) to M3 composition

The separate [corner-extension construction](parity_structure_corner_extension.md)
gives an exact restriction A(2,3) to A(2,2) direct sum one scalar.
It keeps the original A(2,2) coordinates and uses the extra source rows
X(1,3,2), Y(2,1,3), and Z(3,2,1) for the scalar. Every mixed
coefficient vanishes. Composing it with the maps above gives

\[
A(2,3)\longrightarrow M_3
\]

with no external scalar summand. The complete composed maps have
shape nine by twenty-four and denominator two. The certificate
`results/anisotropic-constructions-2026-10-20/parity_balancing_a23_m3.json`
contains every map entry and hashes of both source certificates.
The exact verifier reconstructs all 216 terms of the full A(2,3)
source and checks every one of the 729 target coefficients. It
obtains precisely the standard M3 tensor.

The composition script is `parity_balancing_a23_m3.py`; the same
standard-library verifier used above accepts this composed JSON.
This is a concrete ordinary full-source construction. It does not
remove the scalar requirement from the A(2,2) construction and does
not establish a smaller exponent.
