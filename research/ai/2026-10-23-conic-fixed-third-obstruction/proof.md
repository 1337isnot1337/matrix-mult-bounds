# The prescribed conic third jet is obstructed off the linear components

October 23, 2026. Claim `AI-CONIC-FIXED-THIRD-OBSTRUCTION-001` is
written and unreviewed. Owner-directed Codex work; no independent
mathematical review or formalization is claimed.

## Exact statement and fixed data

Fix the complete mixed-family witness of
[PR107](https://github.com/1337isnot1337/matrix-mult-bounds/pull/107),
at commit `86b514225414662933f88c6ed8270250b40a287d` and the byte hash
in `sources.json`. For every complex a,b,d with d nonzero, put c=-d^3
and Delta=(a+d^3)(b-d^3). The following are equivalent:

1. Its prescribed B0,...,B3, C0,...,C3 and Y1,Y2,Y3 extend to an
   incidence jet of order four.
2. The same complete third jet extends to an all-order formal curve.
3. It extends to a polynomial curve.
4. Delta=0.

On either component in (4), the exact curve is linear:
B(t)=B0+tB1 and C(t)=C0+tC1, with fixed kernel. Off these components,
the fourth coefficient equations are inconsistent even when every
entry of B4, C4 and Y4 is free.

This fixes the third coefficient, including its sixteen-entry kernel
correction. The preceding fixed-two construction preserves the earlier
coefficients and chooses a different third coefficient; its all-order
existence result on the full d-nonzero chart is unchanged. This theorem
concerns rank-twelve incidence of two fourteen-row maps. It does not
construct or exclude every full matrix target or imply an exponent bound.

## Literal source and fourth coefficient equation

Write iota(i,j,z)=28i+7j+z. The canonical source has all 4096
coefficient-one terms

    (iota(i,s,6-p-q), iota(p,j,6-r-s), iota(r,q,6-i-j)),
    i,j,p,q,r,s in {0,1,2,3}.

Let A0 be the twelve first-source coordinates iota(i,s,z) with
i,s in {1,2} and z in {0,3,6}; let K be its 100-coordinate complement.
For the prescribed coefficients set

    Fk = sum_{i+j=k} T(-,Bi,Cj),       Wk=Fk[A0,:].

Every Fk is a 112-by-196 matrix, with output column 14*r+s corresponding
to B output row r and C output row s. A source-row correction Yk is
a 100-by-12 matrix in the fixed graph chart over A0. The prescribed
Y1 and Y2 are zero. Consequently the equation for unknown fourth
coefficients X=B4, Z=C4 and H=Y4 is

    T(-,X,C0)[K,:] + T(-,B0,Z)[K,:] - H W0 + S4 = 0,       (1)
    S4 = (T(-,B1,C3)+T(-,B2,C2)+T(-,B3,C1))[K,:] - Y3 W1.

The unit leading minors are 1,1,-1. Thus this graph chart describes
the required rank-twelve incidence formally, and no additional
parameter guard occurs. Equation (1) allows all 4,336 unknown entries.

## A 28-entry literal-source functional

All output indices below start at zero. For a 14-by-14 matrix M define

    P(M)=d^3*(M[1,5]-M[1,1]-M[5,1])+M[1,7]-M[1,3]-M[5,3],
    Q(M)=P(M)+d^3*M[5,5]+M[5,7].

For a flattened source contraction F, write F_z for its 14-by-14
output matrix in first coordinate iota(1,1,z), and put

    Lambda1(F)=d^3*P(F_1)+Q(F_4),
    Lambda2(F)=d^3*P(F_2)+Q(F_5),
    L(F)=d*Lambda1(F)-Lambda2(F).                         (2)

The functional has 28 nonzero entries, with coefficients only signed
powers of d. Its complete sparse coordinates are exported in
`results/conic-fixed-third-obstruction-2026-10-23/dual-and-linear-branches.json`.
It evaluates only rows in K, so (2) also applies to (1).

We prove that L kills every unknown in (1). The short verification
uses the credited paired-row polynomial cores only to explain the
identity. The acceptance program checks all original source variables
directly and assumes no structure on X or Z.

In the seven-row cores the relevant constant rows are

    u0=(0,-x^3,0,1),            u2=(0,d^3,0,-1),
    v0=(0,0,x^3,-1),            v1=(x^3,-1,0,0),
    v2=(1,0,-a+d^3,-1),         v3=(0,-1,a*d^3,0).

Each first coordinate iota(1,1,z) reads coefficient x^(6-z) in the
core product, using the odd output rows. For arbitrary X, only its
entries paired with the constant C0 support can contribute to (2).
They give arbitrary four-component polynomials of degree at most three
in each selected B output row. The same statement holds for arbitrary
Z against B0. All other entries of X or Z have zero coefficient in L.

Set k(x)=d^3*v0+v1 and k0=d^3*v2+v3. Then

    k0=(d^3,-1,d^6,-d^3),
    k0-k(x)=(d^3-x^3)*(1,0,d^3,0),
    u0+u2=(d^3-x^3)*(0,1,0,0).

For either linear variation X*C0 or B0*Z these identities imply

    Q(variation)=(d^3-x^3)*h(x),     deg(h)<=3,
    deg(P(variation)-Q(variation))<=3.

For the B variation, the last difference is minus its second selected
row multiplied by k0; for the C variation it is minus u2 multiplied
by d^3 times its third selected row plus its fourth selected row.
Hence the coefficients satisfy

    d^3*[x^5]P+[x^2]Q=0,
    d^3*[x^4]P+[x]Q=0.

Both Lambda1 and Lambda2 therefore kill every entry of X and Z.
Moreover P and Q vanish identically on U0(x)V0(x)^T: the expression
for Q contains the pairing (0,1,0,0)*(1,0,d^3,0)^T=0, and the remaining
P-Q term is -u2*k0^T=0. They thus kill all twelve rows of W0. This
also proves L(H W0)=0 for every 100-by-12 matrix H.

## Exact value on the known fourth coefficient

Put alpha=a+d^3 and beta=b-d^3, so Delta=alpha*beta. The compact
first and second core coefficients of the pinned prescribed jet are

    U1=(x^2+d*x)*A*u^T+d^2*Delta*A*f^T,
    V1=-(x^2+d*x)*D*v^T,
    U2=-(2*Delta/3)*x*A*u^T+H2*f^T,
    V2=-(Delta/3)*x*D*v^T,

where

    u=(a,a*d^3,1,d^3)^T,        v=(-b,1,-b*d^3,d^3)^T,
    f=(0,1,0,0)^T,
    A=(-1,b,0,0,-d^3,0,-b*d^3)^T,
    D=(1,a,0,0,0,-d^3,-a*d^3)^T,
    H2=(-Delta^2*(b-2*d^3)/(3*d^2),
        -d*Delta^2*(b+d^3)/3,
         Delta^2*(b-d^3)/(3*d^2),0,0,b*d*Delta^2/3,0)^T.

The third cores have the form U3=(x^2+d*x)*J and
V3=(x^2+d*x)*N for fixed seven-by-four matrices J,N. This is an
entrywise identity of the pinned witness, with no condition on a or b.
For any product (x^2+d*x)^2*M+(x^2+d*x)*N0, applying L gives
d^3*(Q(M)-P(M)). In U1*V3^T, the selected third row of A is zero.
In U3*V1^T, the third and fourth selected rows of D are zero. Thus

    L(T(-,B1,C3))=L(T(-,B3,C1))=0.                         (3)

The sixteen entries of Y3, with q=a*Delta^2*(b-d^3)/(3*d^2), are
four copies of the following assignments, one for each i,s in {1,2}:

    Y3[iota(i,s,1), iota(i,s,0)] = 2*q,
    Y3[iota(i,s,2), iota(i,s,0)] = 2*d*q,
    Y3[iota(i,s,4), iota(i,s,3)] = q,
    Y3[iota(i,s,5), iota(i,s,3)] = d*q.

Here the row and column labels mean their positions in K and A0.
These paired rows imply L(Y3*W1)=0 for every W1.

Finally u^T*v=-Delta and f^T*v=1 give

    U2*V2^T=-(2*Delta^3/9)*x^2*A*D^T-(Delta/3)*x*H2*D^T.

The functional Q evaluates to alpha on A*D^T and to
-d*Delta^2*alpha/3 on H2*D^T. Therefore

    L(S4)=-d*Delta^3*alpha/3
         =-d*(a+d^3)^4*(b-d^3)^3/3.                      (4)

Applying L to (1) forces (4) to vanish. Since d is nonzero and the
field is C, this is equivalent to alpha*beta=Delta=0. This proves
the necessary condition at order four, hence for every formal or
polynomial extension. No finite sampling or solver completeness is used.

## Sufficiency on the entire exceptional locus

On either a=-d^3 or b=d^3, direct substitution in the complete pinned
witness gives B2=C2=B3=C3=0 and Y1=Y2=Y3=0. Thus the proposed linear
maps preserve every entry of the input third jet on both components.

For completeness their exact identity follows from the constant-core
relations

    U0(x)*v=(x^3-d^3)*A,       V0(x)*u=(x^3-d^3)*D.

At Delta=0 the first coefficients reduce to
U1=(x^2+d*x)*A*u^T and V1=-(x^2+d*x)*D*v^T.
Their cross terms cancel, and U1*V1^T is zero because u^T*v=0.
Consequently (U0+tU1)(V0+tV1)^T=U0*V0^T identically.
The literal source contraction has the fixed kernel K at all orders.
The unchanged leading unit minors give formal ranks 14,14,12.
This covers the intersection of the two components as well.

## Acceptance and scope

The standard-library `verify.py` reads the complete source-pinned
third jet with a bounded arithmetic-only Laurent parser. It rebuilds
all 4096 source terms and checks the original incidence equations
through order three, all three unit minors, every one of the 3136
map and 1200 kernel adjoint coefficients, the separate terms in (3)-(4),
and both full linear branches through all their possible product orders.
No constructor, predecessor contraction helper or tangent solver is imported.

A separate Fraction-only contraction at (a,b,d)=(1,2,1) obtains
-16/3, both with zero fourth coefficients and after inserting supplied
nonzero fourth map and kernel coefficients. This is a control of the
literal conventions; the universal polynomial identities prove the theorem.

The d=0 fiber is outside PR107's prescribed mixed chart. Other choices
of the third coefficient, including the preceding fixed-two all-order
construction, are outside this obstruction. Full repository regression,
historical replay and current-head hosted CI remain integration gates.
Computational replay does not provide independent mathematical review.
