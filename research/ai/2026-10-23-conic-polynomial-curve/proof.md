# A polynomial all-order curve on the cubic conic component

October 23, 2026. Owner-directed Codex work. Claim
`AI-CONIC-POLYNOMIAL-CURVE-001` is written and unreviewed.

## Statement and scope

For every complex \(a,b,d\), put \(c=-d^3\). There are explicit matrices

\[
B(t)=B_0+tB_1,\qquad
C(t)=C_0+tC_1+t^2C_2+t^3C_3
\]

of size \(14\times112\), with entries in \(\mathbb Q[a,b,d,t]\), such that:

1. Their constant matrices are exactly those of the credited cubic-conic
   family in [PR107](https://github.com/1337isnot1337/matrix-mult-bounds/pull/107).
2. The contracted canonical tensor is supported on the same twelve
   first-source coordinates \(A_0\) for every \(t\).
3. The maps have row rank fourteen over \(\mathbb C[[t]]\), and the
   first-source flattening has rank twelve, after every specialization
   of \(a,b,d\) to complex numbers.
4. Their first nonboundary coefficients equal those of PR107 exactly.
   Their first normal class is \([1:d]\), including at \(d=0\).

Here rank over the formal power-series ring means that an appropriate
minor is a unit and all larger minors vanish when applicable. The same
ranks hold over \(\mathbb C((t))\) and on a Zariski-open neighborhood of
\(t=0\) for each fixed parameter triple. We do not assert these ranks at
every finite value of \(t\).

This is a complete polynomial curve, so it supplies a lift to every
formal order. Its first boundary velocity differs from PR107; it does
not preserve that full first jet or its second jet. The fourth- and
tenth-order witnesses in the separate higher-jet package address
stronger fixed-coefficient conditions. The concurrent
[PR123](https://github.com/1337isnot1337/matrix-mult-bounds/pull/123)
separately supplies an exact \(d=0\) curve preserving its credited two-jet.
The result here includes that parameter fiber by its own polynomial
identity; it makes no priority claim for solving that fiber.

The curve establishes the local rank-twelve incidence with two
fourteen-row maps. It does not construct the full matrix target
\(M(10,10,11)\), a tensor degeneration to that target, or an improved
matrix multiplication exponent.

## Canonical source and paired-row encoding

Write \(\iota(u,v,z)=28u+7v+z\). The canonical integer source has the
following 4096 coefficient-one terms:

\[
\bigl(\iota(i,s,6-p-q),\ \iota(p,j,6-r-s),\
      \iota(r,q,6-i-j)\bigr),
\qquad i,j,p,q,r,s\in\{0,1,2,3\}.
\]

This source and its constant conic maps are credited local inputs from
[PR101](https://github.com/1337isnot1337/matrix-mult-bounds/pull/101)
and PR107, retained with exact byte pins in `sources.json`.
Let

\[
A_0=\{\iota(i,s,z):i,s\in\{1,2\},\ z\in\{0,3,6\}\},
\qquad K=\{0,\ldots,111\}\setminus A_0.
\]

Take two polynomial cores \(U(x),V(x)\) of size \(7\times4\), each
of degree at most three in \(x\). Label their four components by
\((j,r)\in\{0,1\}^2\), in the order \(2j+r\). Encode them into
fourteen-row source maps by repeating each core row with parity
\(\varepsilon\in\{0,1\}\):

\[
\begin{aligned}
B_{2\ell+\varepsilon,\,\iota(p,3j,4-3r+\varepsilon)}
   &=[x^p]U_{\ell,2j+r}(x),\\
C_{2m+\varepsilon,\,\iota(3r,q,4-3j+\varepsilon)}
   &=[x^q]V_{m,2j+r}(x).
\end{aligned}                                                    \tag{1}
\]

All other entries are zero. Matching a source term to both supports in
(1) forces the component labels \((j,r)\) to coincide. Indeed the
second and third source long indices imply

\[
s=2-\varepsilon_B+3(r_B-r_C),\qquad
i=2-\varepsilon_C+3(j_C-j_B).
\]

Both must lie in \(\{0,1,2,3\}\); the values of their parity terms force
\(r_B=r_C\) and \(j_B=j_C\). Thus
\(s=2-\varepsilon_B\) and \(i=2-\varepsilon_C\).
The entry at first coordinate \(\iota(i,s,z)\) is consequently

\[
[x^{6-z}]\sum_{j,r}U_{\ell,2j+r}(x)V_{m,2j+r}(x).
                                                                  \tag{2}
\]

Therefore every coefficient of the complete tensor contraction outside
\(A_0\) vanishes if each entry of \(UV^T\) contains only the powers
\(x^0,x^3,x^6\). This reduction is exact over the polynomial coefficient
ring; it uses neither a sampled parameter point nor a tangent truncation.

## Explicit constant cores

The credited constant maps have the following cores:

\[
U_0(x)=\begin{pmatrix}
0&-x^3&0&1\\
-x^3&0&1&0\\
0&d^3&0&-1\\
-1&-b-d^3&0&1\\
0&bd^3+d^6&1&-x^3\\
0&-bd^3&-1&0\\
0&bd^6&x^3&0
\end{pmatrix},\qquad
V_0(x)=\begin{pmatrix}
0&0&x^3&-1\\
x^3&-1&0&0\\
1&0&-a+d^3&-1\\
0&-1&ad^3&0\\
0&0&-d^3&1\\
0&1&-ad^3+d^6&-x^3\\
0&-x^3&ad^6&0
\end{pmatrix}.                                                   \tag{3}
\]

Let \(U_3=[x^3]U_0\), \(V_3=[x^3]V_0\), and put

\[
u=\begin{pmatrix}a\\ad^3\\1\\d^3\end{pmatrix},\qquad
v=\begin{pmatrix}-b\\1\\-bd^3\\d^3\end{pmatrix},\qquad
e=\begin{pmatrix}0\\0\\1\\0\end{pmatrix},\qquad
\Delta=(a+d^3)(b-d^3).
\]

Direct multiplication in (3) gives

\[
U_0(d)v=0,\qquad V_0(d)u=0,\qquad v^Tu=-\Delta,\qquad u^Te=1.
                                                                  \tag{4}
\]

For reference, the two seven-component vectors used below are

\[
A:=U_3v=(-1,b,0,0,-d^3,0,-bd^3)^T,\qquad
D:=V_3u=(1,a,0,0,0,-d^3,-ad^3)^T.
\]

## The polynomial construction

Define

\[
r=d+\Delta t,\qquad
P=x^2+dx+d^2,\qquad Q=x^2+rx+r^2,
\]

and set

\[
\begin{aligned}
V_*(t,x)&=V_0(x)-(r^3-d^3)De^T,\\
U(t,x)&=U_0(x)+tP Au^T,\\
V(t,x)&=V_*(t,x)-tQ Dv^T. 
\end{aligned}                                                    \tag{5}
\]

These formulas belong to \(\mathbb Z[a,b,d,t,x]\). Their degrees in
\(x\) are at most three, and their degrees in \(t\) are at most one
and three for \(U,V\), respectively. In particular, no inversion of
\(d\), \(\Delta\), or another parameter is used.

We claim the exact identity

\[
U(t,x)V(t,x)^T=U_0(x)V_*(t,x)^T.                                  \tag{6}
\]

Both constant cores have only degrees zero and three in \(x\). By (4),

\[
U_0(x)v=(x^3-d^3)A=(x-d)PA,
\qquad
V_*(t,x)u=(x^3-r^3)D=(x-r)QD.
\]

Expand the left side of (6) using (5). Its difference from the right
side is

\[
\begin{aligned}
&tP A(V_*u)^T-tQ(U_0v)D^T-t^2PQ A(u^Tv)D^T\\
&\qquad=AD^T PQ\{t(x-r)-t(x-d)+t^2\Delta\}\\
&\qquad=AD^T PQ\{t(d-r)+t^2\Delta\}=0.
\end{aligned}
\]

This proves (6) by a polynomial identity, including when \(d=0\) or
\(\Delta=0\). The right side of (6) has only degrees zero, three and
six in \(x\). Equations (1) and (2) now prove

\[
T(-,B(t),C(t))[K,:]=0                                            \tag{7}
\]

identically in \(a,b,d,t\). The source kernel remains fixed; no moving
kernel correction is needed at any order.

For discovery, (5) can also be understood as cancellation of a rank-one
rational gauge. With \(H=I+tvu^T/(x-d)\), one has
\(U=U_0H\) and \(V=V_*H^{-T}\), where
\(H^{-T}=I-tuv^T/(x-r)\). The displayed polynomial proof is the
acceptance argument and requires no rational-chart hypothesis.

## Leading ranks and the normal direction

At \(t=0\), (5) gives exactly (3), and encoding (1) gives PR107's
literal \(B_0,C_0\). For the two map minors, list the sixteen columns

\[
\{\iota(p,j,z):p,j\in\{0,3\},\ z\in\{1,2,4,5\}\}
\]

in the stated product order, delete the first two, and use all fourteen
rows. For \(C_0\), interchange the first two arguments of \(\iota\)
in this product order. Both resulting determinants are identically one.
For the twelve \(A_0\) rows of the contracted constant source, the
output columns

\[
0,1,2,3,14,15,16,17,30,31,44,45
\]

give determinant minus one. The exact verifier checks all three
determinants. After every parameter specialization their continuations
are units in \(\mathbb C[[t]]\). Together with (7), these facts prove
the stated ranks without a generic-parameter qualification.

The coefficients of \(x^2\) and \(x\) in the first core derivatives
from (5) are

\[
[x^2]\dot U=Au^T,\quad [x]\dot U=dAu^T,
\qquad
[x^2]\dot V=-Dv^T,\quad [x]\dot V=-dDv^T.                       \tag{8}
\]

The correction \(V_*-V_0\) has only degree zero in \(x\). Thus it
changes only boundary columns. Encoding (8) gives exactly the credited
normal pair \(N_2+dN_1\) of PR101/PR107. The verifier compares every
nonboundary coefficient with that source: 64 entries on each leg.
In zero-based full-map coordinates,
\((C_1)_{0,102}=-1\) and \((C_1)_{0,95}=-d\), which explicitly
certify the ratio \([1:d]\) and its nonvanishing for all parameters.
The two actual first coefficients each differ from PR107 in 32 boundary
entries; the normal quotient agrees, while the full first jet changes.

## Exact evidence and limits

`construct.py` exports every coefficient of both full \(14\times112\)
maps to `results/conic-polynomial-curve-2026-10-23/polynomial-curve.json`.
There are 32 and 96 nonzero entries in \(B_0,B_1\), and 32, 96, 64,
32 entries in \(C_0,C_1,C_2,C_3\). The exported expressions are
polynomials in \(a,b,d\).

`verify.py` imports neither the construction nor a predecessor solver.
An arithmetic-only parser admits \(\mathbb Q[a,b,d]\), rejecting
parameter denominators, fractional powers and executable expressions.
The verifier independently rebuilds all 4096 source terms and computes

\[
F_k=\sum_{i+j=k}T(-,B_i,C_j),\qquad 0\le k\le4.
\]

It checks all \(100\cdot196\) kernel coordinates at every order,
the three unit minors, and literal equality of the constant and first
normal coefficients. Because the maps are complete polynomials of
degrees one and three, these are all coefficients of the product.
No uncomputed higher-order equations remain. A negative control changes
one entry of \(C_3\); it passes the kernel equations through order three
and is rejected at order four, which tests this distinction directly.

The report is an exact computational check of the supplied identities,
supporting the written proof above. It is not an independent mathematical
review or a proof-assistant formalization. The full matrix target and
the implication to a smaller exponent remain unconstructed.
