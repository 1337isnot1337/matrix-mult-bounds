# Exact ranks when the mixed part is one linear-in-x factor to a power

October 23, 2026. Written and unreviewed, with no historical-priority,
independent-review, formalization or exponent-improvement claim.

Keep the source convention and characteristic-zero field of [the proof](proof.md).
Let2<=a<=b, and suppose the nonzero biform

    f(x,z)=U(x)*V(z)*h(x,z)^e,                         (1)

has degrees at most a-1,b-1. Here U,V are nonzero, e>=1, and h is an
irreducible polynomial over the algebraic closure, depending on both
variables, with degree exactly one in x. Then

    rank R(f)=a(b+e).                                 (2)

The degree assumptions imply e<a. The statement allows arbitrary degrees
in z consistent with the source size, and arbitrary admissible univariate
factors U,V. It is not restricted to binomials or powers of linear forms.

## Removing univariate factors really preserves crossed rank

If q is a nonzero polynomial with deg_x(Uq)<a and deg_z(q)<b, consider
R(q)^T as the coefficient map from vectors y_(j,L) to the a polynomials

    p_r(x)=sum_(j,L) q_(L-r)(x)*x^j*y_(j,L).

Multiplying q by U multiplies every output polynomial p_r by U. Before
multiplication its degree is at most m-1-deg U, where m=a+b-1. Hence
the complete product still fits in the maintained output range H<m.
Polynomial multiplication by U is injective on this image. Consequently

    rank R(Uq)^T=rank R(q)^T.                         (3)

Similarly, R(q) itself has output polynomials in z indexed by j:

    p_j(z)=sum_(H,r) q_(H-j)(z)*z^r*w_(H,r).

Multiplication by V multiplies these polynomials by V injectively, and
deg_z(Vq)<b makes their complete coefficient ranges fit in L<m. Thus

    rank R(Vq)=rank R(q).                            (4)

These are injectivity statements on the actual output images. They do
not assume that a truncated multiplication matrix is invertible: for
example U=x and V=z are permitted. Applying (3)-(4) removes U and V
from (1) without changing rank.

## Matching lower and upper bounds

The mixed-factor multiplicity bound gives rank R(h^e)>=a(b+e).
Because deg_x h^e=e, all columns with H>=b+e vanish. Their complement
has exactly a(b+e) columns, giving the reverse inequality. Equations
(3)-(4) transfer equality to f, proving (2).

For a directly recognizable family, write h=A(z)+x*B(z), with B nonzero,
gcd(A,B)=1 and at least one of A,B nonconstant. The polynomial is
primitive as a polynomial in x over K[z], and is linear and irreducible
over K(z). Clearing denominators proves its irreducibility in K[x,z].
Over an algebraically closed coefficient field it therefore meets the
mixed-factor hypotheses above. Examples include x+z^k and
z^2+x*(1+z), with all source-degree restrictions retained.

The equality cannot be extended by adding multiplicities of different
mixed factors. At a=b=3, f=(x+z)*(x-z) has rank14, whereas a(b+2)=15.
The exact power (x+z)^2 does have rank15. The separate factor/power
hypothesis in (1) is essential to this deduction.

## Verification scope

The companion test module checks five nonlinear or univariate-decorated
instances using symbolic coefficient extraction and an independent exact
rank backend. It also verifies both literal multiplication identities,
including monomial factors with singular truncated matrices, and the
two-distinct-factor boundary. These controls are finite; the all-size
argument is (3)-(4) and the matching bounds. No source-space dimension
classification or complete matrix target follows.
