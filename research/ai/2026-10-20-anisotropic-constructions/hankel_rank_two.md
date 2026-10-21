# Fixed length-two long spaces and the equality threshold

October 21, 2026. This note develops the geometric part of the equality
case of `polynomial_rank_locus.md`. The polynomial equality step is in
`parity_structure_equality.md`. These are arguments from the present
generating session; no external independent review or formalization is
claimed. The matrix-target consequences concern ordinary restrictions.

## Long-coordinate schemes

Write d=a+b-2 and let

\[
 \nu_d(t)=(1,t,\ldots,t^d),\qquad
 \nu_d(\infty)=(0,\ldots,0,1).
\]

For a finite subscheme Z of the projective line, let S_Z be its span
under this rational normal embedding. For example, a pair of distinct
points gives their secant line, while a double point gives the tangent
line. At a finite t, the latter vector space has basis nu_d(t),
nu_d'(t); at infinity its basis is e_d,e_(d-1).

The length counts multiplicity. Thus a coherent vector has support of
length one; a non-coherent vector in a secant or tangent space has
minimal support of length two. We also use vector-valued long sequences
F in G tensor S_Z, where G is the ab-dimensional space of short biform
coefficients.

### Intersections of these spans

If a scheme W has length at most d+1, its evaluation and derivative
functionals on polynomials of degree at most d are linearly independent.
One proof is Hermite interpolation: modulo the product of the powers of
the distinct linear factors, the prescribed jets can be chosen
arbitrarily. Homogenization includes a jet at infinity. Consequently, if
length(Z union W)<=d+1, then

\[
 S_Z\cap S_W=S_{Z\cap W}.                         \tag{1}
\]

Here the intersection and union of zero-dimensional schemes on P1 take
the minimum and maximum multiplicity at each point. The same formula
holds after tensoring each space with G. This follows by choosing a
common basis of jets for the union: both spaces are spanned by subsets
of an independent list.

In particular, when d>=3, a nonzero vector-valued sequence with a
support of length at most two has a unique minimal such support. If
there were two, their union would have length at most four, and (1)
would replace both by their intersection.

## Lines have a common scheme

Assume d>=5. Let F and F' be two nonzero vectors such that every
nonzero element of their linear span belongs to G tensor S_Z for some
scheme Z of length at most two. Let Z_F and Z_F' be their minimal
supports. Then

\[
 \operatorname{length}(Z_F\cup Z_{F'})\le2.       \tag{2}
\]

To prove this, put W=Z_F union Z_F'. Its length is at most four. In the
independent jet basis for W, each point's highest required jet has a
nonzero G-valued coefficient in F or F'. For all but finitely many
scalars c, that coefficient remains nonzero in F+cF'. Its minimal
support *within W* is therefore W itself. By hypothesis F+cF' also
belongs to G tensor S_Z for a scheme Z of length at most two. Since
length(W union Z)<=6<=d+1, equation (1) shows that it belongs to
G tensor S_(W intersection Z). Minimality within W forces W to be
contained in Z, proving (2).

The argument is for vector-valued sequences, rather than only scalar
binary forms. A common factor in the short coefficient polynomials is
not needed.

## Propagation over matrix rank-one parameters

Let a linear injection from a matrix parameter space into G tensor C^(d+1)
take every rank-one matrix into the length-at-most-two locus above.
Its whole image then lies in G tensor S_Z for one fixed scheme Z of
length at most two.

First suppose some rank-one parameter u0 tensor v0 has minimal support
Z of length two. Every line in its first ruling has support contained
in Z by (2), so the whole first ruling lies in G tensor S_Z. The set of
u in this ruling whose image still has minimal support Z is nonempty
and Zariski open. Indeed, a length-two scheme has only finitely many
proper subschemes. For each such u, apply (2) along the second ruling
through u tensor v0. That entire ruling also lies in G tensor S_Z.
These rulings are dense in the rank-one matrix variety. Since
G tensor S_Z is a closed linear space, it contains every rank-one
parameter image, hence their full linear span.

If no rank-one parameter has minimal support of length two, every
such image is a short vector times one coherent long vector. A line
consisting of these decomposable vectors must have a fixed coherent
factor: if its two short factors are independent, their sum would lose
decomposability; if they are proportional, a line would be contained
in the rational normal curve. The latter is impossible for d>=2.
The two connected families of matrix rulings then fix one coherent
factor throughout the rank-one variety and its span.

## Three fixed schemes give an exact eight-dimensional factorization

This step includes tangent schemes and does not need an argument with
singular limits. For a long space S_Z of length at most two, all its
Hankel matrices have common row and column spaces of dimension at most
two. This follows directly from their bases. At a finite double point,

\[
 (p+q)t^{p+q-1}
 = (p t^{p-1})t^q+t^p(q t^{q-1}).                \tag{3}
\]

The short row and column spaces are spanned by evaluation and first
derivative vectors. A distinct pair uses its two evaluation vectors.
At infinity, use the final two coordinate vectors; (3) becomes the
two positions with p+q=d-1. The statement is also immediate for a
single point.

Take fixed length-two spaces on all three source long coordinates,
and denote their bases h_X,alpha, h_Y,beta, h_Z,gamma. There are
two short bases U_X,V_X, U_Y,V_Y, U_Z,V_Z such that

\[
 h_{X,\alpha}(p+q)
 =\sum_{u,v<2}L_X(\alpha,u,v)U_X(u,p)V_X(v,q),
                                                               \tag{4}
\]

and similarly for the Y and Z edges. Write a first-leg coefficient
vector as sum_alpha G_X,alpha(i,s) h_X,alpha, and likewise for Y and Z.
In the six-index contraction of A(a,b), its dependence on this first
vector is entirely through

\[
 \widehat G_X(\alpha,t,z)
 =\sum_{i,s}G_{X,\alpha}(i,s)U_Z(t,i)V_Y(z,s),
 \qquad \alpha,t,z<2.                            \tag{5}
\]

The second and third legs similarly factor through

\[
 \widehat G_Y(\beta,\ell,u),\qquad
 \widehat G_Z(\gamma,v,w).
\]

The resulting core tensor, with at most eight coordinates on each
leg, has coefficient

\[
 L_X(\alpha,u,v)L_Y(\beta,w,z)L_Z(\gamma,t,\ell). \tag{6}
\]

Every flattening therefore has rank at most eight. The conclusion
persists if some of the long schemes have length one. This is a
common-support assertion only for the explicitly fixed long schemes;
it does not use the invalid rule that projecting k directions can
reduce a general matrix space's joint support by only k.

For completeness, the core also has border rank at most eight. Each
double-point plane is a limit of secant planes, using the basis
nu_d(t), (nu_d(t+epsilon)-nu_d(t))/epsilon, with the analogous local
coordinate at infinity. For three distinct-pair planes the contraction
is a sum of eight simple tensors, indexed by the choices of the
three points. Their simultaneous limit is the core in (6). The
ordinary-target exclusion below needs only the exact flattening bound.

## Equality-threshold consequence

The companion equality lemma establishes the following statement for
a,b>=3. If a source slice F has rank at most 2ab, it belongs to
G tensor S_Z for a scalar scheme Z of length at most two. Rank below
2ab was already covered by `polynomial_rank_locus.md`; at equality,
the two polynomial multiplication ranks are both minimal, forcing a
constant second-order scalar Hankel recurrence. The proof in the
companion note is essential to this consequence.

Assume also a+b-2>=5. Consider an ordinary restriction of A(a,b) to a
direct sum of square matrix tensors, with total leg dimension D and
loss k=N-D, where N=ab(a+b-1). A rank-one matrix parameter of a square
block of size n has target slice rank n. Its source lift has rank at
most n+2k. If n+2k<=2ab, the companion equality lemma and the matrix
ruling argument above put the entire block's lifted dual space in one
fixed long scheme on each leg. Equations (5)--(6) then give

\[
 n^2\le8.
\]

Consequently every square block of size n>=3 must satisfy the stronger
necessary condition

\[
 n+2(N-D)\ge2ab+1.                              \tag{7}
\]

For A(5,6) to M16 plus M4, N=300, D=272 and k=28. The M4 block would
give 4+56=60=2ab and flattening rank 16, contradicting the bound eight.
Thus the ordinary target is excluded once the companion equality
lemma is included. This argument does not exclude the same target as
a singular degeneration. It also does not exclude all square
partitions for A(5,6): for example, M16 plus M3 plus M2 plus two scalar
blocks has D=271, and its M3 block has 3+58=61. The equality condition
alone does not close that partition.
The later general theorem in `hankel_symbol_dimension.md` does close it:
its r=3 condition excludes the M16 block itself. Thus this example records
the scope of the equality theorem, not a remaining ordinary candidate.

## Exact controls and scope

`hankel_rank_two.py` constructs (4)--(6) over the integers and compares
all 1,296,000 coefficients for six choices of secant/tangent spaces,
including infinity. It also checks the eight-dimensional cores. The
separate `hankel_symbol_dimension.py` checks Hermite jet independence,
including repeated points and infinity, for 1,000 bounded schemes in
degree nine. These controls are finite checks of the formulas, not
substitutes for the scheme and equality proofs.

Only ordinary source-to-target maps are used in the rank-lift
inequality. No claim here transfers that inequality to a family of
approximating tensors with higher-rank slices, and no exponent
improvement follows from the exclusion.
