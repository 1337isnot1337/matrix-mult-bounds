# Original-source directions in the Laurent collision chart

This construction inserts original A(8,8) directions outside the
134-dimensional [matrix-core extension](parity_structure_jet_extension.md).
It gives explicit full-rank Laurent maps on all 960 source directions
and a completely verified limit with 28,316 nonzero coefficients.
A coordinate projection of that limit is concise in format
`936 by 936 by 935`.

The limit also has a 126-slice cover. Consequently it cannot restrict
or further degenerate to `M27 direct_sum M7`, whose slice rank is 778.
The large coordinate count does not provide an exponent improvement.
This package preserves an explicit original-source cancellation system
and its exact limitation so that the next construction changes the
leading spaces, rather than only adding more high-degree variables.

## 1. The balanced core and the linear cancellation equations

Multiply the first two leg maps of the preceding extension by `t^-2`
and its third leg map by `t^4`. Their product scale is one, so the
contracted tensor is unchanged. Every row now has one parameter power,
with the following multiplicities on each leg:

| Power | Number of old rows |
| ---: | ---: |
| -2 | 36 |
| 0 | 2 |
| 1 | 60 |
| 4 | 36 |

The old maps use 134 distinct original source coordinates on each
leg. Let `Q_i` be the 826-dimensional coordinate complement on leg i.
We first add new target rows of the form `t*q`, where `q` belongs to
`Q_i` and is independent of the old source directions.

For one such new row, the only possible negative powers in its
contraction with two old rows are:

| Powers of the two old rows | Resulting power | Required equation |
| --- | ---: | --- |
| `(-2,-2)` | -3 | Annihilate their complete source contraction |
| `(-2,0)` or `(0,-2)` | -1 | Annihilate the leading/scalar contraction |

Every term containing two new rows has power at least
`1+1-2=0`. Three new rows have power three. Thus these linear equations
are the complete negative-power system for the initial extension.

The [saved matrix](parity_structure_jet_original_fibers_system.json)
records each equation as its pair of old target rows, their combined
power, and the integer coefficient of every original source coordinate.
The verifier regenerates this matrix by looping over all 262,144
original source terms. It does not use a trace-only submodel or infer
cancellation from the known core restriction.

There are 1,420 nonzero equations on each leg. Sparse elimination over
the rational numbers gives exact ranks

\[
(598,598,597),
\]

so the complete kernel dimensions are

\[
(228,228,229).
\tag{1}
\]

Integral kernel bases are included in the Laurent maps. Each was
obtained by rational back-substitution followed by clearing a common
denominator in each vector. The verifier checks every vector against
every equation. A full-rank certificate for the eventual 960-by-960
coefficient matrix also proves that these kernel vectors are independent;
together with the exact nullities (1), they are complete kernel bases.

## 2. Retaining the new directions and completing a source basis

At initial power one, the new rows give target formats
`362,362,363`, but eight rows on each leg are absent from the constant
tensor. The complete Laurent polynomial shows that no nonzero
coefficient contains two of these absent rows. Each such row can
therefore be rescaled independently by its least occurring power,
without producing any negative coefficient.

On each leg four absent rows have least power two and four have least
power three. Their new row powers are respectively minus one and
minus two. After these rescalings, the constant tensor has 16,108
coefficients and all `362,362,363` directions survive independently.
The particular row indices and shifts are saved with the maps.

Complete the source basis using the unit vectors at the pivot
coordinates of the cancellation matrix. The required complementary
dimensions are `598,598,597`. Give every added row power four.
These additions cannot introduce a negative power: all existing row
powers are at least minus two, so any term meeting a new complementary
row has power at least `4-2-2=0`. Terms meeting two complementary rows
have strictly positive power.

The resulting maps have 960 rows on every leg. Every row is a constant
rational functional times one power of `t`. Write the maps as

\[
G_i(t)=\operatorname{diag}(t^{d_{i,r}})B_i.
\tag{2}
\]

Reduction modulo the prime 1009 certifies `rank(B_i)=960` for all three
legs; therefore each rational matrix `B_i` is invertible. Formula (2)
is consequently invertible for every nonzero parameter. This is an
actual degeneration of the full original A(8,8) tensor in a changed
basis, using original source directions beyond the earlier core.

The final row-power multiplicities are:

| Power | X | Y | Z |
| ---: | ---: | ---: | ---: |
| -2 | 40 | 40 | 40 |
| -1 | 4 | 4 | 4 |
| 0 | 2 | 2 | 2 |
| 1 | 280 | 280 | 281 |
| 4 | 634 | 634 | 633 |

## 3. Complete limit certificate

The [sparse maps](parity_structure_jet_original_fibers_sparse.json)
contain 1,337, 1,335 and 1,271 monomials on the three legs, with
denominators `(1,1,2)`. The original source-column conventions are the
same as in the matrix-core construction.

The verifier examines every original source term. It collects every
contribution whose parameter power is nonpositive, including terms
that later cancel. A source term is skipped only when the sum of the
least powers in its three map columns is already strictly positive.
This is an exact bound, not a numerical cutoff.

There are 648 individual contributions at power minus six and 3,935
at power minus three; all cancel exactly. There are 31,047 individual
constant contributions, which collect to the 28,316 nonzero integer
numerators in the [constant tensor](parity_structure_jet_original_fibers_constant.json).
All other powers are positive and hence vanish in the limit. The
entire constant tensor is checked, including unwanted mixed terms;
it is not asserted to be a matrix multiplication tensor.

Sparse elimination modulo 1009 gives flattening-rank lower bounds
`936,936,935`. The report explicitly lists retained coordinate rows
that project the limit to those dimensions. Recomputing all three
flattenings after all three projections gives full ranks, so this
constructs a concise tensor in that smaller format. No upper bound
equal to those ranks is assumed for the unprojected 960-format limit.

The verifier also doubles a nonzero coefficient in the first newly
inserted original-source row. The resulting full Laurent contraction
fails the stored identity. This checks that the cancellation test is
sensitive to the new source fibers, in addition to the separate
earlier tests of the matrix core and its arms.

## 4. An exact 126-slice cover

Every constant coefficient has row powers summing to zero, and the
only available row powers are `-2,-1,0,1,4`. The possible unordered
patterns are

\[
(-2,-2,4),\quad(-2,1,1),\quad(-1,0,1),\quad(0,0,0).
\tag{3}
\]

Each pattern contains a row of power minus two or zero. Select all
such rows on each leg: there are `40+2=42` per leg, or 126 in total.
The verifier checks directly that this selection meets every one of
the 28,316 constant coefficients.

Assign each coefficient to the first selected coordinate that it
meets. Grouping assigned coefficients by that coordinate expresses
the tensor as a sum of at most 126 slices, in the usual tensor
slice-rank sense. The same upper bound holds for every restriction
or further degeneration of this particular limit: slice rank is
monotone under restriction, and its bounded-rank loci are closed.
See Tao and Sawin, [Corollary 2 and Lemma 3](https://terrytao.wordpress.com/2016/08/24/notes-on-the-slice-rank-of-tensors/).

This is a property of the displayed limit and its postcompositions.
It is not a bound on A(8,8), on all singular maps from A(8,8), or on
other choices of leading spaces and valuations.

## 5. Why the proposed matrix target has slice rank 778

Here is a self-contained argument over the complex numbers. More
generally, let

\[
R=\bigoplus_j M_{n_j},\qquad D=\sum_j n_j^2.
\]

We prove `slice_rank(R)=D`. The upper bound follows by expanding
along any one of the D-dimensional legs. For the lower bound, scale
the j-th block by `n_j^(-1/2)`, an invertible change of basis, and call
the resulting tensor `v`. Each matrix-unit coordinate appears in
exactly `n_j` terms of its block. Consequently all three Gram
marginals of `v` are exactly the D-by-D identity matrix.

For arbitrary traceless Hermitian matrices `H_X,H_Y,H_Z`, the function

\[
f(t)=\left\|
(e^{tH_X}\otimes e^{tH_Y}\otimes e^{tH_Z})v
\right\|_F^2
\]

is convex. Indeed, diagonalizing the Hermitian operator
`H_X tensor I tensor I + I tensor H_Y tensor I + I tensor I tensor H_Z`
writes `f` as a sum of positive multiples of real exponentials.
The identity marginals give

\[
f'(0)=2\operatorname{tr}(H_X)+2\operatorname{tr}(H_Y)
+2\operatorname{tr}(H_Z)=0.
\]

Thus `f(1)>=f(0)`. Polar decomposition of arbitrary
`g_X,g_Y,g_Z` in `SL(D,C)` now proves

\[
\|(g_X\otimes g_Y\otimes g_Z)v\|_F\ge\|v\|_F>0.
\tag{4}
\]

Suppose instead that `v` had slice rank `r<D`. A slice decomposition
and a basis extension on each leg give bases in which every nonzero
coefficient meets one of `r_X,r_Y,r_Z` selected coordinates, where
`r_X+r_Y+r_Z=r`. Normalize these fixed basis changes to determinant
one; this changes the transformed tensor by only a nonzero scalar.
On leg i assign selected coordinates weight `r_i/D-1` and the others
weight `r_i/D`. The weights sum to zero on each leg. Every supported
triple has total weight at most `r/D-1<0`.

The determinant-one diagonal matrices with entries `exp(t*weight)`
therefore send the transformed tensor to zero as `t` tends to
positive infinity. Their compositions with the fixed basis changes
are in `SL(D,C)`, contradicting (4). This proves the lower bound D.
The classical single-square conclusion also appears explicitly in
Blasiak et al., [Remark 4.9](https://arxiv.org/pdf/1605.06702).

For the current target, `D=27^2+7^2=778`. Since `126<778`, the
constructed limit cannot supply that target, even through a further
singular degeneration. Flattening rank alone would not justify this
conclusion; the slice-rank proof and the exact support cover do.

## Replay and dependencies

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_original_fibers.py
python -S -m unittest discover -s tests -p test_parity_structure_jet_original_fibers.py -v
```

The package needs the frozen `parity_structure_jet_extension.py` and
its `parity_structure_jet_collision.py` helper. All checks use the
Python standard library. The [report](parity_structure_jet_original_fibers_certificate.json)
contains exact elimination ranks, retained coordinate lists, the
126 selected slices, and a hash of the complete constant tensor.

The next chart must alter its leading spaces or valuations enough
to admit the matrix target's slice rank. Adding still more rows of
power four to this same low-degree part cannot remove cover (3).
