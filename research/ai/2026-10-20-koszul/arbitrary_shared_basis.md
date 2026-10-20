# The catalecticant bound survives every constant shared basis

October 20, 2026. AI-derived written proof, unreviewed. No smaller exponent
is established. This strengthens Section 2 of `source_obstructions.md`; it
still does not exclude a degeneration with a genuinely singular shared map.
The projective-dimension ingredient is standard, with no novelty claim.

Put D=m-1 and N=m(m+1)/2. A target consists of k copies of every
output-shared block C(j+1,m-j), for j=0,...,D. Allow an independent invertible
identification of the full m-dimensional shared space in every block.

**Theorem.** Suppose a degeneration from C(m,B) to this target has a shared
map regular at zero with invertible limit. The other two maps can be arbitrary
Laurent-polynomial maps, with all cancellations allowed. Then

\[
B\ge kN+k\lfloor D^2/4\rfloor-\lfloor D/2\rfloor. \tag{1}
\]

In particular, an arbitrary constant GL(m) shared change does not escape the
asymptotic 50-percent overhead obstruction. The construction criterion needs
less than 2.047211 percent. An everywhere-invertible shared map whose limit
becomes singular is explicitly outside this theorem.

## 1. A matrix lemma

Let P be any invertible (D+1)-by-(D+1) matrix over C. For 0<=q,j<=D form

\[
H_{q,j}(P)_{(r,a),(s,c)}=P_{r+s,a+c},
\quad 0\le r\le q,\ 0\le s\le D-q,
\quad 0\le a\le j,\ 0\le c\le D-j.
\]

Then

\[
\operatorname{rank}H_{q,j}(P)
\ge 1+\min(q+j,2D-q-j). \tag{2}
\]

To prove it, introduce the biform in divided-power coefficient convention

\[
f_P(s,t;u,v)=\sum_{i,l=0}^{D}
 P_{i,l}\frac{s^it^{D-i}}{i!(D-i)!}
          \frac{u^lv^{D-l}}{l!(D-l)!}.
\]

The matrix of the derivatives of bidegree (q,j), with remaining divided-power
monomials as columns, is exactly H_(q,j)(P). Ordinary monomial columns instead
give only invertible diagonal column scalings.

Assume first q+j<=D. A nonzero homogeneous differential operator alpha of
degree q in s,t acts surjectively from degree-D binary forms to degree-(D-q)
forms. Under the perfect apolar pairing its transpose is multiplication by
the corresponding nonzero degree-q polynomial, which is injective. The same
holds for a nonzero degree-j operator beta in u,v. Therefore the coefficient
matrix of alpha*beta*f_P has rank at least

\[
(D-q+1)+(D-j+1)-(D+1)=D-q-j+1>0. \tag{3}
\]

Here we used invertibility of P and the elementary rank-loss inequality for
composition of the two full-row-rank differentiation maps. In particular the
bilinear map (alpha,beta) -> alpha*beta*f_P never vanishes on a pair of
nonzero factors.

For completeness, a bilinear map from vector spaces of dimensions q+1 and
j+1 with this property has image dimension at least q+j+1. Otherwise its
projectivized kernel, of codimension at most q+j, would intersect the Segre
variety P^q x P^j, of dimension q+j. This is the standard projective dimension
theorem; see [Stacks Project, Lemma 33.34.3, tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R).
The resulting nonzero decomposable kernel element is a contradiction. If
q=0 or j=0 the same statement is ordinary injectivity. This proves (2) when
q+j<=D.

Finally H_(D-q,D-j)(P) is the transpose of H_(q,j)(P), up to the displayed
row/column indexing. Apply the first half with these complementary degrees
when q+j>D. This proves (2) in every degree.

## 2. Application to the tensor

Apply the fixed structured map

\[
X_i\longmapsto\sum_{r+s=i}U_r\otimes V_s,
\qquad \dim U=q+1,\quad\dim V=D-q+1,
\]

and flatten (U,Y) against (V,Z). For a block C(j+1,m-j) identified on X by
P, its coefficient matrix is exactly H_(q,j)(P). Thus (2) applies separately
even if the blocks have different invertible shared identifications. They
occupy disjoint Y/Z subspaces, so their flattening ranks add. Consequently

\[
\operatorname{rank}L_q(\text{target})
\ge k\sum_{j=0}^{D}\bigl(1+\min(q+j,2D-q-j)\bigr)
=k(N+q(D-q)). \tag{4}
\]

The source has rank B+q under this same flattening, as proved by its disjoint
row supports in `source_obstructions.md`. If the shared map is fixed at the
identity, arbitrary maps on Y/Z cannot increase that rank, and neither can
their tensor limit. If the shared map A(epsilon) is regular with invertible
limit A_0, apply its regular inverse to the tensor family. The limiting
target has every block's shared identification multiplied by A_0^(-1),
which stays invertible. Equation (4) still applies. Hence
B>=k(N+q(D-q))-q for all q; maximizing gives (1).

For P=I equality holds in (2) for every q,j, so this general lower bound is
sharp. For a singular P it can fail badly: P=E_(0,0) gives rank one in every
H_(q,j), hence total rank only km. A singular shared limit cannot therefore
be inserted into the argument as though it were an invertible basis change.

## 3. Consequence for the concurrent graded search

At concurrent commit `d2d505c`, `graded_shared_discovery.py` on
`research/filtration-compatibility-20261020` uses an arbitrary **constant**
matrix G on the shared factor, and grading weights on Y/Z. It was introduced
to escape the earlier fixed-coefficient obstruction. The theorem above also
excludes this enlarged ansatz at the desired low source cost. In particular
the a=4, B=10 experiment cannot yield a certificate with invertible G: (1)
requires B>=11. Small residuals with a nearly singular G are not evidence to
the contrary. No claim is made about a parameter-dependent singular G.

This is a mathematical scope update, not an independent replay of the other
worker's optimizer. The next construction must use nontrivial shared-factor
weights or a more general singular shared map; a fixed arbitrary basis alone
does not suffice.

## 4. Verification

`rotated_catalecticants.py` records exact ranks for identity, Pascal,
Vandermonde and nontrivial permutation matrices, in all bidegrees for m=2,...,6.
The tests independently assemble transformed tensor flattenings, verify the
divided-power derivative convention and check the singular counterexample.
These finite checks validate the implementation; the all-size argument is
the written proof above and remains unreviewed.

## 5. More generally: every nonsingular bilinear block

The same rank bound does not require a convolution block. Let
b:Y^* x Z^* -> X be any bilinear map with dimensions
(dim Y,dim Z,dim X)=(j+1,D-j+1,D+1) such that b(y,z)!=0 whenever
y,z are both nonzero. Then its structured flattening satisfies

\[
\operatorname{rank}L_q(b)\ge1+\min(q+j,2D-q-j). \tag{5}
\]

Here is a direct proof that also explains (2). Contracting a nonzero
alpha in U^* into Delta_q gives a map X -> V of rank D-q+1; its transpose
is multiplication by a nonzero binary form, hence injective. Its kernel
has dimension q. For any nonzero y, the map b(y,-):Z^* -> X is injective,
so its composite with X -> V has rank at least D-j+1-q. If q+j<=D this
is positive. Thus the flattening's map U^* x Y^* -> V tensor Z has no
nonzero decomposable kernel, and the projective-dimension argument gives
rank at least q+j+1. If q+j>D, transpose the flattening and use
V^* x Z^* in exactly the same way, obtaining 2D-q-j+1. This proves (5).
Invertible changes of any block's shared identification preserve the
nonvanishing hypothesis.

Consequently (1) holds for a matched collection of arbitrary such nonsingular
bilinear blocks, with the same dimensions and multiplicities. This is stronger
than requiring each block to be a convolution in a changed basis.

## 6. A dominant-degree weight region is also excluded

Consider constant matrices P,Q,G applied to C(m,B), followed by weights

\[
w(X_i)=\beta i,\quad
w(Y_{a,b})=\alpha(a+b)-\beta a,\quad
w(Z_{c,d})=\alpha(c+d)-\beta c-\alpha D.
\]

Every canonical target term has weight zero. Suppose alpha>D*abs(beta),
and the constant transformed tensor M has zero coefficients at every negative
weight and the required target coefficients at weight zero.

Every entry with deg(Y)+deg(Z)<D then has negative weight, hence vanishes.
Degenerate M using only the total-degree weights: this retains the blocks
with deg(Y)+deg(Z)=D, with the shared factor fixed at G. In the block of
dimensions (j+1,D-j+1), the retained bilinear map has coefficients

- beta>0: b(e_a,e_c)=X_(a+c) plus terms in X_i with i>a+c;
- beta<0: b(e_a,e_c)=X_(a+c) plus terms in X_i with i<a+c;
- beta=0: the canonical convolution block.

Every such block has no zero divisors. For beta>0, take the lowest indices
of the nonzero coefficients of y and z. Their sum indexes a nonzero leading
coefficient of b(y,z), which no higher-index pair can cancel. For beta<0 use
the highest indices instead. The hypothesis of Section 5 therefore holds.
The first-stage degeneration has constant shared G, so (1) applies to it.
If the final target is concise, G must be invertible: every nonzero-parameter
shared flattening has rank at most rank G, and rank cannot increase in a
limit. Hence no singular constant-G exception is available.

This excludes the whole dominant-degree region alpha>D*abs(beta) at low
source cost, even though the final shared weights are nonzero. The concrete
choice alpha=m+1,beta=1 selected in `ACTIVE.md` lies in this region and is
closed by this proof. The concurrent worker's mixed directions (1,1),
(1,-1), (1,2) at m=4 lie outside this region and are not excluded here.
Nor does this argument address an arbitrary parameter-dependent shared map.

Before the proof was found, ten retained 1,000-cycle exploratory fits were completed
for m=3,4 in this region. None supplied an exact
certificate. The best m=4 residual was about 0.00385 with factor norms about
163; a known-excluded identity shared basis also reached about 0.00505 with
norms about 188. These are partial-coefficient residuals, not tensor-distance
or construction certificates. The bounded records and program are retained
as diagnostics. Repeating this search cannot evade the all-size obstruction.

## 7. A complementary small-slope region is excluded by one slice

Keep the constant-matrix weight ansatz of Section 6, but now suppose
0<alpha<=beta. Then a certificate requires the stronger finite bound

\[
B\ge k\bigl(2N-\lfloor m^2/4\rfloor-1\bigr)-D. \tag{6}
\]

This again has asymptotic source ratio at least 3/2. In particular at m=4,
k=1 it requires B>=12, excluding the concurrent directions (alpha,beta)=(1,1)
and (1,2) at B=10. It does not exclude that worker's direction (1,-1).

To see this, take the X_0 slice M_0 of the constant transformed tensor before
weighting. Its entry at Y_(a,b),Z_(c,d) has exponent

\[
\alpha(b+d-D)+(\alpha-\beta)(a+c).
\]

This is at most alpha*(b+d-D). Negative entries must be zero; entries of
weight zero must equal the target. Thus M_0 is supported only where b+d>D,
together with the k matched entries a=c=0,b+d=D for each such b,d.

Fix 0<=t<=D. Cover the allowed support by all Y rows with b>t, all Z columns
with d>D-t, and the k additional Y rows (a,b)=(0,t). Every allowed edge is
covered: an uncovered strict edge would have b+d<=D, and an uncovered
boundary edge would have b=t,d=D-t,a=c=0. A matrix supported in R rows and
C columns has rank at most R+C, by splitting it into those rows and the
remaining columns. Hence

\[
\operatorname{rank}M_0\le
k\left(\frac{(D-t)(D-t+1)}2+\frac{t(t+1)}2+1\right).
\]

Taking t=floor(D/2) gives k*(floor(m^2/4)+1). On the other hand P and Q must
have rank kN and G must be invertible, since the final tensor is concise and
rank cannot increase under the diagonal weighting limit. Thus M_0 is a
nonzero-polynomial source slice restricted by maps of those ranks. The
ordinary rank-loss argument from `source_obstructions.md` gives
rank M_0>=2kN-B-D. Comparing proves (6).

The displayed cover is an upper bound on the rank of every completion of the
partial coefficient matrix. No floating optimizer outcome or untraced
matching solver is used. Mixed slopes between this region and the
dominant-degree region remain outside these two arguments.
