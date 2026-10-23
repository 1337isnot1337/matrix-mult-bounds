# Sharp source caps below84 and88, and long leading sum136

October23,2026. Owner-directed OpenAI Codex work over C. Written,
computer-assisted and unreviewed. No independent review, formalization,
matrix target or smaller exponent is claimed.

## 1. Statements and adopted inputs

For the canonical cyclic source A4 let M(F) be its112-by112 slice matrix,
with112 coefficient coordinates F_(i,k,z). Its literal entries are

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),            (1)

with short indices in0,...,3, long indices in0,...,6, and out-of-range
coefficients zero. The source and ordinary slice-rank terminology here
are the pinned prior cyclic-source work; matrix rank is meant throughout.

**Source caps.** A complex linear parameter space V satisfying
rank M(F)<84 for every F in V has dimension at most56. With the strict
bound rank M(F)<88 the dimension is at most60. Both dimension bounds
are sharp.

**Laurent consequence.** In any complete formal A4 to M(10,10,11)
degeneration, individually scalar-balance the two long maps to valuation
zero, compensating on the first map. Their leading ranks b,c satisfy

    b+c<=136.                                         (2)

The source caps are sharp dimension statements. The target bound136 is
only a necessary condition and is not claimed attainable.

We adopt the characteristic-zero order-ideal reduction from the pinned
torus-order-ideal proof. Its literal rank-preserving lowering identities
and minimum-weight argument show that any bounded-rank source space has
a coordinate space of the same dimension and rank bound, whose support
is a downward ideal in the4-by7-by4 box. No additional structural theorem
is imported. Prior rank80 work gives b+c<=144; its sources and the
saturated target-support argument retain their original credit. The
staircase lower examples below are prior PR155 constructions. Exact
file versions and SHA-256 pins are in sources.json.

## 2. Pure layers and a disjoint pair give finite pruning rules

For a short coefficient array g, write the28-by28 coherent matrix

    R(g)_((j,L),(H,r)) = g_(H-j,L-r).

At a fixed middle coordinate k, the source matrix is a row/column
reordering of H_k tensor R(g), where H_k(p,q)=1 if p+q=k and0 otherwise.
The ranks of H_k are

    m_k=(1,2,3,4,3,2,1).

The complete source spaces at middle coordinates1 and5 have disjoint
row supports and disjoint column supports, each of size56. Consequently
independent choices g1,g5 give rank exactly2 rank R(g1)+2 rank R(g5).
Acceptance reconstructs all4096 original six-index terms, checks all112
factorizations and these two disjointness conditions.

There are70 downward short ideals in the4-by4 box. Represent one by
nonincreasing heights h=(h0,h1,h2,h3), each between0 and4. For every
such h the certificate gives a coefficient-zero/one coherent slice and
an odd determinant minor proving a rank lower bound r(h). The inventory
of certified lower bounds is:

| r(h) | 0 | 16 | 20 | 24 | 26 | 28 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Short ideals | 1 | 7 | 16 | 26 | 2 | 18 |

These are witness lower bounds; no coherent maximal-rank classification
is required or asserted. An empty shape has its vacuous rank-zero control.
All other displayed ranks are proved by their saved integer minors.

Let S_0 contain S_1 contain ... contain S_6 be the seven short layers
of a downward source ideal. A source space of strict rank bound R must
satisfy

    m_k*r(S_k)<R for every k,
    2*r(S_1)+2*r(S_5)<R.                                (3)

Otherwise a pure-layer or disjoint-pair witness already violates the
rank bound. Pruning with (3) is therefore valid even though r(h) is only
a lower bound.

## 3. Complete remaining inventories and integer minors

If a putative space below rank84 has dimension at least57, trim its
bounded-rank order ideal to exactly57 points by deleting maximal points.
For rank88 use dimension61 instead. Trimming preserves downward closure
and the rank bound. There are exactly the following inventories after (3):

| Strict rank bound | Ideal dimension | Remaining ideals | Minor size |
| --- | ---: | ---: | ---: |
| 84 | 57 | 1404 | 84 |
| 88 | 61 | 118 | 88 |

The two programs enumerate them differently. Discovery walks the directed
graph of all70 shapes ordered by containment, using memoized completion
counts. Acceptance first enumerates all nonincreasing seven-part volume
profiles summing to57 or61, then recursively constructs each layer's
four heights at the specified volume, bounded by the previous layer.
It applies only (3) and necessary remaining-capacity checks. Every valid
ideal has one profile and one height sequence, so this covers every
possible remaining ideal without duplicates. The full ordered inventory
must equal the certificate's ordered shapes, with no missing entries.

For every one of the1404 and118 ideals, the exported coefficient-zero/one
slice lies in that ideal and has a saved integer minor of the stated
size whose determinant is1 modulo2. The determinant is therefore odd
and nonzero over C. This contradicts the strict rank bound in each case
and proves the dimension caps56 and60.

The characteristic-two arithmetic is used only to certify nonzero
integer determinants. The geometric order-ideal reduction is over C;
no characteristic-two version of it is being inferred.

## 4. Sharpness uses the prior staircase spaces

The PR155 family with source coordinates i<2 and arbitrary k,z has
dimension56. Its matrix columns satisfy H=i+j<=4, so at most5*4*4=80
columns occur. All its slices have rank at most80, strictly below84.

Add the four coordinates i=2,k=0 with arbitrary z. The dimension becomes
60. Only H=5,q=0 introduces new columns, with four possible r, giving
joint column count84. All slices have rank at most84, strictly below88.
The verifier checks exact joint supports, not only these upper bounds.
Thus both source dimension bounds are attained. These lower examples
retain the prior staircase construction's credit; the new contributions
are the matching upper caps and their application.

## 5. Improve the necessary long-rank sum

Let b,c be the balanced long leading ranks, each at most110. Let K be
the kernel of the constant projected source slice map. Prior two-sided
rank loss and the saturated target-support inequality give

    rank M(K) <= delta=224-b-c,
    dim K >= 100-floor(b/11)*floor(c/11).                (4)

The second inequality holds at every finite Laurent pole order, with
arbitrary regular higher jets and complex coordinate mixing. The prior
rank80 result gives b+c<=144.

If141<=b+c<=144, then delta<=83. The new rank84 cap gives dim K<=56.
But the two floors sum to at most13, so their product is at most42.
Equation (4) requires dim K>=58, a contradiction.

If137<=b+c<=140, then delta<=87. The rank88 cap gives dim K<=60.
The floors now sum to at most12 and their product is at most36, forcing
dim K>=64, another contradiction. Therefore (2) holds. All644 integer
rank pairs in these intervals are also replayed exactly, with minimum
dimension margins2 and4 respectively. No target or exponent follows.

## 6. A concrete boundary of the dimension-only method

At b=c=68, (4) requires a source space of dimension at least64 and rank
at most88. The prior staircase with i<2, together with i=2,k=0,1 and
arbitrary z, has exactly dimension64 and joint column count88. It meets
these two numerical conditions. Thus no universal source-space cap
strictly smaller than64 at rank at most88 can close this balanced pair.

This space is not asserted to be the kernel of an actual two-sided
compression of these defects, and supplies no compatible higher maps.
Further progress can use such compression incidence, stronger compatible
target supports or the all-order equations. The example does not exclude
those routes or establish a surviving degeneration.

## 7. Verification and evidence status

Discovery is separate from acceptance. Acceptance imports no discovery
module; it reconstructs the literal tensors, checks all coherent controls,
independently enumerates both complete inventories and verifies every
minor. Frozen reports record exact scope. Source pins and corrupted,
missing or inflated evidence are tested. These finite checks support the
written arbitrary-complex-space and all-order arguments; they do not
formalize or independently review them. The matrix target and an exponent
below9/4 remain unconstructed.
