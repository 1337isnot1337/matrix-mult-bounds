# Exclude the first four singular long-leg defects for A4

October 23, 2026. Written, unreviewed, owner-directed OpenAI Codex work.
No independent mathematical review, formalization or exponent improvement.

## 1. Statement

There is no complex formal degeneration from the canonical cyclic source
A4 to M(10,10,11) if either long map is regular and its constant matrix
has rank at least 106. The first map and the other long map can have
arbitrary finite Laurent poles. There is no assumption on the lift of
the target identity.

Equivalently, in every remaining candidate, both long maps have rank at
most 105 after scalar balancing. Scalar balancing multiplies a map by a
power of t so that its minimum entry valuation is zero, and compensates
by the inverse scalar on another map. It does not use a singular source
frame change.

This result extends the full-rank long-leg obstruction in
[PR113, commit 08ac3e9](https://github.com/1337isnot1337/matrix-mult-bounds/blob/08ac3e983e270cf3df4e26d960ceb16415f7ef31/research/ai/2026-10-23-one-regular-leg/proof.md).
The proof below repeats its unit-kernel identity with credit, then uses
the maintained source rank gap and the geometry of a target rank-one
ruling. No construction or bound below 9/4 follows.

## 2. A regular correction with a singular column map

Set O=C[[t]] and K=C((t)). Suppose a complete degeneration has the form

    B(t) M(F(t)(X)) C(t) = X tensor I_11 + O(t),
    X in Mat_10(C).

Here the source slice map M takes 112 parameters to 112-by-112 matrices,
B has size 110-by-112, and C has size 112-by-110. Assume C is regular
with rank C(0)=110-c, where 0<=c<=4. Its generic rank is 110: the target
unit equation forces that rank even though the constant matrix is singular.

Let m be the minimum entry valuation of F. Replace F by t^(-m)F and B
by t^m B. The complete tensor output is unchanged. Now F is regular
and its constant linear map F_0 is nonzero.

Write

    Y_X=M(F(X)) C,       D=Y_I,       G=B D=I_110+O(t).

Both Y_X and D are regular. Replace B by G^(-1)B. This preserves every
target constant term and makes B D=I_110 exactly. Put

    Z_X=B Y_X,       W_X=Y_X-D Z_X=(I_112-D B)Y_X.

Over K, the projection I_112-D B has image ker B and rank two. Therefore
rank_K W_X<=2. The expression Y_X-D Z_X proves W_X is regular, including
when B or the projection has poles. Specializing its vanishing 3-by-3
minors gives

    M(F_0(X)) C_0 = D_0 (X tensor I_11)+W_X(0),
    rank W_X(0)<=2.                                      (1)

This is the unit-kernel argument of PR113. Full rank of C_0 was not used
in obtaining (1). Its only new loss below is the codimension 2+c.

## 3. Source rank gap and a linear-space bound

The maintained [minimum-rank classification](../2026-10-20-koszul/cyclic_finite_target.md),
Sections 2 and 4, and [rank-gap theorem](../2026-10-20-anisotropic-constructions/slice_rank_gap.md),
Sections 1-2, give the following facts over C:

1. Every nonzero A4 slice has rank 16 or rank at least 20.
2. Every rank-16 parameter is a pure tensor u tensor h tensor v in
   C^4 tensor C^7 tensor C^4. Its middle Hankel matrix also has rank one.

In particular, a linear subspace of parameters whose every nonzero
element has source rank 16 has dimension at most seven. The following
elementary argument uses only pure-tensor containment, so it does not
need the stronger condition on h.

A linear subspace of rank-at-most-one matrices has a common left factor
or a common right factor. Indeed, fix a nonzero a tensor b. A second
rank-one matrix must share a factor with it, since the sum of two pure
matrices with independent left and right factors has rank two. If one
element varies the left factor and another varies the right factor,
their sum has rank two. Thus both types of variation cannot occur.

Apply this observation first to the flattening C^4 tensor C^28. A common
right factor bounds the dimension by four. Otherwise there is a common
left factor, and the remaining subspace lies in C^7 tensor C^4 with
every nonzero element still rank one. The same observation bounds its
dimension by max(7,4)=7. Consequently

    no ten-dimensional linear subspace lies in the rank-16 source cone.
                                                               (2)

The dimension bound seven is sufficient here; no optimal linear-space
classification for the Hankel-restricted cone is claimed.

## 4. A nonzero target ruling would produce a forbidden ten-plane

Write a nonzero rank-one target parameter as X=a b^T, with a,b in C^10.
By (1), and because multiplication by C_0 loses at most 2+c source ranks,

    rank M(F_0(a b^T))
      <= rank(D_0 ((a b^T) tensor I_11))+2+(2+c)
      <= 15+c < 20.                                      (3)

If F_0(a b^T) is nonzero, the source rank gap forces its rank to be 16.
The same identity then gives

    rank(D_0 ((a b^T) tensor I_11)) >= 16-(2+c)-2
                                                    =12-c>2.    (4)

Fix a for which F_0(a b^T) is nonzero for at least one b. Such an a
exists if F_0 is nonzero, because rank-one matrices span Mat_10(C).
For every nonzero b,

    (a b^T) tensor I_11=(a tensor I_11)(b^T tensor I_11),

and b^T tensor I_11 is surjective. Therefore

    rank(D_0 ((a b^T) tensor I_11))
                     =rank(D_0(a tensor I_11)),            (5)

which is independent of b. It exceeds two by the active choice and (4).
If F_0(a b^T) vanished for any other nonzero b, (1) would express that
same matrix as -W_(a b^T)(0), whose rank is at most two. This is impossible.

Thus the linear map b |-> F_0(a b^T) is injective on C^10. Every nonzero
element of its image has source rank 16, by (3). This gives the forbidden
ten-plane from (2). Hence F_0 must be zero, contradicting scalar balancing.

The proof applies after exchanging the two long legs. For a Laurent
long map, first make its minimum entry valuation zero by a scalar and
compensate in F. If the resulting constant rank were at least 106,
the theorem would apply. This proves the statement in Section 1.

## 5. General form of the argument

The same argument applies to Xi(X)=X tensor I_n for X in Mat_m(C),
with source size N, target size R=mn, and k=N-R. Assume:

* every nonzero source slice has rank mu or rank at least mu+delta;
* the rank-mu parameter cone contains no m-dimensional linear subspace;
* C is regular with rank C_0=R-c;
* n+2k+c < mu+delta and mu-2k-c > k.

Then no complete Laurent degeneration exists. The correction has rank
at most k. Rank-one target lifts have rank at most n+2k+c, so every
nonzero one has rank mu. An active ruling has image rank at least
mu-2k-c>k, forcing injectivity along that entire m-dimensional ruling.
This contradicts the source linear-space hypothesis.

For A4 the data are

    (N,R,m,n,k,mu,delta)=(112,110,10,11,2,16,4).

At c=4 the two strict margins are

    20-(11+4+4)=1,       (16-4-4)-2=6.

At c=5, the first margin is zero: lifted slices can have rank 20.
There are actual A4 slices of rank 20, for example the parameter with
F_(0,0,0)=F_(1,0,1)=1 and all other coefficients zero. The verifier
reconstructs this slice and computes its exact rational rank. Thus this
proof makes no claim at long-map rank 105. Classifying linear spaces
of source rank at most 20 is a distinct next question.

## 6. Evidence and attribution

The source rank minimum, pure-tensor minimum locus, and gap above rank16
are prior repository results, pinned in sources.json. The rank-gap proof
retains its stated use of Grothendieck's splitting theorem on P^1. This
continuation adds no external theorem. PR113 supplies the regular
unit-kernel correction and scalar balancing. The new step is the
active-ruling injectivity argument and its use of the existing rank gap
to handle four singular leading-rank defects.

The exact controls reconstruct minimum and rank20 source slices, check
rank preservation under the ruling's surjective right factor, verify
isolated sharp singular-column rank budgets, and record the strict
thresholds. Those finite controls do not prove the all-series theorem.
The written proof remains unreviewed. Both scalar-balanced long maps
of ranks at most105, the full matrix target, and an exponent improvement
remain open.
