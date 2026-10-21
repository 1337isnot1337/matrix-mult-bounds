# Newton-support peeling excludes every ordinary fixed-torus profile

## Result

There is no ordinary restriction

\[
 A(8,8)\longrightarrow M_{27}\oplus M_7
\]

that maps target matrix units homogeneously for the source grading

\[
 \operatorname{weight}F(i,k,s)=i+s-k.
 \tag{1}
\]

This includes **all integer vertex-charge lists on all three target
vertex spaces**, including unequal lists, holes, different widths, and
different charge lists for the two matrix summands. No enumeration of
vertex-charge profiles is used. The three linear maps may be unrelated.

The proof repeatedly removes source coordinates that cannot occur in
any homogeneous target matrix-unit image. The exact dimensions are

\[
 960\longrightarrow922\longrightarrow834\longrightarrow468<778.
 \tag{2}
\]

The target has dimension `27^2+7^2=778` on every leg, so the final
inequality contradicts injectivity of its parameter maps.

The statement concerns ordinary maps preserving the fixed source
grading. It does not exclude ungraded maps, maps with cross-weight
coefficients, or arbitrary singular degenerations. It does not
establish a smaller matrix multiplication exponent. The ungraded
`A(8,8) -> M27 direct_sum M7` construction remains open in this work.

Two other agents checked the proof in this generating session. One
also replayed all three rounds with separate hull and rank code. The
primary certificate verifier does not use a convex-hull algorithm:
it checks exact separating lines for every removed point. There has
been no external independent review or proof-assistant formalization.

## Source coordinates and exact coordinate-slice ranks

Put `m=a+b-1` and `N=abm`. Use the common coordinate order

\[
 F(i,k,s),\qquad 0\le i<a,\quad0\le k<m,\quad0\le s<b.
\]

The common-order source tensor is

\[
 S=A(a,b)=
 \sum_{\substack{0\le i,p,r<a\\0\le j,q,s<b}}
 X_{i,p+q,s}\,Y_{p,r+s,j}\,Z_{r,i+j,q}.
 \tag{3}
\]

The three common coordinate spaces have the same dimension. Formula
(3) is cyclic: rotate `(i,p,r)` and `(j,q,s)` in the corresponding
orders to rotate the tensor legs.

Every pair of source coordinates appears in at most one term. For
example, from `X=(i,k,s)` and `Y=(p,ell,j)`, the only possible third
coordinate has

\[
 q=k-p,\qquad r=\ell-s,\qquad Z=(r,i+j,q),
\]

provided the short indices are in range. The two cyclic versions give
the same uniqueness for the other coordinate pairs. Therefore a slice
at any fixed source coordinate is a partial permutation matrix: each
of its rows and columns has at most one nonzero entry, and each such
entry is one.

Let `K` be any common subset of the source coordinates, and restrict
all three parameter spaces to their span. Write the resulting tensor
as `S_K`. A coordinate slice of `S_K` is still a partial permutation
matrix. Its rank is exactly

\[
 r_K(c)=\#\{\text{terms of (3) through }c
                   \text{ whose other two coordinates lie in }K\}.
 \tag{4}
\]

The three rank tables agree because the common coordinate restriction
is cyclic. The certificate verifier computes all three tables and
checks this agreement; it does not merely assume it from one table.
It also checks injectivity of all three pair projections of the full
source support. The ranks in (4) are exact over every field.

## The rank budget improves after removing coordinates

Suppose a concise target tensor `T`, of dimension `D` on each leg,
is realized by three ordinary parameter maps into `K`. Each map is
injective. Suppose further that each target leg has a homogeneous
basis all of whose slice ranks are at most `r`.

For any one of these basis vectors `e`, let `F=J(e)` be its source
image. The matrix of the slice `S_K(F)` restricts on the other two
leg images to the target slice `T(e)`. Each of these two images has
codimension `|K|-D`. Deleting that many row and column directions
can lower matrix rank by at most their sum. Consequently

\[
 \operatorname{rank}S_K(F)
 \le r+2(|K|-D)=:R(K).
 \tag{5}
\]

For `M27 direct_sum M7`, take the matrix-unit basis on each leg.
Every unit is homogeneous for any integer vertex-charge assignment.
Its slice is a matching with 27 entries in the large summand, or
seven in the small summand. Thus

\[
 D=778,\qquad r=27.
 \tag{6}
\]

After a valid coordinate removal, the actual maps land in a smaller
common space `K'`. They remain injective. Applying (5) with `K'`
therefore gives a smaller rank budget. It would be incorrect to keep
using the original codimension after establishing this stronger
containment; the new codimension is exactly `|K'|-D`.

## A source torus exposes each Newton vertex

The primary grading (1) is not the only diagonal symmetry of (3).
For any integers `alpha,beta`, assign the following auxiliary weights:

\[
\begin{aligned}
 d_X(i,k,s)&=-\beta k+\alpha s,\\
 d_Y(i,k,s)&= \beta i-\alpha k,\\
 d_Z(i,k,s)&= \alpha i+\beta s.
\end{aligned}
 \tag{7}
\]

Their sum on each term of (3) is zero. Hence multiplying source
coordinates by the corresponding powers of a formal parameter is a
diagonal tensor symmetry. Every coordinate restriction `S_K` retains
this symmetry, because its diagonal actions preserve `K`.

On a fixed primary weight `w`, the long index is determined by
`k=i+s-w`. Thus the projection

\[
 F(i,k,s)\longmapsto(i,s)
\]

is injective on that weight space. For a homogeneous source slice
`F`, take the convex hull of its nonzero coefficient positions in
the `(i,s)` plane. This is its Newton polygon, with segments and
singletons allowed.

Every vertex `c` of this polygon can be uniquely minimized by an
integer linear functional `alpha*i+beta*s`. Use (7) on the `Z` leg,
and multiply the transformed slice by a common power of the formal
parameter so that its lowest exponent is zero. The leading slice is
the nonzero coefficient of `F` at `c` times the coordinate slice.
Before specializing the parameter to zero, the other two leg matrices
have merely undergone invertible diagonal changes and a nonzero
scalar multiplication. Therefore

\[
 r_K(c)\le\operatorname{rank}S_K(F).
 \tag{8}
\]

This is a rank calculation over a Laurent rational-function field,
followed by polynomial specialization. It does not assume convergence
of a numerical optimization. Cyclic rotation gives the same statement
for images in either of the other two legs.

## One exact removal step

For each primary weight `w`, define the admissible coordinate set

\[
 G_w(K)=\{c\in K:\operatorname{weight}(c)=w,
                         \ r_K(c)\le R(K)\}.
 \tag{9}
\]

By (5) and (8), every Newton vertex of a homogeneous target basis
image belongs to `G_w(K)`. The support of that image must therefore
lie in the convex hull of the projected points of `G_w(K)`. In
particular, every coefficient at a point outside this hull vanishes.
If `G_w(K)` is empty, no nonzero homogeneous target basis image can
have weight `w`.

This conclusion applies to every homogeneous matrix unit separately.
Those units span each target leg, so linearity puts the **entire**
leg image into the resulting coordinate subspace `K'`. The same
`K'` works on all three source legs, independently of the target
charge lists. Equation (5) now applies with `K'`, and the procedure
can be repeated.

For the certificate it is not necessary to prove that every possible
coordinate was removed. Any set of removals justified by (9) gives
a valid smaller containing space and hence a valid next rank budget.

## The three exact rounds for A(8,8)

Here `N=8*8*15=960`. The exact computation gives:

| Round | Input dimension | Retained source terms | Rank budget `27+2(|K|-778)` | Removed coordinates | Output dimension |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 960 | 262,144 | 391 | 38 | 922 |
| 1 | 922 | 211,240 | 315 | 88 | 834 |
| 2 | 834 | 123,472 | 139 | 366 | 468 |

The final dimension 468 is smaller than the required dimension 778
of each injective target map. This contradiction proves the stated
ordinary graded restriction exclusion.

The first round has a direct geometric interpretation. On the
zero-weight source space, `k=i+s`. The two corner coordinates

\[
 a_0=F(0,7,7),\qquad b_0=F(7,7,0)
\]

each have full source slice rank 512. For example, fixing the `Z`
coordinate to `a_0` leaves exactly the matching

\[
 X=(i,p+7,s),\qquad Y=(p,s,7-i),
 \qquad0\le i,p,s<8.
\]

The 512 row coordinates and 512 column coordinates are all distinct.
If a zero-weight image has a nonzero coefficient at either corner,
the corresponding corner is exposed and (8) gives rank at least 512,
contradicting 391. The adjacent exposed points with `|i-s|=6` have
coordinate-slice rank 448 and are also removed. Thus the zero-weight
dimension first drops from 64 to 58. Performing the same hull step
on all weights removes 38 coordinates in total.

The corner calculation also explains the earlier endpoint arguments.
Whenever a composable pair of extreme target units would force
`a_0` or `b_0` to be nonzero in a zero-weight matrix-unit lift, its
source rank would be at least 512. Removing 182 row directions and
182 column directions would leave rank at least 148, while the target
slice has rank at most 27. The peeling proof additionally handles
profiles with no extreme target units at all.

## Certificate format and independent verification

The report records every current coordinate-slice rank, every removed
coordinate, and an integer separating line for each removal. For a
removed point `(i,s)`, that line has coefficients `A,B,C` satisfying

\[
 A i'+B s'\le C\quad\text{for every point in }G_w(K),
 \qquad A i+B s>C.
 \tag{10}
\]

If `G_w(K)` is empty, the report explicitly records that case.
The verifier recomputes (4), (5), and (9) before checking (10).
It never calls either the hull-construction function or the
point-in-polygon function. Thus a defect in the discovery hull code
cannot validate an unjustified removal. The final contradiction
requires only the certified removals and the resulting dimension.

For this certificate the verifier checks all three pair projections
of the 262,144 source terms, all three coordinate-rank tables in each
round, and 10,544 separating-line inequalities. It validates 492
coordinate removals. A separate worker's implementation, stored in
`parity_balancing_newton_pruning_audit.py` with its result report,
independently obtains the same dimensions and all three rank tables.
This is a second-agent check within the generating session, not
external independent review.

The tests reject altered separators and altered rank budgets. They
also disable the discovery geometry while verifying the saved
certificate, check small actual identity and matrix restriction
controls that must survive, and replay the exposed-corner rank
formulas at unequal source sizes as well as at `(8,8)`.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/torus_support_peeling.py
python -S research/ai/2026-10-20-anisotropic-constructions/torus_support_peeling.py --verify results/anisotropic-constructions-2026-10-20/torus-support-peeling-a88-m27-m7.json
python -S -m unittest discover -s tests -p test_torus_support_peeling.py -v
```

The formal role of the computation is finite: it certifies the three
sets of removals in (2). The written rank and torus arguments explain
why each certified removal constrains every proposed ordinary map.
No conclusion about unrestricted maps or singular limiting maps is
drawn from the same finite calculation.
