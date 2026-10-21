# A dimension bound from the Hankel symbol of a matrix block

October 21, 2026. This note combines the polynomial slice-rank bound
with the geometry of a rational normal curve. The matrix-block
consequence was developed in this generating session and checked by a
second agent in the same session. No external independent review or
formalization is claimed. It is an obstruction
to ordinary restrictions, not to singular degenerations, and does not
give a smaller matrix multiplication exponent.

The scalar identification of Hankel rank loci with secant varieties of
a rational normal curve is classical. For a primary reference, see
Claudiu Raicu, *3x3 Minors of Catalecticants*, arXiv:1011.1564v3,
Section 1, especially equation (1.1):
https://arxiv.org/abs/1011.1564. A proof of the set-theoretic statement
needed here is included below, so that this argument does not depend
on a determinantal ideal theorem or its indexing conventions.

## Statement for square matrix blocks

Set m=a+b-1 and N=abm, and choose an integer r such that

\[
 1\le r<\min(a,b),\qquad 3r\le m.                \tag{1}
\]

Suppose ordinary linear maps restrict A(a,b) to a concise direct sum
of square matrix tensors, with total leg dimension D. Let M_n be any
one of its blocks. Then

\[
 n^2>rab\quad\Longrightarrow\quad
 n+2(N-D)\ge(r+1)ab.                             \tag{2}
\]

The contrapositive is often useful: if every lifted rank-one parameter
of this block has slice rank below (r+1)ab, the block's n^2-dimensional
dual space injects into r copies of the ab-dimensional biform space.

For example, take A(5,6), where ab=30, N=300 and m=10. The choice r=3
is permitted. Even a single M16 block would have D=256 and loss 44,
giving

\[
 16+88=104<120=(r+1)ab,
 \qquad 16^2=256>90=rab.
\]

Thus an ordinary M16 restriction is impossible, and adding further
direct-sum blocks cannot repair it. The exact finite partition screen
in `square_sum_frontier.md` can apply (2) for every permitted r.

## 1. Scalar Hankel rank and a short scheme on P1

Work first over an algebraically closed field L. Let h=(h_0,...,h_d),
where d=a+b-2, and let H=(h_(p+q)) have format a by b and rank s with
0<s<min(a,b). Regard h as the linear functional on homogeneous
polynomials S^d=L[u,v]_d that takes u^(d-k)v^k to h_k.

The left kernel W of H is a subspace of S^(a-1), with dimension a-s.
It has the property

\[
 h(W\,S^{b-1})=0.                               \tag{3}
\]

Let q be the greatest common homogeneous divisor of the elements of
W, and put e=deg q. Since W is contained in q S^(a-1-e),

\[
 a-s=\dim W\le a-e,
 \qquad e\le s.                                 \tag{4}
\]

We need the following elementary polynomial multiplication fact.

**Multiplication fact.** If V is a k-dimensional subspace of S^u
whose elements have no common zero on P1, then

\[
 V S^v=S^{u+v}\qquad\text{whenever }v\ge u-k+1.  \tag{5}
\]

Here is a proof. Dehomogenize to polynomials in t of degree at most u.
There is an element p of V of degree exactly u, because infinity is
not a common zero. In the u-dimensional algebra B=L[t]/(p), the
image of V has dimension k-1. Let V_j be the image of V times
polynomials of degree at most j. If V_(j+1)=V_j while V_j is proper,
then V_j is stable under multiplication by t. It is therefore an ideal
of B containing the image of V. But the elements of V have gcd one,
so that ideal is all of B, a contradiction. Until it is full, its
dimension grows by at least one at every step. Thus V_j=B by
j=u-k+1. In degree at most u+v, the kernel of reduction modulo p is
p times the polynomials of degree at most v; those multiples already
belong to V S^v. Surjectivity modulo p therefore gives the whole
polynomial space. Homogenization proves (5). The case u=0 is
immediate and can be separated from the quotient argument.

Apply (5) to V=W/q. Here u=a-1-e and k=a-s, so u-k+1=s-e. Since
b-1>=s, multiplication by S^(b-1) fills the required degree:

\[
 W S^{b-1}=q S^{d-e}.                            \tag{6}
\]

Equation (3) says that h annihilates q S^(d-e). The zero scheme Z of
q has length e, and this annihilator is exactly its span under the
degree-d rational normal embedding. One can see this directly from
polynomial remainders or Hermite interpolation. At a point t, its
basis consists of the value and successive jet vectors of
(1,t,...,t^d), up to the multiplicity prescribed by q; jets at infinity
use the reversed coordinates.

The Hankel pairing of a functional supported on a length-e scheme
factors through its e-dimensional algebra of jets, so its rank is at
most e. Combining this with rank H=s and (4) gives e=s. In particular,
every h of Hankel rank at most r<min(a,b) is supported on a scheme of
length at most r. Conversely every such scheme gives Hankel rank at
most r. The zero sequence is included separately.

## 2. Lines of bounded Hankel rank have one supporting scheme

For a finite subscheme Z of P1, write S_Z for its vector span in
L^(d+1). If length(Z union Z')<=d+1, Hermite interpolation gives

\[
 S_Z\cap S_{Z'}=S_{Z\cap Z'}.                    \tag{7}
\]

Indeed, the jets for the union are an independent list. Both spaces
are spanned by subsets of that list. On P1, union and intersection
take the maximum and minimum multiplicity at each point.

Assume 3r<=d+1. A nonzero sequence of Hankel rank at most r has a
unique minimal support of length at most r: two possible supports
have union of length at most 2r, so (7) reduces them to their
intersection.

Now let h and h' be two nonzero sequences whose entire pencil has
Hankel rank at most r. Denote their minimal supports by Z and Z',
and set W=Z union Z', of length at most 2r. For all but finitely many
c in L, the coefficient of the highest required jet at each point of
W remains nonzero in h+c h'. Thus its minimal support within W is all
of W. The pencil hypothesis supplies another support T of length at
most r. Since length(W union T)<=3r<=d+1, equation (7) implies that
h+c h' belongs to S_(W intersection T). Minimality within W forces
W to be contained in T. Therefore

\[
 \operatorname{length}(Z\cup Z')\le r.           \tag{8}
\]

The qualification about the generic member is essential. For example,
a secant line has rank-one endpoints and generic rank two. One must
use the maximum rank occurring in a family, rather than fix the
support from a point whose rank is smaller than that maximum.

The numerical condition 3r<=d+1 also cannot simply be removed from
this fixed-scheme statement. At d=3r-2, the pencil

\[
 h(c)=\delta_{r-1}+c\delta_{2r-1}
\]

has constant Hankel rank r for suitable a,b>r with a+b=3r. Its finite
members have annihilating polynomial t^r-c, so their supporting
schemes vary. Its member at infinity is supported at the length-r
scheme at infinity. The controls include r=2,3,4,5; for r=2 this is
the three-by-three Hankel pencil with sequence (0,1,0,c,0). This
counterexample concerns fixed schemes. It does not assert that every
possible dimension bound fails outside (1).

## 3. Matrix rank-one parameters fix an r-dimensional symbol space

Let Phi be any L-linear map from the space of l by h matrices to
L^(d+1). It need not be injective. Suppose Phi takes every rank-one
matrix to a sequence of Hankel rank at most r, with (1) satisfied.
Then

\[
 \dim_L\operatorname{image}\Phi\le r.            \tag{9}
\]

If Phi is zero, there is nothing to prove. Otherwise let s<=r be the
largest Hankel rank attained on a rank-one parameter. Choose
u0 tensor v0 where that rank is s, and let Z be its minimal scheme,
of length s. Apply (8), with s in place of r, to every line in the
first matrix ruling through u0 tensor v0. Since all points of that
ruling have rank at most s, every image in it lies in S_Z.

The u for which Phi(u tensor v0) still has rank s form a nonempty
Zariski-open set: an s by s Hankel minor is nonzero at u0. Through
each such point, apply the same line argument to the second ruling.
The entire second ruling lies in S_Z. These rulings cover a dense
set of rank-one parameters. The space S_Z is closed and linear, so
it contains all rank-one parameter images and their linear span.
Rank-one matrices span the full matrix space, proving (9).

If a ruling has dimension zero, it can simply be omitted; its other
ruling is the entire rank-one parameter space. Zero images cause no
problem in the line argument. Notice that this proof does not need
the images of rank-one parameters to remain injective after a field
extension.

## 4. Applying the symbol map over C(x,z)

Return to the source tensor over C. Let E be the lifted dual space
of one target matrix block on one source leg. It is a C-linear
subspace of the source slice space. In the notation of
`polynomial_rank_locus.md`, its slices have long sequences

\[
 f_k(x,z)=\sum_{i<a,s<b}F_{i,k,s}x^i z^s.
\]

Put K=C(x,z). Suppose every lifted rank-one matrix parameter has
full slice rank below (r+1)ab. The polynomial injection bound gives

\[
 \operatorname{rank}_K(f_{p+q})\le r              \tag{10}
\]

for every complex rank-one parameter.

Equation (10) also holds for rank-one parameters over an algebraic
closure of K. To justify that step, write a rank-one matrix as
u tensor v. Every (r+1) by (r+1) minor is a polynomial in u,v,x,z.
It vanishes as a polynomial in x,z for every complex u,v. The field C
is infinite, so each coefficient in x,z vanishes identically as a
polynomial in u,v. The same minor therefore vanishes after any field
extension. This argument is needed; a C-linear injection into the
source need not stay injective after forming only its K-valued long
sequence map.

Apply (9) over the algebraic closure of K to this sequence map. Its
image has dimension at most r. Matrix rank is unchanged by extending
K, so the K-span H of all sequences coming from E also has dimension
at most r. The supporting scheme may vary with x and z. This proof
does **not** assert that it is constant.

Choose dim_K H of the ordinary sequence coordinates f_k so that
projection onto them is injective on H. Such coordinates are pivot
rows of a full-column-rank matrix for H. If a vector of E has zero
polynomials at those selected coordinates, its whole sequence is
zero over K, hence every coefficient F_(i,k,s) is zero. Thus this
projection is also a C-linear injection from E to at most r copies
of the biform coefficient space. Each copy has dimension ab, giving

\[
 \dim_{\mathbb C} E\le rab.                     \tag{11}
\]

The last step counts polynomial coefficients, not rational function
dimensions. It is why a variable supporting scheme still gives the
finite-dimensional obstruction.

## 5. Ordinary source-to-target maps

A concise target forces each ordinary source leg map to be surjective,
so the dual map embeds its block parameter spaces in the source.
If the other two leg maps have kernels of dimensions k_Y,k_Z, a
target slice of rank t has a source lift of rank at most

\[
 t+k_Y+k_Z.                                      \tag{12}
\]

For a block M(l,h,n), every rank-one parameter on its lh-dimensional
leg has target slice rank n. Combining (11)--(12) proves the
rectangular form of the result:

\[
 lh>rab\quad\Longrightarrow\quad
 n+k_Y+k_Z\ge(r+1)ab.                            \tag{13}
\]

There are two cyclic versions. For a direct sum of square blocks,
k_Y=k_Z=N-D and l=h=n, so (13) becomes (2).

This is separate from the constant-scheme equality theorem in
`parity_structure_equality.md` and `hankel_rank_two.md`. That theorem
uses equality in the two polynomial multiplication ranks to obtain a
constant length-two long space, and then an eight-dimensional
three-leg factorization. The present dimension bound needs neither
polynomial equality nor a constant scheme, but requires the block
leg dimension to exceed rab.

## Scope of the result

The bound applies to one copy of the indicated source under ordinary
linear restrictions. It imposes necessary conditions; a target that
passes them is not thereby constructed. It does not exclude arbitrary
singular degenerations, auxiliary-source constructions, or targets
from tensor powers. Exact controls of the polynomial and finite
dimension statements are in `hankel_symbol_dimension.py`. A separate
partition computation is responsible for any finite frontier claim.
