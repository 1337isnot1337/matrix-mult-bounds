# Equality at twice the minimum slice rank

October 21, 2026. This note proves a containment for ordinary source slices.
It does not claim a tensor restriction, a singular-degeneration exclusion,
or a smaller matrix multiplication exponent. The proof was developed in
this generating session; no external independent review or formal
verification is claimed.

## Statement

Let a,b>=3, d=a+b-2, and let F be a slice of A(a,b), in the conventions of
[`polynomial_rank_locus.md`](polynomial_rank_locus.md). Write

\[
f_k(x,z)=\sum_{i<a,\,s<b}F_{i,k,s}x^iz^s,
\qquad B_F=(f_{p+q})_{0\le p<a,\,0\le q<b}.
\]

If the full slice matrix M_F has rank at most 2ab, then there is a
**constant** subscheme Z of P^1 of length at most two such that every
long-coordinate sequence

\[
(F_{i,0,s},\ldots,F_{i,d,s})
\]

lies in the vector span H_Z of its image under the degree-d rational
normal curve. Thus

\[
F\in \mathbb C^{a}\otimes H_Z\otimes\mathbb C^{b}.
\tag{1}
\]

For length two, H_Z is either the span of two coherent evaluation vectors
or an evaluation vector and its first derivative at one point. The
support and recurrence are constants, independent of x and z. A point
at infinity is allowed. This is a necessary condition only: arbitrary
choices of the biform coefficients in (1) need not have rank at most 2ab.

The existing strict-inequality theorem supplies the case where B_F has
rank one. The argument below supplies the equality case of Hankel rank
two. Its key step uses the polynomial rank bound in both variable orders.

## 1. Equality in a polynomial coefficient map

Let L be a field, let C(t) be a polynomial matrix with column rank r over
L(t), and let T be a positive integer. Apply C(t) to vectors whose entries
have degree below T, keeping every output coefficient. Denote this finite
L-linear coefficient map by Phi_T.

Then

\[
\operatorname{rank}_L\Phi_T\ge Tr.
\]

Equality holds if and only if every column of C is an L-linear
combination of any selected r columns independent over L(t).

To prove the forward implication, select independent columns c_1,...,c_r.
Their multiples by polynomials of degree below T have dimension Tr. Under
equality they span the whole image of Phi_T. For every other column c,
there are polynomials p_j,q_j of degree below T with

\[
c=\sum_jp_j(t)c_j,
\qquad t^{T-1}c=\sum_jq_j(t)c_j.
\]

Independence over L(t) gives q_j=t^(T-1)p_j. The degree bound on q_j
forces every p_j to be constant, including when T=1. The converse follows
because constant column combinations do not enlarge the image, and the
chosen r columns still give an injective Tr-dimensional input space.
No output truncation is permitted in this lemma.

## 2. Both inner coefficient maps attain equality

Put r=rank_(C(x,z)) B_F. The proof in `polynomial_rank_locus.md` gives

\[
\operatorname{rank}M_F\ge b\rho\ge ab r,
\tag{2}
\]

where rho is the rank over C(x) of the full coefficient map

\[
(v_q(z))_{q<b}\longmapsto
\left(\sum_{q<b}f_{p+q}(x,z)v_q(z)\right)_{p<a},
\qquad \deg v_q<a.
\tag{3}
\]

For clarity, reversing the variable order gives another full coefficient
map, not an assumed symmetry of a rectangular matrix. Define J(z) by

\[
J(z)_{(j,p),(H,q)}
=\sum_{s=0}^{b-1}F_{H-j,p+q,s}z^s,
\]

with j<b, p<a, H<a+b-1 and q<b. Terms with H-j outside [0,a) are zero.
Multiplication by J on vector polynomials of degree below a is exactly
M_F: the coefficient from input (H,q,r) to output (j,p,L) is
F_(H-j,p+q,L-r). Its transpose J^T is the coefficient map over C(z)

\[
(u_p(x))_{p<a}\longmapsto
\left(\sum_{p<a}f_{p+q}(x,z)u_p(x)\right)_{q<b},
\qquad \deg u_p<b.
\tag{4}
\]

If sigma=rank_(C(z)) J, the same two injections therefore give

\[
\operatorname{rank}M_F\ge a\sigma\ge ab r.
\tag{5}
\]

Suppose now r=2 and rank M_F<=2ab. Both chains are equalities:
rho=2a and sigma=2b. Applying Section 1 to (3) shows that every column
of B_F is a C(x)-linear combination of two independent columns; the
combination coefficients are independent of z. Applying it to (4) shows
that every row of B_F is a C(z)-linear combination of two independent
rows; those coefficients are independent of x.

These are statements about polynomial coefficient maps. No factorization
of joint row or column supports of biform convolution matrices is used.

## 3. A constant shear makes the leading Hankel minor nonzero

Work temporarily over K=C(x,z). For any constant lambda in C, set

\[
f'_k=\sum_{j=k}^{d}\binom{d-k}{j-k}\lambda^{j-k}f_j.
\tag{6}
\]

This upper triangular change of the long coordinates is invertible. Let
S_n(lambda) have rows and columns numbered 0,...,n-1, with entry

\[
(S_n)_{p,j}=
\begin{cases}
\binom{n-1-p}{j-p}\lambda^{j-p},&j\ge p,\\
0,&j<p.
\end{cases}
\]

The binomial convolution identity gives

\[
B_{F'}=S_a B_F S_b^{\mathsf T}.
\tag{7}
\]

The same constant block row and block column operations act on the full
slice matrices, whose (p,q) blocks are the biform matrices R(f_(p+q)).
Consequently both the Hankel rank and the full slice rank are preserved.
The x,z degree bounds are also preserved. Thus Section 2 applies to F'.

There is some constant lambda for which

\[
\Delta=f'_0f'_2-(f'_1)^2\ne0.
\tag{8}
\]

Indeed, put G(t)=sum_(k=0)^d binom(d,k) f_k t^k. As functions of lambda,
the three entries in (8) are G, G'/d, and G''/[d(d-1)]. If Delta vanished
identically, then

\[
dGG''-(d-1)(G')^2=0.
\]

Over an algebraic closure of K, a root of G of multiplicity e would give
the leading coefficient e(e-d) in this identity. Hence every root has
multiplicity d. Since deg G<=d, G is a scalar multiple of a d-th power
of a linear form, or is constant. Its weighted coefficient sequence has
Hankel rank one, contradicting r=2. Therefore Delta is a nonzero
polynomial in lambda over K. It cannot vanish at every constant in the
infinite field C. This proves (8), including cases initially supported
only at the two endpoints of the long sequence.

## 4. One recurrence, independent of both variables

Replace F by F' and omit the primes. The leading two columns and rows of
B_F are independent by (8). Section 2 supplies c_0,c_1 in C(x) such that

\[
\text{column}_2=c_0\text{column}_0+c_1\text{column}_1.
\]

The first two entries determine them uniquely through

\[
\begin{pmatrix}f_0&f_1\\f_1&f_2\end{pmatrix}
\binom{c_0}{c_1}=\binom{f_2}{f_3}.
\tag{9}
\]

The corresponding relation for row 2 has coefficients in C(z) and gives
the identical system (9). Uniqueness and
C(x) intersection C(z)=C inside C(x,z) imply

\[
c_0,c_1\in\mathbb C.
\]

The Hankel relations then propagate to every index:

\[
f_{k+2}=c_0f_k+c_1f_{k+1},\qquad 0\le k\le d-2.
\tag{10}
\]

Here is an explicit propagation argument. Column 2 gives (10) for
0<=k<a. For each row index 2<=p<a, subtract c_0 times row p-2 and c_1
times row p-1 from row p. The resulting row remains in the two-dimensional
row space of B_F. Its first two entries vanish by the already established
recurrences. Projection of that row space to its first two entries is
injective, by (8), so the whole row vanishes. Letting p run from 2 to a-1
and the column index q from 0 to b-1 covers every k from 0 through d-2.

The scalar solution space of (10) has dimension two. If the roots of
t^2-c_1t-c_0 are distinct, it is spanned by the two evaluation sequences
(r^k) and (s^k). For a repeated root r, it is spanned by (r^k) and its
derivative (k r^(k-1)), interpreted polynomially also at r=0. Undoing the
constant shear transforms this into a constant secant or tangent space,
possibly involving infinity. Comparing coefficients of x^i z^s in (10)
proves (1).

Finally, rank M_F<=2ab implies r<=2 by the general polynomial rank bound.
When r=1, the strict-rank classification gives a single constant coherent
factor; when r=0, F=0. This completes the claimed containment.

## 5. Scope and finite checks

The polynomial-multiplication equality is essential. A Hankel symbol of
rank two alone can have a variable recurrence. For A(5,6), the sequence

\[
f_{2j}(x,z)=x^j\quad(0\le j\le4),\qquad f_{2j+1}=0
\]

has recurrence f_(k+2)=x f_k and symbolic Hankel rank two. Its full slice
rank over Q is 75, strictly above 60. The two equality conditions fail
to hold simultaneously, as they must.

`parity_structure_equality.py` checks rational slice ranks, both
intermediate polynomial-matrix ranks, constant recurrences, and the
endpoint shear on explicit examples. These finite checks do not replace
the proof. A separate line-family argument is needed to infer a common
H_Z for a whole lifted target block. No such consequence is assumed in
this note.
