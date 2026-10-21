# Constant matrices admit a polynomial flag normal form

AI-derived written argument, 2026-10-20. Unreviewed; no exponent improvement.
The generic-position ingredient is the elementary nonvanishing of a
Wronskian in characteristic zero. No historical priority is claimed.
For a primary reference on this classical fact, see Bostan and Dumas,
[Wronskians and linear independence](https://arxiv.org/abs/1301.6598),
arXiv:1301.6598v1, 2013 (journal publication 2010). Only the polynomial,
characteristic-zero case is used below, with its argument supplied here.

Put D=m-1, N=m(m+1)/2, and work over C. Consider constant matrices G,P,Q
applied to C(m,B), followed by diagonal parameter weights on target X,Y,Z.
Suppose the resulting limit is canonical T_m. Then the constant maps have
full target rank, since the target is concise and flattening rank cannot
increase at a limit.

This note concerns that constant-matrix-plus-diagonal-weight class. It does
not reduce an arbitrary Laurent input matrix to a constant matrix.

## 1. Allowed constant row operations

Order the target coordinates of one leg by strictly increasing parameter
weight. If L is unit lower triangular in this order and D(epsilon) is the
diagonal weighting, then

    D(epsilon) L D(epsilon)^(-1) -> I.

Thus replacing that leg's constant matrix M by LM preserves its limiting
target. This uses a regular parameter-dependent operation with identity
limit; it does not assert the constant tensors before weighting are equal.

Distinct coordinate weights can be assumed for this existence question.
Every nonzero unwanted coefficient in a valid constant tensor has strictly
positive weight. A sufficiently small rational perturbation within the
target's compatible grading preserves all those inequalities. Wanted terms
stay weight zero and unwanted zero coefficients stay zero. Avoid the finite
hyperplanes where coordinate weights tie, then clear denominators.

The compatible weights have the form

    wX(p)=gamma+beta*p,
    wY(u,a)=eta_u-beta*a,
    wZ(u,c)=-gamma-eta_u-beta*c.

Indeed the sector C(2,m-1) forces constant successive differences of wX;
the other equations then give the displayed formula. Reversing the binary
degree coordinates allows beta>0 after generic perturbation. In the current
pilots gamma=0 and beta is a positive integer.

## 2. One source automorphism makes all flags generic

Interpret the rows of G and P as polynomials of degrees at most D and B-1.
Interpret Q's rows as linear functionals on polynomials of degree B+D-1.
Multiplication of homogeneous binary forms is GL(2)-equivariant. A common
constant change of its two variables acts on G,P and contragrediently on Q,
leaving the source tensor unchanged.

For any independent r polynomials, their Wronskian is not the zero
polynomial. Choose a basis of their span with distinct polynomial degrees.
The leading Wronskian coefficient is a nonzero product of their leading
coefficients and the Vandermonde determinant of those distinct degrees.
Characteristic zero is used here.

Apply this fact to every prefix of each ordered row flag. For the Q flag,
use the equivariant apolar identification of the dual binary-form space;
in monomial coordinates its coefficient reversal has nonzero binomial
factors. There are finitely many nonzero Wronskians. Choose a projective
point where they all are nonzero and move it to infinity by GL(2).

All leading jet minors for G and P and the opposite minors for Q are now
nonzero. Using the permitted row operations of section 1 gives:

- G row p has degree D-p, for p=0,...,D.
- P row y has degree B-1-rankY(y), where rankY orders its target weight.
- Q row z annihilates all monomials of degree below rankZ(z), where rankZ
  orders its target weight. Its value on that pivot monomial is nonzero.

Every stated leading/pivot coefficient is nonzero. Prefixes have full rank
because the constant maps have full target rank. The same argument applies
when B>N and P,Q are rectangular.

## 3. A combinatorial obstruction

The constant tensor coefficient at (p,y,z) is Q_z(G_p P_y). If

    (D-p)+(B-1-rankY(y))=rankZ(z),                       (1)

the product polynomial has degree exactly Q_z's first nonzero monomial.
The coefficient is exactly the product of three nonzero pivot coefficients.
It cannot vanish. Consequently a valid degeneration requires every such
entry to have positive parameter weight, or weight zero at an actual target
term. A negative weight, or a weight-zero unwanted term, is a certificate
of nonexistence in this whole constant-matrix class over C.

This is stronger than rejecting one numerical basis. It allows arbitrary
constant matrices on all three legs, but remains a grading-specific
obstruction. Passing it is only a necessary condition.

For m=4,B=10, beta=1, eta=(7,14,21,0), the entry p=1,
Y_(0,3),Z_(0,3) satisfies (1). Its three source degrees/pivots are 2,6,8.
Its weight is 1+0-7=-6. This excludes the weight order that produced the
smallest residual in the earlier 24-order fit. Five other entries provide
the same obstruction. The earlier floating sequence is not a witness.

More generally, suppose eta_m is the smallest sector offset, eta_1 is next,
eta_1-eta_m>D*beta and eta_u-eta_1>D*beta for every other sector. Such a
grading requires B>=N+m-1. To see this, write B=N+s with 0<=s<=m-2. The
Y_(0,D) row has rank m-1 and degree B-m. The Z_(0,D) row has rank N-2.
Choose p=s+1. Its source degree D-p plus B-m equals N-2, so the coefficient
is forced nonzero, but its weight beta*(s+1)+eta_m-eta_1 is negative.
Generic perturbation handles ties between the remaining sector coordinates
without changing these separated groups or any valid limiting tensor.
This is a whole grading cone obstruction; its additive overhead does not
exclude the general asymptotic construction premise.

## 4. Gauge anchors for discovery

For a fixed strict weight order, this normal form cuts the m=4,B=10
constant matrices from 246 complex entries to 150 triangular entries.
The compatible target diagonal stabilizer has dimension m+2. If lambda_D
and lambda_(D-1) are the last two G pivot coefficients, use the target
scaling X_p->gamma*s^p X_p with s=lambda_(D-1)/lambda_D and an appropriate
gamma to make those two pivots one. In each Y sector, use its independent
Y/Z inverse scaling to set the a=0 row's pivot to one.

The source affine substitution can then make G_(D-1)=t and G_D=1. It
preserves all polynomial-degree flags and the pivot normalizations. This
leaves 143 free complex coefficients at m=4,B=10: seven in G, 51 in P,
and 85 in Q. Solving Q linearly leaves 58 nonlinear complex parameters.

These counts describe a discovery parametrization. Numerical residuals,
including complex residuals or Jacobian controls, remain insufficient for
a construction. A successful candidate needs exact coefficient replay and
then the unbounded construction and exponent argument.
