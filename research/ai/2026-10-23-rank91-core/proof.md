# A common rank-91 core and total leading rank at most 198

October 23, 2026. Claims AI-A4-RANK91-LINEAR-SPACE-001 and
AI-A4-LEADING-RANK-SUM198-001 are written and unreviewed. Exact integer
certificates support the proof; internal replay is not independent
external mathematical review or formalization.

## 1. Statements and frozen prerequisites

For the canonical A4 source, let F have coordinates F_(i,k,s), with
0 <= i,s <= 3 and 0 <= k <= 6. Its 112-by-112 source slice is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),             (1)

where j,p,q,r range from zero to three, H,L from zero to six, and
out-of-range F coordinates are zero.

**Source theorem.** If V is a complex linear parameter space and
rank M(F) < 91 for every F in V, then dim V <= 67.

Equivalently, every 68-dimensional complex source parameter space
contains a slice of rank at least 91. The dimension cap 67 is not
claimed sharp. The threshold is strict: the pinned preceding construction
has dimension 68 and maximum slice rank exactly 91.

**Target theorem.** For every complete complex Laurent A4 presentation
of M(10,10,11), let a,b,c be the individually scalar-balanced leading
ranks, with a on the 100-dimensional target leg. Then

    a+b <= 133,   a+c <= 133,   b+c <= 136,
    a+b+c <= 198.                                       (2)

The only ordered integer triples of total 198 surviving the stated
necessary screens are (62,66,70) and (62,70,66). These are arithmetic
endpoints, not constructed targets. The inherited implication
a=100 => b,c<=28 remains valid. The necessary total leading-rank loss
is at least 320-198=122.

This continuation retains the complete
[leading-rank202 proof](../2026-10-23-leading-rank202/proof.md), including
its all-order support inequalities and every-pair136 prerequisites.
It also retains the
[sharp source caps below92 and96](../2026-10-23-rank92-rank96-spaces/proof.md),
the [characteristic-zero order-ideal reduction](../2026-10-23-torus-order-ideal/proof.md),
and the [canonical source convention](../2026-10-20-koszul/cyclic_finite_target.md).
All are pinned to exact bytes in sources.json. None of those files is
modified. Their previous coherent-minor, saturation, and PR151 credits
remain in force. No new external structural theorem is imported.

## 2. Equality in the preceding dimension-68 bound

Assume for contradiction that every slice of V has rank at most 90
and dim V >= 68. The preceding sharp cap below92 gives dim V <= 68,
so equality holds. The credited order-ideal reduction yields a coordinate
order ideal of the same dimension whose slices still have rank at most90.
Write its seven short layers as S_0,...,S_6, with sizes n_0,...,n_6.
They are nested and 16 >= n_0 >= ... >= n_6 >= 0.

The preceding proof bounds these seven sizes by one of four profiles,
each of total 68. Equality of total size forces componentwise equality:

| Label | (n_0,n_1,n_2,n_3,n_4,n_5,n_6) |
| --- | --- |
| A | (16,16,16,8,8,4,0) |
| B | (16,16,12,8,8,4,4) |
| C | (16,12,12,8,8,8,4) |
| D | (16,12,8,8,8,8,8) |

The reduction and this equality argument concern complex spaces.
Modulo-two computations below only certify nonzero integer minors.

Recall the coherent matrix

    R(g)_((j,L),(H,r)) = g_(H-j,L-r).                    (3)

A pure middle-k source slice has rank
(1,2,3,4,3,2,1)_k times rank R(g). The middle pairs (0,4),(1,5),(2,6)
have disjoint row and column supports. Coefficient vectors on two
layers can be chosen independently. The credited lower rank available
on a short ideal of size n is

    rho(0)=0;
    rho(n)=16,20,24,28 on the intervals
    1..4, 5..8, 9..12, 13..16, respectively.             (4)

These are lower bounds for available witnesses, not assertions that
every vector or every short space has that rank.

## 3. A strip lemma and the eight remaining ideals

For d=1,2,3, the coherent binomial with coefficient one at (d,0)
and (0,d) has an odd minor of size 20,24,26, respectively. The first
two witnesses are copied from the preceding certificates with credit.
The third is a new fixed 26-minor. Only the indicated lower ranks are
used; no general binomial-rank classification is assumed.

**Strip lemma.** A downward-closed short ideal of size 4d, all of whose
coherent slices have rank below 20,24,26 respectively, is a full strip
of d rows or d columns in the 4-by-4 grid.

Indeed, if it contains both (d,0) and (0,d), the binomial contradicts
the rank bound. If it misses (d,0), downward closure confines it to
i<d. That strip has exactly 4d cells, so equality of sizes fills it.
If it misses (0,d), the same argument confines and fills s<d.

Apply the lemma to the four profiles:

1. Each profile has n_3=8. The pure middle-three rank is four times
   the coherent rank, so every S_3 slice has coherent rank at most22.
   Therefore S_3 is a two-row or two-column strip. Equal-size nested
   layers coincide, so every other size-eight layer is the same strip.
2. In B and C, a size-twelve S_2 has nonempty S_6. The disjoint pair
   (2,6) gives 3 rank R(g_2)+16 <=90, so rank R(g_2)<=24<26.
   In C and D, the size-twelve S_1 has a size-eight S_5, for which
   a rank20 witness is available. Thus 2 rank R(g_1)+40<=90,
   so rank R(g_1)<=25<26. Every size-twelve layer is a three-strip.
3. In A and B, S_1 is the full short grid and has an available rank28
   slice. The pair (1,5) gives 56+2 rank R(g_5)<=90, so the size-four
   S_5 has coherent rank at most17<20. In C, S_2 has an available
   rank24 slice, so (2,6) gives 72+rank R(g_6)<=90 and the size-four
   S_6 has rank at most18<20. These size-four layers are axes.
   The equal-size layers S_5,S_6 in B coincide.

These statements are uniform over each indicated layer: the witness
on the other layer can be chosen independently of the tested vector.
Nesting forces all strips to have the same orientation. A full
two-row strip contains an entire row of length four, so it cannot lie
in a three-column strip; likewise, the perpendicular full axis cannot
lie in the two-row strip. Transposition gives the other orientation.

Consequently exactly four canonical ideals and their transposes remain.
For a profile entry 4d, its canonical short shape is d full rows;
size-zero and size-sixteen layers are empty and full. This specifies
all eight ideals without a large coordinate-ideal census.

## 4. One common core excludes all eight ideals

Every canonical ideal contains the following coordinate core I. A
short shape (h_0,h_1,h_2,h_3) includes (i,s) exactly when s<h_i.

| Middle k | Short shape of I |
| ---: | --- |
| 0 | (4,4,4,4) |
| 1 | (4,4,4,0) |
| 2 | (4,4,0,0) |
| 3 | (4,4,0,0) |
| 4 | (4,4,0,0) |
| 5 | (4,0,0,0) |
| 6 | (0,0,0,0) |

The dimension of I is 16+12+8+8+8+4=56. The fixed coefficient vector
and minor in certificates.json give an odd 91-by-91 determinant:

    coefficient mask: 0xd000006c0082d1d0d949fb
    row mask:         0x183fff019ffffffffffffffffff
    column mask:      0xf00efffffffffffffffffffff

Bits select source coordinates in lexicographic (i,k,s) order. Rows
use index (4j+p)*7+L, and columns use (4H+q)*4+r. Thus these three
integers specify a complete exact witness, not a numerical rank estimate.
Acceptance reconstructs every entry from the original six-index source
sum and verifies the selected square minor by binary elimination.
An odd integer determinant is nonzero over the complex numbers.

Transposing the two outer source indices preserves matrix rank. More
precisely, F_(i,k,s) -> F_(s,k,i) corresponds to transposition and the
row/column reindexing

    ((j,p,L),(H,q,r)) -> ((r,q,H),(L,p,j)).                (5)

Substitution in (1) proves (5), and acceptance checks it on all 4,096
literal terms. Thus the transposed ideals contain a rank91 witness too.
All eight cases contradict the assumed uniform rank at most90. This
proves the source theorem. It does not classify extremal spaces at
dimension67 or prove that dimension67 is attainable below rank91.

## 5. The mixed-pair bound and total leading rank

The target hypotheses and all-order argument are those of the frozen
leading-rank202 proof. For any chosen pair of outgoing maps with
balanced leading ranks p,q, scalar powers make those two maps regular
and are compensated on the remaining map. This leaves the same pair
of leading ranks and permits arbitrary finite Laurent poles on the
unselected map.

The linear cancellation kernel K of the two constant maps satisfies

    rank M(F) <= 224-p-q for all F in K,
    dim K >= 110-floor(p/10)floor(q/10) for a mixed pair,
    dim K >= 100-floor(p/11)floor(q/11) for a long pair.  (6)

The first inequality is the elementary compression rank bound; the
other two are the pinned saturated target-support inequalities. They
hold for arbitrary complex leading kernels and arbitrary higher map
coefficients in the complete Laurent identity. No finite-jet,
coordinate-kernel, or regular target-unit premise is introduced.

Every pair already has sum at most136. If a mixed pair has sum134..136,
then its source ceiling in (6) lies between88 and90. The source theorem
gives dim K<=67. But the two quotients by10 have sum at most13, so their
product is at most42 and (6) gives dim K>=68. This contradiction proves
the two mixed-pair bounds133. The long bound136 remains in force.

Write T=a+b+c. The pair bounds in (2) imply

    T-136 <= a <= 266-T,
    T-133 <= b,c <= 269-T.                               (7)

Suppose T>=199. Then (7) gives 63<=a<=67 and 66<=b,c<=70. Each mixed
sum is at least129 and at most133. Since floor(a/10)=6, a long rank
at most69 would make the quotient product36. The frozen202 screen
requires product at least38 at sums129..132 and at least42 at sum133.
Thus both b,c must be at least70, contradicting b+c<=136. This proves
T<=198. All earlier screens remain available, including the exceptional
high-sum exclusions that the new source cap alone does not establish.

For completeness, the new cap also strengthens the long-pair quotient
product to at least33 when its sum is134..136. The old bound at sum133
remains32, and all lower-sum rules are unchanged.

## 6. Arithmetic endpoints and limits of the conclusion

If T=198, (7) gives 62<=a<=68 and 65<=b,c<=71. Interchange the long
legs so that b<=c.

If a>=64, every mixed sum is at least129. The same quotient argument
forces b,c>=70, impossible. If a=63, the only pair not immediately
excluded by that argument is (b,c)=(65,70). Its long sum135 has quotient
product floor(65/11)floor(70/11)=30, below the required33, so it is
excluded too. Thus a=62 and b+c=136. The possibilities are
(65,71),(66,70),(67,69),(68,68). The first fails the long product bound;
the last two fail a mixed product bound. Only (66,70) remains.

Both ordered triples (62,66,70),(62,70,66) pass the necessary screens:
the mixed sums are128 and132, and the latter has quotient product42;
the long sum136 has quotient product36>=33. This proves exactness of
the arithmetic maximum198. It does not construct compatible source
kernels, higher Laurent coefficients, or a target with these ranks.

The old numerical endpoint (70,66,66) is now excluded: each mixed
pair needs dim K>=68 but its source ceiling88 forces dim K<=67.
The inherited full-short condition a=100 => b,c<=28 is retained.
No stronger full-short theorem is claimed in this package.

The acceptance report replays four integer minors, enumerates the
four size profiles and all eight strip ideals independently, and checks
the transpose identity. It then checks all 20,706 admissible-domain rank
pairs and all 1,050,804 rank triples, exporting the complete old and new
survival masks. There are 36 new mixed-pair and 24 new long-pair
exclusions, which remove 5,250 further triples. The written structural and quotient arguments supply
the universal theorems. The finite census checks their arithmetic
consequences. No source dimension sharpness at67, target sharpness,
external review, formalization, or exponent improvement is claimed.
