# Two-stage mixed-leg border seeds and a saturated-anchor obstruction

Claim: AI-EXTERNAL-DOUBLE-LEG-ANCHOR-012. Written proof, unreviewed.
Field: Q and characteristic-zero extensions. No exponent or rank improvement.

## Four exact physical families

Start with the externally attributed rank-76 M(4,5,5) integer tensor
pinned at SHA-256 bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3.
Reuse the exact eleven U and two W replacements, plus the common
physical stabilizer, from the predecessor 2026-10-23-mixed-leg-splits.
The three basis matrices have determinants (1,1,-1), with weights

    r=(0,3,22,60), s=(0,6,22,22,3), t=(0,0,-13,-13,6).

Make two additional W replacements after the prior U replacements.
All indices are zero-based; each new replacement scalar is +1.

| Variant | New W changes | U/V/W projective directions | Positive Laurent coefficients |
| --- | --- | --- | --- |
| 24-30 | W24 -> W26, W30 -> W32 | 65 / 76 / 54 | 527 |
| 24-32 | W24 -> W26, W32 -> W30 | 65 / 76 / 54 | 513 |
| 26-30 | W26 -> W24, W30 -> W32 | 65 / 76 / 54 | 534 |
| 26-32 | W26 -> W24, W32 -> W30 | 65 / 76 / 54 | 533 |

The two-stage tensor identity for an old U_i -> c U_j and a
new W_i -> W_k replacement reads

    U_i (x) V_i (x) W_i
      = c U_j (x) V_i (x) W_k
        + (U_i-c U_j) (x) V_i (x) W_i
        + c U_j (x) V_i (x) (W_i-W_k).

Here (x) denotes tensor product. Both correction tensors are retained.
In all four variants the two new discarded tensors have valuation
sum exactly 10 under this one physical family. The thirteen earlier
discarded tensors also have strictly positive total valuations. Each
variant therefore has 91 exact expanded terms, 76 surviving rank-one
terms, and 15 discarded rank-one terms vanishing at the limit.

The verifier recomputes all 10,000 constant coordinates of M(4,5,5),
every nonzero Laurent coefficient and the entire discarded error
over exact rationals. No negative-degree coefficient survives. The
surviving factors are reconstructed from the pinned original integer
source rather than from numerical arrays. These are alternative
border factorizations, not smaller border-rank bounds.

## A necessary cover test passes, but no nine-cover exists

The predecessor's 56 W directions have nonnegative integer weights
totaling 152. Its complete 367,290-four-subset F_101 certificate
proves the weight cap 16 in every rank-at-most-four flat. The two
new replacements delete distinct weight-four directions. Each new
54-direction configuration has total weight exactly 144 and
inherits the cap 16. The prior U retained weight remains 214
against capacity 216. Hence both old screens pass and the stronger
W inequality reaches equality, 144=9*16. This equality is necessary
for a nine-flat cover; it is not a construction of one.

Let w35 be the unchanged third-leg direction of original term 35.
Its canonical integer vector is

    (0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0),

with weight zero. The positive-weight directions span dimension 20.
If nine rank-at-most-four spaces cover all displayed W directions,
each must contain weight 16; otherwise their combined weight is at
most 143. In particular the space F covering w35 is saturated.

A saturated F must be spanned by its positive-weight rational
directions. If their span had rank at most three, appending another
positive-weight direction outside it would create a rank-at-most-four
set of weight greater than 16, a contradiction. Therefore that span
has rank four. This makes F rationally spanned even when the proposed
cover field extends Q. Since w35 belongs to F, three other displayed
rational W directions form a basis together with w35.

The C99 certificate enumerates all C(53,3)=23,426 triples with w35
over F_101. Exactly 23,352 produce independent four-spaces. The
maximum weight of the entire resulting finite-field four-space is
15, for EACH of the four configurations. There is no saturated
four-space containing w35.

The finite-field scan is valid over any characteristic-zero extension.
Every canonical W coordinate is 0,+1,-1. Hadamard bounds put all
four-by-four integer minors at absolute value at most 16 and
five-by-five minors below 5^(5/2)<101. Thus rank-four independence
and five-vector incidence among these displayed integer directions
agree over Q and F_101. Any rational saturated F containing w35
would reduce to an enumerated four-space of weight at least 16,
contradicting the bound 15.

The nine covering spaces can therefore account for at most
8*16+15=143 of the required 144 weight. The specified termwise
Q(6,4) alignment requiring nine W four-spaces is impossible for
these four displayed W configurations, including common invertible
physical transforms and nonzero term gauges.

This does NOT exclude subsequent shared-factor flips, block
refactorizations, another physical family, new singular limits,
other grid orientations or non-termwise Q(6,4) source maps.

## Reproduce and continue

From the repository root:

    python research/ai/2026-10-23-double-leg-anchor/verify.py
    python -m unittest discover -s tests -p 'test_double_leg_anchor.py' -v

The default verifier compiles its C99 checker and exhausts the
23,426 triples in each variant. The --no-enumerate flag still
checks every Laurent tensor but does not rerun the anchored census.
The prior 56-vector flat cap is checked against its saved report;
its independent full 367,290-subset replay remains a separate command.
Same-session code audits are not independent mathematical review.

The next constructive target is a factor change that removes w35
or breaks its saturated obstruction, then an explicit nine-space
W cover, a compatible U cover and ACTUAL Q(6,4) source maps.
The four exclusions concern precisely the displayed two-stage
families and their stated physical action, not all mixed splits.
