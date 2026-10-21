# Source-weight windows and an exact three-term rank cancellation

## Result

In every ordinary restriction

\[
 A(8,8)\longrightarrow M_{27}\oplus M_7,
\]

**at least one target matrix-unit image must contain source weights
whose difference is at least four**, for the fixed source weight

\[
 \operatorname{wt}F(i,k,s)=i+s-k.
 \tag{1}
\]

The interval containing each image may depend on that matrix unit and
on the leg. No relation to target vertex charges is required. The
statement therefore applies to arbitrary target charge choices and to
maps that already mix source weights.

This is a bound on the *span* of the nonzero source weights, not their
number. For example, weights `-2,0,2` have span four but use only three
weight spaces. The previous result in
[`parity_balancing_mixed_grading.md`](parity_balancing_mixed_grading.md)
separately requires at least 19 images using three or more weight
spaces on each of two legs.

The present calculation excludes maps for which every matrix-unit
image lies in some interval of span at most three. It does not exclude
ordinary maps with larger spans, or arbitrary singular degenerations.
No smaller matrix multiplication exponent is established.

An exact positive rank control realizes the first surviving span:

\[
 F=F(0,5,7)+\varphi F(0,7,7)+F(0,9,7),
 \qquad \varphi^2=\varphi+1.
 \tag{2}
\]

Its full source slice has rank `384`, while its middle weight component
has rank `512`. Thus the middle component can have larger rank than the
whole three-weight slice. This is an actual cancellation in the source
matrix, not only a convex-hull possibility. It is a single source
parameter direction; it is not a three-leg matrix multiplication map.

## The three-dimensional Newton argument

Use the common source tensor

\[
 S=\sum_{i,p,r,j,q,s=0}^{7}
 X_{i,p+q,s}Y_{p,r+s,j}Z_{r,i+j,q}.
 \tag{3}
\]

Each leg has 960 coordinates `F(i,k,s)` with `0<=i,s<8` and
`0<=k<15`. Its full diagonal torus has weights

\[
\begin{aligned}
 d_X(i,k,s)&=a i+b k+c s,\\
 d_Y(i,k,s)&=-b i-c k+a s,\\
 d_Z(i,k,s)&=c i-a k-b s.
\end{aligned}
\tag{4}
\]

The sum on every term of (3) is zero. On each individual leg, the
three parameters realize every linear functional in `(i,k,s)`.
Every coordinate restriction of the source retains these diagonal
symmetries.

Allow different coordinate masks `K_X,K_Y,K_Z`. Each coordinate slice
of the restricted source is a partial permutation matrix, so its rank
is the number of remaining source terms through that coordinate.
Every hypothetical full target map is injective. A lifted target
matrix unit on leg `i` consequently has slice rank at most

\[
 R_i=27+\sum_{j\ne i}(|K_j|-778).
 \tag{5}
\]

The proof is the row and column codimension estimate already used in
the mixed-grading note. It is applied to the currently restricted
source, so the smaller masks give smaller rank budgets.

For an arbitrary source slice, form the convex hull of its nonzero
coefficient positions in three dimensions. Each vertex is exposed by
an integer linear functional from (4). Normalize the corresponding
torus action and specialize its parameter to zero. The resulting
coordinate slice cannot have greater rank than the original slice.
Every such Newton vertex therefore has coordinate-slice rank at most
`R_i`.

Suppose the source weights of an image lie in the interval `[u,u+B]`.
Its support must be contained in the convex hull of

\[
 G_{i,u}=
 \{F(i',k,s)\in K_i:
    u\leq i'+s-k\leq u+B,
    \ \operatorname{rank}S_K(F(i',k,s))\leq R_i\}.
 \tag{6}
\]

The particular interval is unknown. A coordinate can therefore remain
only if it lies in at least one of these hulls. Take their union over
all integer starts `u=-14,...,14-B`. This range covers every possible
support interval in the source. Remove coordinates outside the union,
and repeat (5) and (6). Linearity puts the entire leg image in the new
mask because the matrix units span its domain.

The argument does not isolate the individual weight components of a
three-weight image. It exposes vertices of the full three-dimensional
support at once, which is why it remains valid when the middle
component has the larger rank illustrated by (2).

## Exact finite certificate

The stored certificate contains `306` integer supporting planes and
`222` references to interval polytopes. A plane is an inequality

\[
 a i+b k+c s\leq d
\]

with all four coefficients integral. For every interval of every
selected leg in every round, the verifier reconstructs the admissible
set (6), then checks that **every admissible coordinate satisfies every
supplied plane**. It recomputes the coordinates retained by the union
of those polyhedra and checks every resulting dimension and mask hash.
It also reconstructs the full source and all coordinate ranks.

For the exclusion proof, it is enough that the supplied polyhedra
contain the actual hulls. Facet completeness and numerical hull
accuracy are not assumptions: removing only coordinates separated by
verified inequalities is a valid, possibly weaker, pruning step.
Numerical convex-hull code was used to discover candidate planes. The
acceptance verifier uses only integer arithmetic and the Python
standard library.

When all three legs satisfy the same maximum-span condition, the
three masks agree. The exact rounds are:

| Maximum span | Available dimension | Slice-rank budget | Retained dimension |
| ---: | ---: | ---: | ---: |
| 2 | 960 | 391 | 940 |
| 2 | 940 | 351 | 876 |
| 2 | 876 | 223 | 740 |
| 3 | 960 | 391 | 948 |
| 3 | 948 | 367 | 906 |
| 3 | 906 | 283 | 844 |
| 3 | 844 | 159 | 622 |

Both final dimensions are below 778. Span at most three on all images
is therefore impossible, proving the stated necessary span of four.

The separate-mask controls are deliberately narrower in scope:

| Selected legs | Maximum span | Final mask dimensions | Outcome of this screen |
| --- | ---: | --- | --- |
| Two | 2 | `(876,876,960)` | Stable; no exclusion |
| Two | 3 | `(906,906,960)` | Stable; no exclusion |
| Three | 4 | `(960,960,960)` | No first-step pruning |
| Two | 4 | `(960,960,960)` | No first-step pruning |

Thus this calculation alone does not require a span of four on two
legs. The stronger cardinality statement about two legs comes from
the separate two-weight argument, and should not be conflated with
this span statement.

There is also a direct explanation of the span-four fixed point.
Before restriction, the slice at `F(i,k,s)` has rank

\[
 64\min(k+1,15-k).
\]

At the initial budget `391`, every coordinate with `k<=5` or `k>=9`
is admissible. Any remaining coordinate has `k=6,7,8`, and lies on the
segment between the admissible coordinates `F(i,5,s)` and `F(i,9,s)`.
Those endpoints have source weights differing by four. Their common
span-four interval therefore already contains the given coordinate
in its admissible hull. Every source coordinate survives the exact
first hull step. This is a limitation of the support test, not a
construction of the target maps.

## Exact rank cancellation at weights -2, 0, and 2

Let `h_5=h_9=1`, `h_7=phi`, and let all other `h_k` vanish. Form the
eight-by-eight Hankel matrix

\[
 H_{pq}=h_{p+q},\qquad 0\leq p,q<8.
\]

Even-even and odd-odd entries vanish. Reordering by parity and reversing
the appropriate four columns leaves two independent copies of

\[
 T=\begin{pmatrix}
 \varphi&1&0&0\\
 1&\varphi&1&0\\
 0&1&\varphi&1\\
 0&0&1&\varphi
 \end{pmatrix}.
\]

Its vector `(1,-phi,phi,-1)` is in the kernel. Its leading
three-by-three minor is

\[
 \varphi^3-2\varphi=1.
\]

Hence `rank(T)=3` and `rank(H)=6`. The verifier independently performs
Gaussian elimination over `Q(phi)` and checks these displayed kernel,
minor, and parity-block identities.

For the source slice (2), fixing each pair `(r,j)` in (3) leaves
the row/column block

\[
 Y_{p,r+7,j}\;Z_{r,j,q}
 \quad\text{with coefficient }h_{p+q}.
\]

The 64 choices of `(r,j)` have disjoint rows and columns. The entire
source slice is therefore a direct sum of 64 copies of `H`, plus
zero rows and columns, and has rank `64*6=384`. The verifier checks
this identity against all `262144` source terms; the slice has 1280
nonzero entries. Keeping only the middle coordinate gives 64 copies
of an invertible anti-diagonal eight-by-eight matrix, of rank 512.

Thus the full three-term slice obeys the initial target-lift budget
`384<=391` even though its middle homogeneous component does not.
Its weights are `2,0,-2`, so it uses the minimum surviving span in
this screen. This supplies an explicit candidate direction for an
ungraded map search. It supplies no complete matrix tensor and has
no standalone asymptotic-sum or exponent consequence.

## Reproduction and review scope

From the repository root:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_weight_windows.py
python -S -m unittest discover -s tests -p 'test_parity_balancing_weight_windows.py'
```

The JSON is a complete exact-plane certificate, not a cache of trusted
rank results. Focused tests alter a supporting plane, an exclusion
claim, and a nonzero atom coefficient and require rejection. The
reported result has not received external independent review or
proof-assistant formalization.
