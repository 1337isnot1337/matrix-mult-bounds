# The A(8,9) equality investigation

October 21, 2026. Historical investigation and exact counterexamples.
The later `block_hankel_dimension.md` excludes the M30 plus M3 ordinary target.

The candidate M(30,30,30) plus M(3,3,3) has all target leg dimensions 909.
For A(8,9), N=1152 and ab=72, so each output kernel has dimension 243.
A rank-at-most-three parameter in the large block has target slice rank at
most 90. Its ordinary source lift therefore has rank at most

    90 + 243 + 243 = 576 = 8 ab.

The existing polynomial symbol bound only gives Hankel rank at most eight,
which is automatic for the 8-by-9 symbol. Strict inequalities cannot be
substituted at this equality. This explains why the rank-three saturation
argument leaves the candidate open; it is not evidence that maps exist.

A possible next step is to classify slices of rank exactly 8ab with symbol
rank eight. Both polynomial coefficient injections must attain equality.
The general coefficient-map equality lemma in
`../2026-10-20-anisotropic-constructions/parity_structure_equality.md`
then forces constant linear dependencies in each successive coefficient map.
However, its published rank-two recurrence proof does not immediately extend:
at rank eight there is no ninth row in the 8-by-9 symbol to recover the same
recurrence from both orientations. A purported generalization that simply
uses that missing row would be invalid.

A proof would need to use equality in the outer coefficient map as well,
or independently classify the relevant bivariate Hankel matrix spaces. Even
a pointwise classification would still need a family argument for the lifted
rank-at-most-three parameter variety. Neither classification nor that family
argument is supplied in this checkpoint.

A direct construction remains an alternative: explicit three-leg maps must
produce all 27,000 large-block multiplication coefficients and all 27 small-
block coefficients, with every mixed coefficient zero. Passing the numerical
score or these necessary rank tests is not such a construction.

## An exact warning against the unrestricted equality extension

For A(2,3), take the symbol sequence (0,x,0,1). Its Hankel matrix is
[[0,x,0],[x,0,1]], of rank two over Q(x). The full rational source slice
has rank exactly 12=2ab. But the two coefficient sequences (0,0,0,1) and
(0,1,0,0) have no common nonzero quadratic annihilator: their stacked
recurrence matrix has rank three. Hence they lie in no constant length-two
scheme span, including nonreduced schemes or schemes containing infinity.
The companion `equality_counterexample.py` checks both ranks over Q.

This does not contradict the maintained rank-two theorem, which assumes
both a,b>=3. It disproves the proposed extension allowing symbol rank equal
to the smaller format size without additional hypotheses. In general, setting
all z-coefficients except s=0 to zero makes the full slice split into a copies
of an ab-by-bm matrix, giving rank at most a^2 b. Thus that equality threshold
contains a substantial family which cannot be classified by merely repeating
the lower-rank proof. The later block-Hankel dimension proof excludes M30 plus M3 by a different argument.

## Counterexample in the actual frontier format

The failure persists for every A(a,a+1), a>=2, including A(8,9). Put

    f_k(x,z) = sum_(t=1)^a t^k + x (a+1)^k,   0<=k<2a.

These coefficients obey the required degree bounds and are independent of z.
At x=0 the leading a-by-a Hankel minor is V V^T, where V is the square
Vandermonde matrix of 1,...,a. Its determinant is nonzero. Thus the symbol
has full row rank a over Q(x). The general polynomial rank inequality gives
rank(M_F)>=a^2(a+1); the constant-z block decomposition in the preceding
section gives the reverse bound. Equality holds exactly.

Suppose the coefficient sequences shared a constant scheme of length at
most a. A nonzero degree-a homogeneous annihilator would give an affine
polynomial q of degree at most a. Applying it to the constant-in-x sequence
for shifts 0,...,a-1 yields

    sum_(t=1)^a t^k q(t)=0,  0<=k<a.

Vandermonde invertibility forces q(1)=...=q(a)=0. Applying it to the
coefficient of x forces q(a+1)=0. Hence q is identically zero, a contradiction.
This includes a possible root at infinity, since the affine polynomial may
have degree smaller than a. The supplied Q-rank calculation for a=8 checks
one 72-by-144 block of rank72, repeated eight times, and the stacked
annihilator matrix of rank9. It certifies slice rank576 with no constant
length-eight scheme. This is a family of source slices, not tensor maps to
the proposed direct sum, so it supplies no improved exponent.

## The equality threshold cannot be rounded upward

There is also an exact A(8,9) slice with full symbol rank eight, full source
rank577, and crossed rank nine: take f_0=1, f_7=xz, all other f_k=0.
The leading symbol minor is a nonzero signed power of xz. The crossed
flattening has two disjoint blocks of ranks one and eight.
`equality_one_step.py` constructs the complete source support, computes rank
577 over F2, and verifies a row/column support cover of size577. The modular
lower bound and characteristic-zero support upper bound agree, certifying
rank577 over Q without a floating computation. The recorded cover is replayable.
Thus a lifted-rank upper bound577 cannot be treated as576. A hoped-for gap
of eight above576 is false, and no such rounding is used in the screen.
