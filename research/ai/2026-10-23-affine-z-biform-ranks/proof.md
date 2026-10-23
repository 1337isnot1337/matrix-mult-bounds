# Exact ranks for biforms affine in the long variable

October 23, 2026. Owner-directed AI-assisted research. The theorem below has a complete written proof and finite exact controls, but no independent mathematical review or formalization. It does not establish a tensor degeneration or an exponent improvement.

## Setup and result

Let K be any field and 2 <= a <= b, with m=a+b-1. For a polynomial f(x,z) of bidegree at most (a-1,b-1), use the cyclic-source coefficient matrix R_(a,b)(f), with rows (j,L), 0<=j<b and 0<=L<m, columns (H,r), 0<=H<m and 0<=r<a, and entry

    R[(j,L),(H,r)] = coefficient of x^(H-j) z^(L-r) in f.

Negative and out-of-range coefficients mean zero. This is the convention from the source pinned in sources.json.

Consider every nonzero polynomial f(x,z)=u(x)+z*v(x), with deg u, deg v <a. If both u,v are nonzero, let g=gcd(u,v), let u0=u/g and v0=v/g, and set d=max(deg u0,deg v0). When one coefficient is zero, set d=0.

**Theorem (complete long-affine rank formula).** Over every field, including every positive characteristic,

    rank_K R_(a,b)(u+z*v) = ab + min(b,a*d).                (1)

The possible ranks for this entire family are exactly

    {ab + min(b,a*d) : d=0,...,a-1}.                      (2)

All are attained over every field by f=1+x^d*z. For d=0 the polynomial is separable and the rank is ab. The theorem is restricted to biforms affine in z; it does not concern all biforms or a full three-leg tensor map.

Examples: at (a,b)=(3,7), f=1+x^2*z has rank 27, rather than the general nonseparable lower bound 24. At (a,b)=(3,4), f=(1+x)+z*(1+x^2) has rank 16.

## Proof (all fields, all coefficient choices)

Since f has z-degree at most one, a nonzero entry requires L-r in {0,1}. Consequently all row groups indexed L>a are zero. The remaining a+1 groups, L=0,...,a, have b rows each, totaling b(a+1) active rows.

Encode an arbitrary linear dependence among the active rows by polynomials

    lambda_L(x) = sum_(j=0)^(b-1) lambda_(j,L) x^j,
    L=0,...,a,

each of degree <b. For a fixed column (H,r), the contraction of this row dependence is the coefficient of x^H in

    u(x)*lambda_r(x) + v(x)*lambda_(r+1)(x).             (3)

Both products have degree at most (a-1)+(b-1)=m-2, and every H=0,...,m-1 occurs among the columns. Thus the active-row dependence is in the left kernel precisely when the following are complete polynomial identities:

    u*lambda_r + v*lambda_(r+1) = 0, for r=0,...,a-1. (4)

If u or v is zero (but not both), the equations force exactly a of the a+1 polynomials lambda_r to vanish; the remaining polynomial is arbitrary of degree <b. The left kernel has dimension b, so the rank is ab.

Suppose u and v are both nonzero. Dividing the equations by g reduces to the coprime pair u0,v0. The recursion in K(x) gives

    lambda_r = (-u0/v0)^r lambda_0.                      (5)

Because lambda_a is polynomial and gcd(u0,v0)=1, the relation v0^a | (u0^a lambda_0) implies v0^a | lambda_0. Write lambda_0=v0^a*h. It follows that every solution and only a solution has

    lambda_r = (-1)^r u0^r v0^(a-r) h,
    r=0,...,a.                                          (6)

The maximum degree of these a+1 nonzero factors (without h) is a*d: the degrees vary affinely with r, and at least one endpoint has degree a*d. Thus all lambda_r have degree <b if and only if deg h < b-a*d. The left kernel has dimension max(0,b-a*d), and rank-nullity on the b(a+1) active rows gives

    rank R = b(a+1)-max(0,b-a*d) = ab+min(b,a*d).

The formula is independent of characteristic. Taking u=1 and v=x^d, for each 0<=d<a, proves that every listed rank is attained, completing the spectrum classification. No external structural theorem is used.

## Acceptance and precise limits

Run from the repository root:

    python -I research/ai/2026-10-23-affine-z-biform-ranks/verify.py
    python -m unittest discover -s tests -p 'test_affine_z_biform_ranks.py' -v

The verifier constructs the original full bm-by-am coefficient matrix and performs exact modular elimination. Exhaustive and fixed-seed cases cover several finite fields and rectangular formats; the saved receipt is results/affine-z-biform-ranks-2026-10-23/controls.json. Such tests are finite corroboration, not the all-field proof. The code is standard-library only.

The coefficient convention and general ab versus at-least-ab+a gap come from the exact main-branch source pinned in sources.json. PR171 studies two-monomial biform ranks; PR186 studies an arbitrary-biform gap and a different special nonlinear-factor family; PR207 studies diagonal-polynomial f(xz) Toeplitz ranks. The current result gives exact ranks for *all coefficients* in u(x)+z*v(x), including unequal a,b, and imports none of those concurrent claims.

No independent external review, formal verification, historical priority, general biform rank classification, linear-space cap, full tensor degeneration or matrix-multiplication exponent gain is asserted.

**Next construction question.** For f=u(x)+z*v(x)+z^2*w(x) with a>=3, classify the polynomial syzygy module for the three-term row-dependency recurrence and identify precisely which primitive-degree data can or cannot determine rank. The diagonal f(xz) subproblem belongs to PR207, so use a genuinely nondiagnonal sample or a different structural invariant. A future exponent result additionally needs compatible maps on all three tensor legs and the exact tensor-character implication.
