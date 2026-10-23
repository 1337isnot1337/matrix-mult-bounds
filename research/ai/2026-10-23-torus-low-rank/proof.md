# A sharp linear-space bound below A4 slice rank 24

October 23, 2026. Written, unreviewed, owner-directed OpenAI Codex work.
No independent mathematical review, formalization or exponent improvement.

## 1. Results

Let M be the maintained canonical A4 slice map, with parameter space
C^4 tensor C^7 tensor C^4 and matrix size 112. Then

    max {dim V : V is linear and rank M(f)<=23 for every f in V}=8.
                                                               (1)

The subspaces V in (1) are arbitrary complex subspaces. There is no
coordinate, homogeneity or fixed-basis hypothesis on V.

Consequently, no complete Laurent degeneration A4 to M(10,10,11) has a
regular long map whose limiting rank is at least 102. After separately
scalar-balancing the two long maps, both constant ranks in any remaining
candidate are at most 101. The other maps can have arbitrary finite poles.

The first result is a source linear-space theorem. The second combines
it with the unit-kernel correction of
[PR 113 at 08ac3e9](https://github.com/1337isnot1337/matrix-mult-bounds/blob/08ac3e983e270cf3df4e26d960ceb16415f7ef31/research/ai/2026-10-23-one-regular-leg/proof.md)
and the active-ruling argument of the preceding
[singular-long-rank note](../2026-10-23-singular-long-rank/proof.md).
No improving matrix target is constructed.

## 2. A rank-preserving diagonal action

Use the source coordinates from the pinned
[canonical source note](../2026-10-20-koszul/cyclic_finite_target.md):

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),

where j,p,q,r run from 0 to 3, H,L run from 0 to 6, and out-of-range
parameter indices contribute zero. Define a diagonal parameter map

    D(t) F_(i,k,s)=t^(i+4k+28s) F_(i,k,s).

Its 112 weights are exactly 0,...,111, with no repetition. For t nonzero,

    M(D(t)F)_((j,p,L),(H,q,r))
       = t^(-j+4p+28L) M(F)_((j,p,L),(H,q,r))
                           t^(H+4q-28r).                 (2)

The left and right diagonal matrices are invertible. Thus D(t) preserves
the rank of every source slice. Negative weights on those matrix legs
cause no problem; only t nonzero is used in this assertion.

## 3. Every bounded-rank subspace has a coordinate specialization

Let V have dimension d, and assume every slice in V has rank at most q.
Order the parameter coordinates by the distinct weights in Section 2.
Put a basis of V in reduced row-echelon form for that ordering. Write
its vectors as v_1,...,v_d, with distinct pivot coordinates p_1,...,p_d.
All nonpivot nonzero coordinates of v_j occur after p_j. The vectors

    w_j(t)=t^(-weight(p_j)) D(t)v_j

are therefore polynomial in t, and w_j(0) is exactly the p_j coordinate
vector. For every fixed tuple of complex scalars z_j, the combination
sum_j z_j w_j(t) belongs to D(t)V for t nonzero. Its slice matrix has
rank at most q by (2). All its (q+1)-minors are polynomial in t and
vanish for t nonzero, so they vanish at zero as well.

It follows that the coordinate subspace spanned by the p_j has dimension
d and consists entirely of slices of rank at most q. This argument
proves the required specialization directly, including preservation of
every linear combination. It does not assume that the original subspace
has any torus symmetry.

## 4. Coordinate subspaces below rank 24 have dimension at most eight

For a coordinate parameter e_(i,k,s), every nonzero matrix entry is a
pivot in a distinct row and column. Its rank is

    16 h_k,       (h_0,...,h_6)=(1,2,3,4,3,2,1).          (3)

Indeed h_k counts pairs (p,q) with p+q=k, and each pair contributes
the sixteen choices of j,r. The source indices distinguish all their
rows and columns.

A coordinate subspace of rank at most 23 can therefore use only middle
coordinates k=0 or k=6. A sum with one nonzero coordinate at each extreme
has rank 32: its two rank-16 pieces occupy disjoint row blocks p=0,3 and
column blocks q=0,3. Thus a bounded-rank coordinate subspace uses only
one of the two middle extremes.

At that extreme, parameter coordinates form a 4-by-4 grid (i,s). Partition
the grid into the eight pairs

    (i,s) and (i+2 modulo 4, s+2 modulo 4).

The sum of the two coordinates in each pair has rank at least 24. Here
is an explicit uniform minor. Put i_0=min(i,i') and s_0=min(s,s'), and
choose the 24 source rows and 24 source columns

    rows:    (j,p,L),   0<=j<4, s_0<=L<=s_0+5,
    columns: (H,q,r),   i_0<=H<=i_0+5, 0<=r<4,

where p=q=0 for k=0 and p=q=3 for k=6. The selected determinant is 1.
After removing the common coordinate shifts and grouping by the parities
of j,H and L,r, this matrix has four 6-by-6 diagonal blocks. Each block
is the coefficient matrix for the biform 1+xz or x+z on the ranges
j,r=0,1 and H,L=0,1,2. Each 6-by-6 block has determinant of absolute value 1.
The saved explicit minors also verify all eight pair choices at both
middle extremes by integer arithmetic.

At most one member of each pair can belong to the coordinate subspace.
Its dimension is at most eight. Section 3 transfers this bound to every
complex V of slice rank at most 23.

The bound is attained. Take the eight coordinates k=0, i=0,1 and
s=0,1,2,3. Their matrices are supported on columns with q=0, H=0,...,4
and r=0,...,3. There are only 20 such columns, so every slice in this
eight-dimensional parameter subspace has rank at most 20. This proves (1).

## 5. Consequence for singular long-leg limits

Suppose

    B(t) M(F(t)(X)) C(t)=X tensor I_11+O(t),
    X in Mat_10(C),                                    (4)

and C is regular with rank C_0=110-c, where 0<=c<=8. Scalar-balance F,
compensating in B, so F is regular and F_0 is a nonzero linear map.
The target unit gives regular D=M(F(I))C and G=BD=I+O(t). Normalize
B by the regular invertible G^(-1), so BD=I exactly.

For Y_X=M(F(X))C and Z_X=BY_X, the correction

    W_X=Y_X-D Z_X=(I-DB)Y_X

is regular and has generic rank at most 112-110=2. Specialization gives

    M(F_0(X)) C_0 = D_0(X tensor I_11)+W_X(0),
    rank W_X(0)<=2.                                    (5)

These are the credited unit-kernel identities. They remain valid for
singular C_0 because the unit still gives generic rank 110.

For rank-one X=a b^T, multiplication by C_0 loses at most 2+c source
ranks. Therefore

    rank M(F_0(a b^T)) <=11+2+(2+c)=15+c<=23.            (6)

If F_0(a b^T) is nonzero, the maintained source minimum rank 16 also gives

    rank(D_0((a b^T) tensor I_11)) >=16-(2+c)-2=12-c>2. (7)

Choose a with at least one such nonzero image. It exists because F_0 is
nonzero and rank-one matrices span Mat_10. For every nonzero b, the map
b^T tensor I_11 is surjective, so the rank on the left of (7) equals
rank(D_0(a tensor I_11)), independently of b. If another nonzero b had
F_0(a b^T)=0, equation (5) would make that same rank at most two.
Consequently b |-> F_0(a b^T) is injective.

Its image is a ten-dimensional linear parameter subspace. Every element
has source slice rank at most 23 by (6), contradicting (1). This excludes
(4). Transposing the two long legs proves the symmetric statement: the
source transpose is identified with M(F') for F'_(i,k,s)=F_(s,k,i), using
row and column permutations, and the target transposes X to X^T.

Scalar-balancing either original Laurent long map and compensating in F
preserves the complete identity. Thus each balanced long-map leading
rank in a remaining candidate is at most 101.

## 6. Exact boundary and evidence

At c=8, the upper rank in (6) is 23 and the lower rank in (7) is 4.
At c=9, the upper rank is 24. The linear-space bound used here does not
extend to rank 24: the twelve-dimensional coordinate space with k=0,
i=0,1,2 and arbitrary s has at most 24 nonzero matrix columns. This is
an explicit reason that this argument stops at long-map rank 101.

The verifier reconstructs all 4096 source terms, all 112 coordinate ranks,
the 256 cross-extreme pair ranks and the 16 determinant-one matching
minors. It verifies the diagonal rank-preserving weights, example echelon
specializations, both support-dimension controls and the strict c=8/c=9
boundary. The all-subspaces and all-Laurent-order claims rest on the
written argument, whose status remains unreviewed.

The source coefficient convention and minimum rank 16 retain their prior
credit and byte pins. The earlier singular-long-rank note supplies the
active-ruling argument. The new contribution is the sharp bound (1), its
elementary specialization proof and its wider long-leg exclusion. No
additional external theorem is imported. General singular constructions
with both balanced long ranks at most 101 and the exponent goal remain open.
