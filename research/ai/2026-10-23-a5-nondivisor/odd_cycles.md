# Sharp nondivisor source caps from odd cycles

October23,2026. Written, unreviewed owner-directed OpenAI Codex work.
No independent mathematical review, formalization or exponent improvement.

## 1. Statement

Let w>=1 and a=2w+1. Use the canonical balanced cyclic source A_a with
slice formula

    M(F)_((j,p,L),(H,q,r))=F_(H-j,p+q,L-r),                (1)

where short indices range from0 to a-1, long indices from0 to2a-2,
and out-of-range coefficients are zero. If an integer Q satisfies

    a(a+w-1)<=Q<=a^2+2w^2,                               (2)

the maximum vector dimension of a complex linear parameter space V
with rank M(f)<=Q for every f in V is exactly aw.

In particular, at a5,w2 this maximum is10 for every Q=30,31,32,33.
For w>1, w is a nondivisor of a. This is separate from PR148's divisor
strip intervals. The Q34 endpoint at a5 is not established by this
cycle argument.

## 2. Torus specialization to a coordinate space

Assign parameter weight i+a*k+a*(2a-1)*s. These are all distinct integers
from0 to a^2(2a-1)-1. The corresponding source row and column weights
are -j+a*p+a*(2a-1)*L and H+a*q-a*(2a-1)*r. Their sum is the parameter
weight in (1), so the diagonal action preserves matrix rank for t!=0.
This is the credited torus mechanism of PR129, written here at all sizes.

Put a basis of V in echelon form in increasing weight order, multiply
by the diagonal action and divide each vector by its leading t power.
The resulting vectors are regular and tend to distinct coordinate
vectors. Every constant linear combination has the original rank bound
for t!=0; all expressing minors are polynomial and still vanish at zero.
Thus the coordinate limiting space has the same dimension and the same
rank bound for every one of its members. No invariance of V is assumed.

A coordinate at middle k has rank a^2*h_k, where h_k counts p+q=k.
Since Q<2a^2, only k0 or k(2a-2) can occur. A sum with one coordinate
at each extreme has rank2a^2 on disjoint row and column blocks, so a
bounded coordinate space uses just one middle extreme. The remaining
parameters form an a-by-a grid (i,s). At either extreme the nonzero
source block is the biform matrix

    R_a(g)_((j,L),(H,r))=g_(H-j,L-r).                     (3)

## 3. Exact adjacent-pair ranks

Partition the grid into the a orbits of

    (i,s) -> (i+w,s+w) modulo a.

Since gcd(w,2w+1)=1, every orbit is a cycle of length a. Adjacent
vertices differ in each short index by absolute value w or w+1.
Common monomial shifts add only zero rows/columns and degree shifts
to (3), preserving rank. Reversing a short factor is a fixed source
row/column permutation; for the x factor it sends j to a-1-j and
H to2a-2-H, and for z it sends L to2a-2-L and r to a-1-r.
Thus every adjacent sum has the rank of R_a(1+x^p z^q), with
p,q each in {w,w+1}.

Separate j,H by residues modulo p and r,L by residues modulo q. After
discarding zero padding, each block is R(1+xz) with input lengths u,v,
where u,v belong to {1,2,3}. Its rows are (j,L), j<u,L<=v; its columns
are (H,r), H<=u,r<v. Grouping by j+L=H+r gives bidiagonal path blocks
with a unit maximal minor. Their rank is

    uv+min(u,v).                                         (4)

Equivalently, the nine cases u,v=1,2,3 have ranks

    2  3  4
    3  6  8
    4  8 12.

Each has an explicit unimodular maximal minor. The row/column counts
give the matching upper bound, so (4) is exact. These fixed small
identities suffice for every w; no growing numerical rank assumption
is being made.

For p=w, the residue input lengths are one3 and w-1 copies of2.
For p=w+1, they are w copies of2 and one1. The sum of the uv terms
over all blocks is a^2. The sum of the minimum terms in (4) is

    p=q=w:       2w^2+1;
    {p,q}={w,w+1}: 2w^2+w;
    p=q=w+1:     2w^2+2w+1.

All three values are at least2w^2+1. Thus every adjacent grid pair
has rank at least a^2+2w^2+1, exceeding Q in (2).

## 4. The sharp dimension bound

The selected coordinates in each odd cycle cannot contain adjacent
vertices. If their indicators are x_j, summing x_j+x_(j+1)<=1 gives
2*sum x_j<=2w+1. At most w vertices are selected. There are a disjoint
cycles, so the bounded coordinate space has dimension at most aw.
Section2 transfers this bound to every complex V.

It is attained by the aw coordinates k0,0<=i<w and0<=s<a. Every matrix
in this strip has nonzero columns only at q0,0<=H<=a+w-2 and0<=r<a.
There are a(a+w-1) such columns. Its rank is therefore at most the
lower endpoint in (2), proving sharpness throughout that interval.

## 5. Scope and provenance

The literal source, torus specialization and divisor-strip investigation
retain their original source and PR129/148 credit. The odd-cycle cover,
residue counts and nondivisor interval are the local continuation. Only
elementary linear algebra, polynomial coefficient shifts and finite
unimodular identities are used. No new external theorem is imported.

The initial a5 discovery correctly records that nine adjacent pairs
have rank34, twelve rank35 and four rank38. Hence the originally
proposed rank35 lower bound for every edge was false. The corrected
universal argument uses rank34 and stops at Q33. A separate complete
finite-support investigation at Q34 must supply its own certificate;
it does not follow by changing the strict inequality in this proof.
Neither result supplies a matrix multiplication target or improves9/4.
