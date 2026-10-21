# Mixed middle modules do not repair the embedded Q(5,4) boundary chart

## Scope

Work over a field and write `P_d` for polynomials of degree at most d.
Let U,V be four-dimensional subspaces of P_4 and W a two-dimensional
subspace of P_3. Let H be a four-dimensional subspace of P_3 tensor W.
Assume both multiplication maps

\[
V\otimes W\longrightarrow P_7,
\qquad U\otimes H\longrightarrow P_7\otimes W
\tag{1}
\]

are isomorphisms. Their duals give the ordinary restriction
Q(5,4) to M(4,4,4) described below. H need not be a tensor product.

Embed these long-leg maps in Q(6,4). Keep their old convolution columns
0 through 7, but allow arbitrary images of all four new B columns
B_(y,8) and all four new C columns C_(8,v) in the old 16-dimensional
target supports. Then the first-leg map, before applying any A map,
has rank at least 35.

Consequently these leading maps cannot extend to M(5,4,5) by any
finite-order Laurent map on A and regular maps on B and C whose new
outer target modes vanish at the leading order. The saturated-slice
dimension argument in `outer_product_boundary.md` requires that leading
first-leg rank be at most 27.

This statement concerns the specified family. In particular, it does
**not** address four-dimensional U,V in P_5, arbitrary leading maps,
or arbitrary degenerations of Q(6,4). It gives no improvement of omega.
The determinant lemma received a same-session agent audit; no external
mathematical review is claimed.

## The exact M4 maps

Use bases U_h, V_i, W_b, and H_j, with h,i,j in {0,1,2,3} and b in
{0,1}. Write H_j(y,b) for its coefficient of t^y tensor W_b. Let

\[
L^B_{i,b;s},\qquad L^C_{h,j;z,b}
\]

be the dual bases to the two product bases in (1). The local maps are

\[
A_{p,q}\mapsto\sum_{i,h}U_h(p)V_i(q)a_{i,h},
\]

\[
B_{y,s}\mapsto\sum_{i,j,b}H_j(y,b)L^B_{i,b;s}b_{i,j},
\]

\[
C_{z,v}\mapsto\sum_{h,j,b}L^C_{h,j;z,b}W_b(v)c_{j,h}.
\tag{2}
\]

Substitute these into
Q(5,4) = sum_(p,q<5;y,v<4) A_(p,q) B_(y,q+v) C_(p+y,v).
The q,v contraction uses the first dual identity in (1), leaving
the p,y contraction of U_h H_j against L^C. That second contraction
is the second dual identity. The result is exactly
sum_(i,j,h<4) a_(i,h) b_(i,j) c_(j,h).

## A polynomial-matrix lemma

Regard H(t) as a 4 by 2 polynomial matrix, with row j giving H_j(t),
and let H_3 be its coefficient of t^3. Surjectivity of the second map
in (1) forces H_3 to have rank two: its degree-seven output must cover
the two-dimensional coefficient space W.

Choose a constant rank-two quotient pi: F^4 to F^2 with kernel
image(H_3). Then

\[
F(t)=\pi H(t)
\]

is a 2 by 2 polynomial matrix of degree at most two. We claim
det F(t) is a nonzero polynomial.

If det F(t) were identically zero, F would have a nonzero polynomial
left kernel r(t)^T of degree d at most two. For rank one, take the
two-entry syzygy of a nonzero column; if F is zero, take a constant
vector. Set R(t)=pi^T r(t). Then R is nonzero,
H(t)^T R(t)=0, and its four components lie in the span of two scalar
polynomials r_1 and r_2.

Write U=ker ell inside P_4. For h in P_(4-d), the conditions
ell(h R_i)=0 for all four components impose at most two linear
conditions: they are linear combinations of ell(h r_1)=0 and
ell(h r_2)=0. But dim P_(4-d)=5-d is at least three. Some nonzero
h satisfies these conditions, and hR is a nonzero element of U^4
annihilated by H(t)^T. This contradicts injectivity in (1).

## A projection retaining all 36 old source directions

On B apply id_(F^4) tensor pi. This kills every old B_(3,s) image.
On C quotient by the images of C_(z,3), z=0,...,7. The latter span
an eight-dimensional space because L^C is invertible and the vector
(W_0(3),W_1(3)) is nonzero. This vector is nonzero since the first
map in (1) reaches degree seven.

After identifying this C quotient with P_7, there is a nonzero
w in W with degree at most two for which

\[
C_{z,v}\longmapsto w(v)e_z.
\]

Define u_q in F^4 tensor F^2 by

\[
(u_q)_{i,b}=\sum_{v=0}^3 w(v)L^B_{i,b;q+v},\qquad 0\le q<6.
\]

These six vectors are independent: they are the invertible dual
coordinates of the independent polynomials t^q w(t) in P_7.

For an A-input matrix X, the projected old source is polynomial
matrix multiplication by F(t), separately on each i component, applied
to

\[
\sum_{p,q=0}^5 X_{p,q}t^p u_q.
\tag{3}
\]

There is no truncation: its degree is at most 5+2=7. Multiplication
by F(t) is injective over F[t] because det F(t) is nonzero. Expression
(3) is injective in X because the u_q are independent. Thus the
projected zero-boundary first-leg map has rank 36.

## Arbitrary new boundary columns change only one projected slice

A new B column can occur only when q=5 and v=3. If its accompanying
C column is old, the C quotient kills it. Similarly a new C column
requires p=5,y=3, and the B quotient kills its accompanying old
B column. The only surviving modification is therefore the product
of the new B_(3,8) and C_(8,3) images in the A_(5,5) slice.

The projected first-leg map is a rank-at-most-one update of an
injective 36-dimensional map. Its rank is at least 35, proving the
stated result. This is a restriction on the leading chart, not a
general border-rank obstruction.

## Exact finite controls

`mixed_middle_boundary.py` uses the nonproduct integer middle space

\[
H=(1\otimes W_0,\ (t+2t^2)\otimes W_0+1\otimes W_1,
       t^3\otimes W_0,\ t^3\otimes W_1)
\]

with U=V=(t,t^2,t^3,1-t^4), W=(1,t^3). Its product map is
unimodular. The script checks all 4,096 M4 coefficients, gives a
36 by 36 nonzero minor of the projected Q64 source, and checks that
a full integer assignment to all boundary columns changes only A55
after projection. It also supplies a deliberately singular F and
an explicit nonzero syzygy in U^4, checking the lemma's failure mode.
These controls illustrate the proof; they are not exhaustive searches.
