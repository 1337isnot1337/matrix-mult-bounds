# A homomorphism obstruction when the shared coordinates stay fixed

October 20, 2026. AI-derived proof, unreviewed and not formalized.
No exponent improvement. This applies to a narrower transformation class than
the exact-restriction barrier: here singular maps on the two other legs are
allowed, but the canonical shared coordinates are held fixed.

If `C(a,B)` degenerates to the canonical `T_a tensor B_X(k)` through changes
on Y and Z alone, with padding to the source format, then

$$\boxed{B\ge k(N_a+a-2)-1.} \tag{1}$$

The first cost-one case `a=4,k=1,B=10` is therefore impossible in this class,
despite passing every full-space Koszul test. This does not exclude arbitrary
parameter-dependent changes on the shared leg.

## A two-column test representation

Fix the `a` coefficient indices `i=0,...,a-1`. Let `U_i` be the matrices for
`C(a,2)`, with two columns and `a+1` rows. For a tuple `M=(M_i)` of matrices
with common domain Y and codomain Z, define

$$\operatorname{Hom}(U,M)=\{(F,G): G U_i=M_iF\text{ for every }i\},$$

where `F:C^2 -> Y` and `G:C^(a+1) -> Z`. These are linear equations in F,G,
whose coefficients depend linearly on M. The kernel dimension cannot decrease
in a limit. It is unchanged by independent invertible basis changes on Y and Z.
Thus it is a valid degeneration test with the shared coefficient coordinates
fixed. Taking arbitrary shared basis changes would not preserve this test.

For the source `C(a,B)`, write the columns of F as polynomials `f_0,f_1` of
degree less than B. Compatibility of the consecutive columns of U says
`f_1=t f_0`. Hence `deg f_0<=B-2`; G is then determined. Therefore

$$\dim\operatorname{Hom}(U,C(a,B))=B-1.$$

## The target count

For a canonical block `C(u,v)` with shared output `a=u+v-1`, its arrow matrices
have coefficient `M_i[s,r]=1` if `i=r+s`, and zero otherwise.

If `v>=2`, writing the F columns as vectors `f_0,f_1` gives

$$f_0[0]=0,\quad f_1[u-1]=0,\quad f_1[r]=f_0[r+1]\ (0\le r<u-1).$$

All remaining equations are these repetitions; G is determined. The dimension
is `u-1`. If `v=1` (so `u=a`), there are no two endpoint equations, and the
dimension is `a+1`.

Sum over `u=1,...,a` to obtain

$$\dim\operatorname{Hom}(U,T_a)
=\sum_{u=1}^{a-1}(u-1)+(a+1)=N_a-a+2.$$

The target has `k` copies. Padding its Y space from `kN_a` to B adds
`2(B-kN_a)` homomorphism parameters: the map F is arbitrary into each zero Y
direction. Padding Z contributes none because the images of the `U_i` span
all of `C^(a+1)`. Thus the padded target dimension is

$$k(N_a-a+2)+2(B-kN_a)=2B-k(N_a+a-2).$$

It must be at least `B-1`, proving (1).

## Consequence for the graded search

The coefficient ansatz in `graded_discovery.py` keeps X fixed. Cost-one runs
at `a>=4` are consequently excluded analytically; their small residuals and
growing condition numbers must not be interpreted as construction evidence.
The trust-region run was stopped after the completed a=3 control and a=4
experiment when this obstruction was applied; its a=5 case was unfinished.

The next admissible width at `k=1` is `B=N_a+a-3`. For `a=3,4,5` elementary
coordinate examples meet it. At `a=6` it gives B=24, one below the coordinate
packing obstruction's B=25. This is the next selected numerical discovery
case. The overhead at this lower bound tends to zero, so (1) does not rule
out the asymptotic improvement criterion.

**Subsequent concurrent correction to the active route.** The Koszul worker's
[`6bdab15`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/6bdab15),
`source_obstructions.md`, proves the stronger catalecticant bound
`B>=kN_a+k floor((a-1)^2/4)-floor((a-1)/2)` while the shared coefficient
structure is fixed (also allowing its induced two-variable transformations).
It rejects the selected `a=6,B=24` case. The homomorphism calculation here is
therefore a weaker alternative, not an additional escape route. Further
numerical discovery must permit an arbitrary shared `GL(a)` basis.

The temporary run directory and its process handle were unavailable after a
goal continuation. No result is claimed for the unfinished `a=6,B=24` run,
and the stronger obstruction makes rerunning it unnecessary.

The test is elementary kernel semicontinuity for a quiver homomorphism space.
No general orbit-closure criterion, sufficiency of (1), or border construction
is asserted.
