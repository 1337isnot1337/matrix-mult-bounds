# Full-channel overlap and the cost of leading rank loss

October 23, 2026. Owner-directed OpenAI Codex work. Claim
`AI-PAIRED-COLUMN-OVERLAP-001` is written and unreviewed.
No matrix multiplication exponent improves.

## 1. Result and scope

The paired source is

\[
Q_{n,m}=\sum_{p,q<n}\sum_{y,v<m}
 A_{p,q}B_{y,q+v}C_{p+y,v},\qquad n\ge1,\quad m\ge2.
\]

Its first leg has dimension `n^2`; each other leg has dimension
`m(n+m-1)`. The target is

\[
M(l,m,r)=\sum_{i<l,j<r,\alpha<m}
 a_{i,j}b_{j,\alpha}c_{\alpha,i},\qquad D=lr.
\]

Work over a field K, with O=K[[t]] and L=K((t)). Choose injections

\[
\sigma_B:\{0,\ldots,r-1\}\longrightarrow\{0,\ldots,n+m-2\},
\quad
\sigma_C:\{0,\ldots,l-1\}\longrightarrow\{0,\ldots,n+m-2\}.
\]

At retained source polynomial columns, the long maps are

\[
B_{y,\sigma_B(j)}\mapsto
 \sum_{\alpha<m}\beta_j(t)_{y,\alpha}b_{j,\alpha},\qquad
C_{\sigma_C(i),v}\mapsto
 \sum_{\delta<m}\gamma_i(t)_{v,\delta}c_{\delta,i},       \tag{1}
\]

where each channel matrix belongs to Mat_m(O). Other source columns
map to zero. The coefficients may depend arbitrarily on the retained
column. In particular, their common shift-window span and their channel
rank may both be full. The routing injections are fixed for the family.

For a source column s define its covered first indices

\[
J(s)=\{s-m+1,\ldots,s\}\cap\{0,\ldots,n-1\}.
\]

Let U_B be the union of J(sigma_B(j)) over all retained B columns.
Let U_B^g use only columns whose beta_j(0) is invertible. Define U_C and
U_C^g in the same way. Put

\[
N=|U_B||U_C|,\qquad G=|U_B^g||U_C^g|.
\]

For each side, retain only its good source-column positions in the full
window interval `[m-1,n-1]`. Join two positions when their distance is
strictly less than m. Let c_B,c_C be the numbers of connected components,
with zero for an empty set, and put c=c_B c_C.

**Theorem.** Suppose arbitrary Laurent first maps and arbitrary Laurent
maps on a fixed auxiliary tensor R give

\[
(A(t),B(t),C(t))Q_{n,m}+E_R(t)=M(l,m,r)+O(t).            \tag{2}
\]

The two contributions in (2) need not be regular separately. Then

\[
\boxed{\operatorname{rank} R_{A\mid BC},\ \underline R(R)
 \ \ge\ \max(0,D-N+G-c).}                            \tag{3}
\]

The flattening statement holds over every field for the stated formal
identity. Over C it gives the displayed usual border-rank lower bound.
This is a restriction on the maps (1), not a lower bound for arbitrary
paired-source constructions. Mixing distinct polynomial columns on
either long leg is outside the theorem.

## 2. The ordinary leading intersection

Let H_0 be the first-slice plane of `(id,B(0),C(0))Q`. Write a first
parameter as f=(f_pq), extending it by zero outside the source square.
At target outer position (i,j), its m-by-m channel block is

\[
\beta_j(0)^T F_{ij}(f)\gamma_i(0),\qquad
F_{ij}(f)_{y,v}=f_{\sigma_C(i)-y,\sigma_B(j)-v}.       \tag{4}
\]

Let T be the target first-slice plane. Its blocks are `w_ij I_m`.
If either channel matrix in (4) is singular, equality with a target
slice forces w_ij=0. The same conclusion holds if either window is
outside `[m-1,n-1]`: F then has a zero row or a zero column.

At a remaining good pair, both matrices are invertible, so

\[
F_{ij}(f)=w_{ij}\,\beta_j(0)^{-T}\gamma_i(0)^{-1}.
                                                               \tag{5}
\]

Consider two good C positions separated by delta with `0<delta<m`,
and fix one good B position. Their windows share `m-delta` full rows.
Restricting (5) to these common source rows gives

\[
w_{ij}K=w_{i'j}K',                                      \tag{6}
\]

where K and K' are nonzero matrices. Each consists of a nonempty subset
of rows of an invertible matrix. Thus the two scalar coordinates either
are proportional with a fixed nonzero ratio, or both must vanish.
The same argument for B positions uses common columns.

The graph on good outer pairs is the Cartesian product of the two
position graphs. It has c_B c_C connected components. Along each
component, (6) leaves at most one scalar degree of freedom; a cycle may
remove that degree of freedom. All other scalar coordinates vanish.
Consequently

\[
\dim(H_0\cap T)\le c.                                 \tag{7}
\]

This argument needs invertibility of individual channel matrices, not
low rank of a common channel factor. It also explains why separated
routing components cannot be omitted from the bound.

## 3. Count every direction created by a singular leading map

Let H(t) be the first-slice plane of `(id,B(t),C(t))Q` over L, and
write r_gen=dim H(t), r_0=dim H_0. Source parameters outside U_C x U_B
have zero image for every t, hence

\[
r_{\rm gen}\le N.                                     \tag{8}
\]

At every good leading pair, (4) can be inverted to read the entire
coefficient window of f. These windows cover U_C^g x U_B^g. A parameter
in the leading slice-map kernel therefore vanishes on every one of its
G coordinates, proving

\[
r_0\ge G.                                              \tag{9}
\]

Let bar(H) be the saturated limit of H(t): intersect H(t) with the
ambient free O-module and reduce modulo t. This intersection is a
saturated submodule over the discrete valuation ring O. A Smith basis,
or successive elimination of lowest valuations, shows that its reduction
has dimension r_gen. Every regular source column reduces into bar(H),
so H_0 is contained in bar(H). Therefore

\[
\dim\bigl(\bar H/H_0\bigr)=r_{\rm gen}-r_0\le N-G.
\]

Passing from H_0 to bar(H) can enlarge its intersection with any fixed
linear space by at most that quotient dimension. Combining with (7),

\[
\dim(\bar H\cap T)\le c+N-G.                          \tag{10}
\]

In particular, no coefficientwise limit of a raw polar source column
has been taken. Saturation accounts for cancellations and for every
new slice direction.

## 4. Auxiliary poles cannot evade the dimension budget

Let k be the first flattening rank of E_R(t) over L. It is at most the
first flattening rank of R. Its kernel V in the D-dimensional target
first-covector space has dimension at least D-k.

The saturated lattice V intersect O^D has a reduction bar(V) of the same
dimension. For each of its basis vectors w(t), equation (2) gives

\[
(A(t),B(t),C(t))Q(w(t))
 =M(w(0))+O(t),                                        \tag{11}
\]

because E_R(t)(w(t)) is exactly zero over L. Each right side lies in the
saturated source lattice. Its reduction lies in bar(H). Since M has
injective first flattening, the independent vectors of bar(V) give at
least D-k independent members of bar(H) intersect T. By (10),

\[
D-k\le c+N-G.
\]

This proves the flattening bound (3). A tensor of border rank q has
first flattening rank at most q: its `(q+1)` minors vanish on rank-q
tensors and on their closure. This supplies the border-rank conclusion.
Ramified formal parameters may be renamed t. No bound on first-map or
auxiliary pole orders is needed.

## 5. Consequences for a scalable construction

If every retained leading channel matrix is invertible, U_B^g=U_B and
U_C^g=U_C. The lower bound is simply

\[
\underline R(R)\ge D-c_Bc_C.                          \tag{12}
\]

For contiguous full-window routing on each side, c_B=c_C=1. Thus even
full channel rank leaves an auxiliary first-flattening cost at least
`lr-1`. Arbitrary first-map poles do not change this conclusion.

More generally, fix m and take l/n,r/n to one. Suppose all but o(n) of
the retained leading channel matrices are invertible on each side.
The retained injections omit o(n) source columns. A good source-column
set of size n-o(n) covers n-o(n) first indices: the map
`s -> min(s,n-1)` is injective except for at most m-1 upper-end positions.
Thus G=n^2-o(n^2), while N is at most n^2.

Each extra connected component among the good interior positions needs
at least m-1 missing positions between components. Hence c_B,c_C=o(n),
and (3) yields

\[
\underline R(R)\ge n^2-o(n^2).                        \tag{13}
\]

The construction criterion requires a subquadratic correction. A route
within (1) must therefore use extensive leading singularity, or change
the routing model to mix polynomial columns.

There is a quantitative version, still with fixed m and l/n,r/n tending
to one. Suppose the fractions of retained
leading invertible blocks, divided by n, tend to alpha and beta. The
coverage and missing-position counts above imply

\[
\liminf\frac{\underline R(R)}{n^2}
 \ge \max\left(0,\alpha\beta-
  \frac{(1-\alpha)(1-\beta)}{(m-1)^2}\right).           \tag{14}
\]

For equal fractions alpha=beta, a subquadratic correction requires
`alpha<=1/m`. At width four, retaining a nonsingular leading channel
block on more than one quarter of each long leg already forces a
positive quadratic cost by this estimate. This is a necessary condition
inside (1), not a claim that the remaining singular families work.

## 6. Exact constructions that test the boundary

### Separated windows give a genuine restriction

Put k=floor(n/m), and select source polynomial positions
`s_i=m(i+1)-1`, for i<k, on both long legs. Use identity channel maps.
The windows are disjoint. Map a source A coordinate to a_ij exactly
when

\[
p=mi+m-1-y,\quad q=mj+m-1-y
\quad\text{for some }0\le y<m,
\]

and to zero otherwise. Literal substitution gives

\[
Q_{n,m}\ \ge\ M(k,m,k)                                \tag{15}
\]

over every field, with unit coefficients and no cancellation. Here
c_Bc_C=k^2=D and (12) permits zero repair. The outer ratio is about 1/m,
so this calibration does not supply the near-full construction criterion.

### A full-channel example attains the `D-1` flattening bound

Over Q, choose m distinct nonzero rationals lambda_a and let
`V[y,a]=lambda_a^(-y)`. For full windows at positions z_i,s_j, put

\[
\beta_j^T=\operatorname{diag}(\lambda_a^{-s_j})V^{-1},
\qquad
\gamma_i=(V^T)^{-1}\operatorname{diag}(\lambda_a^{-z_i}),
\qquad
f_{pq}=\sum_a\lambda_a^{p+q}.
\]

Then F_ij(f)=V diag(lambda_a^(z_i+s_j)) V^T, and every mapped channel
block is I_m. Map A_pq to f_pq a_00. The source image is
`a_00 tensor sum_(i,j,alpha) b_(j,alpha)c_(alpha,i)`.
Its residual to M has first-flattening kernel exactly the line of
constant arrays w_ij, hence rank D-1. The encoded source contraction
has full channel rank m. This example lies outside the earlier strict
low-channel-rank hypothesis and attains (12) when the two graphs are
connected. Sharpness here concerns the flattening bound, not an exact
tensor border-rank formula for the residual.

## 7. Evidence boundary

The proof establishes the uniform statement. The accompanying exact
controls reconstruct native source terms and compare every output
coefficient. They test full channel rank, disconnected components,
leading rank loss, and pole cancellation. Finite controls do not replace
the argument or constitute independent mathematical review.

The paired-source definition and correction criterion retain their
original repository credit. The normalization of an auxiliary-kernel
lattice follows the separate argument in PR211. The overlap graph,
leading intersection bound, and resulting dimension budget are this
continuation. The source pins and exact validation receipt are retained
with the package.
