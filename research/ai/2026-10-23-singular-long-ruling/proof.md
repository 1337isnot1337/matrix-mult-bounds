# Excluding singular A4 long-leg limits of rank at least106

October 23, 2026. Owner-directed OpenAI Codex work. Written and unreviewed;
no independent mathematical review, formalization or exponent improvement.

## 1. A general ruling criterion

Work over O=C[[t]], K=C((t)). Let M:A -> Mat_N(C) have minimum nonzero
slice rank mu. Let Xi:Mat_m(C) -> Mat_R(C) be `Xi(X)=X tensor I_n`,
where R=mn and m,n>=1. Put k=N-R>=0. Suppose C is a regular N-by-R
matrix with rank C(0)=c, and there are Laurent maps F and B such that

    B M(F(X)) C = Xi(X)+O(t) for every X in Mat_m(C).     (1)

Put L=n+k+N-c. Assume:

* every vector subspace U of A with all its nonzero slices of rank at
  most L has dimension at most ell, for some ell<m;
* mu>N-c+k.

Then (1) is impossible. No regular unit lift, prescribed leading flags
or finite bound on Laurent pole orders is assumed. The source row-leg
contraction minimum is not needed. The symmetric assertion holds after
transposing the source slices and exchanging the two long legs.

## 2. Scalar balance and a shared regular correction

The unit parameter in (1) makes F nonzero. Let v be the smallest
valuation of its finitely many entries. Replace F by t^-v F and B by
t^v B. The identity is unchanged, C stays regular, and the new F is
regular with F_0 nonzero. Put

    Y_X=M(F(X)) C,       T=Y_I,       Z_X=B Y_X.

All these matrices except B are regular, and Z_X(0)=Xi(X). The matrix
G=B T=I_R+O(t) is regular invertible. Normalize B by G^-1, after which
BT=I_R exactly and all Z_X still have the stated constant terms.

The rank-k projector P=I_N-T B may have poles. Nevertheless

    W_X=P Y_X=Y_X-T Z_X                               (2)

is regular for every X. This is the regular-right-inverse mechanism
used in concurrent PR113 (pinned in sources.json), retained with its
credit; PR112 also derives general regularity from this projector.

More is true than the separate inequalities rank W_X(0)<=k. Choose a
constant basis X_1,...,X_(m^2) of the target parameter space and concatenate
the matrices W_(X_j) horizontally. Over K their common left factor P
gives rank at most k. The whole concatenation is regular, so every
(k+1)-minor remains zero at t=0. There is therefore one fixed column
space V in C^N, dim V<=k, containing every column of every W_X(0).

Let pi:C^N -> C^N/V be the constant quotient and let A=pi T(0).
Taking (2) at zero gives, for every X,

    M(F_0(X)) C(0)=T(0) Xi(X)+W_X(0),
    pi M(F_0(X)) C(0)=A Xi(X).                         (3)

No polar projector is itself specialized. The entire shared correction
matrix, which (2) proves regular, is specialized instead.

## 3. A target ruling forces the quotient unit image to vanish

For every rank-one X, Xi(X) has rank n. Equation (3) before taking pi
implies rank(M(F_0(X)) C(0))<=n+k. Restoring the missing source columns
loses at most N-c ranks, so

    rank M(F_0(X))<=n+k+N-c=L.                         (4)

Fix u in C^m, u nonzero. The matrices X=u v^T, v in C^m, form an
m-dimensional vector ruling, consisting of rank-one matrices and zero.
Its F_0 image is a vector subspace all of whose slices have rank at most
L, so its dimension is at most ell.

If A(u tensor I_n) is nonzero, the linear map

    v -> A Xi(u v^T)

is injective: its j-th n-column block is v_j A(u tensor I_n), and one
entry of the latter matrix is nonzero. By (3), F_0(u v^T)=0 would force
this matrix to vanish, hence v=0. Thus F_0 maps this ruling injectively
into a vector space of dimension at most ell<m, a contradiction.

Consequently A(u tensor I_n)=0 for every u. These column spaces span
C^R, so A=0. Equation (3) now puts the columns of M(F_0(X)) C(0) in V
for every X, giving matrix rank at most k. If F_0(X) is nonzero, the
source rank minimum and rank C(0)=c instead give rank at least
mu-(N-c)>k. Hence F_0=0, contrary to scalar balancing. This proves the
general criterion at every finite Laurent order.

## 4. Prior A4 rank geometry and its use

Adopt the existing canonical source A4, with N=112 and mu=16. The
pinned [rank-gap proof](../2026-10-20-anisotropic-constructions/slice_rank_gap.md)
gives no nonzero ranks strictly between16 and20. The pinned
[minimum-rank classification](../2026-10-20-koszul/cyclic_finite_target.md),
Section 4, says its minimum slices are exactly

    f=u tensor h tensor v,
    u,v in C^4, h on the degree-six rational normal curve in C^7.

Every vector subspace wholly in this cone has dimension at most four.
Here is the elementary linear-space justification. In a linear space
of decomposable three-factor tensors, comparison of each pair and their
sum forces at most one projective factor to vary; otherwise a two-factor
flattening of their sum has rank two. Comparing with one fixed nonzero
tensor makes this the same varying factor for the entire linear space.
The outer factors have vector dimension four. The middle curve contains
no projective line: for distinct coherent endpoints a GL2 change makes
their degree-six forms the two pure endpoint powers, whose nontrivial
sum has Hankel rank two. Thus the middle factor contributes at most one
vector dimension. The maximum is four and is attained by varying u
with h,v fixed.

The target M(10,10,11) has m=10, n=11, R=110, k=2. For c>=106,

    L=11+2+112-c<=19<20,
    ell=4<10,         mu-(N-c)>=16-6=10>2.

The criterion excludes (1). There is no A4 to M(10,10,11) formal
degeneration with either long map regular and of limiting rank at least106,
even with arbitrary finite poles in both other maps and in the original
identity lift. This extends PR113's rank110 premise to singular limits.

Any Laurent long map can be scalar-balanced to be regular; compensate
by the inverse scalar on F to preserve (1). Thus every remaining target
candidate must have rank at most105 in the scalar-balanced leading
coefficient of each long map. This necessary condition does not construct
or exclude candidates satisfying it. The two balances are applied in
separate uses of the theorem, not assumed simultaneously achievable with
a common nonzero leading first map.

## 5. Boundary, dependencies and evidence tier

At c=105, L=20. An actual source slice with biform 1+xz and coherent
middle factor has rank20 and lies outside the minimum cone. Hence the
adopted minimum-cone dimension bound four is not justified for this cap.
This proof supplies no exclusion at c105. A sharper bound for linear
spaces of rank-at-most20 slices could improve the criterion, but is a
separate question, not an accepted premise here.

The rank-gap proof uses Grothendieck's splitting theorem for holomorphic
vector bundles on P^1(C): the kernel bundle splits as a direct sum of
line bundles. Its citation is the 1957 article, Theorem2.1, printed p126,
DOI10.2307/2372388; the primary scan is linked in sources.json. The
coefficient-map and rank arguments, source definitions and classification
remain credited to their existing repository packages. The local new step
is to retain the common correction column space and test complete target
rulings, allowing a singular long-leg limit.

Exact finite controls support shared correction specialization, target
ruling injectivity and actual source ranks, but do not formalize arbitrary
series, classify all bounded-rank linear spaces or supply independent
mathematical review. The full matrix target and any exponent below9/4
remain unconstructed.
