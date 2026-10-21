# Screening the free-interior M7 maps as a fixed small block

October 21, 2026. The low and high M7 maps in the exact interior
construction cannot be frozen as the final small block in
A(8,8) -> M27 direct sum M7. Their charge-compatible scalar diagonal
mixtures also fail. This statement concerns these displayed map
spaces; it does not exclude a different or moving M7 embedding.

## The necessary mixed-coefficient inequality

Fix two maps of the small M7 block. Contracting them against the source
defines a linear map from the remaining 960-dimensional source leg
to the space of bilinear forms on those two small target legs.
Let its rank be R. Every row of the remaining M27 map must lie in
its kernel, since a coefficient with one large and two small variables
must be zero. Those 729 large rows must be independent. Therefore

\[
729\le960-R.\tag{1}
\]

In the torus grading this holds separately at every weight w:

\[
\dim (M_{27})_w\le \dim A(8,8)_w-R_w.\tag{2}
\]

This check uses only two-small/one-large coefficients. Further mixed
equations can impose more conditions, so passing it would only be a
necessary condition for completion.

## The two pure maps

In common source coordinates, the low map sends E_IJ to F(I,J,0),
for 0<=I,J<7. Given the neighboring low matrix units E_IJ and E_KL,
the source coefficient on the remaining leg is

\[
F(L,I,J-K)\quad\text{if }J\ge K,
\]

and zero otherwise. Every point of the low cube
0<=i,k,s<7 occurs. Each pair row selects a single source coordinate,
so the exact contraction rank is 343. Reflection gives the same
rank for the high map. Equation (1) fails because

\[
960-343=617<729.
\]

At weight zero the rank is 28, counted by i+s=k inside the low
cube. The source weight-zero space has dimension 64 and the M27
target weight-zero space has dimension 53. Thus the stronger local
failure is

\[
64-28=36<53.\tag{3}
\]

The full per-weight ranks are replayed and recorded for all three
remaining-leg choices. The low and high lists are reflections of
each other.

## Diagonal mixtures do not repair this screen

Reverse the high vertex order so both blocks have target charges
0 through 6. The high map is then

\[
H(E_{IJ})=F(I+1,J+8,7),
\qquad L(E_{IJ})=F(I,J,0).
\]

For each leg i choose scalar coefficients alpha_i,beta_i and use
alpha_i L + beta_i H. The exact M7 direct sum M7 construction shows
that the resulting tensor is

\[
(\alpha_X\alpha_Y\alpha_Z+
\beta_X\beta_Y\beta_Z)M_7.\tag{4}
\]

The scalar in (4) must be nonzero to normalize to M7. Hence at least
one of the two threefold products is nonzero. For each pair of legs,
the associated channel pair is then nonzero. Projection of the
pair-contraction matrix onto that channel's source cube has rank
343, proving R>=343. The other channel cannot cancel these projected
coordinates.

More explicitly, the cross contractions L times H and H times L
vanish on the whole remaining source leg: the reconstructed first
short index is respectively L+8 or L-7, outside its allowed range.
If both channel products are nonzero, pairs with J>K give 294
independent low coordinates, pairs with J<K give 294 independent
high coordinates, and J=K gives 49 independent low/high combinations.
Thus R=637. Its weight-zero rank is 49, leaving only 15 of the 53
required large-block directions. Rescaling the nonzero coefficients
does not change these ranks.

This argument also survives changes of target bases within either
fixed channel image when the two selected channel pairs remain full
M7 maps: projection onto a source cube still has rank 343. It does
not assert that arbitrary maps through all three interior summands
must split into these scalar channel choices.

## Exact replay

`parity_structure_free_m7_screen.py` loads the saved integral interior
maps, forms each of the three pair contractions by traversing the
complete 262,144-term source, and computes the rank over the rationals
weight by weight. It checks both pure maps and the equal diagonal
mixture. The latter initially gives 2M7, and dividing one leg by two
normalizes the small tensor without changing a pair rank.

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_free_m7_screen.py
```

The original interior M7 direct sum M7 direct sum M6 restriction is
unaffected. This screen explains why freezing one of its displayed
M7 components would leave too few source directions for the final
M27 block. No new exponent or general small-block obstruction is
claimed.
