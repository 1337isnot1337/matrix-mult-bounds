# A score ceiling for full-matrix quotient corrections

October 21, 2026. Written argument and exact integer certificate. The
reduction was checked by a second agent in this generating session.
No external independent review, formalization, or smaller matrix
multiplication exponent is claimed.

The triangular construction raises a natural question: could a larger
physical quotient, followed by a full matrix correction, improve the
finite source score? The following bound excludes that particular direct
comparison, even if the larger quotient exists.

## Statement and scope

Let a,b>=2, put x=a+b-1 and q=ab, and suppose a surjective quotient of the
q-dimensional physical space has dimension m. Assume a linear lift
J:Mat_m -> W_(a,b) satisfies pi J(A)=A pi. Its residual matrix size is
r=q-m. The lift is injective, so

\[
m^2\le qx.                                                     \tag{1}
\]

The resulting exact correction would give

\[
A(a,b)\oplus M_r\longrightarrow M_m.
\]

Set p=9/4. For every integer m satisfying (1),

\[
\boxed{(6m)^p-(6r)^p<\frac{93}{100}(3x+1)^3.}                 \tag{2}
\]

Thus no single lower bound lambda(A(a,b))>=m^S-r^S from such a quotient
passes this package's usual finite 9/4 source comparison. This statement
allows quotients larger than the known dimension x. It is an arithmetic
obstruction under the necessary dimension condition, not a proof that
those quotients do not exist.

For unequal a,b, apply the construction to both cyclic orientations.
The existing six-orientation comparison then gives P(a,b)^S>=m^S-r^S
when the right side is positive, while
6^S P(a,b)^S<=[3(a+b)-2]^3=(3x+1)^3. Equation (2) prevents a
contradiction at S=p. When m>r, the score is increasing in S>=0, so
the same single comparison cannot exclude a smaller exponent either.

This does not exclude joint use of several tensor identities, a cheaper
residual tensor, cancellation on shared variables, or another source
inequality. It does not apply to an arbitrary restriction with an added
matrix source unless the injective quotient-lift condition (1) holds.

## A one-variable inequality

For 0<=u<=1 define

\[
c(u)=(1+u)^p(1-u^p).
\]

Its derivative has the sign of
1-u^(5/4)(1+2u). The latter expression strictly decreases from positive
to negative. Hence the unique maximum occurs at u_* in (0,1) satisfying

\[
u_*^5(1+2u_*)^4=1.
\]

At this point,

\[
c(u_*)^4=u_*^5(1+u_*)^{13}.                                   \tag{3}
\]

The rational number v=553/1000 satisfies both exact inequalities

\[
v^5(1+2v)^4>1,\qquad v^5(1+v)^{13}<16.                       \tag{4}
\]

All factors are positive and increasing in v. Therefore u_*<v and
(3)-(4) prove c(u)<2 throughout [0,1]. The certificate checks (4)
by clearing denominators and comparing integers; decimal estimates
play no role.

## Reduction to four small source formats

For fixed q the expression m^p-(q-m)^p strictly increases with m on
[0,q]. Also q>x, since (a-1)(b-1)>0. If q>=4x, condition (1) gives
m<=q/2, and the score is nonpositive.

Otherwise 1<sqrt(q/x)<2. Substitute the relaxed upper value
m=sqrt(qx), and put u=sqrt(q/x)-1. Then

\[
(6m)^p-(6(q-m))^p=(6x)^p c(u)<2(6x)^p.                       \tag{5}
\]

The ratio 2(6x)^p/(3x+1)^3 decreases for x>1: its logarithmic
derivative is p(1-x)/[x(3x+1)]. For x>=6, the exact inequality

\[
200^4\,36^9 < [93\,19^3]^4                                  \tag{6}
\]

therefore gives

\[
\frac{2(6x)^p}{(3x+1)^3}\le\frac{2\,36^p}{19^3}<\frac{93}{100}.
\]

Sorting a<=b, the remaining x<=5 formats are (2,2), (2,3), (2,4),
and (3,3). The score increases with m, so it suffices to use
m=floor(sqrt(abx)) in each. Their respective (m,r) values are
(3,1), (4,2), (6,2), and (6,3).

For Q=10^6, the certificate supplies an integer upper bound U for
Q(6m)^p and a lower bound L for Q(6r)^p. It verifies

\[
U^4\ge Q^4(6m)^9,\qquad L^4\le Q^4(6r)^9,
\qquad100(U-L)<93Q(3x+1)^3.
\]

This proves (2) for the remaining formats. These four cases and the
analytic reduction cover every a,b>=2; no unbounded search or floating
optimization is assumed.

## Reproduction and attribution

`quotient_score_barrier.py` produces
`results/anisotropic-constructions-2026-10-20/quotient-score-barrier.json`
using only the Python standard library. The regression test checks the
saved inequalities directly with integer powers, independently of the
integer-root algorithm used to generate the bounds.

The quotient/correction setup is from the companion
`parity_balancing_triangular.md`. The source score is the existing
two-orientation finite-amplitude comparison in this package's README,
derived from the externally credited character framework. This note
claims neither of those as a new exponent theorem.
