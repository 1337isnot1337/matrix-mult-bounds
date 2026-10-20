# Two obstructions to constructing the all-dimension targets

October 20, 2026. Written proofs, unreviewed. These restrict construction
methods; they do not exclude all polynomial degenerations or improve omega.
Use T_{m,k} and N=m(m+1)/2 from [the target note](all_dimension_targets.md).

## 1. Arbitrary linear restrictions need about 50 percent overhead

If an ordinary linear restriction C(m,B) >= T_{m,k} exists, then

\[
\boxed{B\ge kN+k\lfloor m^2/4\rfloor-m+1.} \tag{1}
\]

No basis restriction is imposed in this statement. Contract C(m,B) by any
nonzero covector on its m-dimensional input. The resulting B-by-(B+m-1)
matrix has rank B: it represents multiplication by a nonzero univariate
polynomial, which is injective. Since T_{m,k} is concise on X, its X map in
any restriction is invertible. Its Y and Z maps have rank kN by conciseness.
After restricting the source input to a kN-dimensional subspace, the matrix
still has rank kN. Projecting its output to dimension kN can decrease rank by
at most B+m-1-kN. Thus every nonzero target slice has rank at least

\[
2kN-B-m+1. \tag{2}
\]

The maximum slice rank of T_{m,k} is

\[
k\sum_{u=1}^m\min(u,m+1-u)
=k\lfloor(m+1)^2/4\rfloor. \tag{3}
\]

Every block is bounded by its smaller dimension. Equality holds simultaneously:
take X_i=1/(i+1), making each block a rectangular Hilbert matrix with a
nonsingular leading square minor. Comparing (2)-(3), and using
N-floor((m+1)^2/4)=floor(m^2/4), proves (1).
The overhead in (1) tends to 50 percent uniformly for k>=1 as m grows.
In particular, general linear restrictions cannot meet the construction
criterion. This argument does not extend to degenerations by replacing
restriction matrices with their limits: those matrices may become singular,
and coefficient cancellations can preserve a concise limiting tensor.

## 2. A catalecticant obstruction permits arbitrary bases on two legs

Fix 0<=q<=m-1 and put h=m-1-q. Define the linear map on the shared factor

\[
\Delta_q:X_i\longmapsto\sum_{r+s=i}U_r\otimes V_s,
\quad 0\le r\le q,\quad 0\le s\le h.
\]

After applying Delta_q, flatten a tensor between (U,Y) and (V,Z). Denote
this matrix by L_q. Unlike the full-space Koszul tests, this construction
uses the specified polynomial coefficient structure on X.

For the source C(m,B), its row (r,j) has a one at column (s,r+s+j) for
every s. Rows depend only on r+j; the resulting B+q distinct rows have
disjoint support. Therefore

\[
\operatorname{rank}L_q(C(m,B))=B+q. \tag{4}
\]

For an output-shared block C(u,v), where u+v=m+1, the entry at row (r,i),
column (s,j), equals one exactly when r+s=i+j. Grouping by r-i=j-s gives
disjoint all-ones blocks, one for each integer in
[-u+1,q] intersect [-h,v-1]. The rank is consequently

\[
\min(q,v-1)+\min(u-1,h)+1.
\]

Summing over all u and all k copies gives

\[
\operatorname{rank}L_q(T_{m,k})=k(N+qh). \tag{5}
\]

Arbitrary substitutions on Y and Z induce ordinary row and column operations
on L_q; its rank cannot increase under restriction or degeneration. Thus a
degeneration with the shared X factor fixed requires B>=k(N+qh)-q. Maximizing
over q gives

\[
\boxed{B\ge kN+k\lfloor(m-1)^2/4\rfloor-\lfloor(m-1)/2\rfloor.} \tag{6}
\]

This recovers the coordinate-weight lower bound by a different method and
**extends it to arbitrary polynomial changes of basis on Y and Z** when X
retains its stated coefficient identification. It excludes C(4,10k) to
T_{4,k} even in that larger class, since B>=12k-1.

The same bound holds when the X transformation is induced by a change of two
homogeneous polynomial variables: Delta_q intertwines that action with the
corresponding actions on U and V. One may formulate this using divided-power
bases, or verify it on the pure-power vectors (1,t,...,t^(m-1)), which span X.
For every nonzero parameter these induced maps are invertible, and the rank
bound passes to the tensor limit.

An arbitrary GL(m) change on X need not intertwine Delta_q and may increase
the source rank in (4). Equation (6) is therefore **not** an obstruction to
the full construction premise H(rho). No claim is made that a general
degeneration can be reduced to the restricted form used here.

## 3. Why a broad class of shared-factor flattenings cannot help

The survival of shared Koszul tests has a more general explanation. Let
L:X->Hom(U,V) be any linear map, let r=max_{x in X} rank L(x), and set

\[
M(z)=\sum_{i=0}^{m-1}z^iL(X_i).
\]

Suppose rank over C(z) of M(z) is r. Form a linear tensor flattening by
applying L on X and grouping (U,Y) against (V,Z). Then, for every B>=1,

\[
\operatorname{rank}K_L(C(m,B))\ge Br. \tag{7}
\]

Indeed, the source map is multiplication by the polynomial matrix M(z), from
U-valued polynomials of degree <B to V-valued polynomials of degree <B+m-1.
Choose r columns independent over C(z). The map on polynomials supported on
these columns is injective, giving a Br-dimensional subspace of the image.
This elementary polynomial-matrix argument is a local rederivation, with no
priority claim.

Every rank-one tensor has K_L rank at most r. Consequently **every target of
border rank at most B** has K_L rank at most Br. Such a target cannot violate
this source flattening inequality. In particular this applies to T_{m,k}
when B=kN.

If L is GL(X)-equivariant between fixed representations, its rank is constant
on all nonzero x, so the hypothesis holds automatically. This covers every
linear equivariant Young/Pieri flattening of this form on the shared factor.
It also covers every projected shared Koszul flattening: for a nonzero linear
projection pi, the polynomial vector pi(1,z,...,z^(m-1)) is not identically
zero, because the rational-normal-curve vectors span X. Wedge multiplication
by that vector has the same rank as wedge multiplication by any nonzero
vector in the projected space. No choice of that projection can exclude the
border-rank-B target by this shared-factor rank test.

The curve-rank hypothesis is essential. For the catalecticant map Delta_q,
the vectors (1,z,...,z^(m-1)) map to rank-one matrices, while an arbitrary x
can give rank greater than one. Section 2 exploits exactly this gap. It uses
extra polynomial structure, which an arbitrary shared-factor basis change
need not preserve. This result does not cover every nonlinear invariant or
flattenings based on the other factors.

## 4. Remaining scope

A useful positive control is that C(2,3k) does degenerate to T_{2,k} for every
k>=1. Order the source Y intervals with lengths (1,2) repeated k times. Give
the length-one blocks Y weight zero, the length-two blocks Y weight one,
and each matched Z block the negative weight; project unused Z coordinates
to zero. Reverse each block's Y order to match the coefficient convention.
The only surviving terms are the target sectors; every cross term has
positive weight. Likewise C(3,6) degenerates to T_{3,1} using Y interval
lengths (2,3,1) and weights (0,1,0). These exact finite controls are covered
by coefficient tests. They keep m fixed and do not meet H(rho).

A successful low-overhead construction must use a genuine degeneration and
must use the shared factor more freely than the fixed coefficient-space
action considered above. The unrestricted shared-factor problem remains
open. Numerical small-instance orbit fitting, if attempted, is exploratory;
even a small residual would not certify a degeneration or an exponent bound.

The bounded [orbit probe](../../../results/koszul-2026-10-20/orbit_probe_summary.json)
ran 16 real and 16 complex starts at m=4, each for 6,000 alternating
least-squares cycles. The best relative residuals were about 0.22369.
Nine 3,000-cycle calibration runs included known-positive m=2 and m=3
instances; one m=3 start stalled near 0.31643 despite the exact construction.
Thus these failed fits supply no exclusion theorem. Their code and actual
logs are retained, and none of their floating values enters a proof.
