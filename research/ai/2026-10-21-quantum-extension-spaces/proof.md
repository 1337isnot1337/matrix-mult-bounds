# Minimum matrix rank and the first extension spaces

Written proof, unreviewed. Work over C; the explicit linear algebra is
over Q after four nonzero output row rescalings on each leg.

## 1. Saturation and the concise target

Let T have first-leg dimension a. Write S(t) for the first flattening of
(1,P(t),Q(t))T, where P,Q are regular. Let L0 be the reduction of the
saturation of its row module. It has dimension at most a. The argument
in the pinned quantum-jet-filtration proof gives

    W1 = rowspan S0 + {x S1 : x S0=0} subset L0.

Each matrix in W1 is supported on the sum of the leading output row and
column spaces. If their dimensions are b0,c0, every such matrix has
ordinary matrix rank at most b0+c0. This follows by writing it as the sum
of a matrix with image in im P0 and a matrix supported on im Q0.

Suppose an arbitrary Laurent first-leg map gives a regular tensor with
first-slice space R of dimension d, and every nonzero member of R has
matrix rank at least n. Its regular rows belong to the saturated module,
so R is a subspace of L0. If n>b0+c0 then R intersects W1 trivially.
Consequently

    d + dim W1 <= dim L0 <= a.                         (1)

For M(l,h,n), a first slice is X tensor I_n up to a fixed permutation,
with X an l-by-h matrix. Thus its first-slice space has dimension lh
and minimum nonzero matrix rank n. This proves (1) directly for that
target, without using a slice-rank formula or a monotonicity inference
through additional projections.

For a=112, l=h=10, n=11 and b0=c0=4, (1) says dim W1<=12.
The explicit leading tensor below has rank 12, so necessarily

    W1 = rowspan S0.                                  (2)

This statement is about the final output maps. Constant surjections that
preserve their leading images can be incorporated before applying it.
If they reduce either leading rank, the explicit rank-12 premise must
be recalculated; the classification below makes no claim in that case.

## 2. The normalized leading maps

Index each 112-dimensional source leg by (i,j,z), with 0<=i,j<=3 and
0<=z<=6, flattened as (4i+j)7+z. The 4096 unit source terms have indices

    A=(i,s,6-p-q), B=(p,j,6-r-s), C=(r,q,6-i-j).

For each of the four primitive order-three/six phases inspected in the
leading-flags package, the nonzero output rows are 70,71,73,74. Exact
number-field evaluation and independent row rescaling give the same
four covectors, in the order z=1,2,4,5:

    G_z = e_(0,3,z) - e_(3,0,z).

Let G be their span. For (1,G,G)T, the only nonzero first rows are

    A0 = {(i,s,z): i,s in {1,2}, z in {0,3,6}}.

The twelve rows are independent, as checked by the saved nonzero minor.
The kernel K of the first flattening is therefore the span of the
remaining 100 coordinate covectors. The four-dimensional annihilator of
the leading row space in the 16 output coordinates is also saved exactly.

## 3. Maximal one-sided extension spaces

Define E_B to be the covectors b such that (K,b,G)T=0. The corresponding
400-by-112 constraint matrix has rank 92. A basis of its kernel consists
of the following 20 rows:

    e_(p,j,z),                   p,j in {0,3}, z in {1,2,4,5};
    e_(0,j,z)+e_(3,j,z-3),       j in {1,2}, z in {4,5}.       (3)

The first group has 16 rows; the second has four. They are independent
by their disjoint supports. Substitution verifies that each annihilates
the constraints. The rank-92 minor proves completeness. Swapping the
first two short indices gives the basis of E_C, defined by (K,G,c)T=0.
It has the same dimension and an independent rank-92 certificate.
Both spaces contain G (up to sign after the swap).

Normalize the leading images to the first four output coordinates. In
S1=P1 Q0 T+P0 Q1 T, project the B output away from its leading image.
The second summand vanishes. Equation (2) then says that every new row
of P1 lies in E_B. Similarly every new row of Q1 lies in E_C. Conversely
these conditions kill every outside-leading block of K S1. The block
outside both leading images is automatically zero at first order.

The top four rows of P1 and Q1 can cancel each other. They must satisfy
that K S1 in the 4-by-4 output block belongs to rowspan S0. Pairing with
the four saved annihilator rows yields 400 linear equations in 896
coefficients. Rational elimination and a nonzero modular minor give rank
364, so this coupled solution space has dimension 532. These conditions
are necessary and sufficient for (2), since they account for every output
block of K S1. They do not ensure a matrix target in the limiting space.

For two 110-row output maps the complete linear solution space therefore
has dimension

    2*(110-4)*20 + 532 = 4772.

The report gives the explicit bases, annihilator and rank certificates;
`extensions.py` reconstructs the entire coupled system from all source
terms. There is no grading constraint on the derivatives.

## 4. The bilinear next coefficient

Use the bases (3) and its transpose, listing the sixteen boundary rows
first. Put H=(K,E_B,E_C)T. Exact contraction gives first flattening rank
25. More structurally, H is identically zero on the first sixteen rows
and first sixteen columns together. Every H slice therefore has block
form

    [ 0_(16x16)  X_(16x4) ]
    [ Y_(4x16)   Z_(4x4)  ].

The last four rows have rank at most four, and the remaining rows are
supported on four columns. Every slice has matrix rank at most eight.
The frozen source contraction verifies every coefficient of the zero
block exactly. This is a bound for arbitrary linear combinations, not
an inference from sampled matrix ranks.

For changed first jets satisfying (2), H describes the P1 Q1 contribution
after projecting away both leading output images. The complete second
coefficient also contains P2 Q0 and P0 Q2, and the top first-jet rows can
contribute to blocks meeting a leading image. Neither a rank-eight bound
for the full second coefficient nor an obstruction to all higher jets is
asserted. Constructing or excluding the required saturated rowspace
remains open.
