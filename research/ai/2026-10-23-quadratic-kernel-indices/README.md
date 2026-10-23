# Quadratic biform ranks from two polynomial-kernel indices

For every field and every nonzero `f=u(x)+z*v(x)+z^2*w(x)` with
coefficient degrees below `a`, the [written proof](proof.md) gives

    rank R_(a,b)(f) = ab + min(b,mu1) + min(b,mu2),

for `a>=2`, `b>=3`. After dividing the coefficient gcd, let `D` be
the largest remaining degree. The two indices satisfy
`mu1+mu2=aD`. The smaller one is the first degree `ell` at which the
explicit three-term recurrence coefficient matrix has a nonzero kernel;
only `0<=ell<=floor(aD/2)` need be searched. This one computation
determines the source rank for every width `b`.

Zero coefficient polynomials, common factors, the case `D=0`, positive
characteristic, and every original output endpoint are included. For
`D>0`, the first index is zero exactly when the primitive homogeneous
quadratic in `z` has a fixed linear factor over the ground field.

The package specializes and makes effective the prior biform
kernel-bundle formula. It credits the separately solved affine,
constant-endpoint quadratic, and one-polynomial-top families, and the
identical-resultant examples demonstrating the need for finer data.
[sources.json](sources.json) pins the literal source and prior bundle
argument, with the arbitrary-field splitting theorem cited explicitly.
No implementation from an unmerged branch is required.

This is a written, unreviewed one-slice rank result. It supplies no
linear-space cap, compatible three-leg construction, independent
mathematical review, formalization, or smaller matrix-multiplication
exponent. Exact finite controls corroborate the implementation, not the
all-size proof.
