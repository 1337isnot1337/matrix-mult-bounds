# Saturated weight blocks exclude the width-13 common profile

Status: proof written; checked in the generating session. No external review
or formal proof is claimed. This result does not improve the matrix
multiplication exponent.

## A necessary rank inequality

Let a concise graded tensor T be an ordinary grading-preserving restriction
of a graded tensor S. Write its three injective parameter maps as
J_X, J_Y, J_Z. Fix weights x+y+z=0. Suppose

    dim T_X,x = dim S_X,x,  dim T_Y,y = dim S_Y,y.

Then these two weight-space maps are isomorphisms. Let R_S and R_T be the
ranks of the third-leg flattenings of the corresponding (x,y,z) blocks.
Set delta = dim S_Z,z - dim T_Z,z. Necessarily

    R_T >= R_S - delta.                                      (1)

Indeed, after identifying the first two parameter spaces through their
isomorphisms, the target third flattening is the source linear map
S_Z,z -> S_X,x* tensor S_Y,y* restricted to the image of J_Z. Restricting
a linear map to a subspace of codimension delta lowers its rank by at most
delta. Conciseness gives injectivity of J_Z. This argument is valid over
every field. It concerns ordinary restrictions; it does not establish the
same necessary inequality for arbitrary singular limiting maps.

## Exact source ranks

Use common coordinates F(i,k,s), with 0<=i,s<8 and 0<=k<15, of weight
i+s-k. The source is

    sum X(i,p+q,s) Y(p,r+s,j) Z(r,i+j,q),

where all six short indices run from 0 through 7. For fixed source
coordinates X=(i,k,s), Y=(p,ell,j), there is at most one matching Z:

    q=k-p, r=ell-s, Z=(r,i+j,q),

provided 0<=q,r<8. Thus the pair contractions are zero or individual
coordinate functionals, with coefficient one. Their rank is exactly the
number of distinct output coordinates; this is an exact rank computation
in every characteristic, not a numerical estimate.

For weights (-11,11,0), the output coordinates are precisely

    F(r,r+q,q),  0<=r<=3, 4<=q<=7.                          (2)

For the upper inclusion, writing k=i+s+11=p+q and ell=p+j-11=r+s
gives r<=3 and q>=4 from the short-index bounds. The remaining inequalities
are the ordinary source ranges. For the lower inclusion, given r,q in
(2), put i=max(0,r+q-7). A pair producing the required coordinate is

    X=(i,i+11,0), Y=(11+i-q,r,r+q-i).

Here 0<=i<=3, 0<=11+i-q<=7, and 0<=r+q-i<=7. The pair weights are
-11 and 11. Consequently R_S=16. The saved certificate contains all
sixteen witnesses and rechecks this image by an independent six-index
expansion of all 262144 source terms.

## The width-13 profile

Give the 27-dimensional target vertex space multiplicities

    (1,2,2,2,2,2,2,2,2,2,2,2,2,2)

at charges 0 through 13. Give the seven-dimensional target vertex space
one vertex at each charge 0 through 6. Use the same vertex charges on
all three target spaces. Matrix unit E_ij has weight c_i-c_j.

The nonnegative weight dimensions are:

| Weight | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Source | 64 | 63 | 61 | 58 | 54 | 49 | 43 | 36 | 28 | 21 | 15 | 10 | 6 | 3 | 1 |
| Target | 60 | 56 | 51 | 46 | 41 | 36 | 31 | 26 | 22 | 18 | 14 | 10 | 6 | 2 | 0 |

Negative dimensions agree by symmetry. The profile passes all dimension
budgets. Its weight -11 and weight 11 parameter maps must be
isomorphisms, since both source and target dimensions are 10.

For the target (-11,11,0) block, a nonzero term has vertices i,j,k with
c_i-c_j=-11 and c_j-c_k=11. Hence c_i=c_k is 0, 1, or 2. All pairs at
these three charges occur. Their multiplicities are 1,2,2, so the third
flattening rank is

    R_T = 1^2 + 2^2 + 2^2 = 9.

The M7 summand has no weight 11 or -11 parameter. The third map has
codimension 64-60=4. Inequality (1) would therefore require

    9 >= 16-4 = 12,

which is impossible. **There is no ordinary grading-preserving
restriction A(8,8) -> M27 direct-sum M7 with this charge profile.**

Orientation matters: the opposite (11,-11,0) block has target rank 12,
so that comparison alone gives no contradiction. The program saves all
eight nonzero comparisons using the saturated weights +/-11 and +/-12.

## Verification and scope

`torus_saturated_blocks.py` also accepts unequal charge lists on the three
vertex spaces through `screen(a,b,blocks)`. It only applies (1) after
checking saturation on both input spaces. It also checks the usual
unconditional upper bound R_T<=R_S for every ordered block, since
flattening rank cannot increase under linear restriction. Its positive control is the
identity A(1,1)->M1. Passing the screen is only a necessary condition.

The recorded exclusion does not address ungraded maps, other charge
profiles, or arbitrary Laurent degenerations with poles. It does not
exclude the ungraded A(8,8)->M27 direct-sum M7 frontier.

Replay:

```sh
python research/ai/2026-10-20-anisotropic-constructions/torus_saturated_blocks.py --verify results/anisotropic-constructions-2026-10-20/torus-saturated-width13.json
python -m unittest discover -s tests -p 'test_torus_saturated_blocks.py' -v
```
