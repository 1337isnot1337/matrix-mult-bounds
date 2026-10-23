# The inner-index shifted long-leg chart has a near-terminal frontier

October 23, 2026. Written, unreviewed, owner-directed Codex research.

## Tensor and maps

Use

\[
Q(n,4)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{3}
 A_{p,q}B_{y,q+v}C_{p+y,v}
\]

and

\[
M(n,4,n)=\sum_{i,h=0}^{n-1}\sum_{j=0}^{3}
 a_{i,h}b_{i,j}c_{j,h}.
\]

For each `n`, choose arbitrary integers `0<=k_B,k_C<n`, possibly
depending on `n`. Let `U` be any linear map on the first leg and use
\[
B_{y,s}\mapsto b_{s-k_By,y},\qquad
C_{z,v}\mapsto c_{v,z-k_Cv},
\]
when the displayed target indices lie in `[0,n-1]`, and zero otherwise.
For a first-leg flattening input `x`, define
`ell_(p,q)(x)=<x,U(A_(p,q))>`. Let `D_n` be the target minus this
source image.

## Off-diagonal blocks

The source term `(p,q,y,v)=(p,q,1,0)` maps to
\[
b_{q-k_B,1}c_{0,p+1}.
\]
It is valid for `q>=k_B` and `p<=n-2`. The target has no term with
unequal inner indices, and this monomial identifies `(p,q)` uniquely.
Its correction coefficient is `-ell_(p,q)(x)` on this region.

The source term `(p,q,0,1)` maps to
\[
b_{q+1,0}c_{1,p-k_C}.
\]
It is valid for `q<=n-2` and `p>=k_C`; it is another unique
off-diagonal monomial absent from the target. Its correction coefficient
is `-ell_(p,q)(x)`.

Because `k_B,k_C<n`, the union of the two valid regions misses exactly
the corner `(p,q)=(n-1,n-1)` and the rectangle
`0<=q<k_B`, `0<=p<k_C`. The rectangle contains `k_B*k_C` entries.
Therefore a vector in the correction-flattening kernel must satisfy
\[
ell_{p,q}(x)=0
\]
outside a set of size `1+k_B*k_C`.

## Matched block and rank lower bound

The source term with `y=v=0` maps to `b_(q,0)c_(0,p)`. Its target
coefficient is `x_(q,p)` and its source coefficient is `ell_(p,q)(x)`.
Thus kernel membership gives
\[
x_{q,p}=ell_{p,q}(x).
\]
The flattening kernel is supported on at most `1+k_B*k_C` target
coordinates. Hence
\[
\operatorname{rank}D_n^{(1)}\ge n^2-1-k_B*k_C.
\tag{1}
\]

## Necessary condition for linear correction cost

Border rank dominates flattening rank, and restriction cannot increase
border rank. If an auxiliary correction has border rank at most `C n`
for a fixed `C`, (1) implies
\[
k_Bk_C\ge n^2-Cn-1.
\]
Set `d_B=n-k_B` and `d_C=n-k_C`, both nonnegative. Then
\[
d_B+d_C-\frac{d_Bd_C}{n}\le C+\frac1n.
\]
The left side is at least each of `d_B` and `d_C`, so both are `O(1)`.
Thus the only multiplier regime not excluded by this flattening argument
has
\[
k_B=n-O(1),\qquad k_C=n-O(1).
\]

The exact rational replay checks four small multiplier pairs and six
first-leg maps for `n=1,...,6`; it is an indexing control, not the
all-size argument. The near-terminal pair, other long-leg maps,
independent review, formalization and exponent improvement remain open.
