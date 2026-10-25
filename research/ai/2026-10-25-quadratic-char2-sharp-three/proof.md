# Sharp characteristic-two invertible quadratic dimension bound

October 25, 2026. Claim `AI-CHAR2-QUADRATIC-SHARP-THREE-001` is a written,
unreviewed proof. Exact polynomial controls and a separate same-session
algebra audit corroborate the argument; neither is independent mathematical
review, formalization, or an exponent improvement.

**Theorem.** Over any field K of characteristic two, a K-linear coefficient
family W for the complete literal quadratic source R_(3,3), with geometric
source rank at most fourteen and coefficient determinant not identically
zero, has dimension at most three. This bound is attained over every such
field by the pinned universal three-plane. Thus the maximum dimension is
exactly three. No classification of all attaining three-spaces is asserted.

The geometric hypothesis means that det R vanishes as a polynomial on W,
not merely at K-rational points. Write M=[[a,b,c],[d,e,f],[g,h,i]]. Rows of
the 15-by-15 source are (j,L), j=0,1,2 and L=0,...,4; columns are (H,r),
H=0,...,4 and r=0,1,2, in lexicographic order, with

    R[(j,L),(H,r)]=M[H-j,L-r],

and out-of-range entries zero. The pinned cap-four package supplies the
integer determinant identity, its integral-linear-form equivalence in
characteristic two, and the permitted binary actions. In characteristic two,

    A2=bh+df,
    T4=a^2*i^2+abhi+ach^2+adfi+af^2g+b^2gi+bcgh+bdfh
       +befg+c^2g^2+cd^2i+cdeh+cdfg+ce^2g,
    det R=D^2*(D^3+e^2*D*T4+e*T4^2+e*A2*D^2), D=det M.

These formulas come from integer representatives before reduction. No
uncleared division by two is used. Exact dependencies and prior attribution
are recorded in sources.json. All new case arguments are given below;
no unpublished scratch note is a proof or runtime dependency.

Pass to the algebraic closure k. If dimW>=4 and D|W nonzero, choose a
four-space through an invertible point. The pinned integral lemma gives

    T4=D*ell,     D=e*q,     q=A2+e*ell+ell^2,
    U=W intersect {e=0},    dimU=3,    D|U=T4|U=0.

Here M=[[a,b,c],[d,e,f],[g,h,i]], A2=bh+df, and T4 is the pinned integral
quartic reduced modulo two. Every normalization of W below uses permitted
binary actions M -> A(g) M A(h)^t and re-applies the integral lemma.
Here for g=[[alpha,beta],[gamma,delta]],

    A(g)=[[alpha^2,alpha*gamma,gamma^2],
          [0,det(g),0],
          [beta^2,beta*delta,delta^2]].

These actions multiply e by det(g)*det(h), preserving the e=0 section.
Their kernel-vector orbits have representatives eta=(0,1,0), e0=(1,0,0),
and e0+eta. The pinned equality proof establishes these source symmetries
using ordinary monomial bases and duals, without division by two.
Arbitrary GL3 actions in the singular-space classification do not preserve
source rank and are undone before the exclusions.

## 1. Singular three-space classification in characteristic two

Every singular three-space U in Mat3(k) is contained in a common-kernel
six-space, common-left-kernel six-space, a five-dimensional compression
C(L,E)={M:M(E) subset L}, dimE=2,dimL=1, or is left-right equivalent to the
three-space of alternating matrices. This claim has an elementary proof.

The rank-one pencil lemma says a space of rank-at-most-one matrices has
a fixed image line or a fixed row functional line: for a fixed nonzero
x*phi, any y*psi must share one factor, or their sum has rank two. A
member differing in image and a member differing in functional cannot
both occur, since their own sum would have rank two. This also bounds
such a space by the larger matrix side.

If every matrix has rank at most one, that lemma forces a
fixed image or fixed row functional, yielding a kernel container. Otherwise
choose rank-two A, temporarily make it diag(I2,0), and write each member as
B=[[P,u],[v^t,0]]. The determinant coefficients give the pointwise identities
v^t u=0 and v^t adj(P)u=0. If I is the image in pairs (u,v), the
nondegenerate polar form of v^t u makes I isotropic, so r=dimI<=2.
Retain the pointwise quadratic identity in characteristic two; polar
isotropy alone is insufficient. If K0 is the kernel in Mat2, dimK0=3-r. If r=0, a common kernel exists.

If r=1, a zero factor gives a kernel container. Otherwise u0,v0 are
nonzero and perpendicular; the functional f0(P)=v0^t adj(P)u0 annihilates
K0 and the linear section. Normalize u0=e0,v0=e1 by simultaneous block
changes. Then p21=0, and all matrices are supported in the first row or
second column: a five-dimensional compression. For r=2 with a projection
of rank zero, a kernel exists. If a projection has rank one, pointwise
v^t u=0 forces the other projection into its perpendicular line, so I is
the product of two lines. The K0 and section cubic identities again force
p21=0 and give the same compression.

If r=2 and both projections have rank two, write v=L u, with L invertible.
The pointwise identity u^t L u=0 makes L a nonzero scalar multiple of
J=[[0,1],[1,0]]. Scale the bottom row to set L=J. The annihilator of all
functionals P -> (Ju)^t adj(P)u is precisely k*I2, so K0=k*I2. Choose a
linear section P(x,y), u=(x,y), v=(y,x). Write

    P=[[a*x+b*y,c*x+d*y],[f*x+g*y,h*x+j*y]].

The cubic (Ju)^t adj(P)u=0 forces
f=d=0, h=g+a, j=c+b. Absorb (a*x+b*y)I2 in the scalar coordinate lambda:

    P=[[0,c*x],[g*y,g*x+c*y]].

Right multiplication by [[I2,0],[(g,c),1]] adds u*(g,c) to P, leaving
P=g*x*I2, which can again be absorbed in lambda. The family becomes
[[lambda,0,x],[0,lambda,y],[y,x,0]]. Swapping its first two rows gives
[[0,lambda,y],[lambda,0,x],[y,x,0]], the full alternating three-space.
This exhausts the classification. All changes here are temporary coefficient
changes only, with inverse changes included in the resulting P Alt(x) Q
representation in the original coordinates.

## 2. Primitive alternating type cannot have T4=0

For an arbitrary 3-by-3 M in characteristic two, let N=adj(M) and

    S(N)=N11^2+N10*N12+N01*N21+N00*N22,
    Q0(v)=v1^2+v0*v2.

Direct polynomial expansion gives

    S(adj(M))=T4(M)+e*D(M),
    S(u*v^t)=Q0(u)*Q0(v).

For Alt(x)=[[0,x2,x1],[x2,0,x0],[x1,x0,0]], adj(Alt(x))=x*x^t.
If U=P Alt(x) Q with P,Q invertible, then

    adj(M)=det(P)*det(Q)*(Q^-1*x)*(P^-t*x)^t.

Since D=0, T4 is the product of the two nonzero quadratic polynomials
Q0(Q^-1*x) and Q0(P^-t*x), times a nonzero square scalar. Neither quadratic
can be zero because its linear substitution is invertible. Their product
is nonzero in k[x0,x1,x2], contradicting T4|U=0. This argument works in
the original coordinates; it does not assert source invariance under P,Q.

## 3. Common kernel eta

Identify C_eta with Mat_(3,2), using columns 0 and 2. Its quartic is
T4=m02^2+m01*m12, where mij are the row minors. Both rank possibilities
must be handled: unlike a four-space, a three-space can consist entirely
of rank-one matrices.

### 3.1. The section contains a rank-two matrix

For a rank-two A, the column-plane normal (m12,m02,m01) lies on the conic
n1^2+n0*n2=0, whose points over k are evaluation vectors (s^2,st,t^2).
The permitted left action is transitive on this conic of normals, through
A(g)^(-t). The permitted right action on columns 0 and 2 is entrywise-square
GL2, hence every GL2 over the algebraic closure. As in the pinned cap-four
proof, normalize A to [[1,0],[0,1],[0,0]], preserving C_eta and e=0.
For B=[[p,q0],[r,s0],[u,v]] in U, the coefficients of T4(A+tB) are

    [t]   u,
    [t^2] v^2+r*v+p*u,
    [t^3] (p+s0)*r*v+(s0^2+q0*r)*u,
    [t^4] (p*v+q0*u)^2+(p*s0+q0*r)*(r*v+s0*u).

Thus u=0 and v*(v+r)=0 on U. If v is nonzero, r=v, the cubic gives p=s0,
and the quartic gives q0=0. Only p,v remain, contradicting dim U=3.
Therefore v=0 and U lies in the four-space
B={[[a,0,c],[d,0,f],[0,0,0]]}.

Choose an e=1 complement M0 and denote its bottom-middle entry by h0.
Regardless of its other entries,
q|U=h0*(af+cd), A2|U=df. Hence h0*(af+cd)+df restricts to ell_U^2.
Its polar determinant in a,c,d,f is h0^4. A nondegenerate alternating
form on four dimensions cannot have a three-dimensional isotropic space,
so h0=0. The polar form of df has radical span(a,c). An isotropic U3
contains this radical, hence has arbitrary first row and one second-row
line in (d,f). The permitted right action normalizes that line to (1,0),
retaining h0=0. Reapply the integral lemma in the new coordinates:

    U={[[a,0,c],[d,0,0],[0,0,0]]},       ell_U=0.

Subtract U from the e=1 complement, obtaining

    M=[[a,b0*t,c],[d,t,f0*t],[g0*t,0,i0*t]],
    q=t*(a*i0+b0*d*i0+c*g0)+b0*f0*g0*t^2,
    A2=d*f0*t,       ell=lambda*t.

The a*t and c*t coefficients of q=A2+t*ell+ell^2 force i0=g0=0,
making D identically zero, a contradiction. Subtracting U may make the
chosen complement singular; the proof uses only nonzero D on W.

### 3.2. Every section matrix has rank at most one

The rank-one pencil lemma gives a fixed image line or a fixed row
functional. In Mat_(3,2), a fixed image has dimension at most two, so U3
must be the full space {v*phi:v in k^3} for a nonzero row functional phi.
The permitted right squared GL2 action sends phi to (1,0), making U the
first-column-only space. Subtract U from an e=1 complement to write

    M=[[a,b0*t,c0*t],[d,t,f0*t],[g,h0*t,i0*t]],
    D=t^2*L,
    L=a*(i0+f0*h0)+d*(b0*i0+c0*h0)+g*(b0*f0+c0),
    q=t*L,       A2=d*f0*t+b0*h0*t^2.

The restricted square identity gives ell_U=0, so ell=lambda*t. Comparing
a*t,d*t,g*t coefficients gives

    i0+f0*h0=0,    b0*i0+c0*h0=f0,    b0*f0+c0=0.

Substitution of the first and third into the middle equation yields f0=0,
then c0=i0=0. Consequently L=0 and D=0, a contradiction. Both branches
are excluded; transposition gives the middle-left-kernel case.

## 4. Common kernel e0: evaluation-vector orbit

U is a three-space in the five variables b,c,f,h,i with first column and
e zero. Choose an invertible M0 with e(M0)=1. Its first column is (A,d0,G).

If d0 is nonzero, this coefficient vector is a nonsingular binary quadratic.
An allowed left change sends it to (0,d,0), d nonzero; rescale the complement
to e=1 again. The condition first column zero on U is preserved. Writing
e=t, one has first column (0,dt,0), and

    q=d*(bi+ch),        A2=bh+d*t*f,
    q|U+A2|U=d*(bi+ch)+bh.

The last quadratic has polar rank four with radical the pure f direction.
A three-dimensional isotropic U must contain that radical. Thus f is a free
coordinate in W. In q=A2+t*ell+ell^2, the f^2 coefficient forces ell_f=0,
and then the t*f coefficient is d on the right and zero on the left, a
contradiction. Arbitrary complement offsets of b,c,h,i do not depend on f.

Therefore d0=0. The first column of M0 is nonzero because M0 is invertible.
It is a square binary quadratic, so an allowed left change sends it to
(A,0,0), A nonzero. An additional diagonal binary change adjusts the ratio
of first entry to e to one. Hence first column (t,0,0), e=t, and

    D=t*(t*i+f*h),       q=t*i+f*h,       A2=bh,
    q|U+A2|U=h*(b+f).

The polar radical in the ambient five-space is span(c,i,b=f,h=0), of
dimension three. An isotropic U3 intersects that radical in dimension at
least two, and hence intersects span(c,i) nontrivially. Let its direction
be (c=C,i=I). Absence of its square term in q+A2 forces ell on this
direction to be zero; the t times this direction coefficient then forces
I=0. Thus the pure c direction belongs to U, and ell_c=0.

For these first-column coordinates, the full quartic is

    T4=t^2*i^2+t*b*h*i+t*c*h^2.

Comparing the free c coefficient in T4=D*ell forces t*h^2=0 as a polynomial,
so h=0 on W. Now q=t*i and A2=0. Restricting to U gives ell_U=0, so
ell=lambda*t; the q identity gives i=delta*t, delta=lambda+lambda^2.
D nonzero forces delta nonzero. T4=D*ell gives delta^2=delta*lambda, so
delta=lambda, hence lambda^2=0 and delta=0, a contradiction.

## 5. Common kernel e0+eta

U is a three-space in the five variables a,c,f,g,i with d=e=0,b=a,h=g.
Its quartic is (ai+cg)^2+ag*f^2. If f vanishes on U, then ai+cg vanishes
there. The polar form of ai+cg on the remaining four variables is
nondegenerate, so a three-space is impossible. Thus f is nonzero.
Unique factorization of (ai+cg)^2=ag*f^2 forces the linear forms a,g on U
to be proportional unless one vanishes; their joint image has dimension
at most one. If both vanish, U is the full third-column-only space and
has common kernel eta, already excluded.

Otherwise an allowed left binary action sends the nonzero coefficient
line (a,0,g) to the first coordinate line. The common-kernel equation is
preserved by left multiplication. Reapply the integral lemma to get T4=0
in the new coordinates. Now g=0 and a is nonzero, so T4=a^2*i^2 forces i=0.
By dimension U is the entire space [[a,a,c],[0,0,f],[0,0,0]]. Subtract U
from an e=1 complement:

    M=[[a,a+b0*t,c],[d0*t,t,f],[g0*t,h0*t,i0*t]].

Here q|U=a*f*(h0+g0), A2|U=0. Being a square forces h0=g0 and ell_U=0.
With ell=lambda*t, the coefficient of t in q=A2+t*ell+ell^2 gives

    i0*(1+d0)=g0,       b0*g0=d0,       g0*(1+d0)=0.

Indeed q=t*[a*i0*(1+d0)+b0*f*g0+c*g0*(1+d0)]+b0*d0*i0*t^2,
and A2=t*(a*g0+d0*f)+b0*g0*t^2. If g0=0 the first two equations give
d0=i0=0 and D=0. If g0 is nonzero, the third gives d0=1, contradicting
the first. The mixed kernel orbit is excluded.
Transposition handles all common-left-kernel containers.

## 6. Compression containers

Suppose U is contained in C(L,E), dimension five. If C is contained in
e=0, permitted normalization makes it the first-row/first-column space
[[a,b,c],[d,0,0],[g,0,0]]. T4=c^2*g^2 forces c or g to vanish on U, giving
an evaluation-vector common kernel or left kernel, already excluded.

Otherwise U is contained in V=C intersect {e=0}, dimension four. If eta
belongs to E and L is outside eta-perp, V has common kernel eta. If eta is
outside E and L lies in eta-perp, V has common left kernel eta. Both are
excluded. In the remaining case eta is outside E and L is outside eta-perp,
independent permitted changes normalize L=span(eta), E=eta-perp. Then

    V=[[0,b,0],[d,0,f],[0,h,0]],       T4=b*d*f*h.

Since k[U] is a domain, one of b,d,f,h vanishes on U. Respectively this
gives a common left kernel e0, common kernel e0, common kernel e2, or
common left kernel e2. These are all evaluation-vector cases. This closes
the last container. The case eta in E and L in eta-perp was exactly C
contained in e=0 and is already included.

## 7. Sharpness and evidence boundaries

Every singular-section container is excluded. Therefore no four-space W
with the stated hypotheses exists; the upper bound is three. The pinned
universal construction

    M(x,y,z)=[[x,x,0],[0,y,0],[0,z,z]]

has coefficient determinant xyz, a nonzero polynomial source kernel and a
literal 14-minor -x^6*y^3*z^5. It is defined over every field, and its point
x=y=z=1 is invertible with source rank fourteen. This supplies sharpness
without a field extension. The maximum outside characteristic two remains
in [3,4] under the preceding results; it is not decided here.

The first continuation explicitly identified a gap in reusing the
four-space rank-two premise for a three-space. Section 3.2 closes it; the
rank-one first-column family and its full extension obstruction are retained
in the exact checks. The verifier also checks the adjugate identities,
primitive block cubic and shear, polar minors, complete kernel-extension
formulas, and compression substitutions. It checks algebraic certificates,
not the geometric classification or dimension argument by computation.

Separate same-session auditing found no blocking algebraic error and
requested self-contained middle-kernel cases and explicit e=0 preservation;
both are included. This is not independent mathematical review, a claim of
historical priority, formalization, or an exponent improvement. Compatible
tensor maps and classification of all attaining three-spaces remain open.
