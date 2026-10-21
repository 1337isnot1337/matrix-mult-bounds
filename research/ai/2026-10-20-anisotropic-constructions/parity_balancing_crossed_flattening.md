# An optimal crossed-module branch and its ordinary large-target limit

**Claim ID: AI-CROSSED-FLAT-104.** Research calculation, October 21, 2026.
This note proves three scoped statements.

1. In the identity/product branch, the exact module constructions
   $R_0\to M(2,2,11)$ and $R\to M(2,2,22)$ attain the largest possible
   integer middle dimensions.
2. Under arbitrary ordinary linear maps,
   $R\not\to M(2,2,27)$. This stronger statement uses a first-leg
   normalization justified specifically at middle dimension 27.
3. In the full source $A(8,8)$, fixing the sixteen first images
   $E_{(i,t),(p,u)}\mapsto F(i,2p+t,2u)$ forces $r\le22$ for
   $M(4,4,r)$, even when both other maps are arbitrary.

The source $R$ is a particular subsystem of $A(8,8)$. These statements
do not exclude unrestricted full-source constructions or arbitrary
singular first-leg families, and they do not establish a new exponent.

## 1. Source and four-factor flattening

Let $R_0$, of format $(4,40,36)$, have coefficient one at

$$
 (x,y,z)=(2i+u,\;8(a+u)+j,\;9a+j+i),
 \qquad i,u\in\{0,1\},\quad 0\le a<4,\quad0\le j<8.
$$

It is the crossed product $C(2,4)\otimes C(2,8)$. Two matched copies
share the first space. Their source $R$, of format $(4,80,72)$, has
the same terms with $y$ increased by $40e$ and $z$ by $36e$,
where $e=0,1$.

Split the first index as the two binary indices $(i,u)$. Regard the
source as a four-factor tensor, and flatten it by grouping

$$
 (i,Y)\quad\hbox{against}\quad(u,Z).
 \tag{1}
$$

For one copy this is an $80\times72$ matrix with entries

$$
 F_{(i,L,j),(u,a,H)}
 =\mathbf1_{L=a+u}\mathbf1_{H=j+i}.
$$

After row and column permutations, this is a Kronecker product of

$$
 P_{L,(u,a)}=\mathbf1_{L=a+u},
 \qquad
 Q_{(i,j),H}=\mathbf1_{H=j+i}.
$$

The first factor has format $5\times8$ and rank 5; the second has
format $16\times9$ and rank 9. Both ranks have unit coordinate
minors. For the first, select columns $(u,a)=(0,0),\ldots,(0,3),(1,3)$.
For the second, select rows $(i,j)=(0,0),\ldots,(0,7),(1,7)$.
The selected submatrices are identity matrices in degree order.
Consequently

$$
 \operatorname{rank}F(R_0)=45,\qquad
 \operatorname{rank}F(R)=90.
 \tag{2}
$$

The matched-copy statement follows because (1) is a direct sum over
the common copy label $e$ after permutation.

## 2. Target rank and branch optimality

In the target $M(2,2,r)$, the nonzero entries are

$$
 T_{2i+u,\;ur+\alpha,\;ir+\alpha}=1,
 \qquad0\le\alpha<r.
$$

Flattening (1) is a $4r\times4r$ permutation matrix: row
$(i,u,\alpha)$ is paired with column $(u,i,\alpha)$. It has rank $4r$.

If the first map is the identity, arbitrary maps on $Y$ and $Z$
act on (1) by left and right multiplication. If the first map is a
product change on the two binary factors, it likewise acts by
invertible left and right changes. Therefore (2) gives

$$
 r\le11\quad\hbox{for }R_0,\qquad
 r\le22\quad\hbox{for }R.
 \tag{3}
$$

These bounds are attained by the rational eleven-channel witness and
its two matched copies. The full-source lifts are replayed separately
in the companion cross-module lift note.

For a product change followed by first-index transpose, the source
flattening instead groups $(u,Y)$ against $(i,Z)$. Its two factors
have formats $10\times4$ and $8\times18$ and ranks 4 and 8:

$$
 P'_{(u,L),a}=\mathbf1_{L=a+u},\qquad
 Q'_{j,(i,H)}=\mathbf1_{H=j+i}.
$$

The identity minors are obtained by setting $u=0$ in the first and
$i=0$ in the second. Thus this branch has source ranks 32 and 64,
giving the stricter bounds $r\le8$ and $r\le16$.

The first-map hypothesis matters. An arbitrary $GL_4$ change need not
preserve the four-factor flattening rank. The verifier includes an
explicit non-product shear for which the source rank is larger than 45.

## 3. Why arbitrary ordinary first maps normalize at the large target

Write $J_0,J_1:\mathbb C^4\to\mathbb C^5$ for the shifted injections
$J_ue_a=e_{a+u}$, and write
$K_0,K_1:\mathbb C^9\to\mathbb C^8$ for the shifted projections
$K_ih_H=e_{H-i}$ when the index lies in $\{0,\ldots,7\}$.
For first coefficient matrix $f=(f_{iu})$, the source slice is

$$
 S(f)=\sum_{i,u}f_{iu}\,J_u\otimes K_i.
$$

The two independent binary polynomial changes of variables act as
$GL_2\times GL_2$ on $f$, with induced invertible changes on the other
source legs. Hence its nonzero slice ranks depend only on whether $f$
has rank one or two.

The rank-one normal form $J_0\otimes K_0$ has rank 32. The rank-two
normal form $J_0\otimes K_0+J_1\otimes K_1$ has rank 36. To check the
latter directly, a kernel vector consists of four vectors $v_a$ in
$\mathbb C^9$. Its first four block equations force

$$
\begin{aligned}
v_0&=c_0h_8,\\
v_1&=-c_0h_7+c_1h_8,\\
v_2&=c_0h_6-c_1h_7+c_2h_8,\\
v_3&=-c_0h_5+c_1h_6-c_2h_7+c_3h_8.
\end{aligned}
$$

The last equation is
$-c_0e_4+c_1e_5-c_2e_6+c_3e_7=0$, so the kernel is zero.
The matched source $R$ therefore has nonzero slice ranks 64 and 72.

Suppose there were an ordinary restriction
$R\to M(2,2,27)$. The first parameter map is invertible because its
source and target dimensions are both four and the target is concise.
A rank-one first coefficient matrix in the target has slice rank 27.
The source lift can have rank at most

$$
 27+(80-54)+(72-54)=71.
 \tag{4}
$$

Here the two added quantities are precisely the codimensions of the
other target parameter spaces. Restricting a bilinear form to those
spaces can reduce its rank by at most the sum of these codimensions.

The 72-rank stratum is forbidden by (4). Thus the invertible first
map sends every rank-one $2\times2$ matrix to a rank-one matrix.
The determinant quadric is irreducible, so the determinant after this
linear change is a nonzero scalar multiple of the original determinant.
The two rulings of the quadric are the maximal linear spaces with one
factor fixed. An invertible map either preserves the rulings or
interchanges them. It therefore has the form

$$
 f\longmapsto PfQ
 \quad\hbox{or}\quad
 f\longmapsto Pf^{\mathsf T}Q
$$

for invertible $2\times2$ matrices $P,Q$. Equivalently, one can recover
this description by choosing two distinct lines from each ruling:
their four intersections determine the product bases, and the remaining
rank-one lines force the coefficient scalings to factor.

The first case contradicts $27>22$ in (3). The transpose case
contradicts $27>16$. This proves the stated arbitrary ordinary exclusion.
The same reasoning excludes $R_0\to M(2,2,14)$, using the budget
$14+(40-28)+(36-28)=34<36$ and branch bounds 11 and 8.

## 4. Exact controls and limits

The standard-library verifier checks every source flattening coefficient
against the displayed Kronecker factors, verifies all four source ranks
over the prime field of order 65,521, and checks the target permutation
matrices. The unit minors and factorization prove that the ranks over
$\mathbb Q$ are exactly the recorded ranks.

The ordinary normalization in Section 3 is not applied to an arbitrary
singular family. In such a family the intermediate tensors need not be
the exact target, and the first maps need not stay regular or remain in
the product/transpose subgroup. No exclusion of those families is
claimed here. Likewise, extra source directions omitted by the crossed
module may participate in a full $A(8,8)$ construction.

The argument has been checked by other agents in this generating
session. No external independent review or formalization is claimed.

## 5. The full source with these sixteen first images fixed

The restriction to the crossed subsystem omitted some source directions
on the other two legs. Those directions still do not increase the
middle dimension if the sixteen first images remain

$$
 E_{(i,t),(p,u)}\longmapsto F(i,2p+t,2u),
 \qquad i,t,p,u\in\{0,1\}.
 \tag{5}
$$

This statement imposes no support or other restriction on the two
remaining full-source maps.

To see this, begin with every original $A(8,8)$ source term

$$
 X(i,p'+q',s)Y(p',r'+s,j)Z(r',i+j,q').
$$

After (5), a contributing term has $p'+q'=2p+t\le3$. Hence
$p',q'\in\{0,1,2,3\}$. Also $s=2u$, so its other coordinates lie in
the spaces

$$
 Y:\ 0\le p'<4,\quad0\le L<10,\quad0\le j<8,
 \qquad
 Z:\ 0\le q'<4,\quad0\le r'<8,\quad0\le H<9.
$$

Their dimensions are 320 and 288. Coefficients of arbitrary $Y,Z$
maps on every other source coordinate make no contribution.

Write $r'=e+2a$ and $L=e+2(a+u)$. The contributing tensor factors
exactly as

$$
 J_4\otimes R,\qquad
 (J_4)_{(t,p),p',q'}=\mathbf1_{p'+q'=2p+t}.
 \tag{6}
$$

It has format $(16,320,288)$ and 2560 nonzero coefficients. Here $R$
is the same matched crossed source as before. The grouping of factors
in the target first space is $(i,t)$ against $(p,u)$.

Flattening $J_4$ by $(t,p')$ against $(p,q')$ gives an $8\times8$
matrix of rank 4. In lexicographic order row 3 is zero, rows
5,6,7 repeat rows 0,1,2, and rows 0,1,2,4 contain an identity minor
in columns 0,5,4,1. Thus the full flattening of (6), by

$$
 ((i,t),Y)\quad\hbox{against}\quad((p,u),Z),
$$

has rank $4\cdot90=360$. For $M(4,4,r)$ the same flattening is a
$16r\times16r$ permutation matrix. Arbitrary changes of the two other
maps can only decrease its rank, so $16r\le360$ and $r\le22$.

The verifier independently enumerates all 262,144 original source terms,
keeps the terms selected by the literal first maps (5), and compares
the resulting sparse flattening with the product in (6). It checks
the integer rank-four factor and its identity minor as well.

In particular a full $M_{27}$ target, or the $M_{27}$ block of
$M_{27}\oplus M_7$, cannot retain the sixteen first images (5).
Restricting such a target to four first-vertex rows and four
second-vertex columns would otherwise yield the forbidden
$M(4,4,27)$. This conclusion requires those fixed images; it is not
an exclusion for a changed first map or an unrestricted full-source
construction.
