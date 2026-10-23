# Fixed inner-index shift multipliers have quadratic corrections

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

Fix nonnegative integers `k_B,k_C`, and let `U` be any linear map on
the first leg. Map
\[
B_{y,s}\mapsto b_{s-k_By,y},\qquad
C_{z,v}\mapsto c_{v,z-k_Cv},
\]
when each displayed target index is in `[0,n-1]`, and zero otherwise.
For a first-leg flattening input `x`, define
`ell_(p,q)(x)=<x,U(A_(p,q))>`. Let `D_n` be the target minus this
image of `Q(n,4)`.

Assume `n>max(k_B,k_C)`, so both fixed shifts fit inside the index range.

## Off-diagonal blocks

The source term `(p,q,y,v)=(p,q,1,0)` maps to
\[
b_{q-k_B,1}c_{0,p+1}.
\]
It is valid exactly on `q>=k_B`, `p<=n-2`. Since its inner indices
differ, the target coefficient is zero. Its two outer indices determine
`p,q` uniquely, so the correction coefficient is
`-ell_(p,q)(x)` on this region.

The source term `(p,q,0,1)` maps to
\[
b_{q+1,0}c_{1,p-k_C}.
\]
It is valid exactly on `q<=n-2`, `p>=k_C`; it is also a unique
off-diagonal monomial absent from the target. Its correction coefficient
is `-ell_(p,q)(x)`.

The union of these two regions contains every source pair except
`(p,q)=(n-1,n-1)` and the rectangle
`0<=q<k_B`, `0<=p<k_C`. The rectangle has `k_B*k_C` entries because
`n>max(k_B,k_C)`. Thus, if `x` is in the flattening kernel,
\[
ell_{p,q}(x)=0
\]
outside a set of size `1+k_B*k_C`.

## Matched block and rank bound

The source term with `y=v=0` maps to `b_(q,0)c_(0,p)`. The target
coefficient there is `x_(q,p)` and the source coefficient is
`ell_(p,q)(x)`. Kernel membership gives
\[
x_{q,p}=ell_{p,q}(x).
\]
Therefore a flattening kernel vector can be supported only on at most
`1+k_B*k_C` target coordinates. The first-leg flattening rank satisfies
\[
\operatorname{rank}D_n^{(1)}\ge n^2-1-k_B*k_C.
\]
For fixed `k_B,k_C`, this is quadratic in `n`.

Border rank dominates flattening rank, and restriction cannot increase
border rank. Any auxiliary tensor restricting to `D_n` must therefore
have border rank at least `n^2-1-k_B*k_C`; no `O(n)` correction is
possible for this fixed-multiplier family.

The first-leg map may be arbitrary and singular. The exact rational
replay checks the four pairs `(k_B,k_C) in {0,1}^2` and six first-leg
maps for `n=1,...,6`; it is an indexing control, not the all-size proof.
Nonlinear or size-dependent shift multipliers, other long-leg maps,
independent review, formalization and exponent improvement are not
claimed.
