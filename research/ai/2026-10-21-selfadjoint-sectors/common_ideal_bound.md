# A finite rank bound for the common isotropic ideal construction

October 21, 2026. AI-derived proof, checked within the same research session.
External mathematical review and formalization remain outstanding.
This is a necessary condition for the specified construction class. It does
not exclude arbitrary Laurent maps or arbitrary simultaneous isotropic spaces.
It leaves the exact rational C(6,20) five-sector witness valid.

## Hypotheses

Let a, B, H be positive integers with H<B.
The shared source polynomials belong to P_{a-1}. The second source polynomials
belong to P_{B-1}. A linear functional ell on univariate polynomials obeys
ell(z^j)=0 for j>=2H. Target coefficients are produced by the moment pairing

    ell(u f g),   u in P_{a-1}, f,g in P_{B-1}.

All target rows on one nonshared leg with degrees p=0,...,s-1 have source
polynomials f divisible by z^H. Thus they lie in z^H P_{B-H-1}.
Arbitrary linear combinations within this ideal are allowed. Coefficients,
row bases, and ell may depend rationally on a Laurent parameter, provided
these degree, ideal, and moment-vanishing hypotheses hold away from zero.
The argument also allows any subspace of these source polynomial spaces.

The retained tensor has matched degree sectors C(p+1,m-p), with their common
output space of dimension m. Each sector may have its own invertible shared
map H_p. All negative Laurent coefficients and unwanted constant coefficients
must vanish so that there is an actual tensor limit.

## Source flattening bound

For the low rows, every product u f is divisible by z^H and has degree at
most B+a-2. The functional ell discards all terms of degree at least 2H,
even after multiplication by another polynomial with nonnegative exponents.
Therefore the linear map

    span{u tensor f : f is a low row} -> (P_{B-1})^*,
    u tensor f -> [g -> ell(u f g)]

factors through the coefficient space with exponents

    H, H+1, ..., min(B+a-2,2H-1).

Its rank is at most

    min(H, B+a-H-1).                                    (1)

Restricting the other nonshared factor, choosing dense bases, and applying
invertible Laurent weights cannot increase this rank. Rank<=r is defined by
the vanishing of all (r+1)-minors; it is closed under a coefficientwise tensor
limit. Thus the same upper bound holds for the retained partial target.
This use of closedness concerns the whole actual partial tensor limit, not an
isolated coefficient of a Laurent series with uncancelled negative terms.

## Target flattening rank

Restrict the target to low p=0,...,s-1 on that nonshared leg. Its opposite
nonshared factor is the direct sum of disjoint degree-(m-1-p) spaces. In the
p-th block, the flattening on the opposite factor has rank m-p because
C(p+1,m-p) is concise and H_p is invertible. The images of different blocks
are independent: they occupy different low-degree subspaces in the product
of the shared and low factors. Hence the partial target flattening has rank

    M_s = sum_{p=0}^{s-1}(m-p) = sm-s(s-1)/2.             (2)

Combining (1) and (2) gives M_s<=H and M_s<=B+a-H-1, hence

    B+a-1 >= 2M_s.                                     (3)

The actual input/output orientation is retained in this argument. The rank
is the opposite nonshared flattening of the target after selecting all low
rows; it is not the sum of the low input dimensions.

## Consequence for a proposed unbounded family

Use all strictly lower degrees under the symmetric weights p-(m-1)/2, so
s=floor(m/2), and set a=m+O(1). Then M_s=(3/8)m^2+O(m), while
N=m(m+1)/2=(1/2)m^2+O(m). Equation (3) forces

    B >= (3/4)m^2+O(m),   liminf B/N >= 3/2.              (4)

The cost B=N+O(m) is therefore impossible within these hypotheses. In the
specific choice a=m+1 and B=N+m, the necessary test already fails at m=10
and every larger m. For m=2r the necessary lower bound is 3r^2-r, compared
with N+m=2r^2+3r; their difference is r(r-4). For m=2r+1 it is
3r^2+r-1, compared with N+m=2r^2+5r+2; the difference is r^2-4r-3.
The first odd failure is m=11. The companion JSON checks m=4,...,12 exactly.
These finite tests illustrate the symbolic proof, rather than replacing it.

## Principal-ideal extension and ways outside the hypotheses

The same argument applies to the ideal (h) in a Frobenius algebra K[z]/(h^2),
where deg(h)=H and ell annihilates the ideal (h^2). A polynomial f of degree
at most B-1 divisible by h is h times a polynomial of degree at most B-H-1.
Multiplication by u has image in h times a space of dimension at most
B+a-H-1; reduction modulo h limits that dimension to H. This gives (1).
It does not require h=z^H, a particular basis, or nilpotence at one point.

Possible constructions outside this proof include low spaces that are not
contained in a common principal isotropic ideal, independent maps on the two
nonshared factors with different annihilation mechanisms, and pairings that
do not factor through the stated moment truncation or quotient. No positive
asymptotic construction from these alternatives is established here.

Sources within the session: the exact [five-sector construction](README.md)
and [six-sector construction](m6_construction.md), and the existing
[matched-sector criterion](../2026-10-20-construction-sprint/independent_sector_bases.md).
The character conversion and its external attribution remain in that
criterion. This proof is elementary linear algebra and makes no additional
claim about the tensor spectrum.

The six-sector construction uses ordinary low-degree monomials for target
degree two. Its full strictly lower-degree space therefore lies outside the
common-ideal hypothesis. Mixed or recursive moment constructions are not
excluded by this proof.
