# An exact polynomial curve preserving the prescribed conic two-jet

October 23, 2026. Claim `AI-CONIC-FIXED-TWO-CURVE-001` is written
and unreviewed. Owner-directed Codex work; no independent mathematical
review or formalization is claimed.

## Result and precise preserved data

For every complex \(a,b,d\) with \(d\ne0\), set \(c=-d^3\).
The complete two-jet exported by
[PR107](https://github.com/1337isnot1337/matrix-mult-bounds/pull/107)
extends to polynomial maps

\[
B(t)=\sum_{k=0}^{8}t^kB_k,\qquad
C(t)=\sum_{k=0}^{9}t^kC_k,
\quad B_k,C_k\in\operatorname{Mat}_{14\times112}
       (\mathbb Q[a,b,d,d^{-1}]).
\]

The complete source contraction is supported on the same twelve
first-source coordinates \(A_0\) at every order. The constant leading
minors remain \(1,1,-1\), so the maps have formal row ranks fourteen
and the first-source flattening has formal rank twelve, after every
parameter specialization in the stated chart.

All six matrices \(B_0,B_1,B_2,C_0,C_1,C_2\) equal the prescribed
PR107 matrices exactly. Its supplied source-kernel corrections are
\(Y_1=Y_2=0\); these are also preserved. The new curve has a fixed
kernel at every later order. Thus the statement preserves the complete
incidence two-jet, including its specified kernel parametrization,
rather than just its normal class or map coefficients.

The construction has parameter pole orders at most five on \(B\) and
six on \(C\). It excludes \(d=0\), where the prescribed mixed-chart
second coefficient itself has poles. The separate
[PR123](https://github.com/1337isnot1337/matrix-mult-bounds/pull/123)
retains credit for the earlier polynomial two-jet's exact \(d=0\) curve.
No third or later coefficient of PR107 is fixed here; its \(Y_3\)
has sixteen nonzero entries, while the present kernel stays fixed.

This is the local rank-twelve incidence of two fourteen-row maps. No
full matrix target, target degeneration, or exponent improvement follows
from this result alone.

## Source and compact form of the credited two-jet

Use the canonical integer source, \(A_0\), its complement \(K\),
the seven-row cores \(U_0(x),V_0(x)\), and the paired-row encoding
from the [preceding polynomial package](../2026-10-23-conic-polynomial-curve/proof.md).
The source consists of all 4096 coefficient-one terms

\[
\bigl(\iota(i,s,6-p-q),\iota(p,j,6-r-s),\iota(r,q,6-i-j)\bigr),
\quad i,j,p,q,r,s\in\{0,1,2,3\},\quad \iota(u,v,z)=28u+7v+z.
\]

The constant cores have only \(x\)-degrees zero and three. Write

\[
u=(a,ad^3,1,d^3)^T,\quad v=(-b,1,-bd^3,d^3)^T,
\quad f=(0,1,0,0)^T,\quad e=(0,0,1,0)^T,
\]

\[
\Delta=(a+d^3)(b-d^3),\quad U_3=[x^3]U_0,\quad V_3=[x^3]V_0,
\quad A=U_3v,\quad D=V_3u.
\]

The existing identities are

\[
U_0(x)v=(x^3-d^3)A,\qquad V_0(x)u=(x^3-d^3)D,
\qquad u^Tv=-\Delta,\quad f^Tv=e^Tu=1.                 \tag{1}
\]

Define the seven-component vector

\[
H=\left(
-\frac{\Delta^2(b-2d^3)}{3d^2},\
-\frac{d\Delta^2(b+d^3)}3,\
\frac{\Delta^2(b-d^3)}{3d^2},\
0,0,\frac{bd\Delta^2}3,0\right)^T.
\]

The full first and second core coefficients of PR107 are

\[
\begin{aligned}
U_1&=(x^2+dx)Au^T+d^2\Delta Af^T,&
V_1&=-(x^2+dx)Dv^T,\\
U_2&=-\frac23\Delta xAu^T+Hf^T,&
V_2&=-\frac13\Delta xDv^T.
\end{aligned}                                                    \tag{2}
\]

These formulas merely rewrite the pinned predecessor coefficients.
The acceptance program compares every full-map entry through order
two; it does not assume this identification from the short formulas.

## A second-order change of gauge vector

Put

\[
w=\left(\frac{\Delta^2(b-d^3)}{3d^2},\ 0,\
         \frac{bd\Delta^2}3,\
         \frac{\Delta^2(b-d^3)}{3d^2}\right)^T,
\qquad v(t)=v+t^2w,
\]

\[
\kappa=w^Tu=\frac{\Delta^2(\Delta+bd^3)}{3d^2},\qquad
s(t)=d-\frac23\Delta t+\frac{\Delta^2}{9d}t^2,
\]

\[
r(t)=s(t)-t\,v(t)^Tu
     =d+\frac13\Delta t+\frac{\Delta^2}{9d}t^2-\kappa t^3.
                                                                  \tag{3}
\]

Direct multiplication gives the additional identity

\[
U_0(d)w=-H-\frac13d\Delta^2A.                                  \tag{4}
\]

It also gives \(f^Tv(t)=1\), since the second component of \(w\)
is zero. All expressions lie in the Laurent parameter ring
\(R=\mathbb Q[a,b,d,d^{-1}]\).

## Boundary interpolation followed by an exact projection

Start with boundary cores

\[
\begin{aligned}
U_{\mathrm p}(t,x)
 &=U_0(x)+t d^2A(\Delta f-u)^T
       +t^2\left(Hf^T+\frac43d\Delta Au^T\right),\\
V_{\mathrm p}(t,x)
 &=V_0(x)+t d^2Dv^T+t^2\frac23d\Delta Dv^T.
\end{aligned}                                                    \tag{5}
\]

Their exact root residuals are

\[
R_U(t)=U_{\mathrm p}(t,s(t))v(t),\qquad
R_V(t)=V_{\mathrm p}(t,r(t))u.
\]

Both residuals are divisible by \(t^3\). For \(R_V\), equation (1)
gives the explicit scalar expression

\[
R_V=\left(r^3-d^3-d^2\Delta t-\frac23d\Delta^2t^2\right)D,
\]

and (3) gives the required zero coefficients through degree two.
For \(R_U\), set \(E=U_3w\). Using (1) and (4), expansion gives

\[
\begin{aligned}
R_U={}&\left(s^3-d^3+2d^2\Delta t-\frac53d\Delta^2t^2
                 -d^2\kappa t^3+\frac43d\Delta\kappa t^4\right)A\\
&\quad+t^2(s^3-d^3)E.
\end{aligned}                                                    \tag{6}
\]

Here
\(s^3-d^3=-2d^2\Delta t+\frac53d\Delta^2t^2+O(t^3)\),
so the first three coefficients again vanish. This uses a finite
expansion to prove preservation of the input jet, not to infer the
later source equations.

Now project the boundary cores exactly:

\[
\widehat U=U_{\mathrm p}-R_Uf^T,\qquad
\widehat V=V_{\mathrm p}-R_Ve^T.                                \tag{7}
\]

Because \(f^Tv(t)=e^Tu=1\), these satisfy
\(\widehat U(t,s(t))v(t)=0\) and
\(\widehat V(t,r(t))u=0\) identically. The corrections in (7) begin
at \(t^3\); hence they leave every coefficient through order two of
the interpolating boundary cores unchanged.

The cores in (7) still have only degrees zero and three in \(x\), and
their \(x^3\) coefficients remain \(U_3,V_3\). Consequently

\[
\widehat U(t,x)v(t)=(x^3-s^3)U_3v(t),\qquad
\widehat V(t,x)u=(x^3-r^3)D.                                   \tag{8}
\]

## Complete polynomial curve and its exact identity

Set \(A(t)=U_3v(t)\), \(P_s=x^2+sx+s^2\) and
\(P_r=x^2+rx+r^2\), and define

\[
U=\widehat U+tP_sA(t)u^T,\qquad
V=\widehat V-tP_rDv(t)^T.                                      \tag{9}
\]

Let \(\Delta(t)=-v(t)^Tu\). By (3), \(r=s+t\Delta(t)\).
Expansion using (8) proves the exact polynomial identity

\[
\begin{aligned}
UV^T-\widehat U\widehat V^T
 &=A(t)D^TP_sP_r
     \{t(x-r)-t(x-s)+t^2\Delta(t)\}\\
 &=0.
\end{aligned}                                                    \tag{10}
\]

The product on the right has only \(x\)-degrees zero, three and six.
The credited paired-row source encoding therefore gives

\[
T(-,B(t),C(t))[K,:]=0
\]

identically in \(R[t]\). This proves every order simultaneously.
There is no moving kernel or uncomputed formal recurrence.

The root degrees are two and three, while \(v(t)\) has degree two.
Equations (5)-(9) give degrees at most eight and nine in \(t\) for
\(U,V\). The exported maps attain these degrees over \(R\).
The same formulas give parameter pole bounds five and six; the verifier
independently enforces those bounds when reading every coefficient.

To identify the first two coefficients, use that (7) begins at order
three and \(v(t)=v+O(t^2)\). The root velocities are
\(s'(0)=-2\Delta/3\) and \(r'(0)=\Delta/3\). Expanding (9)
through degree two gives exactly (2). The factors
\(4d\Delta/3\) and \(2d\Delta/3\) in (5) cancel the constant
terms from these root velocities. Literal full-map comparison confirms
this identification with PR107, including \(Y_1=Y_2=0\).

## Acceptance, performance and remaining scope

`construct.py` exports every coefficient of the full maps. It computes
the finite scalar root powers and the projection residuals coefficient
by coefficient, avoiding redundant expansion of a large symbolic
matrix product. Neither the proof nor acceptance depends on a solver.

`verify.py` is a separate literal-source implementation. Its non-executing
AST parser permits rational Laurent arithmetic only, clears \(d^5\)
from \(B\) and \(d^6\) from \(C\), and rejects poles in any other
parameter or larger powers of \(d\). Thus its sparse polynomial
contractions check \(d^{11}T(-,B,C)\); multiplication by \(d^{11}\)
is injective on the stated chart, so the checked identities are exactly
the required identities.

All 4096 source terms are rebuilt. At each of the eighteen complete
product orders, every source term whose first coordinate lies in
\(K\) is retained, with its full multiplicity. Positive-order rows in
\(A_0\) are unrestricted, so avoiding their expansion drops no required
equation. The constant contraction is also rebuilt without this filter
to verify the unit rank minor. In total the kernel checks cover all
\(18\cdot100\cdot196=352800\) coefficient positions.

The focused tests run the expensive complete acceptance once, then use
preflight rejection and selected exact coefficient checks for altered
inputs. A changed last \(C_9\) boundary coefficient leaves order nine
unchanged but produces a nonzero order-ten kernel coefficient. Other
controls change the prescribed second coefficient, kernel data, chart,
degrees and permitted coefficient ring. These controls do not replace
any order of the positive complete-source replay.

The leading unit minors certify the formal ranks on the entire stated
parameter chart; they do not assert full ranks at every finite value of
\(t\). The degree and pole bounds are supplied bounds, with no claim of
minimality. Prescribed third jets, other first-jet representatives, the
complete matrix target and an exponent improvement remain outside this
result. Computational checks and within-session algebra audits do not
change the written proof's unreviewed status.
