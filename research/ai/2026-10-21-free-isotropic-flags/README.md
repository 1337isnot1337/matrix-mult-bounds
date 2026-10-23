# Exact free isotropic flag at C(7,15)

Date: 2026-10-21.

This package proves a finite characteristic-zero degeneration
C(7,15) -> matched T_5, with an independent invertible shared basis in each
of its five convolution sectors. It supplies no unbounded family and no
smaller matrix-multiplication exponent.

The text and verifier were recovered after an execution-service failure.
The original seed, Jacobian minor, opens, and all source coefficients had
been checked by coordinated agents in the same generating session.
The recovered seed, all 4,500 Jacobian entries, pivot rank, and the opens
below have also been replayed in a fresh pure-JavaScript implementation.
This is not external independent certification. The binary seed is not
being presented as a characteristic-zero coefficient list.

## 1. Integral equations and exact seed

Let A=K[t]/f, where f is monic of degree 13, and let tau take the coefficient
of t^12 in the remainder modulo f. Set U=<u_0,...,u_4> inside P_6 and
L=<l_0,l_1,l_2>, with l_0=1. The unknowns are U, mu, l_1, l_2, g, and the
13 lower coefficients of f. Require

    tau(mu u_i l_j l_k)=0       (0<=i<5, 0<=j<=k<=2),       30 equations;
    tau(mu u_i g l_j)=0         (0<=i<5, 0<=j<=2),           15 equations.

All coefficients of the equations are integers: reduction by a monic
polynomial uses no division.

Encode a binary polynomial by the integer whose bit j is its t^j
coefficient. An exact F_2 point is

    f  = 10717;
    U  = [109,114,60,83,18];
    mu = 5780;
    L  = [1,2050,7656];
    g  = 2550;
    G  = mu*g mod f = 1921.

The 100 variables are ordered as U (five blocks of seven coefficients),
mu (13), l_1 (13), l_2 (13), g (13), and f (13, with its leading coefficient
fixed to one). The 45 Jacobian rows have rank 45 over F_2. A square
nonsingular minor uses columns

    0,2,7,9,14,16,21,23,28,30,
    35,36,37,38,39,40,41,42,43,44,45,46,
    49,50,51,52,53,54,55,56,57,58,
    62,63,64,65,66,67,68,69,70,71,75,76,87.

Fixing f drops the rank to 44, so allowing the modulus to move matters.

The verifier obtains each Jacobian entry from
(F(x+2 e_j)-F(x))/2 modulo 2, evaluating the integral equations modulo 4.
This includes the derivative of the modulus and avoids relying on a
symbolic differentiation routine. It also replays an exact lift through
2^12. The finite replay is a control; the odd square minor is what proves
arbitrarily many lift steps by Hensel's lemma.

## 2. Open conditions

At the seed:

- U has dimension 5 and U+tU=P_7.
- mu and g are units in A.
- <L,g> has dimension 4.
- UL has dimension 9.
- The symmetric central tensor below has shared rank 5.
- Its one-dimensional annihilating conic is
  x^2+xy+y^2+z^2. The integer conic discriminant is 3.
- The outer 4-by-5 pencil has an invertible 20-by-20 degree-three
  Sylvester matrix.
- Its degree-four polynomial kernel has five independent coefficient
  vectors, whose four nonzero images under the first pencil matrix are
  independent. This is a direct certificate of its normalizing bases.
- The functional nu=delta_2+delta_5 makes
  H_(i,k)=nu(u_i t^k), 0<=i,k<5, invertible.

These are polynomial nonvanishing conditions after adjoining inverses
where necessary. They remain nonzero in the exact 2-adic lift.

The first 30 equations alone would only give dim UL<=10. The additional
15 equations are essential: mu<L,g> lies in (UL)^perp and has dimension
four, so dim UL<=9. The rank-nine minor then gives equality in the lift.

An exact Q_2 point satisfying a finite rational equation system and these
open conditions implies a point over algebraic closure of Q, hence over C.
For example, encode each open condition by an inverse variable and use
faithful field extension and the Nullstellensatz. Thus the result is an
exact characteristic-zero existence theorem.

## 3. Source maps

Write K=(UL)^perp, of dimension four, and K0=U^perp, of dimension eight,
using the Frobenius pairing tau(ab). Then

    K = mu L + <G>,      G=mu g.

Use the shared map given by U in P_6. In the 15-dimensional input space
P_14 choose the following rows, grouped by target degree p:

    p=0: G;
    p=1: f, tf;
    p=2: mu*l_0, mu*l_1, mu*l_2;
    p=3: four lifts of a basis of K0/K;
    p=4: five rows dual to the independent functionals tau(u_i *).

The polynomial representatives of elements of A have degree at most 12.
The f,tf rows are independent of these representatives, so all 15 input
rows are independent.

Define output functionals on P_20, grouped by target degree q:

    q=0: tau;
    q=1: tau(l_1 *), tau(l_2 *);
    q=2: tau(g^(-1) l_j *), j=0,1,2;
    q=3: z_c(f v)=nu(t^c v), and z_c(U G)=0, c=0,1,2,3;
    q=4: five functionals dual to U G.

The q=3 prescription is consistent: f P_7 intersects U G trivially,
because G is a unit modulo f and U has degree below 13. Extend all
partially specified functionals linearly to P_20.

For p+q<4 every coefficient is zero. For p+q=4 the five blocks are:

- C(1,5) and C(5,1), from the two dual choices;
- C(2,4), from the invertible H defined by nu;
- C(4,2), from the single Kronecker outer pencil;
- C(3,3), from the symmetric central tensor
  tau(mu g^(-1) u_i l_j l_k).

The central tensor spans a hyperplane in Sym^2(K^3). Its annihilating
conic is nonsingular, so over C an invertible congruence takes that
hyperplane to the Hankel plane. This follows from diagonalizing a
nondegenerate ternary quadratic form; the Hankel relation
v_0 v_2-v_1^2 is itself nondegenerate in characteristic zero.

For the outer pencil A+sB, the verifier also solves its degree-four
polynomial kernel, a rank-24 system on 25 coefficients. Write its vector
as q_0+s q_1+...+s^4 q_4. The five q_i form a basis, and the four
A q_1,...,A q_4 form a basis of the other space. The identities
A q_0=0, A q_i=-B q_(i-1), B q_4=0 therefore put A and B into the two
consecutive coordinate-deletion maps. This is exactly C(4,2), after a
sign and order choice on the two-dimensional leg. The kernel and bases
vary rationally on the stated nonzero-minor chart, so the same argument
applies to the characteristic-zero lift. Each matched sector allows
its own invertible identification of the shared five-space.

Scale the input rows by epsilon^p and the output rows by epsilon^(q-4).
All negative coefficients vanish and the constant coefficient is precisely
the five claimed sectors. Positive powers disappear in the limit.
Conciseness of the constant target forces the output map to have full
rank 15 as well.

## 4. Reproduction and scope

Run:

    python research/ai/2026-10-21-free-isotropic-flags/verify_chart.py
    python research/ai/2026-10-21-free-isotropic-flags/verify_source.py
    python -m unittest discover -s tests -p test_endpoint_flag_certificates.py -v

The verifier checks the integral seed, all Jacobian entries, the specified
minor, an exact finite Hensel replay, and the open conditions. A separate
chart-to-source reconstruction checks the full 1,125 coefficient positions;
it was performed by the construction and audit agents. The root agent
independently repeated every coefficient and open-condition check.
The literal binary maps, separate full-source report, and independent
Jacobian report are stored alongside the chart report. The final binary
maps swap the two raw degree-one output rows and apply the central
basis change with binary rows [1,6,3]. These harmless basis changes are
recorded explicitly; the integral 45-equation chart keeps its original L.
The maintained `verify_source.py` multiplies the literal polynomials in the
original C(7,15) source, without reduction by f. The focused tests reject
both a nonzero negative coefficient and a corrupted constant coefficient,
as well as a repeated column in the alleged nonsingular Jacobian minor.

This result is outside the scalar shifted-block ansatz: the later input
and output rows are free quotient-space vectors. It is also outside the
a=m+1 exact-cost outer bound, because its source shared size is a=m+2.
It remains a finite construction. Its source aspect is 7/5, so it is not
an asymptotic exponent improvement on its own.

