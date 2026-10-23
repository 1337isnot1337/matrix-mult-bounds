# A regular right inverse and the A4 rank102 unit-image chart

October 23, 2026. Owner-directed OpenAI Codex continuation over C.
Written and unreviewed; no independent review or formalization.

## 1. Hypotheses and conclusion

Put O=C[[t]] and K=C((t)). Let M:A -> Mat_N(C) be a linear source
slice map, with d=dim A. Assume every nonzero source slice has rank at
least mu_A. Assume every nonzero source row covector lambda gives a
contraction `f -> lambda M(f)` of rank at least mu_B.

Let Xi:E -> Mat_R(C) be injective, dim E=D, with minimum nonzero matrix
rank nu and a parameter u for which Xi(u)=I_R. Suppose Laurent maps F,
B and C of sizes d-by-D, R-by-N and N-by-R satisfy, coefficientwise,

    B M(F(x)) C = Xi(x)+O(t), for every x in E.          (1)

Assume C is regular with rank C(0)=R and F(u) is regular. Write

    S=M(F(u)),  T=S C,  k=N-R,  rank T(0)>=r,  q=N-r,

where 1<=r<=R. If

    mu_A>2k,       nu>q,       D>d-mu_B+k,              (2)

then F and B are regular. Their constant terms give an ordinary target
restriction. In particular B(0) has full row rank and T(0) has rank R.

The first inequality alone already forces F to be regular, independently
of the value of rank T(0). This part does not assert that F(0) is injective.
The second inequality forces injectivity; the third then excludes a pole
in B. All finite Laurent pole orders are allowed.

## 2. Normalize the unit and retain its regular right inverse

Let G=B S C=I_R+O(t). It is regular invertible, so replace B by G^-1 B.
This leaves (1)'s constant tensor and the conclusion unchanged. Now

    B T=I_R exactly,                 T=S C is regular.

Over K set P=I_N-T B. Then P^2=P and rank P=k: T B is a projection
onto the R-dimensional image of T. P may have arbitrary finite poles.
It is not legitimate to specialize P itself when it is polar.

For x in E put Y=M(F(x)) C and Z=B Y, which is regular by (1). Then

    P Y=Y-T Z.                                         (3)

This identity is the regularization used below. The rank of P Y over K
is at most k. Whenever a power of t makes P Y regular, all its
(k+1)-minors still vanish after specialization. Thus any such regularized
leading coefficient has rank at most k. A raw constant coefficient of a
polar product need not have this rank; no such coefficient is used.

## 3. Exclude every first-map pole using source defect k

Suppose F has a pole of order h>0. Choose x with f=F_-h(x) nonzero.
Since C is regular, t^h Y is regular with constant term M(f) C(0).
Because T and Z are regular, t^h T Z has zero constant term. Equation
(3) shows t^h P Y is regular and

    (t^h P Y)(0)=M(f) C(0),  hence rank(M(f) C(0))<=k.

Restricting a matrix to the R-dimensional image of C(0) loses at most
k in rank. Therefore rank M(f)<=2k, contrary to mu_A>2k. F is regular.
This argument uses no inverse of S, no chosen unit-image columns and no
compressed target. It also applies when F(u)(0)=0, provided the other
hypotheses of this step hold.

## 4. Injectivity and the remaining long map

Suppose F(0)x=0. Now Y is regular and Y(0)=0. Equation (3) is regular,
with constant term -T(0) Xi(x). Consequently

    rank(T(0) Xi(x))<=k.                               (4)

For any nonzero x, Xi(x) has rank at least nu. The kernel of T(0) has
dimension at most R-r, so

    rank(T(0) Xi(x))>=nu-(R-r)>k,

where the strict inequality is precisely nu>N-r=q. Thus F(0) is
injective. This step is the only use of the unit-image rank lower bound.

If B has a pole of order s>0, the leading coefficient of (1) gives

    B_-s M(F(0)x) C(0)=0 for all x in E.

Choose a nonzero row lambda of B_-s. The map
`f -> lambda M(f) C(0)` has rank at least mu_B-k. Its kernel therefore
has dimension at most d-mu_B+k, but contains the injective D-dimensional
image F(0)E. This contradicts the last inequality of (2). B is regular.
The normalized unit equation at zero gives B(0) T(0)=I_R. Reversing the
regular normalization recovers the original regular B. Finally (1)
specializes to an ordinary restriction, as asserted.

If a nonzero target slice has rank less than mu_A-2k, the ordinary
restriction is impossible: its source lift is nonzero, while full-rank
B(0), C(0) lose at most k each. This is an additional exclusion condition,
not a consequence of the three sufficient regularity inequalities.

## 5. Canonical A4 and the exact boundary of this criterion

The prior [source calculation](../2026-10-20-koszul/cyclic_finite_target.md),
Sections 2-3, supplies, for A4 and Xi(X)=X tensor I_11,

    d=N=112, R=110, k=2, D=100, mu_A=mu_B=16, nu=11.

For r=102, q=10, the three strict margins are

    16-2*2=12,       11-10=1,       100-(112-16+2)=2.

Thus every formal degeneration with a regular full-rank C, a regular
identity lift and rank(S(0) C(0))>=102 would be ordinary. But an ordinary
source slice has target rank at least 16-4=12, whereas Xi has rank11
slices. No such degeneration exists. Transposing the slice identity gives
the symmetric assertion for a regular full-rank map on the other long leg;
the source row-contraction bound is then replaced by its equal column bound.

In particular every such regular source unit S(0) of corank at most eight
is excluded, because rank(S(0) C(0))>=110-corank S(0)>=102. Units of
higher corank may also satisfy the image hypothesis, depending on C(0).

At r=101, q=11, the injectivity margin is zero. This criterion supplies
no exclusion there: rank(T(0) Xi(x)) can equal k=2 for a nonzero target
rank-one parameter. The exact boundary control below exhibits this linear
algebra without pretending to construct an A4 degeneration. Singular
long-leg limits, unit-image ranks at most101 and polar unit lifts remain
outside the exclusion. The first-map regularity lemma still applies
without the image-rank assumption when C and the unit lift are regular.

## 6. Evidence, scope and attribution

The cyclic source, all-size minimum ranks, ordinary A4 exclusion and
previous normalized/partial-unit Laurent arguments are prior repository
work, preserved and pinned in sources.json. This continuation retains
the full regular right inverse and its rank-k projector. Only elementary
linear algebra over K and specialization of regular minors are added;
no additional external theorem or historical priority is claimed.

Finite exact controls check polar projector identities, regularization,
the source restriction rank budget, the target injectivity boundary and
source-row dimension margins. They do not enumerate all formal series,
formalize the proof or establish independent mathematical review. Neither
the full matrix target nor an exponent below9/4 is constructed.

## 7. Concurrent stronger A4 exclusion

After the first committed version c34ffcd, concurrent PR113 at08ac3e9
was inspected. Its scalar-balancing and low-rank-spanning argument with
the same regular unit-kernel correction excludes every A4 chart with
one regular full-rank long map, even for a polar original unit lift.
Thus the A4 corollary in Section5 is subsumed by that written unreviewed
result; its rank101 boundary is not an active A4 gap. The general
regularity theorem here remains distinct: it does not require a target
spanning set of low-rank slices and proves regularity of the given maps.
No independent mathematical review or historical priority is claimed.
