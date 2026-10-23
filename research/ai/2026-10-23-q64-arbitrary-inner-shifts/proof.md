# Arbitrary coordinate translations require quadratic correction

October 23, 2026. Written, unreviewed, owner-directed Codex research.

## Setup

Work over any field \(\mathbb F\) and use the maintained coefficient convention
\[
Q(n,4)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{3}
 A_{p,q}B_{y,q+v}C_{p+y,v}
\]
and
\[
M(n,4,n)=\sum_{i,h=0}^{n-1}\sum_{j=0}^{3}
 a_{i,h}b_{i,j}c_{j,h}.
\]
Choose arbitrary integer shifts \(\beta_0,\ldots,\beta_3\) and
\(\gamma_0,\ldots,\gamma_3\), which may depend on \(n\). Map
\[
B_{y,s}\mapsto b_{s-\beta_y,y},\qquad
C_{z,v}\mapsto c_{v,z-\gamma_v},
\]
when the translated indices lie in \(\{0,\ldots,n-1\}\), and send the term to zero otherwise. Let the first-leg map be arbitrary.

Let \(E\) be the \(n^2\)-dimensional coefficient space with basis indexed by \((p,q)\). Let \(S:E\to B\otimes C\) be the two-long-leg image of the source, before applying its first-leg map. Its image is \(W=\operatorname{im}S\). Let \(\mathcal T:\mathbb{F}^{n^2}\to B\otimes C\) be the target first-flattening map with basis outputs
\[
T_{i,h}=\sum_{j=0}^3 b_{i,j}c_{j,h},\qquad
V=\operatorname{im}\mathcal T=\operatorname{span}\{T_{i,h}:0\le i,h<n\}.
\]
The \(T_{i,h}\) are linearly independent, so \(\dim V=n^2\). A first-leg map induces an arbitrary linear map \(L:\mathbb{F}^{n^2}\to E\) on first-flattening coefficients. The correction flattening is \(\mathcal T-SL\).

For the quotient map \(\pi:B\otimes C\to (B\otimes C)/W\),
\[
\pi(\mathcal T-SL)=\pi\mathcal T,
\]
so every first-leg map satisfies
\[
\operatorname{rank}(\mathcal T-SL)\ge
\operatorname{rank}(\pi\mathcal T)=n^2-\dim(V\cap W).
\tag{1}
\]
In fact, equality is the minimum over all \(L\): choose a projection \(P:V\to V\cap W\), lift it through \(S\) using a right inverse on \(W\), and use the lift composed with \(\mathcal T\) as \(L\). Thus it suffices to bound \(\dim(V\cap W)\).

## Constraints on a source vector in the intersection

Suppose \(S\lambda=\sum_{i,h}x_{i,h}T_{i,h}\). Put
\[
a_j=\beta_j-j,\qquad c_j=\gamma_j-j.
\]
In the matched inner block \((j,j)\), the target coefficient at \(b_{i,j}c_{j,h}\) can only come from the unique source coefficient
\[
\lambda_{p,q},\qquad p=h+c_j,\quad q=i+a_j,
\tag{2}
\]
provided both indices lie in \(\{0,\ldots,n-1\}\). If either index is out of range, then \(x_{i,h}=0\). This holds for each of the four matched blocks.

## Case 1: one adjacent C shift is small

Write \(\Delta_u=\gamma_{u+1}-\gamma_u\) for \(u=0,1,2\). Suppose some \(|\Delta_u|\le f=\lfloor n/2\rfloor\). For a target coordinate \((i,h)\) with \(i<n-1\) and \(0\le h-\Delta_u<n\), if \(x_{i,h}\ne0\), (2) gives an in-range source pair \((p,q)=(h+c_u,i+a_u)\). The same source coefficient contributes in the off-diagonal source block \((y,v)=(u,u+1)\) to
\[
b_{i+1,u}c_{u+1,h-\Delta_u}.
\]
This monomial is in range and absent from \(V\). For fixed \((u,u+1)\), the pair \((p,q)\) is uniquely determined by its output monomial, and different inner-index pairs occupy different blocks. Hence its coefficient \(\lambda_{p,q}\) must be zero, contradicting the matched coefficient \(x_{i,h}\ne0\).

Therefore the support of \(x\) lies among the last column \(i=n-1\), or among the at most \(|\Delta_u|\) values of \(h\) for which \(h-\Delta_u\) is out of range. Consequently
\[
\dim(V\cap W)\le n+(n-1)|\Delta_u|
\le n+(n-1)f.
\]
By (1),
\[
\operatorname{rank}(T-SL)\ge n^2-n-(n-1)f
\ge \frac{n(n-1)}2.
\tag{3}
\]

## Case 2: every adjacent C shift is large

Otherwise \(|\Delta_u|\ge f+1\) for all \(u=0,1,2\). Since
\[
c_{u+1}-c_u=\Delta_u-1,
\]
we have \(|c_{u+1}-c_u|\ge f\), so \(\max_j c_j-\min_j c_j\ge f\). By (2), any nonzero entry \(x_{i,h}\) must satisfy \(0\le h+c_j<n\) for every \(j\). The intersection of these four intervals contains at most \(n-f=\lceil n/2\rceil\) values of \(h\). Ignoring any additional restrictions on \(i\),
\[
\dim(V\cap W)\le n\lceil n/2\rceil.
\]
Equation (1) then gives
\[
\operatorname{rank}(T-SL)\ge n\lfloor n/2\rfloor
\ge \frac{n(n-1)}2.
\tag{4}
\]

Together, (3) and (4) prove the stated bound for every size and every choice of the eight shifts and the first-leg map. Flattening rank is a lower bound for border rank, so this coordinate-shift family cannot use an auxiliary correction of border rank \(O(n)\).

## Evidence and limits

`verify.py` constructs the exact rational source and target subspaces, computes their intersection dimensions by exact ranks, and checks the resulting minimum correction rank for deterministic shift profiles through the selected size. This finite replay checks coefficient indexing and the subspace calculation; the two-case argument is the all-size proof.

This result covers coordinate translations only. Arbitrary linear long-leg maps, non-coordinate variable-window maps, general source restrictions, independent review, Lean formalization, and exponent improvement remain unclaimed.
