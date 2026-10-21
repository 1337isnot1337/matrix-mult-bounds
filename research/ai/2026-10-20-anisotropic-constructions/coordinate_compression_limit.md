# A dimension limit for common coordinate codes

October 21, 2026. This note limits one particular way to extend the
new endpoint seed. It does not exclude arbitrary monomial maps,
mixed coefficient maps, or singular degenerations. No smaller matrix
multiplication exponent is established.

## The proposed family

Let S be a set of n distinct vertices (i_u,q_u) in the a-by-b physical
grid, with 0<=i_u<a and 0<=q_u<b. In the physical trace model

\[
W(F)_{(i,q),(p,s)}=F(i,p+q,s),
\]

the most direct coordinate lift of a target matrix unit selects

\[
J(E_{uv})=\lambda_{uv}\,e_{(i_u,q_u+i_v,q_v)},
\qquad \lambda_{uv}\ne0.
\tag{1}
\]

Here e is a source coefficient vector; its physical matrix can have
several nonzero entries. Formula (1) describes a restricted family of
maps. It is not a normal form for arbitrary restrictions.

If even one leg of a proposed restriction to M_n uses (1), the map
must have n^2 linearly independent rows. Matrix multiplication is
concise: every target matrix unit participates in a nonzero product.
Thus all n^2 source coordinates selected in (1) must be distinct.
Nonzero scalar factors cannot repair two coincident coordinates.

## The necessary integer inequality

Let r be the largest number of vertices of S in any one physical row,
and let c be the largest number in any one physical column. Choose a
row i with r neighbors Q and a column s with c neighbors I. Every
pair (q,p) in Q times I occurs among the target matrix units, and its
selected source coordinate is (i,q+p,s).

Consequently all rc sums q+p must be different. They are integers in
the interval from 0 through a+b-2, so

\[
rc\le a+b-1.
\tag{2}
\]

The row and column pigeonhole bounds give r>=ceil(n/a) and
c>=ceil(n/b). Combining them proves

\[
\boxed{\left\lceil\frac n a\right\rceil
       \left\lceil\frac n b\right\rceil\le a+b-1.}
\tag{3}
\]

This argument already concerns injectivity, before any cubic tensor
coefficient is checked. It also applies to an M_n block within a
larger concise direct sum when its rows have form (1).

## Consequence for the live A(8,8) target

If n>=25, each ceiling in (3) is at least four, but 16>15. Therefore
every map of this form has n<=24. In particular, the common coordinate
code cannot supply the M27 block of the live M27 plus M7 target.

The exact endpoint M4 and product M12 seeds pass this injectivity
test. An M27 construction must leave this common coordinate-code family
on every target leg. General monomial assignments need not
come from a common physical vertex set S and are outside this proof.
The endpoint equations with bilinear slack also remain outside it.

## Exact collision certificates

`coordinate_compression_limit.py` constructs an explicit pair of
distinct target matrix units selecting the same source coordinate.
It checks three specified 27-vertex subsets of the 8-by-8 grid and
two collision-free seed controls. These examples exercise the
certificate extractor; the pigeonhole proof establishes the result
for every S in the stated family.

The verifier independently checks the two selected source coordinates.
Its tests reject a corrupted collision certificate. Reproduce with:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/coordinate_compression_limit.py
```

Review status: author-checked proof and exact finite certificates.
There is no external independent mathematical review or formalization.
