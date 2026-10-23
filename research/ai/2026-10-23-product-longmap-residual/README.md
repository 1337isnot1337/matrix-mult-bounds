# First-map freedom with the fixed product long maps

**Status: proof written, exact finite replay supplied; same-session review
does not constitute external mathematical review.** This note concerns the
two particular long-leg maps in
[`q_product_projection.py`](../2026-10-20-paired-direct-sums/q_product_projection.py).
It allows every linear map on the first leg. It proves no obstruction for
other long-leg maps or for a general tensor degeneration. It gives no new
matrix-multiplication exponent.

## 1. Exact result

Let `K` be a field of characteristic different from two and let `n >= 5`.
Put `r = n-1`. The paired convolution tensor and matrix target are

\[
 Q(n,4)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{3}
 A_{pq}B_{y,q+v}C_{p+y,v},\qquad
 M(r,4,r)=\sum_{i,k=0}^{r-1}\sum_{j=0}^{3}
 a_{ik}b_{ij}c_{jk}.
\]

Fix the two long maps `B_old,C_old` defined in Section 3. For any first map
`A : K^(n^2) -> K^(r^2)`, write

\[
 E_A=M(r,4,r)-(A\otimes B_{\rm old}\otimes C_{\rm old})Q(n,4).
\]

Here `rank_A(E_A)` means the ordinary matrix rank of the first
flattening of the residual tensor. The subscript names the tensor leg;
it does not mean a rank of the chosen local map.

**Theorem.** With these two long maps fixed,

\[
 \boxed{\min_A\operatorname{rank}_A(E_A)
 =(n-1)^2-\max(9-n,1)^2.}                         \tag{1}
\]

The old product first map already attains the minimum. Thus changing only
that first map cannot concentrate the error on fewer first-leg slices.
In particular, for every `n >= 8`, the minimum is `(n-1)^2-1`.

| `n` | Target first dimension | Source/target slice intersection | Minimum residual first rank |
| --- | ---: | ---: | ---: |
| 5 | 16 | 16 | 0 |
| 6 | 25 | 9 | 16 |
| 7 | 36 | 4 | 32 |
| 8 | 49 | 1 | 48 |
| 9 | 64 | 1 | 63 |
| 10 | 81 | 1 | 80 |
| 11 | 100 | 1 | 99 |
| 12 | 121 | 1 | 120 |
| 16 | 225 | 1 | 224 |
| 32 | 961 | 1 | 960 |

Over the rationals, the prior reference proves a nonzero `(n-5)^2`
diagonal residual minor for its particular first map. Formula (1)
computes its complete first rank
and permits an arbitrary replacement of the first map. It retains the
same two long maps throughout.

## 2. Two linear-algebra lemmas

### 2.1 Optimizing the first map is a quotient-space rank problem

Let `S,T` be subspaces of a finite-dimensional vector space `Z`, and
regard `T` as the target slice space. Among all linear maps `F:T -> S`,

\[
 \min_F\operatorname{rank}(\iota_T-F)
 =\dim T-\dim(S\cap T),                          \tag{2}
\]

where `iota_T:T -> Z` is the inclusion.

**Proof.** Let `q:Z -> Z/S` be the quotient. Since `qF=0`, every residual
`iota_T-F` has rank at least the rank of `q iota_T`, which is the
right-hand side of (2). For equality, choose a complement
`T=(S cap T) direct_sum T_1`. Define `F` to equal the inclusion on
`S cap T` and to vanish on `T_1`. The residual then has image `T_1`.

For a tensor with two local maps fixed, all rows of the remaining local
map can be chosen independently. Consequently its slice map can realize
every `F:T -> S`; a surjection onto `S` has a linear section. Formula
(2) therefore applies even when the source slice map has a kernel.

### 2.2 Intersections of product subspaces

If `H_1,W_1` are subspaces of `Z_1` and `H_2,W_2` are subspaces of `Z_2`,
then

\[
 (H_1\otimes H_2)\cap(W_1\otimes W_2)
 =(H_1\cap W_1)\otimes(H_2\cap W_2).             \tag{3}
\]

**Proof.** Choose, in each `Z_i`, a basis of `H_i cap W_i`; extend it to
a basis of `H_i`, to a basis of `W_i`, and then to a basis of `Z_i`.
These extensions are compatible because the complements of the
intersection in `H_i` and `W_i` have zero intersection. Products of the
chosen bases give a basis of `Z_1 tensor Z_2`. The basis products that
occur in both spaces on the left of (3) are exactly the products of the
two intersection bases. This proves (3) over every field.

## 3. The fixed long maps, without a numerical ansatz

Set `m=n+3`. Identify `K^m` with coefficient lists
`z=(z_0,...,z_(n+2))`, and put

\[
 \alpha_s=\begin{cases}\tfrac12,&4\le s\le n-2,\\1,&\text{otherwise}.
 \end{cases}
\]

Define linear functionals `L_(i,a):K^m -> K`, with `0 <= i < r` and
`a in {0,1}`, as follows. For `1 <= t <= n-2`,

\[
\begin{aligned}
 L_{t-1,0}(z)&=\alpha_t z_t+\mathbf1_{t=3}z_{n+2},\\
 L_{t-1,1}(z)&=\alpha_{t+3}z_{t+3}
                    +\mathbf1_{t=n-4}z_0.
\end{aligned}                                                   \tag{4}
\]

For the last outer index,

\[
 L_{r-1,0}(z)=z_0,\qquad L_{r-1,1}(z)=-z_{n+2}.                 \tag{5}
\]

These are exactly the rational `dual` rows in the pinned old file.
The long maps keep only native short indices zero and three. With
`a,b,y,v in {0,1}`, their coefficients are

\[
\begin{aligned}
 (B_{\rm old})_{(i,2y+a),(Y,s)}
   &=\mathbf1_{Y=3y}\,(L_{i,a})_s,\\
 (C_{\rm old})_{(2b+v,k),(s,V)}
   &=\mathbf1_{V=3v}\,(L_{k,b})_s.
\end{aligned}                                                   \tag{6}
\]

The target row ordering is `b_(i,j)` and `c_(j,k)`. All entries not
specified in (6) are zero.

Let `V=K^n` with coefficient indices `0,...,n-1`, and let
`U=K^r`. Write `E_b:V -> K^m` for the shift by `3b`:
`(E_b x)_s=x_(s-3b)`, interpreting coefficients outside `0,...,n-1`
as zero. Define

\[
 H:V\longrightarrow U\otimes K^{2\times2},\qquad
 H(x)_{i,a,b}=L_{i,a}(E_bx),
 \quad W=U\otimes\operatorname{span}\{I_2\}.                    \tag{7}
\]

The `n` vectors `H(e_q)` are independent. Indeed their diagonal entries
recover every coefficient: the regular `(i,0,0)` entries recover
`x_1,...,x_(n-2)` through nonzero factors `alpha_t`; the two last-index
diagonal entries recover `x_0` and `-x_(n-1)`.

## 4. The paired slice spaces factor

For a source first slice `X=(X_(p,q))`, the compressed long-leg matrix
has coefficient

\[
 \sum_{p,q}X_{p,q}
       L_{i,a}(E_v e_q)L_{k,b}(E_y e_p)                          \tag{8}
\]

at the target long-leg coordinate pair
`(b_(i,2y+a),c_(2b+v,k))`.

Regroup the six indices as `(i,a,v)` and `(k,b,y)`. This is a fixed
permutation of coordinates of the ambient matrix space, so it preserves
the dimension of every slice space and every intersection. Equation
(8) shows that the full source slice space becomes

\[
 S=H(V)\otimes H(V).
\]

The target coefficient for a first slice `Y=(Y_(i,k))` is
`Y_(i,k) delta_(y,b) delta_(a,v)`. Under the same regrouping, its slice
space becomes

\[
 T=W\otimes W.
\]

The source and target dimensions are consequently `n^2` and `r^2`.
By (3),

\[
 \dim(S\cap T)=\dim(H(V)\cap W)^2.                             \tag{9}
\]

This factorization depends on the long maps in (6). In particular,
mixing the native short blocks differently can destroy it.

## 5. Solving the one-factor intersection

For a regular index `i=t-1`, equations (4) and (7) give

\[
\begin{aligned}
 H(x)_{t-1,0,0}&=\alpha_t x_t,\\
 H(x)_{t-1,0,1}&=\alpha_t x_{t-3}+\mathbf1_{t=3}x_{n-1},\\
 H(x)_{t-1,1,0}&=\alpha_{t+3}x_{t+3}
                                      +\mathbf1_{t=n-4}x_0,\\
 H(x)_{t-1,1,1}&=\alpha_{t+3}x_t.
\end{aligned}                                                  \tag{10}
\]

At the final outer index the matrix is

\[
 H(x)_{r-1}=\begin{pmatrix}x_0&0\\0&-x_{n-1}\end{pmatrix}.
\]

Membership in `W` means that each of these two-by-two matrices is a
scalar multiple of the identity. The off-diagonal equations and the
last diagonal equation are equivalent to

\[
 x_0+x_{n-1}=0,\qquad
 x_1=\cdots=x_{n-5}=0,\qquad
 x_4=\cdots=x_{n-2}=0,                                         \tag{11}
\]

where an empty interval imposes no equations. These equations also
imply every remaining diagonal equality in (10). To see this, an
interior coefficient that survives (11) must have `n-4 <= t <= 3`;
for these indices both `alpha_t` and `alpha_(t+3)` equal one.

Thus the complete inverse image of `W` is

\[
 H^{-1}(W)=\operatorname{span}\{e_0-e_{n-1}\}
   \;\oplus\;\operatorname{span}\{e_t:n-4\le t\le3\}.           \tag{12}
\]

As `H` is injective,

\[
 d:=\dim(H(V)\cap W)=1+\max(8-n,0)=\max(9-n,1).                \tag{13}
\]

Combining (2), (9), and (13) proves the minimum in (1).

## 6. The old first map attains the minimum

Let `O:U -> V` have columns

\[
 O(e_i)=e_{i+1}\quad(0\le i\le r-2),\qquad
 O(e_{r-1})=e_0-e_{n-1}.                                      \tag{14}
\]

Let `J:U -> W` be `J(u)=u tensor I_2`, and let `G` be the span in `U`
of `e_(r-1)` and all `e_(t-1)` with `n-4 <= t <= 3`. Equations
(10)--(12) prove

\[
 H(Ou)=J(u)\quad\text{for every }u\in G,\qquad \dim G=d.
\]

The old first map has coefficient
`A_((i,k),(p,q))=O_(p,k) O_(q,i)`. Its compressed target slice map is
`(HO) tensor (HO)`, after the regrouping above. Its residual therefore
vanishes on `G tensor G`, a space of dimension `d^2`. Its first rank
is at most `r^2-d^2`, while (1) gives the reverse inequality. Equality
follows, and the kernel is exactly `G tensor G`.

## 7. Reproducible checks and limits

`verify.py` independently constructs (4)--(7), checks the complete
one-factor equations over the rationals, and calculates all required
dimensions by exact Gaussian elimination. Its optional direct replay
forms the complete paired source and target slice matrices and checks
their ranks without using (3). All arrays are scaled by two in each
factor to keep their entries integral; ranks are unchanged.

The certificate includes `n=5,...,12`, a larger direct paired replay,
and larger one-factor controls. The test file checks boundary cases,
the old-map coefficient correspondence, arbitrary-first-map rank
minimization on a separate example, and deliberate perturbations. A
floating optimization is neither used nor accepted as a proof.

The direct rational paired replay includes `n=16`. One-factor rational
controls also include `n=32,64,200`; the theorem supplies their paired
formula. Direct checks in characteristics three and five confirm the
stated characteristic scope. In characteristic three the prior `3/4`
minor vanishes, while the complete rank in (1) is unchanged.

From the repository root:

```sh
python -S research/ai/2026-10-23-product-longmap-residual/verify.py
python -S -m unittest discover -s tests -p test_product_longmap_residual.py -v
```

The verifier is standalone. When running the test file in a scratch
package before integration, set `MATRIX_BOUNDS_REFERENCE_REPO` to the
repository root so the tests can validate the old-source byte pins.

The separate scratch rank-two residual pilot at `n=6` is not part of
this theorem or its certificate. Its nonzero error proves nothing about
the existence of other maps. The fixed long maps here use the same
product structure as the old injection construction; a new construction
can change either long map or leave this product structure entirely.

## Sources and provenance

The exact source definition and two long maps are pinned to
`research/ai/2026-10-20-paired-direct-sums/q_product_projection.py`, SHA-256
`5fafd9b140f04a438ea2b1d3cf34aa71cd7c391a2d7f3ba367586aa07015f156`.
The previous product-injection construction is in
[`outer_product_injection.md`](../2026-10-20-paired-construction/outer_product_injection.md),
pinned in `sources.json`. All lemmas and the full residual-rank formula
above are proved in this note. No external tensor obstruction is imported.
