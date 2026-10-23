# Every balanced A4 leading-rank pair has sum at most136

October23,2026. Claim `AI-A4-ALL-PAIR-RANK136-001` is a written,
unreviewed theorem over C, with exact integer controls. It is
owner-directed AI-derived work, without independent external
mathematical review or formalization.

## 1. Statement and credited prerequisites

In any complete Laurent presentation of an A4 degeneration to
M(10,10,11), divide each outgoing map by its lowest entrywise power
of t. Let a,b,c be the ranks of the resulting first nonzero
coefficients, with a on the100-dimensional target leg.

**Theorem.** Every such presentation satisfies

    a+b<=136,       a+c<=136,       b+c<=136.              (1)

Their total is at most204. If a=100, then b<=36 and c<=36.
These are necessary conditions only. No sharpness of the leading-rank
bounds, occurrence of a remaining rank triple, target construction,
or smaller matrix multiplication exponent is claimed.

The [every-pair144 theorem](../2026-10-23-all-pair-rank144/proof.md)
is a retained prerequisite. In particular, it already excludes all
larger sums, including the exceptional mixed pair(100,100), and
records the individual bounds a<=100 and b,c<=101. Its canonical
source, saturated-lattice argument, earlier source caps, and credited
PR151 compression method retain their original attribution.

The new [source-space theorems](../2026-10-23-rank84-rank88-spaces/proof.md)
give, for arbitrary complex linear spaces V of canonical A4 source
parameters,

    rank M(F)<84 for every F in V  implies dim V<=56,
    rank M(F)<88 for every F in V  implies dim V<=60.     (2)

The source theorems are sharp, but that sharpness does not imply
sharpness of the target leading-rank conditions. Exact versions of
both prerequisite proofs are pinned in `sources.json`. This package
adds only the all-order target application and its finite integer
endpoint checks.

## 2. All-order compression and support hypotheses

Choose any two target-leg maps. Multiply each by a scalar power of t
to make it regular with a nonzero constant coefficient, compensating
the product of those scalar factors on the remaining map. This keeps
the full tensor identity unchanged and gives the same two ranks as
individual balancing. The remaining map can have arbitrary finite
Laurent poles; both regular maps can have arbitrary higher jets and
complex leading kernels.

Write the regular pair in slice convention as B(t),C(t), with leading
ranks p,q. For the112-by112 canonical source define

    K={F : B(0) M(F) C(0)=0},       h=dim K.

The image of C(0) has dimension q. Every M(F), F in K, sends it into
the(112-p)-dimensional kernel of B(0). Extending the domain by a
complement therefore gives

    rank M(F)<=224-p-q for every F in K.                 (3)

The saturation argument retained in the every-pair144 proof gives

    h>=100-floor(p/11)*floor(q/11)       for a long pair,
    h>=110-floor(p/10)*floor(q/10)       for a mixed pair. (4)

To recall its all-order content, the flattening after the two regular
maps has a generic row space of dimension at most112. Its saturated
C[[t]] lattice has a residue of the same dimension. This residue
contains both the constant projected-source space, of dimension112-h,
and the full limiting target matrix space. Laurent coefficients on
the remaining map do not invalidate that containment because the
complete output is regular. The intersection therefore has dimension
at least the target parameter dimension minus h.

The target slices have the form X tensor I_m, with m=11 for the long
pair and m=10 for a mixed pair. If such a subspace lies in the leading
images of dimensions p and q, its underlying joint column and row
dimensions are at most floor(p/m) and floor(q/m). Its dimension is
at most their product, proving(4). Thus no coordinate-kernel or
regular target-unit assumption, and no finite pole-order ceiling,
is introduced by this application.

## 3. Close sums137 through144

By the retained theorem it remains only to consider sums at most144.
For sums141 through144, the right side of(3) lies between80 and83,
so the first bound in(2) gives h<=56. For sums137 through140, it lies
between84 and87, and the second bound in(2) gives h<=60.

For a long pair of sum at most144, the two floor quotients in(4)
have sum at most13. Their product is at most6*7=42, so h>=58.
For a long pair of sum at most140, the quotient sum is at most12,
their product is at most6*6=36, and h>=64.

For a mixed pair of sum at most144, the quotient sum is at most14,
their product is at most7*7=49, and h>=61. This bound holds in both
new intervals. Thus the complete contradictions are:

| Pair type | Leading-rank sum | Required h minimum | Source cap for h |
| --- | --- | ---: | ---: |
| Long/long | 141 through144 | 58 | 56 |
| Long/long | 137 through140 | 64 | 60 |
| Short/long | 141 through144 | 61 | 56 |
| Short/long | 137 through140 | 61 | 60 |

Every row has a strictly larger lower bound than upper bound. Combined
with the prior144 theorem, this proves every inequality in(1).

Adding the three pair inequalities gives twice the total rank at most
408, hence a+b+c<=204. Setting a=100 in either mixed inequality gives
the long-rank upper bound36.

## 4. Exact finite controls and limits

The standalone verifier uses only integer arithmetic. It enumerates
all10,302 mixed pairs with0<=a<=100,0<=b<=101 and all10,404 long
pairs with0<=b,c<=101. Allowing rank zero enlarges the checked range.
It retains the prior exclusions above144 and checks every new pair
at sums137 through144:

| Pair type | Prior excluded pairs above144 | Newly excluded pairs | All pairs above136 |
| --- | ---: | ---: | ---: |
| Mixed | 1,653 | 492 | 2,145 |
| Long/long | 1,711 | 500 | 2,211 |

The checker verifies the exact interval minima in the preceding table.
The prior144 result is not discarded: the special mixed pair(100,100)
still relies on that prerequisite, since the new dimension caps alone
are too weak there. No large source matrix or earlier finite minor
census is copied into this application checker.

Both thresholds in(2) are strict. A source rank ceiling84 uses cap60,
not cap56. At a pair sum136, equation(3) gives rank at most88, so the
strict rank88 theorem does not apply. The controls therefore retain
(68,68) in both pair formats and mixed(100,36) as open to this argument.
These are arithmetic boundary controls, not target constructions.

The written proofs of the imported source theorems and the saturation
argument provide the universal hypotheses. The integer enumeration
checks their finite consequence and does not replace those proofs,
establish external independent review, or formalize the theorem.
