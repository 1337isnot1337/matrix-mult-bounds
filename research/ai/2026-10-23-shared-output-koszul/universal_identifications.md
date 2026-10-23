# The obstruction survives independent target first identifications

Date: 2026-10-23. Owner-directed Codex work. Written and unreviewed.
This is a separate extension of the frozen canonical certificate in `proof.md`.

## 1. Statement and notation

Keep the canonical source `S=10 Full(5,4)`. In the target

\[
10\,\mathrm{Full}(5,3)+\mathrm{Full}(5,2)+2O,
\qquad O=P_{5,4,2},
\tag{1}
\]

allow each of the thirteen blocks its own arbitrary invertible identification
of its five-dimensional first space with `A`. Keep the nonshared spaces
disjoint. Independent basis changes in those spaces are also allowed.

**Theorem.** Every target `T` in (1) has

\[
\operatorname{rank}K_B(T)\ge2616>2595=
\operatorname{rank}K_B(S).
\tag{2}
\]

Consequently, no complex degeneration from the canonical source to any such
target exists, including degenerations with singular or polar first maps.
The lower bound is sharp: the canonical target attains 2616.

The source's ten first identifications remain one common coefficient basis.
This theorem does not assert that arbitrary independent source identifications
retain rank 2595. The proof concerns this specific target profile; it does not
exclude all mixed-orientation packings.

For a Full block of dimensions `(a,b,a+b-1)`, let

\[
E_b\subset A\otimes B_b
\]

denote its coefficient space, the image of its third dual leg. In canonical
bases it is the space of `a`-by-`b` Hankel matrices

\[
H(u)_{ij}=u_{i+j},\qquad 0\le i<a,\ 0\le j<b.
\tag{3}
\]

It has dimension `a+b-1`. A first identification replaces it by `g E_b` for
an invertible `g` on `A`. This use of `E_b` for the coefficient space is local
to this note; `proof.md` used the same letter for the whole block.

Let `L` denote the two-dimensional coefficient space of `O` in
`A tensor D`, where `dim D=4`. Its elements are

\[
M(s,t)=\sum_{j=0}^{3}(s a_j+t a_{j+1})\otimes d_j.
\tag{4}
\]

Every nonzero `M(s,t)` has matrix rank four: it is multiplication of a cubic
polynomial by the nonzero linear polynomial `s+t z`. Independent first
identifications preserve this property.

For any pair of target blocks with coefficient spaces `R_i,R_j`, the
cross-map rank from `proof.md`, Section 3, is its domain dimension minus

\[
\dim I(R_i,R_j),\qquad
I(R_i,R_j)=(R_i\otimes B_j)\cap(B_i\otimes R_j),
\tag{5}
\]

where both spaces are reordered into `A tensor B_i tensor B_j`.
We prove that all five target pair-kernel dimensions are at most their
canonical values.

## 2. Two elementary facts about Hankel coefficient spaces

**Contraction fact.** For any nonzero `q` in `B_b^*`, contraction

\[
q:E_b\longrightarrow A
\tag{6}
\]

is surjective, and its kernel has dimension `b-1`.

Indeed, the transpose of (6) is multiplication of a polynomial of degree
less than `a` by the nonzero polynomial whose coefficients are `q`. Polynomial
multiplication has no zero divisors, so this transpose is injective. The
domain in (6) has dimension `a+b-1`, proving the claim. It remains true after
any invertible first identification.

Choose `q(z)` of degree `b-1` with distinct finite roots `t_1,...,t_(b-1)`.
For

\[
x_a(t)=(1,t,\ldots,t^{a-1}),\qquad
y_b(t)=(1,t,\ldots,t^{b-1}),
\]

the kernel in (6) has the basis

\[
x_a(t_r)\otimes y_b(t_r),\qquad 1\le r\le b-1.
\tag{7}
\]

These vectors are killed by `q`; their second factors are independent
Vandermonde vectors, and their number is the kernel dimension. After first
identification `g`, replace `x_a(t_r)` by `g x_a(t_r)`.

**Fixed-first-vector fact.** Suppose `a>=2`. For any nonzero `x` in `A`,

\[
\dim\{v\in B_d:x\otimes v\in E_d\}\le1.
\tag{8}
\]

For a Hankel rank-one matrix the adjacent relations are

\[
x_{i+1}v_j=x_i v_{j+1}.
\tag{9}
\]

If `x_0` is nonzero, the relation for `i=0` determines every `v_j` from
`v_0`. If the first nonzero coordinate is `x_h`, `h>0`, the relation for
`i=h-1` forces `v_0,...,v_(d-2)` to vanish; only `v_(d-1)` can remain.
Thus the solution space has dimension at most one. When `d=1`, this is
automatic. For `g E_d`, apply this argument to `g^{-1}x`.

## 3. Full/Full pair kernels cannot exceed their canonical values

For `a>=2` and arbitrary independent first identifications, we have

\[
\dim I(g E_b,h E_d)\le a+b+d-2.
\tag{10}
\]

Choose the contraction `q` from (7) on `B_b`. It maps the intersection in
(10) into `h E_d`, so its image has dimension at most `a+d-1`.
An element of its kernel has the unique form

\[
\sum_{r=1}^{b-1}(g x_a(t_r))\otimes y_b(t_r)\otimes v_r.
\tag{11}
\]

Membership in `B_b tensor h E_d`, together with independence of the vectors
`y_b(t_r)`, forces each `(g x_a(t_r)) tensor v_r` to lie in `h E_d`.
The fixed-first-vector fact gives at most one degree of freedom for each
`v_r`. Thus the kernel dimension is at most `b-1`; adding the image bound
proves (10). For `b=1`, the contraction kernel is zero and the same bound
follows immediately.

In our target `a=5`, this gives

\[
\dim I(E_3,E_3)\le9,\qquad
\dim I(E_3,E_2)\le8,
\tag{12}
\]

with any independent first identifications understood.

## 4. Full/shared-output and shared-output/shared-output pairs

For a three-tensor `V` in `A tensor B tensor D`, its support dimension
on `D` means the rank of the map `D^* -> A tensor B`. If `V` belongs to
`K tensor D`, this rank is at most `dim K`. Contracting any other factor
cannot increase it. We use these elementary rank facts below.

### 4.1 The `E3/O` pair kernel is zero

Suppose `V` lies in `I(g E_3,h L)`. Since `dim L=2`, write its membership
in `B_3 tensor h L` as two coefficient matrices with second-leg vectors
spanning a subspace `U` of `B_3` of dimension at most two. Choose nonzero
`q` in `B_3^*` annihilating `U`. Then

\[
V\in\ker(q:g E_3\to A)\otimes D.
\]

The contraction fact gives this kernel dimension two, so `V` has `D`-support
dimension at most two. If `V` were nonzero, some contraction on `B_3`
would give a nonzero member of `h L`. Every such member has matrix rank
four by (4). This would force the `D`-support dimension of `V` to be at
least four, a contradiction. Hence

\[
I(g E_3,h L)=0.
\tag{13}
\]

### 4.2 The `O/O` pair kernel is zero

Suppose `V` lies in `I(g L,h L)`, with separate four-dimensional nonshared
spaces `D_1,D_2`. Its membership in `D_1 tensor h L` puts its `D_1` support
in a space of dimension at most two. If `V` is nonzero, its membership in
`g L tensor D_2` supplies a contraction on `D_2` that is a nonzero member
of `g L`, of matrix rank four. This forces its `D_1` support dimension
to be at least four. Therefore

\[
I(g L,h L)=0.
\tag{14}
\]

### 4.3 The `E2/O` pair kernel has dimension at most one

An element `V` of `I(g E_2,h L)` gives a linear map

\[
\varphi_V:B_2^*\longrightarrow h L
\tag{15}
\]

between two-dimensional spaces, by contraction. If `V` is nonzero but
`varphi_V` is singular, choose nonzero `q` in its kernel. The contraction
fact now puts `V` in `K tensor D`, where `dim K=1`. Its `D`-support
dimension is at most one. A nonzero contraction on `B_2` nevertheless
belongs to `h L` and has matrix rank four, a contradiction.

Thus every nonzero member of the linear subspace of maps (15) is invertible.
Over the complex numbers such a subspace of two-by-two matrices has dimension
at most one. Indeed, if `P,Q` were independent members, both would be
invertible, and `det(P+tQ)` would be a nonconstant degree-two polynomial.
It has a complex root, producing a nonzero singular member. Consequently

\[
\dim I(g E_2,h L)\le1.
\tag{16}
\]

## 5. The universal rank bound

The intrinsic block ranks are invariant under their independent first
identifications, so their sum remains 141. Equations (12)--(16) give the
following pair-map lower bounds using (5):

| Pair | Domain dimension | Kernel upper bound | Rank lower bound | Count |
| --- | ---: | ---: | ---: | ---: |
| `E3/E3` | 42 | 9 | 33 | 45 |
| `E3/E2` | 32 | 8 | 24 | 10 |
| `E3/O` | 34 | 0 | 34 | 20 |
| `E2/O` | 28 | 1 | 27 | 2 |
| `O/O` | 16 | 0 | 16 | 1 |

The block decomposition of the full Koszul map remains valid: only the
nonshared direct-sum structure is needed. Therefore every independently
identified target has rank at least

\[
141+45(33)+10(24)+20(34)+2(27)+16=2616.
\]

The canonical source has rank 2595 by the exact certificate. Semicontinuity
from `proof.md`, Section 2, proves (2) and the claimed degeneration exclusion.
The same canonical certificate shows each pair bound, and hence their total,
is attained simultaneously.

## 6. Evidence and provenance

The proof above is an all-parameter algebraic argument; finite sampling of
first identifications is neither required nor asserted as its justification.
The frozen canonical certificate verifies sharpness and the source upper bound.
It uses ten determinant-`+/-1` minors and 56 independent kernel vectors, with
five focused standard-library tests passing. No new external structural theorem
is imported: the needed polynomial, Vandermonde, tensor-support, and complex
quadratic-root facts are stated and proved or used in their elementary form.

The research-frontier agent supplied the squarefree-contraction proof of
the Full/Full bound and the `E2/O` determinant argument. The audit agent and
research-frontier agent independently derived the `E3/O` and `O/O` bounds
and checked the combined deduction. This is same-session collaboration,
not independent mathematical review. No historical priority, formalization,
general mixed-orientation barrier, or exponent improvement is claimed.
