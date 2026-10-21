# A four-map obstruction to the first extreme-slice seed

October 21, 2026. The first rational A88 seed satisfies every coefficient
in its six extreme slices. The following exact identity shows that
four of its next-layer maps cannot be held fixed in a full M27 plus M7
restriction. This is a restriction on that seed, not on general source
maps or on the corrected endpoint construction.

## Coordinates and fixed maps

Write e(i,k,s) for a source coefficient vector in the common physical
ordering W(F)_(i,q),(p,s)=F(i,p+q,s). All three legs use this ordering,
with the cyclic permutations already specified in the source notes.
The 27 target vertices have the charge profile in `parity_structure_torus_seed.md`.
Vertices 0, 1, 25, 26 have charges 0, 1, 13, 14.

The original seed fixes these four maps, after dividing by its common
denominator 64:

\[
\begin{aligned}
J_X(E_{0,25})&=e(0,13,0)+e(0,14,1)+e(1,14,0),\\
J_X(E_{1,26})&=e(0,13,0)-e(0,14,1)-e(1,14,0),\\
J_Y(E_{25,0})&=e(7,1,7)-e(7,0,6)-e(6,0,7),\\
J_Y(E_{26,1})&=e(7,1,7)+e(7,0,6)+e(6,0,7).
\end{aligned}
\tag{1}
\]

Let X be the difference of the first two maps and Y the difference
of the last two. Direct physical matrix multiplication gives, for
every source vector F on the third leg,

\[
\operatorname{tr}\bigl(W(X)W(Y)W(F)\bigr)=-4F(0,7,7).
\tag{2}
\]

For a short verification, W(X)=2(W(e(0,14,1))+W(e(1,14,0))) and
W(Y)=-2(W(e(7,0,6))+W(e(6,0,7))). Their product has exactly one entry:
-4 at physical row (1,7), column (0,6). The corresponding trace
coefficient of W(F) is F(0,1+6,7), proving (2).

## Contradiction with the already normalized extreme slices

The target matrix identity is

\[
(E_{0,25}-E_{1,26})(E_{25,0}-E_{26,1})=E_{00}+E_{11}.
\tag{3}
\]

The extreme maps on the first two legs are
J_X(E_(0,26))=e(0,14,0) and J_Y(E_(26,0))=e(7,0,7).
Their physical product is the diagonal unit at (0,7). Therefore
their already satisfied slice equation forces, for every target Z,

\[
J_Z(Z)(0,7,7)=Z_{00}.
\tag{4}
\]

Equations (2)-(4) would require -4Z_00=Z_00+Z_11 for every Z. Taking
Z=E_11 gives 0=1. This contradiction holds regardless of how the
remaining third-leg coordinates are changed, and therefore excludes
any completion retaining (1) and the stated normalized extreme maps.
The unused M7 block cannot repair the contradiction inside the M27 block.

This is stronger than failure to optimize the 722 free source columns:
even changing other boundary coordinates cannot help while the four
maps (1) and the extreme maps remain fixed. It does not exclude changing
those four maps. No arbitrary Laurent family is classified here.

## Exact control showing how to escape

The monotone M4 endpoint seed uses instead

\[
e(0,13,0),\quad e(1,14,0),\quad e(6,0,7),\quad e(7,1,7)
\tag{5}
\]

for those four target units. Its image of E_11 is e(1,8,7).
The left side of (3), evaluated on this third-leg vector, is exactly
one. Thus the new endpoint maps escape this particular obstruction.
Their full M4 identity is checked in `monotone_endpoint_seeds.py`.

The standard-library verifier `fixed_anchor_obstruction.py` checks all
960 coefficients of the functional (2), the exact extreme functional
(4), the target product (3), and the corrected endpoint control (5).
It rejects a changed coefficient in the four fixed maps. The saved
certificate is `results/anisotropic-constructions-2026-10-20/fixed-anchor-obstruction.json`.

Review status: author-checked algebra and exact coefficient replay.
No external independent review, formalization, or exponent improvement
is claimed.
