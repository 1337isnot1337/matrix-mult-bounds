# The source rank gap forces a normalized long-rank sum of at most 204

October 23, 2026. Owner-directed OpenAI Codex continuation.
Written and unreviewed. No smaller matrix multiplication exponent.

Claim `AI-A4-GAP-LONG-RANK-SUM-004`.

## Statement and dependencies

Consider a complex formal Laurent degeneration from A4 to M(10,10,11).
Independently divide each long map by the smallest valuation of its entries.
Compensate for both scalar factors in the first map.
The two long maps are then regular and have nonzero constant terms.
Let their constant ranks be r_B and r_C.

The necessary condition is

    r_B + r_C <= 204.

This improves the elementary bound 208 by importing the existing source rank gap.
It concerns this scalar normalization. Singular matrix changes of basis can
change the leading ranks and are not treated as rank-preserving operations.

The proof uses three credited ingredients:

- Every nonzero A4 slice has rank 16 or rank at least 20.
- The rank-16 parameters are exactly u tensor h tensor v, where u and v
  belong to C^4 and h lies on the degree-six rational normal curve.
- The regular kernel residual for the other long map has rank at most two.

The first ingredient is proved in
`research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md`,
at immutable commit `8722b361fde7713949b8f0e72fab681066ce10bd`.
Its SHA-256 is
`43c90e01de6d87ee56b733eb332829b0cbec839ea331f7063fc5f5a5515eea71`.
That proof imports the splitting theorem for vector bundles on the projective line.
This note adopts its proof status and original attribution.
The classification also appears in the maintained cyclic-source note, Section 4.
The kernel residual retains the concurrent PR113 credit recorded in `proof.md`.

## 1. Linear spaces in the minimum-rank locus have dimension at most four

Let L be a linear subspace of the A4 parameter space.
Suppose every nonzero parameter in L gives a source slice of rank 16.
The classification writes each nonzero parameter as

    u tensor h(alpha,beta) tensor v,
    h(alpha,beta)_k = alpha^(6-k) beta^k,

with nonzero u and v in C^4.

First, all members of L have the same projective middle factor h.
To see this, take two members and group the outer factors together.
The sum of two simple tensors is simple only if one pair of factors is
proportional. If their middle factors differ, their outer tensor factors
must therefore be proportional. The whole projective line between their
middle factors would then belong to the rational normal curve.

That curve contains no projective line. For a direct check, move the two
distinct projective binary points to (1,0) and (0,1) by an invertible
change of variables. The sum of their degree-six pure powers has nonzero
extreme coefficients and zero interior coefficients. It is not a pure
power, since a pure power with both extreme coefficients nonzero has
nonzero interior coefficients over C. This gives the required contradiction.

After fixing h, identify L with a linear subspace of C^4 tensor C^4
whose nonzero members have matrix rank one. Choose u0 tensor v0 in it.
Every other member must have its first factor proportional to u0 or its
second factor proportional to v0. Otherwise its sum with u0 tensor v0
would have matrix rank two.

Thus L lies in the union of u0 tensor C^4 and C^4 tensor v0.
A linear subspace cannot be the union of two proper linear subspaces.
For example, the sum of a vector outside the first and a vector outside
the second lies outside both when each vector lies in the other subspace.
Consequently L lies in one ruling, and

    dim L <= 4.                                            (1)

## 2. The leading polar coefficient lies in that minimum locus

Write the normalized complete identity as

    B(t) M(F(t)(X)) C(t) = Xi(X) + O(t),
    Xi(X) = X tensor I_11,       X in Mat_10.

Both B and C are regular. Their sizes are 110 by 112 and 112 by 110.
Suppose, for a contradiction, that

    r_B + r_C >= 205.                                      (2)

The map F must have a pole. Otherwise the constant coefficient would
be an ordinary restriction from A4 to the target, which the maintained
ordinary obstruction excludes.

Let h>0 be the pole order of F and set F_hat=t^h F.
Then F_hat is regular and F0=F_hat(0) is a nonzero linear map.
The coefficient of t^(-h) in the complete identity is

    B0 M(F0(X)) C0 = 0       for every X.                  (3)

The elementary restriction bound gives

    rank M(F0(X)) <= (112-r_B)+(112-r_C) <= 19.            (4)

Every nonzero F0(X) therefore has source rank 16 by the credited rank gap.
The entire linear image of F0 lies in the minimum-rank cone.
Equation (1) gives rank F0 <= 4. Hence

    dim ker F0 >= 96.                                     (5)

A subspace of Mat_10 consisting entirely of singular matrices has dimension
at most 90. The self-contained square-matrix proof is given in
`corank_one.md`, Section 3. Thus there is an invertible matrix X in ker F0.

## 3. The regular residual contradicts the invertible kernel element

Transpose the complete identity if necessary, and use X^T as target parameter.
We may therefore arrange r_C >= r_B without changing any rank or image
dimension used above. Equation (2) gives

    r_C >= 103.                                          (6)

Replace F by F_hat and B by t^(-h)B. Their scalar factors cancel.
The map C remains regular with the same constant rank r_C.
Choose an invertible V with F0(V) nonzero. Such a V exists because the
invertible matrices form a dense open set and F0 is nonzero.

Put H=Xi(V)^(-1), S=M(F_hat(V)), and D=S C H.
The complete identity makes G=B D regular with G(0)=I_110.
Replace B by G^(-1)B. Then B D=I_110 exactly, while the target constant
tensor remains Xi. Put T_X=B M(F_hat(X)) C.

For each X, the regular matrix

    W_X = M(F_hat(X)) C - D T_X

has columns in the two-dimensional kernel of B over C((t)).
Its three-by-three minors vanish before and after specialization, so

    rank W_X(0) <= 2,
    M(F0(X)) C0 = D0 Xi(X) + W_X(0).                     (7)

The nonzero source slice M(F0(V)) has rank 16.
Restriction by C0 loses at most 112-r_C ranks.
Since H is invertible, equations (6) and (7) give

    rank D0 >= 16-(112-r_C) = r_C-96 >= 7.               (8)

For the invertible X in ker F0, equation (7) instead gives

    D0 Xi(X) = -W_X(0).

The left side has rank rank D0, and the right side has rank at most two.
This contradicts (8) and proves r_B+r_C<=204.

## Scope

The bound holds for every finite Laurent order after the stated independent
scalar normalizations. It does not exclude equality at 204 or construct a
degeneration below that boundary. It imports the existing complex source
rank gap; no characteristic-independent rank-gap statement is made.

This proof is separate from the sharp minimum-rank-six result for PR103's
fixed resolvent. It does not use that certificate. The new contribution
here is the use of the credited rank gap and regular residual to improve
the normalized rank-sum constraint. No independent mathematical review,
formalization, or improved exponent is claimed.
