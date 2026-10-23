# A unit-kernel obstruction with one regular long leg

October 23, 2026. Claims `AI-UNIT-KERNEL-LOW-RANK-001` and
`AI-A4-ONE-REGULAR-LEG-002` are written and unreviewed. Owner-directed
OpenAI Codex work; no independent review, formalization or exponent gain.

## 1. General statement

Put O=C[[t]] and K=C((t)). Let M:A -> Mat_N(C) be a source slice map
with rank M(a)>=mu for every nonzero a in A. Let Xi:E -> Mat_R(C)
be a target slice map such that:

* Xi(x_unit)=I_R for some x_unit in E;
* E is spanned by a set Gamma with rank Xi(gamma)<=rho for every gamma.

Assume N>=R and set k=N-R. If

    mu > rho+2k,                                             (1)

there are no Laurent linear maps F:E -> A, B in Mat_(R,N)(K), and
C in Mat_(N,R)(O), with rank C(0)=R, satisfying the complete identity

    B(t) M(F(t)(x)) C(t) = Xi(x)+O(t) for every x in E.        (2)

Every finite Laurent pole order in F and B is allowed. There is no
assumption on their leading flags or on the original lift F(x_unit).
Only the first-leg minimum source rank is used; there is no row-rank
minimum or source-kernel dimension hypothesis. The symmetric statement
holds after exchanging the row and column tensor legs.

The assertion requires a square target slice space with a unit and a
spanning set of low-rank slices. It is not asserted for an arbitrary
target using only its minimum slice rank.

## 2. Scalar balancing and the exact right inverse

The unit in (2) implies F is not identically zero. Let m be the smallest
valuation among its finitely many matrix entries. Replace F by t^(-m)F
and B by t^m B. Linearity of M preserves (2) exactly. Now F is regular
and its constant linear map F_0 is nonzero. This step may change whether
the particular unit lift is polar or vanishing; it preserves C.

Define the regular matrices

    Y_x=M(F(x)) C,                 D=Y_(x_unit).

The unit equation says G=B D=I_R+O(t), a regular invertible matrix.
Replace B by G^(-1)B. Every output remains regular with constant Xi(x),
and now

    B D=I_R exactly.                                         (3)

No inverse of D(0), source unit slice or minor of its limit is used.
In particular D(0) can have any rank, including zero.

## 3. The common kernel correction is regular

Write Z_x=B Y_x, which is regular with Z_x(0)=Xi(x). Set

    P=I_N-D B,          W_x=Y_x-D Z_x=P Y_x.                 (4)

Over K, (3) implies B has rank R, B P=0 and P acts as the identity on
ker B. Thus rank_K P=k, and rank_K W_x<=k. Although P can have poles,
the expression Y_x-D Z_x shows that W_x is regular.

All (k+1)-minors of W_x vanish over K and therefore vanish at zero.
Consequently

    rank W_x(0)<=k,
    M(F_0(x)) C(0)=D(0) Xi(x)+W_x(0).                        (5)

The regularity in this step is essential. A raw constant coefficient of
a polar rank-k matrix need not have rank at most k. Equation (4) proves
regularity of the actual correction before specializing it.

## 4. Low-rank generators force the leading first map to vanish

Fix gamma in Gamma. Equation (5) gives

    rank(M(F_0(gamma)) C(0)) <= rho+k.                        (6)

Since C(0) has rank R, deleting its complementary k source columns can
lose at most k in matrix rank. If F_0(gamma) is nonzero, the source
minimum therefore gives

    rank(M(F_0(gamma)) C(0)) >= mu-k > rho+k,                 (7)

a contradiction. Hence F_0 vanishes on Gamma. Because Gamma spans E,
F_0=0, contrary to scalar balancing. This proves the theorem.

The proof does not conclude that the original maps become regular.
Instead, a regular leading first map exists by scalar balancing, and
every possible such leading map is excluded.

## 5. The A4 consequence

For the canonical cyclic convolution source A4, N=112 and mu=16.
These values and the all-field minimum-rank proof are prior maintained
work, pinned in sources.json: see Sections 2-3 of
[the source note](../2026-10-20-koszul/cyclic_finite_target.md).

Take E=Mat_10(C), R=110 and Xi(X)=X tensor I_11. The one hundred
matrix units E_ij span E, and every Xi(E_ij) has matrix rank11.
The target identity is Xi(I_10)=I_110. Thus k=2, rho=11 and

    16 > 11+2*2=15.                                        (8)

There is no A4 to M(10,10,11) formal degeneration with either long map
regular and of rank110 at zero. In the transposed case Xi becomes
X^T tensor I_11 and the same generators and unit apply. Both other
maps may have arbitrary finite poles, including a polar original unit
lift. This removes all the unit-image hypotheses of the earlier
[partial-unit theorem](../2026-10-23-regular-unit-image/proof.md).
Its claims and original proof retain their status and attribution.

More invariantly, for any Laurent matrix A(t) let v(A) be the minimum
valuation of its nonzero entries. A scalar-balanced matrix t^(-v(A))A
is regular with a nonzero constant term. If either long map has a
rank110 limit after this balancing, rescale it by that scalar and
compensate in F; (2) is preserved and the theorem applies. Every remaining
candidate must therefore have rank at most109 in the scalar-balanced
leading coefficient of each long map. This is a necessary condition,
not an exclusion of those candidates. Singular source frame changes
are not allowed in deriving it.

## 6. Evidence, limits and attribution

This result concerns the full112-dimensional source, not the separate
fourteen-row conic incidence or the asymmetric boundary problem. The
source minimum, ordinary A4 rank obstruction and earlier Laurent work
retain their prior credit and exact source pins. The scalar balancing,
regular right-inverse correction and low-rank spanning argument here
use elementary linear algebra and formal Laurent coefficients. No new
external theorem or historical priority is claimed.

The exact finite controls check polar projections with regular
corrections, zero-rank unit images, scalar balancing, isolated sharp
rank-loss budgets, the100 target generators and an actual minimum source
coordinate slice. They do not formalize the arbitrary-series proof or
constitute independent mathematical review. Cases with both balanced
long-leg limits singular remain open, as does the full target. There
is no matrix multiplication construction or improvement below9/4.
