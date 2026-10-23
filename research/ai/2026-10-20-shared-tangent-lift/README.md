# First and second order tests for the proposed shared Laurent family

Continuation of the October 20, 2026 sprint. AI-derived written proofs with same-session review by a
separate research agent. Not externally reviewed or formalized. These are
obstructions to two specified parameterizations, not an exponent improvement.

## Result and scope

The preceding
[singular shared-map family](../2026-10-20-singular-shared-normalization/README.md)
passes every transported shared catalecticant rank test at the limit. At its
central test the limiting rank equals the full source allowance. That equality
makes the first two orders of a putative lift informative.

Put `m=2s>=4`, `D=m-1`, `N=m(m+1)/2`, and `c(t)=(1,t,...,t^D)^T`. Write

\[
P_0=\sum_{j=0}^{s}c(j)c(j)^{\mathsf T},\qquad
P_1=\sum_{j=s+1}^{D}c(j)c(j)^{\mathsf T}.
\]

There are no integer-power Laurent maps on the two other legs that complete
either of the proposed shared maps

\[
A_\epsilon=(P_0+\epsilon P_1)^{-1},\qquad
A_t=(P_0+t^2P_1)^{-1}
\]

from `C(m,N)` to the canonical `T_m`.

The proof covers arbitrary finite pole orders on the two missing maps; it
does not merely reject the numerical degree-one ansatz. The second statement
also permits a freely varying first-order target tensor. Higher ramification,
different leading shared matrices, and noncanonical target identifications
are not excluded here.

## 1. The central matrix and a pair of kernel vectors

Use the central catalecticant `Delta=Delta_(s-1)` with auxiliary spaces
`U` of dimension `s` and `V` of dimension `s+1`. For a tensor `S`, let

\[
\Phi(S)_{(r,y),(v,z)}=S_{r+v,y,z},
\quad 0\le r<s,\quad 0\le v\le s.
\]

Thus `Phi(P S)` means first applying `P` to the shared factor of `S`.
The source rank bound from
[source_obstructions.md, Section 2](../2026-10-20-koszul/source_obstructions.md)
is `rank Phi(C(m,N))=N+s-1`. Therefore a completed degeneration with
resulting tensor `S(parameter)` would satisfy

\[
\operatorname{rank}\Phi(P(\text{parameter})S(\text{parameter}))
\le R:=N+s-1. \tag{1}
\]

The preceding family's exact formula gives
`rank M_0=R`, where `M_0=Phi(P_0 T_m)`.

Split the retained nodes into sets `A={0,...,s-2}` and `C={s-1,s}`. Define

\[
a(t)=\prod_{j\in A}(t-j),\quad c(t)=\prod_{j\in C}(t-j),
\quad g(t)=a(t)c(t)=\prod_{j=0}^{s}(t-j).
\]

Polynomial coefficient vectors are padded with zeros to their indicated
spaces. In the target block with `Y` degree `s` and `Z` degree `s-1`, set

\[
L=a(U)^T\otimes c(Y)^T,\qquad R_0=c(V)\otimes a(Z).
\]

Both are legitimate: their respective degrees are `s-1,2,2,s-1`, within
the four degree bounds `s-1,s,s,s-1`. Evaluating a row or column factor at
any retained node gives `g(j)=0`. Hence

\[
L M_0=0,\qquad M_0 R_0=0. \tag{2}
\]

For every tensor perturbation `S`, including one with arbitrary coefficients
outside this block, contraction through the two auxiliary factors gives

\[
L\Phi(P_0 S)R_0=0. \tag{3}
\]

Indeed, each retained-node summand has the auxiliary scalar factor
`a(j)c(j)=g(j)=0`; no property of `S` is needed. By contrast,

\[
L\Phi(P_1 T_m)R_0
=\sum_{j=s+1}^{D}g(j)^2>0. \tag{4}
\]

For `m=4`, the polynomials are `a(t)=t`, `c(t)=t^2-3t+2`, and the value
in (4) is `g(3)^2=36`.

## 2. The first-order obstruction

If a matrix series `M_0+epsilon M_1+...` has rank at most `rank M_0`, then
every left kernel vector `l` and right kernel vector `r` satisfy
`l M_1 r=0`. This follows by choosing an invertible rank-sized minor and
expanding the vanishing complementary Schur block to first order.

Any integer-power Laurent completion having finite limit `T_m` produces
a tensor series `T_m+epsilon S_1+...`. With `P=P_0+epsilon P_1`, its first
matrix coefficient is

\[
M_1=\Phi(P_0 S_1+P_1T_m).
\]

Equations (3)-(4) contradict the necessary first-order kernel condition.
This proves the first exclusion, without restricting the Laurent orders
of the individual tensor maps.

## 3. The complete second-order condition

For `P=P_0+t^2P_1`, write the unknown result as
`T_m+t S_1+t^2 S_2+...`. Then

\[
M_1=\Phi(P_0S_1),\qquad
M_2=\Phi(P_0S_2+P_1T_m).
\]

Let `G` be any inner inverse of `M_0`, so `M_0 G M_0=M_0`. Under the
first-order tangent condition for the **whole** left and right kernels,
the second-order rank condition is

\[
l M_2 r=l M_1 G M_1 r
\quad\text{for every }l\in\ker M_0^T,\ r\in\ker M_0. \tag{5}
\]

This is the second-order term of the same Schur complement. It is independent
of the inner inverse: tangency puts `M_1 r` in the image of `M_0` and makes
`l M_1` annihilate its kernel.

Thus the proposed ramified construction must solve a linear tangent system
for `S_1`, followed by the quadratic system (5), with the linear freedom
`Phi(P_0 S_2)`. The following argument shows that its one selected equation
already has no solution.

## 4. Why the selected quadratic correction vanishes

Write `u_j=(1,j,...,j^(s-1))^T`. The `s+1` vectors
`v_j=(1,j,...,j^s)^T` form a basis of `V`. In that auxiliary basis, the
matrix `M_0` has node column blocks

\[
M_0=[\,u_j\otimes T_m(c(j))\,]_{j=0}^{s}.
\]

Let `E_j` be the image in `Y` of the coherent slice `T_m(c(j))`. It is
the direct sum, over the degrees `0,...,D`, of the one-dimensional spaces
spanned by `(1,j,...,j^ell)` in that degree sector. Therefore

\[
E_j\cap E_k=K\quad(j\ne k),
\]

where `K` is the common degree-zero line. In particular `K` is contained
in every `E_j`. Any `s` of the vectors `u_j` are independent.

Put `H_A=span{u_j:j in A}`, of dimension `s-1`. The precise intersection
identity needed below is

\[
\operatorname{im}M_0\cap(H_A\otimes Y)
=\sum_{j\in A}u_j\otimes E_j. \tag{6}
\]

To prove it, reduce a vector `sum u_j tensor e_j`, with `e_j in E_j`,
modulo `H_A`. Only the two nodes in `C` remain. Their images in the
one-dimensional quotient `U/H_A` are nonzero and proportional. Their
`E_j` components must therefore agree up to a scalar, and lie in their
intersection `K`. The resulting contribution in `H_A tensor K` can be
represented using the `A` blocks, since the `u_j` for `j in A` span
`H_A` and `K` lies in every one of their `E_j`. This proves (6).

For an arbitrary `M_1=Phi(P_0 S_1)`, contraction by `R_0` kills the two
`C` column blocks because `c(j)=0` there. Thus `M_1R_0` lies in
`H_A tensor Y`. Full tangency also puts it in `im M_0`. By (6), it has an
`M_0` preimage supported only in the `A` column blocks. But `L M_1`
vanishes on those blocks because `a(j)=0` for `j in A`. Independence of
the inner inverse now gives

\[
L M_1 G M_1R_0=0 \tag{7}
\]

for **every** first-order tangent motion `S_1`. The left side of (5), with
`l=L,r=R_0`, is the strictly positive value (4), by (3). This proves the
second exclusion.

## Verification and next construction choices

`verify_tangent_obstruction.py` checks exact rational block ranks, the kernel
identities, the perturbation-annihilation coefficients, and the positive
forcing for `m=4,6,8,10`. The universal second-order assertion rests on the
image-intersection proof; finite arithmetic is not a substitute for it.

The failed numerical degree-one Laurent completion contained all negative
coefficients and reached only nonzero floating residuals with large map
norms. The proof above explains why that literal family could not yield
an exact certificate. No inference is based on the size of those residuals.

The active construction search now allows source length `B=N+O(m)`.
That overhead still has asymptotic cost one in the existing all-size
criterion, while even `B=N+1` removes the sharp-rank hypothesis used here.
The first concrete tests use `C(4,11)` and `C(4,12)`. Different leading
shared matrices and higher ramification are also outside the two claims
proved here. None of these alternatives has a verified full-target map.
