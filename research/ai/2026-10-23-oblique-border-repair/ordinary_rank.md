# The correction core has ordinary rank seven

October 23, 2026. Owner-directed Codex research. Written proof with
exact integer checks of its explicit inputs. Separate checks in the same
session are not independent mathematical review. No historical priority
or exponent improvement is claimed.

## Statement

Let k be any field. Give A, B, and C the respective bases

\[
(u,v,w),\qquad (X,Z,a,\eta,y),\qquad(P,Q,R,S,T).
\]

Consider

\[
K=u(XP+ZQ)+v(aR+\eta S)
  +w(XQ+ZT+\eta R+yS+XR).
\tag{1}
\]

The ordinary tensor rank of K over k is exactly seven. The
[six-term integer polynomial degeneration and unit Koszul minor](proof.md)
give formal border rank exactly six in every characteristic, and usual
complex border rank exactly six. The present proof concerns ordinary
rank only; it does not prove optimal rank for any larger residual in
which K is embedded.

## 1. The upper bound and generic slice matrix

The following identity gives the seven-term upper bound over every
field:

\[
\begin{aligned}
K={}&(u+w)(X+Z)Q+uX(P-Q)+wZ(T-Q)\\
 &+(v+w)\eta(R+S)+v(a-\eta)R+w(y-\eta)S+wXR.
\end{aligned}
\tag{2}
\]

Use u,v,w also as the three independent polynomial variables that record
a generic contraction in the first leg. The corresponding B-by-C matrix
is

\[
M=
\begin{pmatrix}
u&w&w&0&0\\
0&u&0&0&w\\
0&0&v&0&0\\
0&0&w&v&0\\
0&0&0&w&0
\end{pmatrix}.
\tag{3}
\]

Its right and left kernel vectors over k(u,v,w) can be chosen as

\[
\rho=(w^2,-uw,0,0,u^2)^{\mathsf T},\qquad
\lambda=(0,0,w^2,-vw,v^2)^{\mathsf T}.
\tag{4}
\]

Direct multiplication verifies both kernel identities. The minor on
rows X,Z,a,eta and columns P,Q,R,S is u-squared times v-squared, so M
has generic rank four over every field.

The tensor is concise in B and C. For B, the coordinates uP, uQ, vR,
vS, and wS distinguish X,Z,a,eta,y. For C, the coordinates uX, uZ, va,
veta, and wZ distinguish P,Q,R,S,T. In particular every decomposition
has second- and third-leg factors spanning dimension five.

Concision excludes a decomposition with fewer than five terms. In a
five-term decomposition the second- and third-leg factor matrices would
be invertible 5-by-5 matrices. Multiplication by the diagonal matrix of
the five nonzero first factors would make M generically invertible,
contradicting (3). It remains to exclude rank six.

## 2. What a six-term decomposition would imply

Suppose

\[
K=\sum_{i=1}^6 \ell_i\,b_i c_i,
\tag{5}
\]

with every factor nonzero. Each ell_i is a nonzero linear form in u,v,w.
Let U and V be the 5-by-6 matrices whose columns are b_i and c_i.
Concision gives rank(U)=rank(V)=5. Choose nonzero column vectors

\[
p\in\ker U,\qquad q\in\ker V,
\]

which each span their one-dimensional kernel. Write

\[
D=\operatorname{diag}(\ell_1,\ldots,\ell_6),\qquad M=UDV^{\mathsf T},
\]

and let I and J be the supports of p and q.

### The right kernel determines the first factors on I

Since M rho=0, the vector D V-transpose rho lies in the k(u,v,w)-span
of p. There is a nonzero homogeneous cubic polynomial F such that

\[
\ell_i g_i=p_i F\quad(1\le i\le6),\qquad
g_i=c_i^{\mathsf T}\rho\in k[u,w]_2.
\tag{6}
\]

To see that F is a polynomial, choose any i with p_i nonzero and set
F=ell_i g_i/p_i. It is nonzero because V-transpose is injective and
rho is nonzero. If i is not in I, (6) gives g_i=0. If i is in I, then
g_i is nonzero and ell_i divides F.

The six g_i span the entire three-dimensional space k[u,w]_2. Indeed,
the c_i span C, while the map c to c-transpose rho has image spanned
by w-squared, -uw, and u-squared. Indices with proportional ell_i
give proportional g_i in (6). Thus the forms ell_i with i in I have
at least three distinct projective classes. Since each divides the
degree-three polynomial F, they have at most three classes. There are
exactly three, and F is a nonzero scalar times their product.

Every one of these three distinct forms divides some g_j: choose j
corresponding to one of the other forms. Since that g_j belongs to
k[u,w], its linear factors have zero v coefficient. Hence all first
factors indexed by I lie in span(u,w), and there are exactly three
distinct projective first factors among them.

Also, if i is not in I, then c_i-transpose rho=0 as a polynomial.
The three coefficient vectors of rho span the P,Q,T coordinate
subspace of the dual of C. Therefore

\[
i\notin I\quad\Longrightarrow\quad c_i\in C_1:=\operatorname{span}(R,S).
\tag{7}
\]

### The left kernel gives the analogous information on J

Apply the same argument to lambda-transpose M=0. There is a nonzero
homogeneous cubic G with

\[
\ell_i h_i=q_i G,\qquad
h_i=b_i^{\mathsf T}\lambda\in k[v,w]_2.
\tag{8}
\]

Thus the first factors indexed by J have exactly three distinct
projective classes, all in span(v,w), and

\[
i\notin J\quad\Longrightarrow\quad b_i\in B_0:=\operatorname{span}(X,Z).
\tag{9}
\]

### Only two support patterns are possible

For every index in I intersect J, ell_i lies in both span(u,w) and
span(v,w), so it is a nonzero multiple of w. Moreover, from
V-transpose rho=F D-inverse p and Vq=0 we obtain

\[
q^{\mathsf T}D^{-1}p
 =\sum_{i\in I\cap J}\frac{p_iq_i}{\ell_i}=0.
\tag{10}
\]

The intersection cannot have exactly one index: its single summand
would be nonzero. If the intersection is nonempty, it consequently
has at least two indices. Each of I and J needs two additional,
distinct first factors other than w. These lie outside the intersection.
There are only six indices in total. Therefore exactly one of the
following holds:

1. I and J are disjoint, each has three elements, and their union is
   all six indices.
2. I intersect J has two elements with first factors proportional to
   w; I minus J and J minus I each have two elements; their union is
   all six indices. The first factors on each of the two exclusive
   pairs are distinct and are not proportional to w.

We now rule out both cases.

## 3. Disjoint supports force an impossible block splitting

Write

\[
B=B_0\oplus B_1,\quad B_1=\operatorname{span}(a,\eta,y),\qquad
C=C_0\oplus C_1,\quad C_0=\operatorname{span}(P,Q,T).
\]

Assume I and J are disjoint. Equation (9) gives b_i in B_0 for i in I.
The relation p gives a nontrivial dependence among these three b_i.
The second-leg factors for indices in J comprise at most a
three-dimensional subspace. Since all six factors span B, it follows
that the b_i with i in I span exactly B_0, and the b_j with j in J
span a three-dimensional complement B-prime to B_0. Likewise, (7)
and the relation q imply that the c_j with j in J span C_1, and the
c_i with i in I span a three-dimensional complement C-prime to C_1.

These complements are graphs of constant linear maps

\[
L:C_0\longrightarrow C_1,\qquad N:B_1\longrightarrow B_0.
\]

The tensor from indices in I belongs to A tensor B_0 tensor C-prime,
and the tensor from indices in J belongs to A tensor B-prime tensor
C_1. Projection onto the B_0-by-C_0 block of (1) gives

\[
T_1=uXP+uZQ+wXQ+wZT,
\]

while projection onto the B_1-by-C_1 block gives

\[
T_2=vaR+v\eta S+w\eta R+wyS.
\]

Consequently the mixed B_0-by-C_1 block of K must equal

\[
(\operatorname{id}_A\otimes\operatorname{id}_{B_0}\otimes L)T_1
 +(\operatorname{id}_A\otimes N\otimes\operatorname{id}_{C_1})T_2.
\tag{11}
\]

For any tensor in this mixed block, define the linear functional

\[
\mathcal L(T)=[wXR]T-[uZR]T-[vXS]T,
\tag{12}
\]

where brackets denote coefficient extraction. The first tensor in
(11) has equal wXR and uZR coefficients, both the R coefficient of
L(Q), and has zero vXS coefficient. The second has equal wXR and
vXS coefficients, both the X coefficient of N(eta), and has zero
uZR coefficient. Thus (11) has L-functional zero.

The actual mixed block of K is wXR, on which (12) equals one. This
is a contradiction in every characteristic.

## 4. Shared w factors leave a matrix of rank at least three

Consider the second support pattern. Absorb nonzero scalars into the
second or third factors, so the first factors in I minus J become

\[
u+\alpha_1w,\quad u+\alpha_2w,
\]

the first factors in J minus I become

\[
v+\beta_1w,\quad v+\beta_2w,
\]

and the two shared first factors are w.

Only the two I-minus-J terms contribute to the u slice. Their two
rank-one B-by-C matrices therefore sum to XP+ZQ, a matrix of rank
two. In any two-term expression for a rank-two matrix, the two column
factors span its column space and the two row factors span its row
space. Hence these two terms have second factors in span(X,Z) and
third factors in span(P,Q). Their contribution to the w slice is
also supported in span(X,Z) tensor span(P,Q).

Similarly, only the two J-minus-I terms contribute to the v slice.
Their sum is aR+eta S. Their second factors belong to span(a,eta)
and their third factors belong to span(R,S). Their contribution to
the w slice has this same support.

After subtracting these four contributions from the w slice of (1),
the remaining matrix must be a sum of the two rank-one matrices
whose first factors are w. However, its submatrix on rows X,Z,y
and columns R,T,S is

\[
\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}.
\tag{13}
\]

The I-minus-J corrections vanish in these columns; the J-minus-I
corrections vanish in these rows. Thus the residual matrix has rank
at least three, and cannot be a sum of two rank-one matrices.
This is again a contradiction in every characteristic.

Both possible six-term support patterns are impossible. Equation (2)
therefore proves R(K)=7 over every field.

## Scope and verification

This proof uses the displayed kernel identities, concision, polynomial
factorization in k[u,v,w], and elementary matrix ranks. No classification
of matrix spaces or small tensors is assumed. Its statements apply to
ordinary rank over the chosen field, including extension fields.

The distinction between the isolated core and the full residual is
essential. The argument proves R(K)=7, but it supplies no additive
lower bound for a sum of embedded cores and gives no lower bound of
nineteen for the full n=6 residual. Its role is to explain the exact
rank versus border rank separation in the certified local construction.


The standard-library verifier reconstructs all 75 coefficients of (2),
both polynomial kernel identities, the generic slice minor, two concise
flattening minors, all twelve basis images in (11), and (13). These are
the explicit finite inputs to the proof. The argument in Sections 2-4,
not a finite search over decompositions, proves the lower bound.

```bash
python research/ai/2026-10-23-oblique-border-repair/ordinary_rank.py
python -m unittest discover -s tests -p test_oblique_core_ordinary_rank.py -v
```

`ordinary-rank-certificate.json` records these exact checks. The original
source maps and four pinned source files remain unchanged.
