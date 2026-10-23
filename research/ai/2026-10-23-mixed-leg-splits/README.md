# Mixed U/W splits and a new static cover obstruction

**Claim:** `AI-EXTERNAL-MIXED-LEG-SPLIT-SEED-011`

**Status:** written-unreviewed

**Field:** the rationals and characteristic-zero extensions

This package gives an exact 76-term border decomposition of `M(4,5,5)`
after eleven U-factor replacements and two W-factor replacements. It passes
both weighted tests retained from the original configuration. A new exact
weight assignment nevertheless excludes a nine-space cover of its current
W directions. These are compatible conclusions: each weight assignment
gives one necessary inequality, and passing one does not construct a cover.

| Quantity | Exact result |
| --- | ---: |
| U replacements / W replacements | 11 / 2 |
| Expanded exact terms / surviving border terms | 89 / 76 |
| Distinct U / V / W projective directions | 65 / 76 / 56 |
| Nonzero constant coefficients / constant positions checked | 100 / 10,000 |
| Nonzero coefficients at negative Laurent degrees | 0 |
| Nonzero coefficients at positive Laurent degrees | 506 |
| Retained old U weight / nine-group capacity | 214 / 216 |
| Retained old W weight / nine-group capacity | 141 / 144 |
| New W weight / nine-group capacity | 152 / 144 |

The positive construction changes the factors available for further work.
It retains 76 terms and gives no improvement in rank, border rank, or the
matrix multiplication exponent. The negative result concerns the displayed
W configuration and common invertible images of it. It does not establish
an obstruction after arbitrary flips, refactorizations, new splits, or
singular limits. No complete `Q(6,4)` source map is constructed or excluded.

## The simultaneous mixed split

Start from the externally attributed integer algorithm in
[`factors.json`](../2026-10-21-external-grid-seed/factors.json), with SHA256
`bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3`.
It gives

\[
M=\sum_{i=0}^{75}U_i\otimes V_i\otimes W_i,
\qquad U_i\in\mathbb Q^{4\times5},\quad
V_i\in\mathbb Q^{5\times5},\quad W_i\in\mathbb Q^{5\times4}.
\]

For a U replacement `(i,j,c)`, use the exact identity

\[
U_i\otimes V_i\otimes W_i
=cU_j\otimes V_i\otimes W_i
 +(U_i-cU_j)\otimes V_i\otimes W_i.
\]

For a W replacement, use

\[
U_i\otimes V_i\otimes W_i
=U_i\otimes V_i\otimes cW_j
 +U_i\otimes V_i\otimes(W_i-cW_j).
\]

Every factor on the right is read from the original source. All 13 changed
term indices are distinct, so these identities add without cross terms.
Let `S` be the resulting 76-term tensor, and let `D` be the sum of the 13
differences. Then `M=S+D` exactly.

All indices below are zero-based. Factor minima refer to the common physical
action defined in the next section.

| Leg | Changed i | Destination j | c | Minimum factor valuations | Tensor valuation |
| --- | ---: | ---: | ---: | --- | ---: |
| U | 16 | 3 | -1 | `(0,-19,22)` | 3 |
| U | 24 | 12 | -1 | `(3,-3,3)` | 3 |
| U | 26 | 13 | -1 | `(0,0,3)` | 3 |
| U | 30 | 12 | 1 | `(3,-3,3)` | 3 |
| U | 32 | 13 | -1 | `(0,0,3)` | 3 |
| U | 51 | 64 | -1 | `(-22,-35,60)` | 3 |
| U | 52 | 47 | -1 | `(3,-35,60)` | 28 |
| U | 55 | 1 | -1 | `(-54,-16,73)` | 3 |
| U | 60 | 54 | -1 | `(6,-22,22)` | 6 |
| U | 63 | 34 | -1 | `(-3,-16,22)` | 3 |
| U | 73 | 47 | 1 | `(-16,-35,73)` | 22 |
| W | 12 | 8 | -1 | `(0,3,0)` | 3 |
| W | 13 | 8 | -1 | `(-3,6,0)` | 3 |

Terms 12 and 13 supply U destinations while their own W factors change.
Their U factors remain unchanged. A rule forbidding every destination index
from appearing anywhere among changed terms would incorrectly reject this
valid mixed construction. The maintained splitter instead reads original
factors and enforces one changed leg per source term. The exact full tensor
identity is also checked independently.

## One common physical family

Use the three basis matrices from the retained
[`five_split_certificate.json`](../2026-10-23-flip-escape/five_split_certificate.json),
SHA256 `12cedfc73b6de98bb302b93941c05027b8acc41df03e4606b99363cb323e1c91`.
Their determinants are `(1,1,-1)`. The new integer weights are

\[
r=(0,3,22,60),\qquad s=(0,6,22,22,3),\qquad t=(0,0,-13,-13,6).
\]

For bases `B_R,B_P,B_T`, define

\[
R(\epsilon)=B_R\operatorname{diag}(\epsilon^{r_a}),\quad
P(\epsilon)=B_P\operatorname{diag}(\epsilon^{s_b}),\quad
T(\epsilon)=B_T\operatorname{diag}(\epsilon^{t_c}).
\]

The physical action is

\[
\Phi_\epsilon(U,V,W)
=(R^{-1}UP,\ P^{-1}VT,\ T^{-1}WR).
\]

Adjacent physical matrices cancel in the elementary-matrix expression for
`M`, so this action fixes `M`. Consequently

\[
\Phi_\epsilon(S)=M-\Phi_\epsilon(D).
\]

For a nonzero Laurent vector, its valuation is its smallest nonzero
coordinate exponent. A rank-one tensor product has valuation equal to the
sum of the factor valuations: choosing a minimum coordinate in each factor
gives a nonzero product at that summed exponent.

Every discarded term in the table has positive total valuation. Therefore
each term of `Phi_epsilon(D)` tends to zero, as does their finite sum. This
proves

\[
\lim_{\epsilon\to0}\Phi_\epsilon(S)=M.
\]

Individual factors can have poles. The assertion concerns their tensor
products, whose positive valuations are proved exactly. The 76-term
surviving tensor is generally different from `M` at nonzero parameter.
The complete expanded identity includes all 13 discarded terms.

### Product-preserving factor gauges

A factor gauge multiplies the three factors of a term by nonzero scalars
whose product is one, preserving the tensor term exactly. After
`epsilon=z^3`, a discarded term with factor minima `(a,b,c)` can use powers
of `z` with exponents

\[
(1-3a,\ 1-3b,\ 3a+3b-2).
\]

These exponents sum to zero. The new minima are
`(1,1,3(a+b+c)-2)`, all strictly positive. The certificate saves these
gauges; tests also contract the gauged factors and check that the entire
discarded tensor equals the original one after ramification.

## The earlier weight assignments both pass

The previous
[`grid-escape` certificate](../2026-10-23-grid-escape/README.md)
assigns total weight 251 to the 76 original U directions, with weight at
most 24 on every rank-at-most-four subset. Nine groups have capacity 216.
The eleven changed U directions remove weight 37, leaving 214.

That certificate assigns total weight 149 to the 58 original W directions,
with cap 16 per rank-at-most-four subset. The two W replacements remove the
singleton directions of terms 12 and 13, each of weight four. They both use
the retained direction of term 8. The remaining weight is therefore 141,
below the nine-group capacity 144.

The verifier computes these values from the actual surviving direction sets
and the pinned prior weight assignments. Neither inequality is sufficient
for a cover. Their passage explains why this witness warranted a fresh
geometric screen.

## A stronger exact obstruction for the current W directions

Normalize each surviving W factor by its first nonzero coordinate, and keep
one vector per projective direction in order of first occurrence among the
76 terms. The result has 56 integer vectors with entries in `{-1,0,1}`.
`w_obstruction.json` saves those vectors, their term classes, and a new
weight in `{0,1,2,3,4}` for each direction. The total new weight is 152.

The retained exact C99 enumerator checks all

\[
\binom{56}{4}=367290
\]

four-subsets modulo 101. Of these, 366288 are independent. For each
independent subset, it tests all 56 vectors for membership in its span and
sums their weights. The largest sum is 16. The stored histograms count
bases, so a flat with several bases appears several times. They are not
counts of distinct flats.

The verifier checks a rational rank-four equality witness separately. Its
class indices are `(0,1,2,46,49,54)`, and their weights sum to 16. The entire
configuration has rank 20 modulo 101. Therefore any subset of reduced rank
at most four extends to one of the enumerated independent four-subsets.
Nonnegative weights make the same cap valid for all smaller spans.

If a set of these integer vectors has rank at most four over a
characteristic-zero extension, all of its five-minors vanish as integers.
They still vanish modulo 101. The reduced set thus has rank at most four,
so the exhaustive bound gives it weight at most 16. This proves the cap
over the rationals, the complex numbers, and characteristic-zero Laurent
fields. Common invertible linear images and nonzero scalar rescalings
preserve these rank conditions.

Any cover of the 56 directions by nine spaces of dimension at most four
would satisfy

\[
152\le 9\cdot16=144,
\]

which is impossible. The weight bound therefore requires at least ten
groups. In the specified termwise `Q(6,4)` evaluation-grid assignment, each
long leg must fit into nine rank-at-most-four groups, as proved in the
[original seed package](../2026-10-21-external-grid-seed/README.md).
The displayed seed fails that necessary condition on W.

The obstruction also applies after a common invertible physical action,
including over a Laurent field, and after product-one factor gauges. It
does not establish that the same W directions persist under later flips or
refactorizations. Singular limits can change the direction configuration
and are outside this static statement.

### A further necessary inequality for replacement searches

Extend the new weights to all 58 original W directions by giving weight
zero to the omitted directions of terms 12 and 13. Every rank-at-most-four
subset of the enlarged set still has weight at most 16: its positive-weight
part is a subset of the configuration just certified. The total is still
152. Any future seed whose W directions are a subset of the original 58
must remove at least eight units of this new assignment to satisfy the
nine-group inequality. The present two W replacements remove zero units of
the new assignment. This is a reusable necessary screen, not a sufficiency
test or an exclusion of replacements using new directions.

## Discovery, replay, and scope

Discovery considered mixed U and W replacements in fixed physical bases.
A bounded numerical mixed-integer run of about 55 seconds first found a
13-split candidate removing old U weight 34 and old W weight 12. Small
rational integer weights and a subsequent binary selection at those fixed
weights produced the accepted eleven-U/two-W batch, removing weights 37
and 8. The retained fixed-weight run used the weight bound 60 and 1225
pairwise support-cycle cuts. Its solver status is recorded as discovery
provenance only; it is not a mathematical optimum or completeness claim.
The rationalized intermediate record inherited valuation fields from the
earlier numerical run; its added notice identifies those unrecomputed
values. The accepted certificate and final fixed-weight record contain the
recomputed exact minima.
Numerical optimization also suggested the new W weights. Exact arithmetic
is the acceptance criterion in both parts.

`certificate.json` contains every surviving and discarded Laurent factor.
The standard-library verifier byte-checks the original factors, physical
bases, and prior weighted sources. It reconstructs the mixed split,
contracts every Laurent coefficient, checks all 10,000 constant positions,
checks the full remainder identity and gauges, and counts all three sets of
projective directions. No scratch file or numerical solver is needed.

The quick command validates the stored W report and exact witnesses. The
complete command also repeats all four-subsets, using a C99 compiler:

```sh
python research/ai/2026-10-23-mixed-leg-splits/verify.py
python research/ai/2026-10-23-mixed-leg-splits/verify.py --enumerate
python -m unittest tests.test_mixed_leg_split_seed -v
```

The report explicitly says whether exhaustive enumeration was rerun.
The C calculation uses residues from 0 through 100. Products are at most
10000 and four-term membership sums at most 40000. The enumeration counters
are below 2^32, so ordinary conforming 32-bit-or-larger integer types
suffice for this registered input.

Focused tests cover the full replay and regeneration, mixed destination
bookkeeping, exact gauge preservation, source/scope and coefficient
corruption, an independent dense nonzero-parameter identity, and the
complete W enumeration when a C99 compiler is available. Passing tests
does not change the written-unreviewed mathematical status.

## Attribution

The external integer rank-76 algorithm retains the AlphaTensor credit to
Fawzi and collaborators, Nature (2022), through the pinned conversion in
the source package. Its existing conversion license notice is unchanged.
The physical bases and earlier weighted screens are prior local work.
The simultaneous mixed batch, new physical weights, complete coefficient
replay, and new W weight certificate are owner-directed AI continuation.

The physical-stabilizer deletion viewpoint is discussed in Dumitriu et al.,
*Fast and Stable Arbitrary Precision Approximate Matrix Multiplication*,
[arXiv:2610.13905v1](https://arxiv.org/html/2610.13905v1), Theorems 2.1 and 2.2
and Section 2.3. The specific split, valuation, gauge, and weighted-cover
arguments used here are proved directly above. Source versions and pins
are retained in `sources.json`. No historical priority, independent
mathematical review, formalization, or exponent improvement is asserted.
