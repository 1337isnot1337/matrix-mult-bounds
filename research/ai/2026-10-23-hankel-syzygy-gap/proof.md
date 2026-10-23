# Degree-one Hankel syzygies and the A4 cap23 linear-space bound

October23,2026. Owner-directed OpenAI Codex work over C. Written and
unreviewed; no independent mathematical review or formalization.

## 1. Source and result

Adopt the canonical cyclic source A4. Its minimum nonzero source slice
rank is16. The prior below-rank32 theorem says every such slice is
g tensor h, with g a biform of bidegree(3,3) and h a coherent middle
factor. On a linear source space below32, h is fixed. Source matrix rank
then equals the rank of the28-by28 coefficient map R(g), whose entry is

    R(g)_((j,L),(H,r))=g_(H-j,L-r),

with j,r in0..3, H,L in0..6 and out-of-range coefficients zero.

We prove:

> Every vector subspace of A4 source slices of rank at most23 has
> dimension at most eight. This bound is attained already at rank20.
> Consequently there is no A4 to M(10,10,11) formal degeneration if
> either scalar-balanced long-map leading rank is at least102, with
> arbitrary finite poles in both other maps and the original unit lift.

This strengthens the earlier cap20/rank105 criterion. It does not
construct the full matrix target or exclude smaller leading ranks.

## 2. A polynomial symmetric rank-one factorization

If a nonzero symmetric polynomial matrix A(t) over C[t] has rank one
over C(t), write its rational column line as C(t)v(t), with v primitive
over C[t]. Symmetry gives A=c(t) v v^T. Since the components of v have
gcd one, their pairwise products also have gcd one; polynomial entries
of A force c in C[t]. Therefore

    degree A=degree c+2 degree v.                       (1)

There is no cancellation in a diagonal entry of a component of maximal
degree. In particular degree A<=1 makes its column line constant, and
degree A<=2 makes v have degree at most one.

## 3. Rank-two Hankel pencils have one fixed length-two support

Let q(t)=(q_0(t),...,q_6(t)) have entries of degree at most one, and
let Q(t)=(q_(i+j)(t))_(0<=i,j<=3). Suppose Q has generic rank two.
We first obtain a nonzero constant cubic w in its common kernel.

The second compound C_2(Q) is symmetric, has degree at most two and
has rank one over C(t). By (1) its column line has a primitive generator
v(t)=v_0+t v_1. These are Pluecker coordinates of Im Q(t). If v is
constant, those two-dimensional images lie in a fixed two-space. If its
coefficients are independent, the identity v(t) wedge v(t)=0 makes v_0
and v_1 decomposable and v_0 wedge v_1=0. Their two-planes intersect
in a line and together span a three-space T. Every Im Q(t) lies in T.
Thus in either case all images lie in a constant space of dimension at
most three. Symmetry puts a nonzero constant vector w in every ker Q(t).
The argument takes place over C(t), so its polynomial identities also
hold at parameters where rank drops.

Interpret q(t) as a functional on binary sextics and w as a binary cubic.
The common-kernel equation says q(t) annihilates w*S_3. Its fixed
three-dimensional quotient is the space of values and jets on the length-three
zero scheme D of w, by the prior Hermite-interpolation lemma. Choose a
constant coordinate with no point of D at infinity. In the corresponding
jet basis, q(t)'s coefficients a,b,c are polynomial and linear in t.
The multiplication pairing on cubic forms has one of the following
three-by-three Gram matrices:

* Three distinct points: diag(a,b,c), determinant a*b*c.
* A double point and a simple point: [[a,b,0],[b,0,0],[0,0,c]],
  determinant -b^2*c.
* A triple point, using second derivative divided by two:
  [[a,b,c],[b,c,0],[c,0,0]], determinant -c^3.

Evaluation and jet columns on cubics are independent, so these Gram
matrices have the same rank as Q. Rank at most two makes the indicated
determinant identically zero in the integral domain C[t]. In the first
case one coefficient vanishes identically. In the second, either b or c
does; in the third, c does. In every case the entire pencil is supported
on one fixed subscheme D_2 of D of length at most two. Generic rank two
forces length exactly two. The argument includes constant pencils and
multiple roots. Homogeneous coordinates include support at infinity.

For its quadratic equation h, the cubic kernel of Q(t) is therefore

    h*S_1, over C(t).                                  (2)

The two corresponding fixed evaluation/jet vectors in the sextic dual
annihilate h*S_4. These details follow from the same multiplication and
Hermite bases, including a double point. No Kronecker classification is
imported into this argument.

## 4. No positive degree-one kernel generator at primitive degree at least two

Write g(x,z) as a cubic in z and remove the common x divisor of its four
coefficient forms. Let the resulting primitive vector f(x) have degree
d. Its four-row multiplication matrix H_f(x) has rows z^r f(x,z), r=0..3,
and seven coefficient columns. Suppose d>=2.

We show every degree-at-most-one polynomial q(x) in ker H_f is generated
by constant kernel vectors, with scalar coefficients of degree at most one.
The equations are

    Q(q(x)) f(x)=0,                                    (3)

where Q is the symmetric4-by4 Hankel pencil from Section3. If q is
nonzero, Q is nonzero and its generic rank is at most three.

If rank Q=3, its adjugate is a nonzero symmetric rank-one polynomial
matrix of degree at most three. Formula(1) gives a primitive generator
of ker Q of degree at most one. Since f is primitive and spans that
same rational kernel line, it is a constant multiple of this generator.
This contradicts d>=2.

If rank Q=2, Section3 supplies a fixed quadratic h(z), with q(x) in
the constant length-two sextic jet space. By (2), f(x,z) is divisible
by h(z). Every vector of that constant jet space therefore annihilates
all z^r f(x,z), since these lie in h*S_4. In particular both coefficient
vectors of q(x) are constant elements of ker H_f, as required.

If rank Q=1, (1) applied directly to the linear polynomial matrix Q
makes its column line constant. Q, and hence q, is a scalar linear
polynomial times a constant matrix/vector. Equation(3) makes that constant
vector a constant kernel vector. Rank zero would make q zero.
This proves the assertion for every primitive degree d>=2.

The prior kernel-bundle splitting over P^1(C) has degrees mu_1,mu_2,mu_3.
Constant generators are exactly the degree-zero summands. A positive
mu_j=1 would contribute a degree-one section not generated by constant
sections. The proved assertion excludes it. Thus

    d>=2 ==> every positive mu_j is at least two.       (4)

The degree hypothesis matters: primitive degree-one examples do have
degree-one generators. It is retained in the theorem and exact controls.

## 5. The cap23 factor containment

The prior exact coefficient-map formula is

    rank R(g)=16+sum_j min(4,mu_j),
    mu_j>=0,               sum_j mu_j=4d.              (5)

It uses the existing Grothendieck splitting theorem with the stated
complex projective-line hypotheses. If d<=1, g has a quadratic x divisor.
Otherwise d=2 or3. At rank at most23, the truncated sum in (5) is at
most seven. If all three degrees were positive, (4) makes each at least
two. If all were at most four, their sum would be4d>=8. If one exceeds
four, it contributes four and the other two contribute at least four
together. Both cases contradict the cap seven. Hence some mu_j=0,
giving a nonzero constant q in ker H_f.

Such a q forces a common linear z divisor. Indeed its constant Hankel
matrix Q is nonzero and annihilates every z-coefficient vector of f.
If rank Q=3, its kernel is a single constant cubic, so f is separable
in z. If rank Q=2, the constant case of Section3 gives a fixed quadratic
divisor. If rank Q=1, the Hankel rank-one identities make q an evaluation
at one projective point; every kernel cubic vanishes at that point.
For the last statement, write Q=c u u^T. If u_0 is nonzero, the Hankel
identities make u_i proportional to powers of one scalar; if u_0=0,
they successively force u_1=u_2=0, leaving the endpoint at infinity.
Restoring the removed x divisor preserves the z divisor.

Apply the same reasoning after transposing the biform map. A biform
outside the quadratic-x and quadratic-z families has primitive degree at
least two in both variables, so has a linear divisor on both sides.
Thus every cap23 biform lies in the union of three projectively closed
factor families:

    V_x2,          V_z2,          V_x1z1.               (6)

These are multiplication images of products of projective coefficient
spaces. This is a containment, not a classification of which members
of the third family have rank22 or23. The same argument also excludes
source rank21: at d>=2 the truncated sum five would require a positive
degree one, while d<=1 gives ranks16 or20.

## 6. Linear spaces in the factor families

We use the following consequence of the prior generic-pencil gcd lemma.
Let W be a linear space of b-component binary forms of degree D, all
of whose nonzero elements have a common divisor of degree at least e.
Fix f_0 in W. Every g rationally independent of f_0 shares a degree-e
divisor with it: the generic pencil has common-divisor degree at least e,
and the pencil lemma identifies it with the joint gcd. There are only
finitely many degree-e divisors of the fixed gcd of f_0. Hence W is
contained in a finite union of fixed-divisor linear spaces and the linear
space of forms rationally proportional to f_0. A vector space over C
cannot be a finite union of proper linear subspaces. Therefore either
W has one fixed degree-e divisor, or all its elements are rationally
proportional to f_0. In the latter case f_0=h v with v primitive, and
W is contained in S_(degree h)*v, of dimension at most D+1.

The first two families in (6) have sharp linear-space dimension eight
by the prior rank20 proof. Suppose W lies in V_x1z1. If dim W>4, the
preceding lemma in x gives one fixed linear x divisor. Divide it out;
the coefficient vector now has three components as a cubic in z.
Applying the same lemma in z gives either dimension at most four, or
one fixed linear z divisor and dimension at most3*3=9.

Dimension nine is impossible at rank cap23. Equality would make W
the entire space h_x h_z*(S_2(x) tensor S_2(z)). It contains a rank24
slice: choose the biform (X_0 Z_0+X_1 Z_1)^2 after factoring out the two
linear divisors. Removing and restoring univariate common factors does
not change the coefficient-map kernel, as in the prior gap proof; the
rank of this displayed biform map is24. Its literal exact witness is
checked separately. Thus dim W<=8 in this third family as well.

A linear space contained in the finite union (6) lies in one of its
closed components. The coherent middle factor is fixed on the original
source linear space. Therefore every source linear space at cap23 has
dimension at most eight. A fixed quadratic divisor times the full
bidegree(1,3) space, with a fixed coherent middle factor, attains eight.

## 7. Laurent consequence and the cap24 boundary

Use the prior shared-correction target-ruling theorem with

    N=112, R=110, k=2, m=10, n=11, mu=16.

If a regular long map has leading rank c>=102, its source cap is
11+2+112-c<=23. The proved linear-space bound is8<10, and its nonzero
lift margin is16-(112-c)-2>=4>0. The theorem excludes the complete
A4 to M(10,10,11) Laurent degeneration, allowing arbitrary finite poles
in both other maps and in the original identity lift. Scalar balancing
and transposition give the same exclusion when either balanced long-map
leading rank is at least102. Every remaining candidate has both ranks
at most101; existence of such a candidate remains open.

At c101 the cap becomes24. A fixed linear x divisor times all forms
of bidegree(2,3) is a twelve-dimensional source linear space of rank at
most24: after dividing that factor, (5) has d<=2 and truncated sum at
most eight. This supplies a ten-dimensional subspace as well. Thus the
uniform source-dimension hypothesis used here fails at cap24. It does
not rule out an improvement using additional target structure.

## 8. Attribution and evidence limits

The source, coherent-factor theorem, splitting formula and its external
Grothendieck1957 Theorem2.1 over P^1(C), prior generic-pencil gcd lemma,
rank20 dimension bound and shared-correction criterion retain their
original credit and exact pins. The Hermite jet argument is the prior
local length-two source geometry. The symmetric adjugate/compound
derivation, degree-one syzygy exclusion and cap23 application are local
continuations, with no historical priority claim or new imported
classification theorem.

Exact finite controls support the polynomial identities, kernel counts
and literal ranks. They do not prove the universal statements, formalize
arbitrary series or supply independent mathematical review. No complete
degeneration exclusion, matrix construction or exponent improvement follows.
