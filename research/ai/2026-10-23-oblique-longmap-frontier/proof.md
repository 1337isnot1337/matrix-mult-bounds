# Fixed good rows and exact finite long-map screens

## 1. Source, target and surjective benchmark

Work over a field k. The source and target are

\[
 Q(6,4)=\sum_{p,q=0}^{5}\sum_{y,v=0}^{3}
 A_{pq}B_{y,q+v}C_{p+y,v},\qquad
 M(5,4,5)=\sum_{i,j=0}^{4}\sum_{\alpha=0}^{3}
 a_{ij}b_{i\alpha}c_{\alpha j}.
\]

Their formats are `(36,36,36)` and `(25,20,20)`. Map matrices are
target by source. The source coordinate orders are `6p+q`, `9y+z`
and `4z+v`; the target orders are `5i+j`, `4i+alpha` and `5alpha+j`.
All coefficients below are integers.

Use outer polynomials

\[
 (U_0,U_1,U_2,U_3,U_4)=(t,t^2,t^3,1-t^4,t^5),
 \qquad (W_0,W_1)=(1,t^3).
\]

On a coefficient vector z of length nine, define ten decoder rows,
ordered by `(i,a)`, as

\[
 (L_{00},L_{01},L_{10},L_{11},L_{20},L_{21},L_{30},L_{31},L_{40},L_{41})
 =(z_1,z_0+z_4,z_2,z_5,z_3+z_7,z_6,z_0,-z_7,0,z_8).
\]

These decode all products `U_i W_a` except `U_4 W_0=t^5`, which duplicates
`U_1 W_1`. Begin with the inherited product-map template

\[
\begin{aligned}
 A_{(i,j),(p,q)}&=(U_j)_p(U_i)_q,\\
 B_{(i,2a+v),(y,z)}&=(W_a)_y(L_{iv})_z,\\
 C_{(2a+v,j),(z,V)}&=(L_{ja})_z(W_v)_V.
\end{aligned}                                                    \tag{1}
\]

Add four coefficients equal to one:

\[
 B_{(4,0),(1,8)},\quad B_{(4,2),(2,8)},\quad
 C_{(0,4),(8,1)},\quad C_{(1,4),(8,2)}.             \tag{2}
\]

The sixteen good B rows have `i<4`; the sixteen good C rows have `j<4`.
Each good block has independent decoder rows on native long coordinates
zero through seven. The four added outer rows use the four distinct
native short sectors at long coordinate eight. Thus both long maps are
surjective over every field. The certificate also records unit
twenty-by-twenty minors for those assertions.

The [prior exact Q(5,4) construction](../2026-10-20-paired-construction/outer_product_injection.md)
gives the exact M4 corner with `i,j<4`. Its source first coefficients
have `p,q<=4`, so the new long-coordinate-eight entries do not change
that corner. Hence the residual of (1)--(2) is supported on the nine
first coordinates with `i=4` or `j=4`. Section 3 proves the matching
lower bound nine over every field. Exact rational native contraction
also gives the full residual rank vector `(9,18,18)`. Those two long-leg
residual ranks are reported over Q, not asserted uniformly in every
characteristic.

This benchmark does not improve the earlier residual ranks `(9,11,11)`
or their scalar costs. Its purpose is to supply full long-map ranks.

## 2. Optimizing the entire first map

Fix any two long maps. Let S be the image of the raw source first-slice
map in the space of twenty-by-twenty matrices. Let T be the
twenty-five-dimensional target slice space. The elementary
[quotient formula](../2026-10-23-product-longmap-residual/README.md#21-optimizing-the-first-map-is-a-quotient-space-rank-problem)
is

\[
 \min_A r_A\bigl(M-(A\otimes B\otimes C)Q\bigr)
 =25-\dim(S\cap T).                                      \tag{3}
\]

Indeed, passage to the quotient by S gives the lower bound. For equality,
choose a complement of `S intersect T` in T and a section of the source
slice map onto S. Match the intersection and use zero on the complement.
Every row of the first local map is free, so this construction is allowed.
There is no product or coordinate restriction on A in (3).

## 3. Universal bound with the good rows fixed

**Theorem.** Keep the sixteen good B rows and sixteen good C rows from
(1). Change the remaining four rows on each leg arbitrarily, including
their coefficients in every native source column. Then every first map
has residual first rank at least nine, over every field. The benchmark
(2) attains nine; arbitrary fillers need not attain equality.

Project each output long leg onto its sixteen good coordinates, and
write this two-leg projection as pi. The projected target slice space
`pi(T)` has dimension sixteen. We show that the raw thirty-six-dimensional
source first-slice map into `pi(S)` is injective.

There is a small explicit unit minor. Inside the good B block choose rows

\[
 R_B=(12,0,4,8,1,5),
\]

and inside the good C block, ordered locally as `4alpha+j`, choose

\[
 R_C=(3,0,1,2,8,9).
\]

These rows select native short coordinates `y=0` and `v=0`, respectively.
The surviving six decoder forms on each degree-at-most-five coefficient
vector are

\[
 (x_0,x_1,x_2,x_3,x_0+x_4,x_5).
\]

Their matrix is `F=I_6+E_(4,0)`, with determinant one. In source row order
`(p,q)` and selected output column order `(u,v)`, the thirty-six-square
minor has entries

\[
 F_{u,p}F_{v,q}.
\]

It is `F^T tensor F^T`, so its determinant is one. The verifier reconstructs
all native source contributions and checks this entire matrix identity;
the saved record only needs its column indices and the small matrix F.
The minor remains nonzero over every field.

Arbitrary filler rows do not change pi. Consequently pi is injective on
the full compressed source slice space S, for every choice of fillers.
It follows that

\[
 \dim(S\cap T)=\dim\pi(S\cap T)\le\dim\pi(T)=16.
\]

Equation (3) gives the claimed lower bound nine. This theorem fixes the
good output rows. It is not a theorem about unrestricted long maps or
their Laurent degenerations.

## 4. The 384 finite shift controls

Start with the full benchmark maps. Choose distinct inner coordinates
`a,b` in `{0,1,2,3}`, two shifts `sigma_B,sigma_C` in `{-1,1}`, two signs
`epsilon_B,epsilon_C` in `{-1,1}`, and one bit tau. On every outer index
make the changes

\[
\begin{aligned}
 B'_{(i,a),(y,z)}&=B_{(i,a),(y,z)}
       +\epsilon_B B_{(i,b),(y,z+\sigma_B)},\\
 C'_{(a',j),(z,v)}&=C_{(a',j),(z,v)}
       +\epsilon_C C_{(b',j),(z+\sigma_C,v)},
\end{aligned}                                                    \tag{4}
\]

where `(a',b')=(a,b)` if tau is zero and `(a',b')=(b,a)` otherwise.
Out-of-range native long indices contribute zero. All other rows stay
unchanged. There are exactly `12*2^5=384` parameter tuples. These changes
affect old good rows, so Section 3 does not by itself settle this screen.

For each tuple, compute the source slice space S modulo T. A quotient
map deletes the `alpha=0` pivot from each target slice and subtracts its
coefficient from the other three diagonal-inner positions. All 384
quotient matrices have a twenty-by-twenty minor nonzero modulo 32003.
The matrices have integer coefficients, so their rational rank is at
least twenty. Since `dim(S)<=36`,

\[
 25-\dim(S\cap T)=25-\dim S+\dim((S+T)/T)\ge25-36+20=9.
\]

This is a complete finite check of (4) at the listed parameter values.
It is not a theorem for all shift filters, all rational parameters,
variable-coefficient families or growing n. No modular rank upper bound
is promoted to a rational upper bound.

## 5. The 61 valid mixed-middle corner controls

Retain the four outer polynomials `(t,t^2,t^3,1-t^4)` and `W=(1,t^3)`.
Use the middle basis, expressed in `P_3 tensor span(W)`,

\[
\begin{aligned}
 H_0&=1\otimes W_0,\\
 H_1&=1\otimes W_1+(at+bt^2)\otimes W_0,\\
 H_2&=t^3\otimes W_0+(ct+dt^2)\otimes W_1,\\
 H_3&=t^3\otimes W_1,
\end{aligned}                                                    \tag{5}
\]

for all 81 tuples `(a,b,c,d)` in `{-1,0,1}^4`. This follows the prior
[mixed-middle template](../2026-10-20-paired-construction/mixed_middle_boundary.py).
The eight products `U_i W_v` have an invertible eight-square coefficient
matrix. The sixteen products `U_j H_alpha` have a sixteen-square
coefficient matrix D. Invert these two product matrices to define the
long maps, with zero coefficients at native long coordinate eight.

When D is invertible, the product-decoder identities give an exact M4
corner. The first contraction decodes `U_i W_v`; the second decodes
`U_j H_alpha`. This proves the corner identity over any field where D
is invertible. The verifier separately reconstructs all 4096 target
coefficient positions modulo 32003 for every valid tuple.

Exactly sixty-one tuples have nonzero determinant modulo 32003. Each
then defines the same rational maps by matrix inversion, since the
integer denominator determinant is nonzero and not divisible by the
prime. Every raw source first-slice matrix has a thirty-six-square
minor nonzero modulo the prime. Its rational first-slice map is
therefore injective as well. The projection argument of Section 3
gives first residual lower bound nine for arbitrary fillers extending
each of these sixty-one fixed rational corners.

The other twenty tuples are recorded as singular modular decoders and
are skipped. Their modular singularity is not used as a general
rational exclusion. No claim is made for parameters outside this finite
grid. In particular, this census does not classify mixed-middle corners.

## 6. Evidence and limitations

The full native contraction, selected unit minors, all finite screen
minors and all product-decoder determinants are reconstructible from
[frontier.py](frontier.py). Five inherited source files are pinned in
[sources.json](sources.json). No earlier implementation or test is
modified. Tests include altered and omitted certificate records.

The universal theorem permits arbitrary first maps and arbitrary
filler coefficients, while fixing the good rows. The finite screens
permit a different explicitly enumerated choice of good rows on each
control. Neither statement excludes unrestricted long maps, arbitrary
first-map mixing with changed long maps, or general degenerations.
No first residual below nine or exponent improvement is constructed.
