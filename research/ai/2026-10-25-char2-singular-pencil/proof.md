# Singular characteristic-two pencils have a common kernel

October 25, 2026. Claim `AI-CHAR2-SINGULAR-PENCIL-KERNEL-001` is
**proof-written-unreviewed**. Same-session algebra checks and a finite
census support the argument but are not independent review or formalization.

## Statement and consequence

Let K be any field of characteristic two, including finite and nonperfect
fields. Let U=span_K(A,B) be a two-dimensional space of 3-by-3 coefficient
matrices. Assume the literal polynomial identities

    D(sA+tB)=0, T4(sA+tB)=0 in K[s,t],

where D is the coefficient determinant and T4 is the pinned integer quartic
reduced in characteristic two. Then U has a nonzero common right kernel
or a nonzero common left kernel, defined over K itself.

Consequently every three-dimensional characteristic-two family for the
complete quadratic source with geometric source rank at most fourteen and
D not identically zero has a common right or left coefficient kernel in
its intrinsic section U=ker(e), e=M11. This conclusion uses the previously
proved integral-linear-form lemma. It rules out a singular two-section
without either common kernel. It does not classify the remaining kernel
cases, ground-field forms or compatible tensor maps. No exponent improvement
or historical priority is claimed.

The identities are polynomial conditions, not just conditions at K-rational
points. Section 6 gives an explicit GF2 counterexample to the pointwise
replacement. No arbitrary GL3 change is applied to the source or quartic.

## 1. Literal adjugate identities

For N a 3-by-3 matrix and z a three-vector, put

    S(N)=N11^2+N10*N12+N01*N21+N00*N22,
    Q(z)=z1^2+z0*z2.

The pinned sharp-three package proves in characteristic two that

    S(adj(M))=T4(M)+e(M)*D(M),
    S(u*v^t)=Q(u)*Q(v).

Both identities are rechecked here in the original coordinates. For the
second, expansion gives u1^2*v1^2+u1^2*v0*v2+u0*u2*v1^2+u0*u2*v0*v2,
which is exactly Q(u)Q(v). Thus S(adj(sA+tB)) is the zero polynomial.

## 2. Generic rank at most one

If sA+tB has rank at most one over K(s,t), all its two-minors vanish
identically. In particular A, B and A+B have rank at most one. Since A,B
are independent they are nonzero, so write A=u*v^t and B=x*y^t over K.
If both pairs u,x and v,y were independent, the product
[u x]*[v y]^t would have rank two. This product is A+B, a contradiction.
Thus either u,x are proportional, giving a common image line and a
nonzero common left kernel, or v,y are proportional, giving a nonzero
common right kernel. All these spaces and vectors are defined over K.

## 3. Homogeneous rank-one adjugate factorization

It remains to handle generic rank two. Work in the UFD R=K[s,t]. The
nonzero matrix X=adj(sA+tB) has rank one over Frac(R), and its nonzero
entries are homogeneous of degree two. Factor it as

    X=gamma*u*v^t,

where gamma is a nonzero homogeneous polynomial and u,v are primitive
homogeneous polynomial vectors. Here primitive means their entries have
gcd one, not that they generate the unit ideal.

For completeness, choose a nonzero column and divide it by the homogeneous
gcd of its entries to obtain primitive u. Every other column is a rational
multiple (p/q)u. Taking p,q relatively prime in R, polynomiality forces q
to divide every entry of u, so q is a unit. The column multipliers therefore
form a polynomial row. Divide that row by its homogeneous gcd gamma to
obtain primitive v. Since all original nonzero columns have degree two,
the nonzero entries in each factor have a common homogeneous degree.

Write r=deg(u), h=deg(v), d=deg(gamma). These nonnegative integers satisfy
r+h+d=2. The adjugate identities M*X=X*M=0 imply M*u=0 and v^t*M=0:
use a nonzero component of each opposite factor and the fact that R is a
domain. If r=0, u is a nonzero constant vector and coefficient comparison
gives A*u=B*u=0. If h=0, v gives a common left kernel over K.

Suppose instead that neither common kernel exists. Then r,h>=1, hence
r=h=1 and d=0. The two literal identities in Section 1 give

    0=S(X)=gamma^2*Q(u)*Q(v).

Because R is a domain, Q(u)=0 or Q(v)=0 as a polynomial. Section 4 shows
that neither can vanish for a primitive homogeneous degree-one vector.

## 4. A primitive linear vector cannot lie on the evaluation conic

Let u=s*a+t*b, with a,b in K^3, and suppose Q(u)=0. Its coefficients give

    qa=Q(a)=0, qb=Q(b)=0, C=a0*b2+a2*b0=0.

Put p01=a0*b1+a1*b0 and p12=a1*b2+a2*b1. Direct characteristic-two
expansion gives the two Plucker-coordinate identities

    p01^2=a0*b0*C+a0^2*qb+b0^2*qa,
    p12^2=a2*b2*C+a2^2*qb+b2^2*qa.

Thus p01^2=p12^2=0. A field has no nonzero nilpotents, so p01=p12=0;
the remaining two-by-two minor is C=0. All minors of [a b] vanish,
which makes a,b proportional over K. There is therefore a nonzero
constant vector c and a nonzero homogeneous linear form L(s,t) with
u=L*c. All nonzero entries share L, contradicting primitivity.
The same argument applies to v. This completes the proof of the lemma.
No square root, algebraic closure or normal-form descent is needed.

## 5. Application to characteristic-two attaining three-spaces

For a family W as in the statement, the pinned integral-linear-form lemma
gives a K-linear ell with

    T4=D*ell, D=e*(A2+e*ell+ell^2).

Since D is a nonzero polynomial, e is a nonzero linear form on W.
Its kernel U consequently has dimension two. Restricting the displayed
identities gives D|U=T4|U=0. The pencil lemma supplies a common right
or left kernel of U over K. This is a kernel of the singular section,
not a common kernel of all W: W includes coefficient-invertible matrices.

Over an algebraic closure, the pinned permitted binary action has the
three kernel-vector orbit representatives e0=(1,0,0), eta=(0,1,0) and
e0+eta. Optional transposition interchanges left and right. The published
evaluation-kernel classification already treats the e0 case. This lemma
reduces the remaining geometric classification to the eta and e0+eta
cases; it does not prove that those cases are exhausted by known examples.
Over arbitrary ground fields we assert the common kernel, not descent
of all orbit normalizations or a classification of forms.

## 6. Finite evidence and the pointwise trap

The accompanying exhaustive GF2 census visits every two-dimensional
coefficient space once: its three nonzero matrices have unique increasing
bit encodings a<b<a XOR b. There are 43,435 such spaces. Exactly 8,575
have polynomial D=0, and 3,623 also have polynomial T4=0; 98 of the latter
have generic rank at most one. All coefficients are checked using exact
GF2 polynomial multiplication, not just evaluations. Common right/left
kernel dimensions among the 3,623 qualifying spaces are

    (1,2):49, (2,1):49, (1,1):957, (0,1):1284, (1,0):1284.

There are no cases with both common kernels zero. This finite census is
supporting evidence only; Sections 1-4 prove the arbitrary-field result.

The polynomial hypothesis cannot be replaced by GF2 pointwise vanishing.
Take the pencil

    M(s,t)=[[0,s+t,0],[s,0,t],[0,t,0]].

It has D=0 and T4=s*t^2*(s+t). The quartic vanishes at all three GF2
projective points but is not the zero polynomial. Both common kernels
are zero: coefficient comparison in M*u=0 and M^t*v=0 forces all three
coordinates of the respective constant vector to vanish. Its adjugate
factors into two moving linear kernel vectors,

    adj(M)=(t,0,s)^t*(t,0,s+t),

and Q(t,0,s)Q(t,0,s+t)=s*t^2*(s+t), agreeing with the obstruction in
the proof. This is a counterexample only to the weaker pointwise statement,
not to the lemma. The exact report and tests preserve it.

## Attribution and limits

Source and quartic conventions, the adjugate identity, integral linear
form, kernel orbits and prior classification retain their original package
attribution and exact pins. The new contribution is the primitive-adjugate
degree argument, its ground-field Plucker proof, the section-kernel
consequence and the explicit pointwise counterexample. Discovery initially
assumed algebraic closure; the factorization and coefficient proof remove
that unnecessary assumption. Same-session auditing and exact computation
are not independent review. Complete characteristic-two attainer
classification, compatible tensor maps and exponent improvement remain open.
