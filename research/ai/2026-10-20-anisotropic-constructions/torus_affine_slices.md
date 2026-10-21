# Exact propagation of the next torus slices

October 21, 2026. The complete next-slice equations exclude the corrected
fixed-boundary family whose six extreme slices and initial M4 were exact.
This is a limitation of those fixed boundary coefficients. A separate
[degree-13 pencil proof](torus_degree13_pencils.md) subsequently excludes
the full original ordinary torus profile. The ungraded source restriction
remains open. No smaller
matrix multiplication exponent is established.

## The affine family

The common physical source is

\[
W(F)_{(i,q),(p,s)}=F(i,p+q,s),\qquad 0\le i,p,q,s<8.
\]

Put v=(0,7) and u=(7,0). The 238 boundary source coordinates determine
the two rows and two columns indexed by v and u. The remaining 722
coordinates form a space K: every W(F) with F in K has zero rows and
columns at both endpoints. Their coordinate description is

\[
\begin{array}{c|c|c}
\text{middle index}&\text{allowed first and last indices}&\text{count}\\
0\le k\le6&0\le i,s\le6&343\\
k=7&1\le i,s\le6&36\\
8\le k\le14&1\le i,s\le7&343.
\end{array}
\]

For the torus profile, all source coordinates of weights +13 and -13
belong to the boundary. Thus the two target rows at each of these
weights are completely fixed on each leg. In the corrected seed their
physical matrices have no block from the 62 interior vertices to
themselves. If S is any of these fixed matrices and U,V belong to K,
then tr(SUV)=0. Consequently each complete fixed-slice equation is
affine-linear jointly in the free maps on the two other legs.

The script reconstructs this fact directly from every one of the
262,144 source terms. It checks the vanishing free-by-free block for
all twelve slices: four target rows on each of three legs. For each
slice, 7,420 target coefficient pairs have the correct total charge;
all other target coefficient pairs vanish by the torus condition.

## A three-coordinate contradiction

The corrected seed with SHA-256
`8a76858cfecfae6c690b3c9e99917438629ab25d2ef79680a717e7d02b45b67e`
fixes the following three boundary parts, in target row order
(25,726,707):

\[
\begin{aligned}
J_X(E_{0,25})&=e(0,13,0),\\
J_Y(E_{26,24})&=e(7,7,2)+U,\\
J_Z(E_{26,5})&=e(7,2,6)+V,
\end{aligned}\qquad U,V\in K.
\tag{1}
\]

The first map is completely fixed by its weight -13. Let X, Y0, Z0
denote the three displayed coordinate vectors. Direct multiplication
gives, for every common source vector F,

\[
\operatorname{tr}(W(X)W(Y0)W(F))=F(7,2,6),\qquad
\operatorname{tr}(W(Z0)W(X)W(F))=F(7,7,2).
\tag{2}
\]

Both coordinates on the right belong to the boundary. Thus (2) vanishes
on every permitted free variation. The constant tr(W(X)W(Y0)W(Z0)) is
one. The free-by-free term vanishes by the endpoint block observation.
It follows that the full image of the coefficient in (1) is always one.

Its matrix multiplication coefficient is zero, because
E_(0,25) E_(26,24)=0. The small M7 block has no variable in this
coefficient and cannot affect the conclusion. Therefore no choice of
the 722 free source columns completes this fixed boundary to M27
direct sum M7.

This does not dispute either positive partial identity: the six extreme
slices and the initial M4 tensor were checked exactly. They did not
include the coefficient in (1). It also does not exclude changing the
boundary maps, changing the weight profile, or arbitrary singular maps.

## Reusable exact solver

`torus_affine_slices.py` constructs all the affine equations for any
selected fully fixed target-weight blocks, after verifying that their
free-by-free source block is zero. It uses integer sparse elimination.
If inconsistent, it exports a rational linear combination of original
equations whose left side is zero and whose right side is nonzero.
That combination is substituted back into the original equations.
If feasible, an exact rational point is substituted into every original
equation instead. Neither outcome decides the unexamined cubic equations.

For the corrected seed the twelve full slices produce 19,872
nontrivial equations, with 20,220 nonzero linear coefficients involving
18,642 of the 94,698 free torus parameters. Each equation has at most
two variables. The coefficient (1) is already the equation 0=-1,
so the contradiction needs no elimination or numerical rank estimate.

The saved complete run is
`results/anisotropic-constructions-2026-10-20/torus-affine-slices-corrected.json`.
Its input SHA identifies the fixed seed even if a later seed uses
different boundary choices. The dependency-free function
`fixed_boundary_contradiction_control()` separately verifies (1)-(2),
all 722 free basis endpoint conditions, and the required target zero,
without requiring the large seed file.

Run the complete propagation with:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/torus_affine_slices.py results/anisotropic-constructions-2026-10-20/parity_balancing_torus_anchor_seed.json --output results/anisotropic-constructions-2026-10-20/torus-affine-slices-corrected.json
```

The three-coordinate argument was checked by the root agent and a
second construction agent in this generating session. There has been
no external independent review or formalization.
