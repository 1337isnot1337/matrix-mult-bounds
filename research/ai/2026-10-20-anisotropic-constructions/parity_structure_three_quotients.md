# The scalar correction for three different A22 quotients

October 21, 2026. Written, AI-derived proof and exact finite controls.
This is a restriction on the specified quotient construction. It is
not an obstruction to arbitrary A22 degenerations or an improved
matrix multiplication exponent.

Allowing three different regular quotient kernels does not make the
scalar correction in the A22 triangular construction vanish. The
three scalar coefficient matrices have determinant product exactly
one. In the normalization where the quotient term is exactly M3,
the correction has Frobenius norm at least the norm of M3 itself.

The argument works over the complex numbers. Every finite check
below uses exact rational arithmetic.

## 1. The regular quotient chart

The physical matrix space for A22 is

\[
W(F)=
\begin{pmatrix}
F_{000}&F_{001}&F_{010}&F_{011}\\
F_{010}&F_{011}&F_{020}&F_{021}\\
F_{100}&F_{101}&F_{110}&F_{111}\\
F_{110}&F_{111}&F_{120}&F_{121}
\end{pmatrix}.
\tag{1}
\]

Thus it is the 12-dimensional subspace of 4-by-4 matrices defined
by

\[
W_{1,s}=W_{0,2+s},\qquad W_{3,s}=W_{2,2+s},\qquad s=0,1.
\tag{2}
\]

As explained in `parity_balancing_triangular.md`, the trace of three
such matrices is the original A22 tensor, after the stated cyclic
coordinate identifications.

Let an output kernel vector be alpha=(1,x,y,z), and set

\[
\Delta_\alpha=z-xy,\qquad
\pi_\alpha=
\begin{pmatrix}-x&1&0&0\\-y&0&1&0\\-z&0&0&1\end{pmatrix}.
\tag{3}
\]

The map W to pi_alpha W is invertible precisely when
Delta_alpha is nonzero. Indeed, an element of its kernel has the
form alpha ell^T. Substituting into (2) gives two copies of the
linear system with coefficient matrix

\[
\begin{pmatrix}x&-1\\z&-y\end{pmatrix},
\]

whose determinant is Delta_alpha. Domain and codomain both have
dimension twelve. For a general nonzero kernel vector alpha, the
regularity condition is alpha_0 alpha_3-alpha_1 alpha_2 != 0.

Use an input kernel beta=(1,u,v,w), with Delta_beta=w-uv nonzero.
For a 3-by-3 matrix A, there is consequently a unique J_(alpha,beta)(A)
in W satisfying

\[
\pi_\alpha J_{\alpha,\beta}(A)=A\pi_\beta.
\tag{4}
\]

It maps beta to a scalar multiple of alpha:

\[
J_{\alpha,\beta}(A)\beta
=\alpha\lambda_{\alpha,\beta}(A).
\]

Write the scalar linear functional as
lambda_(alpha,beta)(A)=sum_(i,j) C_(alpha,beta)[i,j] A[i,j].

## 2. The exact coefficient matrix

The matrix is

\[
C_{\alpha,\beta}=\frac1{\Delta_\alpha}
\begin{pmatrix}
z\Delta_\beta&-v(y+zv)&-w(y+zv)\\
0&1+xv&u+xw\\
-x\Delta_\beta&v(1+xv)&w(1+xv)
\end{pmatrix}.
\tag{5}
\]

Here is a direct derivation. Let S embed the quotient coordinates
into physical coordinates 1,2,3, and put W_0=S A pi_beta. Every
solution of (4) has the form W_0+alpha ell^T. For s=0,1 define

\[
t_{1,s}=(W_0)_{1,s}-(W_0)_{0,2+s},\qquad
t_{2,s}=(W_0)_{3,s}-(W_0)_{2,2+s}.
\]

Solving (2) gives

\[
\ell_s=\frac{y t_{1,s}-t_{2,s}}{\Delta_\alpha},\qquad
\ell_{2+s}=\frac{z t_{1,s}-x t_{2,s}}{\Delta_\alpha}.
\tag{6}
\]

Since W_0 beta=0, the required scalar is ell^T beta. Substituting
the columns of pi_beta into (6) yields every entry of (5).

The determinant factors without any numerical or symbolic solver.
Put L=y+zv, M=1+xv, N=u+xw. Expansion of the numerator matrix in
(5) gives

\[
\det(\Delta_\alpha C_{\alpha,\beta})
=\Delta_\beta(zM-xL)(wM-vN)
=\Delta_\alpha\Delta_\beta^2.
\]

Therefore

\[
\boxed{\det C_{\alpha,\beta}
=\left(\frac{\Delta_\beta}{\Delta_\alpha}\right)^2.}
\tag{7}
\]

If the scalar functional is written as tr(H A), then H=C^T and
has the same determinant.

## 3. Cyclic quotient maps and all choices of bases

Choose three regular kernels alpha_0,alpha_1,alpha_2. Lift the
three target matrices using output kernel alpha_i and input kernel
alpha_(i+1), with subscripts taken modulo three. Each lift maps the
input kernel line to the output kernel line and induces its target
matrix on the quotient. Thus the trace decomposition is exactly

\[
\operatorname{tr}(J_0(A)J_1(B)J_2(C))
=\operatorname{tr}(ABC)+\lambda_0(A)\lambda_1(B)\lambda_2(C).
\tag{8}
\]

By (7), all kernel discriminants cancel cyclically:

\[
\boxed{\det C_0\det C_1\det C_2=1.}
\tag{9}
\]

This does not depend on the normalized quotient bases in (3).
Replace pi_i by G_i pi_i, with G_i invertible. The corresponding
lift is the old one applied to G_i^(-1) A G_(i+1), so its scalar
coefficient matrix becomes

\[
C_i'=G_i^{-T} C_i G_{i+1}^{T}.
\]

Its determinant acquires det(G_(i+1))/det(G_i), whose product is
one. Rescaling a kernel vector multiplies adjacent scalar actions
by inverse factors, which also cancel cyclically. Finally, the
chart with first kernel coordinate nonzero is dense in the regular
quotient locus. The identity extends to all regular kernels by
these kernel rescalings and continuity of the unique linear lifts.
Equivalently, one can clear denominators to obtain the same
polynomial identity on every regular chart.

## 4. A uniform norm consequence within this construction

The correction tensor in (8) is the rank-one tensor of the three
scalar coefficient vectors. Its Frobenius norm is

\[
\|\lambda_0\otimes\lambda_1\otimes\lambda_2\|_F
=\prod_{i=0}^2\|C_i\|_F.
\]

For any complex 3-by-3 matrix C, the arithmetic-geometric mean
inequality on its three squared singular values gives

\[
\|C\|_F^2\ge3|\det C|^{2/3}.
\]

Combining this with (9) yields

\[
\|\lambda_0\otimes\lambda_1\otimes\lambda_2\|_F
\ge3\sqrt3=\|M_3\|_F.
\tag{10}
\]

The last equality holds because the standard M3 tensor has exactly
27 unit coefficients. Equality is attained when all three kernels
are (1,0,0,1): formula (5) gives C_i=I_3.

Consequently, as long as the quotient equations retain the exact
M3 term in (8), the relative residual from M3 is always at least
one. Allowing unequal kernels, approaching a singular quotient,
or changing cyclic quotient bases does not yield a sequence in
this normalized family whose correction tends to zero. The
inequality holds at every regular member of such a sequence.

This conclusion concerns the exact quotient-lift family. It does
not address maps which do not satisfy (4), constructions using a
different residual source, or arbitrary degenerations of A22.

## 5. Exact controls and provenance

`parity_structure_three_quotients.py` reconstructs the lifts from
(6) using the Python standard library. For each of three cyclic
kernel triples, it checks all nine target matrix units on each
leg against (2), (4), the kernel action, and (5). It then checks
every one of the 729 trilinear coefficients in (8). The total is
2,187 complete trace-tensor coefficients. All three determinant
products equal one exactly; the common canonical kernel attains
the norm lower bound exactly.

The rational matrices, determinant values, norm values, and precise
scope are saved in `parity_structure_three_quotients_certificate.json`.
Reproduce without site packages:

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_three_quotients.py
```

Within-session provenance: the parity-balancing worker proposed
the cyclic determinant identity and obtained numerical controls.
The anisotropic-construction worker supplied the closed matrix
formula (5). The parity-structure worker rederived it by (6),
factored its determinant explicitly, supplied the norm consequence,
and performed the exact matrix-unit and tensor replay. This is
collaboration within the generating session, with no external
independent review or formalization.
