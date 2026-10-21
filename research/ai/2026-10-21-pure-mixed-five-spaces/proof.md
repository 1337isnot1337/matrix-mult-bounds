# Pure mixed five-spaces are trapped when b is nonzero

Written proof, unreviewed, October21,2026. Claim
`AI-PURE-MIXED-FIVE-SPACES-089`. Work over C with the canonical four-row
leading flags and the source and normal equations of the preceding packages.

Suppose the compatible rank-one partners are

    u=(ab,-a,-b,1), v=(ab,b,a,1), b != 0.

Let B have the complete effective seven-frame and let the effective C
first space V have dimension five and contain the **pure** mixed row
m_C(v). Allow every choice of the remaining four boundary directions,
all higher regular maps, unequal positive first-growth orders, and an
arbitrary Laurent first map. These data cannot yield M(10,10,11).

This does not cover every mixed boundary graph. It establishes no smaller
exponent or stronger global first-rank frontier. The proof is not
independently reviewed or formalized.

## 1. Source scaling reduces to b=1

In each112-dimensional source leg give e_(i,j,z) weight i+j+z. Every
nonzero source term has sum of weights18, directly from the source rule

    A=(i,s,6-p-q), B=(p,j,6-r-s), C=(r,q,6-i-j).

Scaling covectors by lambda^(i+j+z) therefore scales the whole tensor by
lambda^18. A compensating scalar on one map makes this a source
isomorphism for every nonzero lambda. Each leading G_z has both terms
of weight3+z, so its four-dimensional span is preserved.

The four mixed coordinates have weights5,6,6,7. After normalizing the
last coordinate, both partner parameters transform as

    (a,b) -> (a/lambda,b/lambda).

The pure mixed row stays pure, and the maximal compatible frames are
transported with it. Take lambda=b. It suffices to prove the assertion
for b=1 and every complex a. The verifier separately checks the4096
source weights, leading flags and symbolic partner normalization.

## 2. Thirty-six normals and a thirty-two-dimensional quotient

Adopt the complete B-frame normal kernel of dimension88 and the uniform
virtual third tensor from claim088. Its C obstruction Psi(D) is200-by7.
Its virtual C correction error factors through Psi, so the corrections
are valid on V contained in ker Psi(D).

The sixteen adapted source vectors e_(2,s,z)-a e_(1,s,z) have rank-one
third slices modulo Psi. The target rank gap forces those slices to
vanish on V. Because V contains the pure mixed row, column6 of Psi and
column6 of every one of those slices vanish. These are312 linear
equations in the88 normal parameters. Their complete kernel has
dimension36 at every complex a.

A fixed rank52 minor is identity plus a strictly triangular polynomial
matrix after normalization, and the full polynomial kernel has an
identity free-coordinate block. Thus no exceptional a is lost. Four
constant common-plane directions lie in this kernel, and their full
obstruction and projected third tensor are identically zero. Select a
constant complement in the36 free coordinates. This leaves32 quotient
normal parameters d, with all plane motions accounted for separately.

Stack Psi and all rows of the sixteen vanishing third slices into Z(d).
Its rows annihilate V, hence rank Z(d)<=2. Its mixed column is zero.
The joint coefficient matrix in the seven C coordinates and32 parameters
has a uniform44-row basis. A second constant nonzero minor and complete
polynomial rowspace identities certify this at every a. We henceforth
use its six boundary columns, denoted

    (E0,O0,E1,O1,E2,O2).

The row operations depend polynomially on a and are independent of d;
they preserve the pointwise rowspace of Z(d).

## 3. A stable row part and a projection of minimum rank two

Define the three-column projection

    Q(d) = (O0-a^3 E0, O1-a^3 E1, O2-a^3 E2).          (1)

On the joint coefficient matrix, the space of row combinations killed
by (1) has dimension14 uniformly. Its polynomial kernel gives14 rows
W(d) in the rowspace of Z(d), each satisfying

    W_odd = a^3 W_even.                               (2)

The coefficient matrix of W_even has uniform rank26 in the32 normal
parameters. Its complete polynomial kernel K_W therefore has dimension6.

The projection Q has the following stronger property:

    rank Q(d)<=1 implies Q(d)=0.                      (3)

To prove (3), first use a uniform polynomial row basis for Q. Repeated
two-by-two minors with diagonal c1*L(d),c2*L(d) force L(d)=0 whenever
rank Q<=1. All ci are nonzero rational constants. Three rounds have
parameter dimensions

    32 -> 24 -> 16 -> 14.

Every kernel substitution is complete and polynomial, with a fixed
constant nonzero minor. The final Q is identically zero. Conversely,
Q=0 satisfies every forced condition, so the final14-dimensional
polynomial kernel K_Q is exactly ker Q. This proves (3) over all C,
including a=0 and a^3=-1. Every nonzero Q(d) thus has rank at least two.

For fixed a,d, project the rowspace of Z by (1). Its image is the
rowspace of Q, and its kernel contains the rowspace of W. Therefore

    rank Z(d) >= rank Q(d)+rank W(d).                 (4)

If Q(d) is nonzero and W(d) is nonzero, (3)--(4) give rank Z>=3,
contradicting the five-space condition. Consequently every admissible d
belongs to one of two **linear** kernels:

    d in K_W (dimension6), or d in K_Q (dimension14).  (5)

No claim that the entire obstruction space has minimum rank three is
made. Nonzero rank-two controls exist before the remaining target
conditions are imposed. At a^3=-1 the two kernels can overlap. The
argument (4) remains valid and never divides by a^3+1.

## 4. Both linear families vanish under the remaining target conditions

For each family in (5), continue to stack source-slice rows already
proved zero on V into Z. Subtract polynomial combinations of its joint
row basis from the virtual third slices. This preserves their values on V.
Use the unitriangular source change

    e_(2,s,z) -> e_(2,s,z)-a e_(1,s,z),
    e_(i,2,z) -> e_(i,2,z)+e_(i,1,z)

on all64 long-kernel coordinates. It is invertible for every a.

A reduced source slice is certified to have rank at most two either by
a cover of its support by at most two row/column vertices, or by joint
B coefficient rank at most two. In the latter test the coefficient
matrix has polynomial entries: rank at most two over Q(a) means all
three-minors are zero polynomials, so the upper bound remains valid at
every complex specialization. No nonzero minor or generic rank is
asserted at exceptional values.

The old four-row/four-column cross has rank at most eight. A slice of
rank at most two would make its target component have rank at most ten,
below the minimum eleven of Mat10 tensor I11. That component and its
double projection vanish. Add the raw slice rows to Z. Since the pure
mixed row belongs to V, the new mixed columns must again vanish.

For K_W, twelve such source slices force all six parameters to zero.
For K_Q, eight source slices reduce fourteen parameters to two. Repeated
three-by-three minors of Z then force the last two parameters to zero.
Their determinants are nonzero rational constants times cubes of linear
forms. The saved polynomial certificates prove every step uniformly:

    K_W: 6 -> 0;
    K_Q: 14 -> 2 -> 0.

Thus every admissible normal belongs to the four common-plane directions
removed in Section2. All choices of the four boundary directions in V
were retained: only dim V=5 and containment of the pure mixed row were used.

## 5. Shifted induction and the remaining scope

Adopt the shifted-order calculation of the third-boundary proof. At the
first normal error t^N D from moving boundary modules, the off-diagonal
equations occur at N+s_B,N+s_C. Until N+s_B+s_C the corrected residues
lie in the old cross and can be canceled in W0. At the terminal order
the double-new-output coefficient is precisely the virtual tensor used
above, restricted to the actual first spaces. Higher source corrections
and boundary contributions have zero double projection at that order.

The preceding elimination therefore forces a common-plane error at
each induction step. Absorb it into the moving plane and increase N.
Both output maps stay in rank56 boundary modules over C((t)); they
cannot reach the two110-dimensional target legs. Scaling from Section1
completes the b!=0 statement, and the already verified source reversal
transports it to the corresponding opposite chart.

An arbitrary mixed five-space can be W plus span(m_C(v)+h), with h not
in its four-dimensional boundary part W. Such a space need not contain
m_C(v), so Section2's mixed-column equations cannot be assumed there.
Those graphs, remaining partner strata, smaller first spaces and other
leading flags remain open. This is a local exclusion, not a construction
of the target and not an exponent improvement.
