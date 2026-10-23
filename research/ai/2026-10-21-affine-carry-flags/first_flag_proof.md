# An affine carry first flag

This package records an exact starting flag for the convolution-source program.
It does not construct every sector of T_m and does not improve the exponent.

Work over any field. Let m >= 4 and choose a,b in the field. Put

    r(t) = 1 + b t^m + a t^(m+1),
    U = span(r, t r, t^3, ..., t^m).

The shared space has dimension m and fits in the degree-(m+2) polynomial
window, hence in the shared leg of C(m+3,B). Let h and g be arbitrary
polynomials of degrees at most B-2 and B-3, respectively. The six input rows are

    Y_0 = 1;
    Y_1 = (h, t h);
    Y_2 = (g, 1+t g, t+t^2 g).

These rows fit in the input window of dimension B. Their independence is an
additional open condition; it is not needed for the product-space upper bound.

## Exact product-space identity

The space I = {u in U : t u is in U} has dimension m-2 and basis

    r, t^3, ..., t^(m-1).

Indeed U+tU has basis r,tr,t^2r,t^3,...,t^(m+1), of dimension m+2.
The first three members have distinct nonzero lowest coefficients in degrees
0,1,2, and the remaining members are monomials in higher degrees.

For every u in I the following three relations hold:

    (t u)h - u(t h) = 0,
    (t u)g - u(1+t g) + u*1 = 0,
    (t u)(1+t g) - u(t+t^2 g) = 0.

As vectors in U tensor K^6, where K^6 is the formal input label space,
these 3(m-2) relations are independent. This argument does not require
the six displayed polynomials themselves to be independent. The first group is the only one using
the input label th. After that group vanishes, the third group is the
only one using the input label t+t^2g. The second group is then
independent because multiplication by t is injective on polynomials.

Consequently

    dim U*span(Y_0,Y_1,Y_2) <= 6m - 3(m-2) = 3m+6.

The verification script evaluates all relations over the integers, checks
their independent coefficient rows modulo101, and supplies integer choices
of h,g for which the product rank reaches the upper bound. The modular
rank lower bound and the exact relations together certify the rank for
those examples over Q.

## Relation to the finite six-sector search

The new F2 source C(9,23) uses m=6 and a=b=1, with the displayed shared
basis (r-t^6,tr,t^3,t^4,t^5,t^6). Its binary polynomial masks are

    h = 4181000, g = 1322951.

The product rank is24, leaving seven output moment directions. A complete
finite-field continuation is recorded separately in
../../../results/affine-carry-flags-2026-10-21/m6-f2-witness.json. Its all-coefficient replay passes. A finite
2-adic lift is also recorded separately; it is not a characteristic-zero
certificate.

These are same-session AI-derived calculations. The convolution source,
matched-sector target and exponent criterion retain the provenance of
the parent repository. No external review or asymptotic completion is claimed.

