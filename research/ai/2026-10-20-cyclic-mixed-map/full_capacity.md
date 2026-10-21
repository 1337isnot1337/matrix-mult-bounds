# Full-capacity square targets are excluded at every tensor power

**AI-CYCLIC-FULL-CAPACITY-047.** Written proof, unreviewed. Let a>=2,
r>=1, d=a^2(2a-1), and D=d^r. Over C, A_a^r cannot degenerate to a
direct sum of square matrix multiplication tensors whose leg dimensions
sum to D. In particular, if n^2=D, it cannot degenerate to M(n,n,n).
Arbitrary singular Laurent changes of all three legs are allowed.

This does not exclude targets with smaller leg dimensions. It does not
give a uniform asymptotic loss or improve the matrix multiplication
exponent. The A_4 to M(10,10,11) and S_4 to M(106,106,106) targets
remain open under general degeneration.

## 1. Minimum slice rank at all powers

The minimum nonzero ordinary slice rank of A_a^r is exactly a^(2r),
over any field. This extends the r=1 triangular-minor proof in
[claim 042](../2026-10-20-koszul/cyclic_finite_target.md).

Write all six short indices as vectors in {0,...,a-1}^r and let every
addition and subtraction of such indices be componentwise. A first-leg
slice has coefficient array F(i,k,s), with k in {0,...,2a-2}^r.
Its matrix, with rows (j,p,L) and columns (H,q,t), has entry

    F(H-j, p+q, L-t),

where out-of-range short indices mean zero. Choose k0 for which
f(i,s)=F(i,k0,s) is nonzero. Set b=2a-1. Give the coordinates of i
the weights 1,b,...,b^(r-1), and those of s the weights
b^r,...,b^(2r-1). These weights, denoted u and v, give distinct values
u.i+v.s on the short-index grid. Choose a nonzero pivot (i0,s0) at
which this value is maximal. Choose p0,q0 in the short grid with
p0+q0=k0.

Take the minor whose rows and columns are

    rows:    (j, p0, t'+s0),
    columns: (j'+i0, q0, t),

for all j,t',j',t in the short grid. All their long indices are valid.
Its size is a^(2r), and its entry is

    f(i0+j'-j, s0+t'-t).

Order row pairs (j,t') and column pairs (j',t) by the same scalar
eta(j,t)=u.j-v.t. These values are distinct: a nonzero difference has
base-b digits of magnitude at most a-1, and its highest nonzero digit
dominates all lower digits. A nonzero matrix entry implies

    eta(j',t) <= eta(j,t'),

by maximality of the pivot. Thus the minor is lower triangular, with
every diagonal entry equal to the same nonzero f(i0,s0). Its determinant
is f(i0,s0)^(a^(2r)), which proves the lower bound without any
characteristic restriction.

For equality, set only F(0,0,0)=1. Then p=q=0, H=j and L=t, so the
slice has precisely a^(2r) nonzero entries in distinct rows and columns.
The other two legs have the same minimum by cyclic symmetry.

## 2. The cyclic source has a closed special-linear orbit

We use Proposition 4.8 of Peter Burgisser and Christian Ikenmeyer,
[*Fundamental invariants of orbit closures*, arXiv:1511.02927v2](https://arxiv.org/abs/1511.02927v2).
For a tensor of format D-by-D-by-D, its sufficient hypotheses are:

1. A reductive subgroup of its stabilizer in SL_D^3 has centralizer
   contained in the diagonal matrices.
2. Its support admits a probability distribution with uniform marginals.

The conclusion is polystability: its SL_D^3 orbit is closed. This is an
external invariant-theory theorem, not a result of this repository.

Put e=a-1. Binary polynomial multiplication is equivariant for SL_2,
with the two short factors of degree e and the long factor of degree 2e.
Duals can be used according to the tensor convention; each is an
irreducible SL_2 module. The product of the 3r separate SL_2 groups
therefore stabilizes A_a^r. Each of the three tensor legs is an external
tensor product of irreducible modules for these separate groups, hence
is irreducible. The group image is reductive and has determinant one on
each leg. By Schur's lemma its centralizer on each leg consists of
scalars; within SL_D this is finite, in particular diagonal.

For the support condition, on a single C(a,a) use

    p(i,j) = binom(e,i) binom(e,j)
             / ((2e+1) binom(2e,i+j)).

It is strictly positive and has uniform marginals on both short indices
and the long index i+j. The identities are proved in
[claim 038](../2026-10-20-koszul/finite_target_screens.md).
The product distribution for the 3r factors is uniform on each grouped
leg, whose dimension is D. All hypotheses of Proposition 4.8 hold.
Consequently A_a^r is polystable over C.

## 3. A semistable boundary target would already be isomorphic

Here semistable means that some homogeneous SL_D^3-invariant polynomial
of positive degree is nonzero. The boundary statement below is external:
it is Proposition 5.3 of van den Berg, Christandl, Lysikov, Nieuwboer,
Walter and Zuiddam,
[*Computing moment polytopes*, arXiv:2510.08336v1](https://arxiv.org/abs/2510.08336v1),
which attributes it to Burgisser--Ikenmeyer. We include a short sequence
proof for clarity, without claiming a new invariant-theory lemma.

**Lemma.** If a nonzero tensor T has closed SL_D^3 orbit, and a semistable
tensor U of the same format belongs to the closure of GL_D^3.T, then
U belongs to GL_D^3.T itself.

To prove it, take a converging sequence g_k.T -> U. Choose determinant
roots to write g_k.T = z_k h_k.T with h_k in SL_D^3. Because the orbit
SL_D^3.T is closed and excludes zero, every point on it has norm at
least some delta>0. Thus |z_k| is bounded. Pass to a convergent
subsequence z_k -> z. If z is nonzero, then h_k.T -> U/z, which lies
in the closed SL orbit. If z=0, every homogeneous invariant f of
positive degree satisfies

    f(U) = lim z_k^(deg f) f(T) = 0,

contradicting semistability. This proves the lemma. For complex algebraic
group orbits, Euclidean and Zariski orbit closures agree; equivalently
one may use an approaching curve in the orbit.

Square matrix multiplication tensors are polystable by Corollary 4.9
of the same external paper. For a direct sum of squares with
sum_j n_j^2=D, the support of M(n_j,n_j,n_j) in block j can be assigned
probability 1/(D*n_j) per nonzero coefficient. Every coordinate marginal
is 1/D. The blockwise standard matrix-multiplication stabilizer has a
diagonal centralizer: its diagonal torus separates coordinates within
each nontrivial block, and the independent block scalings separate blocks.
Applying Proposition 4.8 again proves polystability, hence semistability,
of this direct sum. Alternatively, multiplying block j by
1/sqrt(D*n_j) gives scalar reduced density matrices, the usual
moment-map criterion for polystability.

## 4. Contradiction at full capacity

Suppose A_a^r degenerates to a direct sum of square matrix tensors
with sum_j n_j^2=D. Both source and target have full leg dimensions D.
The maps of any such degeneration are generically invertible: an
identically rank-deficient map would force the limiting flattening rank
below D. Thus the target belongs to the GL_D^3 orbit closure of the
source. Sections 2 and 3 force an isomorphism.

Minimum nonzero slice rank is preserved by such an isomorphism. The
source has minimum a^(2r), while the target has minimum min_j n_j.
But

    min_j n_j <= sqrt(D)
               = a^r (2a-1)^(r/2)
               < a^(2r),

because a^2>2a-1 for a>=2. This is the contradiction.

Concrete consequences include A_2^2 not degenerating to M(12,12,12),
A_5 not degenerating to M(15,15,15), and S_4=A_4^2 not degenerating
to M(112,112,112). The last statement does not decide M(106,106,106).

## Evidence, attribution, and limits

The proof uses an external polystability theorem and the local source
distribution from claim 038. Its all-power triangular minor is an
extension of the local r=1 argument. Neither a finite coefficient check
nor merging this note constitutes independent mathematical review.

The Burgisser--Ikenmeyer versioned PDF has SHA-256
`a4138fc3ef45f144f367f227514b8345ddd74690c19ca07e1ef4be707fd6ea7b`.
Proposition 4.8, Corollary 4.9 and the surrounding hypotheses were
inspected. The moment-polytope paper's versioned PDF has SHA-256
`c3e087d74dcf3b66b4f5b36cb4988825403e0931d9f6fb92b5479e3286a94d0d`;
Theorems 5.1--5.2 and Proposition 5.3, including its attribution footnote,
were inspected. No claim relies on treating a padded lower-dimensional
matrix tensor as semistable in the larger format: it is not, and that
is exactly why this argument stops at full capacity.

The finite companion checks triangular minors and corner equality
slices. It does not verify the external invariant-theory theorem or
replace the all-size proof above. No asymptotic profile gain follows
from a strict finite deficit of one coordinate.
