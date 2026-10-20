# A capacity obstruction beyond fixed shared-coordinate order

AI-derived written proof, 2026-10-20; unreviewed. This does not improve the
matrix exponent. It closes a precise perfect-dimension coordinate ansatz
at all m>=10, including arbitrary permutations of the shared coordinates.
It does not exclude asymptotic overhead 1+o(1), arbitrary input mixing, or
general Laurent families.

## Statement and scope

Let N=m(m+1)/2. For m>=10, there is no degeneration C(m,N) to the canonical
T_m of the following form: permute the two source input coordinate bases,
use coefficient-one input maps, apply any constant output linear map, and
apply diagonal integer weights on the resulting target coordinates.

The shared permutation can be arbitrary, beyond the fixed polynomial-space
action covered by the concurrent catalecticant obstruction. Output rows may
sum several source coordinates. More general constant input matrices are
not covered. The argument permits arbitrary diagonal weights, provided the
target really is the leading tensor.

## 1. Active source output sets must be disjoint

Write x_p for the source X index selected for target X_p, and y_(u,a) for
the source Y index selected for degree-sector u, 0<=a<u. These maps are
permutations of m and N coordinates. The desired coefficient at output
(u,c), 0<=c<v=m+1-u, comes from source output index

    y_(u,a)+x_(a+c),   0<=a<u.

Let S_(u,c) be the set of these indices. They must have nonzero coefficients
in that output row. No S sets for distinct target output rows can overlap.
Indeed, if a source index supports wanted terms in rows z and z', let the
input weight sums of those terms be g and g'. Desired leading terms give
g+w_z=g'+w_z'=0. Their appearances in the other output rows must not have
negative weights, so g+w_z'>=0 and g'+w_z>=0. The two inequalities force
w_z=w_z'. Both cross terms would then survive at weight zero. Each target
input pair has exactly one desired output, a contradiction. Nonzero output
coefficients cannot cancel: each selected input pair has exactly one source
output. Unused source coefficients in an output row can be removed.

There are N output rows, each using at least one source coordinate, within
a source output space of dimension N+m-1. Hence the total excess satisfies

    E = sum_(u,c) (|S_(u,c)|-1) <= m-1.                 (1)

## 2. Repetition of difference windows

Put d_p=x_(p+1)-x_p, a word of length n=m-1. If |S_(u,c)|=1, successive
desired sums are equal, so

    (d_c,...,d_(c+u-2))

is the fixed word -(y_(u,a+1)-y_(u,a))_(a=0,...,u-2), independent of c.
Let M_l be the maximum multiplicity of a length-l consecutive word in d.
For u>=2, at most M_(u-1) of its v=m+1-u output rows can use a singleton.
Every other row contributes at least one excess. Therefore

    E >= R(d) := sum_(l=1)^n (n-l+1-M_l).               (2)

**Word-gap lemma.** For n>=5, a word that is neither constant nor constant
apart from one endpoint satisfies R(d)>=2n-4.

For 2<=l<=n-3 there are v=n-l+1>=4 windows. If v-1 windows were identical,
two starts would be consecutive; the repeated window would be constant.
Those v-1 intervals cover the whole word except possibly a single endpoint,
because their gaps are at most two and l>=2. This would be one of the
excluded word forms. Thus the deficit in each such length is at least two.
The deficits at lengths n-2 and n-1 are at least one for any nonconstant
word. If the length-one deficit is at least two, their sum is at least
2+2(n-4)+1+1=2n-4. Otherwise the word has precisely one exceptional letter,
at an interior position. Its three length-(n-2) windows are distinct, giving
deficit two there and the same lower bound 1+2(n-4)+2+1.

For m>=6, equations (1)-(2) exclude all these words, since 2m-6>m-1.
Thus d must be constant or constant apart from an endpoint. Since x is a
permutation of 0,...,m-1, its arithmetic run of length m-1 has step +1 or
-1. The only possibilities are the two affine permutations and the four
permutations obtained by moving one endpoint to the opposite end of a
monotone list. This classification follows from the proof, not enumeration.

## 3. Affine and endpoint cases

For the affine permutations, the concurrent fixed-shared-basis catalecticant
obstruction (`6bdab15`, source_obstructions.md, section 2) gives

    N >= N+floor((m-1)^2/4)-floor((m-1)/2),

which is impossible for m>=4. Its first-leg action hypothesis is satisfied:
weight-zero target coefficients in the u=2 sector force the X weights to
be an arithmetic progression, an induced polynomial-variable scaling.
The input coordinate maps here have coefficient one. Source reflection
handles the reversed affine order.

For an endpoint permutation, reflect the source indices and/or reverse the
target degree coordinates inside every sector. These operations preserve
the active-set disjointness problem. After an irrelevant translation of
source X indices, use

    x_p=p for p<m-1,  x_(m-1)=-1.

Every sector 2<=u<=m-1 has repetition lower bound one. Their total is m-2,
leaving at most one additional excess in (1). For 2<=u<=m-3, we have v>=4.
All but the last of its difference windows are the constant word 1; only
the last window contains the endpoint jump. Unless y_(u,a)=K_u-a, at most
that last window can give a singleton, causing at least v-1>=3 excesses.
This would exceed the available extra one. Consequently all m-4 sectors
u=2,...,m-3 have Y interval

    [L_u,L_u+u-1],   L_u=K_u-u+1.

Their active output sets together contain the interval
[L_u+u-1,L_u+m-1] and the additional point L_u-1. For two such Y intervals
in source order, L_w>=L_u+u by input injectivity. The next sector's output
point L_w-1 must avoid the previous sector's output interval, forcing

    L_w >= L_u+m+1.

There are m-4 such intervals. Their first start is nonnegative and the last
has length at least two. Thus the N-coordinate source Y space must satisfy

    N >= (m-5)(m+1)+2 = m^2-4m-3.                       (3)

For m>=10 this contradicts N=m(m+1)/2. This completes the stated obstruction.

## What it leaves open

The proof requires B=N exactly. The conclusion does not rule out
B=N+O(m), which would still have limiting overhead one, or a construction
using a larger short input. Constant input mixing can introduce cancellation
between several source contributions to one target input pair; section 1
does not apply to it. It is therefore neither a rejection of the general
mixed-target premise nor an exponent improvement.

`collision_combinatorics.py` implements (2) and the finite filters. Tests
check the word-gap lemma on short binary/ternary words and the permutation
classification through m=8. The all-size claims rely on this written proof.
