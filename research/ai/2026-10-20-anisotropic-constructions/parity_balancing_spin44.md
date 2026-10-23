# An exact balanced spin module with four parity copies

October 21, 2026. The rational maps accompanying this note prove

\[
 \boxed{A(4,4)\longrightarrow M(3,3,8),\qquad
        A(8,8)\longrightarrow M(3,3,32).}
 \tag{1}
\]

The second restriction uses four matched parity copies of the first
module inside one copy of the original source. The three map
denominators are $2,42,2$. No scalar correction, auxiliary tensor,
or additional source copy is used.

These are rectangular core constructions. They do not produce a
full square target or improve the matrix multiplication exponent.
The 32-channel construction permits a choice of 27 retained channels,
with five channels left out; any extension or response reduction
still requires its own complete coefficient proof.

## 1. The balanced reduced source

Use binary $i,p,q,s$ and $a,j\in\{0,1,2,3\}$. The reduced tensor is

\[
 R=\sum X(i,p+q,s)\,Y(p,a+s,j)\,Z(q,a,i+j).
 \tag{2}
\]

Its format is $(12,40,40)$, and it has 256 terms. The three
coordinate orders are

\[
 (i\cdot3+p+q)\cdot2+s,\qquad
 (p\cdot5+a+s)\cdot4+j,\qquad
 (q\cdot4+a)\cdot5+i+j.
 \tag{3}
\]

The target row orders are $3I+J$, $8J+\alpha$, and
$8I+\alpha$. The last row denotes $Z_{\alpha I}$.

Let $V=\mathbb Q^{16}$ with coordinates $(a,j)$.
For $t=0,1$, let

\[
 J_t:V\to\mathbb Q^{20},\quad e_{a,j}\mapsto e_{a+t,j},
 \qquad
 K_t:\mathbb Q^{20}\to V,\quad (K_tz)_{a,j}=z_{a,j+t}.
 \tag{4}
\]

There are four left maps
$L_{p,s}:V\to\mathbb Q^2\otimes\mathbb Q^{20}$, placing $J_s$
in block $p$. Their order is $L_0=L_{0,0}$,
$L_1=L_{0,1}$, $L_2=L_{1,0}$, $L_3=L_{1,1}$.

## 2. The fixed spin first map

For a $3\times3$ matrix
$A=\left(\begin{smallmatrix}a&b&c\\d&e&f\\g&h&i\end{smallmatrix}\right)$,
the first coefficient vector is

\[
 F(A)=
 (e+i,\ 2d-h/2,\ b/2,\ a,\ c,\ -b/2,\
  h/2,\ g,\ i,\ -h/2,\ b/2-2f,\ a+e).
 \tag{5}
\]

Define the physical four-square matrix
$J(A)_{(i,q),(p,s)}=F(A)_{i,p+q,s}$. With

\[
 P=\begin{pmatrix}
 0&1&0&1\\
 1&0&0&0\\
 0&0&1&0\\
 0&-1&0&1
 \end{pmatrix},
 \qquad
 \ell(A)=(d-h/2,\,-a+i,\,b/2-f),
\]

direct multiplication gives

\[
 P^{-1}J(A)P=
 \begin{pmatrix}A&0\\ \ell(A)&\operatorname{tr}A\end{pmatrix}.
 \tag{6}
\]

The verifier checks (6) on all nine matrix units.
This is the same triangular spin mechanism as in the
[four-by-eight module](spin_module14.md), now with both intermediate
polynomial directions of length four.

After this change of basis, the three useful left maps are

\[
 L'_0=L_1,\qquad L'_1=(L_0-L_3)/2,\qquad L'_2=L_2.
 \tag{7}
\]

For a pair $(z_0,z_1)\in\mathbb Q^{20}\oplus\mathbb Q^{20}$,
the transformed right tuple is

\[
 (K_0z_1,\ K_0z_0-K_1z_1,\ K_1z_0,\ K_0z_0+K_1z_1).
 \tag{8}
\]

The transpose in the physical source factorization is responsible
for this order. The complete coefficient replay also checks the
orientation directly from (2).

## 3. A six-dimensional intermediate space

Identify $V$ with polynomials of degree at most three in both
$x$ and $y$. Put

\[
 \begin{aligned}
 g_0&=y^2+x(1+y-y^2),\\
 g_1&=-1+x(-1+y-y^3),
 \end{aligned}
 \qquad
 U=\operatorname{span}\{g_0,xg_0,x^2g_0,g_1,xg_1,x^2g_1\}.
 \tag{9}
\]

The six displayed columns are independent. Define

\[
 W=\sum_{p,s=0}^1 L_{p,s}U.
 \tag{10}
\]

Each length-three chain in (9) contributes at most four columns
after applying the two $x$ shifts. The two independent $p$ blocks
give $\dim W\le16$. The saved 16-column basis proves equality.

The endpoint-pair space is

\[
 D=\{(z^+,z^-):
 K_1z^+\in U,\quad K_0z^-\in U,\quad
 K_0z^+-K_1z^-\in U\}.
 \tag{11}
\]

A saved ten-row annihilator of $U$ gives 30 independent equations
on the 40 pair coordinates, so $\dim D=10$.

Choose the eight pairs encoded by the third map in the
[rational witness](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin44_witness.json).
In that file the first eight third rows have form $(0,z^+)$
and the last eight have form $(z^-,0)$, so the pairs are directly
recoverable from the actual map. Set $v_\alpha=K_0z^+_\alpha$.
The three right images for channel $\alpha$ are

\[
 \zeta_{0\alpha}=(0,z^+_\alpha),\qquad
 \zeta_{1\alpha}=(z^+_\alpha/2,-z^-_\alpha/2),\qquad
 \zeta_{2\alpha}=(z^-_\alpha,0).
 \tag{12}
\]

By (8) and (11), their transformed right tuples equal
$e_I\otimes v_\alpha$ modulo $U^4$, with fourth component zero
modulo $U$.

## 4. The exact forty-square join

Form

\[
 B=[\,W,\ L'_0v_0,\ldots,L'_0v_7,\
          L'_1v_0,\ldots,L'_1v_7,\
          L'_2v_0,\ldots,L'_2v_7\,].
 \tag{13}
\]

This is a $40\times40$ rational matrix. With the basis and pair
ordering in the witness,

\[
 \det B=\frac{21}{128}.
 \tag{14}
\]

Take the last 24 rows of $B^{-1}$ as the second map. They annihilate
$W$ and are dual to the last 24 columns in (13).

The triangular matrix in (6) preserves $U^4$. Its action on (12),
modulo $U^4$, is the usual action of $A^T$ on the first three
components; the fourth remains zero. Applying the left maps and
then the join dual therefore gives exactly

\[
 \sum_{I,J=0}^{2}\sum_{\alpha=0}^{7}
       A_{IJ}Y_{J\alpha}Z_{\alpha I}.
 \tag{15}
\]

Thus $R\to M(3,3,8)$, including every zero coefficient.
The code verifies the endpoint equations, determinant (14),
and all 24-by-40 dual equations over the rationals, represented
by exact integers and common denominators.

## 5. Original-source embeddings

Use the common source coordinates
$F(i,k,s)$ on each leg of $A(n,n)$, with terms

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{16}
\]

For $A(4,4)$, embed the reduced coordinates by

\[
 X(i,k,s)\mapsto F(i,k,s),\quad
 Y(p,L,j)\mapsto F(p,L,j),\quad
 Z(q,a,H)\mapsto F(a,H,q).
 \tag{17}
\]

Every active original source term is then exactly a term of (2).

For $A(8,8)$, use four pairs of parity labels $(e,f)\in\{0,1\}^2$:

\[
 \begin{aligned}
 X(i,k,s)&\mapsto F(2i,k,2s),\\
 Y_{e,f}(p,L,j)&\mapsto F(p,e+2L,f+2j),\\
 Z_{e,f}(q,a,H)&\mapsto F(e+2a,f+2H,q).
 \end{aligned}
 \tag{18}
\]

Suppose a selected second coordinate has labels $(e,f)$ and a
selected third coordinate has labels $(e',f')$. Their first short
indices in (16) must be

\[
 i_{\rm physical}=f'-f+2(H-j),\qquad
 s_{\rm physical}=e-e'+2(L-a).
 \tag{19}
\]

Every selected first image has even short indices. Since all labels
are binary, (19) forces $e=e'$ and $f=f'$. The remaining equations
are precisely the reduced source equations. Hence all mixed-copy
coefficients vanish and the four matching copies share the same
first $3\times3$ matrix:

\[
 A(8,8)\longrightarrow M(3,3,4\cdot8)=M(3,3,32).
 \tag{20}
\]

The target middle coordinate is $8(2e+f)+\alpha$.
All source coordinates in (18) lie in their declared ranges.
The construction uses one $A(8,8)$ source, of leg dimension 960.

Doubling both short indices does not by itself justify combining
the first map with a transposed module. The canonical nine-dimensional
first image and its short-swap/target-transpose image are different;
their combined span has dimension 12. Such a combination would
require a separate compatibility construction.

## 6. Complete exact checks

| Source replay | Original source terms | Target coefficients | Nonzero coefficients |
|---|---:|---:|---:|
| Reduced format $(12,40,40)$ | 256 | 5,184 | 72 |
| $A(4,4)$ | 4,096 | 5,184 | 72 |
| $A(8,8)$ | 262,144 | 82,944 | 288 |

All remaining target coefficients are zero. The map denominator
product is $2\cdot42\cdot2=168$, so the full contractions use
integers throughout.

~~~bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin44.py
python -S -m unittest discover -s tests -p test_parity_balancing_spin44.py
~~~

The [full maps](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin44_full_maps.json)
and [replay certificate](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin44_certificate.json)
contain the complete deliverable. The optional discovery and
reconstruction scripts use NumPy and SymPy; the accepted verifier
imports neither. The finite-field search found the square join
on its second polynomial-generator trial, after which rational
reconstruction and every-coefficient replay established (1).

The proof, verifier, and tests were checked by two other agents in
this generating session. No external independent review or
formalization is claimed.
