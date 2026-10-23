# Geometric diagonal-polynomial slices: exact ranks in every characteristic

October 23, 2026. Owner-directed AI-assisted mathematical work. Status: **proof written, unreviewed**. No matrix-tensor degeneration or exponent improvement is claimed.

## Theorem

Let \(K\) be any field, \(a\ge2\), \(1\le d<a\), and \(c,\lambda\in K^\times\). Put
\[
g(x,z)=c\sum_{k=0}^d(\lambda xz)^k,\qquad m=d+1,\qquad q=a\bmod m\in\{0,\ldots,m-1\}.
\]
In the maintained cyclic-source coefficient convention,
\[
R_a(g)_{(j,L),(H,r)}=[x^{H-j}z^{L-r}]g,
\quad 0\le j,r<a,\quad 0\le H,L<2a-1,
\]
one has the exact formula
\[
\boxed{\operatorname{rank}_K R_a(g)=a^2+ad-E_m(q)},\qquad
E_m(q)=\begin{cases}0&q=0,\\(q-1)(m-q)&1\le q<m.\end{cases} \tag{1}
\]
It is valid over **every** field, with no characteristic restrictions or exceptional values of \(c,\lambda\). The largest defect over residue classes is \(\lfloor d^2/4\rfloor\), achieved for infinitely many \(a>d\) for each fixed \(d\).

The finer statement is as follows. For \(1\le \ell\le d\), put \(r=d-\ell\) and
\[
T_{a,\ell}[u,v]=c_{\ell+v-u},\qquad
c_k=\begin{cases}c\lambda^k&0\le k\le d,\\0&\text{otherwise.}\end{cases}
\]
Then
\[
\dim_K\ker T_{a,\ell}=
\begin{cases}
0&q=0,\\
\min\{\ell,d-\ell,q-1,m-q\}&1\le q<m.
\end{cases}\tag{2}
\]
Explicit all-field kernel bases are given below.

This settles simultaneous defects of the central Toeplitz blocks for this geometric-progression subfamily of the degree-\(d\) diagonal polynomials. It does **not** classify arbitrary coefficient vectors.

## I. Reduction from the original source tensor

An entry of \(R_a(g)\) vanishes unless \(H-j=L-r\), so both indices have conserved sum \(s=j+L=H+r\). After independent permutations of the row and column bases, the source is the direct sum of blocks
\[
B_s[u,v]=c_{s-u-v},\quad
u,v\in I_s=[\max(0,s-2a+2),\min(a-1,s)]\cap\mathbb Z,\quad
0\le s\le3a-3.
\]
For \(0\le s<a\), reversing columns makes \(B_s\) triangular with diagonal \(c_0\ne0\), contributing ranks \(1,\ldots,a\). For \(a+d\le s\le2a+d-2\), discarding the zero rows and columns and reversing columns makes it triangular with diagonal \(c_d\ne0\), contributing ranks \(a-1,\ldots,1\). Blocks at larger \(s\) vanish. The other \(d\) blocks have \(s=a,\ldots,a+d-1\); all their row and column index sets equal \(\{0,\ldots,a-1\}\). Reversing their columns gives precisely \(T_{a,\ell}\) for \(\ell=1,\ldots,d\). Therefore
\[
\operatorname{rank}R_a(g)=a^2+\sum_{\ell=1}^d\operatorname{rank}T_{a,\ell}.\tag{3}
\]
This all-degree decomposition was already derived in [concurrent PR #207](https://github.com/1337isnot1337/matrix-mult-bounds/pull/207). It is included here to make the proof stand independently of that unmerged PR; priority for (3) is not claimed.

## II. Kernel of one banded block

Write \(T^{(1)}_{a,\ell}\) for the block with \(d+1\) consecutive coefficients equal to one. There is an exact invertible diagonal factorization
\[
T_{a,\ell}=c\lambda^\ell
\operatorname{diag}(\lambda^{-u})_{u=0}^{a-1}
T^{(1)}_{a,\ell}
\operatorname{diag}(\lambda^v)_{v=0}^{a-1}.\tag{4}
\]
It suffices to calculate the kernel of \(T^{(1)}\).

Extend a vector \(x=(x_0,\ldots,x_{a-1})\) by zero outside its index interval. Its row equations are
\[
S_u=\sum_{v=u-\ell}^{u+r}x_v=0,\quad 0\le u<a,\qquad \ell+r=m-1.
\]
For \(1\le u<a\), consecutive-row subtraction gives
\[
0=S_u-S_{u-1}=x_{u+r}-x_{u-\ell-1}.\tag{5}
\]
The two indices differ by \(m\). Because \(a\ge m\), these equations identify *all* in-range entries with the same residue modulo \(m\), except for the residue classes set to zero by the boundary equations. At the left boundary, \(u=1,\ldots,\ell\) kills
\[
L_\ell=\{r+1,\ldots,m-1\}\subseteq\mathbb Z/m\mathbb Z.
\]
At the right boundary, \(u=a-r,\ldots,a-1\) kills
\[
R_\ell=\{(a-m+i)\bmod m:0\le i<r\}.
\]
These exhaust the equations in (5) having exactly one in-range index: the interior pairs are all linked, and \(a\ge m\) precludes simultaneous left/right overflows.

Set \(F_\ell=(\mathbb Z/m\mathbb Z)\setminus(L_\ell\cup R_\ell)\). Since \(|L_\ell|=\ell\), \(|R_\ell|=r\), and \(\ell+r=m-1\),
\[
|F_\ell|=1+|L_\ell\cap R_\ell|.\tag{6}
\]
Every free residue lies in \(\{0,\ldots,r\}\); at least one remains free. The one equation not implied by (5) is \(S_0=x_0+\cdots+x_r=0\), the sum of the free residue values. Its coefficients are one and it is nonzero over every field. Thus
\[
\dim\ker T_{a,\ell}=|L_\ell\cap R_\ell|.\tag{7}
\]

An explicit basis is available. Select any \(p\in F_\ell\). For each \(j\in F_\ell\setminus\{p\}\), let
\[
x^{(j)}_i=\lambda^{-i}
\bigl(\mathbf 1_{i\bmod m=j}-\mathbf 1_{i\bmod m=p}\bigr),\quad 0\le i<a.\tag{8}
\]
These vectors are linearly independent (each free residue occurs in the index range) and satisfy the entire equation system. Their number is (7), so they span the kernel. The same argument works in characteristic two.

If \(q=0\), the right boundary residues are \(\{0,\ldots,r-1\}\), disjoint from \(L_\ell\); the defect is zero. If \(1\le q<m\), the wrapped portion of \(R_\ell=\{q,\ldots,q+r-1\}\bmod m\) is strictly below \(r+1\) and misses \(L_\ell\). The intersection reduces to that of the ordinary integer intervals \([q,q+r-1]\) and \([r+1,m-1]\), of size
\(\min\{\ell,r,q-1,m-q\}\). This proves (2).

## III. Exact sum of the simultaneous defects

Suppose \(1\le q<m\), and substitute \(t=m-\ell\). Then \(t\) runs from \(1\) through \(m-1\). A residue \(j\) belongs to \(L_\ell\cap R_\ell\) exactly when
\[
q\le j\le m-1,\qquad t\le j,\qquad j\le q+t-2,\tag{9}
\]
because wrapped right-boundary residues never contribute. For each fixed \(j=q,\ldots,m-1\), (9) allows exactly the \(q-1\) values
\[
t=j-q+2,\ldots,j.
\]
Double-counting gives
\[
\sum_{\ell=1}^d|L_\ell\cap R_\ell|=(m-q)(q-1).\tag{10}
\]
For \(q=0\), all intersections vanish. Substitute \(\operatorname{rank}T_{a,\ell}=a-|L_\ell\cap R_\ell|\) into (3) to obtain (1). Finally, the two nonnegative factors \(q-1\) and \(m-q\) sum to \(m-1=d\), proving \(E_m(q)\le\lfloor d^2/4\rfloor\).

For \(d=2\), this recovers PR #207's \(1+t+t^2\) defect at \(a\equiv2\pmod3\). At \(d=3\), defects are \(0,0,2,2\) for residues \(0,1,2,3\) modulo four. At \(d=4\), they are \(0,0,3,4,3\).

## Reproduction, provenance, limitations

The standard-library verifier in this package builds the literal unpermuted coefficient matrix separately from the Toeplitz kernel generator. It checks ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), both available ratios \(1,2\), nonzero scalars, the explicit kernel basis, conserved-index blocks, and every individual defect. These bounded computations are controls, not the proof of the all-field assertion.

The original source convention was checked at SHA-256 \`4ca101d6e82faca9ddf0c8a5852f57c4857b088bcc2eb9ba201c0e8b39c8fa63\` in \`research/ai/2026-10-20-koszul/cyclic_finite_target.md\`. The earlier arbitrary-biform source \`research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md\` has SHA-256 \`43c90e01de6d87ee56b733eb332829b0cbec839ea331f7063fc5f5a5515eea71\`. PR #207 at \`09041022f0bb8dd2233eee95eec0017ee6998b1e\` retains credit for the all-degree block identity and quadratic case. PRs #171 and #186 have distinct, non-imported biform results. No external theorem is imported or historical priority asserted.

The claim is about individual rank-deficient diagonal slices. It does not prove a bounded-rank linear space, an actual three-leg tensor construction, a characteristic-zero Laurent lift, a border-rank target, or an exponent less than \(9/4\). The remaining bottleneck is compatibility of these individual defects across multiple slices and all three tensor legs.