# An exact polynomial curve preserving the full conic first jet

October 23, 2026. Claim `AI-CONIC-FIXED-FIRST-CURVE-001` is written
and unreviewed. Owner-directed Codex work; no independent mathematical
review or formalization is claimed.

## Result

For every complex \(a,b,d\), with \(c=-d^3\), the polynomial constant
and first coefficients exported by
[PR107](https://github.com/1337isnot1337/matrix-mult-bounds/pull/107)
extend to exact polynomial maps

\[
B(t)=\sum_{k=0}^3t^kB_k,\qquad C(t)=\sum_{k=0}^3t^kC_k,
\qquad B_k,C_k\in\operatorname{Mat}_{14\times112}(\mathbb Q[a,b,d]).
\]

The complete canonical source contraction vanishes on the fixed
100-coordinate kernel \(K\), to every order. Leading minor determinants
\(1,1,-1\) give map ranks fourteen and first-source rank twelve over
\(\mathbb C[[t]]\), after every parameter specialization. These are
formal unit-minor statements, not assertions of the same ranks at every
finite \(t\).

Both full first coefficients agree with PR107, including its eight
boundary entries on \(B_1\) and its zero boundary velocity on \(C_1\).
The first source-kernel correction is zero, as in PR107. The normal
class remains \([1:d]\). The coefficient ring has no parameter
denominators, so the polynomial first-jet data also extend at \(d=0\)
and at the intersections with the linear components.

The second coefficients here are new. This result does not preserve
PR107's specified two-jet or assert that every first tangent with the
same normal class extends. The concurrent
[PR123](https://github.com/1337isnot1337/matrix-mult-bounds/pull/123)
already treats a stronger fixed-two-jet question at \(d=0\).
The construction remains local rank-twelve incidence with two
fourteen-row maps. It supplies no full matrix target or exponent gain.

## Credited source, cores and encoding

Use the integer source, fixed set \(A_0\), and complement \(K\) from
the [preceding polynomial construction](../2026-10-23-conic-polynomial-curve/proof.md).
Its 4096 terms are

\[
\bigl(\iota(i,s,6-p-q),\iota(p,j,6-r-s),\iota(r,q,6-i-j)\bigr),
\quad 0\le i,j,p,q,r,s\le3,\quad \iota(u,v,z)=28u+7v+z.
\]

Its explicit \(7\times4\) cores \(U_0(x),V_0(x)\), containing only
degrees zero and three in \(x\), encode exactly PR107's constant maps.
Write

\[
u=(a,ad^3,1,d^3)^T,\quad v=(-b,1,-bd^3,d^3)^T,\quad
f=(0,1,0,0)^T,\quad \Delta=(a+d^3)(b-d^3),
\]

and

\[
A=U_3v=(-1,b,0,0,-d^3,0,-bd^3)^T,\qquad
D=V_3u=(1,a,0,0,0,-d^3,-ad^3)^T.
\]

Here \(U_3=[x^3]U_0\), \(V_3=[x^3]V_0\). The credited direct
identities are

\[
U_0(x)v=(x^3-d^3)A,\quad V_0(x)u=(x^3-d^3)D,
\quad u^Tv=-\Delta,\quad f^Tv=1.                         \tag{1}
\]

The same paired-row encoding is used: for component \(2j+r\),
\(j,r\in\{0,1\}\), coefficient \(x^p\) of core row \(\ell\) goes
to row \(2\ell+\varepsilon\) at column
\(\iota(p,3j,4-3r+\varepsilon)\) on \(B\); on \(C\), coefficient
\(x^q\) goes to \(\iota(3r,q,4-3j+\varepsilon)\).
The literal source then reads coefficients of \(UV^T\). Having only
degrees \(0,3,6\) in that product is exactly sufficient for the
contraction to be supported on \(A_0\).

## Moving both roots

Put

\[
s=d-\frac23\Delta t,\qquad r=d+\frac13\Delta t,
\]

\[
\alpha=d^2t-\frac23d\Delta t^2+\frac4{27}\Delta^2t^3,
\qquad
\beta=d^2t+\frac13d\Delta t^2+\frac1{27}\Delta^2t^3.
\]

Define two boundary cores and the full cores by

\[
\begin{aligned}
U_*&=U_0+\alpha A(\Delta f-u)^T,&
V_*&=V_0+\beta Dv^T,\\
U&=U_*+t(x^2+sx+s^2)Au^T,&
V&=V_*-t(x^2+rx+r^2)Dv^T.
\end{aligned}                                                   \tag{2}
\]

Every expression is polynomial in \(a,b,d,t,x\) with rational constant
denominators only. In particular the displayed definitions of
\(\alpha,\beta\) require no division by \(\Delta\). They satisfy

\[
2\Delta\alpha=d^3-s^3,\qquad \Delta\beta=r^3-d^3,
\qquad (\Delta f-u)^Tv=2\Delta.
\]

Equations (1) therefore give

\[
U_*v=(x^3-s^3)A,\qquad V_*u=(x^3-r^3)D.                 \tag{3}
\]

Writing \(P_s=x^2+sx+s^2\) and \(P_r=x^2+rx+r^2\), expansion
using (3) proves

\[
\begin{aligned}
UV^T-U_*V_*^T
&=AD^TP_sP_r\{t(x-r)-t(x-s)+t^2\Delta\}\\
&=AD^TP_sP_r\{t(s-r)+t^2\Delta\}=0.                 \tag{4}
\end{aligned}
\]

The cores \(U_*,V_*\) have only \(x\)-degrees zero and three, so
their product has only degrees zero, three and six. The source encoding
and (4) establish the complete fixed-kernel identity. The argument is
valid when \(\Delta=0\) or \(d=0\), since it is a polynomial identity.

## All core coefficients and full first-jet matching

Expanding (2) gives a compact specification of every coefficient:

\[
\begin{aligned}
U_1&=(x^2+dx)Au^T+d^2\Delta Af^T,&
V_1&=-(x^2+dx)Dv^T,\\
U_2&=-\tfrac23\Delta(x+d)Au^T-\tfrac23d\Delta^2Af^T,&
V_2&=-\tfrac13\Delta(x+d)Dv^T,\\
U_3^{\mathrm{curve}}&=\tfrac8{27}\Delta^2Au^T+\tfrac4{27}\Delta^3Af^T,&
V_3^{\mathrm{curve}}&=-\tfrac2{27}\Delta^2Dv^T.
\end{aligned}                                                   \tag{5}
\]

The superscript in the last line distinguishes the \(t^3\) coefficients
from the earlier constant-core \(x^3\) coefficients. The generator
exports the full maps using (5), and separately checks (3)-(4).

The \(x^2\) and \(x\) parts of the first line give the credited normal
\(N_2+dN_1\). Its \(B\)-boundary part is exactly \(d^2\Delta Af^T\),
which encodes PR107's eight specified entries; the \(C\)-boundary part
is zero. Direct coefficient comparison in the acceptance program checks
all entries of \(B_0,C_0,B_1,C_1\), not only their normal projections.
The unchanged constant minors are checked again against the literal
source, proving the uniform leading ranks.

The second coefficients differ from PR107 by boundary terms. For
example, the present \((C_2)_{0,88}=-d\Delta/3\) is generically nonzero,
whereas PR107's entry there is zero. This records the precise remaining
fixed-two-jet question without treating a longer truncation as a proof.

## Acceptance and evidence

The accepted witness contains every full-map coefficient in
`results/conic-fixed-first-curve-2026-10-23/polynomial-curve.json`.
Its numbers of nonzero polynomial entries are
\((32,72,64,32)\) for \(B\) and \((32,64,64,32)\) for \(C\).

The acceptance program imports only the preceding arithmetic-only
polynomial parser, sparse arithmetic, determinant helper and literal
4096-term source contraction. It imports neither construction nor gauge
formulas. It recomputes every product coefficient
\(F_k=\sum_{i+j=k}T(-,B_i,C_j)\) for \(0\le k\le6\), checking
all \(100\cdot196\) kernel coordinates at each order. Cubic maps have
no higher product coefficients, so this is a complete polynomial
identity rather than finite-order evidence for an uncomputed extension.

Source pins, a coefficient-level first-jet check, complete-degree
controls, a forbidden-parameter-denominator control and a changed cubic
coefficient control accompany the witness. The preceding all-order
normal-class theorem is preserved. This continuation strengthens its
specific cubic representative by fixing the entire credited first jet;
it does not construct the full matrix target.
