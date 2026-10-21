# Exact extension limit for the fixed product core

October 21, 2026. Written, AI-derived proof and exact standard-library
coefficient controls. No external independent review, formalization, or
smaller exponent is claimed.

For the exported A(7,8) to M12 product core, the contraction against
the other two core legs has rank 672 and kernel dimension 112 on
each source leg. Therefore any ordinary matrix multiplication
extension with these core row spaces held fixed has total target
leg dimension at most 256.

In particular, a fixed-core extension to M_N requires N<=16. A
fixed-core extension to M_N plus M5 requires N<=15. The proposed
M25 plus M5 target cannot be reached while retaining this M12 core.
This statement does not exclude maps whose core row spaces move.

## The three-factor contraction

Use the U,V,R bases of `parity_structure_full_residual.md`, with
d=a-1, b=a+1, m=2a, and n=2d. Their core row maps are

\[
\begin{aligned}
X_{I,J}(i,t,s)&=U_{\alpha_I}(i)R_{\alpha_J,\beta_I}(t)V_{\beta_J}(s),\\
Y_{J,K}(j,p,u)&=V_{\beta_K}(j)U_{\alpha_J}(p)R_{\alpha_K,\beta_J}(u),\\
Z_{L,I}(v,q,r)&=R_{\alpha_I,\beta_L}(v)V_{\beta_I}(q)U_{\alpha_L}(r).
\end{aligned}
\]

Every vertex label has an alpha in {0,1} and a beta in
{0,...,d-1}. The labels K and L are independent when taking the
full two-core contraction. For an unrestricted X-leg row F, its
coefficient at (Y_(J,K),Z_(L,I)) is

\[
\sum_{i,t,s}F_{i,t,s}
 A_{\alpha_I,\beta_L,\beta_K}(i)
 G_{\alpha_J,\beta_I}(t)
 B_{\alpha_K,\beta_J,\alpha_L}(s),
\tag{1}
\]

where

\[
\begin{aligned}
A_{\alpha,\beta,\kappa}(i)
 &=\sum_j R_{\alpha,\beta}(i+j)V_\kappa(j),\\
G_{\alpha,\beta}(t)&=[x^t]\bigl(U_\alpha V_\beta\bigr),\\
B_{\alpha,\beta,\eta}(s)
 &=\sum_r R_{\alpha,\beta}(r+s)U_\eta(r).
\end{aligned}
\tag{2}
\]

Formula (1) is obtained by separating the three convolution pairs
in the source coefficient formula. Its three index groups are
disjoint and exhaust the eight indices of I,J,K,L. Consequently
the entire contraction row space is exactly

\[
\operatorname{span}(A)\otimes
\operatorname{span}(G)\otimes
\operatorname{span}(B).
\tag{3}
\]

This is equality of row spaces, not just containment: every product
of one listed A row, one listed G row, and one listed B row occurs
for one choice of the independent vertex indices.

The G span has dimension 2d because the products U_alpha V_beta
have the explicit left inverse R. The A span is the full first
short dual space, of dimension a=d+1. Indeed, contracting R_(0,j)
against V_*=1+x^(d+1) gives e_j for 1<=j<d; R_(0,*) gives e_0.
Contracting R_(1,2)=e_(d+2) against V_2=x^2 gives e_d. These
functionals constitute the standard basis.

The B span is the full second short dual space, of dimension
b=d+2. Contract against U_0=1. The R_(0,j) and R_(0,*) rows give
e_0,...,e_(d-1). The rows R_(1,*)=gamma e_1+e_d and
R_(1,1)=-e_0+e_(d+1) supply the two remaining directions.

Thus for every a>=5 in this product-core family,

\[
\operatorname{rank}(\text{two-core contraction})=a(2d)b.
\tag{4}
\]

The long product span has annihilator H=span(h_0,h_1). Equation
(3) therefore gives the full kernel, in the original X coordinate
order:

\[
\ker(\text{two-core contraction})
 =\mathbb C^a\otimes H\otimes\mathbb C^b.
\tag{5}
\]

It has dimension 2ab. The Y and Z statements are the cyclic
permutations of (5), using their respective coordinate orders.
At a=7 this gives rank 7 times 12 times 8 = 672, and kernel
dimension 7 times 2 times 8 = 112.

## Consequence for a fixed-core extension

Suppose a restriction to M_N, or to M_N plus additional concise
direct-sum blocks, uses this core as the standard M_n subblock
inside M_N. Let D be the common target leg dimension. On any leg,
the D-n^2 rows outside the core annihilate the other two core
legs: the matrix multiplication indices cannot close a triangle
with two core edges and one edge outside the core, and direct-sum
cross terms are zero.

All D row vectors of each restriction map are linearly independent,
because the target is concise. In particular, the D-n^2 outside
rows give that many independent elements of (5). Hence

\[
D-n^2\le2ab,\qquad D\le n^2+2ab.
\tag{6}
\]

For A78 and n=12, the right side is 144+112=256. The M_N
consequence is N^2<=256. If a direct-sum M5 is also required,
the consequence is N^2+25<=256, so N<=15.

Changing bases within the same core row spaces does not change
the kernel or this conclusion. Moving those source row spaces
can change the kernel; (6) is not an obstruction to such a search.
No singular degeneration or unrestricted ordinary target is
excluded by this fixed-core calculation alone.

## Exact completed controls

`parity_structure_fixed_core.py` imports only the Python standard
library and the adjacent standard-library sparse-certificate loader.
It checks the following against the actual exported A78 maps:

- Every coefficient of all three core maps agrees with U,V,R.
- Exact rational row reduction gives the three factor ranks 7,12,8.
- Both h functionals annihilate all 12 core products and are independent.
- The complete contraction of all 175,616 source terms with both other core legs agrees with (1), at all output coefficients. There are 13,312 nonzero coefficients in that contraction.
- The source and the three core maps have the stated exact cyclic coordinate identifications, so the same factorization and rank apply on every leg.

The resulting rank and scope are recorded in
`parity_structure_fixed_core_certificate.json`. Reproduce without
site packages from the repository root:

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_fixed_core.py
```

The completed calculation makes a concrete search decision: the
M12 seed cannot be fixed inside the larger M25 plus M5 target.
Any continued attempt at that target must alter its core row spaces.
