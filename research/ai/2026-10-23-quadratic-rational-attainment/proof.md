# Exact rational attainment of the quadratic rank defect

October 23, 2026. Owner-directed Codex research, written and unreviewed.
Checking in this package belongs to the generating session. It is not
independent mathematical review or formalization. The result concerns a
single crossed biform source block; it provides no tensor construction
or improved matrix-multiplication exponent.

The two-index formula and balanced four-value containment are prior
results of the merged [kernel-index package](../2026-10-23-quadratic-kernel-indices/README.md).
The recurrence/line-bundle correspondence, including singular curves,
is prior work in the merged [torsion package](../2026-10-23-quadratic-torsion/README.md).
The new conclusion here is the exact attainment criterion over Q. Its
necessity uses Mazur's theorem with its original attribution; sufficiency
uses four explicit integer polynomial identities. Sources and exact
versions are pinned in [sources.json](sources.json).

## 1. Statement and literal source

Let a>=3 and let

    f(x,z)=u_original(x)+z v_original(x)+z^2 w_original(x)

be nonzero over Q, with each coefficient polynomial of degree below a.
Use the full crossed source matrix

    R_(a,a)(f)[(j,L),(H,r)] = [x^(H-j) z^(L-r)] f,
    0<=j,r<a,                  0<=L,H<2a-1.              (1)

In particular, this is an a(2a-1)-square matrix with every source
endpoint retained. At most a(a+2) rows can be nonzero for a
quadratic-in-z slice; “full active rank” below means that number.

**Theorem.** For every a>=3 the exact set of nonzero ranks in (1) is

    {a^2, a^2+a, a^2+2a}
       union {a^2+2a-1 : gcd(a+1,210)>1}.                 (2)

Thus the one-unit defect a^2+2a-1 is attainable over Q exactly when
a+1 has a prime divisor in {2,3,5,7}. This does not assert that the
order of every relevant line bundle divides 210: orders such as 8,
9 and 12 are compatible with the external torsion bound. Only their
prime divisors matter for this existence statement.

The scope is quadratic-in-z slices with the indicated x-degree bound.
For a>3 this is not the whole biform coefficient space or a classification
of a full cyclic source. The argument uses no unmerged split-family
result.

## 2. Precise inherited reduction

Divide the three coefficient polynomials by their monic common gcd and
denote the primitive triple by u,v,w. Put D=max(deg u,deg v,deg w).
The prior kernel-index formula proves that this common-gcd operation
does not change the rank under the original degree bounds. The balanced
containment in Section 7 of its dichotomy note is

    rank R_(a,a)(f) in {a^2,a^2+a,a^2+2a-1,a^2+2a}.       (3)

It also proves that a one-unit defect requires D=2 and no fixed rational
homogeneous z-root:

    u s^2+v s t+w t^2 is not the zero polynomial
                           for every [s:t] in P1(Q).     (4)

Homogenize u,v,w to degree two in X and form

    F(X,Z)=U(X) Z0^2+V(X) Z0 Z1+W(X) Z1^2,
    C=V(F) in P1_X x P1_Z,       L=O_C(1,-1).             (5)

Theorem A of the prior torsion proof applies exactly to (4). The bundle
L is nontrivial and has degree zero on every geometric component. For
every n>=2, define T_n to be the coefficient matrix of

    u lambda_r+v lambda_(r+1)+w lambda_(r+2)=0,
    0<=r<n-1,  0<=j<=n,  deg lambda_j<=n-2.              (6)

All coefficients in degrees 0,...,n are equations. This is an
(n^2-1)-square matrix, and the prior theorem gives

    ker T_n = H0(C,L^n),
    dim ker T_n = 1 if L^n is trivial, and 0 otherwise.   (7)

At n=a+1, equation (6) is the complete bounded source-kernel recurrence,
so

    rank R_(a,a)(f)=a^2+2a-1  iff  L^(a+1) is trivial.    (8)

These facts require neither smoothness nor C(Q) nonempty. The prior
proof explicitly identifies the coefficient map using Laurent monomials
in a Cech calculation, so (6) has no suppressed endpoints, derivative
coefficients or characteristic-dependent binomial normalization.

We also use the following already-proved geometric facts. Over Qbar,
C is integral of bidegree (2,2), the union of two smooth (1,1) graphs,
or a doubled smooth (1,1) graph; there are no vertical or horizontal
components. Moreover H0(C,O_C)=Q and h1(C,O_C)=1, also after base
extension. Actual line bundles and their powers are trivial over Q
exactly when they become trivial over Qbar. Indeed flat cohomology base
change then supplies a nonzero rational section, whose geometric
extension is a nonzero constant trivialization and hence has no zeros.
Faithful flatness reflects this property. This argument concerns an
actual bundle over Q, not descent of an arbitrary invariant geometric
Picard class; in particular it preserves its exact order.

## 3. Necessity: smooth curves

Suppose (8) holds, and let d be the order of L. Then d>1 and d divides
a+1. If C is smooth and geometrically integral, it is a smooth proper
genus-one curve. Its Jacobian J exists over Q even if C has no rational
point. The natural map from actual degree-zero line bundles on C into
J(Q) is injective, and dim J=1. Thus J, equipped with its identity,
is an elliptic curve over Q, and the image of L is a rational point of
exact order d. These are [Milne's Theorem 1.1, Remark 1.5 and Proposition
2.1](https://www.jmilne.org/math/xnotes/JVs.pdf), in the revision dated
June 12, 2021, pages 2, 4 and 5 respectively. Proposition 2.1 is the
dimension statement; no rational point on C is chosen here.

[Mazur's torsion theorem](https://www.numdam.org/item/PMIHES_1977__47__33_0.pdf),
Chapter III, Section 5, Theorem 5.1 and Corollary 5.2, printed page 156
of the 1977 paper, gives the possible orders of a rational torsion point:
they are at most 10 or equal 12. Therefore every prime divisor of d is
one of 2,3,5,7. Since d>1 divides a+1, this proves gcd(a+1,210)>1 in
the smooth case. This imports Mazur's theorem; it does not supply a new
proof or a strengthening of that theorem.

## 4. Necessity: singular and doubled boundaries

Put k=Qbar. First suppose C_k is reduced and geometrically singular.
Its normalization is one P1, or two P1s in the two-component case.
Consider the group G of geometric line bundles of degree zero on each
component. Their pullbacks to the normalization are trivial. The
normalization/gluing unit sequences show that G is algebraically G_a
or G_m. Here is the exact genus bookkeeping behind this use: gluing
points on different connected components introduces no Picard kernel;
gluing two points within a connected component introduces G_m; a
tangent contraction introduces G_a. The normalization has h1=0 and
C_k has h1=1, so there is exactly one genus-increasing step. These are
[Stacks 53.15.4--6](https://stacks.math.columbia.edu/tag/0C1H), together
with the h0/h1 bookkeeping in the proof of
[53.17.3](https://stacks.math.columbia.edu/tag/0C20), applied over the
algebraically closed field k. The identification is by algebraic gluing
parameters, not merely an abstract group isomorphism.

If G is additive, it has no nonzero torsion in characteristic zero.
The nontrivial class L_k therefore has infinite order and cannot satisfy
(8). If G is multiplicative, choose an algebraic-group coordinate and
let zeta in k^* represent L_k. Transporting Galois through this coordinate
gives actions

    t |-> sigma(t)^(epsilon_sigma),
    epsilon_sigma in {1,-1}.                              (9)

After coefficient conjugation is removed, the action is an algebraic
group automorphism of G_m. Such an automorphism is identity or inversion:
units of k[t,t^-1] have form c t^m, preservation of the identity forces
c=1, and invertibility forces m=1 or -1. Equivalently, in the nodal
case the two branches give one gluing ratio; in the two-component case
the two intersection points give a cycle ratio. Permuting these data
can only invert that ratio. Conjugate branches or components are
therefore included.

The actual Q-defined bundle has an invariant geometric class. Equation
(9) implies sigma(zeta) is zeta or zeta^-1 for every sigma, hence

    [Q(zeta):Q] <= 2.                                    (10)

If a prime ell divides the finite order d of zeta, then
eta=zeta^(d/ell) is a primitive ell-th root of unity in Q(zeta).
The polynomial Phi_ell(X)=1+X+...+X^(ell-1) is irreducible over Q:
Phi_ell(Y+1)=((Y+1)^ell-1)/Y is Eisenstein at ell. Thus
[Q(eta):Q]=ell-1<=2, forcing ell=2 or 3. This rules out any further
prime from a nonsplit multiplicative boundary without assuming that
every Galois-invariant geometric class descends.

Finally suppose C_k=2D for a smooth (1,1) graph D. Its square-zero
ideal is I=O_D(-D)=O_P1(-2). The unit sequence for a square-zero
thickening, [Stacks 37.4.1](https://stacks.math.columbia.edu/tag/0C6Q),
identifies 1+I with the additive sheaf I. Constants lift from D to 2D,
and therefore

    ker(Pic(2D) -> Pic(D)) = H1(P1,O(-2)) = (k,+).         (11)

The restriction of L_k to D is trivial, so its nonzero class lies in
this torsion-free kernel. This boundary also cannot satisfy (8).
Preservation of the order of actual bundles under base extension, as
explained in Section 2, completes every descent step. All singular
cases consequently introduce only the primes 2 and 3, and necessity
of gcd(a+1,210)>1 follows in full generality.

## 5. Four explicit prime-order certificates

The following four polynomials have primitive degree-two coefficient
triples and no fixed rational homogeneous z-root:

    q2 = x^2-z^2,
    q3 = x^2+xz+z^2,
    q5 = 1-x-z+x^2 z^2,
    q7 = 1-x-z-xz+4x^2 z^2.                              (12)

For q2 and q3 a coefficient is a nonzero constant. For q5 the middle
coefficient is -1. For q7 the first two coefficients 1-x and -1-x
are coprime because their difference is 2. These prove primitivity.
In the fixed-root identity us^2+vst+wt^2=0, the x^2 coefficient forces
s=0 for q2 and q3, then the constant coefficient forces t=0. For q5
and q7 the x^2 coefficient first forces t=0, and then u forces s=0.
Thus (4) holds in every case.

For q2 the nonzero tuple (0,1,0) is in ker T_2. For q3 the tuple
(0,1,-x,0) is in ker T_3. For q5 and q7 the following arrays give the
coordinates lambda_0,...,lambda_p in ascending powers of x. Zeros at
the displayed degree endpoints are intentional.

    p=5, each row [constant,x,x^2,x^3]:
    [-1, -2,  1,  2]
    [-1, -1,  2,  1]
    [-1,  0,  2,  0]
    [-1,  1,  1,  0]
    [-1,  2,  0,  0]
    [ 0,  1,  0,  0]

    p=7, each row [constant,x,x^2,x^3,x^4,x^5]:
    [-4, -44, -140, -36, 384, 320]
    [-4, -36,  -76,  68, 240,  64]
    [-4, -28,  -28,  92,  96,   0]
    [-4, -20,    4,  68,  16,   0]
    [-4, -12,   20,  28,   0,   0]
    [-4,  -4,   20,   4,   0,   0]
    [-4,   4,    8,   0,   0,   0]
    [-3,   6,    1,   0,   0,   0]                      (13)

These arrays satisfy the integer polynomial identities

    (1-x)lambda_r-lambda_(r+1)+x^2 lambda_(r+2)=0,
                                              0<=r<4,
    (1-x)lambda_r-(1+x)lambda_(r+1)
                         +4x^2 lambda_(r+2)=0, 0<=r<6,  (14)

respectively. They can be verified by direct multiplication of the
displayed rows. Together with the one equation for q2 and two for q3,
there are thirteen polynomial identities, including the first and last
equations in each recurrence. The exact verifier reconstructs both
these polynomial products and the full coefficient matrices.

Equations (7), (13) and (14) give L^p trivial for the corresponding
prime p. Since L itself is nontrivial, its order is exactly p. Neither
a smoothness assertion nor a conversion to an elliptic model is needed
to certify these orders. T_2 and T_3 are auxiliary cohomology matrices;
they are not source-rank claims at the excluded sizes a=1 and a=2.

For any a>=3 with p dividing a+1, q_p has its coefficient degrees below
a and L^(a+1) is trivial. Equation (8) supplies the required defect.
This proves sufficiency for every a in (2).

The integer identities give a useful, separate field scope. The
order-2, order-3 and order-5 tuples remain nonzero and their triples
remain primitive of degree two without a fixed homogeneous root over
every field; their displayed tuples contain a coefficient 1 or -1.
The order-7 assertion remains valid in characteristic different from
2: the coprimality and leading coefficient 4 survive, and the last
coordinate has x^2 coefficient 1. Thus gcd(a+1,30)>1 suffices for a
defect over every field, and gcd(a+1,210)>1 suffices in characteristic
different from 2. These are sufficient conditions only outside Q.
In characteristic 2, q7=(1+x)(1+z), whose primitive triple has degree
zero; the order-7 certificate is explicitly excluded there. No finite
field sweep is asserted for this consequence of the integer identities.

## 6. The other ranks and completeness

The slices 1 and 1+xz attain a^2 and a^2+a respectively by the prior
two-index formula. To obtain full active rank over Q at every a>=3,
use q=(z-x)^2. This is a primitive degree-two triple without a fixed
homogeneous root. We give a direct calculation, with no split-family
dependency. Set n=a+1. Every solution of its recurrence is determined
by P=lambda_0 and Q=lambda_1, and induction gives

    lambda_r=x^(r-1)(r Q-(r-1)xP),    1<=r<=n.           (15)

If all coordinate degrees are at most n-2, the last coordinate in
(15) forces n Q-(n-1)xP=0. Since n is invertible in Q, substitute
Q=(n-1)xP/n into the preceding coordinate to obtain

    lambda_(n-1)=x^(n-1)P/n.

The same degree bound forces P=0, and hence Q=0 and the entire tuple
zero. Thus ker T_n=0, and (7)--(8) give rank a^2+2a. Combined with
the four-value containment (3), the necessity in Sections 3--4 and
the positive certificates in Section 5 prove the exact set (2).

## 7. Finite verification and evidence limits

The companion verifier independently constructs (1) and (6), uses exact
rational elimination, and checks the four integer tuples. It imports no
prior verifier implementation. The bounded report records four exact
recurrence ranks (2 of 3, 7 of 8, 23 of 24 and 47 of 48), the thirteen
polynomial equations, and ten full rational source matrices. One separate
F2 source at a=3 has rank 9 for q7 mod 2, checking the primitive-degree-zero
boundary excluded above. Each prime witness has controls at sizes where
a+1 is a multiple and a nonmultiple of its order:

| Witness order | Source sizes a checked |
| --- | --- |
| 2 | 3, 4 |
| 3 | 4, 5, 8 |
| 5 | 4, 5, 9 |
| 7 | 6, 7 |

The order-5 and order-7 vectors were supplied by the discovery run.
Their original JSON receipts are preserved byte-for-byte and pinned;
the verifier checks the supplied vectors rather than rerunning that
discovery. This is a separation of construction and checking within
one session, not independent review. The all-size assertion uses the
written proof and credited external theorems, not extrapolation from
the ten source computations. No claim about compatible restrictions,
degenerations, or the matrix-multiplication exponent follows here.
