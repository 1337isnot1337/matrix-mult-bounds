# Shift-separation rank forces a quadratic paired-source repair

October 23, 2026. Owner-directed AI-derived proof. Written and unreviewed; not formalized.

## Statement

Let `K` be a field, `n >= 1`, and `m >= 2`. Use the maintained paired-convolution source and matrix target

\[
Q_{n,m}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
 A_{p,q}B_{y,q+v}C_{p+y,v},\qquad
M_{n,m,n}=\sum_{i,h=0}^{n-1}\sum_{t=0}^{m-1}a_{i,h}b_{h,t}c_{t,i}.
\]

The first-leg map `A` is arbitrary. Choose finite nonnegative bandwidths `D_B,D_C`, exceptional source-column sets `E_B,E_C` of sizes `e_B,e_C`, and scalar profiles `alpha_1,...,alpha_J` on `{0,...,n+m-2}`. On every nonexceptional B column `s`, require

\[
B_{y,s}\longmapsto
\sum_{t=0}^{m-1}\sum_{k=-D_B}^{D_B}\sum_{j=1}^J
\alpha_j(s)\,\beta^{(j)}_{y,t,k}\,b_{s-k,t}.
\tag{1}
\]

Terms whose target index `s-k` is out of range are omitted. On every nonexceptional C column `z`, require the Toeplitz rule

\[
C_{z,v}\longmapsto
\sum_{u=0}^{m-1}\sum_{\ell=-D_C}^{D_C}
\gamma_{v,u,\ell}c_{u,z-\ell},
\tag{2}
\]

with the same out-of-range convention. Maps on exceptional columns are unrestricted.

Put

\[
L=m-1+\max(D_B,D_C),\qquad
I=\{L,L+1,\ldots,n-1-L\}.
\]

For each profile define its shift matrix

\[
\Phi_j=(\alpha_j(q+v))_{q\in I,\ 0\le v<m},
\qquad \delta_j=\operatorname{rank}_K(\Phi_j),
\qquad \Delta=\sum_{j=1}^J\delta_j.
\tag{3}
\]

If `I` is empty, its matrices have rank zero. Assume `Delta < m`. For `T=(A,B,C)(Q_{n,m})` and residual `R=M_{n,m,n}-T`,

\[
\boxed{\operatorname{rank}_{A\mid B\otimes C}(R)\ \ge\ g_Bg_C,\qquad
\underline R(R)\ \ge\ g_Bg_C,}
\tag{4}
\]

where

\[
g_B=\max(0,n-2L-me_B),\qquad
g_C=\max(0,n-2L-me_C).
\]

The border-rank lower bound holds over an algebraic closure of `K`. If `m` is fixed and `D_B,D_C,e_B,e_C=o(n)`, then `g_Bg_C=n^2-o(n^2)`. Thus an auxiliary tensor of border rank `o(n^2)` cannot repair this ordinary restriction to the full target: if the sum `Q_{n,m}\oplus S` maps ordinarily to `M_{n,m,n}`, then the image of `S` equals the residual, and linear maps cannot increase border rank. In particular, the stated map class cannot meet an `O(n^alpha)` repair budget for any `alpha<2`.

## Proof

Use the Laurent polynomial ring `K[X^{±1},Y^{±1}]` and its fraction field `K(X,Y)`. Encode a tensor on the B and C target legs as an `m` by `m` matrix whose `(t,u)` entry records the coefficients of `b_{h,t}c_{u,i}` as `X^hY^i`.

For each `j`, matrix rank in (3) gives functions `f_{j,r}:I->K` and `g_{j,r}:{0,...,m-1}->K`, for `1<=r<=delta_j`, such that

\[
\alpha_j(q+v)=\sum_{r=1}^{\delta_j}f_{j,r}(q)g_{j,r}(v)
\quad(q\in I,\ 0\le v<m).
\tag{5}
\]

Define column vectors of Laurent polynomials

\[
F^{(j)}_t(X,Y)=\sum_{y=0}^{m-1}\sum_{k=-D_B}^{D_B}
\beta^{(j)}_{y,t,k}X^{-k}Y^y,
\]

\[
G^{(j,r)}_u(X,Y)=\sum_{v=0}^{m-1}\sum_{\ell=-D_C}^{D_C}
g_{j,r}(v)\gamma_{v,u,\ell}X^vY^{-\ell}.
\]

Take `p,q` in `I`, outside the exceptional-column neighborhoods: `p+y not in E_C` for every `y`, and `q+v not in E_B` for every `v`. All prescribed formulas apply. The output indices are in `{0,...,n-1}` by the definition of `L`, so truncation does not occur. Direct substitution into the `(p,q)` source slice gives its symbol matrix

\[
X^qY^p\sum_{j=1}^J\sum_{r=1}^{\delta_j}
f_{j,r}(q)\,F^{(j)}(X,Y)G^{(j,r)}(X,Y)^T.
\tag{6}
\]

Each summand is an outer product. The q-dependence has been separated by (5); this is why the rank bound applies after summing different source slices.

Let `P_good` and `Q_good` be the surviving p and q indices, and `G=P_good x Q_good`. Each exceptional column removes at most `m` indices from the interior interval `I`, so

\[
|P_{good}|\ge g_C,\qquad |Q_{good}|\ge g_B,
\qquad |G|\ge g_Bg_C.
\tag{7}
\]

Contract the first target leg against a functional `w=(w_{i,h})`, and write `a_{p,q}(w)` for its coefficient on the source coordinate `A_{p,q}`. Let `V` be the subspace defined by `a_{p,q}(w)=0` for every `(p,q) not in `G`. These impose at most `n^2-|G|` linear conditions on an `n^2`-dimensional space, so `dim(V)>=|G|`.

For `w in V`, summing (6) shows that the symbol matrix of the contracted image `T(w)` is a sum of at most `Delta` outer products. Therefore it has rank at most `Delta<m` over `K(X,Y)`. The contracted target has symbol matrix

\[
M(w)=\left(\sum_{i,h=0}^{n-1}w_{i,h}X^hY^i\right)I_m.
\tag{8}
\]

If `R(w)=0`, then (8) equals the symbol matrix of `T(w)`. A nonzero Laurent polynomial times `I_m` has rank `m`, contradicting `Delta<m`; hence the Laurent polynomial in parentheses is zero. Distinct monomials imply every `w_{i,h}=0`. Thus contraction by `R` is injective on `V`, proving the flattening bound in (4). Flattening rank is a lower bound for border rank, which gives the second inequality. This proof works over every field.

## Limits

The hypothesis is on a displayed coefficient presentation (1): the sum of the shift-matrix ranks in (3) must be below `m`. A generic profile can have shift rank `m`, and the proof says nothing then. The other long-leg map must obey (2) outside its specified exceptional columns. The result covers ordinary restrictions only; it does not control arbitrary variable-coefficient maps, arbitrary Laurent degenerations, or cancellations with auxiliary pole terms. The bound is not an exponent improvement.
