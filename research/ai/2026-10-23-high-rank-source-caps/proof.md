# Sharp high-rank A4 source caps and the full-short target boundary

October 23, 2026. The four claims
`AI-A4-RANK100-SHARP-LINEAR-SPACE-001`,
`AI-A4-RANK104-SHARP-LINEAR-SPACE-001`,
`AI-A4-RANK108-SHARP-LINEAR-SPACE-001`, and
`AI-A4-RANK112-SHARP-LINEAR-SPACE-001`, together with the target claim
`AI-A4-FULL-SHORT-LONG20-001`, are written and unreviewed. Exact finite
acceptance is not independent external review or formalization.

## 1. Statements

Let V be a complex linear space of canonical A4 source parameters.
Its source slices M(F) are 112-by-112 matrices. The exact maximum
dimensions under the following strict rank hypotheses are:

| Hypothesis for every F in V | Maximum dimension of V | Maximum slice rank in the explicit attaining space |
| --- | ---: | ---: |
| rank M(F)<100 | 84 | 96 |
| rank M(F)<104 | 88 | 100 |
| rank M(F)<108 | 92 | 104 |
| rank M(F)<112 | 96 | 108 |

All spaces V are allowed; coordinate support is used only after the
credited characteristic-zero reduction. The last column describes
explicit attaining examples, not a classification of all extremizers.

For the target consequence, consider any complete complex Laurent
presentation of an A4 degeneration to M(10,10,11). Individually divide
each outgoing map by its lowest entrywise power of t and take its leading
rank. Let a be the short leading rank, and b,c the long leading ranks.

**Target theorem.** If a=100, then b,c<=20. More precisely, each positive
long leading rank belongs to

    {1,2,...,12,20}.                                      (1)

Arbitrary complex leading kernels, higher coefficients and finite Laurent
poles are allowed. This is a necessary condition. No target-compatible
kernel, complete target construction, sharp target bound or improved
matrix multiplication exponent is asserted.

## 2. Credited source reduction and rank inequalities

In the [canonical source convention](../2026-10-20-koszul/cyclic_finite_target.md),
write F_(i,k,s) for the 112 parameters, where i,s range from zero to
three and k from zero to six. The slice matrix is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),              (2)

with out-of-range coordinates interpreted as zero. The short indices
j,p,q,r range from zero to three, and H,L from zero to six.

The [order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md)
replaces every complex bounded-rank parameter space by a coordinate
order ideal of the same dimension and rank bound. It uses the proved
rank-preserving lowering actions and minimum Plucker weight in a closed
Grassmannian locus. Its characteristic-zero hypotheses are retained.
For such an ideal the seven middle layers are nested. Their sizes obey

    16 >= n0 >= n1 >= ... >= n6 >= 0.                    (3)

The [coherent-minor bounds](../2026-10-23-torus-rank80/proof.md), in the
form recorded in the [rank-92/rank-96 proof](../2026-10-23-rank92-rank96-spaces/proof.md),
give a coefficient vector of coherent rank at least rho(n) inside
every short ideal of size n, where

    rho(0)=0,
    rho(n)=16 for 1<=n<=4, 20 for 5<=n<=8,
           24 for 9<=n<=12, 28 for 13<=n<=16.             (4)

The coherent matrix is R(g)_((j,L),(H,r))=g_(H-j,L-r).
A source slice in middle layer k is, after fixed reorderings, H_k
tensor R(g), with rank H_k equal to

    (1,2,3,4,3,2,1)_k.                                   (5)

The middle pairs (0,4), (1,5), and (2,6) have disjoint row supports
and disjoint column supports. Their ranks add, and their coefficient
vectors can be chosen independently in a coordinate parameter space.
Consequently, if every source slice has rank strictly below R, then

    (1,2,3,4,3,2,1)_k*rho(nk) < R for every k,
    rho(n0)+3*rho(n4) < R,
    2*rho(n1)+2*rho(n5) < R,
    3*rho(n2)+rho(n6) < R.                               (6)

Each inequality uses its own coefficient witness. No simultaneous
maximization of the different lower bounds is required. All imported
source formulas, proofs, coherent certificates and reused arithmetic
code are pinned by exact bytes in `sources.json`.

## 3. The four upper bounds

For every threshold R considered here, n3<=12: otherwise (4)-(6) give
rank at least 4*28=112, which is excluded even at the largest threshold.

### Rank strictly below 100

If n0>=13, the first paired inequality implies n4<=8, since
28+3*24=100. If n2>=13, the last paired inequality forces n6=0,
since 3*28+16=100. These give the exhaustive cases:

| Case | Componentwise upper bound on (n0,...,n6) | Total |
| --- | --- | ---: |
| n0<=12 | (12,12,12,12,12,12,12) | 84 |
| n0>=13 and n2>=13 | (16,16,16,12,8,8,0) | 76 |
| n0>=13 and n2<=12 | (16,16,12,12,8,8,8) | 80 |

All remaining entries follow from nesting, n3<=12 and the trivial
upper bound 16. Thus dim V<=84.

### Rank strictly below 104

If n1>=13, then n5<=8 because 2*28+2*24=104. If n2>=13,
then n6<=4 because 3*28+20=104. The complete cases are:

| Case | Componentwise upper bound on (n0,...,n6) | Total |
| --- | --- | ---: |
| n1<=12 | (16,12,12,12,12,12,12) | 88 |
| n1>=13 and n2>=13 | (16,16,16,12,12,8,4) | 84 |
| n1>=13 and n2<=12 | (16,16,12,12,12,8,8) | 84 |

Therefore dim V<=88.

### Rank strictly below 108

If n2>=13, the last paired inequality gives n6<=8, since
3*28+24=108. This leaves only two cases:

| Case | Componentwise upper bound on (n0,...,n6) | Total |
| --- | --- | ---: |
| n2<=12 | (16,16,12,12,12,12,12) | 92 |
| n2>=13 | (16,16,16,12,12,12,8) | 92 |

Thus dim V<=92.

### Rank strictly below 112

The bound n3<=12 alone gives

    n0+...+n6 <= 3*16+4*12 = 96.                         (7)

The credited reduction transfers all four coordinate-ideal bounds to
arbitrary complex linear spaces V. The strict inequalities in (6) are
essential: equality at 100, 104, 108 or 112 is excluded only by the
corresponding strict rank hypothesis.

## 4. Sharp staircase spaces and attained ranks

Specialize the [credited all-size staircase](../2026-10-23-source-staircase-spaces/proof.md)
to a=4, d=3 and m=0,1,2,3. Let V_m have coordinate support

    i<3, with arbitrary k,s;
    or i=3, k<m, with arbitrary s.                       (8)

The two parts are disjoint, so dim V_m=84+4m. Its exact joint column
support in (2) consists of

    H<=5, with arbitrary q,r;
    or H=6, q<m, with arbitrary r.                       (9)

There are 96+4m such columns. For containment, i<3 forces H=i+j<=5.
If H=6 then i=j=3 and p+q=k<m, so q<m. Conversely, every column in
the first group occurs with an allowed i<3 and j having sum H, p=0
and s=0. Every added column occurs with i=j=3, p=s=0. This also
proves that (9) is the exact union of the basis column supports.

Every slice in V_m therefore has rank at most 96+4m, over any field.
This is strictly below the corresponding threshold 100+4m and proves
attainment of each dimension bound in Section 3. The saved integer
coefficient vectors additionally have odd minors of sizes
96,100,104,108. Acceptance rebuilds those minors from the literal
source (2), proving that each maximum slice rank in the first table
is exact over C. No randomness is used in acceptance.

At m=4 the same supported-column formula gives 112 columns, which
does not prove the strict rank-112 hypothesis. The boundary control
records only that limitation; this package does not claim an attained
rank for that extra space.

The strict thresholds cannot be replaced by weak inequalities at the
same caps. V_1,V_2,V_3 have dimensions 88,92,96 at rank ceilings
100,104,108, exceeding the preceding caps 84,88,92. At ceiling 112,
the full 112-dimensional parameter space is a trivial counterexample
to extending cap 96, since every source matrix is 112-by-112.

## 5. Consequence at full short leading rank

The [total-202 and full-short-28 theorem](../2026-10-23-leading-rank202/proof.md)
and its [every-pair prerequisite](../2026-10-23-all-pair-rank136/proof.md)
are retained unchanged. In particular, a=100 already forces each
long rank r to be at most 28.

For the mixed pair (100,r), scalar-balance both maps and compensate
on the remaining map. The pinned all-order cancellation-kernel and
saturated-support arguments produce a complex linear kernel K with

    rank M(F) <= 124-r for every F in K,
    h=dim K >= 110-10*floor(r/10).                        (10)

These statements allow arbitrary finite Laurent poles on the remaining
map and arbitrary leading kernels and higher coefficients. They follow
from the complete tensor identity, not from a truncation to finitely
many jets.

If 21<=r<=28, equation (10) gives h>=90. The source ceiling lies
between 96 and 103, so the first two source theorems give h<=88
(or the stronger h<=84). This contradiction proves r<=20.

There is also a gap below 20. If 13<=r<=19, equation (10) gives
h>=100, while the source ceiling lies between 105 and 111. The last
two source theorems give h<=96 (or h<=92), again a contradiction.
This proves (1), since an individually balanced nonzero map has
positive leading rank.

The exact arithmetic survivors of the prior bound and these four new
caps are r in {0,...,12,20}, if rank zero is included to enlarge the
finite census. For r<=12, the source ceiling is at least 112, so no
new strict source theorem applies. At r=20 the ceiling is 104, and
the applicable source cap is 92; the lower bound h>=90 is compatible.
Using cap 88 at this equality would incorrectly apply a strict theorem
at its excluded boundary.

For any b,c in that surviving set, the long-pair sum is at most 40,
so the long-pair source ceiling is at least 184 and none of the new
caps applies there. The earlier pair and total screens are also
satisfied. The unique full-short numerical maximum is therefore
(a,b,c)=(100,20,20), of total 140. It is not a target construction or
an assertion that the necessary bound is sharp.

## 6. Exact evidence, reproduction and limits

The acceptance program reconstructs all 4,096 literal source terms
and all 256 coherent terms. It checks the 112 middle-layer tensor
factorizations and all three disjoint row-and-column support pairs,
then replays the eleven credited coherent minors and four new sharpness
minors. It verifies the exact joint column support of every basis
slice in each staircase space.

An independent enumeration in acceptance checks all 245,157 nested
seven-layer size profiles against (6) and the written cases. Its
admissible populations at thresholds 100,104,108,112 are respectively
172,062, 210,614, 222,224 and 222,924. The maximum volumes are
84,88,92,96, with respectively 1,1,2,1 maximizing size profiles.
These size-profile counts do not classify actual extremal source spaces.

The target controls export all 102 one-leg decisions for r=0,...,101
and check all 10,404 pairs of long ranks at a=100. The prior bound
retains 841 triples; the new caps retain 196 and exclude 645 additional
triples. Exactly fifteen previously allowed one-leg ranks are excluded:
13 through 19 and 21 through 28. The arithmetic maximum and its unique
endpoint are recovered from the enumeration.

Discovery uses a fixed seed and bounded binary trials only to select
the four new minor witnesses. Each succeeds on its first trial.
Acceptance uses saved integer coefficients, a separate pivot convention,
and no search or symbolic dependency. Modular arithmetic certifies that
integer determinants are odd; the order-ideal geometry remains over C.

All source and target prerequisites retain their exact pinned versions.
The concurrent rank-91 investigation and open coherent-binomial work
are separate from this proof. The upper bounds do not classify all
extremizers or turn source sharpness into target compatibility. No
complete target, smaller exponent, formalization or independent external
mathematical review is claimed.
