# Rectangular shared maps and the convolution row condition

Date: October 20, 2026.

Status: exact reformulation and a restricted search exclusion. There is no
new degeneration to the full fat-point tensor and no improvement of the
matrix multiplication exponent. The proof review described below was by
another AI agent in the same research session, not an external review.

## 1. An exact condition with two independent nonshared maps

Write `C(a,B)` for the convolution tensor with slices
`K_i[j,k] = 1` when `k=i+j`, for `0 <= i < a`, `0 <= j < B`, and
`0 <= k < B+a-1`. Work over a field, including a Laurent series field.
Suppose `H_0,...,H_(a-1)` are `B by n` matrices.

The following are equivalent.

1. There are an invertible `B by B` matrix `Y` and a `(B+a-1) by n`
   matrix `Z` such that `H_i = Y K_i Z` for every `i`.
2. There is a basis `w_0,...,w_(B-1)` of the row space of dimension `B`
   such that

   `w_j H_(i+1) = w_(j+1) H_i`

   for every `j < B-1` and `i < a-1`.
3. There are a matrix `J`, a column `v`, and rows `r_i` such that

   `H_(i+1) = J H_i + v r_i`,

   and the pair `(J,v)` is controllable: the columns
   `v,Jv,...,J^(B-1)v` span the entire state space.

For `1 => 2`, use the rows of `Y^-1`. For `2 => 1`, put these rows
in a matrix `S`. The entries of `S H_i` with the same `i+j` are equal,
by the adjacent identities. They therefore define the rows of `Z`
uniquely. Set `Y=S^-1`.

For `2 => 3`, conjugate the matrix with ones on its superdiagonal and
zeros elsewhere by `S`, and conjugate its last coordinate vector by
the same change of basis. The missing last row in each adjacent
identity supplies `r_i`.

For `3 => 2`, choose a row `w_0` with
`w_0 J^k v=0` for `k<B-1` and `w_0 J^(B-1)v=1`.
Controllability guarantees its existence. Set `w_j=w_0 J^j`.
The resulting rows are independent, as is seen by pairing them with
the reversed controllability basis. The residual term `v r_i`
vanishes after applying `w_j` for `j<B-1`, giving condition 2.

This is an exact criterion; a small numerical residual is not a
certificate. The controllability requirement cannot be discarded.
It is also a model with independent input and output maps, with no
assumption that they preserve a multiplication algebra or a pairing.

## 2. One extra shared coordinate leaves one free matrix

Let `A` be a surjective `m by (m+1)` shared map, let `R` be a right
inverse, and let `h` span its kernel. For a desired regular tensor
family `T_epsilon -> T_m`, every lifted source-slice sequence has the
form

`H_i = sum_r R[i,r] T_epsilon,r + h_i Q_epsilon`,

where `Q_epsilon` is an arbitrary matrix over the Laurent series
field. The row condition above is therefore a concrete search for
this matrix, a row basis, and the target error terms. A pole in the
kernel direction is allowed because `A` kills it.

If `A` simply omits the source monomial `t^s`, the lift reads

`H_0=T_0,...,H_(s-1)=T_(s-1), H_s=Q,
 H_(s+1)=T_s,...,H_m=T_(m-1)`.

This statement concerns the matrix lifts before the row condition
is imposed. It does not itself construct a restriction.

For a target input dimension smaller than `B`, one can use an enlarged
regular tensor family with `B` input rows, whose extra rows tend to
zero. This does not assume that an arbitrary constant completion has
zero extra rows. Given a Laurent degeneration, additional independent
input rows can be scaled by a sufficiently high positive power to
make their images tend to zero; conversely, the extra rows can be
discarded.

## 3. Exact parity factorization and the remaining right equations

Let `m=2s>=4`, `D=m-1`, and `N=m(m+1)/2`. Split the shared index as
`i=2j+alpha`, with `alpha in {0,1}` and `0 <= j < s`.
Reshape the target into rows `(alpha,Y)` and columns `(j,Z)`.
Its exact rank is

`R = N+s-1`.

Here are explicit factors. Label a target input row by `(p,a)`,
where `p` is its total degree and `0 <= a <= p`. For `p<D`, take
middle labels `(p,r)` with `-1 <= r <= p`. For `p=D`, take only
`r=0,2,...,D-1`. Set

`L_alpha[(p,a),(p,r)] = 1` if `r=a-alpha`, and zero otherwise.

For an output monomial of degree `v` and first exponent `c`, set

`R_j[(p,r),(v,c)] = 1` if `v=D-p` and `r=2j-c`, and zero otherwise.

All unlisted entries are zero. Direct multiplication gives
`T_(2j+alpha)=L_alpha R_j`.

The stacked left factor has independent columns. In a block `p<D`
they are

`e_(1,0)`, `e_(0,a)+e_(1,a+1)` for `0 <= a < p`, and `e_(0,p)`.

The last block has the `s` disjoint columns
`e_(0,2j)+e_(1,2j+1)`. Every middle label is also attained by a
column of the concatenated right factors. For `p<D`, use `c=0`
or `c=1` according to the parity of `r`, and use `c=1,j=0` for
`r=-1`. The last block uses `c=0`. Thus both factors have the
required full middle rank, proving the reshape rank formula.

The left pencil is explicit: each block `p<D` is the pair
`[0 I_(p+1)]`, `[I_(p+1) 0]`. The last block is the direct sum of
`s` pairs of maps from a one-dimensional middle space to a
two-dimensional input space. This description fixes the maps
without depending on a convention for Kronecker block names.

### Polynomial-pencil source

Choose an `s`-dimensional subspace `G` of the binary forms of degree
`D`, with basis `g_j`. Use the shared source forms
`u_(2j)=g_j` and `u_(2j+1)=t g_j`, written in one affine chart.
They lie in the shared space of `C(m+1,B)`. Suppose their span has
dimension `m` and the forms `g_j` have no common projective root.
The same reshape of this source factors through the degree-`B`
polynomials, of dimension `B+1`, and has rank `B+1`.

This suggests the size

`B=N+s-2`,

where the two reshape ranks agree. This size is `N+O(m)`; the
matching rank is a necessary compatibility, not a construction.

For `m=4`, a generic hyperplane of quartics has this form for a
cubic pencil. More generally, for a hyperplane `U=ker(lambda)` in
`S^(2s)`, put

`H_lambda={g in S^(2s-1): lambda(g)=lambda(tg)=0}`.

Away from dependent equations this has dimension `2s-2`. Choose
an `s`-plane `G` in it for which `G+tG` has dimension `2s`.
Such choices form a nonempty open family: the monomial example
`G=span(1,t^2,...,t^(2s-4),t^(2s-1))` has
`G+tG` equal to the hyperplane missing `t^(2s-2)`. The open-family
statement follows by viewing these choices as an open subset of
the Grassmann bundle over the hyperplanes with independent
equations. It does not assert that every hyperplane is suitable.

### Right-factor compatibility is still required

Let `K_0=[I_B 0]` and `K_1=[0 I_B]`. After choosing a regular
deformation of the target factorization, the left identification
to be constructed is

`L_alpha(epsilon)=Y(epsilon) K_alpha Q(epsilon)`,

with `Q` invertible over the Laurent series field. Put
`F_j=Q R_j(epsilon)`. The remaining condition is the existence
of output moment rows `z_0,...,z_(B+D)` such that

`F_j[h,:]=sum_(d=0)^D g_(j,d) z_(h+d)`, for `0 <= h <= B`.

This condition is necessary and sufficient for an output map
once `Q`, `g_j`, and the factorized tensor family are fixed.
Equivalently, every bounded polynomial relation
`sum_j p_j g_j=0`, with `deg(p_j)<=B`, must satisfy

`sum_(j,h) p_(j,h) F_j[h,:]=0`.

Necessity follows by substituting the moments. For sufficiency,
these equations make the assignments on the products `p_j g_j`
well-defined as a linear functional. Extend it to the whole output
polynomial space. This is done independently in every output
coordinate.

For `m=4,B=10`, coprime cubics `g_0,g_1` have precisely the
bounded syzygies `(p_0,p_1)=(q g_1,-q g_0)`, with `deg(q)<=7`.
The missing equations therefore reduce to eight vector equations:

`sum_(d=0)^3 (g_(1,d) F_0[h+d,:] - g_(0,d) F_1[h+d,:])=0`,

for `h=0,...,7`. At target output dimension ten this is eighty
scalar equations. The fourteen moment rows are then unique,
because `g_0 S^10+g_1 S^10=S^13`.

The monomial `G` example above supplies especially simple
all-size syzygies: adjacent exponent gaps are two, except for
one final gap of three. More general mixed pencils and mixed
left gluing are allowed. No successful simultaneous solution
of the left identification and right equations is supplied here.

## 4. Why the symmetric degree split fails for C(5,10)

Work over the complex numbers. Let `D=3`, and write the target as

`T_4 = sum_(a+b+c+d=3) X_(a+c) Y_(a,b) Z_(c,d)`.

The spaces of degree at most one have dimension three. The remaining
degrees two and three have dimension seven. Consider a constant
shared map whose image is a four-dimensional subspace
`U=span(u_0,u_1,u_2,u_3)` of the binary quartics `S^4`.
Consider only the following proposed Laurent maps:

- `Y = epsilon^-1 Y_0 + Y_1`, where `Y_0` has target rows only in
  degrees at most one, and `Y_1` only in degrees at least two;
- `Z = Z_0 + epsilon Z_1`, with the same support split.

**Claim.** These maps cannot degenerate `C(5,10)` to `T_4` for any
such constant shared map.

### Base-point-free shared subspaces

First assume that the four quartics have no common projective root.
The target has full input rank ten. Therefore the ten constant rows
formed by the three nonzero rows of `Y_0` and the seven nonzero rows
of `Y_1` form a basis of `S^9`. Row scaling is the only dependence of
`Y` on the parameter.

Let `z_x,z_y` denote the two functionals in `(S^13)^*` obtained from
the degree-one target rows `Z_(1,0),Z_(0,1)` of `Z_0`.
Cancellation of the negative coefficient and matching the degree
two-by-degree one target block imply, on all of `S^9`,

`u_0 z_x=0`, `u_3 z_y=0`, and
`u_i z_y=u_(i+1) z_x` for `i=0,1,2`.

Here `u z` is the functional `f -> z(uf)`.

One may make a simultaneous linear change in the two target
variables. It preserves the degree split and changes the shared
basis by its cubic representation. After this change, the endpoint
quartics `u_0,u_3` can be assumed coprime. To see this, choose one
coherent target direction. Its source quartic has finitely many
roots. At each root, base-point-freeness says that the binary cubic
of shared values is nonzero, so it excludes only finitely many
choices for the other coherent direction. Choose the other direction
outside that finite set and distinct from the first.

Since `z_x` annihilates `u_0 S^9`, every `u_j z_x` annihilates
`u_0 S^5`. Likewise every `u_j z_y` annihilates `u_3 S^5`.
For coprime quartics,

`u_0 S^5 + u_3 S^5 = S^9`.

Indeed, each summand has dimension six and their intersection is
`u_0 u_3 S^1`, of dimension two. Consequently the two annihilators
in `(S^9)^*` have zero intersection. Every equality
`u_i z_y=u_(i+1) z_x` must have both sides zero.

In particular, `z_x` annihilates both `u_0 S^9` and `u_3 S^9`.
These sum to `S^13`: their dimensions are ten each and their
intersection `u_0u_3 S^5` has dimension six. Hence `z_x=0`.
The same argument gives `z_y=0`, contradicting the required target
coefficients.

### Shared subspaces with a base point

A four-dimensional subspace of `S^4` with a common factor must have
a common linear factor, and is exactly that factor times `S^3`.
Factoring it out reduces the maps to a fixed-shared `C(4,10)`
degeneration. The established fixed-shared threshold is eleven,
so this case is excluded as well. See the existing
[`alternating-degree-packing` note](../2026-10-20-alternating-degree-packing/README.md)
for the threshold and its exact construction at eleven.

### Scope

This excludes only the specified symmetric support split with a
constant shared map. It does not exclude mixed leading rows,
asymmetric support splits, additional Laurent coefficients,
varying rectangular shared maps, or `C(5,10) -> T_4` in general.
The construction search continues in those larger families.

The construction agent checked both the target-index orientation
and the coherent-endpoint argument in the same session. The proof
was used to stop the corresponding restricted numerical search.

## 5. Exact controls

`verify_module.py` checks the row reconstruction, including the
known `C(2,3) -> T_2` Laurent control, and checks the polynomial
dimension argument for a concrete base-point-free quartic example.
It also replays every coefficient of the explicit parity factors
for `m=4,6,8,10`, and verifies the cubic syzygy reconstruction.
It uses exact rational arithmetic. These controls accompany the
proofs; they do not constitute a new target degeneration.
