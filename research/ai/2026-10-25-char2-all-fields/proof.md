# Classification over every characteristic-two field

October 25, 2026. Claim `AI-CHAR2-ALL-FIELD-ATTAINERS-001` is
**proof-written-unreviewed**. Direct author audit and exact identities support
this proof; they are not independent review or formalization. The preceding
perfect-field result was merged in PR241 at
78825b4b38e79a7dd0c5a0d34f29fe93f2c2793b. Its exact source and discovery
records are pinned in sources.json. This result removes its perfection
hypothesis while preserving the earlier statements and attribution.

## Statement and conventions

For every characteristic-two field K, all geometric complete quadratic-source
attainer classes are

    (K/AS(K))_P disjoint-union {N} disjoint-union (K/AS(K))_V.

Here AS(K)={z^2+z:z in K}. An attainer is a three-dimensional K-linear
coefficient subspace W of Mat_3(K) with D=det(M) not identically zero and
geometric source rank at most fourteen. Explicitly, in lexicographic pair
orders with out-of-range coefficients zero, the complete source is

    R(M)[(j,L),(H,r)]=M[H-j,L-r], j,r=0,1,2 and L,H=0,...,4.

The condition is det(R(M))=0 as a polynomial on W, including over finite K.
This is stronger than vanishing at K-rational points. The pinned sharp-three
cap proves that dimension three is maximal in characteristic two.
Equivalence means independent permitted binary changes
M -> A(G) M A(H)^t and optional transpose, where

    A([[a,b],[c,d]])=[[a^2,a*c,c^2],[0,a*d+b*c,0],[b^2,b*d,d^2]],
    G,H in GL2(K).

Invertible linear parameter changes only reparametrize the same space.
The representatives of the two copies of [c] and the single N class are

    P_c(t,x,y)=[[c*t+x+y,t+y,t],[c*t,t,t],
                 [c^2*t+(c+1)*x+y,c*t+(c+1)*y+x,c*t]],
    N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]],
    M_(1,c), where
    M_LJ(t,x,y)=[[x,J^2*t,J^3*t],[y,t,x+(L*J^2+J)*t],
                  [L^3*t,L^2*t,y+(L+L^2*J)*t]].

The split V representative is M_00. The preceding arbitrary-field P theorem
is imported unchanged. The new work descends N and V without assuming K
perfect. The geometric classification supplies exactly the P,N,V types,
whose section common kernel dimensions/types distinguish them.

Put e=M11. The integral lemma gives e nonzero on W, a unique linear ell,
and identities T4=D*ell and D=e*(A2+e*ell+ell^2), where
A2=M01*M21+M10*M12 and T4 is the pinned integer quartic reduced modulo two.
The intrinsic section is U=ker(e|W). Binary actions scale e by
delta=det(G)det(H) and D by delta^3. Thus q_U=(D/e)|U transforms by a
nonzero scalar and invertible parameter substitution. Common kernels
transform by the dual actions A^-t, which preserve the evaluation conic
Q(u)=u1^2+u0*u2=0 and fix the eta line (0,1,0).

## 1. A form of N forces a ground-field square root

For a K-form of geometric N, the common section kernel spaces are kernels of
linear equations over K. Their dimensions are unchanged by field extension.
Orient the unique right evaluation kernel to e0 with the root-free normalizer
from PR241. The first column is e*v, with v nonzero and v1=0: otherwise the
geometric nonsingular first-column chart would give P. Put t=e. Swap outer
coordinates if necessary to make v0 nonzero, then use the right binary
diag(1/v0,1). The ratio of the first column to the new e becomes (1,0,C).
Thus every such family is

    M=[[t,b,d],[0,t,f],[C*t,h,i]].

The restrictions b|U,h|U are independent. To prove this without assuming a
root, extend to the algebraic closure and compare with N. In this orientation
any equivalence has no transpose, since the common kernel dimensions are
(1,0). The right binary factor preserves e0 under its dual action, hence is
upper triangular; it scales the middle column on U. The left factor is
invertible. Thus its middle-column image rank agrees with the rank-two
middle-column image (x,0,y) of the canonical N. Rank is unchanged by field
extension. Consequently t,b,h are K-coordinates.

Write f=A*b+B*h+k*t and ell=lambda*b+mu*h+alpha*t. In this chart A2=b*h,
and literal determinant expansion gives

    D/t = t*i + f*h + C*b*f + C*d*t.

The integral equation Q=D/t+A2+t*ell+ell^2=0 restricts on U to

    (A*C+lambda^2)*b^2 + (A+B*C+1)*b*h + (B+mu^2)*h^2 = 0.

Independent coefficient comparison gives B=mu^2 and A=1+C*mu^2, followed by

    (lambda+C*mu)^2=C.

Thus r=lambda+C*mu is a square root of C already in K, forced by attainment.
The binary G=[[1,r],[0,1]] satisfies A(G)*(1,0,C)^t=(1,0,0)^t and has
determinant one. The first column is now exactly t*e0. The pinned square-chart
classification works over any field once this chart exists and has an explicit
shear to N. Hence every N-form is N over K, without perfection. The maintained verifier checks the full restricted equation, the forced root and its action.

## 2. Normalize the moving V section using the left factor

For a K-form of geometric V, orient its intrinsic section so its common right
kernel is eta and its left common kernel is zero. Its generic rank is two.
The ground-field primitive-adjugate and linear-vector arguments from PR240
apply in K[x,y]: adj(M)=eta*v^t, with v primitive quadratic and Q(v)=0.
Unique factorization gives

    v0=alpha*l0^2, v1=beta*l0*l2, v2=gamma*l2^2,
    beta^2=alpha*gamma,

with nonzero constants and independent linear l0,l2 over K. Divide v by alpha
and put y=l0, x=(beta/alpha)*l2. Then its line is (y^2,x*y,x^2), with no
square root extraction. The degree-one syzygies give the two outer section
columns K(x,y)C, C in GL2(K), where K(x,y)=[[x,0],[y,x],[0,y]].

The earlier proof used a right factor whose entrywise square was C^(-1).
Instead use the exact identity

    A(G)K(x,y)=K(G^t*(x,y)^t)*G^t.

Let Delta=det(C) and choose G=adj(C)^t. This is an invertible binary matrix
over K, with determinant Delta. Then

    A(G)K(x,y)C = K(Delta*adj(C)*(x,y)^t).

The displayed parameter change has determinant Delta^3, nonzero. Thus the
moving section normalizes over every K using the LEFT binary action alone.
The middle column remains zero on U and e scales by nonzero Delta. The
pinned extension coefficient proof uses no roots or divisions by L,J and
therefore gives exactly M_LJ over K. No perfection is used. For example, over the nonperfect field F2(s),
C=diag(s,1) is normalized by the left G=diag(1,s), with parameters
(s*x,s^2*y). This avoids adjoining a square root of s or 1/s.

## 3. Realize enough stabilizers without square roots

For any T in GL2(K), take G=T^[2] (entrywise square) and H=(T^t)^(-1).
Then H^[2]=(G^t)^(-1); both binary factors exist over K by ordinary matrix
inversion. The permitted pair preserves the normalized section with
parameters z=G^t*(x,y)^t and scale delta=det(T). Its action on q_U is the
usual weighted action for G. Because q_U=L^2*x^2+xy+J^2*y^2, the induced
pair transformation is the ordinary weighted action on (L,J), without roots.
We need only these exact generator identities (the script checks whole
three-by-three families, not merely the section):

* T=diag(a,1), a!=0: L'=L/a, J'=a*J, with
  (t',x',y')=(a*t,a^2*x,y). The parameter determinant is a^3.
* T=[[1,0],[z,1]]: L'=L, J'=J+z+L*z^2, with
  (t',x',y')=(t,x+z^2*y+L^3*z^4*t,y). The parameter determinant is one.
* T=[[1,z],[0,1]]: L'=L+z+J*z^2, J'=J, with
  t'=t,
  x'=x+(J^3*z^2+J^2*z)*t,
  y'=y+z^2*x+(J^2*L*z^2+J*z^2+z)*t.
  The parameter determinant is one.

In each case A(G)M_LJ(t,x,y)A(H)^t=M_(L',J')(t',x',y').
If L=0, the lower generator with z=J gives (0,0), hence V.
If L!=0, the diagonal generator with a=L gives (1,L*J). The lower
generator then realizes every AS shift c -> c+z^2+z. Finally (1,0)
becomes (0,0) under the upper generator with z=1. This proves sufficiency
of the invariant [L*J] and gives representatives M_(1,c) for all [c].

Necessity is already supplied by the arbitrary-field scalar AS invariant:
q_U has coefficients (L^2,J^2), so its class is [(L*J)^2]=[L*J]. Any
permitted equivalence acts by a scalar and invertible parameter substitution;
polar normalization gives the weighted action. Optional transpose cannot
identify distinct forms in the chosen right-kernel orientation, and preserves
the intrinsic quadratic invariant in any event. Hence the V forms over
arbitrary K are exactly K/AS(K).

## 4. Exhaustion and evidence limits

The pinned geometric classification has precisely P,N,V. The section common
kernel dimensions and evaluation/eta types descend over K by the linear
kernel equations and the invariant conic. Thus PR241's P theorem and the
preceding N/V arguments give the full classification over every
characteristic-two field. No new geometric orbit search or finite census is
required. The perfect/finite-field conclusions of PR241 remain valid, with
unchanged evidence status.

The N rank-transfer argument, the primitive quadratic parametrization and
the geometric exhaustion are written arguments. The verifier checks the
N restricted coefficients and forced-root identity, kernel/column covariance,
root-free V section normalization, the displayed whole-family stabilizers,
their parameter determinants and the scalar AS invariant. Mutation controls
reject missing terms, wrong transpose/square/scaling conventions and damaged
source pins. No new finite census is claimed. The exact-five finite-field
corollary from PR241 is unchanged: AS(K) has index two over every finite
characteristic-two field.

Direct author audit found no blocking gap within this scope. The proof is
not independently reviewed or formalized. Compatible three-leg tensor maps,
historical priority and a smaller matrix-multiplication exponent remain
outside this result.
