# A universal invertible quadratic three-plane

October25, 2026. Claim `AI-QUADRATIC-UNIVERSAL-THREE-PLANE-001` is
**proof-written-unreviewed**. Same-session derivation, algebra audit and exact
certificates are not independent review or formalization. No historical
priority, compatible tensor map or exponent improvement is claimed.

## Statement and literal source

Over every field K, the coefficient matrices

    M(x,y,z)=[[x,x,0],[0,y,0],[0,z,z]]

form a three-dimensional K-linear space with geometric source rank at most
fourteen. Its coefficient determinant is xyz. At every point with xyz!=0,
its source rank is exactly fourteen. Thus the family contains an invertible
coefficient point and an exact-rank-fourteen source point over every ground
field, including Q and F2, without adjoining roots or extending that field.

Use exactly the full fifteen-by-fifteen source convention of the pinned
quadratic determinant package:

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    0<=j,r<=2, 0<=L,H<=4,

with out-of-range entries zero and both pair orders lexicographic. All
source endpoints are retained. The three coefficient entries M00,M11,M22
are x,y,z, respectively, proving independence in every characteristic.
Direct coefficient expansion gives detM=xyz.

## Integral kernel and rank certificate

With zero-based source column indices 0,...,14, define v by

    v2=-y*z^2, v4=v5=x*z^2,
    v9=v10=-x^2*z, v12=x^2*y,

and all other coordinates zero. Direct multiplication in Z[x,y,z] gives
R(M)v=0. Since v12=x^2*y has coefficient one, v is nonzero over the
fraction field K(x,y,z) for every K. Thus detR=0 in that fraction field
and therefore as a polynomial in K[x,y,z]. This proves the geometric rank
cap, including parameters where v itself specializes to zero; it is not
an inference from finitely many points.

Delete row (j,L)=(2,4) and column (H,r)=(4,0), zero-based indices14 and12,
retaining the natural order on all other rows and columns. Exact determinant
expansion over Z[x,y,z] gives

    det R_minor=-x^6*y^3*z^5.

The maintained verifier constructs this literal minor and computes the
identity directly. Consequently it is nonzero whenever xyz!=0 over any
field, so rankR=14 at every invertible coefficient point of the family.
At x=y=z=1 the integer minor is -1; the full14-by-14 integer matrix is
exported in the report and reconstructed by a separate pair-indexed test.
A unit minor has no exceptional residue characteristic.

The original scratch elimination used a different row order and obtained
+1 for the same deleted pair. The seven row-order inversions change its
sign to the -1 used here. No reduction modulo two is used to certify other
characteristics.

## Integer invariant cross-check and correction history

The determinant package supplies the integer identity detR=D*P12, where
D=detM, A2=2ai+2cg-bh-df for M=[[a,b,c],[d,e,f],[g,h,i]], T4 is its pinned
quartic, and

    P12=D^4+(eD+2T4)(eD*T4+T4^2-A2*D^2).

Here A2=xz, T4=0 and D=e*A2=xyz. Hence P12=D^4-e*A2*D^3=0. This corroborates
the direct kernel proof without division by the earlier normalization2048.
The exact source versions and scratch records are pinned in sources.json.

During discovery the first integer calculation omitted the2ai term in A2
and incorrectly asserted detR=2D^5, suggesting a characteristic-two-only
example. A separate same-session audit caught that mistake before
publication. The corrected integer A2=+xz makes the example universal.
A regression mutation deliberately omits2ai and must fail. The discovery
pilot's255 F2-defined two-planes through one point (16 passing as F2[t]
identities) led to the construction; that finite pilot is not a classification
of higher-dimensional families or fields.

## This particular three-plane has no larger linear extension

A strictly larger geometric rank-at-most-fourteen family containing W would
contain W+K B for some coefficient matrix B outside W. Write
B=[[a,b,c],[d,e0,f],[g,h,i]] and work with M(x,y,z)+tB. Since the coefficient
determinant D at t=0 is xyz, it is a nonzero polynomial. Differentiate the
pinned integral identity F=detR=D*P12 at t=0. Using T4=0 and D=e*A2 there,

    dotF=D^3*C,
    C=D*(dotD-A2*dote-e*dotA2)+(e^2-2*A2)*dotT4.

Direct differentiation gives

    dotD=yz*a-xz*d+xz*e0-xz*f+xy*i,
    dotA2=2z*a+2x*i-z*b-x*h,
    dotT4=xz^2*(a-b+c)+x^2*z*(i-h+g),

so

    C=c*x*y^2*z^2-(d+f)*x^2*y*z^2+g*x^2*y^2*z
      -2*(a-b+c)*x^2*z^3-2*(i-h+g)*x^3*z^2.

Every extension must make this polynomial zero. Its distinct monomials
force c=g=0 and d+f=0 in every characteristic. When two is invertible,
they also force a=b and i=h. After subtracting a member of W, B is then
w*(E21-E23), in one-based coefficient indexing. On the resulting candidate,
exact integer substitution gives

    detR([[x,x,0],[w*t,y,-w*t],[0,z,z]])
       =-t^2*w^2*x^4*y^5*z^4.

This cannot vanish identically unless w=0, a contradiction.

In characteristic two, the first-order equations leave, modulo W,
B=u*E12+v*E33+w*(E21-E23). Thus use the matrix

    [[x,x+u*t,0],[w*t,y,-w*t],[0,z,z+v*t]].

The pinned characteristic-two identity detR=D^2*G9, with
G9=D^3+e^2*D*T4+e*T4^2+e*A2*D^2, forces G9=0 in the polynomial domain,
since D has nonzero constant-in-t term xyz. Its t^2 coefficient is

    x^2*y*z^2*(u^2*z^2+u*w*y*z+v^2*x^2+v*w*x*y+w^2*y^2).

The distinct monomials x^2*y*z^4, x^4*y*z^2 and x^2*y^3*z^2 have
coefficients u^2,v^2,w^2. A field has no nonzero square-zero element,
so u=v=w=0. This again contradicts B outside W.

The argument survives scalar extension and proves inclusion maximality of
this specific three-plane in every characteristic. It does NOT exclude
four-dimensional families elsewhere. The exact verifier checks the integral
chain rule, complete coefficient differential, odd candidate determinant
and characteristic-two forcing coefficients. An initial same-session
extension calculation omitted the -xz*f term of dotD and therefore selected
the wrong fourth direction; root inspection corrected it before publication.
The regression includes the corrected differential explicitly.

## Consequence and remaining gap

The prior cap-four proofs cover all fields of characteristic different from
two, including characteristic zero, for geometric families containing an
invertible coefficient point. This construction raises their lower bound
to three over every such field, so the maximum dimension lies in [3,4].

In characteristic two the prior equality classification says that every
six-dimensional geometric rank-at-most-fourteen family consists entirely
of singular coefficient matrices. A hypothetical family of dimension at
least six containing an invertible point would contain a six-space through
that point after algebraic closure, contradicting that classification.
Thus the previously established upper bound on this stratum is five, and
the new lower bound gives [3,5] in characteristic two.

These intervals concern families containing invertible coefficient points.
Singular families of dimension six continue to exist. We exclude only extensions of this particular three-plane; we do not establish
a dimension-four example or exclude other four-spaces, and do not improve the
characteristic-two upper bound. One source block and its rank certificates
do not supply the compatible three-leg tensor maps needed for an exponent
improvement. All imported upper bounds remain written and unreviewed.
