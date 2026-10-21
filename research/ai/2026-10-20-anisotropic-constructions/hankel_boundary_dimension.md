# Hankel Segre images at the first boundary

October 21, 2026. This note gives a written proof at m=3r-1, one step
outside the earlier fixed-scheme range. The proof was checked by two
other agents in this generating session. It is not a tensor
construction or an exponent improvement, and no external independent
review, formalization, or historical priority is claimed.

Work over an algebraically closed field F of characteristic zero.
Let

\[
r\ge2,\qquad r<\min(a,b),\qquad m=a+b-1=3r-1,
\qquad d=m-1=3r-2.
\]

For h in (S^d F^2)^*, its a-by-b Hankel matrix has entries h_(i+j).
Write X_r for the cone where this matrix has rank at most r. For a
length-s subscheme Z of the projective line, let S_Z denote its
s-dimensional span of evaluation and derivative functionals in
(S^d F^2)^*.

The classical scalar Hankel statement, proved elementarily in
[hankel_symbol_dimension.md](hankel_symbol_dimension.md), identifies
every rank-s point, for s<min(a,b), with a unique minimal scheme of
length s. Spans of schemes have their expected intersection whenever
the union has length at most m. We use these facts with repeated
points and points at infinity included.

## The dimension statement

**Theorem.** If a linear map

\[
\Phi:U\otimes V\longrightarrow F^m
\]

sends every rank-one input into X_r, then

\[
\dim_F\operatorname{im}\Phi\le\max(r,4).
\tag{1}
\]

In particular, the bound is r for every r>=4 at this boundary.
Neither U nor V needs to have a specified dimension, and Phi need
not be injective. The proof first classifies the relevant linear
spaces inside X_r, then applies that result to the two Segre rulings.

## 1. A moving line has disjoint endpoint schemes

Take rank-r points h_0,h_1 whose full projective line lies in X_r.
Let their minimal schemes be Z_0,Z_1, each of length r. If the schemes
differ, their union Y has length between r+1 and 2r.

A generic linear combination h_0+t h_1 uses all of Y: the coefficient
of the highest jet at each support point is a nonzero linear
polynomial in t, so it is nonzero away from finitely many values.
If Y had length at most 2r-1, a minimal scheme Z_t of length at most r
for this combination would satisfy

\[
\operatorname{length}(Y\cup Z_t)\le3r-1=m.
\]

Independence of these jets would force the combination into
S_(Y intersect Z_t), contradicting its full support on Y. Therefore
Y has length 2r and the endpoint schemes are disjoint.

The same argument shows that the generic scheme Z_t on a moving
line is disjoint from each endpoint scheme. Here a *moving line*
means one whose generic minimal scheme is not constant. A line with
one fixed scheme is already contained in its scheme span.

## 2. The annihilator of a moving line is itself a pencil

Choose an affine coordinate whose point at infinity avoids the two
endpoint schemes. Write their monic annihilating polynomials as
q_0,q_1, of degree r. They are coprime by Section 1. Their product
Q=q_0 q_1 has degree 2r.
This coordinate also avoids the generic moving scheme: the degree-r
annihilator is regular near the rank-r endpoint whose support avoids
infinity, so its leading coefficient stays nonzero on an open set.

Set

\[
R_i=F[z]/(q_i),\qquad R=F[z]/(Q)=R_0\oplus R_1.
\]

Each endpoint functional h_i induces a functional ell_i on R_i.
The bilinear pairing ell_i(fg) is nondegenerate. Indeed, degeneracy
would give a nonzero ideal annihilated by ell_i and hence a proper
quotient of R_i supporting h_i, contrary to minimality of its
length-r scheme.

The image of polynomials of degree at most 2r-2 in R is a hyperplane.
Its annihilator is the functional kappa that extracts the coefficient
of z^(2r-1) from the remainder modulo Q. The pairing kappa(fg) is
nondegenerate: for a nonzero remainder f of degree e, multiplying
by z^(2r-1-e) gives a nonzero top coefficient without any reduction.
Its restrictions to the two summands of R are therefore also
nondegenerate.

Consequently there are fixed units w_i in R_i such that

\[
\kappa|_{R_i}(f)=\ell_i(w_i f).
\tag{2}
\]

Existence and uniqueness follow from the nondegenerate ell_i pairing.
The elements w_i are units because the resulting kappa pairing is
nondegenerate as well.

For generic nonzero t, let q_t be a degree-r annihilator of
h_t=h_0+t h_1. The annihilation equations hold on all polynomial
multipliers p of degree at most

\[
d-r=2r-2.
\]

Thus the functional on R defined by

\[
p\longmapsto
\ell_0((q_t\bmod q_0)p)+
t\ell_1((q_t\bmod q_1)p)
\]

is a scalar multiple c_t kappa. Using (2) and nondegeneracy gives

\[
q_t\bmod q_0=c_t w_0,\qquad
q_t\bmod q_1=(c_t/t)w_1.
\tag{3}
\]

The scalar c_t is nonzero: otherwise q_t would be divisible by the
coprime product q_0q_1, despite having degree r.

Let f and g be the degree-less-than-2r Chinese remainder lifts of
(w_0,0) and (0,w_1), respectively. Equation (3) gives, as an actual
polynomial identity of degree less than 2r,

\[
q_t=c_t f+(c_t/t)g.
\tag{4}
\]

Since q_t has degree at most r for infinitely many t, both f and g
have degree at most r. The polynomial f is nonzero and divisible
by q_1, while g is nonzero and divisible by q_0. Hence

\[
q_t\ \text{is proportional to}\ \beta q_0+t\alpha q_1
\quad\text{for fixed nonzero }\alpha,\beta.
\tag{5}
\]

In characteristic zero a pencil of two coprime degree-r binary
forms has a reduced generic member. For example, in an affine
coordinate a multiple root must also be a zero of the nonzero
Wronskian q_0' q_1-q_0 q_1'. There are finitely many such critical
values of the pencil parameter. Equation (5) therefore proves:

**Every moving line has a reduced generic minimal scheme.**

This conclusion is needed below. It avoids assuming that the
generic point of an arbitrary subspace starts with a reduced scheme.

## 3. A moving linear space has dimension at most two

Let L be a vector subspace contained in X_r. Suppose its generic
point has rank r and its minimal scheme varies. Section 2 supplies
one reduced rank-r point of L, and reducedness is open. Thus at a
generic point h in L we may write

\[
h=\sum_{i=1}^r c_i\,\operatorname{ev}_{z_i},
\tag{6}
\]

with distinct finite z_i and nonzero c_i. The coefficients and roots
are local algebraic coordinates, after an etale extension if needed.
Equivalently, the unique degree-r annihilator is locally regular,
its simple roots can be continued locally, and the weights are
recovered from an invertible Vandermonde matrix.

The tangent span is

\[
S_{2Z}=\operatorname{span}
\{\operatorname{ev}_{z_i},\operatorname{ev}'_{z_i}:1\le i\le r\},
\]

of dimension 2r. For a direction v in L, the straight line h+t v
lies in X_r. Differentiate its expression (6) twice. Since the
second derivative of h+t v is zero, reduction modulo S_(2Z) gives

\[
\sum_{i=1}^r c_i\,\dot z_i(v)^2
\operatorname{ev}''_{z_i}=0\pmod{S_{2Z}}.
\tag{7}
\]

There is exactly one relation among the r classes of second
derivatives in this quotient. Indeed, the full scheme 3Z has length
3r=m+1, its span has dimension m, and 2Z has span dimension 2r.
Every coordinate of this unique relation is nonzero: removing one
highest jet leaves a scheme of length m, whose jets are independent.

Write the nonzero relation coefficients as kappa_i. Equation (7)
implies identities of quadratic polynomials on the vector space L:

\[
\frac{c_i}{\kappa_i}\dot z_i^2
=\frac{c_1}{\kappa_1}\dot z_1^2,
\qquad 1\le i\le r.
\tag{8}
\]

The functions dot z_i are linear forms on L. Over the algebraically
closed field, equality of their squares up to nonzero constants
forces them all to be proportional (or all to vanish). Thus the
differential of the minimal-scheme map has rank at most one.
Characteristic zero implies that this map has image dimension at
most one.

Put ell=dim L. Since the scheme varies, its image dimension is one.
For a generic scheme Z in this image, its fiber in P(L) is the open
rank-r portion of P(L intersect S_Z). Therefore

\[
\dim(L\cap S_Z)=\ell-1.
\tag{9}
\]

For two distinct generic schemes Z and Z', Section 1 gives
disjointness. Their spans have zero intersection, since their union
has length 2r<=m. The two subspaces L intersect S_Z and L intersect
S_Z' are consequently disjoint subspaces of L. By (9),

\[
2(\ell-1)\le\ell,
\]

so ell<=2.

If the generic rank in L is s<r, then 3s<=m and the earlier
fixed-scheme line argument applies: any such L has one fixed scheme
of length at most s. We have proved the classification needed here:

**Every linear subspace L contained in X_r of vector dimension at
least three lies in one fixed scheme span of length at most r.**

## 4. Applying the linear-space statement to a Segre image

Let p and q be the generic, equivalently maximum, ranks of the maps

\[
V\longrightarrow F^m,\quad v\longmapsto\Phi(u,v),
\qquad
U\longrightarrow F^m,\quad u\longmapsto\Phi(u,v),
\]

respectively. If the generic Hankel rank on rank-one inputs is s<r,
the previous 3s<=m theorem already bounds the whole image by s.
Assume it is r.

Suppose p>=3. For generic u, Section 3 places the entire ruling
Phi(u,V) in the span of one fixed length-r scheme Z_u. We claim
that Z_u is independent of generic u.

Otherwise choose generic u_0,u_1 for which Z_0 and Z_1 differ, and
for which u_0+u_1 is generic as well. For generic v the rank-r points
Phi(u_0,v), Phi(u_1,v), and their sum have these fixed ruling
schemes Z_0,Z_1,Z_2. The first two span a line in X_r. Section 1
implies that all three schemes are pairwise disjoint; Z_2 cannot
equal either endpoint scheme because the other endpoint would then
lie in their zero span intersection.

The third ruling is contained in

\[
(S_{Z_0}+S_{Z_1})\cap S_{Z_2}.
\]

This intersection has dimension exactly one. Its two summands have
dimensions 2r and r, and the union of the three disjoint schemes has
length 3r=m+1 and span dimension m. Thus the intersection dimension
is 3r-m=1. This contradicts the generic ruling dimension p>=3.
Hence the ruling scheme is constant and the whole image has
dimension at most r. The same argument applies if q>=3.

It remains that p<=2 and q<=2. A general elementary bilinear bound
gives dim im Phi<=pq. To see it, choose u_1,...,u_q whose images
Phi(u_i,v) are independent for generic v. They then span Phi(U,v)
for generic v. All these images lie in the fixed vector space

\[
W_0=\sum_{i=1}^q\Phi(u_i,V),\qquad\dim W_0\le qp.
\]

Polynomial continuation from generic v puts every Phi(u,v) in W_0.
Thus the image dimension is at most four. This proves (1).

## 5. Consequence for ordinary source restrictions

The polynomial slice-rank injection and coefficient-coordinate
argument in the earlier note apply without change. For an ordinary
restriction of A(a,b) to a concise square direct sum with common leg
dimension D, put N=abm and k=N-D. At this boundary, every square
block M_n must satisfy

\[
n^2>\max(r,4)ab
\quad\Longrightarrow\quad
n+2k\ge(r+1)ab.
\tag{10}
\]

The strict inequality in the antecedent is essential. The premise
that every lifted rank-one slice has symbol rank at most r follows
from n+2k<(r+1)ab. The theorem bounds the span over the algebraic
closure of F(x,z); selecting independent long-coordinate rows then
injects the original coefficient space into at most max(r,4) copies
of the ab-dimensional biform space. No constant scheme in x,z is
assumed in this final step.

For A(7,8), take r=5,m=14,ab=56,N=784. The proposed ordinary target
M25 plus M5 has D=650 and k=134. Its M25 block would have

\[
625>5\cdot56=280,
\qquad25+2\cdot134=293<6\cdot56=336,
\]

contradicting (10). This does not exclude arbitrary singular
degenerations, and does not establish an improved exponent.

## 6. Exact controls

The standard-library script checks moving pencils for r=2,...,6.
Their endpoint annihilators are z^r and (z-1)^r, so the endpoints
have repeated support. The five parameter values 0,1,2,3,infinity
give 25 exact controls. At each value the script checks every
annihilation equation and recovers its unique normalized annihilator
over the rationals. It verifies the full Hankel rank in every
admissible a<=b format at these parameters. At parameter two, a
coprimality check with the derivative confirms reducedness.

For the same five ranks it also finds the exact primitive integer
relation among the 3r jets at r distinct points. Each highest-jet
coefficient is nonzero, and deleting any one highest jet leaves full
rank m. The stored ranks modulo101 certify the rational rank lower
bounds; every displayed relation itself is checked over the integers.
The tests additionally protect the strict threshold in (10),
including an equality case where no exclusion is made.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/hankel_boundary_dimension.py --output results/anisotropic-constructions-2026-10-20/hankel-boundary-dimension-controls.json
python -S -m unittest discover -s tests -p 'test_hankel_boundary_dimension.py'
```

The finite controls check the formulas and implementation. The
all-size result rests on the written proof in Sections1 through4.
