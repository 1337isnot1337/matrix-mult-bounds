# Four polynomial chains with a smaller ignored space

October 21, 2026. This package gives a second explicit rational
construction of

\[
R_{\rm spin}\longrightarrow M(3,3,14),\qquad
A(4,8)\longrightarrow M(3,3,14),\qquad
A(8,8)\longrightarrow M(3,3,28).
\tag{1}
\]

The construction uses the same first spin-one map as
[the earlier fourteen-channel module](spin_module14.md), but changes
both other maps. Its ignored subspace has dimension 34, and the exact
join has dimension 76. The earlier saved construction used dimensions
36 and 78. This creates a different space of possible exact corrections;
it does not by itself increase the number of channels.

The full first response of the new saved maps has rank 192. A specified
27-channel deletion has a transfer matrix of rank 117, with three exact
coordinate kernel vectors. These statements concern the displayed maps.
They neither construct the full square target nor establish a smaller
matrix multiplication exponent.

## 1. Source and general construction

Use the reduced source

\[
\sum_{i,p,q,s\in\{0,1\},\ a<4,\ j<8}
 X(i,p+q,s)Y(p,a+s,j)Z(q,a,i+j).
\tag{2}
\]

Its format is \((12,80,72)\), with coordinate orders
\((i\cdot3+k)\cdot2+s\), \((p\cdot5+L)\cdot8+j\), and
\((q\cdot4+a)\cdot9+H\). For a matrix
\(A=\left(\begin{smallmatrix}a&b&c\\d&e&f\\g&h&i\end{smallmatrix}\right)\),
the first functional is

\[
F(A)=\left(e+i,2d-h/2,b/2,a,c,-b/2,
 h/2,g,i,-h/2,b/2-2f,a+e\right).
\tag{3}
\]

Identify \(V=\mathbb Q^{32}\) with polynomials of degree at most three
in \(x\) and seven in \(y\). Define

\[
J_s e_{a,j}=e_{a+s,j}\in\mathbb Q^{40},\qquad
(K_i z)_{a,j}=z_{a,j+i},\quad K_i:\mathbb Q^{36}\to V.
\]

Let \(L_{p,s}=e_p\otimes J_s\), in order
\(L_0=L_{0,0},L_1=L_{0,1},L_2=L_{1,0},L_3=L_{1,1}\), and put

\[
L'_0=L_1,\qquad L'_1=(L_0-L_3)/2,\qquad L'_2=L_2.
\tag{4}
\]

For a chosen subspace \(U\subset V\), define the pair space

\[
D=\{(z^+,z^-): K_1z^+,\ K_0z^-,\ K_0z^+-K_1z^-\in U\}.
\tag{5}
\]

Given selected pairs, write \(v_\alpha=K_0z^+_\alpha\). The three last-leg
rows for a channel are

\[
\zeta_{0,\alpha}=(0,z^+_\alpha),\quad
\zeta_{1,\alpha}=(z^+_\alpha/2,-z^-_\alpha/2),\quad
\zeta_{2,\alpha}=(z^-_\alpha,0).
\tag{6}
\]

Set \(W=\sum_{p,s}L_{p,s}U\). If

\[
B=[\operatorname{basis}(W), L'_0v_\alpha,L'_1v_\alpha,L'_2v_\alpha]
\tag{7}
\]

has independent columns, choose the second-leg rows dual to its last
three channel groups and zero on \(W\). The spin-one block identity in
[the general construction, Sections 1–3](spin_module14.md) then gives

\[
Y_{j,\alpha} S(F(A))\zeta_{i,\beta}
 =A_{ij}\delta_{\alpha\beta}.
\tag{8}
\]

For completeness, the mechanism is that the transformed first physical
matrix is
\(\left(\begin{smallmatrix}A&0\\\ell(A)&\operatorname{tr}A\end{smallmatrix}\right)\).
The three vectors (6) transform to \(e_i\otimes v_\alpha\) modulo
\(U^4\), with their fourth component in \(U\). The transformed first
matrix preserves \(U^4\); all error terms therefore land in \(W\) and
are killed by the second map. This includes both the trace and lower-row
terms. The verifier also contracts all coefficients of (2), so no
unverified cancellation is needed for (1).

## 2. The four chains and exact join

Use the integral polynomials

\[
\begin{aligned}
g_0&=-y-y^3-y^6,& g_1&=y-y^3-y^4,\\
g_2&=-1+x(1-y^4),& g_3&=y^2-y^3+xy^2.
\end{aligned}
\]

Let \(U\) be spanned by \(g_0,xg_0,x^2g_0,x^3g_0\) and by
\(g_j,xg_j,x^2g_j\) for \(j=1,2,3\). Then

\[
\dim U=13,\qquad \dim W=34,\qquad \dim D=15.
\tag{9}
\]

The chain lengths are \((4,3,3,3)\). They give the structural upper
bound \(\dim W\le 2\sum_j(\ell_j+1)=34\). The verifier rebuilds an
independent set of 34 columns. It also checks a rank-19 annihilator of
\(U\), every pair equation, and the rank-57 constraint matrix defining
\(D\subset\mathbb Q^{72}\).

Take the canonical rational nullspace basis \(d_0,\ldots,d_{14}\) of
these pair equations, using ascending free-variable order. Select

\[
d_\alpha+d_{14},\qquad 0\le\alpha<14.
\tag{10}
\]

The mixing in (10) matters: the successful selected space was found
after tests that retained only canonical basis columns failed. No
general exclusion of such column selections is asserted.

The \(80\times76\) join (7) has the saved rational minor

\[
\det B_{\rm saved\ rows}=\frac1{73728}\ne0.
\tag{11}
\]

The exact maps have the following sizes. Every coefficient is included
in the witness JSON.

| Map | Shape | Common denominator | Nonzero entries |
|---|---:|---:|---:|
| First | \(9\times12\) | 2 | 16 |
| Second | \(42\times80\) | 48 | 1909 |
| Third | \(42\times72\) | 24 | 658 |

The optional generator uses rational linear algebra. The maintained
verifier uses integer and rational arithmetic from the Python standard
library; it does not import the generator.

## 3. Original-source maps and complete replay

All full-source maps use the common coordinate
\(F(i,k,s)\), numbered \((i(a+b-1)+k)b+s\), on each leg.
The full tensor is

\[
\sum F_X(i,p+q,s)F_Y(p,r+s,j)F_Z(r,i+j,q).
\tag{12}
\]

The embedding into \(A(4,8)\) sends reduced coordinates to
\(X(i,k,s)\mapsto F(i,k,s)\),
\(Y(p,L,j)\mapsto F(p,L,j)\), and
\(Z(q,a,H)\mapsto F(a,H,q)\).

For the two matched copies in \(A(8,8)\), use \(e\in\{0,1\}\) and

\[
X(i,k,s)\mapsto F(i,k,2s),\quad
Y_e(p,L,j)\mapsto F(p,e+2L,j),\quad
Z_e(q,a,H)\mapsto F(e+2a,H,q).
\tag{13}
\]

The source equation \(e_Y+2L=e_Z+2a+2s\) forces \(e_Y=e_Z\), then
\(L=a+s\). The other equations recover (2). Thus all mixed-copy
coefficients vanish. Target row orders are \(3i+j\),
\(j\cdot\text{middle}+\alpha\), and
\(i\cdot\text{middle}+\alpha\); the last row denotes \(Z_{\alpha,i}\).

| Source | Original source terms checked | All target coefficients | Nonzero coefficients |
|---|---:|---:|---:|
| Reduced source | 512 | 15876 | 126 |
| \(A(4,8)\) | 32768 | 15876 | 126 |
| \(A(8,8)\) | 262144 | 63504 | 252 |

Each surviving coefficient is exactly one after division by
\(2\cdot48\cdot24=2304\). The replay compares the entire sparse result
against the full matrix multiplication tensor, including every required
zero coefficient.

## 4. Full first response

The new saved second-leg maps use only \(p=0,1\), and the third-leg maps
use only \(q=0,1\). Therefore their complete response on the original
first source leg is supported on the 192 coordinates
\(F(i,k,s)\) with \(k\in\{0,1,2\}\).

The response certificate selects 192 target-coordinate pairs. The
verifier regenerates their integer coefficients from all of (12) and
checks a minor whose determinant is 29618 modulo 65521. The structural
upper bound and this nonzero minor prove

\[
\operatorname{rank}\mathcal R_X=192\quad\text{over }\mathbb Q.
\tag{14}
\]

Consequently, the saved 28-channel pair has a first-response kernel of
dimension 768. This has not been reduced by the construction itself.
Numerical or finite-field correction probes are not part of the exact
claim in (14).

## 5. A changed transfer after deleting one channel

Delete original middle channel zero from both the second and third
maps. This gives the exact subsystem \(M(3,3,27)\). In the following
formula, keep original middle labels: the surviving channels are
\(1,\ldots,27\), and channel one is the distinguished channel.

For the remaining wrong channels \(\beta=2,\ldots,27\), define the
integer transfer matrix using the saved third-map numerators:

\[
G_1[(i,s,I,\beta),(L,j)]
=Z_{I,\beta}(r=L-s,\ H=i+j,\ q=1),
\tag{15}
\]

with a zero coefficient when \(r\notin\{0,\ldots,7\}\). Here
\(i,s,j<8\), \(I<3\), and \(L<15\). Its shape is \(4992,120\).
The exact kernel is

\[
\ker G_1=\operatorname{span}\{e_{(0,5)},e_{(0,6)},e_{(0,7)}\}.
\tag{16}
\]

The verifier checks all 4992 rows against each displayed vector and
checks their independence. It then rebuilds the saved 117-square minor,
whose determinant is 24747 modulo 65521. These two checks prove (16)
and rank 117 over the rationals, without assuming that a modular rank
is an upper bound.

This is a concrete transfer freedom for these changed maps. It does
not by itself provide a complete added row, column, or square block;
those constructions also require the other coefficient identities.

## 6. Reproduction and scope

Run the exact maintained replay from the repository root:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_w34.py
python -S -m unittest discover -s tests -p 'test_parity_structure_spin_w34.py'
```

The tests contract the complete source, regenerate both rank
certificates, reject a nonzero-to-nonzero map change, and reject a false
kernel vector. The optional `parity_structure_spin_w34_generate.py`
reconstructs the maps using SymPy and the saved finite-field discovery
record.

The full source coefficient identity was also checked by a second agent
in this generating session; no external independent review is claimed.
The construction, rank data, and any future deformation of these maps
must retain their separate scopes. No smaller matrix multiplication
exponent is established here.
