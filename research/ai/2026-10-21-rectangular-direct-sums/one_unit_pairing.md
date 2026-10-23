# A factor criterion for the one-unit stratum

October21,2026. Written proof, unreviewed. No matrix target constructed.

Assume2<=a<=b, full scalar-symbol rank a and crossed coefficient rank a+1.
Choose a constant minimal rank factorization of the crossed matrix. It gives

    B_F(x,z) = U(z) V(x),

where U has size a-by-(a+1), V has size(a+1)-by-b, deg U<b and deg V<a.
Their stacked coefficient factors have full rank a+1. Then source rank
 a^2*b+1 is equivalent to the following conditions:

1. U and V have rational-function rank a.
2. The primitive right kernel c(z) of U and primitive left kernel d(x)^T
   of V both have polynomial degree one.
3. The nonzero biform g(x,z)=d(x)^T c(z) is separable: g=f(x)h(z).

This is a factor criterion within the specified symbol/crossed-rank
stratum. It does not classify which such products are Hankel, produce the
large target's maps, or settle crossed rank a.

## Necessity of the ranks and the first pencil

The preceding one-unit relation lemma gives the degree-one primitive
kernel c(z) of U: its columns are a basis of the inner polynomial span.
Since B has rank a, U has rank a and V has rank at least a. If V had
rank a+1 over C(x), it would map degree-below-a polynomial inputs in z
onto all(a+1)-component inputs of that degree. Multiplication by U would
then have rank a^2+1. This contradicts the forced inner coefficient rank
rho=a^2. Hence V has rank a. Let delta>=1 be the degree of its primitive
left kernel d(x). Constant independence rules out delta=0.

## Exact rank through the intermediate space

Factor the full source slice through the (a+1)*a*b coordinates (h,j,r):

    P[(j,p,L),(h,j',r)] = [j=j'] U_(L-r)[p,h],
    Q[(h,j,r),(H,q,r')] = [r=r'] V_(H-j)[h,q].

Then M=P Q. The kernel of P consists of c(z)t_j(z), with deg t_j<a-1,
so its dimension is b(a-1). The left kernel of Q consists of d(x)s_r(x),
with deg s_r<b-delta, so it has dimension a*max(0,b-delta).
If delta>=b, Q is surjective onto the intermediate space and rank M
is rank P=a^2*b+b, too large. Thus delta<b.

Pair the two kernel spaces by the ordinary nondegenerate coordinate
pairing. Its matrix R_g has rows(u,r), columns(j,v), and entries

    (R_g)_((u,r),(j,v)) = g_(j-u,r-v),

where0<=u<b-delta,0<=r<a,0<=j<b,0<=v<a-1. Orthogonality of im Q and
ker Q^T gives the exact formula

    rank M = a(a+1)b-a(b-delta)-b(a-1)+rank R_g.       (1)

The biform g is nonzero: otherwise ker U would lie in im V and UV would
have rank below a.

## A lower bound forces the second pencil

Transpose R_g and represent the u coordinates by polynomials in x of
degree<b-delta. It is the full coefficient map of the (a-1)-by-a matrix
whose entries are g_(r-v)(x). Over C(x), this matrix has row rank a-1:
its transpose is multiplication by the nonzero polynomial g(x,z), of
z-degree at most one, on polynomials of degree<a-1.
Select a-1 independent columns over C(x). Restricting polynomial inputs
to those columns gives an injection and proves

    rank R_g >= (a-1)(b-delta).

Equation(1) therefore gives rank M>=a^2*b+delta. At one-unit excess,
delta=1 necessarily. Both kernels are now primitive pencils.

## The bilinear pairing must be separable

For delta=1, g has degree at most one in each variable. If g=f(x)h(z),
the coefficient map above is a constant rank-(a-1) matrix followed by
injective polynomial multiplication by f. Thus

    rank R_g = (a-1)(b-1).

If g is nonseparable, its two z-coefficients g_0(x),g_1(x) are independent
linear forms after degree-one homogenization. They are coprime. The
(a-1)-by-a coefficient matrix has a one-dimensional rational kernel with
primitive polynomial generator

    ((-g_1)^(a-1), g_0*(-g_1)^(a-2), ..., g_0^(a-1)),

of degree a-1. Its degree-below-(b-1) input kernel has dimension b-a.
Consequently rank R_g=a(b-1)-(b-a)=b(a-1). Substitution in(1) gives

    rank M = a^2*b+1    if g is separable,
    rank M = a^2*b+a    if g is nonseparable.         (2)

This proves necessity and sufficiency of the stated conditions. A change
of constant minimal rank factorization transforms c and d contragrediently;
it preserves g up to a nonzero scalar, so the criterion is well-defined.

## Controls and remaining construction problem

The verifier checks R_g directly for g=1, x*z, 1+x*z, and higher-degree
x^delta+z. It verifies the full P Q factorization on small coefficient
models and checks original one-unit Hankel examples separately. General
coefficient models are explicitly labeled when they are not Hankel sources.
The construction question is now to realize the required large matrix
parameter space while preserving the Hankel equations and these kernel
pencils. The factor criterion alone does not accomplish that.

## Local deformation pilot

At the actual Hankel slice f0=1, f_(a-1)=xz, fix its two kernel pencils.
The coefficient factors have1262 free entries for A(8,10). Exact rational
elimination gives full derivative rank1212 and Hankel-defect derivative
rank1063. Therefore the image of the linearized solution space has dimension
149. The smaller controls A23 and A34 give8 and21, respectively.

These are tangent-image dimensions at one sparse point with fixed pencils.
They do not prove an integrable149-dimensional family, a smooth component,
a global dimension bound or a matrix-target restriction. In particular149
is above the126-dimensional rank-two parameter variety of the remaining
ordinary target, so this pilot alone does not exclude that target.
