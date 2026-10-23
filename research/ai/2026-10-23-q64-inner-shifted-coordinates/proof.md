# The inner-index shifted long-leg chart has a quadratic correction

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

Let `U` be any linear map on the first leg. On the other legs use
\[
B_{y,s}\mapsto b_{s-y,y},\qquad
C_{z,v}\mapsto c_{v,z-v},
\]
when the displayed target index is between `0` and `n-1`, and zero
otherwise. Define `ell_(p,q)(x)=<x,U(A_(p,q))>` for a first-leg
flattening input `x=(x_(i,h))`. Let `D_n` be the target tensor minus
the source image under these maps.

## Two off-diagonal coordinate blocks

The coefficient of `b_(q-1,1)c_(0,p+1)` in `D_n(x)` is
`-ell_(p,q)(x)` whenever `q>=1` and `p<=n-2`. Its only source
contribution has `(y,v)=(1,0)`, so no target term occurs and no other
source coordinate contributes to this monomial.

Likewise, the coefficient of `b_(q+1,0)c_(1,p-1)` is
`-ell_(p,q)(x)` whenever `q<=n-2` and `p>=1`. Its only source
contribution has `(y,v)=(0,1)`, again with no target term.

For `n>=2`, these two valid regions cover every source pair `(p,q)`
except `(0,0)` and `(n-1,n-1)`. Therefore, if `x` lies in the kernel of
the correction flattening, then
\[
ell_{p,q}(x)=0
\quad\text{for all }(p,q)\notin\{(0,0),(n-1,n-1)\}.
\tag{1}
\]

## Matched block and rank bound

For each `p,q`, the matched source term with `y=v=0` contributes to
`b_(q,0)c_(0,p)`, whose target coefficient is `x_(q,p)`. Kernel
membership therefore gives
\[
x_{q,p}=ell_{p,q}(x).
\tag{2}
\]
Together, (1) and (2) show that every kernel vector is supported only
at the two target coordinates `(0,0)` and `(n-1,n-1)`. Thus the
first-leg flattening kernel has dimension at most two, and
\[
\operatorname{rank} D_n^{(1)}\ge n^2-2.
\]
For `n=1` the same numerical lower bound is trivial because the right
side is negative; the flattening has nonnegative rank. For `n>=2` the
argument above proves it directly.

Tensor border rank dominates flattening rank, and restriction cannot
increase border rank. Any auxiliary tensor restricting to `D_n` must
have border rank at least `n^2-2`, which is quadratic in `n`.

The proof allows arbitrary `U`, including singular maps. It concerns
only the stated shifted maps on the two long legs. The accompanying
finite replay checks six rational first-leg maps at `n=1,...,6`; it is
not the all-size argument. No independent review, formalization, or
exponent improvement is claimed.
