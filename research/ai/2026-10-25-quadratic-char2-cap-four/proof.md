# Characteristic-two cap four for invertible quadratic families

October 25, 2026. Written proof, unreviewed. Exact polynomial controls and
separate same-session algebra auditing corroborate this argument; they do
not establish independent mathematical review, formalization, historical
priority, or an exponent improvement.

**Theorem.** Over any field K of characteristic two, a linear coefficient
family W for the literal complete quadratic source R_(3,3), with geometric
source rank at most fourteen and D=det M not identically zero, has dimension
at most four. In particular this holds when W contains an invertible
K-rational coefficient point. Combining the pinned odd-characteristic cap
and universal three-plane gives lower bound three and upper bound four over
every field. Dimension-four sharpness remains open.

The geometric hypothesis means polynomial vanishing of det R on W, rather
than only vanishing at K-rational points. Extend to k=Kbar when classifying
spaces; dimension and polynomial identities are preserved. A nonzero D
then supplies an invertible point. No descent of a chosen normal form is
needed for the dimension bound.

## Source convention and integral invariants

Write M=[[a,b,c],[d,e,f],[g,h,i]]. The source rows are (j,L), j=0,1,2,
L=0,...,4, and columns (H,r), H=0,...,4,r=0,1,2, in lexicographic order:

    R[(j,L),(H,r)] = M[H-j,L-r],

with out-of-range entries zero. The pinned integer determinant proof gives

    A2 = 2ai+2cg-bh-df,
    T4 = a^2 i^2-abhi-2acgi+ach^2-adfi+af^2g
         +b^2gi-bcgh+bdfh-befg+c^2g^2+cd^2i-cdeh-cdfg+ce^2g,
    P12 = D^4+(eD+2T4)(eD*T4+T4^2-A2*D^2),
    det R = D*P12.

Reduce these integer polynomials before using characteristic two; no
division by 2048 is performed. Thus A2=bh+df and

    det R = D^2*G9,
    G9 = D^3+e^2*D*T4+e*T4^2+e*A2*D^2.

The exact local sources and earlier attribution are pinned in sources.json.
The integral-linear-form and four-space lemmas below publish the previously
unpublished prerequisites, so no scratch file is a runtime or proof dependency.

## 1. Integral linear form over the ground field

Let W be a K-linear family with D|W nonzero as a polynomial. Then
geometric rankR<=14 is equivalent to the existence of a (necessarily
unique, possibly zero) K-linear form ell on W such that

    T4=D ell,       D=e(A2+e ell+ell^2).                 (I)

Proof: work in the polynomial ring R=K[W]. D nonzero forces G9=0.
If e|W=0, G9=D^3 contradicts this, so e is a nonzero linear form.
Restriction to U=ker e gives D^3=0 in K[U], hence e divides D in R.
Write D=e q_D. In Frac(R), ell=T4/D satisfies

    ell^2+e ell+A2+q_D=0.

This is monic, so integral closedness of the polynomial ring puts ell
in R. The homogeneous quotient T4/D has degree one, or is zero; thus
ell is linear over K. Rearranging gives (I). Conversely, substitution
in G9 gives D^2[D+e^2 ell+e ell^2+e A2]=0, hence detR=0.
The argument uses polynomial identities, never a census of K-points.

## 2. Singular four-spaces over the algebraic closure

Over an algebraically closed field, every singular four-dimensional
subspace U of Mat_3 lies in a common-kernel six-space, a common-left-kernel
six-space, or a five-dimensional compression {M:M(E) subset L}, where
E has dimension two and L has dimension one. This extends the elementary
pinned equality package's singular-five-space proof; it is not asserted to be historically new.

For completeness, a rank-at-most-one linear matrix space has dimension
at most the larger matrix side. Fix a nonzero x*phi. A second rank-one
y*psi can share its pencil only if x,y or phi,psi are proportional;
otherwise a two-by-two minor of their sum is nonzero. If there is a member
with image outside k*x, its functional is proportional to phi, and any
member with functional outside k*phi must have image k*x. Those two
members would themselves have a rank-two sum, a contradiction. Thus the
whole space has a fixed image line or a fixed functional line. Its
dimension is bounded by the appropriate matrix side. Consequently a
singular four-space in Mat_3, or any four-space in Mat_(3,2), contains a
rank-two A. Temporarily
use arbitrary left/right GL3 coordinates to make A=diag(1,1,0). For
B=[[P,u],[v^t,b33]], det(A+tB)=0 gives b33=0 and

    v^t u=0,       v^t adj(P)u=0.

Let I be the image of U in pairs (u,v), r=dim I, and K0 its kernel in
Mat_2. The pointwise quadratic identity v^t u=0 implies that I is totally
isotropic for its nondegenerate polar form, so r<=2 and dimK0=4-r.
In characteristic two the pointwise identity is essential: polar
isotropy alone does not imply it.

If r=0, both common kernel and left kernel exist. If r=1 and one factor
of its generator is zero, one common kernel exists. Otherwise its factors
u0,v0 are nonzero and perpendicular. The nonzero functional
f0(P)=v0^t adj(P)u0 kills K0; dimK0=3 makes K0=ker f0. The cubic identity
on a lift of the generator puts that lift's P component in ker f0 too.
Normalize u0=(1,0)^t,v0=(0,1)^t by simultaneous block changes. All members
are then supported on the first row or second column, inside the stated
five-dimensional compression (the two off-block parameters are free in
the ambient compression, though only one is used by this U).

If r=2 and both projections I->u,I->v have rank two, write v=L u with
L invertible. The functionals f_u(P)=(Lu)^t adj(P)u span dimension three:
adj is a linear isomorphism on Mat_2, and multiplication by L^t is
invertible, so P->the binary quadratic f_u(P) is onto the three-dimensional
space of binary quadratics (also in characteristic two). Evaluations span
its dual because a quadratic vanishing at every vector over the infinite
field k is zero. This contradicts
K0 dimension two, since every f_u annihilates K0. Thus a projection has
rank at most one. Rank zero gives a common kernel or left kernel. For
rank one write u=a(z)u0; the polynomial identity a(z)*v(z)^t u0=0 implies
v(z) lies in u0-perp. Since I has dimension two, its pairs are exactly
(alpha*u0,beta*v0) for perpendicular nonzero u0,v0. K0 lies in ker f0.
For a linear section P(alpha,beta), the cubic identity
alpha*beta*f0(P(alpha,beta))=0 forces the section into ker f0. The same
normalization gives containment in the five-dimensional compression.

These arbitrary GL3 changes classify singular coefficient spaces only.
They do NOT preserve the literal source rank or A2,T4; the exclusions below therefore use only the permitted binary changes.

## 3. Reduction of the five-space and permitted changes

If the theorem fails, choose a five-space W through an invertible point.
The linear-form lemma gives a four-space U=W intersect {e=0}, with
D|U=T4|U=0. Write q=D/e, so q=A2+e*ell+ell^2.
The singular-four-space lemma supplies one of its three
containers. Put eta=(0,1,0)^t and e0=(1,0,0)^t.

For g=[[alpha,beta],[gamma,delta]] in GL2(k), the permitted action is

    A(g)=[[alpha^2,alpha*gamma,gamma^2],
          [0,det(g),0],
          [beta^2,beta*delta,delta^2]],
    M -> A(g) M A(h)^t.

As proved in the pinned equality package, these binary substitutions
preserve source rank by natural contraction and multiplication in ordinary
monomial bases and their duals. They scale e by det(g)*det(h). Their
kernel-vector orbits are eta,e0,e0+eta. Transposition preserves source rank
and A2,T4. Each transformed W therefore satisfies the linear-form lemma
with its own ell; no invariance of T4 under arbitrary GL3 is asserted.

## 4. Common kernel: the evaluation-vector orbit e0

The permitted kernel-vector action has projective orbits represented by
eta=(0,1,0), e0=(1,0,0), and e0+eta, as proved in the pinned equality package.
For kernel e0, U is a hyperplane in the five variables b,c,f,h,i with
first column and e zero. Choose an invertible M0 with e(M0)=1; it exists
because all e=0 points of W are singular. Write its first column (A,D0,G).
On W with e=t, the general first column is (At,D0t,Gt). The necessary
identity (I) restricted to U gives

    q|U+A2|U=A*f*h+D0*(c*h+b*i)+G*b*f+b*h=ell_U^2.

The polar form of this quadratic on the ambient five-space vanishes on
U, a four-space, so its rank is at most two. Its four-variable Pfaffian
on b,c,h,i is D0^2; hence D0=0. The remaining form on b,f,h has rank two
because its b-h coefficient is one. Its three-dimensional radical contains
the pure c and i directions. Every four-dimensional totally isotropic
subspace contains that full radical: the quotient is nondegenerate of
dimension two. Therefore U contains those two independent free directions.

Now W has d=0 and

    q=f*(A*h+G*b)+t*(A*i+G*c),       A2=b*h.

In the polynomial identity q=A2+t*ell+ell^2, absence of c^2 and i^2 forces
their coefficients in the linear form ell to be zero. The t*c and t*i
coefficients then force G=A=0. With D0=0, the chosen M0 has zero first
column and is singular, a contradiction. Arbitrary other entries of M0
do not affect this argument; c and i are genuinely free coordinates.

## 5. Common kernel: e0+eta

Here U lies in the five-space d=e=0,b=a,h=g, with coordinates a,c,f,g,i.
It is a hyperplane there, while direct reduction gives

    T4=(a*i+c*g)^2+a*g*f^2.

This polynomial has no linear factor. If a putative hyperplane equation
has nonzero f coefficient, solve it as f=L0(a,c,g,i). The i^2 coefficient
after substitution is a^2+a*g*lambda_i^2, never identically zero. If the
hyperplane equation has zero f coefficient, its linear form must divide
both a*g and (a*i+c*g)^2. It is therefore proportional to a or g, but
neither divides the latter. This contradicts T4|U=0.

## 6. Common kernel eta: a quartic four-space lemma

Middle column zero identifies C_eta with Mat_(3,2), using columns0 and2.
Let m01,m02,m12 be its three row minors. Then

    T4=m02^2+m01*m12.

For a rank-two member A, its column-plane normal n=(m12,m02,m01) lies on
the conic n1^2+n0*n2=0. A four-space contains a rank-two member: a linear
space of rank-at-most-one 3-by-2 matrices has dimension at most three.
Over k, the conic consists of evaluation vectors (s^2,s*t,t^2). The allowed
left action sends normals by A(g)^(-t), and A(g)^t maps evaluation vectors
by the ordinary change of (s,t), so this action is transitive on the conic.
Send the plane of A to span(e0,e1). On columns0,2 the allowed right action
is the entrywise-square GL2 block. Frobenius is onto over k, so this is
arbitrary GL2 and can make A=[[1,0],[0,1],[0,0]]. C_eta and e=0 are preserved.

For any B=[[p,q0],[r,s0],[u,v]] in U, expanding T4(A+tB) gives

    [t]   u,
    [t^2] v^2+r*v+p*u,
    [t^3] (p+s0)*r*v+(s0^2+q0*r)*u,
    [t^4] (p*v+q0*u)^2+(p*s0+q0*r)*(r*v+s0*u).

Thus u=0 on U and v*(v+r)=0 as a polynomial on U. Since k[U] is a domain,
either v=0 identically or r=v identically. The first case puts U in the
bottom-row-zero four-space, hence U equals it. In the second case assume
v nonzero; the cubic coefficient forces p=s0, then the quartic forces
q0*v^3=0, so q0=0. Only p,v remain, contradicting dimU=4.

Consequently the normalized U is exactly

    [[a,0,c],[d,0,f],[0,0,0]].

Subtract a member of U from an e=1 complement to make it
M0=[[0,b0,0],[0,1,0],[g0,h0,i0]]. This replacement may make the chosen
complement singular, which is harmless: W is unchanged and D|W remains a
nonzero polynomial. On X+tM0 one has

    q|U=h0*(a*f+c*d),        A2|U=d*f.

Their sum cannot be a square of a linear form: its d-f polar coefficient
is one. This contradicts (I), closing the eta orbit and, by transposition,
all common-left-kernel containers too.

## 7. The remaining five-dimensional compression containers

Let C={M:M(E) subset L}, dimE=2,dimL=1, contain U.

If C subset {e=0}, then eta belongs to E and L subset eta-perp. The same
permitted normalization as the pinned equality package makes C the first-row/first-column space
[[a,b,c],[d,0,0],[g,0,0]]. Its T4 is c^2*g^2. Since U is linear and k[U]
is a domain, c or g vanishes on U. Then U has respectively a common right
kernel or common left kernel, already excluded.

Otherwise U=C intersect {e=0}, by dimensions. If eta belongs to E and
L is not in eta-perp, the condition e=0 forces M eta=0 on U; this is the
common-kernel eta case. If eta is outside E and L subset eta-perp,
eta^t M vanishes on E and also on eta, hence on the entire domain: this
is a common-left-kernel eta case.

It remains that eta is outside E and L is not in eta-perp. Then both L
and the coefficient line annihilating E have nonzero middle coefficient.
Over k a binary quadratic with nonzero middle coefficient in characteristic
two has distinct roots, so an allowed binary change sends its line to eta.
The left and right choices are independent: on the domain E transforms by
A(h)^(-t), so its annihilator line transforms by A(h). Normalize
L=span(eta), E=eta-perp. Then

    C=[[0,b,0],[d,e,f],[0,h,0]],
    U=[[0,b,0],[d,0,f],[0,h,0]].

Here T4=b*d*f*h, a nonzero polynomial in the four free coordinates,
contradicting T4|U=0. Every container has now been excluded.

## Evidence, corrections, and remaining question

All possible containers for U have been excluded, proving the theorem.
Together with the pinned odd-characteristic theorem and universal
three-plane, the maximum invertible-family dimension is either three or
four over every field. The three-plane is already inclusion-maximal; any
four-space witness must use a different family. No such witness is supplied.

The earlier scratch derivation and this package received separate
same-session algebra audits, not independent mathematical review. The first
exact replay caught an incorrect pre-specialization cubic coefficient in
Section 6: its u multiplier is s0^2+q0*r, not p*s0+q0*r. The u=0 consequence
leaves the subsequent argument unchanged. The full formula is corrected and
a mutation regression rejects that actual discovery error. The proof also
retains the pointwise quadratic condition in the singular-space lemma and
explicitly allows the normalized eta complement to be singular.

The verifier checks characteristic-two polynomial identities, the integral
reduction and converse, the three orbit/compression substitutions, the
polar minor and complete Taylor expansion. Its report is algebraic
corroboration. It does not computationally certify the integral-closedness
argument, geometric classification, normalization, or dimension bound.
No finite-field point census replaces the polynomial hypotheses. No tensor
target, independent review, formalization, or exponent improvement follows.
