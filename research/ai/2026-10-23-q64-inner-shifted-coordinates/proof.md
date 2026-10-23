# All inner-index proportional long-leg shifts have quadratic corrections

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

For each `n`, choose arbitrary integers `0<=k_B,k_C<n`, and let `U`
be any linear map on the first leg. Use
\[
B_{y,s}\mapsto b_{s-k_By,y},\qquad
C_{z,v}\mapsto c_{v,z-k_Cv},
\]
when the target indices lie in `[0,n-1]`, and zero otherwise. For a
first-leg flattening input `x`, put
`ell_(p,q)(x)=<x,U(A_(p,q))>`. Let `D_n` be the target tensor minus
the source image.

## A support bound from off-diagonal blocks

For `(y,v)=(1,0)`, the source term `(p,q)` maps to
\[
b_{q-k_B,1}c_{0,p+1}.
\]
It is valid when `q>=k_B` and `p<=n-2`. The target has no unequal
inner-index term, and this monomial determines `(p,q)` uniquely. Its
correction coefficient is `-ell_(p,q)(x)`.

For `(y,v)=(0,1)`, the term maps to
\[
b_{q+1,0}c_{1,p-k_C},
\]
valid when `q<=n-2` and `p>=k_C`. This is also a unique monomial
absent from the target, so its correction coefficient is
`-ell_(p,q)(x)`.

The union of these two regions misses the corner `(n-1,n-1)` and the
rectangle `0<=q<k_B`, `0<=p<k_C`, containing `1+k_B*k_C` source pairs
in total. Thus a kernel vector satisfies `ell_(p,q)(x)=0` outside that
set.

The matched `(y,v)=(0,0)` coefficient of `b_(q,0)c_(0,p)` is
`x_(q,p)-ell_(p,q)(x)`. Therefore a flattening-kernel vector is
supported on at most `1+k_B*k_C` target coordinates, proving
\[
\operatorname{rank}D_n^{(1)}\ge n^2-1-k_B*k_C.
\tag{1}
\]

## The high-multiplier case

Consider the matched inner slice `j=2`, namely coordinates
`b_(s,2)c_(2,z)`. A source term can contribute only with `y=v=2`; its
long-leg indices are
\[
s=q+2-2k_B,\qquad z=p+2-2k_C.
\]
If `2*k_B>n+1`, then even the largest possible source value `q+2=n+1`
maps below zero, so there is no source contribution to any such
coordinate. If `2*k_C>n+1`, the analogous third-leg image is always
out of range. Either condition makes this entire projected correction
block the identity on the `n^2` first-leg coordinates. Hence
\[
\operatorname{rank}D_n^{(1)}=n^2
\]
in this case.

## The low-multiplier case

Otherwise both `k_B,k_C <= (n+1)/2`, so
\[
k_Bk_C\le (n+1)^2/4.
\]
By (1),
\[
\operatorname{rank}D_n^{(1)}
\ge n^2-1-(n+1)^2/4
=\tfrac34n^2-\tfrac12n-\tfrac54
\ge \tfrac12n^2
\]
for every `n>=4`.

The two cases prove a uniform quadratic lower bound for all
size-dependent multiplier choices. Border rank dominates flattening
rank, and restriction cannot increase border rank, so no auxiliary
tensor of border rank `O(n)` can restrict to this correction.

The exact rational replay exhausts all multiplier pairs through `n=6`
for six first-leg maps. It checks indexing and finite ranks; the case
split above is the all-size proof. Other long-leg maps, independent
review, formalization and exponent improvement are not claimed.
