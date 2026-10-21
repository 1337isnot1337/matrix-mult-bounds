# An explicit convolution family in the one-unit source stratum

October21,2026. Written proof, unreviewed. This constructs source slices,
not a matrix-multiplication restriction or a smaller exponent.

For2<=a<=b, choose polynomials

- A(z) of degree at most b-2 and C(x) of degree at most a-2;
- B_0(z),...,B_(a-2)(z), each of degree at most b-1;
- D_0(x),...,D_(a-2)(x), each of degree at most a-1.

Set B_(a-1)=z A and D_(a-1)=x C. Define the source sequence by

    f_k(x,z) = sum_(r=k)^(a-1) B_r(z) D_(a-1+k-r)(x)
                  + [k=0] A(z)C(x),      0<=k<a,
    f_k=0,                              a<=k<a+b-1.  (1)

These are valid source coefficients: x-degree<a and z-degree<b.
The image closure of this polynomial family has dimension

    ab+a^2-a-2.                                      (2)

Every slice in it has source rank at most a^2*b+1. On a nonempty open
set the scalar symbol rank is a, crossed rank is a+1, and source rank is
exactly a^2*b+1. In particular A(8,10) has a134-dimensional explicit
family of source slices of generic rank641.

## Full Hankel factorization

Use a+1 states indexed0,...,a. Set

    U_(p,0)= [p=0] A(z),
    U_(p,h)= B_(p+a-h)(z),  1<=h<=a,
    V_(0,q)= [q=0] C(x),
    V_(h,q)= D_(h-1+q)(x), 1<=h<=a,

where B_r,D_r outside0,...,a-1 vanish. In the product UV the h>=1
sum has indices r=p+a-h and s=h-1+q, with r+s=a-1+p+q.
All admissible r between p+q and a-1 occur. Therefore

    (UV)_(p,q)=f_(p+q)

for every p,q, not merely a selected submatrix. This is the complete
Hankel identity in the original source format.

The kernel pencils are fixed:

    c(z)=e_1-z e_0,       d(x)=e_a-x e_0,
    U c=0,               d^T V=0,       d^T c=xz.

For a>=2 the last equality holds because e_1 and e_a are distinct.
Its pairing is nonzero and separable. The top sequence coefficient is
f_(a-1)=xz A C, so when A C is nonzero the a-by-a anti-triangular Hankel
minor has nonzero determinant. Hence the scalar symbol has rank a.

At A=C=1, all B_r,D_r with r<a-1 zero, the slice is exactly
f_0=1, f_(a-1)=xz. Its crossed rank is a+1. Thus full crossed rank a+1
holds on a nonempty open set of the parameter space. The preceding
one-unit pairing criterion proves source rank a^2*b+1 on this open set.
Every larger source minor is a polynomial in the parameters and vanishes
there, so it vanishes on the entire parameter space. This proves the
rank upper bound for every member, including boundary specializations.

## Exact image dimension

The parameter space has dimension

    (ab-1)+(a^2-1)=ab+a^2-2.

Reverse the two coefficient lists:

    B_rev(t)=sum_(j=0)^(a-1) B_(a-1-j) t^j,
    D_rev(t)=sum_(j=0)^(a-1) D_(a-1-j) t^j.

Their product modulo t^a gives the convolution term in(1). The group of
units g(t) in C[t]/(t^a), of dimension a, acts by

    B_rev -> g B_rev,    D_rev -> g^-1 D_rev.

It scales A and C reciprocally, preserving A C, and preserves every degree
bound. Thus it leaves the source slice unchanged. When A is nonzero the
action is free: comparing successive coefficients of (g-1)B_rev=0 forces
g=1. Generic fibers therefore have dimension at least a, and the image
has dimension at most ab+a^2-a-2.

At the sparse point above, varying only the B-side parameters gives the
linear family

    f_0=A(z)+x B_0(z),
    f_k=x B_k(z) for1<=k<a-1,
    f_(a-1)=xz A(z),

of dimension ab-1. Varying only the D-side gives the corresponding
family with x,z exchanged and dimension a^2-1. Their intersection has
dimension a: A=C must be constant, and the a-1 remaining coefficients
are constant multiples of xz. Hence the differential image has dimension
ab+a^2-a-2. Differential rank is at most generic image dimension over C,
so this matches the upper bound and proves(2).

## Why this still falls short of the desired target

The family genuinely integrates a134-dimensional set of deformations;
it is not just the149-dimensional fixed-pencil tangent image computed
previously. It does not prove that the remaining fifteen tangent directions
are obstructed or that134 is a global maximum for the whole rank locus.

The two one-factor source families have dimensions79 and63 at A(8,10).
A rank-two parameter ruling of the desired M(32,33,33) target requires
64 or66 independent coordinates, depending on orientation. Thus simply
mapping its two factor variables into these two separate one-factor
spaces falls short on the63-dimensional side. More general parameter
maps or other parts of the slice locus remain open. No complete target
leg maps or source-to-target tensor identity are supplied.

The finite controls replay every Hankel coefficient, both kernel pencils,
the truncated-unit gauge, and the nonzero rank witnesses. Small cases
also reconstruct and rank the complete source matrix over the rationals.
The general argument remains written and unreviewed, with no historical
priority or exponent-improvement claim.
