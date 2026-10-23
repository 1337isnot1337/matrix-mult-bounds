# Exact ranks for quadratic-in-z biforms with constant outer coefficients

October 23, 2026. Owner-directed AI-assisted mathematics. Written proof, not independently reviewed or formalized. This is a theorem about one source slice, **not** a matrix-multiplication exponent improvement.

## Literal source and theorem

Let K be **any field**, let a >= 2 and b >= 3, and put m=a+b-1. Let R_(a,b)(f) have rows (j,L) with 0 <= j < b, 0 <= L < m, columns (H,r) with 0 <= H < m, 0 <= r < a, and entries

    R[(j,L),(H,r)] = [x^(H-j) z^(L-r)] f(x,z).

Here brackets denote a coefficient, zero for negative exponents. This is the maintained cyclic-source convention, originally pinned at the main-branch source in `sources.json`.

For arbitrary alpha,gamma in K^*, and arbitrary v(x) in K[x] of degree < a, set

    f(x,z) = alpha + z*v(x) + gamma*z^2.

Write d=deg(v) when v != 0, and d=0 when v=0.

**Theorem (all fields, all middle polynomials).** The literal full coefficient matrix satisfies

    rank_K R_(a,b)(f)
      = ab + min(b,ceil(a/2)*d) + min(b,floor(a/2)*d).       (1)

Its left kernel has the explicit K-basis constructed in Section 3. Consequently the rank depends only on the degree of v, even in positive characteristic. Every value in (1) for 0 <= d < a occurs (choose v=x^d, with v=0 also giving d=0).

The theorem differs from the simultaneous diagonal-polynomial Toeplitz study in PR207 and the affine-in-z classification in PR209: f has a genuinely quadratic z term, and v is an **arbitrary polynomial** rather than a diagonal or monomial restriction.

## Reduction to a complete recurrence

Because f has z-degree two, nonzero matrix rows have 0 <= L <= a+1. They are all present since b >= 3 implies m-1 >= a+1. Thus there are (a+2)b active rows.

Encode their coefficients in a putative left-kernel vector as polynomials

    lambda_L(x) = sum_(j=0)^(b-1) lambda_(j,L) x^j,
                   0 <= L <= a+1,

all of degree < b. For each r=0,...,a-1, the scalar product with column (H,r) is the coefficient of x^H in

    alpha*lambda_r + v(x)*lambda_(r+1) + gamma*lambda_(r+2).

Each summand has degree <= m-1, and the columns include *every* H from 0 to m-1. No endpoint coefficient is discarded. Hence the left kernel is **exactly** the polynomial solution space of

    alpha*lambda_r + v*lambda_(r+1) + gamma*lambda_(r+2) = 0,
                     r=0,...,a-1,                              (2)

subject to deg(lambda_L)<b.

## Central-pair parametrization and predictable degrees

Set c=a/2 if a is even, and c=(a+1)/2 if a is odd (integer notation). Prescribe the two central polynomials

    lambda_c = h,       lambda_(c+1) = k.

Since alpha and gamma are nonzero *scalars*, (2) recursively determines all earlier and later lambda polynomials without denominators involving x:

    lambda_r = -(v*lambda_(r+1)+gamma*lambda_(r+2))/alpha
        for r=c-1,...,0;
    lambda_(r+2) = -(alpha*lambda_r+v*lambda_(r+1))/gamma
        for r=c,...,a-1.                                      (3)

Every pair (h,k) in K[x]^2 gives one polynomial solution of (2), and every solution arises uniquely this way. The center entries make this module identification injective.

For d>0, the crucial **predictable-degree identities** are

    a=2s:    max_(0<=r<=a+1) deg(lambda_r)
                 = max(deg(h)+s*d, deg(k)+s*d),               (4)

    a=2s+1:  max_(0<=r<=a+1) deg(lambda_r)
                 = max(deg(h)+(s+1)*d, deg(k)+s*d).           (5)

Use deg(0)=-infinity. To prove the upper bounds, iterate (3): every outward step uses either multiplication by v (adding at most d to degree) or a scalar multiplication. For a=2s, the largest h-distance and k-distance are s on the respective outside endpoints. For a=2s+1, the largest h-distance is s+1 on the left and the largest k-distance is s on the right. These give precisely the displayed upper bounds.

For the lower bounds, note that repeated multiplication by v has nonzero leading coefficient, since the leading coefficient of v and alpha,gamma are nonzero. When a=2s, lambda_0 contains an h term of degree deg(h)+s*d and a k term of degree at most deg(k)+(s-1)*d; lambda_(a+1) contains a k term of degree deg(k)+s*d and an h term of degree at most deg(h)+(s-1)*d. If deg(h)>=deg(k), the first term dominates uniquely in lambda_0. If deg(k)>deg(h), the second dominates uniquely in lambda_(a+1). This proves (4), with zero cases interpreted in the evident way.

For a=2s+1, lambda_0 contains an h term of degree deg(h)+(s+1)*d and a k term of degree at most deg(k)+s*d; lambda_(a+1) contains a k term of degree deg(k)+s*d and an h term of degree at most deg(h)+(s-1)*d. If deg(h)+(s+1)*d > deg(k)+s*d, the left h term dominates. Otherwise the right k term dominates (its competing h term is at least 2d lower). This proves (5), even in a characteristic where other coefficients vanish.

If d=0, including v=0, (3) uses only scalar coefficients. Thus every lambda_r has degree <= max(deg h,deg k), while the central entries attain this maximum, so the same identities hold with d=0.

Equations (4)-(5) now show that all deg(lambda_r)<b if and only if

    deg(h) < b-ceil(a/2)*d,
    deg(k) < b-floor(a/2)*d.                               (6)

The polynomial vector space of degree strictly less than t has dimension max(0,t). Hence the left-kernel dimension equals

    (b-ceil(a/2)*d)_+ + (b-floor(a/2)*d)_+.

Subtracting from the (a+2)b active rows proves (1) without any characteristic assumption.

## Explicit kernel basis and examples

An explicit basis is obtained by applying recurrence (3) to the pairs

    (h,k)=(x^j,0),  0<=j<b-ceil(a/2)*d;
    (h,k)=(0,x^j),  0<=j<b-floor(a/2)*d.

An empty interval contributes no vectors. The vectors are independent because their central coordinates are independent. This also gives constructive finite certificates for any prescribed coefficients.

At (a,b,d)=(5,3,1), (1) gives rank 15+3+2=20 for every nonzero alpha,gamma and every linear v of degree one. By contrast, the affine-in-z family alpha+z*v has rank 18 by the separately credited PR209 formula. At a=b=3,d=2, the quadratic family has rank 14. With a=5,b=9 and v=1-2x+3x^2 over Q, rank is 45+6+4=55 irrespective of nonzero alpha,gamma.

When b>=ceil(a/2)*d the formula simplifies to rank ab+a*d. The source has no associated general linear-space cap or compatible three-leg extraction established here; this finite one-slice rank formula does not imply any bound on omega.

## Exact acceptance and remaining limits

From the repository root:

    python -I research/ai/2026-10-23-quadratic-z-middle/verify.py
    python -I research/ai/2026-10-23-quadratic-z-middle/verify_charzero.py
    python -m unittest discover -s tests -p 'test_quadratic_z_middle_ranks.py' -v

The primary standard-library verifier reconstructs the full source matrix and checks exact modular ranks, complete polynomial kernel bases, and the original column identities. The independent characteristic-zero implementation places source terms instead of retrieving coefficients and checks rational kernel vectors against all columns. Its full modular rank gives a rational lower bound, and the rational null vectors give the matching upper bound. Both implementations are from the same research session; they are *not* independent external mathematical review. Exact case counts are in `validation.json`.

Original source attribution and the concurrent PR boundaries are recorded in `sources.json`. No archive bytes were modified, no historical-priority claim is made, and no tensor degeneration or exponent improvement follows.

**Next precise bottleneck:** drop the assumption that alpha and gamma are constant units. For general quadratic f=u(x)+z*v(x)+z^2*w(x), the central-pair recursion is rational and polynomial integrality creates a nontrivial two-generator syzygy lattice. Its degree-filtered Hilbert function, not just the three coefficient degrees, governs rank. Classify its minimal polynomial basis or give exact examples separating equal-degree triples. This is distinct from the diagonal Toeplitz question owned by PR207 and from the arbitrary full three-leg target.
