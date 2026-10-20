# A two-sector upper bound and a smaller endpoint amplitude interval

2026-10-20. AI-derived written argument, unreviewed and not Lean formalized.
**No smaller exponent is established.** The finite Fourier source and sector
packing use standard tools. No historical priority is claimed.

## 1. A source-rank constraint for every character

For all positive integers a,b, put r=a+2b-1. Restrict W_r to first-leg
indices 0<=i<a. Split each of its other index ranges into [0,b-1] and
[b,r-1]. Give those Y spaces weights -1,0 and the Z spaces weights 0,1;
the first leg has weight zero.

The potentially negative left/left block is identically zero: there
i+j+k <= (a-1)+2(b-1)=r-2, whereas supported terms have i+j+k=r-1.
The right/right block has positive weight and disappears. The two matched
off-diagonal blocks remain, sharing their first leg.

For Y left and Z right, reverse the Z index to k'=r-1-k. Then k'=i+j,
giving C(a,b). For Z left and Y right, reverse Y instead. This is C(a,b)
with its second and third tensor legs exchanged. All coefficients are one.

The shared-leg entropy inequality, multiplied over the six orientations and
optimized with equal probabilities, gives

    P(W_(a+2b-1)) >= 2 P(a,b).

The cyclic Fourier certificate gives lambda(W_r)<=r. W_r is invariant under
every permutation of its legs, so P(W_r)=lambda(W_r)^(1/t). Consequently

    2 P(a,b) <= (a+2b-1)^(1/t).                         (1)

By symmetry, the same bound holds with 2a+b-1 on the right. This is an
all-size character inequality, not a conjectural packing or a dimension-only
score. It can strengthen the old rank upper bound even though the matching
profile survives it at t=3/4.

The verifier checks every retained coefficient for 144 (a,b) choices and
the critical matching-profile comparison for every a,b<=128. It finds no
profile violation. Those finite controls are separate from the proof above.

There is also an all-size compatibility certificate, so extending that grid
is unnecessary. Write H_m=(3m-1)/2; the earlier bound is h_m^3<=H_m.
If b>=a then

    (2P_*(a,b))^3/(a+2b-1)^4 <= H_a/(a+2b-1) <= 1/2.

If a>=b put R=a+2b-1 and C=3b-1. Then

    (2P_*(a,b))^3/R^4 <= (C/2)(2R-C)^3/R^4 <= 27/32.

The last inequality follows by maximizing the displayed one-variable ratio
at R=2C, or by the exact factorization

    27v^4-16(2v-1)^3=(v-2)^2(27v^2-20v+4)>=0,
    v=R/C>=1.

Equality in the global comparison occurs at (a,b)=(3,1). Thus P_* survives
the whole family with the uniform cubed score deficit 27/32. This is a
barrier for this explicit family, not a lower bound on omega.

## 2. Consequence for the hypothetical endpoint character

Use the scaling/rigidity theorem on concurrent branch
`research/filtration-compatibility-20261020`, commit `b381178`, file
`research/ai/2026-10-20-concavity-equivalence/homogeneous_rigidity.md`.
That written theorem, building on Uznański's earlier rescaling, supplies
the limit and critical shape. It is another worker's result, not proved
anew or independently reviewed here. Its hypotheses are the actual profile's
replication, rank bound, positivity, symmetry, concavity and tripling.

If a character has t=3/4, its scaling limit therefore is

    F(x,y)=K min(x,y)^(1/3) (max(x,y)+min(x,y)/2), K>0.

Scale (1) by a common integer and pass to the established limit:

    2F(x,y) <= (x+2y)^(4/3).

Taking x=4,y=1 yields 9K <= 6^(4/3), or

    K^3 <= 16/9.                                        (2)

This is the optimal consequence of (1) for this homogeneous shape. With
x/y=a>=1 the cubed upper bound is (a+2)^4/(2a+1)^3, and

    9(a+2)^4-16(2a+1)^3=(a-4)^2(9a^2+16a+8)>=0.

The other aspect-ratio half gives no smaller bound, by symmetry and the
second version of (1).

On the other hand the first-pass lower profile forces, for every integer m,

    K^3 >= h_m^3/m.

Indeed F(m,b)>=P_*(m,b); divide by b and let b tend to infinity. The limit
of h_m/m^(1/3), already computed in the first pass, is 1/Gamma(4/3).
Thus every hypothetical endpoint character must have

    1/Gamma(4/3) <= K <= (16/9)^(1/3),

approximately 1.1198465217 <= K <= 1.2114137286. The old simple rank bound
only gave K^3<=128/27. The new interval is narrower but is **nonempty**.
Neither the existence of such a character nor its exclusion follows.

## 3. Dependencies and source comparison

The normalization and shared-leg theorem are from OpenAI's October 2, 2026
paper at fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. The scalar lower profile
is prior local work. The critical-shape bridge is credited above. The full
text of Uznański v2 was checked here, especially Sections 2--5: its
two-sector splitting is the different determinant splitting with a retained
dot factor, and its three-sector splitting gives the prior tripling law.
This source check is not a claim that the construction (1) is historically
new. Its role here is an additional explicit necessary constraint.

The next task is to find a constraint inconsistent with the entire remaining
amplitude interval, or another uniform improvement mechanism. Rechecking
that P_* survives (1) at larger finite sizes cannot by itself do that.
