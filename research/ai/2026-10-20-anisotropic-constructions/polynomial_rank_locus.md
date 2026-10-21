# The full locus below twice the minimum slice rank

October 21, 2026. This is a new argument developed in this generating
session. A second agent checked the polynomial-multiplication proof and
the three-leg consequence; no external independent review or formal
verification is claimed. The target exclusions below concern ordinary
linear restrictions. They do not exclude singular degenerations.

## Statement

Let a,b>=2, m=a+b-1 and N=abm. For a first-leg slice F of A(a,b), write

\[
 f_k(x,z)=\sum_{i=0}^{a-1}\sum_{s=0}^{b-1}F_{i,k,s}x^i z^s,
 \qquad
 B_F(x,z)=(f_{p+q}(x,z))_{0\le p<a,\ 0\le q<b}.
\]

The following statements hold over any field for the rank calculations;
the geometric restriction statements below are over C.

1. If r is the rank of B_F over the rational function field in x,z, then

   \[
   \operatorname{rank}M_F\ge ab\,r.                 \tag{1}
   \]

2. A nonzero slice has rank below 2ab if and only if

   \[
   F_{i,k,s}=g_{i,s}h_k,
   \qquad \operatorname{rank}(h_{p+q})=1.           \tag{2}
   \]

   Every slice in (2) has rank at most min(a,b)m<2ab. Its projective
   locus is P^(ab-1) times the degree-(m-1) rational normal curve.

3. Every nonzero linear space of slices lying wholly below rank 2ab
   has one fixed h in (2).

The previous minimum-rank gap distinguished ab from ranks at least
ab+min(a,b). The present statement describes the whole larger locus
below 2ab. It also identifies a sharp threshold: choosing separable g
and a rank-two scalar Hankel h gives slice rank exactly 2ab.

## Two polynomial multiplication injections

The source coefficient formula gives

\[
 (M_F)_{(j,p,L),(H,q,r)}=F_{H-j,p+q,L-r},
\]

with coefficients outside the index ranges equal to zero. The first
transpose multiplication sends an input array u_(j,p,L) to

\[
 v_{H,q,r}=\sum_{j,p,L}F_{H-j,p+q,L-r}u_{j,p,L}.
\]

Represent u_(p,L)(x)=sum_j u_(j,p,L)x^j, of degree below b. This is
multiplication by the polynomial matrix K(x), whose rows are (q,r),
columns are (p,L), and entries are

\[
 K(x)_{(q,r),(p,L)}
 =\sum_{i=0}^{a-1}F_{i,p+q,L-r}x^i.
\]

There are ab rows and am columns. The outputs have degree below m,
so this is exactly the finite coefficient map M_F^T, not a truncation
with discarded high-degree terms. Choose rho columns of K that are
linearly independent over the rational function field in x. Restricting
the input to arbitrary degree-below-b polynomials in these rho columns
is injective. Therefore

\[
 \operatorname{rank}M_F\ge b\rho,
 \qquad \rho=\operatorname{rank}_{\mathbb C(x)}K.    \tag{3}
\]

Now work over the field C(x). The transpose K(x)^T is itself the full
coefficient map for polynomial multiplication

\[
 (v_q(z))_{q<b}\longmapsto
 \left(\sum_{q<b}f_{p+q}(x,z)v_q(z)\right)_{p<a},
 \qquad \deg v_q<a.
\]

The output degrees are below m. Indeed, the coefficient from input
(q,r) to output (p,L) is f_(p+q,L-r)(x), exactly the displayed entry
of K. Select r columns of B_F independent over C(x,z). The vector
polynomials supported on those columns, each of degree below a, form
an ar-dimensional subspace on which this multiplication is injective.
Consequently rho>=ar. Combining with (3) proves (1).

Both injections use independent columns over a rational function field.
They do not assume that a nonzero polynomial is a unit or that a finite
coefficient map has the same rank as its polynomial symbol.

## Rank-one Hankel symbols force a constant ratio

If a nonzero slice has rank below 2ab, (1) forces B_F to have rank one.
This is a Hankel matrix over the field C(x,z).

If f_0=0 and k is the first nonzero index with k<m-1, select consecutive
rows and columns whose upper-left entry has index k-1. Such a choice
exists because 0<=k-1<=a+b-4. The resulting minor is

\[
 \det\begin{pmatrix}0&f_k\\f_k&f_{k+1}\end{pmatrix}
 =-f_k^2\ne0,
\]

a contradiction. Thus in this case only f_(m-1) is nonzero. This is
the coherent endpoint at infinity.

If f_0 is nonzero, the rank-one Hankel identities imply

\[
 f_k=f_0 R^k\quad(0\le k\le m-1),\qquad R=f_1/f_0.
\]

The case R=0 is the other coherent endpoint. Otherwise write R=P/Q
with coprime nonzero polynomials in C[x,z]. The last identity implies
Q^(m-1) divides f_0. Write f_0=GQ^(m-1); then
f_(m-1)=GP^(m-1). All these polynomials have x-degree at most a-1 and
z-degree at most b-1. But m-1=a+b-2 exceeds each of those two bounds.
Since degrees in either variable add under multiplication of nonzero
polynomials, P and Q must be constant in both variables. Thus R is a
constant and (2) follows.

Conversely, if F=g tensor h and h has Hankel rank one, its block matrix
is the tensor product of the scalar Hankel matrix of h with the biform
coefficient matrix R(g) from `slice_rank_gap.md`. The latter has format
(bm,am), so its rank is at most min(a,b)m<2ab. This proves statement 2.
No change of basis or algebraic closure is needed for this classification.

## Linear spaces have one coherent factor

View (2) as decomposable vectors g tensor h. Suppose a projective line
in this locus contained two different coherent factors h and h'. If
the corresponding g and g' were linearly independent, their sum would
not be decomposable. If g and g' were proportional, the whole line
spanned by h and h' would have to lie in the rational normal curve.
That curve has degree m-1>=2 and contains no projective line. Both
possibilities are impossible. Hence every line has fixed h, and so does
every linear space in the locus. A one-dimensional vector space has a
fixed h trivially.

## Ordinary matrix-target consequence

Suppose ordinary linear maps take A(a,b) to a concise target. Each leg
map is surjective, so its transpose injects the target dual space into
the source slice space. If the other two source leg maps have kernels
of dimensions k_Y,k_Z, every lifted slice satisfies

\[
 \operatorname{rank}(\text{source lift})
 \le \operatorname{rank}(\text{target slice})+k_Y+k_Z. \tag{4}
\]

For a rectangular block M(l,h,n), every rank-one matrix parameter in
its first dual space has target slice rank n. If

\[
 n+k_Y+k_Z<2ab,                                     \tag{5}
\]

its Segre variety of rank-one parameters maps into the locus (2).
Every ruling line has fixed coherent h. The two families of rulings
connect this Segre variety, so h is constant on the entire variety and
on its linear span. The whole lh-dimensional block dual space then
fits in the ab-dimensional space of g coefficients. Thus (5) requires
lh<=ab.

For a single rectangular matrix target with lh>ab, this yields

\[
 n(l+h-1)\le 2N-2ab,                                \tag{6}
\]

and the two cyclic analogues when their block leg dimensions exceed ab.
All four previously surviving single-block A(5,5) targets in the saved
ordinary frontier fail this strengthened condition.

## A three-leg consequence for direct sums

There is a second consequence that does not use joint row or column
support estimates. Let E_X,E_Y,E_Z be nonzero lifted target dual
subspaces, each of whose source slices has rank below 2ab. By statement
3, their long-coordinate factors h_X,h_Y,h_Z are fixed. Factor the
three rank-one Hankel matrices as

\[
 h_X(p+q)=a_p b_q,\quad
 h_Y(r+s)=c_r d_s,\quad
 h_Z(i+j)=e_i f_j.
\]

The original six-index source contraction on these subspaces is

\[
 \begin{aligned}
 &\sum_{i,j,p,q,r,s}
    G_X(i,s)G_Y(j,p)G_Z(q,r)
    a_p b_q c_r d_s e_i f_j\\
 &\quad=
 \left(\sum_{i,s}G_X(i,s)e_i d_s\right)
 \left(\sum_{j,p}G_Y(j,p)f_j a_p\right)
 \left(\sum_{q,r}G_Z(q,r)b_q c_r\right).
 \end{aligned}                                      \tag{7}
\]

Its tensor rank is at most one. Thus a target subtensor of rank greater
than one cannot have all three lifted dual spaces below the threshold.

In a direct sum of square matrix targets, let D be the common total
leg dimension and let B be the common leg dimension of any selected
subsum. Every slice of that subsum has rank at most B. With k=N-D,
equation (4) gives the useful necessary condition

\[
 B+2k\ge2ab\qquad\text{for every selected subsum with }B\ge2.
                                                               \tag{8}
\]

For A(5,5) to M14 plus M3, D=205, k=20 and the M3 component has B=9.
Its bound is 9+40=49<50, contradicting (8). For M14 plus M4, the
corresponding calculation is 16+26=42<50. Both ordinary restrictions
are excluded. Two scalar summands also have B=2 and are covered by (8).
One scalar summand has rank one and gives no such contradiction.

There is a stronger condition for every individual non-scalar square
block. Suppose its size is n>=2 and n+2k<2ab. Apply the ruling argument
to its rank-one parameters on each of the three legs. On each leg the
entire n^2-dimensional block space has one fixed coherent factor. This
conclusion does not require n^2>ab: that inequality was only needed for
the one-leg dimension contradiction above. Equation (7) now makes the
whole M_n block have tensor rank at most one, which is impossible.
Consequently every square block of size n>=2 requires

\[
 n+2(N-D)\ge2ab.                                    \tag{9}
\]

For A(5,6) to M16 plus two M3 blocks, D=274 and N=300. Each M3 block
violates (9), since 3+52=55<60. For M16 plus M4, D=272 and the M4
block meets the threshold exactly: 4+56=60. The latter ordinary target
is not excluded by this argument. These conditions combine with exact
partition enumeration without numerical tensor optimization.

## Scope and verification

The argument uses actual ordinary maps in (4). It does not apply that
rank bound to approximating tensors in a degeneration, whose selected
slices can have greater rank before taking the limit. No border or
asymptotic target exclusion is claimed here.

`polynomial_rank_locus.py` checks all 4,095 nonzero binary A(2,2) slices,
including their rational-function Hankel ranks, and tests the exact
three-leg factorization on larger integer examples. Its saved report
also records sharp threshold examples and the stated ordinary targets.
The tests and same-session proof checking support the claims; they are
not formal verification or external review.

The previous [`slice_rank_gap.md`](slice_rank_gap.md) fixes the source and
biform coordinate conventions. The source is the same cyclic convolution
used in the package README and its cited matrix-multiplication paper.
