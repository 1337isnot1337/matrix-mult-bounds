# The forced central space excludes the standard order-three and order-six flags

Written proof, unreviewed, October 20, 2026. This closes a prescribed
graded family, not the general cyclic-source construction question.

Adopt the canonical Cartan classification
[EXP-CYCLIC-CARTAN-FRONTIER-051](../2026-10-20-cyclic-equivariant/torus.md).
The first matrix leg has dimension 100, and the other two have dimension
110. Up to common translation, the vertex profiles are

    U=V=(1,1,2,2,2,1,1), W=(1,2,2,1,2,2,1).

In the local source indexing used by the quantum package, write grade
w=i+j+z, from 0 to 12. The source leg dimensions by grade are

    S=(1,3,6,10,13,15,16,15,13,10,6,3,1).

The two 110-dimensional target characters equal S except for one missing
coordinate in each of grades 3 and 9. The 100-dimensional first target
character U V* has dimension 16 in grade 6, equal to the entire source
first-leg dimension in that grade. These character facts are adopted;
the independent recursion in profiles.py only checks them again.

## The specified root flags

Let M(q) be the local cyclic matrix in the quantum-recoupling package.
For a primitive root of order three or six, let nu be its minimum entry
valuation at the corresponding cyclotomic polynomial Phi. The regular
matrix Phi^(-nu) M has only four nonzero rows in its constant residue G.
They have row labels

    (1,2,1), (1,2,2), (1,2,4), (1,2,5),

with grades 4,5,7,8. The two roots of each order give four possibilities
for G. Either regular leg may use any of these four residues. Thus there
are sixteen ordered pairs of prescribed leading maps.

For each pair, the exact certificate checks a nonzero coefficient of the
grade-six first-leg projection

    S0=(1 tensor G_B tensor G_C) A4.

It computes the coefficient directly over Q(zeta_6), then independently
checks its reduction modulo the prime 786433. For the common primitive
sixth-root phase, source index 45 and output indices 70,74 give
(zeta_6-1)/1024. Every one of the sixteen phase pairs has a retained
nonzero algebraic coefficient. This proves existence of a nonzero
central matrix; no exact complex tensor rank is inferred from a modular
rank. The separate slice-rank certificates use nonzero modular minors
with explicitly nonvanishing residue denominators.

Every such matrix has rank at most four, since its row and column spaces
are contained in the four-dimensional images of the two leading maps.

## Arbitrary higher jets and the first-leg basis

Allow arbitrary weight-preserving regular lifts P(t),Q(t) of these
leading maps. Allow an arbitrary Laurent map on the first leg, and a
constant weight-preserving surjection from each 112-dimensional large
output leg to its prescribed 110-dimensional target representation.
The latter surjections are isomorphisms on grades 4,5,7,8, since only
grades 3 and 9 lose a coordinate. Hence the nonzero matrix above survives
these surjections and still has rank at most four.

Consider the generic first-leg row space after the two regular maps,
and its saturated limiting row space, as in saturation.md. Its grade-six
part has dimension at most 16: there are only 16 source rows of that
grade. It contains the nonzero rank-at-most-four matrix just found.

If the limiting tensor were the graded matrix target, its grade-six row
space would have dimension 16 by claim 051. It would therefore equal
the entire grade-six part of that saturated space and contain the
nonzero low-rank matrix. But every nonzero first-leg slice of
M(10,11,10), in this leg convention, has the form X tensor I_11 up to
fixed row/column permutations. Its rank is 11*rank(X)>=11. This is a
contradiction.

Thus none of the sixteen prescribed root-flag pairs can yield the graded
target, regardless of the regular higher jets and Laurent first-leg map.
The argument does not bound the degrees of those jets and is not a
finite solver negative. It also explains why the ungraded slice ceiling
104 at orders three and six was insufficient by itself.

Different leading flags, weight-breaking maps or projections, and joint
extraction from powers remain outside this theorem. The full matrix
target and an exponent below 9/4 remain unconstructed.
