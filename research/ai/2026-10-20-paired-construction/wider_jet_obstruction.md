# A boundary-jet quotient fails at every inner width

**Status: written proof with complete local coefficient controls and a
same-session audit by a second agent; no external mathematical review.**
This excludes one specified ordinary B quotient of
Q(n,m), independently of the other quotient. It does not classify all
kernels for m greater than two, and it does not exclude singular families.

## The specified quotient

Let `m≥2`, `n≥m+1`, and let J be the m-by-m matrix with ones immediately
above the main diagonal and zeros elsewhere. For

\[
Q_{n,m}=\sum_{p,q<n}\sum_{y,v<m}A_{p,q}B_{y,q+v}C_{p+y,v},
\]

apply this map on B:

\[
B_{y,j}\longmapsto
\begin{cases}
(-J)^{m-1-j}e_y,&0\le j<m,\\
b_{m+(j-m)m+y},&m\le j<n+m-1.
\end{cases}
\tag{1}
\]

Here `e_y=b_y` are the first m output basis vectors; the later b vectors
are independent. This is a surjection from dimension `m(n+m−1)` to `mn`.
Its kernel has dimension `m(m−1)` and is contained in the first m layers
of B. The quotient is specified in the native polynomial coefficient
basis. No claim about arbitrary conjugates of J on the source U factor
is needed.

**Claim.** After (1), no ordinary map on C and invertible map on A can
produce `M(n,m,n)`.

## Proof

Suppose the claimed matrix multiplication tensor were obtained. Define,
after the unspecified C quotient,

\[
c_{p,\alpha}=\sum_{v=\alpha}^{m-1}
(-1)^{m-1-v} C_{p+\alpha+m-1-v,v},
\quad 0\le p<n,\quad0\le\alpha<m.
\tag{2}
\]

The entire q=0 slice fibre is

\[
S(A_{p,0})=\sum_{\alpha=0}^{m-1} b_\alpha c_{p,\alpha}.
\tag{3}
\]

These n linearly independent slice parameters have all their images in
the fixed m-dimensional space spanned by `b0,...,b_(m−1)`. In
`Mat_n⊗I_m`, every such nonzero slice corresponds to a rank-one matrix
with one fixed image line. The n-dimensional parameter space must be its
complete row fibre. Consequently the mn vectors in (2) form a basis of C,
with the n paired dual blocks

\[
\langle c_{p,0}^*,\ldots,c_{p,m-1}^*\rangle.
\]

Every other matrix multiplication slice restricts to each of these blocks
with rank either zero or m: that restriction is one matrix column tensored
with the identity of order m.

The defining identities (2) give, when `z≥m`,

\[
C_{z,v}=(-1)^{m-1-v}
\bigl(c_{z-m+1,v}-c_{z-m,v+1}\bigr)
\quad(0\le v<m-1),
\tag{4}
\]

and

\[
C_{z,m-1}=c_{z-m+1,m-1}.
\]

The parameter `A_(m,1)` exists because `n≥m+1`. Its full slice is

\[
\begin{aligned}
S(A_{m,1})={}&
\sum_{y=0}^{m-1}\sum_{v=\max(0,m-2-y)}^{m-2}
b_{y-m+2+v}\bigl(c_{y,v+1}-c_{y+1,v}\bigr)\\
&+\sum_{y=0}^{m-1}b_{m+y}c_{y+1,m-1}.
\end{aligned}
\tag{5}
\]

On the p=0 paired dual block, only y=0 contributes. The inner sum then
contains only `v=m−2`. Thus the restriction of (5) to that block is

\[
b_0c_{0,m-1},
\]

which has rank one. This contradicts the required rank zero or m. The
contradiction is independent of the C quotient. ∎

## Exact coefficient controls

The script `wider_jet_obstruction.py` expands every source coefficient for
`(n,m)=(3,2),(4,3),(5,4),(13,4)`. It checks all n identities (3), the whole
matrix identity (5), and every zero outside the stated support.

The script retains the original C vectors with `z<m−1` as `m(m−1)` free
coordinates, alongside all mn vectors (2). This is an integer coordinate
change of determinant plus or minus one on the full original C space.
Equation (5) has zero coefficients on every free coordinate. Therefore
arbitrary eventual images of those coordinates cannot repair its rank-one
block.

For the smallest m=4 control, Q(5,4) has format `(25,32,32)` and the
candidate target has format `(25,20,20)`. The certificate stores both full
coordinate maps, the complete `20×32` offending matrix, and its `20×4`
paired block. The larger Q(13,4) control checks the same identity at the
first n covered by the wider divisor-incidence criterion in
`narrow_ordinary_all_n.md`.

```sh
python research/ai/2026-10-20-paired-construction/wider_jet_obstruction.py --output research/ai/2026-10-20-paired-construction/wider-jet-obstruction.json
python -m unittest discover -s tests -p test_wider_jet_obstruction.py -v
```

These finite controls calibrate the symbolic identity. The written formula
proves this specific ordinary-quotient obstruction for every `m≥2` and
`n≥m+1`. Other B kernels and all singular Laurent relaxations remain open.
