# Fixed long-leg coordinate maps force full correction flattening rank

October 23, 2026. Written, unreviewed, owner-directed Codex research.

This proves an all-size obstruction for the maintained `Q(n,4)` source
when its two long-leg maps are fixed to the displayed coordinate maps.
The first-leg map is completely arbitrary and may be singular.

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

Let `U` be any linear map from the first source leg to the target first
leg. On the other two legs, map `B_(y,s)` to `b_(s,y)` for `s<n` and
zero otherwise, and `C_(z,v)` to `c_(v,z)` for `z<n` and zero otherwise.
Let `S_n` be the image of `Q(n,4)` and set
`D_n=M(n,4,n)-S_n`.

For a first-leg coefficient vector `x=(x_(i,h))`, define
\[
\ell_{p,q}(x)=\langle x,U(A_{p,q})\rangle.
\]
The first-leg flattening of `D_n` sends `x` to the remaining bilinear
form. Project this form to two disjoint sets of coordinates, indexed by
the coefficients of `b_(s,0)c_(0,z)` and `b_(s,1)c_(1,z)`.

## The two projected coefficient formulas

For `b_(s,0)c_(0,z)`, only the source term with `y=v=0`, `q=s` and
`p=z` contributes. The projected coefficient of `D_n(x)` is
\[
F_{00}(x)_{s,z}=x_{s,z}-\ell_{z,s}(x).
\tag{1}
\]

For `b_(s,1)c_(1,z)`, a source term exists exactly when `s,z>=1`.
Then `y=v=1`, `q=s-1` and `p=z-1`, so
\[
F_{11}(x)_{s,z}=
\begin{cases}
x_{s,z},&s=0\text{ or }z=0,\\
x_{s,z}-\ell_{z-1,s-1}(x),&s,z\ge1.
\end{cases}
\tag{2}
\]

The source linear functional in (2) is exactly the functional appearing
in (1) at the preceding diagonal position:
\[
F_{00}(x)_{s-1,z-1}=x_{s-1,z-1}-\ell_{z-1,s-1}(x).
\tag{3}
\]
This identity holds for every `U`; no coefficient or rank condition on
the first-leg map is used.

## The stacked projection is injective

Suppose both projected blocks vanish. Equation (2) gives
`x_(s,z)=0` whenever `s=0` or `z=0`. For `s,z>=1`, equations (2) and
(3) imply
\[
x_{s,z}=\ell_{z-1,s-1}(x)=x_{s-1,z-1}.
\]
Iterating this equality along the diagonal `s-z=constant` reaches a
boundary coordinate with one index zero. That coordinate vanishes, so
every `x_(s,z)` vanishes. Thus the projection of the first-leg
flattening to the two selected coordinate blocks has trivial kernel and
rank `n^2`.

Projection cannot increase rank, so the full first-leg flattening of
`D_n` has rank at least `n^2`. Its first-leg dimension is `n^2`; hence
the rank is exactly `n^2`.

## Border-rank consequence and scope

Every tensor has border rank at least each flattening rank, and
restriction cannot increase border rank. Any auxiliary tensor
restricting to `D_n` must therefore have border rank at least `n^2`.
This rules out an `O(n)` correction for every first-leg map when the two
long-leg coordinate maps are fixed.

The replay reconstructs the source, target and both projected blocks
for six rational first-leg maps at `n=1,...,6`. It checks the identities
above and the resulting rank over `Q`; the all-size argument is the
diagonal recurrence. Changes to either long-leg map, general changes of
source, independent review, Lean formalization and exponent improvement
are outside this result.
