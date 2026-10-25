# Ground-field forms of characteristic-two quadratic attainers

October 25, 2026. Claims `AI-CHAR2-PERFECT-ETA-FORMS-001` and
`AI-CHAR2-NONSPLIT-P-FORMS-001` are **proof-written-unreviewed**.
The arguments below are owner-directed AI research, checked in the generating
session. Exact controls are not independent review or formalization.

## Statements and source conventions

Use the complete quadratic source with lexicographic pair orders

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    j,r=0,1,2, L,H=0,...,4,

and zero outside the 3-by-3 coefficient range. A geometric attainer is a
three-dimensional linear coefficient family W with det R identically zero
and D=det M not identically zero. These are polynomial conditions, also over
finite fields. The pinned sharp cap makes three the maximal dimension in
characteristic two. Put e=M11 and U=W intersect {e=0}.

For G=[[a,b],[c,d]], the permitted binary coefficient action is

    A(G)=[[a^2,ac,c^2],[0,ad+bc,0],[b^2,bd,d^2]].

Permitted equivalence means M -> A(G) M A(H)^t, an invertible parameter
change, and optional transpose. For delta=det(G)det(H), e scales by delta
and D by delta^3; thus q_U=(D/e)|U is intrinsic up to nonzero scalar and
invertible parameter change. Common kernel vectors transform by the dual
action, which fixes the line eta=(0,1,0) and preserves the evaluation conic
Q(u)=u1^2+u0*u2=0. All imported statements are pinned in sources.json.

**Theorem A (perfect-field moving-eta forms).** Let K be a perfect field
of characteristic two. Among geometric attainers whose section U has common
right kernel K*eta and zero common left kernel, permitted equivalence classes
are in bijection with K/AS(K), where AS(K)={r^2+r:r in K}. A representative
of [c] is M_(1,sqrt(c)), where

    M_LJ(t,x,y)=[[x,J^2*t,J^3*t],
                [y,t,x+(L*J^2+J)*t],
                [L^3*t,L^2*t,y+(L+L^2*J)*t]].

For M_LJ the invariant is [L*J]; the zero class is V=M_00. Over GF(q),
q=2^m, there are exactly two such classes, with respectively (q-1)^3 and
(q-1)^2(q+1) coefficient-invertible matrices. Transposed families are covered
by swapping left and right.

**Theorem B (explicit forms of P).** Over every characteristic-two field K,
for every c in K the injective family

    P_c(t,x,y)=[
      [c*t+x+y,             t+y,             t],
      [c*t,                 t,               t],
      [c^2*t+(c+1)*x+y,     c*t+(c+1)*y+x,   c*t]]

is a geometric attainer, equivalent over a separable extension of degree
at most two to P(t,x,y)=[[x,x,0],[0,t,0],[0,y,y]]. If c is not in AS(K),
P_c is not equivalent to P over K. Consequently there are at least five
pairwise inequivalent attainers over GF2: P, P_1, the previously published
N=[[t,x,0],[0,t,x],[0,y,0]], V, and M_11.

Neither theorem classifies all P-forms, all attainers over GF2, or arbitrary
nonperfect-field forms. No compatible tensor map or exponent improvement
is asserted.

## 1. The moving section descends over a perfect field

The pinned geometric classification identifies the moving-eta geometric
orbit and supplies the homogeneous adjugate argument and extension equations.
Here we check exactly where its normalization requires field hypotheses.
In the stated locus U has generic rank two: a rank-one pencil has either
fixed image line or fixed row functional, and in either case its two
coefficient matrices have a nonzero common left kernel. Thus

    adj M=eta*v(x,y)^t, Q(v)=0

on U, with v a nonzero homogeneous quadratic vector. The pinned gcd argument
applies over K[x,y]: a gcd of degree two would give a fixed left kernel;
a gcd of degree one leaves a forbidden primitive linear vector on Q=0.
Therefore v is primitive quadratic.

Neither v0 nor v2 vanishes, and they are coprime. Unique factorization in
v1^2=v0*v2 gives v0=alpha*l0^2, v2=beta*l2^2, and
v1=r*l0*l2, with r^2=alpha*beta. Divide the vector by alpha and set
y=l0, x=(r/alpha)*l2. This normalizes its line to (y^2,xy,x^2) without
adjoining a root. The forms x,y are independent by primitivity.

The linear column syzygies are (x,y,0)^t and (0,x,y)^t. Thus the two outer
columns of the section are K(x,y)C, where

    K(x,y)=[[x,0],[y,x],[0,y]], C in GL2(K).

Here perfection is used: entrywise square roots give H in GL2(K) with
H^[2]=C^(-1). The permitted right action normalizes the section to
[[x,0,0],[y,0,x],[0,0,y]]. With t=e and two complement-coordinate shifts,
the pinned extension coefficient proof is entirely over K and gives exactly
the displayed M_LJ. It uses no division by L or J and therefore includes
all exceptional parameter values. Its determinant quadratic is

    q_U=L^2*x^2+x*y+J^2*y^2.

The integral identities T4=D*ell and D=e*(A2+e*ell+ell^2), with
A2=M01*M21+M10*M12 and ell=L*x+J*y+L^2*J^2*t, supply the converse.

## 2. Every weighted binary change is realizable

The pinned stabilizer identity is

    A(G)K(x,y)=K(a*x+c*y,b*x+d*y)*G^t.

For any G in GL2(K), perfection again gives H with H^[2]=(G^t)^(-1).
The resulting permitted pair preserves the normalized section. Its new
section parameters are z=G^t*(x,y)^t, and delta^2=det(G). Consequently

    q_U(z) -> det(G)*q_U((G^t)^(-1)z).               (1)

The coefficient of xy remains one: inverse substitution multiplies it by
1/det(G), and the action scalar cancels that factor. After setting the new
e coordinate to t and absorbing the complement coordinates, the extension
is again M_(L',J'). Its quadratic coefficients determine L',J' uniquely
because squaring is bijective in K. The remaining extension coefficients
are forced. Thus every change (1) is an actual permitted equivalence of
families, not merely a necessary invariant.

Conversely, any equivalence between normalized families acts on q_U by a
scalar and invertible binary substitution. Both polar coefficients are one,
so the scalar is the reciprocal determinant of that substitution. Its
quadratic action therefore has form (1), whether or not it was constructed
using the displayed stabilizer. A single transpose cannot send a chosen
right-eta/no-left representative to another one: it changes kernel dimensions
from (1,0) to (0,1), and subsequent binary actions preserve those dimensions.
Multiple transposes reduce to this case or to an ordinary left-right action.

## 3. Classify the binary quadratics

Write q=A*x^2+x*y+B*y^2. If A=0, the determinant-one substitution
x -> x+B*y gives xy. If A!=0, use G=diag(A,1) in (1), obtaining

    q_c=x^2+x*y+c*y^2, c=A*B.

The determinant-one substitution x -> x+r*y sends c to c+r^2+r.
The form q_0=x(x+y) is equivalent to xy by another determinant-one
substitution. Hence equal classes of A*B in K/AS(K) give equivalent forms.

Necessity has a direct coefficient certificate. Set Delta=ad+bc. Formula
(1) has coefficients

    A'=(db+A*d^2+B*b^2)/Delta,
    B'=(ca+A*c^2+B*a^2)/Delta.

For r=(A*c*d+B*a*b+b*c)/Delta, expansion gives

    A'*B'+A*B=r^2+r.

The checker verifies the cleared polynomial identity modulo two. Thus the
AS class is invariant under every permitted equivalence, proving both
directions of Theorem A. For M_LJ this class is [L^2*J^2]=[L*J], and every
class occurs by taking L=1,J=sqrt(c).

## 4. Finite fields and determinant counts

Over GF(q), AS is F2-linear with kernel {0,1}, so its image has q/2 elements
and its quotient has exactly two classes. These coincide with absolute
trace zero and one. Indeed, the trace vanishes on r^2+r by telescoping;
its nonzero defining polynomial has degree 2^(m-1)<q, so it is a nonzero
function on GF(q). Its kernel therefore has q/2 elements, exactly AS(K).

The exact shift x -> x+L*J^2*t, y -> y+L*t sends D/e to q_U. For each
nonzero t it is an invertible translation of the (x,y) plane. In the split
case q_U is a nonzero scalar times a product of two independent linear
forms and has (q-1)^2 nonzero values. In the nonsplit case it has no
nonzero isotropic vector, so q^2-1 values are nonzero. Multiplying by the
q-1 nonzero choices of t gives (q-1)^3 and (q-1)^2(q+1).

The exact finite controls exhaust all normalized quadratics and weighted
GL2 actions over GF2, GF4, GF8: orbit sizes (3,1), (10,6), (36,28).
All 228696 action checks and 33824 family-matrix determinants agree. These
finite checks are supporting evidence; Sections1-3 prove the perfect-field
statement separately.

## 5. The nonsplit P construction

For P_c, read t from M11, y from M01+t, and x from M00+c*t+y, proving
injectivity. Exact polynomial calculation gives

    D=t*(x^2+x*y+c*y^2), ell=t+x+y,
    T4=D*ell, D=t*(A2+t*ell+ell^2).

The pinned literal source identity proves geometric rank at most fourteen.
On U the last column and middle row vanish, while the outer 2-by-2 block
has determinant x^2+xy+c*y^2. Thus its common right kernel is exactly K*e2
and its common left kernel exactly K*eta.

An explicit transformation establishes the geometric type and exact source
rank at every coefficient-invertible point. Adjoin a root lambda of
lambda^2+lambda+c=0; this needs a separable extension of degree at most two.
Set

    G=[[1,lambda],[1,lambda+1]], H=[[lambda,1],[1,0]],
    b=x+lambda*y, h=x+(lambda+1)*y,
    M0(t,b,h)=[[0,b,0],[t,t,0],[0,h,h]].

Both determinants and the parameter determinant are one. Modulo the root
relation, direct multiplication gives A(G)M0A(H)^t=P_c. The pinned explicit
shear identifies M0 with P. Source rank is invariant under these actions
and unchanged by field extension, so it is exactly fourteen when D!=0.

If c is not in AS(K), x^2+xy+c*y^2 has no K-projective root: y=0 forces
x=0, while y!=0 would make c=(x/y)^2+x/y. The original P has split section
quadratic xy. The intrinsic q_U invariant excludes an equivalence over K.
This proves Theorem B's general construction and inequivalence statement.

## 6. At least five GF2 attainers and evidence limits

P and P_1 have section kernel dimensions (1,1); they have respectively
one and three invertible GF2 coefficient matrices. N has dimensions (1,0)
with an evaluation kernel. V and M_11 have dimensions (1,0) with the
non-evaluation kernel eta, and respectively one and three invertible
matrices. The dimensions, conic type, and counts are preserved under the
permitted actions, with transpose merely swapping sides. These five are
therefore pairwise inequivalent. The checker independently builds all40
literal fifteen-by-fifteen GF2 source matrices. Every rank is at most14,
and every invertible-coefficient instance has rank14.

This is a lower bound of five, not an exhaustive GF2 census. Theorem A
exhausts only the specified moving-eta locus over perfect fields; Theorem B
does not exhaust P-forms. Nonperfect normalization, the remaining ground-field
forms and compatible tensor maps remain open. Earlier packages retain the
literal source, integral lemma, geometric classification, extension formulas,
representatives and stabilizer attribution. The new contributions are the
perfect-field descent, AS classification and scalar identity, finite counts,
and explicit P twist. No independent review, formalization, historical
priority, or matrix-multiplication exponent improvement is claimed.
