# Four-dimensional invertible quadratic families outside characteristic two

October25, 2026. Claim `AI-ODD-QUADRATIC-ATTAINERS-001` is
**proof-written-unreviewed**. A separate same-session algebra audit and exact
polynomial controls corroborate the argument. Neither supplies independent
mathematical review or formalization. No historical priority or exponent
improvement is claimed.

## Theorem and permitted equivalences

Let K be any field with characteristic different from two, including zero.
For M in Mat3(K), use the complete source

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    0<=j,r<=2, 0<=L,H<=4,

with out-of-range entries zero and both pair orders lexicographic. Suppose
a four-dimensional K-linear coefficient space W has detR identically zero
and coefficient determinant D=detM not identically zero. Then, by permitted
binary changes over K and possibly transposition, W is equivalent to

    W0={[[8t,b,c],[0,4t,f],[0,0,t]] : t,b,c,f in K}.

Thus all dimension-four attainers on the coefficient-invertible stratum
have this normal form over their original field, including finite and
nonperfect fields. The pinned sharp-four package proves the converse and
source rank exactly14 at every invertible coefficient point of W0. This
classifies these four-spaces; characteristic-two three-spaces, singular
coefficient families and compatible tensor maps are outside this theorem.

Geometric vanishing is essential: a rank condition at the rational points
of a finite field alone does not imply the polynomial hypothesis. Write
k=Kbar for intermediate classification. Dimension and polynomial identities
are preserved by scalar extension; Section7 returns the changes to K.

For g=[[alpha,beta],[gamma,delta]], define the ordinary binary coefficient
matrix

    A(g)=[[alpha^2,alpha*gamma,gamma^2],
          [2alpha*beta,alpha*delta+beta*gamma,2gamma*delta],
          [beta^2,beta*delta,delta^2]].

The pinned source construction gives rank-preserving transformations
M -> A(g) M A(h)^t and M -> M^t. These preserve the full source, including
its endpoints; arbitrary GL3 coefficient changes generally do not. We use
arbitrary GL3 changes only inside the singular-space lemma below and undo
them before applying source equations. All source and invariant dependencies
are identified by hashes in sources.json.

## 1. The intrinsic singular three-section

For M=[[a,b,c],[d,e,f],[g,h,i]] set

    A2=2ai+2cg-bh-df,
    T4=a^2*i^2-abhi-2acgi+ach^2-adfi+af^2g+b^2gi-bcgh
       +bdfh-befg+c^2g^2+cd^2i-cdeh-cdfg+ce^2g.

The pinned integer identity is

    detR=D*P12,
    P12=D^4+(eD+2T4)*(eD*T4+T4^2-A2*D^2).

The polynomial ring K[W] is a domain. Since D is nonzero, detR=0 forces
P12=0. In its fraction field ell=T4/D satisfies

    2ell^3+3e*ell^2+(e^2-2A2)*ell+D-e*A2=0.

Divide by two to obtain a monic equation. Integral closedness makes ell a
polynomial, and its homogeneous degree one makes it K-linear. Hence

    T4=D*ell, D=(e+2ell)*(A2-e*ell-ell^2).

Put m=e+2ell. This nonzero linear form defines the three-space U=ker m,
with D|U=T4|U=0. It is not generally the section e=0.

These sections are intrinsic under permitted binary changes. For
J=[[0,0,-2],[0,1,0],[-2,0,0]] and H=M^t J M J, direct identities give

    trH=e^2+4A2, s2(H)=16T4+8eD, m=s2(H)/(8D),
    A(g)^t J A(g)=det(g)^2 J, det A(g)=det(g)^3.

If M'=A(g) M A(h)^t and delta=det(g)det(h), then
H'=delta^2 A(h) H A(h)^(-1), D'=delta^3 D, and m'=delta*m.
Transposition preserves D,e,A2,T4 and m. Thus U remains the distinguished
section throughout permitted changes. The displayed expressions use only
powers of two as constant denominators, so they include characteristic three.

## 2. Singular three-space lemma in odd characteristic

Over k, a singular three-space in Mat3 is contained in a common-kernel
six-space, a common-left-kernel six-space, a compression
C(L,E)={M:M(E) subset L}, dimL=1,dimE=2, or is left-right equivalent to the
alternating three-space. We give the signed proof to avoid importing
characteristic-two signs.

A rank-at-most-one matrix space has a fixed image line or fixed row
functional line. Indeed, relative to x*phi^t, every y*psi^t shares one
factor, or their sum has rank two. Members differing in the two respective
factors cannot both occur, since their own sum would have rank two. This
proves the lemma in the rank-one case.

Otherwise temporarily normalize a rank-two member to diag(I2,0). Every
B has form [[P,u],[v^t,0]], since the determinant linear coefficient forces
the bottom-right entry to vanish. The remaining coefficients give
v^t u=0 and v^t adj(P)u=0. Let I be the image in pairs(u,v). The quadratic
v^t u has nondegenerate polar form on four variables, so the totally
isotropic image has r=dimI<=2. Its kernel K0 in Mat2 has dimension3-r.
If r=0 or either projection is zero, a common kernel or left kernel exists.

For r=1 with both factors nonzero, normalize their perpendicular lines to
u along e0 and v along e1. The cubic identity forces P21=0 on the whole
space, including K0. The matrices are then supported in the first row or
second column, a compression. For r=2 with one projection of rank one,
the pointwise identity v^t u=0 forces the other projection into the
perpendicular line: a product of a nonzero linear form and v^t e0 cannot
vanish identically otherwise. Thus I is the product of two lines, and the
cubic again forces P21=0, yielding the same compression.

If r=2 and both projections have rank two, write v=L u. The pointwise
identity makes L an invertible skew matrix. Scale to v=J2*u,
J2=[[0,-1],[1,0]]. The common annihilator of the functionals
P -> (J2*u)^t adj(P)u is k*I2; explicitly the quadratic is
-P21*x^2+(P11-P22)*xy+P12*y^2. Thus K0=k*I2. Take a linear section

    P=[[a*x+b*y,c*x+d*y],[f*x+g*y,h*x+j*y]].

Its cubic is -f*x^3+(a-h-g)*x^2*y+(b-j+c)*x*y^2+d*y^3, so
f=d=0,h=a-g,j=b+c. Absorb(a*x+b*y)I2 into the scalar coordinate lambda,
leaving P=[[0,c*x],[g*y,-g*x+c*y]]. Right multiplication by
[[I2,0],[(-g,-c),1]] adds u*(-g,-c), giving -g*x*I2, again absorbed.
The family becomes [[lambda,0,x],[0,lambda,y],[-y,x,0]]. Left multiplication
by [[0,1,0],[-1,0,0],[0,0,1]] makes it
[[0,lambda,y],[-lambda,0,-x],[-y,x,0]], the full alternating space.
Undoing the temporary changes gives P0*Alt(x)*Q0 in the original coordinates.
This exhausts all cases without asserting GL3 source invariance.

## 3. Primitive alternating and rank-one sections are impossible

For N=adjM put S(N)=N11^2-N10*N12-N01*N21+N00*N22 and
Q0(v)=v1^2-v0*v2. Exact integer identities give

    S(adjM)=T4+eD, S(u*v^t)=Q0(u)*Q0(v).

For Alt(x)=[[0,x2,-x1],[-x2,0,x0],[x1,-x0,0]], adjAlt=x*x^t.
Consequently on P0*Alt(x)*Q1, T4 is a nonzero scalar times the product
of two invertible linear substitutions into the nonzero quadratic Q0.
It is not the zero polynomial. This contradicts D=T4=0 on U.

If U has rank at most one, its dimension three makes it the full space
v*phi^t for fixed phi, or its transpose. The ordinary binary coefficient
action has two projective orbits over k, square and nonsingular quadratics,
represented by e0 and eta=(0,1,0). Normalize phi accordingly and put t=m.
For phi=e0, subtract U from the t=1 complement to obtain

    M=[[a,b0*t,c0*t],[d,e0*t,f0*t],[g,h0*t,i0*t]],
    D=t^2*L(a,d,g), ell=lambda*t.

The t^2 coefficient of T4 must vanish in T4=D*ell. Its a^2 and g^2
coefficients are i0^2 and c0^2, giving i0=c0=0. The remaining coefficient
is a*f0^2*g, so f0=0. The third column vanishes, contradicting D!=0.

For phi=eta, clear the complement's middle column instead:

    M=[[a0*t,b,c0*t],[d0*t,e,f0*t],[g0*t,h,i0*t]],
    D=t^2*L(b,e,h), ell=(t-e)/2.

The quartic T4 has only t^2 and t^4 terms. In D*ell the t^3 coefficient
is L/2, forcing L=0 and again D=0. Thus U has a rank-two member.

## 4. Nonsingular common-kernel vector is impossible

Common-kernel vectors transform by the dual action A(h)^(-t). Its conic is
u1^2-u0*u2=0, with two orbits over k: evaluation-conic e0 and nonsingular
eta. Suppose U*eta=0, so the middle column vanishes. Identifying the other
two columns with Mat(3,2), its quartic is

    T4=m02^2-m01*m12,

where mrs are the row minors. At a rank-two member, the column-plane normal
(m12,-m02,m01) lies on the evaluation conic. Permitted left binary action
normalizes that plane to the first two rows. Temporarily mix the two columns
by GL2 to make the chosen member [[1,0],[0,1],[0,0]]. This temporary change
is used only on U: it scales all minors together and hence preserves T4=0.
It need not preserve source rank on W. We undo it before using W below.

Write B=[[p,q],[r,s],[u,v]]. The first two coefficients of T4(A+tB) are
u and v^2-r*v+(p+2s)*u. Hence u=0 and v(v-r)=0. If v is a nonzero
linear form on U, r=v, the cubic gives (p-s)*v^2=0 and then p=s; the
quartic gives q*v^3=0 and then q=0. Only p,v remain, contradicting
three-dimensionality. Thus v=0. Undoing the temporary column change
preserves the conclusion that the bottom row vanishes. Therefore

    U subset {[[a,0,c],[d,0,f],[0,0,0]]}.

Here e|U=ell|U=0. Let h0 be the bottom-middle entry of a t=1 complement.
The identity D=t*(A2-eell-ell^2), restricted to its t coefficient, gives

    h0*(af-cd)-df=0 on U.

The polar determinant in a,c,d,f is h0^4. A nondegenerate quadratic in
four variables cannot contain an isotropic three-space, so h0=0. Now
df=0 on U, hence d=0 or f=0 identically. A permitted outer-column swap
interchanges them. By dimension, U is exactly
{[[a,0,c],[d,0,0],[0,0,0]]}. Subtract it from the complement to write

    M=[[a,b0*t,c],[d,e0*t,f0*t],[g0*t,0,i0*t]], ell=lambda*t.

In T4=D*ell the c^2 coefficient is g0^2*t^2 on the left and zero on the
right, so g0=0. The c*d^2*t coefficient then forces i0=0. The bottom row
vanishes and D=0, a contradiction. Transposition excludes the analogous
nonsingular common-left-kernel case.

## 5. Compression cases give evaluation kernels

The line L and the annihilator line Eperp in a compression transform by
ordinary binary coefficient actions. Each is square or nonsingular over k.
Normalize each to e0 or eta. The four containers and exact T4 restrictions are

    [[a,b,c],[d,0,0],[g,0,0]]: c^2*g^2;
    [[a,b,c],[0,e,0],[0,h,0]]: a*c*h^2;
    [[a,0,0],[d,e,f],[g,0,0]]: a*g*f^2;
    [[0,b,0],[d,e,f],[0,h,0]]: b*d*f*h.

A vanishing product in k[U] forces one displayed linear factor to vanish.
Each possibility makes a first or third row or column zero. Thus U has
a conic common kernel or common left kernel. Together with Sections2-4,
all surviving cases have such an evaluation-conic line; transpose if needed.
The mixed-compression restriction is a*c*h^2, not zero identically. The
original false zero assertion was caught by exact replay and corrected
before this proof; its nonzero factor is essential to the reduction.

## 6. The first-column direction is also conic

Normalize the common kernel to e0. Every first column in W is m*v for a
fixed nonzero vector v; v=0 would make D identically zero. The ordinary
column conic is v1^2-4v0*v2=0; keep this coefficient convention separate
from the dual kernel formula u1^2-u0*u2. The equations coincide in
characteristic three, and the argument includes that case.
If v is nonsingular, permitted left binary action normalizes it over k to
d*eta with d!=0. Rename m=t. Then

    M=[[0,b,c],[d*t,e,f],[0,h,i]],
    d*(ch-bi)+bh-e^2/4+d*t*f+t^2/4=0.

The second equation is the full determinant identity from Section1. On U,
the quadratic Q=d(ch-bi)+bh-e^2/4 has radical span(f). Its polar determinant
in b,c,e,h,i is -d^4/2, so the full six-variable polar form has rank five
in every odd characteristic. An isotropic three-space contains its radical:
its image in the nondegenerate five-dimensional quotient has dimension at
most two. Thus U contains the pure f direction. Translating W along that
direction changes the full identity by d*t*s, a nonzero polynomial. This
contradiction proves that v lies on the ordinary column conic.

## 7. Normalize over the original field

The preceding cases hold over k. Since U has a rank-two member over k,
any common kernel or common left kernel is exactly one-dimensional. It
is the solution of linear equations defined over K; scalar extension
preserves their rank, so it has a K-basis. This proves descent even for
nonperfect K without appealing only to Galois invariance. Transpose over K
if needed and let u be this kernel vector.

For a K-rational evaluation-conic vector with u0!=0, normalize its scalar
to u=(1,r,r^2). Then h=[[1,0],[r,1]] satisfies A(h)^(-t)*u=e0. If u0=0,
the conic forces u1=0, and a variable swap handles the endpoint. Thus we
can normalize U*e0=0 over K, and m remains K-linear by relative covariance.
The vector v in firstcolumn=m*v lies in K^3. Its ordinary conic equation
makes it a K-scalar times the square of a K-linear form: for v0!=0 it is
v0*(1,2r,r^2), r=v1/(2v0). The change g=[[1,-r],[0,1]] maps this vector
to v0*e0. An endpoint is again handled by swapping. Hence choose g over K
with A(g)v=c*e0, c!=0.

Set h=diag(s,1), which preserves the kernel e0. Under M'=A(g) M A(h)^t,
firstcolumn(M')=s^2*c*m*e0 while m'=det(g)*s*m. Choose s=det(g)/c.
Then firstcolumn(M')=m'*e0. Rename m'=t to achieve, using only permitted
changes over K,

    M=[[t,b,c],[0,e,f],[0,h,i]], m=t, ell=(t-e)/2.

The orientation of the first explicit h matters: [[1,r],[0,1]] would
send (1,r,r^2) to ((r^2-1)^2,r-r^3,r^2), not e0, under A(h)^(-t).
The verifier retains this discovered audit-example correction.

## 8. The evaluation-kernel section forces the triangular normal form

In the normalization above, the two invariant identities become

    Q=ei-fh+bh-e^2/4-2ti+t^2/4=0,
    C=t*i^2-bhi+c*h^2-(ei-fh)*(t-e)/2=0.

Restrict to U (t=0). Combining 8C-4eQ gives

    8c*h^2-4bh*(2i+e)+e^3=0.

If h is a nonzero linear form on U, primality in K[U] gives h|e. Write
e=k*h. Then Q gives f=b+k*i-k^2*h/4, and the combined equation reduces to

    8ch-8bi-4kbh+k^3*h^2=0.

It forces h|b*i, so b=beta*h or i=iota*h. In the first case
c=beta*i+(beta*k/2-k^3/8)*h; in the second
c=(iota+k/2)*b-k^3*h/8. All coefficient entries then depend on at most
two linear coordinates, contradicting dimU=3. Therefore h|U=0.
Now Q gives e(i-e/4)=0 and C gives e^2*i=0 on U. If e were nonzero,
these would force both i=e/4 and i=0, a contradiction. Thus e|U=0 also.

Write e=e0*t,h=h0*t on W. Divide Q,C by their common factor t in the
polynomial domain to get

    (e0-2)i+h0*(b-f)+(1-e0^2)*t/4=0,
    i^2-h0*b*i+h0^2*c*t-t*(1-e0)*(e0*i-h0*f)/2=0.

If h0!=0, the first equation solves f. On U, the second gives
i(i-h0*b)=0, so one linear factor vanishes identically. The map U into
coordinates(b,c,i) is injective after solving f; either factor confines
that image to a two-dimensional hyperplane. This contradicts dimU=3.
Hence h0=0.

Now D=t^2*e0*i is nonzero, so e0 and i are nonzero. The second equation
factors as i*(i-e0*(1-e0)*t/2)=0, forcing i=e0*(1-e0)*t/2. Substitution
into the first gives

    -t*(e0-1)^2*(2e0-1)/4=0.

The root e0=1 would make i=0 and is excluded. Thus e0=1/2 and i=t/8.
No step divided by e0-2 or by three: in characteristic three the surviving
root is e0=2, and the same conclusion holds. Therefore W is contained in
{[[t,b,c],[0,t/2,f],[0,0,t/8]]}. Both spaces have dimension four, so they
are equal. Renaming t=8t gives W0 and proves the theorem over K.

## Evidence boundary and consequences

Every equality case satisfies the intrinsic identities

    16D=m^3, 4(e^2+4A2)=5m^2.

Indeed, the normal form has m=8t,D=32t^3,e^2+4A2=80t^2. Under permitted
binary changes these three quantities scale by delta,delta^3,delta^2,
respectively, and transposition preserves them. Thus the identities hold
in the original coordinates too, including characteristics three and five.
The singular three-section becomes the full strictly upper-triangular
space under the permitted normalization. These are consequences of the
classification, not hypotheses.
The sharp-four source kernel and minor remain credited to their original
package. The prior characteristic-two package supplied the template for
singular-space case organization; the signed odd-characteristic lemma,
complement reduction and descent are written here in full.

The maintained verifier checks the integer invariant identities, singular
three-space algebra, all compression restrictions, rank-one and eta
coefficients, polar minors, conic identities and normalization orientation.
The two intrinsic consequences are checked on the normal form. Their
transport to original coordinates follows from the written covariance
argument, supported by the exact binary-action identities; the verifier
does not directly expand the full symbolic conjugation formula.
These computations do not certify the geometric exhaustion, integral
closedness or descent argument. Those remain written proofs with a separate
same-session audit, not independent review or a formal theorem. No
compatible three-leg tensor map or matrix-multiplication exponent follows.
