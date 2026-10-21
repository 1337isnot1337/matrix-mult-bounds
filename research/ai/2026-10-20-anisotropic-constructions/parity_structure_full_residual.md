# Retaining the full convolution residual

October 21, 2026. Written, AI-derived all-size construction and exact finite
coefficient certificates. The determinant argument and cyclic maps were
checked by a second agent in this generating session; no external independent
review. No historical priority, formalization, or smaller exponent is claimed.

For every integer a>=5, there is a rational ordinary restriction

\[
A(a,a+1)\longrightarrow M_{2a-2}\oplus A(2,a-2).
\tag{1}
\]

This retains the full residual pencil from the construction in
`parity_structure_anisotropic_family.md`. In particular,

\[
A(7,8)\longrightarrow M_{12}\oplus A(2,5).
\]

The latter target has common leg dimension 204 and 2,728 nonzero
coefficients. The exported maps are exact rational matrices of shape
(204,784). This is a reusable tensor restriction; the larger target
needed for an exponent improvement remains unconstructed.

## 1. The local core and its complement

Write d=a-1>=4. The two short polynomial spaces have degree bounds d
and d+1, and the long space has degree bound 2d+1. Let e_j extract
the coefficient of x^j. Choose a positive integer gamma and set

\[
U=(1,x^d),\qquad
V_1=x-\gamma x^d,\quad V_j=x^j\ (2\le j<d),\quad
V_*=1+x^{d+1}.
\tag{2}
\]

The d members of V are ordered 1,...,d-1,*. The 2d products U_alpha
V_beta, in that order, have dual functionals

\[
\begin{aligned}
R_{0,j}&=e_j\quad(1\le j<d),&R_{0,*}&=e_0,\\
R_{1,1}&=-e_0+e_{d+1},&R_{1,*}&=\gamma e_1+e_d,\\
R_{1,j}&=e_{d+j}\quad(2\le j<d).
\end{aligned}
\tag{3}
\]

Their two-dimensional annihilator has basis

\[
h_0=-\gamma e_0+\gamma e_{d+1}+e_{2d},\qquad
h_1=-\gamma e_1-e_d+e_{2d+1}.
\tag{4}
\]

The full list of products followed by x^(2d),x^(2d+1) has integer
inverse with rows (R,h_0,h_1). This follows immediately by evaluation
on (2). In particular, h_0 and h_1 annihilate U times V. The cyclic
product of (2)-(3) supplies the M_(2d) block.

To retain the rest, start with

\[
P^{\rm old}=(x,x^2,\ldots,x^{d-1}).
\]

Let D_lambda be the (d-1)-by-d matrix with entries
h_lambda(x^p V_j), for 1<=p<d. Nonzero entries are precisely

\[
\begin{array}{c|c}
D_0&D_1\\ \hline
(D_0)_{1,1}=-\gamma^2&(D_1)_{p,d-p}=-1\quad(1\le p\le d-2)\\
(D_0)_{p,d+1-p}=\gamma\quad(2\le p<d)&(D_1)_{1,*}=-\gamma\\
(D_0)_{d-1,*}=1&(D_1)_{d-1,1}=-1.
\end{array}
\tag{5}
\]

The first d-1 columns of D_0 are nonsingular, so D_0 has full row rank.

## 2. An explicit polynomial kernel and basis determinant

Put epsilon=(-1)^(d-3), and define a d-component polynomial vector
q(t), with components indexed like V:

\[
\begin{aligned}
q_1(t)&=t-\epsilon\gamma^{d-1}t^{d-2},\\
q_j(t)&=\gamma(-\gamma t)^{d-1-j}(1+\gamma t^2)
\quad(2\le j<d),\\
q_*(t)&=-(1+\epsilon\gamma^d t^{d-1}).
\end{aligned}
\tag{6}
\]

The row equations in (5) give

\[
(D_1-tD_0)q(t)=0.
\tag{7}
\]

For example, the first equation is
gamma^2 t q_1-q_(d-1)-gamma q_*=0. The middle equations are
q_j=-gamma t q_(j+1), and the last is
q_1+gamma t q_2+t q_*=0. These three formulas verify (7) directly.

Write q(t)=sum_(k=0)^(d-1) c_k t^k, and let
C=(c_0 ... c_(d-1)). Thus the rows of C are the coefficient vectors
of (6). Its determinant has magnitude

\[
|\det C|=\gamma^{(d-2)(d+1)/2}
\begin{cases}
1+\gamma^{d+1},&d\text{ even},\\
\bigl(1+(-1)^{(d-1)/2}\gamma^{(d+1)/2}\bigr)^2,
&d\text{ odd}.
\end{cases}
\tag{8}
\]

Here is an elementary verification of (8). Write r(t)=1+gamma t^2.
The components q_2,...,q_(d-1) are nonzero multiples of
r,t r,...,t^(d-3) r, in reverse order. Their span is r times the
polynomials of degree at most d-3. Division by r leaves a
two-dimensional quotient with basis 1,t. If d=2k, the residues of
q_1,q_* are

\[
q_1\equiv c+t,\qquad q_*\equiv -1+\gamma c t,
\qquad c=(-1)^{k-1}\gamma^k.
\]

Their quotient determinant is 1+gamma^(d+1). If d=2k+1, their
residues are c t,-c, with c=1+(-1)^k gamma^(k+1), giving c^2.
The d-2 nonzero component multipliers contribute
gamma^((d-2)(d-1)/2) in magnitude. The basis
r,t r,...,t^(d-3) r,1,t contributes another gamma^(d-2), by its
leading coefficients. Multiplication gives (8).

Consequently gamma=2 works for every d>=4. The smaller choice
gamma=1 works unless d is congruent to 3 modulo 4. The exported
A78 witness uses gamma=1. The singularity of the original choice
at d=7 is an actual basis degeneracy, repaired by gamma=2; it is
not a failure of (1).

## 3. Converting the whole pencil to convolution

Coefficient comparison in (7) gives

\[
D_1c_0=0,\qquad D_1c_k=D_0c_{k-1}\ (1\le k<d),\qquad
D_0c_{d-1}=0.
\tag{9}
\]

Since C is nonsingular and D_0 has rank d-1, the square matrix

\[
S=(D_0c_0\ \cdots\ D_0c_{d-2})
\]

is nonsingular. Set L=S^(-1), P=L P^old, and Q=C^T V, treating
lists of polynomials as column vectors. Equations (9) imply

\[
L D_0 C=(I_{d-1}\ \ 0),\qquad
L D_1 C=(0\ \ I_{d-1}).
\]

Equivalently, with 0<=mu<d-1, 0<=lambda<2, and 0<=nu<d,

\[
h_\lambda(P_\mu Q_\nu)=\delta_{\nu,\mu+\lambda}.
\tag{10}
\]

This proves the full pencil equivalence over the rationals. No
classification theorem for matrix pencils is needed. All d second
short vectors Q remain in span(V), which will also eliminate mixed
coefficients with the core.

## 4. The cyclic tensor maps

For clarity, source coordinates are ordered

\[
X=(i,t,s),\qquad Y=(j,p,u),\qquad Z=(v,q,r),
\]

with original tensor terms

\[
X_{i,p+q,s}Y_{j,p,r+s}Z_{i+j,q,r},
\quad i,p,r<a,\quad j,q,s<a+1.
\tag{11}
\]

All coordinates use increasing lexicographic order. For the core,
write n=2d and I=(alpha_I,beta_I), J=(alpha_J,beta_J),
K=(alpha_K,beta_K), where alpha is in {0,1} and beta is in
{0,...,d-1}. The row maps are

\[
\begin{aligned}
X^{\rm core}_{I,J}(i,t,s)
 &=U_{\alpha_I}(i)R_{\alpha_J,\beta_I}(t)V_{\beta_J}(s),\\
Y^{\rm core}_{J,K}(j,p,u)
 &=V_{\beta_K}(j)U_{\alpha_J}(p)R_{\alpha_K,\beta_J}(u),\\
Z^{\rm core}_{K,I}(v,q,r)
 &=R_{\alpha_I,\beta_K}(v)V_{\beta_I}(q)U_{\alpha_K}(r).
\end{aligned}
\tag{12}
\]

Here a polynomial or functional evaluated at an index means its
coefficient at that index. Core rows use matrix-index order.

The smaller A(2,d-1) coordinates are
X'=(i',t',s'), Y'=(j',p',u'), Z'=(v',q',r'), with i',p',r'<2,
j',q',s'<d-1, and t',u',v'<d. Their row maps are

\[
\begin{aligned}
X'_{i',t',s'}(i,t,s)&=P_{s'}(i)h_{i'}(t)Q_{t'}(s),\\
Y'_{j',p',u'}(j,p,u)&=Q_{u'}(j)P_{j'}(p)h_{p'}(u),\\
Z'_{v',q',r'}(v,q,r)&=h_{r'}(v)Q_{v'}(q)P_{q'}(r).
\end{aligned}
\tag{13}
\]

The three applications of (10) make (13) exactly A(2,d-1), in
the coordinate convention (11). Stack the rows of (13) after the
core rows (12).

Every mixed coefficient vanishes. With one residual row and two
core rows, its long h functional pairs a core U and V. With two
residual rows and one core row, one of the residual long h
functionals pairs a core U and a residual Q. Both pairings vanish
because h annihilates U times V and Q belongs to span(V). This
covers all cyclic placements and proves (1).

## 5. Exact controls and exported witness

The verifier first checks both local inverse identities, the
polynomial kernel identity, the determinant formula, and every
entry of (10). It then applies all three integer numerator maps
to the entire original source tensor, retaining exact Python
integer coefficients, and compares the resulting sparse tensor
with the complete target. There is no floating-point zero test.

| Source | gamma | Target | Target dimension | Target terms | Residual row denominator |
|---|---:|---|---:|---:|---:|
| A(5,6) | 1 | M8 plus A(2,3) | 88 | 728 | 2 |
| A(6,7) | 1 | M10 plus A(2,4) | 140 | 1,512 | 2 |
| A(7,8) | 1 | M12 plus A(2,5) | 204 | 2,728 | 2 |
| A(8,9) | 2 | M14 plus A(2,6) | 280 | 4,472 | 960 |

Additional local identities and determinants are checked at every
a from 5 through 11 using gamma=2. These finite controls support
the code implementation; the argument above proves the all-size
statement.

Files:

- `parity_structure_full_residual.py`: construction and exact verifier, using NumPy and Python's standard fractions module.
- `parity_structure_full_residual_certificate.json`: completed exact checks and counts.
- `parity_structure_full_residual_a78_maps.npz`: A,B,C and x,y,z aliases, exact A_numerator,B_numerator,C_numerator arrays, row_denominators, and all local bases.
- `parity_structure_full_residual_a78_sparse.json`: the same complete A78 witness as compact sparse integer rows and exact row denominators.
- `parity_structure_full_residual_stdlib.py`: a complete coefficient replay using only Python's standard library, including rejection of a deliberately tampered map.
- `parity_structure_full_residual_stdlib_certificate.json`: that replay's recorded coverage and tamper result.

For the A78 export, rows 0 through 143 are M12. Rows 144 through
203 are A(2,5), in the source convention (11). Each numerator
matrix has 2,624 nonzero entries, all 1 or -1. The corresponding
row denominator is one on the core and two on the residual.
The floating A,B,C arrays are exactly representable halves in
this export, but the numerator and denominator arrays remain
the authoritative rational certificate.

Reproduce from the repository root:

```
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_full_residual.py
```

The exported A78 witness can also be replayed without NumPy:

```
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_full_residual_stdlib.py
```

The certificate explicitly records that no smaller exponent is
established. This family strengthens the retained source structure
of a verified restriction, without asserting the still-missing
larger matrix multiplication target.
