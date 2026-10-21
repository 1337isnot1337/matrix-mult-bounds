# Minimum-rank slices of Q(n,m) and loss of A dimensions

**Status: written proof with exact coefficient controls; no external
mathematical review.** These are structural statements about ordinary
quotients. The separate note `narrow_regular_long_legs_obstruction.md`
states the precisely limited consequence for Laurent families.

## 1. A source-slice rank bound

For integers `n,m≥1`, write

\[
Q_{n,m}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

Let X be a nonzero n-by-n matrix of A-slice coefficients, of rank r.
Then

\[
\operatorname{rank} Q_{n,m}(X)\ge r+m^2-1.
\tag{1}
\]

In particular the minimum nonzero slice rank is `m²`, and it is attained
exactly when X has matrix rank one.

### Proof of the bound

The slice matrix has rows `(y,j)`, columns `(z,v)`, and entries

\[
S_X[(y,j),(z,v)]=X_{z-y,j-v},
\]

where an X entry outside its n-by-n range means zero. For each p, let

\[
g_p(t)=\sum_{q=0}^{n-1}X_{p,q}t^q,
\qquad W=\langle g_0,\ldots,g_{n-1}\rangle.
\]

Thus `dim W=r`. Consider first the B row block `y=m−1`. As z and v vary,
its columns are precisely the coefficient vectors of the polynomials
`t^v g_p(t)`. Its rank is therefore

\[
\dim(W+tW+\cdots+t^{m-1}W)\ge r+m-1.
\tag{2}
\]

To justify the inequality, successively add the spaces `t^j W`. At each
step a polynomial with the largest degree in `t^j W` has degree strictly
larger than every polynomial previously present. Hence every step raises
the dimension by at least one.

Let `p0` be the first index with `g_(p0)≠0`. Add the other B row blocks in
descending order, from `y=m−2` to `y=0`. For a new block y, inspect the m
C columns `(z,v)=(p0+y,v)`, `0≤v<m`. Every previously included block
`y'>y` vanishes on these columns, since `p0+y−y'<p0`. On the new block,
these m columns are the coefficient vectors of

\[
g_{p0}(t),\ t g_{p0}(t),\ldots,t^{m-1}g_{p0}(t),
\]

which are linearly independent. Restricting the row span to these m
coordinates therefore shows that the new block adds at least m to its
dimension. Combining all `m−1` additions with (2) gives

\[
\operatorname{rank}S_X\ge(r+m-1)+(m-1)m=r+m^2-1.
\]

If X has rank one, write `X_(p,q)=f_p g_q`. Its source slice is

\[
\sum_{y,v<m}
\left(\sum_qg_q B_{y,q+v}\right)
\left(\sum_pf_p C_{p+y,v}\right).
\]

Each family of m² vectors is independent, because multiplication by a
nonzero polynomial is injective. The slice rank is therefore exactly m².
If X has rank at least two, (1) makes its slice rank larger than m². ∎

## 2. Every full Q(n,2) quotient loses at most one A direction

Let B and C be arbitrary surjections from their source dimensions
`2(n+1)` to `2n`, with two-dimensional kernels `K_B,K_C`. Let

\[
S=(\mathrm{id}_A\otimes B\otimes C)Q_{n,2}.
\]

Then its A flattening has rank at least `n²−1`:

\[
\dim\ker\bigl(S:A^*\to B'\otimes C'\bigr)\le1.
\tag{3}
\]

### Proof

If a nonzero A parameter X is annihilated by both quotients, its source
slice loses all its rank. The two quotients can reduce matrix rank by at
most `2+2=4`. Equation (1), with m=2, therefore forces X to have rank one.
Write `X=f⊗g`, using degree-`n−1` homogeneous binary polynomials.

Its two four-dimensional source images are

\[
E_g=U_2\otimes gP_1,\qquad F_f=fP_1\otimes U'_2.
\]

To lose all four ranks, the two image-kernel intersections must both have
dimension two. Consequently

\[
K_B\subset E_g,\qquad K_C\subset F_f.
\tag{4}
\]

There is an additional orthogonality condition. Identify E_g and F_f by
the matched `(y,v)` coordinates of the pure slice. If `R,S⊂C⁴` are the
preimages of K_B and K_C, the projected identity matrix is zero exactly
when

\[
S=R^\perp
\tag{5}
\]

for the coordinate bilinear pairing. Indeed the quotient rank is
`4−dim R−dim S+rank(pairing on R×S)`, so it is zero precisely when the
pairing vanishes. Both subspaces have dimension two.

Choose any fixed nonzero vector of K_B. At least one of its two degree-n
polynomial components is nonzero. Every g in (4) divides that fixed
polynomial, so only finitely many projective g are possible. The same
argument gives only finitely many projective f. Hence there are only
finitely many projective pure parameters satisfying (4).

The A-flattening kernel is a linear space and all its nonzero elements
are among those finitely many pure lines. A linear space of dimension at
least two has infinitely many projective points. This proves (3). ∎

This reasoning does not assume that S is matrix multiplication or that its
nonzero slice ranks are even. The rank loss of one can occur: the crossed
jet quotient in the companion certificate has A kernel exactly `span A00`.

## 3. Consequence for a leading A pole

Suppose A(t) has Laurent coefficients, B(t) and C(t) are regular at zero,
and their values at zero are the full surjections above. Let the leading
negative coefficient of A(t) be `A_(-d)`, with d positive. If
`(A(t)⊗B(t)⊗C(t))Q` has no negative powers, then

\[
(A_{-d}\otimes B(0)\otimes C(0))Q=0.
\]

Every row functional of `A_(-d)` lies in the A-flattening kernel in (3).
Thus `rank A_(-d)≤1`. If this leading coefficient is nonzero, its input
functional is a pure `f⊗g`, and the two kernel planes obey (4)–(5).

This gives a concrete parameterization for the base of such an attempted
family: two degree-`n−1` forms f,g and one plane `R∈Gr(2,4)`, with the
opposite plane fixed to be `R^perp`. It does not by itself construct a
family or account for singular leading maps on B or C.

## 4. Exact controls

The companion script checks the source ranks for all 511 nonzero binary
3-by-3 A matrices in Q(3,2). The rank pairs and counts are

| Rank of X | Rank of source slice | Count |
|---:|---:|---:|
| 1 | 4 | 49 |
| 2 | 6 | 160 |
| 2 | 8 | 128 |
| 3 | 7 | 66 |
| 3 | 8 | 108 |

It also checks every descending row-block increment on 42 selected
parameters, covering `n=2,3,4,5`, `m=2,3,4`, and every A rank from 1 to n.
All arithmetic is exact over Q. The symbolic proof, rather than the
finite sample, establishes the theorem for all complex parameters.

The same certificate includes the complete crossed-jet rank-five slice
used in `narrow_regular_long_legs_obstruction.md`, with a determinant-one
five-by-five minor and only five nonzero columns.

```sh
python research/ai/2026-10-20-paired-construction/narrow_rank_locus.py --output research/ai/2026-10-20-paired-construction/narrow-rank-locus.json
python -m unittest discover -s tests -p test_narrow_rank_locus.py -v
```
