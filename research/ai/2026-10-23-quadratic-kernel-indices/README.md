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

The [structural sequel](dichotomy.md) narrows the possible first index:
it either equals `(a+1)` times a rational-root height or lies between
`ceil((a-1)D/2)` and `floor(aD/2)`. Homogeneous irreducibility forces
the latter interval; a sufficiently small rational-root height fixes
both indices exactly. Endpoints and inseparable quadratics are included.
It also proves the complete nonzero `a=b=3` biform rank spectrum
`{9,12,14,15}` over every field, excluding rank thirteen, with universal
witnesses for all four values. This is a biform-block spectrum, not a
classification of full cyclic-tensor slices.
For every balanced size `a=b>=3`, quadratic-z biform ranks are contained
in `{a²,a²+a,a²+2a−1,a²+2a}`; only primitive degree two can yield
the one-below-full value. This containment does not assert that every
listed value occurs over each field and size.

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
