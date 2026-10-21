# A limit of supplying the full correction through a corner split

October 21, 2026. This note closes one specific way of using the
[triangular quotient construction](parity_balancing_triangular.md).
It does not exclude cancellation using shared variables, a cheaper
residual tensor, or a different source decomposition.

## Statement and assumptions

Suppose a,b>=2 and a linear map from M_m into the physical source
space W_(a,b) realizes a full m-dimensional quotient. Its invariant
kernel has dimension r=ab-m. Suppose the entire correction is
supplied by a separate source A(c,d) that restricts or degenerates
to M_r, where c,d>=1. Finally, suppose both sources are obtained
from a parent A(A,B) using the two-interval corner split with budget

\[
a+b+c+d\le A+B+1.
\tag{1}
\]

Then the resulting square M_m cannot cross the finite 9/4 gate

\[
216m^3>(3(A+B)-2)^4.
\tag{2}
\]

This holds even if the full quotient is larger than a+b-1 and even
if the residual supplier is better than the known monomial maps.
Only flattening dimensions are used to bound that supplier.

## Dimension inequalities

Write

\[
x=a+b-1,\qquad y=c+d-1,\qquad u=x+y\ge4.
\]

The quotient lift is injective: if J(H)=0, its quotient action H is
zero. The physical source space has dimension abx. Consequently

\[
m^2\le abx=x(m+r).
\tag{3}
\]

Every leg of M_r has flattening rank r^2. The residual supplier has
leg dimension cdy, so

\[
r^2\le cdy\le\frac{(y+1)^2y}{4},
\qquad r\le\frac{(y+1)\sqrt y}{2}.
\tag{4}
\]

This dimension constraint also holds for a degeneration. By (1),
A+B>=u+1. Therefore crossing (2) would require

\[
m>m_0:=\frac{(3u+1)^{4/3}}6.
\tag{5}
\]

We show that even m>=m0 contradicts (3).

## A uniform elementary bound

Set z=y/u in [0,1]. Using (4),

\[
\frac{x}{m_0}+\frac{xr}{m_0^2}
\le (1-z)\bigl(a(u)+b(u)z^{3/2}+c(u)\sqrt z\bigr),
\tag{6}
\]

where

\[
a(u)=\frac{6u}{(3u+1)^{4/3}},\quad
b(u)=\frac{18u^{5/2}}{(3u+1)^{8/3}},\quad
c(u)=\frac{18u^{3/2}}{(3u+1)^{8/3}}.
\]

For u>=4, a and c decrease. The maximum of b is attained at u=5.
Thus

\[
a(u)\le a(4)<\frac45,\qquad
b(u)\le b(5)<\frac58,\qquad
c(u)\le c(4)<\frac16.
\tag{7}
\]

The strict rational bounds are certified, respectively, by the
integer inequalities

\[
30^3<13^4,\qquad 3^{12}5^9<2^{40},\qquad 864^3<13^8.
\]

Elementary maximization on [0,1] also gives

\[
z^{3/2}(1-z)<\frac3{16},\qquad
\sqrt z(1-z)<\frac25.
\tag{8}
\]

For example, their squared maxima are 108/3125 and 4/27, which are
less than 9/256 and 4/25. Combining (6)--(8),

\[
\frac{x}{m_0}+\frac{xr}{m_0^2}
<\frac45+\frac58\frac3{16}+\frac16\frac25
=\frac{1889}{1920}<1.
\tag{9}
\]

If m>=m0, division of (3) by m^2 gives

\[
1\le\frac{x}{m}+\frac{xr}{m^2}
\le\frac{x}{m_0}+\frac{xr}{m_0^2}<1,
\]

a contradiction. This proves the stated limit.

The constants are deliberately loose; no optimization of this
obstruction is needed. In particular, it is not a bound on all
restrictions of the parent source. It applies to the quotient plus
full independent matrix correction routed through (1).

## Verification and review status

`parity_balancing_corner_correction.py` replays the five integer
comparisons used in (7) and (8), and the final rational sum. The
calculus and dimension argument are given above, rather than
inferred from a finite numerical search.

Review status: author-checked proof in this generating session; no
external independent review or formalization is claimed.
