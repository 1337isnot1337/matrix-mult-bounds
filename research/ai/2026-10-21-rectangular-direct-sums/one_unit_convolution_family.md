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

## Stronger linear-span limitation

For a>=3, the linear span of this particular fixed-support family has
dimension a^2*b-a-b, which is622 at A(8,10). Every coefficient with k>=a
is zero. The k=a-1 coefficient is divisible by xz, and the k=a-2
coefficient has zero constant monomial. These give the upper bound
(a-2)ab+(ab-1)+(a-1)(b-1)=a^2*b-a-b. Products of individual B_r and D_s
span every monomial in the first a-2 coefficients. Choosing one top factor
and one next factor spans every nonconstant monomial at k=a-2. Choosing
only A,C and then subtracting its k=0 term gives every xz-divisible monomial
at k=a-1. Thus the bound is attained. The finite span verifier has622
independent coordinate directions over F2 and the same coordinate-support
upper bound. This is a stronger obstruction than the separate-factor
count: an injective1056-dimensional target leg cannot fit in this span.

## Moving the single long-support point does not evade linearity

Identify each length17 long coefficient sequence with a homogeneous binary
form of degree16, using the standard nonzero binomial rescaling if needed
for the source SL2 convention. Support in k<8 means divisibility by a
fixed ninth power of a linear form. A long-factor GL2 transformation moves
that point and preserves the property that all coefficient forms have a
common root of multiplicity at least9.

Let Z be the cone of vector-valued degree16 binary forms having such a
common root. Each nonzero member has a unique such point, since18>16.
Every projective line contained in Z has one fixed point. To see this,
choose a scalar component of its pencil. If the two endpoint polynomials
are nonproportional, any moving multiple root belongs to the finite zero
set of their nonzero Wronskian f'g-fg', with infinity included. One point
therefore occurs for infinitely many pencil parameters. Vanishing of all
derivatives through order8, in every component, is linear in the pencil
parameter, so both endpoints have that same common root. If the chosen
scalar components are proportional, their unique high-multiplicity root
is already fixed, and the other components obey the same vanishing.

Now suppose a linear target-leg map sent every rank-at-most-two matrix
parameter into Z. Any two rank-one parameters span a line of rank at most
two. Their nonzero images must therefore share the unique point. Since
rank-one matrices span the entire parameter space, the whole leg image
has one fixed ninth-power divisor. That coefficient space has dimension
8*80=640, below1056. Thus even the union of all long-GL2 translates of
this single-fat-point construction cannot supply that target-leg map.
This does not exclude multiple long-support points or general slices.
