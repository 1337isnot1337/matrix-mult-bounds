# General quadratic biform kernel degrees

Owner-directed Codex investigation, October 23, 2026. Base main
`bd03b9dadba03b1089595f03ff7a091ee9e7ddbc`.

Determine the exact rank of the literal cyclic-source coefficient matrix
for every nonzero `u(x)+z*v(x)+z^2*w(x)`, with all coefficient degrees below
`a`, `a>=2` and `b>=3`, over an arbitrary field.

The recurrence `u*lambda_r+v*lambda_(r+1)+w*lambda_(r+2)=0` defines a
rank-two polynomial kernel. After dividing the common polynomial factor,
write `D` for the largest coefficient degree. The intended result is an
exact rank formula in terms of its two minimal degrees, with sum `a*D`,
and a bounded coefficient-matrix procedure determining the smaller degree.
Every original source coefficient, including degree endpoints, must be
retained. Export exact controls against the literal source matrix.

PR216 exhibits equal-degree, equal-resultant slices with different ranks
and identifies these kernel degrees as its follow-up. PR217 treats the
special family with only the top coefficient polynomial. PR209 supplies
the earlier affine recurrence, and the constant-endpoint quadratic proof
is preserved in consolidation PR214. This investigation concerns the
general three-polynomial kernel and credits those earlier scopes.

A formula for one slice is not a source-space cap, compatible target maps,
a degeneration, or an exponent improvement. The proof and finite controls
must retain separate evidence statuses. No independent review is assumed.
