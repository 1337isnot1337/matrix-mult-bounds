# Complete perfect-field characteristic-two attainer classification

October 25, 2026. Claims `AI-CHAR2-P-FORMS-001` and
`AI-CHAR2-PERFECT-ATTAINERS-001` are **proof-written-unreviewed**.
Exact identities and direct author self-audit support the proof; they are
not independent mathematical review or formalization. Parent PR240 is
merged at 7939f058c77e3bdd90f0ea67cbb81d8ee2f61b3c; its source and
discovery records are pinned in sources.json.

## Statements

1. Over every characteristic-two field K, all K-forms of the geometric P
orbit are classified by K/AS(K), with representatives P_c from PR240.
2. Over every perfect characteristic-two K, the geometric N orbit has one
K-form. Combining this with (1) and PR240's moving-eta classification gives
all attainer classes as the disjoint union

    (K/AS(K))_P  disjoint-union {N} disjoint-union (K/AS(K))_V.

In particular every finite field of characteristic two has exactly
five classes. The algebraically closed case recovers exactly three.
Nonperfect N/V forms remain outside the second statement.

Let W be a three-dimensional subspace of Mat_3(K). Use the literal complete
quadratic source, with lexicographic pair orders and out-of-range entries zero,

    R(M)[(j,L),(H,r)] = M[H-j,L-r], 0<=j,r<=2, 0<=L,H<=4.

An attainer has D=det(M) not identically zero on W and det(R(M)) identically
zero as a polynomial on W. The latter is geometric source rank at most14,
not merely a test at K-rational points. The pinned sharp-cap theorem proves
that three is the maximum dimension in characteristic two.
Equivalence is equality of subspaces after M -> A(G) M A(H)^t and optional
transpose, where G,H are invertible two-by-two matrices over K and

    A([[a,b],[c,d]])=[[a^2,a*c,c^2],[0,a*d+b*c,0],[b^2,b*d,d^2]].

Linear parameter changes only reparametrize the same subspace. The integral
lemma gives a nonzero linear e=M11, a unique linear ell, and identities
T4=D*ell and D=e*(A2+e*ell+ell^2), with A2=M01*M21+M10*M12.
The integer quartic T4 is pinned in the determinant package and explicitly
reconstructed by verify.py. Define the intrinsic singular two-section
U=ker(e|W). The actions scale e by delta=det(G)det(H), and D by delta^3.
Consequently q_U=(D/e)|U transforms by a nonzero scalar and invertible
parameter substitution. Common section kernels transform by A^-t.
Their dimensions, the evaluation conic Q(u)=u1^2+u0*u2=0, and the fixed
eta line (0,1,0) are intrinsic. PR239 gives precisely the three geometric
orbits P,N,V. PR240 supplies the representatives

    P_c(t,x,y)=[[c*t+x+y,t+y,t],[c*t,t,t],
                 [c^2*t+(c+1)*x+y,c*t+(c+1)*y+x,c*t]],
    N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]],
    M_LJ(t,x,y)=[[x,J^2*t,J^3*t],[y,t,x+(L*J^2+J)*t],
                  [L^3*t,L^2*t,y+(L+L^2*J)*t]].

Here V=M_00, the split P representative is equivalent to P_0, and the V
representative of [c] over a perfect field is M_(1,sqrt(c)). AS(K) denotes
the additive subgroup {z^2+z:z in K}. Sections1-4 prove the first claim
without a perfection hypothesis; Sections5-6 prove the second over perfect K.

## 1. Orient and normalize the P orbit over K

Suppose W becomes P over the algebraic closure. The common section kernels
are solution spaces of linear equations over K, and their dimensions are
unchanged by extension. After optional transpose the right kernel is an
evaluation line and the left kernel is the fixed eta line. Their dimensions
are both one. The right line has a nonzero K-vector on Q(u)=u1^2+u0*u2=0.
It normalizes to e0 over K without square roots: if u0!=0, write its line
as (1,r,r^2) and use h=[[1,0],[r,1]], for which A(h)^t*e0=(1,r,r^2)^t; otherwise it is e2
and the binary swap applies.

The first column is now e*v for a nonzero vector v in K^3. Its middle
coordinate v1 cannot vanish. If it vanished, over the algebraic closure v
would be a square binary quadratic, and the pinned square first-column
chart would put W in the geometric N orbit, a contradiction.
A right binary diag(s,1) multiplies v by s, so choose s=1/v1.
Now v=(a,1,d). Under a left binary G its ratio to the new e is
A(G)v/det(G). If a!=0, G=diag(1/a,1) sends it to (1,1,a*d).
If a=0,d!=0, first swap the outer coordinates. If a=d=0, the shear
G=[[1,0],[1,1]] sends eta to (1,1,0). Thus over K, without perfection,
we normalize the first column to t*(1,1,c), with t=e.

Because eta is the common left kernel on U, the middle row on U vanishes.
The family has shape

    M=[[t,b,d],[t,t,F*t],[c*t,h,i]],

where F,c are scalars and b,d,h,i are linear forms.

## 2. Why t,b,h are independent

This step must not be silently assumed. Over the algebraic closure W is
equivalent to the known P chart

    M0(t,b,h)=[[0,b,0],[t,t,0],[0,h,h]],

whose restricted middle column has image dimension two. Both right kernels
are e0 and left kernels eta. An equivalence in this orientation cannot use
transpose: it would put eta on the right and an evaluation line on the left,
and binary actions preserve both types. In a left-right equivalence the
right binary H=[[a,b],[c,d]] must preserve the e0 kernel line under A(H)^(-t),
which forces c=0. Then right multiplication scales the middle column by
ad; left multiplication is invertible and preserves its rank. Parameter
changes also preserve the rank of the middle-column map on U. Therefore
b|U,h|U are independent over the closure, hence already over K. So t,b,h
are coordinates on W.

## 3. Exhaust all coefficients in the normalized chart

Put delta=b*i+d*h on U; it is a nonzero polynomial because the section
has generic rank two. Literal invariant expansion gives

    (D/t)|U=delta,
    (T4/t)|U=(h+c*b)*delta.

The integral identity T4=D*ell implies ell|U=h+c*b. The other integral
identity D=t*(A2+t*ell+ell^2), restricted after division by t, gives

    b*i+d*h+b*h+(h+c*b)^2=0 on U.

Comparing b^2,b*h,h^2, every family therefore has the form

    d=r*b+h+k*t,
    i=c^2*b+(r+1)*h+u*t,
    ell=c*b+h+v*t,

for scalars r,k,u,v. Define Q=D/t+A2+t*ell+ell^2 and
C=T4/t+(D/t)*ell. The coefficients of Q are exactly

    [b*t]: F*c+c^2+c*r+c+u,
    [h*t]: F+c+k+r,
    [t^2]: F+c*k+u+v^2+v.

Thus u=c^2+c*F+c*r+c, k=F+c+r, and F=c+v^2+v.
After these substitutions, the b*h*t coefficient of C is

    c^2+r^2+v^2=(c+r+v)^2.

Hence v=c+r over any field. All remaining coefficients vanish identically.
The complete normalized family is

    B_(c,r)=[
      [t,   b, r*b+h+(c^2+c+r^2)*t],
      [t,   t, (c^2+r^2+r)*t],
      [c*t, h, c^2*b+(r+1)*h+(c^3+c^2+c*r^2+c)*t]],
    ell=c*b+h+(c+r)*t.

No division by c,r or their products occurs. All zero and exceptional
values are included. The checker verifies the pre-normalization restrictions,
all full residuals, and the exact normalizations below.

## 4. Remove r and classify c

Right multiplication by A([[1,s],[0,1]])^t sends B_(c,r) to B_(c,r+s).
Taking s=r+c gives B_(c,c). Directly,

    B_(c,c)(t,b,h) = P_c(t,x,y) A([[0,1],[1,0]])^t,
    x=h+(c+1)*b+t, y=b+t.

The parameter substitution is invertible over K. Thus every P-form is P_c.
There is also an explicit Artin-Schreier shift:

    A([[1,z],[0,1]]) B_(c,r)(t,b,h)
      = B_(c+z^2+z, r+z^2)(t,b,h+z^2*b+z*t).

This is verified as a polynomial matrix identity. Together with the right
shear, it proves sufficiency of equality of c modulo AS(K), without adjoining
roots or using Galois cohomology.

Necessity follows from the intrinsic determinant quadratic. For B_(c,r),

    q_U=c^2*b^2+b*h+h^2,

whose Artin-Schreier class is [c^2]=[c]. Any equivalence acts by a scalar and
invertible substitution; normalization of the nonzero polar coefficient
forces the weighted GL2 action. PR240's direct scalar identity
A'B'+AB=R^2+R holds over every characteristic-two field, with no perfection
hypothesis. It therefore preserves [c]. The same argument covers transpose.
This establishes the P classification over arbitrary K.

## 5. The N orbit over perfect fields

For a K-form of N, the unique common section kernel is an evaluation line,
defined over K by the linear kernel equations; orient it on the right and
normalize to e0 over K. Again the first column is e*v, v!=0. Its middle
coefficient is zero: a nonzero middle coefficient over the closure would
place it in the nonsingular first-column P chart instead of N.
Over perfect K, v=(a,0,c) is the coefficient vector of a square of a
K-linear form. A binary change defined over K sends it to a nonzero
multiple of e0. The additional right diagonal scaling from the evaluation
package makes the first column exactly t*e0. The pinned square-chart
classification is valid over K once this normalization exists, and supplies
an explicit shear to N. Thus N has only one K-form over perfect K.
This does not justify such a normalization over arbitrary nonperfect fields.

## 6. Exhaustion over perfect K and finite fields

The geometric classification gives exactly P,N,V after algebraic closure.
Their intrinsic section kernel dimensions and evaluation/eta types descend
through linear equations over K. They distinguish the three geometric types
and ensure the preceding normalized cases apply, after optional transpose.
Sections1-4 classify the P case. Section5 treats N. The V case is exactly
the moving-eta/no-left-kernel locus classified by PR240 over perfect K.
Thus the displayed disjoint union exhausts the perfect-field classes.

For GF(q), K/AS(K) has two elements, giving exactly five classes. P and V
each have split and nonsplit representatives, with respectively (q-1)^3
and (q-1)^2(q+1) invertible coefficient matrices; N has (q-1)^3. Distinct
kernel dimensions/types separate the geometric orbits. The AS invariant
separates the two forms in each of P and V.

## Discovery correction and evidence limits

An initial scratch substitution mistakenly used k=F+r+v. Its own Q residual
left (c+v)*h*t and therefore did not close the equations. Coefficient reading
corrects it to k=F+r+c. The original script and the correction are preserved;
only the corrected complete identities support this candidate. No PR240 file
was changed, and its published result does not rely on this follow-up.

The new checks reconstruct the pre-normalization restrictions, all chart
coefficients, the right shear, canonical P_c match, AS shift, kernel
normalizers, middle-column rank covariance, and the square-chart N shear.
Mutation controls reject the preserved wrong k substitution and damaged
transformations. These exact checks do not certify geometric exhaustion or
field descent by computer. The middle-column rank argument in Section2,
the field hypotheses in Section5 and the exhaustion in Section6 are written
mathematical arguments. Direct author self-audit found no blocking gap in
this scope, but supplies no independent review. Nonperfect N/V forms,
compatible tensor maps, formalization, historical priority and exponent
improvement remain outside these claims.
