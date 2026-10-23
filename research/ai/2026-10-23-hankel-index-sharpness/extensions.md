# Unique maximal linear extensions of the saturated pencil

October 23, 2026. Written proof, unreviewed. Work over a field of
characteristic zero. Adopt the explicit family and complete kernels of
the [preceding proof](proof.md). This is a statement about linear Hankel
spaces containing that prescribed pencil, not about arbitrary pencils.

Fix positive integers `epsilon,p,q`, and put

    s=p+q, r=epsilon*s, a=r+p, b=r+q, d=a+b-2.

Let H(u,v) have moments `h_(r-1)=u`, `h_(r+s-1)=v`, all others zero.
Let X_r be the cone of a-by-b Hankel matrices of rank at most r.

**Theorem.** The unique inclusion-maximal vector subspace L of X_r
containing the entire pencil H is the 2epsilon-dimensional space

    h_k=0 unless k=s*j-1 for j=1,...,2epsilon.                (1)

The intersection of the Zariski tangent spaces to X_r along the pencil
is already (1), so the first-order necessary equations give the exact
answer to this linear extension problem.

## 1. Necessary equations, with no generic-only endpoint assumption

Let J belong to such an L, with moment coordinates w_0,...,w_d. At each
seed H(u,v), the left and right kernels have bases formed by shifts of

    P=sum_(k=0)^epsilon (-v)^(epsilon-k)u^k z^(s*k),

by `z^i`, `0<=i<p`, and `z^j`, `0<=j<q`, respectively. The preceding
proof establishes these bases and rank r at every projective point.

At a rank-r matrix, the first derivatives of all (r+1)-minors in
direction J vanish exactly when `x^T J y=0` for all left and right
kernel vectors. Here is the elementary justification. Choose a nonzero
rank-r minor and use invertible row and column operations to put the
matrix in block form `diag(I_r,0)`. The linear term of each bordering
(r+1)-minor is its bottom-right entry of J. Conversely, if that block
is zero, every (r+1)-minor has zero linear term. This also identifies
the determinantal tangent space before restricting to Hankel directions.

Since H+tau J belongs to L, these derivatives must vanish identically.
Expanding the two shifted kernel vectors yields

    sum_(k=0)^(2epsilon) n_k (-v)^(2epsilon-k)u^k
                          w_(s*k+i+j)=0,                    (2)
    n_k=min(k+1,2epsilon-k+1).

Indeed n_k is the number of ordered pairs between zero and epsilon
whose sum is k. The parameter monomials in (2) are independent and
each n_k is nonzero in characteristic zero. Therefore

    w_(s*k+i+j)=0                                            (3)

for every indicated k,i,j. The sums i+j fill the whole integer interval
`0,...,s-2`. Thus (3) kills precisely the intervals

    [s*k,s*k+s-2],  k=0,...,2epsilon.

In `0,...,d=(2epsilon+1)s-2`, their complement is exactly the 2epsilon
indices in (1). This proves necessity and computes the full common
tangent space. Working over the rational function field in u,v would
also suffice for necessity; no endpoint rank drop is being suppressed.

## 2. Every surviving direction integrates inside one linear space

For a Hankel matrix supported as in (1), group row indices by residue
alpha modulo s. Pair that group with column residue `s-1-alpha`.
Every entry between nonpaired groups is zero. For `alpha<p` the paired
block has epsilon+1 rows and epsilon columns. For `alpha>=p` it has
epsilon rows and epsilon+1 columns. These statements follow directly
from `a=epsilon*s+p`, `b=epsilon*s+q` and `s=p+q`.

There are s blocks, each of rank at most epsilon. Consequently every
matrix in (1) has rank at most `s*epsilon=r`. All 2epsilon moments are
free, and the original two-moment pencil belongs to this space. This
proves existence, dimension, uniqueness and the asserted tangent equality.
No higher-order compatibility assumption is needed for these directions:
the whole space, and hence every linear extension inside it, is exact.

The same residue decomposition at the original pencil gives p tall
bidiagonal singular blocks and q wide ones, after column reversal within
each block. This is a direct permutation identity over the integers,
consistent with the complete minimal-index lists in the preceding proof.

## 3. The exact four-space at A10

For `epsilon=2,p=q=2`, (1) has moments

    h_3=A, h_7=B, h_11=C, h_15=D.

Its nonzero blocks are two copies each of

    K=[[A,B],[B,C],[C,D]]

and its transpose. Thus the complete source matrix has rank
`4*rank(K)`, namely zero, four or eight. The rank-drop locus is exactly
the vanishing of all three 2-by-2 minors of K. The binary form

    (BD-C^2)Y^8+(BC-AD)X^4Y^4+(AC-B^2)X^8                    (4)

annihilates the moment sequence: its coefficients satisfy the two
identities obtained by multiplying them by `(A,B,C)` and `(B,C,D)`.
Off that rank-drop locus (4) is nonzero and is the unique degree-eight
annihilator up to scalar. Its two shifts give the full left/right kernels.
The original pencil is recovered at `(A,B,C,D)=(0,u,v,0)`.

Any linear Segre ruling whose image contains this *complete prescribed
pencil* therefore has dimension at most four, with equality attained by
the displayed four-space. A construction search that holds that pencil
fixed and tries to grow the same ruling beyond dimension four is closed.

## 4. Evidence, attribution and remaining gap

`extensions.py` checks the full common tangent operator and a permutation
decomposition of every Hankel coefficient in the declared finite range.
The separate tests reconstruct kernels from the literal seed matrices at
enough rational parameter points to recover the common tangent equations,
without using P or its predicted zero coordinates. Rank-drop controls
check the A10 four-space independently.

All general claims rest on the written proof. The prescribed family and
its preceding index-budget motivation retain their attribution. This
continuation uses only coefficient expansion, elementary determinantal
derivatives and residue permutations. No new external theorem, historical
priority, independent review or formalization is claimed.

Other saturated quadratic pencils are not classified here. It is not
proved that every such pencil is equivalent to this one under a change
preserving the Hankel source. A Segre ruling can avoid this entire seed.
The general boundary Segre-image bound, remaining ordinary targets and
singular degenerations remain open. No exponent below 9/4 follows.
