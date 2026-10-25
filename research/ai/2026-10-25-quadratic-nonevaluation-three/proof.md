# A universal maximal three-plane outside the evaluation-kernel locus

October 25, 2026. Claim `AI-QUADRATIC-NONEVALUATION-THREE-001` is
**proof-written-unreviewed**. Exact certificates and separate same-session
checking are not independent mathematical review or formalization.

## Statement

Over every field K, including finite and nonperfect fields, the family

    V(t,x,y)=[[x,0,0],[y,t,x],[0,0,y]]

has dimension three, coefficient determinant D=txy, and geometric full
quadratic source rank at most fourteen. At every coefficient-invertible
point the source rank is exactly fourteen. This family is inclusion maximal
among linear families with that geometric rank bound, and is inequivalent
over every scalar extension to either previously published universal plane

    N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]],
    P(x,y,z)=[[x,x,0],[0,y,0],[0,z,z]],

under permitted binary changes and optional transpose. Thus characteristic
two has at least three inequivalent dimension-three attainers over every
field. Outside characteristic two these three examples are inclusion
maximal, while the global maximum dimension remains four.

The hypothesis is polynomial rank vanishing, not merely a finite-field
rational-point condition. All three parameters are independent coordinates.
No exhaustive classification, historical priority or compatible three-leg
tensor map is claimed; no matrix-multiplication exponent improvement follows.

## 1. Exact integer source certificates

Use the literal complete source with lexicographic pair orders

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    j,r=0,1,2, L,H=0,...,4,

and zero for out-of-range coefficients. The entries V11,V00,V22 recover
(t,x,y), proving dimension three over every field. Integer expansion gives
D=txy. The following nonzero polynomial vector is a LEFT source kernel:

    w=(0,0,0,-x,t,0,x,0,-y,0,-t,y,0,0,0)^t,
    R(V)^t*w=0.

All fifteen residuals vanish over Z[t,x,y]. The coordinate -x has unit
coefficient, so the vector remains nonzero over every field. Therefore
R is singular over K(t,x,y), and detR is identically zero in K[t,x,y].
This proves the bound at every specialization, even where w specializes
to zero. A polynomial right kernel is also recorded and checked:

    v=(-y^5,-2ty^4,-t^2y^3+xy^4,xy^4,txy^3,-x^2y^3,
       -x^2y^3,0,x^3y^2,x^3y^2,-tx^3y,-x^4y,
       t^2x^3-x^4y,2tx^4,x^5)^t.

The terms with coefficient two are retained before reduction in any field.
Delete zero-based source row3, pair(j,L)=(0,3), and column0,
pair(H,r)=(0,0), keeping all remaining rows and columns in their original
order. Exact expansion of this literal fourteen-by-fourteen minor gives

    det R(V)_(delete 3,0)=t^2*x^4*y^8.

The verifier and a separate pair-indexed regression reconstruct and expand
this determinant. Its coefficient is one, so it is nonzero whenever txy
is nonzero in any field. Together with the kernel identity this proves
exact source rank fourteen there. At t=x=y=1 both D and this minor equal
one, so no field extension is needed for an invertible point.

As a separate invariant cross-check, the pinned integer definitions give

    e=t, A2=xy, T4=0,
    P12=D^4+(eD+2T4)*(eD*T4+T4^2-A2*D^2)=0.

The pinned identity detR=D*P12 agrees with the direct certificate. The
integer definitions are used without division before reducing modulo a prime.

## 2. The intrinsic section and its conic type

Outside characteristic two the pinned integral-linear-form theorem gives
ell=T4/D and the intrinsic linear form m=e+2ell. Under the permitted
binary change M'=A(g) M A(h)^t, it transforms by
m'=det(g)det(h)m; transpose preserves it. In characteristic two, e itself
transforms by the same factor and is preserved by transpose. Consequently
U=ker(m) in odd characteristic and U=ker(e) in characteristic two is an
intrinsic section of any family under consideration. On V, N and P,
T4=0 and D is a nonzero polynomial, so the section is simply e=0.

Write K_R(U) and K_L(U) for the intersections of all right and left
coefficient kernels in U. Invertible left-right actions preserve their
dimensions, and transpose swaps them. For V the section t=0 has basis

    X=[[1,0,0],[0,0,1],[0,0,0]],
    Y=[[0,0,0],[1,0,0],[0,0,1]].

The equations Xu=Yu=0 give u0=u2=0, hence K_R=K*eta with eta=(0,1,0).
The equations X^t*z=Y^t*z=0 force z0=z1=z2=0, hence K_L=0.
These calculations have unit minors and hold in every characteristic.
The earlier pinned computations give (K_R,K_L) dimensions (1,0) for N,
with K_R=K*e0, and (1,1) for P. Thus dimensions distinguish V from P.

To distinguish V from N, retain the conic type of the unique nonzero
common-kernel line. For g=[[a,b],[c,d]] the ordinary binary action is

    A(g)=[[a^2,ac,c^2],[2ab,ad+bc,2cd],[b^2,bd,d^2]].

Set q(u)=u1^2-u0*u2. Direct integer expansion gives

    q(A(g)^t*u)=det(g)^2*q(u).

Also det A(g)=det(g)^3. Thus the dual action A(g)^(-t) preserves the
projective conic q=0 in every characteristic, without assuming that K
is algebraically closed. In fact A(g)^t sends (s^2,st,t^2) to the
corresponding evaluation vector at (as+bt,cs+dt). Right common kernels
transform by A(h)^(-t), left common kernels by A(g)^(-t). Transpose
swaps the two sides. Both the dimension pair and the conic membership
of the unique kernel line are therefore invariant, including after any
field extension. For V, q(eta)=1; for N, q(e0)=0. They cannot be equivalent.
In particular V lies outside the characteristic-two evaluation-kernel
locus classified in the previous package.

## 3. Inclusion maximality

If a larger geometric rank-at-most-fourteen linear family contained V,
choose one extra direction to obtain a four-space W. Its determinant is
not identically zero since its restriction to V is txy. In characteristic
two this contradicts the pinned sharp cap three.

In characteristic different from two the pinned four-dimensional attainer
classification forces 16D=m^3 on W. Its integral linear form satisfies
T4=D*ell. Restricting to V gives (txy)*ell|V=0 in K[t,x,y], hence ell|V=0
and m|V=t. The necessary identity then restricts to 16txy=t^3. This is
impossible: the coefficient of t^3 in t^3-16txy is one in every field.
No division by three or extraction of roots is used. Thus no larger W
exists over any ground field or scalar extension.

## Evidence and remaining question

The candidate was isolated while continuing beyond the evaluation-kernel
classification. Initial symbolic checking used structural matrix equality
before expansion; that check failed. Expanding each residual gives the
exact zero identities above. This was a checker setup error, not evidence
against the construction; the discovery notes and corrected script are
pinned separately. A separate same-session audit found no blocking gap.

The new contribution is V, its integer certificates, the conic-type
separation and the maximality consequence. Prior packages retain literal
source, invariant, binary-action, cap and classification attribution. The
exact checker verifies identities and witnesses, not geometric exhaustion.
A classification of all non-evaluation-kernel attainers and ground-field
forms remains open. A proposed lemma about singular two-pencils without
common kernels is not used here and remains a separate investigation.
