# Total balanced A4 leading rank is at most 202

October 23, 2026. Claim `AI-A4-LEADING-RANK-SUM202-001` is a written,
unreviewed theorem over the complex numbers. The finite acceptance uses
only integers. It does not supply independent external mathematical
review or formalization.

## 1. Statement and exact prerequisites

Consider any complete complex Laurent presentation of an A4 degeneration
to M(10,10,11). For each outgoing map, divide by its lowest entrywise
power of t and take the rank of the resulting constant coefficient.
Write these three individually balanced leading ranks as a,b,c, with
a on the 100-dimensional target leg and b,c on the two 110-dimensional
target legs.

**Theorem.** Every such presentation satisfies

    a+b+c <= 202.                                         (1)

If a=100, then

    b <= 28 and c <= 28.                                  (2)

The pair constraints in Section 3 also hold. They refine the retained
inequalities a+b,a+c,b+c<=136. The total leading target-rank loss is
therefore at least 320-202=118. These are necessary conditions; no
presentation attaining them is constructed or asserted to exist.

The [every-pair 136 theorem](../2026-10-23-all-pair-rank136/proof.md)
is retained in full, including its individual bounds a<=100 and
b,c<=101. The [preceding every-pair 144 proof](../2026-10-23-all-pair-rank144/proof.md)
supplies the inherited all-order saturation argument and exceptional
mixed-pair compression argument. Both retain their canonical-source,
lowering, source-cap, and PR151 credits.

The [new source-space theorems](../2026-10-23-rank92-rank96-spaces/proof.md)
prove that, for arbitrary complex linear spaces V of canonical A4
source parameters,

    rank M(F)<92 for every F in V  implies dim V<=68,
    rank M(F)<96 for every F in V  implies dim V<=72.      (3)

Both source caps are sharp: their explicit source spaces have dimensions
68 and 72 and maximum slice ranks 91 and 95. Source-space sharpness does
not assert target compatibility. All three imported proofs are pinned
by exact SHA-256 digests and repository versions in `sources.json`.
The present package does not change those proofs or their certificates.

## 2. Why the source caps apply at every Laurent order

Fix any two outgoing maps and multiply them by scalar powers of t so
that both are regular with nonzero constant coefficients. Compensate
the product of these scalar factors on the remaining map. This preserves
the complete tensor identity and gives the same two leading ranks p,q
as individual balancing. The unselected map may have arbitrary finite
Laurent poles. The regular maps may have arbitrary higher coefficients
and complex leading kernels.

In the slice convention of the pinned proofs, let B(0),C(0) be the
selected constant maps and define the linear cancellation kernel

    K={F : B(0) M(F) C(0)=0},        h=dim K.

For F in K, M(F) sends the q-dimensional image of C(0) into the
(112-p)-dimensional kernel of B(0). Extending by a complement in the
112-dimensional source gives

    rank M(F) <= 224-p-q for every F in K.                (4)

The pinned saturated-support argument gives

    h >= 110-floor(p/10)*floor(q/10)  for a mixed pair,
    h >= 100-floor(p/11)*floor(q/11)  for a long pair.     (5)

For clarity, its all-order content is the following. The generic row
space after the two regular maps has dimension at most 112. Its saturated
complex power-series lattice has a residue of the same dimension. That
residue contains both the constant projected-source space, of dimension
112-h, and the complete limiting target slice space. Their intersection
has dimension at least the target parameter dimension minus h. A target
slice X tensor I_m supported in leading images of dimensions p,q has
underlying joint column and row dimensions at most floor(p/m),floor(q/m).
The intersection dimension is at most their product. This is (5), with
m=10 or 11. Arbitrary finite Laurent poles on the remaining map do not
remove the target-space containment, because the complete output is
regular. The exact lattice proof is part of the pinned prerequisites.

Thus (3) applies to the whole linear space K whenever the right side
of (4) is strictly below its stated threshold. No coordinate-kernel,
regular target-unit, or finite jet assumption is introduced here.

## 3. The exact additional pair screens

Write s=p+q. By the retained theorem s<=136. Equations (3)-(4) give

| Pair sum s | Source rank ceiling 224-s | Upper bound on h |
| --- | --- | ---: |
| 133 through 136 | 88 through 91 | 68 |
| 129 through 132 | 92 through 95 | 72 |
| At most 128 | At least 96 | No new bound from (3) |

At a ceiling of 92 only the second theorem in (3) applies. At a ceiling
of 96 neither applies. Equality of the lower and upper bounds for h
is allowed; a contradiction requires a strict excess.

Combining this table with (5) gives the complete additional inequalities:

| Pair type | Sum 129 through 132 | Sum 133 through 136 |
| --- | --- | --- |
| Mixed | floor(p/10)floor(q/10)>=38 | floor(p/10)floor(q/10)>=42 |
| Long/long | floor(p/11)floor(q/11)>=28 | floor(p/11)floor(q/11)>=32 |

These are exact descriptions of this arithmetic screen, not sufficient
conditions for a target degeneration. Sums at most 128 get no additional
exclusion from the two new source caps. Sums above 136 remain excluded
by the retained theorem, even when the new caps alone are too weak.
For example, mixed (100,100) has lower bound h>=10 and is not excluded
by (3) alone.

The mixed constraints have a useful equivalent form. Set u=floor(p/10)
and v=floor(q/10). At sum 129, u+v<=12 and uv<=36, so no mixed pair
survives. At sums 130 through 132, u+v<=13 and uv>=38 force

    (u,v) in {(5,8),(6,7),(7,6),(8,5)}.                  (6)

At sums 133 through 136, uv>=42 instead forces

    (u,v) in {(6,7),(7,6)}.                              (7)

Conversely, every pair within the established rank ranges and stated
sum interval with the indicated quotients passes the new screen. This
follows by substituting its quotient product in the table. To see that
the lists are exhaustive, a quotient sum at most 12 has product at
most 36. At quotient sum 13 the products, with the smaller quotient
at most 6, first reach 38 at 5*8=40, and reach 42 only at 6*7.

The analogous long-pair quotient lists, for divisor 11, are recorded
in the finite evidence. At sums 129 through 131 the list is
(4,7),(5,6),(6,5),(7,4). At sum 132 it is the union of that list with
(4,8),(5,7),(6,6),(7,5),(8,4). At sums 133 through 136 it is just
the latter five pairs. These follow from the displayed product bounds
and quotient sums at most floor(s/11).

## 4. The total bound and its unique arithmetic endpoint

Let T=a+b+c. The three retained pair inequalities imply T<=204 and,
for each r among a,b,c,

    T-136 <= r <= 272-T.                                 (8)

The lower bound subtracts the opposite pair from T. For the upper bound,
add the two pairs containing r, obtaining T+r<=272.

Suppose T>=203. Equation (8) puts every rank between 67 and 69. Any
mixed pair then has sum between 134 and 136, source rank ceiling at
most 90, and lower bound h>=110-6*6=74. The first theorem in (3)
forces h<=68, a contradiction. This proves (1).

There is exactly one ordered integer triple with total 202 that passes
these pair screens: (a,b,c)=(70,66,66). Here "ordered" keeps the short
leg in the first coordinate. Indeed, (8) puts every rank between 66
and 70. If a<=69, at least one of b,c is at most 69, because b=c=70
would violate b+c<=136. That mixed pair has sum at least 132 and both
quotients equal to 6. Thus h>=74, while its source ceiling is at most
92 and (3) gives h<=72. This is again impossible. Consequently a=70,
and the two mixed pair inequalities force b=c=66.

The numerical triple (70,66,66) passes: each mixed pair has sum 136,
source ceiling 88, and h lower bound 110-7*6=68, equal to its cap.
The long pair has sum 132, source ceiling 92, and h lower bound
100-6*6=64, at most its cap 72. This proves that 202 is the exact
maximum of these arithmetic screens. It does not prove that the
necessary target bound is sharp or that a complete Laurent presentation
with those leading ranks exists.

## 5. Full short rank

If a=100, the prior mixed bound gives b,c<=36. Suppose one long rank
r lies between 29 and 36. Its mixed pair has sum between 129 and 136,
so (3)-(4) give h<=72 (and sometimes the stronger bound 68). But

    h >= 110-10*floor(r/10) >= 80,

a contradiction. This proves (2). Every integer triple (100,b,c) with
0<=b,c<=28 passes the stated screens: its mixed sums are at most 128
and its long sum is at most 56. Hence the screened full-short maximum
is 156, uniquely at (100,28,28). Again this is an arithmetic endpoint,
not a constructed target. Allowing rank zero enlarges the census; an
individually balanced nonzero map actually has positive leading rank.

## 6. Complete integer evidence and scope

The standalone verifier imports no source constructor or symbolic algebra
package. It enumerates every mixed pair in [0,100] x [0,101] and every
long pair in [0,101]^2, including the strict endpoints in Section 3.

| Pair type | Checked | Prior exclusions above 136 | New exclusions | Retained |
| --- | ---: | ---: | ---: | ---: |
| Mixed | 10,302 | 2,145 | 488 | 7,669 |
| Long/long | 10,404 | 2,211 | 329 | 7,864 |
| Total | 20,706 | 4,356 | 817 | 15,533 |

Of the new mixed exclusions, 262 have sums 129 through 132 and 226
have sums 133 through 136. The corresponding long counts are 125
and 204. The verifier also checks all 1,050,804 triples in
[0,100] x [0,101]^2. The prior pair inequalities retain 603,885;
the new screens retain 541,407 and exclude 62,478 additional triples.
All 841 triples (100,b,c), 0<=b,c<=28, are retained. The claimed
maxima and unique arithmetic endpoints are recovered independently
from the full enumeration.

The compressed census exports two complete bit masks for each domain:
one for prior survival and one for survival after the new screens.
Its documented lexicographic indexing records the outcome for every
case, including prior exclusions. Acceptance rebuilds all masks and
compares them exactly, together with the counts, endpoints, quotient
lists, source pins, and claim scope. The report pins the canonical
uncompressed census bytes. There is no floating-point acceptance.

The universal theorem uses the imported geometric and source-space
proofs and the short contradictions above. The finite census verifies
their integer consequences. Neither the census nor the source sharpness
examples construct target-compatible kernels, solve higher-order target
equations, or improve the matrix multiplication exponent. All new claims
remain written and unreviewed.
