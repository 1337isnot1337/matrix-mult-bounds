# The mixed target needs a genuine degeneration

2026-10-20. AI-derived written rank argument, unreviewed and not Lean
formalized. No improvement of the matrix exponent is established.

Coordination: the fresh remote review found the same canonical exact-
restriction argument in concurrent commit `d2d505c`, and the equivariant
linear-flattening barrier below in the more general polynomial-matrix
argument of `6bdab15`. These independently rediscovered arguments are retained
for local verification and are not counted as distinct theorem progress.
The new executable experiment here permits arbitrary shared-coordinate
permutations and output-coordinate collisions. Its scope and exact witnesses
are in [README.md](README.md).

## The precise open construction

The concurrent Koszul branch, commit `292ba18`, defines T_m with shared
dimension m and two other dimensions N=m(m+1)/2. Its matched sectors are
C(u,m+1-u), 1<=u<=m, with a canonical common output basis. It constructs a
border-rank-N certificate and proves a conditional improvement if
C(m,B_m) degenerates to k_m copies of this target with B_m/(k_m N)
asymptotically below about 1.02047. That target and conditional implication
are the other worker's results. This note investigates what the construction
must do; it does not supply the missing degeneration.

## 1. A lower bound for arbitrary ordinary linear restrictions

Put D=m-1 and T_(m,k)=T_m tensor B_X(k). Suppose C(m,B) restricts to this
target by arbitrary independent linear maps on its three legs. Then

    B >= max(kN, 2kN-D-km).                              (1)

This allows arbitrary changes of basis and noninvertible leg maps, but not
a parameter-dependent limit. In particular, along unbounded m and any
positive k_m, an ordinary-restriction construction must have

    liminf B_m/(k_m N) >= 2.                             (2)

It therefore cannot satisfy the concurrent low-overhead criterion.

### Proof

For every nonzero first-input vector f, the C(m,B) slice is multiplication
by the nonzero polynomial f on polynomials of degree below B. Over C[x]
this is injective, so the slice has rank B.

The target is concise on all its three legs. Hence a restriction producing
it must have an invertible map on the m-dimensional shared leg and full-rank
maps to the kN-dimensional other legs. Pull a nonzero target first-leg
contraction back to a nonzero source f. Restricting the source slice to a
kN-dimensional input subspace leaves rank kN. The output projection has
kernel dimension B+D-kN, so the resulting matrix has rank at least

    kN-(B+D-kN)=2kN-B-D.                                 (3)

The minimum nonzero slice rank of canonical T_m is exactly m. In its u-th
sector a contracted matrix is the u by (m+1-u) Hankel matrix with entries
f_(a+c). Every coefficient f_0,...,f_D occurs in that matrix, so every
nonzero f makes each sector nonzero and of rank at least one. Their other
leg spaces are disjoint, so ranks add. Taking f=(1,0,...,0) gives rank one
in every sector, attaining total m. Thus T_(m,k) has minimum slice rank km.
Substitute that contraction in (3), obtaining (1). Dimension monotonicity
gives the other bound kN. Finally m/N and D/(kN) tend to zero, proving (2).

This is a standard matrix-rank argument applied to the mixed target, not a
new general theorem about tensor rank. In particular, (1) does not assert
that the exact rank of T_m is m^2.

## 2. Even independent sector bases do not rescue exact restrictions

If each sector's shared output is identified independently with the common
m-space, the minimum rank km need not still be simultaneously attained.
Nevertheless every slice has rank at most

    k R_m,  R_m=sum_(u=1)^m min(u,m+1-u)=floor((m+1)^2/4).

Applying (3) to any nonzero contraction therefore gives

    B >= max(kN, 2kN-D-kR_m).                            (4)

Its asymptotic overhead is at least 3/2. This conclusion holds without
assuming the canonical border-rank-N construction survives those independent
identifications. It is a necessary restriction bound for that whole target
format.

For m=4,k=1, the canonical lower bound is B>=13; the independent-basis bound
is B>=11. For m=53,k=1, the canonical bound is B>=2757 whereas N=1431.
These are not lower bounds for arbitrary degenerations. Rank drops in a
singular limit are precisely what an actual low-overhead construction needs.

## 3. Algebra-cover comparison, with its limit

Let A=C[[s,t]]/(s,t)^m. Its length is N and its socle dimension is m.
Ananthnarayan, *Computing Gorenstein Colength*, arXiv:0810.4542v3,
Theorem 3.1, gives

    g(A)=length(C[[s,t]]/(s,t)^(m-1))=m(m-1)/2.

Thus a Gorenstein local algebra mapping onto A has length at least m^2,
and this minimum is attained by the cited theorem. This rules out obtaining
the desired near-N source cost through an actual small Gorenstein algebra
quotient cover.

It does not rule out a tensor degeneration or even a flat family whose
generic fiber is Gorenstein: Gorensteinness can be lost under specialization.
Nor has a general tensor restriction been proved to induce such an algebra
quotient. Smoothability of A alone does not control the short convolution
leg. Those bridges remain unproved and must not be inferred from this
comparison.

## 4. Why every shared-leg equivariant linear flattening passes

This is broader than the full-space Koszul calculations. Let U,V be
finite-dimensional GL(X) representations and L:X -> Hom(U,V) a nonzero
equivariant linear map. For T in X tensor Y tensor Z form the matrix
F(T):Y* tensor U -> Z tensor V by replacing x with L(x). Shared-leg
Young/Pieri flattenings have this form. Put kappa=rank L(x) for nonzero x;
equivariance makes kappa constant on that orbit.

Every nonzero C(m,B) first-input slice has rank B. Project X onto a
nonzero line to obtain x tensor M with rank(M)=B. A projection is a limit
of invertible first-leg maps. Equivariance preserves matrix rank along
those invertible maps; rank cannot increase at their limit. Since

    rank F(x tensor M)=rank(M) rank L(x)=B kappa,

we have rank F(C(m,B))>=B kappa. For every target of border rank at most B,
linearity, the rank-one bound kappa and closedness of matrix-rank conditions
give rank F(target)<=B kappa. No flattening in this class can reject the
target. This applies to canonical T_(m,k) at B=kN.

The argument remains valid after projecting X to any positive dimension:
an injective dual map selects a nonzero polynomial subspace, and every
selected nonzero polynomial still multiplies injectively on the B-space.
Use the representations and rank-one constant for the new projected format.
Projecting the shared leg before taking these flattenings therefore cannot
resolve the construction either.

This does not cover nonshared-leg projections, nonlinear invariant equations,
or functors that involve several legs differently. It does not construct a
degeneration. It explains why enlarging only the shared-leg Koszul list
cannot decide this particular low-border-rank target problem.

## Active next step

The source-rank and Gorenstein-cover shortcuts cannot furnish the needed
ordinary map. Investigate a true Laurent-parameter family or a suitable
global invariant, retaining the m-dimensional short-leg constraint.
Small finite restrictions are not evidence that the asymptotic construction
exists; ordinary numerical fitting with bounded matrices cannot solve it.

The executable checks source and target slice ranks at explicit small
parameters and records the exact formulas for larger sizes. The universal
claims rely on the proof, not those finite checks.
