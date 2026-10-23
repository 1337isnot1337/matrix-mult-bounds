# A full-rank regular long leg preserves the ordinary rank obstruction

October 23, 2026. Owner-directed OpenAI Codex work.
Written and unreviewed. No smaller matrix multiplication exponent.

## Concurrent predecessor and present scope

The kernel-residual proof and its full-rank A4 consequence are already
recorded in [PR113](https://github.com/1337isnot1337/matrix-mult-bounds/pull/113),
at commit `08ac3e983e270cf3df4e26d960ceb16415f7ef31`. Its claims
`AI-UNIT-KERNEL-LOW-RANK-001` and `AI-A4-ONE-REGULAR-LEG-002` retain their
credit. This session independently reached the same argument before
inspecting that checkpoint; it is not registered here as a new A4 claim.

The rectangular statement below is supplied as a self-contained version
of the same mechanism. The new A4 continuation is the
[rank-109 long-map exclusion](corank_one.md), together with the final
normalized leading-rank bound in this note.

## General theorem

Let O=C[[t]] and K=C((t)). Let

    M:A -> Mat_(N_B,N_C)(C)

be a source slice map. Every nonzero source slice has matrix rank at
least mu. Let

    Xi:E -> Mat_(R_B,R_C)(C)

be a nonzero target slice map. Suppose:

1. Xi(v) has full row rank R_B for some v in E.
2. E is spanned by elements x whose target slice rank is at most rho.
3. Laurent maps F:E -> A, B of size R_B by N_B, and C of size N_C
   by R_C satisfy the complete tensor identity

       B(t) M(F(t)(x)) C(t) = Xi(x) + O(t), for every x in E.

4. C is regular and C(0) has full column rank R_C.

Put k_B=N_B-R_B and k_C=N_C-R_C. If

    mu > rho + k_B + k_C,

then no such Laurent maps exist.

The conclusion allows arbitrary finite Laurent poles in B and F. No
rank assumption is made on a limiting source lift of v. Source and
target matrix dimensions may differ on the two long legs. The full-row
target slice is required; in particular R_B<=R_C.

## Proof

### 1. Normalize only a scalar valuation on the first map

The Laurent map F is nonzero because the target is nonzero. Let m be the
smallest t-adic valuation of its nonzero entries. Replace

    F by t^(-m) F, and B by t^m B.

The complete tensor identity is unchanged. Now F is regular and F(0)
is a nonzero linear map. C is unchanged and remains regular with full
column rank at zero. This scalar normalization works whether m is
positive, zero, or negative.

Set S=M(F(v)). The matrix S is regular. It can vanish at zero; it need
not be invertible, or have any specified rank there.

### 2. Produce a regular right inverse of the Laurent row map

Choose a constant R_C-by-R_B matrix H such that Xi(v) H=I_(R_B).
The matrix

    G(t)=B(t) S(t) C(t) H

is I_(R_B)+O(t), so G and its inverse are regular. Replace B by G^(-1)B.
This preserves the target constant tensor. Define

    D(t)=S(t) C(t) H,
    T_x(t)=B(t) M(F(t)(x)) C(t).

Then D and every T_x are regular, B D=I_(R_B) exactly, and
T_x(0)=Xi(x). Consequently B has row rank R_B over K, and its kernel
over K has dimension k_B.

### 3. Use the kernel residual before specializing

For each fixed x in E, define

    W_x(t)=M(F(t)(x)) C(t)-D(t) T_x(t).

Every term is regular. The exact identity B D=I gives B W_x=0.
Every column of W_x therefore belongs to ker_K B, and

    rank_K W_x <= k_B.

All (k_B+1)-minors of W_x vanish over K. Since W_x is regular, those
minors also vanish at zero. Thus

    rank W_x(0) <= k_B.

Regularity is essential here. A raw constant coefficient of a Laurent
matrix with remaining poles need not satisfy its generic rank bound.

At zero the residual identity gives

    M(F(0)(x)) C(0)=D(0) Xi(x)+W_x(0).

Since C(0) has full column rank R_C, restricting columns loses at most
k_C in matrix rank. Therefore

    rank M(F(0)(x))
      <= rank(M(F(0)(x)) C(0)) + k_C
      <= rank Xi(x) + k_B + k_C.

For every spanning element with rank Xi(x)<=rho, a nonzero F(0)(x)
would contradict the source minimum mu. Hence F(0) kills a spanning
set of E and is zero. This contradicts the scalar normalization.

The argument concerns every finite Laurent order. It uses no finite-jet
extrapolation, numerical optimization, inverse of a singular source unit,
or injectivity assumption on F(0).

## A4 consequence

Use the previously proved source minimum from
[the source minimum-rank proof](../2026-10-20-koszul/cyclic_finite_target.md), Sections 2-3:

    N_B=N_C=112, mu=16.

For M(10,10,11), take E=Mat_10 and Xi(X)=X tensor I_11. The two long
dimensions are R_B=R_C=110. The identity matrix supplies the full-rank
target slice. The 100 matrix units span E, and each has target slice
rank rho=11. Thus

    rho+k_B+k_C=11+2+2=15<16=mu.

No degeneration A4 -> M(10,10,11) can have either long map regular
with full-rank limit. Transpose the slice identity to obtain the other
long-leg statement.

This includes regular unit-image ranks 109, 108, 102, 16, and zero.
There is no unit-image threshold. In particular the older regular-unit
and partial-unit-image charts are special cases of the new obstruction.

The [rank-109 extension](corank_one.md) below strengthens this boundary.
General degenerations with more singular long-map limits remain open.
No smaller exponent is established.

## Boundaries and attribution

The source minimum and ordinary one-rank gap retain their original
repository credit. The scalar normalization and regular kernel residual retain the
concurrent PR113 credit above. The present new contribution is the
rank-109 equality analysis and the normalized leading-rank consequence. The proof uses only elementary
matrix rank, a constant right inverse, and specialization of vanishing
minors. No additional external theorem is imported.

The rank bound is non-strict before the source comparison. At equality
mu=rho+k_B+k_C the argument gives no contradiction. A singular C(0)
would replace k_C by N_C-rank C(0), which can remove the A4 gap. These
are limits of the proof, not constructions in the remaining cases.


## Simultaneously normalized long-map ranks

Claim `AI-A4-NORMALIZED-LONG-RANK-SUM-002` concerns a specified scalar
normalization, not an arbitrary Smith basis change. For a nonzero
Laurent matrix Q, let v(Q) be the smallest valuation of its nonzero
entries. For the two long maps set

    B_reg=t^(-v(B)) B,       C_reg=t^(-v(C)) C,
    F_reg=t^(v(B)+v(C)) F.

The complete tensor identity is unchanged. Both long maps are regular
with nonzero constant terms. Write r_B=rank B_reg(0) and
r_C=rank C_reg(0). Each lies between 1 and 110.

Suppose r_B+r_C>208. If F_reg has a pole of order h>0, choose a target
parameter X with nonzero leading source coefficient f. The coefficient
of t^(-h) in the tensor identity is

    B_reg(0) M(f) C_reg(0)=0.

Deleting source rows and columns loses at most
(112-r_B)+(112-r_C) ranks. Consequently

    rank M(f)<=224-r_B-r_C<16,

contrary to the source minimum. Thus F_reg is regular. The target limit
is now an ordinary restriction. Its long-leg flattening ranks are 110,
so both limiting long maps must have rank 110. The prior ordinary A4
rank obstruction excludes that case as well. It follows that every
remaining degeneration satisfies

    r_B+r_C<=208.

The [rank-109 theorem](corank_one.md) additionally gives

    r_B<=108,         r_C<=108.

The pair (109,109) is therefore excluded already by the leading-pole
argument: its source rank budget is six, below sixteen. These necessary
conditions do not construct any surviving pair. Equality at a rank sum
of 208 remains outside this elementary leading-pole contradiction.

Only independent scalar valuations are normalized here. Source or target
basis changes with singular limits can change the leading ranks and are
not treated as harmless gauge transformations.
