# A slice-rank gap for distinct spectral atoms

October21,2026. Written proof, unreviewed. This narrows a construction
ansatz; it does not exclude general source slices or improve the exponent.

Fix a>=2 and b>=a+1. Suppose a source slice has the representation

    F_(i,k,s) = sum_(h=1)^(a+1) u_(h,i) lambda_h^k v_(h,s),

where the lambda_h are distinct finite complex numbers, each polynomial
u_h(x) is nonzero of degree<a, and each v_h(z) is nonzero of degree<b.
Write l=degree(lcm(v_1,...,v_(a+1))) and e=min_h degree(v_h). Then

    delta = max(0, a+e-l),
    rank(M_F) = b*(a*(a+1)-delta).                    (1)

In particular its slice rank is either a^2*b or at least a^2*b+b.
The first case requires every v_h to be proportional. In that case the
crossed coefficient matrix has rank at most a. Thus a crossed-rank-(a+1)
slice in this ansatz has slice rank at least a^2*b+b.

## Factorization and rank calculation

Index the source slice as

    M_F[(j,p,L),(H,q,r)] = F_(H-j,p+q,L-r),

with j,q in [0,b), p,r in [0,a), and H,L in [0,a+b-1).
Coefficients outside their ranges are zero. Factor M_F=P Q using an
intermediate index (h,j,r), of total dimension(a+1)*a*b:

    P[(j,p,L),(h,j',r)] = [j=j'] lambda_h^p v_(h,L-r),
    Q[(h,j,r),(H,q,r')] = [r=r'] lambda_h^q u_(h,H-j).

For a row relation of Q, fix r and form polynomials z_h(x) of degree<b
from the coefficients in j. The relation says

    sum_h lambda_h^q u_h(x) z_h(x)=0 for all q in [0,b).

The b-by-(a+1) Vandermonde matrix has full column rank. Consequently each
u_h z_h is zero, hence every z_h is zero. Therefore Q has full row rank
and rank(PQ)=rank(P).

P is b copies of a smaller map. Its kernel consists of polynomials
z_h(z) of degree<a such that sum_h lambda_h^p v_h z_h=0 for p in [0,a).
The a-by-(a+1) Vandermonde matrix has one-dimensional kernel generated
by c, and each c_h is nonzero. Thus v_h z_h=c_h f for one polynomial f.
This is equivalent to f being divisible by every v_h and satisfying

    degree(f) <= a-1+min_h degree(v_h).

The space of such f has dimension delta in (1), including the zero case.
This proves the rank formula. Since l>=e, delta<=a. Equality delta=a
requires l=e, which forces all v_h to have the same degree and be
proportional. Otherwise delta<=a-1, giving the gap.

When the v_h are proportional, the left factors of the crossed matrix
are lambda_h^p v_s. They lie in the a-dimensional space C^a tensor v.
Its crossed rank is therefore at most a, as asserted.

## Consequence and strict scope

For A(8,10), nine distinct rank-one spectral atoms with crossed rank9
have slice rank at least650. Such a slice cannot occur at a rank-two
parameter of the remaining M(32,33,33) ordinary candidate, whose source
slice ceiling is641. This does not exclude crossed rank8, repeated or
infinite spectral support, higher-rank residues, nonminimal representations,
or general slices. In particular it does not contradict the exact rank641
counterexample already recorded in `equality_one_step.py`.

The proof uses only Vandermonde rank, polynomial divisibility and an explicit
factorization. It has no historical-priority or independent-review claim.
Finite controls reconstruct original source entries, verify the factorization,
and compare the predicted rank with modular lower bounds and exact small
matrix ranks. These controls do not replace the general argument.

The650 bound is sharp within this ansatz. Take nodes1,...,9, every u_h=1,
the first eight v_h=(z+1)^8*(z+2), and v_9=(z+1)^8*(z+3). Then l=10,
e=9, delta=7, so the slice rank is650. The first eight crossed left
factors span C^8 tensor v_1; the ninth is outside that span. The right
factors are independent by their ten-row Vandermonde. Hence crossed rank
is9. A modular lower-bound control gives ranks65 and9 for the small
factor and crossed left factor, respectively; the proved factorization
and polynomial kernel supply the upper bound.
