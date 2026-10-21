# Q(n,2) cannot reach matrix multiplication with both long maps regular

**Status: written proof with exact coefficient controls; no external
mathematical review.** This is a restricted degeneration obstruction.
Arbitrary Laurent families with a singular leading B or C map remain open.

## Statement and precise scope

For every `n≥3`, there is no Laurent family

\[
(A(t)\otimes B(t)\otimes C(t))Q_{n,2}
 =M(n,2,n)+O(t)
\tag{1}
\]

in which B(t) and C(t) are regular at zero and their values at zero are
surjective maps from dimension `2(n+1)` to `2n`. The A map may have poles
of any finite order.

The proof uses two previously written results in this directory:

1. `narrow_rank_locus.md`: every full pair of long-leg quotients loses at
   most one A direction, and a lost direction is a pure parameter.
2. `narrow_ordinary_obstruction.md` and `narrow_ordinary_all_n.md`: there
   is no ordinary full restriction to M(n,2,n), for any n at least three.

We first treat the remaining possibility of a quotient with exactly one
lost A direction whose entire surviving slice space embeds in the matrix
multiplication slice space.

## 1. A deficient quotient cannot embed as a slice subspace

Let S be an ordinary full B/C quotient of Q(n,2), and suppose its
`n²−1`-dimensional slice space lies, after fixed invertible B/C changes,
inside

\[
\{X\otimes I_2:X\in\operatorname{Mat}_n(\mathbb C)\}.
\tag{2}
\]

All its slice ranks must therefore be even. The generic-divisor argument
in the ordinary proof still applies: the entire source A slice space is
being considered here, including its one zero direction. It forces

\[
\dim(K_B\cap E_g),\ \dim(K_C\cap F_f)\in\{0,2\}
\quad\hbox{for every nonzero }f,g.
\tag{3}
\]

There is exactly one projective lost A parameter. The minimum-rank lemma
identifies it as a pure parameter `f0⊗g0`. Its source slice must be killed
by both kernels, so each kernel lies in its four-dimensional divisor
space and their coordinate planes are orthogonal complements.

The kernel classification from the ordinary proof therefore says that
each kernel is uniform or tangent:

\[
U\otimes h,
\qquad
\langle u\ell^n,\ u\ell^{n-1}m+u'\ell^n\rangle.
\tag{4}
\]

### A uniform kernel cannot be part of the killed pair

If K_B is uniform, write `h=g0 ell`. In the pure-slice coordinates it is
`R=U_y⊗ell_v`. Its orthogonal complement is
`R^perp=U_y⊗ell_v^perp`. On C, this means that K_C has one fixed U'_v
factor and the full polynomial pencil `f0 P1` on its other factor.

Such a plane violates (3). Choose a linear form a so that the degree-n
polynomial `f0 a` is not a pure n-th power. It has a divisor f' of degree
`n−1` not proportional to f0. The vector `f0 a` gives a nonzero
intersection of K_C with `f' P1⊗U'`. That intersection is one-dimensional:
if it were two-dimensional, `f0 P1=f' P1`, which would force the common
degree-`n−1` factors to be proportional. This contradicts (3).

Thus neither kernel can be uniform.

### Compatibility of the two tangent planes

Each tangent kernel has one common divisor of degree `n−1`, which is a
pure power. Source polynomial symmetries therefore normalize the killed
parameter to `A00`. Use `(y0,y1)` and `(v0,v1)` for the two local linear
polynomial bases in that pure slice. A tangent B plane then has the form

\[
R=\langle u\otimes v_0,\ u\otimes v_1+u'\otimes v_0\rangle,
\]

where u and u' are independent. Write `u=(a,b)` and `u'=(c,d)`.
Its orthogonal C plane must have a nonzero rank-one member with polynomial
factor y0. For a vector `y0⊗(x,y)` to be orthogonal to R, it must satisfy

\[
ax=0,\qquad cx+ay=0.
\]

If a were nonzero, x and y would both be zero. Hence a=0, and independence
forces c nonzero. Rescaling and subtracting a multiple of the first
generator gives

\[
R=\langle E_{10},\ E_{11}+cE_{00}\rangle,
\qquad
R^\perp=\langle E_{01},\ E_{00}-cE_{11}\rangle,
\quad c\ne0.
\tag{5}
\]

The source torus

\[
A_{p,q}\mapsto\alpha^p\beta^q A_{p,q},\quad
B_{y,j}\mapsto\alpha^y\beta^{-j}B_{y,j},\quad
C_{z,v}\mapsto\alpha^{-z}\beta^v C_{z,v}
\]

preserves every source monomial. Choosing `alpha=c`, `beta=1` changes
(5) to the case c=1. Consequently the only possible pair, up to these
invertible source changes, is

\[
K_B=\langle B_{1,0},B_{0,0}+B_{1,1}\rangle,
\qquad
K_C=\langle C_{0,1},C_{0,0}-C_{1,1}\rangle.
\tag{6}
\]

### Its rank-five slice

Use the surviving original B vectors `B_(0,j),B_(1,j)` with `j≥1`, and
the C vectors `C_(z,v)` with `z≥1`, as quotient bases. Their relations are

\[
B_{1,0}=0,\quad B_{0,0}=-B_{1,1},\qquad
C_{0,1}=0,\quad C_{0,0}=C_{1,1}.
\]

For every n at least three, the slice at `A12+A20` is exactly

\[
\begin{aligned}
S(A_{1,2}+A_{2,0})={}&
B_{0,2}C_{1,0}+B_{0,3}C_{1,1}
 +(B_{1,2}-B_{1,1})C_{2,0}\\
& +(B_{1,3}+B_{0,1})C_{2,1}+B_{1,1}C_{3,1}.
\end{aligned}
\tag{7}
\]

It has five independent C vectors and five independent B coefficient
vectors. Its rank is exactly five, contradicting (2). The certificate
`narrow-rank-locus.json` gives a determinant-one five-by-five minor and
confirms that the full matrix has only five nonzero columns. Thus no
deficient quotient of this kind embeds in (2).

## 2. Why this excludes any A pole order with regular full long maps

Assume (1), and put

\[
S(t)=(\mathrm{id}_A\otimes B(t)\otimes C(t))Q_{n,2}.
\]

This is regular at zero. Let `N=n²`, and regard its A flattening as a
matrix with N columns and `(2n)²` rows. Write T(t) for the tensor on the
left side of (1). Since T(0) is A-concise, an N-by-N minor of its A
flattening is nonzero at zero. That minor has an inverse with regular
entries.

For nonzero t over the Laurent-series field, A(t) is invertible: otherwise
T(t) could not have A rank N. Thus S(t) and T(t) have the same column
space. Solve for the coefficients of each S(t) column in the T(t) basis
by using the selected N rows. The inverse minor and the S(t) entries are
regular, so these coefficients are regular as well. Passing to zero gives

\[
\operatorname{im}S(0)\subseteq\operatorname{im}T(0).
\tag{8}
\]

This is a direct matrix proof of the needed Grassmannian-limit inclusion;
no restriction on the pole order of A(t) was used.

By the rank-loss theorem, S(0) has A rank N or N−1. If its rank is N,
(8) is equality, and a fixed invertible A map gives an ordinary
restriction to matrix multiplication, already excluded. If its rank is
N−1, section 1 excludes (8). This proves the stated theorem. ∎

## 3. What remains possible

A successful Laurent family from Q(n,2) must therefore have a singular
leading map on at least one long leg after scalar powers are removed.
If both leading long maps were full rank, those scalar powers could be
absorbed into A and the theorem would apply.

This conclusion does not exclude general border restriction. Singular
output changes on B or C can change the limiting slice plane, and (8)
then need not describe the ordinary quotient at zero. It also does not
exclude every ordinary restriction to matrix multiplication with one A
entry removed: that task may first retain all N source slice directions
and then select a hyperplane of them. Section 1 applies when the full
B/C quotient itself already loses one direction.
