# Exact maximal-rank windows for the output-leg Koszul maps

Date: 2026-10-23. Owner-directed AI research. Written proof; no independent
mathematical review or priority claim.

This note is an additive necessary-condition result. It does not change the
frozen candidate input or establish a degeneration.

## 1. Statement and conventions

Work over the complex numbers. Let a,b,c be positive integers, put
n=a+b-1 and N=cn, and write

\[
S=c\odot_1\operatorname{Full}_{a,b}
 =\sum_{r=1}^{c}\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
   a_i\otimes b_{r,j}\otimes c_{r,i+j}.
\]

The spaces A,B,C have dimensions a,cb,N. The first space is shared; the
other two spaces are direct sums of the indicated blocks. For
0<=p<=N-1 define

\[
K_{C,p}(S):B^*\otimes\Lambda^pC\longrightarrow
A\otimes\Lambda^{p+1}C.
\tag{1}
\]

**Proposition.** The map (1) is injective for 0<=p<=a-1. It is
surjective for c(a-1)<=p<=N-1. In particular,

\[
\operatorname{rank}K_{C,p}(S)=
\begin{cases}
 cb\binom Np,&0\le p\le a-1,\\
 a\binom N{p+1},&c(a-1)\le p\le N-1.
\end{cases}
\tag{2}
\]

The formulas agree when the intervals overlap. Neither maximal-rank window
can be enlarged: the map has a nonzero kernel whenever a<=p<=N-1, and has
a nonzero cokernel whenever 0<=p<c(a-1). Assertions with empty degree
ranges are omitted.

These are elementary consequences of polynomial interpolation and
Vandermonde independence. The argument below proves the needed consequences
directly. It does not import an all-degree rank formula in the intervening
degrees.

## 2. An interpolation basis

Choose N pairwise distinct complex numbers t_(r,k), with 1<=r<=c and
1<=k<=n. In each output block use its Lagrange interpolation basis
e_(r,k). Polynomial multiplication then gives the exact decomposition

\[
S=\sum_{r=1}^{c}\sum_{k=1}^{n}
u_{r,k}\otimes v_{r,k}\otimes e_{r,k},
\quad
u_{r,k}=\sum_{i=0}^{a-1}t_{r,k}^{\,i}a_i,
\quad
v_{r,k}=\sum_{j=0}^{b-1}t_{r,k}^{\,j}b_{r,j}.
\tag{3}
\]

Indeed, evaluating a product of degrees at most a-1 and b-1 at n=a+b-1
distinct nodes determines it uniquely, which proves (3).

Every collection of at most a vectors u_(r,k) is independent. Within one
fixed block r, every collection of at most b vectors v_(r,k) is independent.
Both statements follow from the nonzero Vandermonde determinant: its
factors are differences of distinct nodes. The vectors e_(r,k) form a
basis of all of C.

Order these N output coordinates once. Write e_J for their ordered
exterior product over a subset J. Write I_r for the part of a subset I
in the r-th output block.

## 3. Injectivity in low degrees

An element of the domain of (1) has a unique expression

\[
x=\sum_{|J|=p}\beta_J\otimes e_J,
\qquad \beta_J\in B^*.
\]

If x is in the kernel, the coefficient of e_I for each (p+1)-element
subset I gives

\[
\sum_{s\in I}\epsilon(I,s)\,
u_s\,v_s(\beta_{I\setminus\{s\}})=0,
\tag{4}
\]

where each epsilon is the nonzero exterior sign. If p<=a-1, the vectors
u_s in (4) are independent. Consequently,

\[
v_s(\beta_J)=0
\quad\text{for every }s\notin J.
\tag{5}
\]

For a fixed J and a fixed block r there are at least

\[
n-|J_r|\ge n-p\ge b
\]

nodes outside J in that block. Their vectors v_s span B_r. Thus (5)
annihilates every B_r, and beta_J=0. This holds for every J, proving
injectivity.

## 4. Surjectivity in high degrees

Choose a nonzero volume form on C and put q=N-p-1. Exterior duality
identifies the transpose of (1), up to invertible identifications and
exterior signs, with

\[
L_q:A^*\otimes\Lambda^qC\longrightarrow
B\otimes\Lambda^{q+1}C,
\tag{6}
\]

using the same tensor (3) with A and B interchanged. Therefore (1) is
surjective if and only if (6) is injective.

Suppose p>=c(a-1). Then q<cb. Let

\[
y=\sum_{|J|=q}\alpha_J\otimes e_J,
\qquad\alpha_J\in A^*
\]

be in the kernel of (6). For any fixed J, the inequality |J|<cb ensures
there is a block r with |J_r|<=b-1. For each s in that block but outside
J, take I=J union {s}. The B_r component of the coefficient of e_I in
L_q(y)=0 is

\[
\sum_{t\in I_r}\epsilon(I,t)\,
v_t\,u_t(\alpha_{I\setminus\{t\}})=0.
\tag{7}
\]

There are at most b summands in (7), so the vectors v_t are independent.
The coefficient belonging to t=s must vanish:

\[
u_s(\alpha_J)=0.
\tag{8}
\]

This argument works for every s outside J in the chosen block. There are
at least n-(b-1)=a such nodes. Their u_s span A, so alpha_J=0. Since J
was arbitrary, (6) is injective. This proves the high-degree assertion.

The strict inequality q<cb is essential in this pigeonhole step. For the
new candidate it gives p>=40, rather than the weaker sufficient cutoff
p>=49 that would result from bounding q by c(b-1).

## 5. Sharpness

In the original coefficient basis, the B-slice selected by b_(1,0)^*
has C support

\[
C_0=\operatorname{span}\{c_{1,0},\ldots,c_{1,a-1}\}
\]

of dimension a. Whenever p>=a, choose a nonzero p-fold exterior product
w whose support contains C_0. Then b_(1,0)^* tensor w is nonzero, but
each term in (1) wedges a vector in C_0 into w and vanishes. Thus (1)
has nonzero kernel in every such degree within its range.

Likewise, the A-slice selected by a_0^* has C support

\[
C_1=\operatorname{span}
 \{c_{r,j}:1\le r\le c,\ 0\le j<b\},
\]

of dimension cb. Whenever q>=cb, the tensor a_0^* tensor w is a
nonzero kernel vector of (6) for any nonzero q-fold exterior product w
whose support contains C_1. This means (1) has nonzero cokernel whenever
p=N-q-1<c(a-1).

These explicit kernels also show why injectivity past degree a-1 or
surjectivity before degree c(a-1) cannot be assumed from dimension
counts alone.

## 6. Consequence for the frozen mixed-orientation candidate

For the source 10 Full(5,10), one has a=5,b=10,c=10,N=140. Hence

\[
\operatorname{rank}K_{C,p}(S)=
\begin{cases}
100\binom{140}{p},&0\le p\le4,\\
5\binom{140}{p+1},&40\le p\le139.
\end{cases}
\]

Any tensor of the same format (5,100,140) has rank at most these ambient
bounds. Therefore the frozen target automatically passes all C-leg Koszul
comparisons in degrees 0 through 4 and 40 through 139. Only degrees 5
through 39 remain to be compared on this leg.

The source is already noninjective at degree 5. In each individual
Full(5,10) block, the degree-five domain has dimension
10*binom(14,5)=20020 and the codomain has dimension
5*binom(14,6)=15015, giving a local kernel of dimension at least 5005.
For the ten source blocks these disjoint intrinsic domain pieces already
supply a kernel of dimension at least 50050. This lower bound on the
kernel is a warning against claiming full column rank in degree 5; it is
not the complete source rank calculation there.

All these conclusions concern necessary rank inequalities. A target
degeneration, a smaller matrix multiplication exponent, and the remaining
C-leg comparisons are not established by this note.

