# Matched-window permutations require a quadratic correction

October 23, 2026. Written, unreviewed, owner-directed Codex research.

## Setup

Work over any field and use
\[
Q(n,4)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{3}
 A_{p,q}B_{y,q+v}C_{p+y,v}
\]
and
\[
M(n,4,n)=\sum_{i,h=0}^{n-1}\sum_{j=0}^{3}
 a_{i,h}b_{i,j}c_{j,h}.
\]
For each `y` and `v`, choose arbitrary permutations \(\sigma_y,\tau_v\) of \(\{0,\ldots,n-1\}\). Set
\[
B_{y,s}\mapsto b_{\sigma_y(s-y),y}\quad(0\le s-y<n),
\qquad
C_{z,v}\mapsto c_{v,\tau_v(z-v)}\quad(0\le z-v<n),
\]
and send terms with out-of-window indices to zero. The first-leg map is arbitrary.

Let \(E\) be the source coefficient space on pairs \((p,q)\), and let
\(S:E\to B\otimes C\) be the source image under the two long-leg maps. Put
\(W=\operatorname{im}S\). Let \(\mathcal T:\mathbb F^{n^2}\to B\otimes C\)
be the target first-flattening map with basis outputs
\[
T_{i,h}=\sum_{j=0}^3 b_{i,j}c_{j,h}.
\]
Its image \(V\) has dimension \(n^2\). A first-leg map gives an arbitrary
linear map \(L:\mathbb F^{n^2}\to E\), and the correction flattening is
\(\mathcal T-SL\). Quotienting by \(W\) gives
\[
\operatorname{rank}(\mathcal T-SL)\ge n^2-\dim(V\cap W).
\tag{1}
\]
As before, the right side is the minimum over all first-leg maps, since a
projection of \(V\) onto \(V\cap W\) lifts through \(S\).

## The matched `(0,0)` and off-diagonal `(0,1)` blocks

Suppose \(S\lambda=\mathcal T(x)\). In block \((0,0)\), the coefficient
of \(b_{i,0}c_{0,h}\) comes from exactly one source pair:
\[
q=\sigma_0^{-1}(i),\qquad p=\tau_0^{-1}(h).
\]
Thus \(x_{i,h}=\lambda_{p,q}\).

If \(q\le n-2\) and \(p\ge1\), the same source coefficient also
appears in block \((0,1)\):
\[
B_{0,q+1}\mapsto b_{\sigma_0(q+1),0},\qquad
C_{1,p}\mapsto c_{1,\tau_1(p-1)}.
\]
The output monomial is absent from the target, whose only inner-index
blocks have equal B and C indices. The map from such pairs \((p,q)\) to
these output monomials is injective because \(\sigma_0\) and \(\tau_1\)
are permutations. No other inner-index pair contributes to that block.
Therefore \(\lambda_{p,q}=0\), and hence \(x_{i,h}=0\).

A nonzero \(x_{i,h}\) can consequently occur only if
\[
\sigma_0^{-1}(i)=n-1
\quad\text{or}\quad
\tau_0^{-1}(h)=0.
\]
These conditions describe one fixed i-coordinate and one fixed h-coordinate,
so at most \(2n-1\) entries of \(x\) may be nonzero. The map
\(V\cap W\to\mathbb F^{n^2}\), \(\mathcal T(x)\mapsto x\), is injective;
therefore
\[
\dim(V\cap W)\le 2n-1.
\]
By (1), every first-leg map has correction flattening rank at least
\[
n^2-(2n-1)=(n-1)^2.
\]
This holds for every size and every choice of the eight permutations. The
flattening lower bound also bounds border rank, so this family cannot use an
auxiliary correction of border rank \(O(n)\).

## Evidence and limits

`verify.py` constructs the exact rational source and target subspaces, computes
their intersection dimensions by exact ranks, exhausts all eight-permutation
profiles at `n=1,2`, and checks deterministic profiles through `n=5`. This
finite replay checks coefficient indexing and the minimum-rank identity; the
argument above proves the all-size result.

This claim covers matched-window coordinate permutations only. General
non-coordinate long-leg maps, broader source restrictions, independent review,
Lean formalization and exponent improvement remain unclaimed.
