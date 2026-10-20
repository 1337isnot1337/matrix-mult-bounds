# Necessary inequalities on fiber means

Written, unreviewed argument for the F4^3:C3 coordinate-potential search.
It gives necessary conditions, not an exponent improvement or a proof that
the whole group cannot work. `quaternary_directions.py` checks the finite
linear maps used below; `quaternary_linear_search.py` uses the conditions
only to reject candidate directions after an exact Farkas check.

Write group elements (a,v), with a in F4* and v in H=F4^3, and multiply by
(a,v)(b,w)=(ab,v+a*w). Suppose each of S,T,U has four points in every scalar
coset, an affine F2-plane. Denote its actual translation-direction plane by
A_a, B_b or C_c, respectively. Thus the translations in S's a-fiber are a
coset of A_a. The normalized planes in the older offset search differ by
scalar multiplication by a^-1.

Take scalar labels a,b,c,a',b',c' satisfying a'*b*c=a*b'*c'. Set r=a/a'
and q=b/b'. The group equation

    s^-1*t * t'^-1*u * u'^-1*s' = identity

on translations is equivalent, in characteristic two, to

    v_s + q*v_t' + r*v_u' = r*v_s' + v_t + q*v_u.

The two sides are affine maps from four-by-four-by-four triples to H. They
are bijective exactly when, respectively,

    A_a + q B_b' + r C_c' = H,
    r A_a' + B_b + q C_c = H.

Here equality means a direct sum; each plane has F2-dimension two. Offsets
only translate these bijections, and therefore do not affect bijectivity.
If both conditions hold, matching their 64 values gives 64 group relations.
If the scalar triples differ, all 64 are extra terms, since at least one
vertex and its primed partner belong to different scalar cosets.

The potential row of each relation is

    phi_s - phi_s' + phi_t' - phi_t + phi_u' - phi_u.

Every point in each of the six fibers appears 16 times in the appropriate
position when the 64 relations are summed. If mu_(S,a) denotes the average
potential of the four points of that fiber, strict positivity of every
extra term forces

    mu_(S,a) - mu_(S,a') + mu_(T,b') - mu_(T,b)
                         + mu_(U,c') - mu_(U,c) > 0.

Consequently any positive integer dependence summing such nine-variable
rows to zero is an exact obstruction for those plane directions, for every
offset choice. The verifier enumerates the two six-dimensional sum maps
and checks the dependence with integers. SAT and floating LP do not supply
the mathematical acceptance condition.

This also explains why changing only the offsets in a graph-plane family
can keep producing pair-injective sets while never yielding valid positive
potentials. It does not establish that every possible direction family has
such a dependence, or cover nonplanar four-point fibers.

## A whole base family is excluded without searching offsets

Suppose one complementary triple of actual fiber planes A_1,B_1,C_1 has
both B_1+C_1 and A_1+C_1 invariant under F4 scalars. This includes three
coordinate F4 lines and the earlier graph-into-C examples. The other fiber
planes may be arbitrary.

The same-coset abelian restriction forces every A_a+B_b+C_c to be a direct
sum H: its 64 triple sums must be distinct in the order-64 group. Fix any
d!=1 in F4*. The crossed labels a=b=d,c=1,a'=b'=c'=1 have both crossed
sums bijective: their direction sums reduce to A_d+B_1+C_1 and
A_1+B_d+C_1. Thus they force the strict mean row

    mu_(S,d)-mu_(S,1)+mu_(T,1)-mu_(T,d)>0.

The reverse labels a=b=c=1,a'=b'=d,c'=1 also have both crossed sums
bijective. Scalar invariance of B_1+C_1 and A_1+C_1 preserves transversality
after multiplying A_d and B_d by d^-1. The resulting row is the negative
of the preceding one. This is impossible.

Hence the entire family with this base-triple property is excluded, even
when all six other plane directions and all offsets vary. The 2000-model
coordinate-base run is an experiment illustrating this argument; its
model limit is not the basis of the all-family statement. Searches with
different base triples are separate and are not excluded by this lemma.
