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
