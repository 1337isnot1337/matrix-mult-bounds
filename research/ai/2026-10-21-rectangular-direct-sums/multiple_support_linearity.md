# Linearity obstructs the explicit multiple-support family

October21,2026. Written proof, unreviewed. No improved exponent.

The141-dimensional family in `multiple_support_family.md` has full ambient
linear span, but it still cannot contain the generic rank-two image of an
injective linear map from Mat_(32,33). This excludes that explicit family
as the missing target-leg construction. It does not classify its arbitrary
confluent closure, support at infinity, or all source-rank641 slices.

## 1. The coefficient-dependency exceptional set is too small

A generic family member has one double and six simple support points.
Its seven top residue vectors are G_1,H_1,...,H_6, each a nonzero rank-one
8-by10 coefficient matrix. A rank-one8-by10 cone has dimension17.
Call an ordered tuple good when its vectors are independent, or its only
linear dependence is one proportional pair. The complement has dimension
at most97 in the space of seven unrestricted rank-one matrices.

Here is an elementary incidence count. A minimal dependency circuit of
k>=3 nonzero rank-one matrices has a relation with every coefficient
nonzero. Factor them as u_i v_i^T and absorb those relation coefficients.
If the8-by-k factor matrix has rank l, its dimension is l(8+k-l), and the
10 rows of the other factor lie in its(k-l)-dimensional kernel. Allow the
projective relation coefficients and subtract the k independent column
rescalings. The circuit tuple therefore has dimension at most

    l(8+k-l)+10(k-l)-1,  1<=l<=k-1.

Adding the7-k free rank-one matrices gives maxima97,91,85,80,75 for
k=3,4,5,6,7. If every minimal circuit has size two, the tuple splits into
independent proportionality classes. Two or more independent dependencies
leave at most five classes and dimension at most5*17+2=87. This proves97.

For fixed nonzero G_1=xzAC, its product AC is determined. The possible
G_0 form an affine space of dimension17:

    AC + xC*C[z]_(<10) + zA*C[x]_(<8).

The two summands have dimensions10 and8 and intersect in the line spanned
by xzAC. The support points contribute seven more parameters. Thus family
members with a nongood top-residue tuple form a set of dimension at most

    97+17+7=121.                                      (1)

The extra constraint on G_1 only decreases this upper bound. By contrast,
the rank-two variety in Mat_(32,33) has dimension2(32+33-2)=126. An injective
linear map preserves that dimension, so its generic image cannot be in (1).

## 2. Good top residues force support to be stationary along every line

At a generic point write its minimal support scheme as one double point
and six simple points. Its length is8 and its reduced support length is7.
After a local algebraic root cover, the points and residue vectors are
regular functions of the parameter. For a straight line of source slices,
the second derivative is zero. Modulo the span of jets on Z+Z_red, this is

    sum_i R_i tensor q_i * (dot(lambda_i))^2 = 0.      (2)

Here R_i are the seven top residue vectors. For the double point q_i is
the class of its third evaluation derivative; for a simple point it is
the class of its second evaluation derivative. Lower derivatives and all
residue-derivative terms are in the quotient's discarded jet span.

The discarded scheme has length15 inside the17-dimensional long space.
Every q_i is nonzero, and any two q_i are independent: adding their two
jets makes a scheme of length17, whose evaluations are independent by
Hermite interpolation.

If the R_i are independent, (2) forces every support velocity to vanish.
If there is one proportional pair and no other dependency, first isolate
the other coefficient directions. Their velocities vanish. The pair then
gives a relation between two independent q_i, so those two velocities also
vanish. Thus good tuples have stationary support along every straight line
contained generically in the family.

## 3. Rank-two parameter lines force globally fixed support

Let Phi be a hypothetical injective linear map from the1056-dimensional
matrix parameter space. Its rank-two image is irreducible of dimension126.
Assume its generic member is in the explicit family with all top residues
nonzero and distinct support points. Section1 makes the generic tuple good.

At X=UV of rank two, tangent directions to the rank-two variety are sums
of delta(U)V and U delta(V). Each summand is the direction of a straight
line consisting of rank-at-most-two matrices. Applying Section2 to these
lines forces the differential of the support-scheme map to vanish on the
entire tangent space. In characteristic zero this makes the support scheme
constant on the irreducible generic locus. Its uniqueness follows from the
minimal scalar recurrence, as in the family note.

Consequently the whole generic image lies in one fixed length-eight long
scheme span. With80 biform coefficients, that is a linear space of dimension
8*80=640. Rank-two matrices span the full matrix parameter space, so the
entire image of Phi would lie in that640-dimensional space. This contradicts
injectivity from dimension1056.

If a generic member of the explicit finite-parameter family instead loses a
top residue, its scalar Hankel rank is at most7. The existing two-ruling
lemma and top-Hankel linear-space cap then bound the scalar image by12 and
the full parameter image by12*80=960, again below1056. Thus this boundary
does not evade the contradiction. Arbitrary confluent limits with diverging
residues are not covered by that statement.

## Verification and scope

The finite controls enumerate the circuit incidence bounds and verify the
15-jet rank and all21 two-extra-jet determinants at distinct rational points.
They support the argument but are not independent review or formalization.
The construction itself remains correct: full linear span and large nonlinear
dimension simply do not imply a compatible linear matrix-parameter image.
Other components of the critical source locus remain open.
