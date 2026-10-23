# Exact contraction-rank strata of the one-dependency oblique residual

October 23, 2026. Owner-directed OpenAI research. This is a written,
unreviewed all-field proof, with independently implemented finite controls
within the same generating session. It supplies **no** exponent improvement
and does not bound border rank beyond the previously credited (12\ldots18)
interval at (r=5).

## Question and tensor

Which ordinary matrix ranks occur in all three spaces of one-leg
contractions of the fixed one-dependency residual, and which first-leg
linear spaces have every nonzero slice of rank two?

Fix any field (F) and integer (k\ge0); write (r=k+2). Use bases

\[
\begin{aligned}
 A&=\langle u,v,w,h_1,\ldots,h_k,z_1,\ldots,z_k\rangle,\\
 B&=\langle X,Z,a,\eta,y,x_1,y_1,\ldots,x_k,y_k\rangle,\\
 C&=\langle P,Q,R,S,T,p_1,q_1,\ldots,p_k,q_k\rangle.
\end{aligned}
\]

Define the integer tensor, viewed over (F),

\[
\begin{split}
E_k={}&u(XP+ZQ)+v(aR+\eta S)\\
 &+w(XQ+ZT+\eta R+yS+XR)\\
 &+\sum_{j=1}^k h_j(Xp_j+Zq_j)
  +\sum_{j=1}^k z_j(x_jR+y_jS).
\end{split}                                                    \tag{1}
\]

Juxtaposition denotes a tensor product, not multiplication in a common
algebra. This is exactly the adapted tensor in PR147's
`full_residual_rank.md` and `oblique-border-equalizer/proof.md`,
with (k=r-2=b-1); those packages prove its identification with the
original projected (Q(b+2,b)\) residual, including integral coordinate
embeddings. We do not reattribute or re-prove that identification.
The theorem below applies directly to the explicitly given tensor (1)
over *every field*, without invoking a border-rank continuity argument.

Let (\rho_D(\ell)\) be the ordinary matrix rank of the contraction of
(E_k) by (\ell\in D^*\), for (D=A,B,C\). A two-column rank below means
the rank over (F) of the matrix whose rows are the displayed pairs.
An empty collection has rank zero.

## Theorem: all three contraction profiles

**First leg.** For
(\alpha=(U,V,W,H_1,\ldots,H_k,Z_1,\ldots,Z_k)\in A^*\), set
(\mathcal H=(U,H_1,\ldots,H_k)\) and
(\mathcal V=(V,Z_1,\ldots,Z_k)\). Then

\[
\rho_A(\alpha)=
\begin{cases}
0,&\alpha=0,\\
2,&W=0\text{ and exactly one of }\mathcal H,\mathcal V\text{ is nonzero},\\
4,&\text{otherwise}.
\end{cases}                                                     \tag{2}
\]

In particular every nonzero first slice has rank two or four, even in
characteristic two. The projective rank-at-most-two locus is exactly

\[
\mathbf P\langle u^*,h_1^*,\ldots,h_k^*\rangle
\ \sqcup\
\mathbf P\langle v^*,z_1^*,\ldots,z_k^*\rangle,
                                                                  \tag{3}
\]
two disjoint projective (k\)-spaces. Every vector subspace of (A^*\)
whose nonzero elements all have rank two lies in one of these two
summands, so its dimension is at most (k+1\); the bound is sharp.

**Second leg.** Let (\beta\in B^*\), writing its coefficients
(b_X,b_Z,b_a,b_\eta,b_y,b_{x_j},b_{y_j}\). Put
\[
 s_B=\operatorname{rank}
 \begin{pmatrix}
 b_a&b_\eta\\
 b_{x_1}&b_{y_1}\\
 \vdots&\vdots\\
 b_{x_k}&b_{y_k}
 \end{pmatrix}.
\]
Then
\[
\rho_B(\beta)=
\begin{cases}
 k+2+s_B,&(b_X,b_Z)\ne(0,0),\\
 \operatorname{rank}
 \begin{pmatrix}
 b_a&b_\eta\\b_\eta&b_y\\
 b_{x_1}&b_{y_1}\\\vdots&\vdots\\b_{x_k}&b_{y_k}
 \end{pmatrix},&(b_X,b_Z)=(0,0).
\end{cases}                                                     \tag{4}
\]

**Third leg.** Let (\gamma\in C^*\), with coefficients
(c_P,c_Q,c_R,c_S,c_T,c_{p_j},c_{q_j}\), and put
\[
 s_C=\operatorname{rank}
 \begin{pmatrix}
 c_P&c_Q\\
 c_{p_1}&c_{q_1}\\\vdots&\vdots\\c_{p_k}&c_{q_k}
 \end{pmatrix}.
\]
Then
\[
\rho_C(\gamma)=
\begin{cases}
 k+2+s_C,&(c_R,c_S)\ne(0,0),\\
 \operatorname{rank}
 \begin{pmatrix}
 c_P&c_Q\\c_Q&c_T\\
 c_{p_1}&c_{q_1}\\\vdots&\vdots\\c_{p_k}&c_{q_k}
 \end{pmatrix},&(c_R,c_S)=(0,0).
\end{cases}                                                     \tag{5}
\]

For (k\ge1\), the generic second and third contraction rank is
(k+4\), attained whenever the respective displayed two-column matrix
has rank two and the distinguished coefficient pair is nonzero. For
(k=0\), the generic second/third rank is three. These are ordinary
contraction ranks, **not** tensor rank, border rank, or the dimension of
a tensor flattening.

## Proof

For the first assertion arrange the second basis as
(\langle X,Z\rangle\oplus
 \langle a,\eta,y,x_j,y_j\rangle\)
and the third basis as
(\langle P,Q,T,p_j,q_j\rangle\oplus\langle R,S\rangle\).
Every first slice is a block upper-triangular matrix

\[
 \begin{pmatrix}L& D\\0&N\end{pmatrix},                     \tag{6}
\]

where (L\) has two rows (indexed (X,Z\)) and
(N\) has two columns (indexed (R,S\)).
If (W\ne0\), the (XQ\) and (ZT\) entries make (L\) rank two:
the (X\) and (Z\) rows have independent coordinates (Q,T\).
At the same time (\eta R\) and (yS\) make (N\) rank two.
The disjoint row and column partitions in (6) then give rank four,
regardless of (D\).

If (W=0\), the off-diagonal block (D\) is zero. The top block is

\[
 \begin{array}{c|ccccc}
 &P&Q&T&p_j&q_j\\
 X&U&0&0&H_j&0\\
 Z&0&U&0&0&H_j
 \end{array}.
\]

Its rank is two exactly when (\mathcal H\ne0\), and otherwise zero.
The bottom block has rows
((V,0),(0,V),(Z_j,0),(0,Z_j)\) in columns (R,S\),
so likewise has rank two exactly when (\mathcal V\ne0\).
The block ranks add, proving (2). Formula (3) and the subspace
maximality follow: a linear space containing nonzero vectors from both
summands also contains their sum, which has rank four. This uses only
field-linear addition and works in every characteristic.

For the second leg, contract (1) by (\beta\). In the first-leg row
basis the nonzero rows of the resulting (A\times C\) matrix are

\[
\begin{array}{c|l}
u&b_XP+b_ZQ\\
w&b_XQ+b_ZT+(b_X+b_\eta)R+b_yS\\
v&b_aR+b_\eta S\\
h_j&b_Xp_j+b_Zq_j\\
z_j&b_{x_j}R+b_{y_j}S .
\end{array}                                                     \tag{7}
\]

When ((b_X,b_Z)\ne0\), the (h_j\) rows are (k\) independent
vectors in the disjoint peripheral coordinate pairs ((p_j,q_j)\).
Modulo (\langle R,S\rangle\), the (u,w\) rows are independent:
if (b_X\ne0\), they have distinct pivot coordinates (P,Q\);
if (b_X=0\), then (b_Z\ne0\) gives the distinct pivots (Q,T\).
The remaining rows (v,z_j\) span a space of rank (s_B\) entirely
in (\langle R,S\rangle\). This proves the first case of (4).
When (b_X=b_Z=0\), only (w,v,z_j\) survive in (\langle R,S\rangle\),
giving the second matrix in (4).

For the third leg, contract (1) by (\gamma\). The nonzero rows of
the resulting (A\times B\) matrix are

\[
\begin{array}{c|l}
u&c_PX+c_QZ\\
w&(c_Q+c_R)X+c_TZ+c_R\eta+c_Sy\\
v&c_Ra+c_S\eta\\
h_j&c_{p_j}X+c_{q_j}Z\\
z_j&c_Rx_j+c_Sy_j .
\end{array}                                                     \tag{8}
\]

When ((c_R,c_S)\ne0\), the (z_j\) rows are independent in their
disjoint peripheral pairs. The (v,w\) rows are independent modulo
(\langle X,Z\rangle\): they reduce to
((c_R,c_S,0)\) and ((0,c_R,c_S)\) in coordinates ((a,\eta,y)\).
The (u,h_j\) rows span an independent complementary block of rank
(s_C\) in (\langle X,Z\rangle\). This proves the first case of
(5). If (c_R=c_S=0\), only (u,w,h_j\) remain and their displayed
two-coordinate rows give the second case. No division by a scalar,
classification theorem or genericity assumption was used. QED.

## Exact verification and limits

`verify.py` reconstructs all (9+4k\) signed coefficients directly
from (1). It calculates contraction matrices without invoking the
formulas (2)--(5) and checks them by exact finite-field elimination,
then compares with a separately coded formula evaluator. An exhaustive
binary census checks every contraction in all three legs for
(k=0,1,2,3\), and seeded rational and odd-prime probes give
additional arithmetic checks. The exhaustive census is finite evidence
only; the preceding block proof supplies the theorem for all (k\)
and all fields. The verifier can also export a JSON receipt.

The source dependency is PR147 at pinned commit
`29a486ac622261c8b4854fc109fb8ab40dcf91a2`. Its original
(Q\)-source contraction and long-map embeddings are credited there,
not reimplemented here. The extracted tensor (1) is self-contained
and is tested independently of that PR's unmerged files. No claim of
independent external mathematical review, a general degeneration
obstruction, or a better exponent is made.
