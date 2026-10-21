# Two scalars: an ordinary-restriction obstruction

**Claim over C, with ordinary maps only.** For the fixed endpoint corner
R of format `(16,18,18)`,

\[
R\oplus D_2\not\ge M(4,4,4).
\]

This note does **not** exclude degeneration from `R direct-sum D2`.
Affine summands can diverge and cancel along a singular family; the
one-scalar Grassmannian proof does not by itself cover two scalars.
There is also no three-scalar claim and no general Q64 claim.

## Data from the exact corner

Let `E_B,E_C` be the endpoint long spaces, each of dimension 14. The
two four-dimensional first-input families are

\[
F_0=t^5\otimes P,\qquad G_0=P\otimes t^5.
\]

All of their nonzero R slices have rank four. Their aggregate supports
are

\[
\begin{array}{c|cc}
&B&C\\\hline
F_0&E_B&F_C\ (\dim F_C=4)\\
G_0&G_B\ (\dim G_B=4)&E_C,
\end{array}
\]

where `F_C` is a subspace of `E_C` and `G_B` is a subspace of `E_B`.
These are the source fibres and exact supports described and checked in
[m1_endpoint_corner.md](m1_endpoint_corner.md).

## Proof

Suppose an ordinary restriction to M4 exists. Write its two scalar
terms as

\[
a_1\otimes b_1\otimes c_1+a_2\otimes b_2\otimes c_2.
\]

The restriction of the first-leg map to R's 16-dimensional A space is
invertible. Otherwise a nonzero target A functional annihilates that
image and leaves a slice of rank at most two, whereas M4 has minimum
nonzero A-slice rank four and has no zero slice.

Pull back `F0,G0` through this dual isomorphism and call the resulting
four-dimensional target functional spaces F and G. On either family,
the R contribution has slice rank four and the scalar contribution has
rank at most two. Thus every nonzero M4 slice in either family has rank
at most six and hence exactly four.

As proved in the one-scalar note, a four-dimensional rank-one matrix
space underlying such M4 slices has aggregate supports `(16,4)` or
`(4,16)`. The a priori support bounds here force

\[
\operatorname{suppdim}M4(F)=(16,4),\qquad
\operatorname{suppdim}M4(G)=(4,16),
\tag{1}
\]

because the source bounds are `(16,6)` for F and `(6,16)` for G.

Let `H_B` be the image of `E_B`. The B support of the F tensor is
contained in

\[
H_B+\langle b_1,b_2\rangle,
\]

whose dimension is at most 16. By (1), its dimension is exactly 16.
Therefore `dim H_B=14`, both scalar B directions are independent modulo
`H_B`, and both scalar A linear forms are nonzero on F. Likewise, G's
16-dimensional C support forces the map on `E_C` to be injective and
forces `c1,c2` to be independent modulo its image.

Write `K_C` for the four-dimensional C support of the F tensor in (1).
There is a direct sum

\[
H_B\oplus\langle b_1,b_2\rangle.
\]

Projecting the F tensor along `H_B` onto either scalar B direction
extracts `ell_i restricted to F tensor c_i`. Since these linear forms
are nonzero, both `c_i` belong to `K_C`.

Projecting instead onto `H_B`, along the two scalar B directions,
extracts the R contribution on F. Thus the image of `F_C` also lies in
`K_C`. The map on `E_C` was just shown to be injective, so this image
has dimension four. It equals `K_C`.

Consequently both scalar C vectors lie in the image of `F_C`, and
therefore in the image of `E_C`. This contradicts the independence
modulo that image forced by G's 16-dimensional C support. The ordinary
restriction is impossible.

The projections in the last two paragraphs are essential. Supports of
two tensors do not in general add: shared factors can combine two
directions into one graph. Here the forced 16-dimensional support gives
the direct-sum decomposition that makes the projections legitimate.

## Why this is not a three-scalar or border claim

With three scalar terms, a scalar A form can vanish on one fibre and
be nonzero on the other. The active scalar B and C spans need not be
the same on F and G. The tight independence argument for two scalars
therefore does not automatically extend.

For degeneration, an ordinary decomposition's affine pieces need not
have finite limits individually. The assertion above is only an
ordinary-restriction exclusion. A singular two-scalar correction is an
open constructive question in this note.

This is a written same-session argument using the already exact corner
identities. Same-session review does not constitute external
mathematical review, and no exponent bound is changed.
