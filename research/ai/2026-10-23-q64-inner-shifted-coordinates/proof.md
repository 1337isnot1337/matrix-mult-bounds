# Neighboring inner-index shifted long-leg charts have quadratic corrections

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

Choose `epsilon_B,epsilon_C` in `{0,1}`. Let `U` be any linear map
on the first leg, and use
\[
B_{y,s}\mapsto b_{s-\epsilon_B y,y},\qquad
C_{z,v}\mapsto c_{v,z-\epsilon_C v},
\]
when the displayed target index lies in `[0,n-1]`, and zero otherwise.
For a first-leg flattening input `x`, put
`ell_(p,q)(x)=<x,U(A_(p,q))>`. Let `D_n` be the target tensor minus
the source image.

## Off-diagonal source functionals

For inner indices `(y,v)=(1,0)`, the source term indexed by `(p,q)`
maps to
\[
b_{q-\epsilon_B,1}c_{0,p+1}.
\]
It is valid when `q>=epsilon_B` and `p<=n-2`. The target has no term
with unequal inner indices, and the output monomial uniquely identifies
`(p,q)`. Its correction coefficient is therefore
`-ell_(p,q)(x)` on this region.

For `(y,v)=(0,1)`, the source term maps to
\[
b_{q+1,0}c_{1,p-\epsilon_C}.
\]
It is valid when `q<=n-2` and `p>=epsilon_C`. Again it is a unique
off-diagonal monomial absent from the target, so its correction
coefficient is `-ell_(p,q)(x)`.

When `n>=2`, these two regions cover every source pair except
`(p,q)=(n-1,n-1)` and, when both shifts are active,
`(p,q)=(0,0)`. Thus if `x` is in the correction-flattening kernel,
\[
ell_{p,q}(x)=0
\quad\text{outside a set of size at most }1+\epsilon_B\epsilon_C.
\tag{1}
\]

## Matched block and rank bound

The matched term `(y,v)=(0,0)` always maps to
`b_(q,0)c_(0,p)`. Its target coefficient is `x_(q,p)` and its source
coefficient is `ell_(p,q)(x)`. Kernel membership yields
\[
x_{q,p}=ell_{p,q}(x).
\tag{2}
\]
By (1) and (2), a kernel vector can be supported only on at most
`1+epsilon_B*epsilon_C` target coordinates. Hence, for `n>=2`,
\[
\operatorname{rank}D_n^{(1)}
\ge n^2-1-\epsilon_B\epsilon_C
\ge n^2-2.
\]
For `n=1`, the final lower bound `n^2-2` is negative and therefore
holds trivially.

Border rank dominates flattening rank, and restriction cannot increase
border rank. An auxiliary tensor restricting to `D_n` must therefore
have border rank at least `n^2-2`, which is quadratic as `n` grows.

The argument permits arbitrary first-leg maps, including singular maps.
The exact rational replay checks the identities for all four shift pairs,
six first-leg maps and `n=1,...,6`; those finite cases are indexing
controls, not the all-size argument. Other long-leg maps, independent
review, formalization and exponent improvement are not claimed.
