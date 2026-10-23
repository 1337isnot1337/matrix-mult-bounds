# Saturated fixed flats cannot accommodate the six-split mobile factors

Claim `AI-EXTERNAL-SIX-SPLIT-MOBILE-009`: written unreviewed implication
with an exact exhaustive certificate.

The explicit six-split seed has 47 permanent third-factor directions
whose minimum cover uses exactly nine rank-at-most-four spaces. That
[positive fixed-subset cover](../2026-10-23-six-split-grid/README.md)
remains valid. This continuation proves that **no** such nine-space
cover can also accommodate all its mobile third factors, after any
finite sequence of standard shared-factor flips. The conclusion also
holds for exact minimum-term refactorizations performed separately
inside its initial components.

Consequently these continuations cannot be assigned termwise to the
Q(6,4) evaluation grid with the 25-dimensional target leg on the first
source leg, placing W on a long leg. The proof works over any
characteristic-zero extension of Q, including a Laurent field. It does
not exclude other seeds, other target-leg alignments, non-termwise
source maps, or further singular degenerations.

## Constant seed and invariant component spans

The verifier reconstructs the six replacements and constant tensor S
from the pinned external AlphaTensor factor arrays, through the preceding
[six-split package](../2026-10-23-six-split-grid/README.md#reconstruct-the-constant-seed-directly).
It does not assert that S itself equals matrix multiplication. All
external source attribution and the physical coordinate convention
remain in the [original source package](../2026-10-21-external-grid-seed/README.md).

There are 52 initial shared-factor components. On each of the three
legs, distinct component spans have zero intersection; the exact replay
checks all 3,978 pair-and-leg combinations. Each component with r terms
has middle-leg flattening rank r, because both its V_i and
U_i tensor W_i lists are independent. Hence finite standard flips stay
within the initial component spans, preserve its tensor, and cannot
create a zero term. Factor gauges have three nonzero scalar multipliers
whose product is one, so they preserve the complete tensor term.
The [component proof](../2026-10-23-fixed-flip-components/README.md#why-the-components-remain-isolated)
gives the induction over arbitrary characteristic-zero extension fields.

This leaves all 47 one-dimensional W-component directions permanently
represented. Two other components will supply the contradiction:

| Component | Its W space E | Line allowed by every saturated flat |
| --- | --- | --- |
| {8,17} | span(W_8,W_17) | Q W_8 |
| {43,58,59} | span(W_58,W_43) | Q W_58 |

Each space E has dimension two. Here all W indices refer to the original
76-term source; none of the six first-factor replacements changes W.

The entire two-dimensional W space must still be represented. Indeed,
the V_i of a component are independent and its U_i are nonzero, so the
products U_i tensor V_i are independent: apply a dual functional that
selects one V_i to any proposed relation. The W-flattening consequently
has image equal to span(W_i). The verifier checks the independence of
these products and the W rank two directly for both displayed components.
Since their tensor is preserved, its W-flattening image is preserved.
Containment in the initial W span then forces the current W factors to
span that full space.

The same statement holds for any r-term exact refactorization of an
individual component. Middle-leg flattening rank r forces its new V
factors to remain independent and every complete term to be nonzero.
Its new U tensor V factors are therefore independent as well, so the
span of its new W factors is exactly the unchanged W-flattening image.
The analogous argument gives the initial U span, and the V-flattening
already gives the initial V span. Such block refactorizations cannot
leave their three component spans or circumvent this obstruction.

## Why every space in a nine-cover must be rationally spanned

The preceding fixed-subset certificate assigns nonnegative integer
weights of total 144 to the 47 permanent directions. Every
rank-at-most-four subset has weight at most 16. If nine spaces cover
the full current W list, they cover all permanent directions too.
Subadditivity gives

\[
144\le\sum_{j=1}^{9}w(F_j\cap\mathcal P)\le9\cdot16=144,
\]

where P is the fixed projective configuration. Thus every space F_j
contains fixed directions of weight exactly 16. Call such a space
*saturated*.

There is no missing lower-rank case in the enumeration below. The
positive-weight fixed vectors span dimension 20, as checked modulo 101.
If a weight-16 fixed subset had rank at most three, some positive-weight
fixed vector would lie outside its span. Appending that vector would
give a rank-at-most-four set of weight greater than 16, contradicting
the accepted cap. Every saturated fixed subset therefore has rank four.

Now let K be any characteristic-zero extension of Q, and allow F_j to
be an arbitrary K-linear space of dimension at most four. Its contained
fixed vectors have rank four, so four of those rational vectors form
a basis for F_j over K. Consequently F_j is the extension of the
rational span of those four vectors. This proves that enumerating all
rational saturated four-flats covers every possible K-linear space in
a nine-cover. No rationality assumption is made about the moving factors
or the original proposed grid spaces.

## Exhaustive classification and exact intersection checks

The C99 program `saturated_flats.c` examines all 178,365 four-subsets
of the fixed directions. It finds 177,997 independent subsets over
F_101 and repeats the complete fixed-weight histogram and cap 16.
Every basis whose full fixed flat has weight 16 is then tested against
both mobile pairs. Deduplication gives exactly 21,649 saturated flats.
This is the full catalog; it is not restricted to a chosen cover or to
the support of a numerical optimizer.

All input coordinates are original integers in {0,1,-1}, which the
Python and C verifiers enforce. For a k-by-k minor, Hadamard's inequality
gives absolute value at most k^(k/2). In particular:

- Every four-minor has absolute value at most 16, below 101.
- Every five-minor has absolute value at most 5^(5/2), below 101.
- Every minor of size at most six has absolute value at most 216,
  below the prime 1009.

The first bound makes rational and F_101 independence agree for every
four-subset. The second makes F_101 membership in each resulting
four-flat agree with rational membership for every fixed vector. Thus
there are no modular collisions or omitted rational flats. Two equal
fixed-membership masks describe the same rational flat, since the mask
contains a four-vector basis. Deduplication by the mask is exact.

For each saturated basis B, set (x,y) = (W_8,W_17) or (W_58,W_43).
The program checks

\[
\operatorname{rank}(B,x,y)=\operatorname{rank}(B,x)+1.
\]

These are ranks of at most six **original** rows, whose entries are
still in {0,1,-1}. The third bound makes their ranks over F_1009 exactly
their rational ranks. Row operations occur only after the bounded
integer matrix has been specified. The retained output records zero
failures for both pairs. All ranks remain the same on extending to K.

The rank increment says y is outside span(B,x). Hence any ax+by in
span(B) must have b=0. Equivalently,

\[
F\cap\operatorname{span}_K(x,y)\subseteq Kx
\quad\text{for every saturated flat }F.
\]

Exactly 25 distinct saturated flats meet the first mobile W space
nontrivially; exactly 26 meet the second. Their intersections are on
the respective allowed lines. Python separately checks a rational
equality witness for each line. The accepted proof does not depend on
the exploratory numerical optimization or on symbolic nullspace output.

## Contradiction and physical Laurent transfer

Every putative nine-cover consists of saturated spaces. All current W
factors from component {8,17} would therefore lie on the single line
K W_8, contradicting its preserved two-dimensional W-flattening image.
The component {43,58,59} gives a second, independent contradiction with
the line K W_58. Either component suffices to exclude the full W cover.

The physical maps U -> R^(-1) U S, V -> S^(-1) V T,
W -> T^(-1) W R are common invertible maps on the factor spaces over K.
They preserve ranks, intersections, and component flattening images.
They also conjugate standard shared-factor flips to standard flips.
Apply their inverse to a proposed cover of the physical Laurent family
to obtain the constant-coordinate setting used above. Thus the proof
applies to the full retained Laurent family and its finite continuations.
It does not treat singular specialization or taking leading coefficients
as an invertible change.

The Q(6,4) evaluation grid supplies only nine spaces of dimension at
most four on either long leg. This obstruction therefore excludes the
specified termwise alignment. It makes no claim about a general
Q(6,4) degeneration or other split seeds.

## Reproduction and construction targets

From the repository root:

```sh
python research/ai/2026-10-23-six-split-mobile-obstruction/verify.py
python research/ai/2026-10-23-six-split-mobile-obstruction/verify.py --enumerate
python -m unittest discover -s tests -p 'test_six_split_mobile_obstruction.py' -v
```

The quick command checks the pinned source, component geometry,
positive-weight span, both W-flattenings, bounded-entry hypotheses,
stored counters, and rational equality witnesses. It explicitly reports
that enumeration has not been rerun. The full command compiles the C99
program in a temporary directory and repeats every four-subset and all
saturated-basis intersection checks. It compares the complete output
with `enumeration.json`. `certificate.json` records that completed replay.
The focused tests run the exhaustive replay when a C99 compiler exists;
only that compiler-dependent test is otherwise skipped.

This result gives concrete next construction targets: change the
permanent direction set, or alter or connect the components {8,17} and
{43,58,59} so their present span constraints no longer apply. It does
not invalidate the exact nine-cover of the 47 fixed directions. That
cover is a useful partial witness, while full grid compatibility has
now been ruled out for the stated continuation class of this seed.

The reasoning and finite certificates are AI-derived work from the same
research session. Evidence status remains written and unreviewed, with
no formalization, general rank lower bound, or exponent improvement.
