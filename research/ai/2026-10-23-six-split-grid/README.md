# The six-split seed's fixed directions need exactly nine groups

Claim `AI-EXTERNAL-SIX-SPLIT-FIXED-COVER-007`: written unreviewed
implication with exact finite certificates.

The 47 permanent third-factor directions of the explicit six-split seed
below can be covered by nine rational subspaces of dimension four.
They cannot be covered by eight subspaces of dimension at most four,
even over a characteristic-zero extension field. Their exact minimum
number of such groups is therefore nine.

This is a positive construction checkpoint. The previous four-split and
five-split seeds had 50 permanent directions that needed at least ten
groups. The six-split seed reaches the nine-group requirement for its
permanent subset. The certificate does **not** cover the remaining
mobile third factors, give simultaneous covers on both long legs, or
construct source maps from Q(6,4). It gives no new exponent or matrix
multiplication algorithm.

## Reconstruct the constant seed directly

Use the original 76 integer factor triples U_i, V_i, W_i from
[`../2026-10-21-external-grid-seed/factors.json`](../2026-10-21-external-grid-seed/factors.json).
Their source package records the external AlphaTensor attribution to
Fawzi et al., Nature (2022), the Lille catalogue, Perminov's conversion,
the source hashes, and the physical matrix convention. The arrays have
shapes 76-by-20, 76-by-25, and 76-by-20.

Retain every second and third factor. Make these six first-factor
replacements, using the original right-hand sides and zero-based indices:

\[
\begin{aligned}
U_0&\leftarrow-U_{18},&U_{17}&\leftarrow U_8,&
U_{48}&\leftarrow-U_2,\\
U_{56}&\leftarrow-U_{22},&U_{43}&\leftarrow-U_{59},&
U_{47}&\leftarrow U_{73}.
\end{aligned}
\]

The verifier reconstructs the resulting constant tensor directly from
the byte-pinned original data. It needs no temporary discovery file or
external six-split certificate. It does not assert that this constant
tensor equals matrix multiplication. The finite geometry result also
holds for its common invertible physical transforms over a Laurent
field, since those preserve all factor incidences.

## Which directions are permanent

Join term indices when their factors are proportional on at least one
leg. The six-split seed has 52 initial connected components: 35 singletons,
13 pairs, two triples, one component of size four, and one of size five.
The exact replay checks all 3,978 pairs of components and choices of leg.
For each such pair, the two factor spans have zero intersection. Within
every component, both the middle factors V_i and the products
Z_i = U_i tensor W_i are linearly independent.

These are the hypotheses of the
[component-containment proof](../2026-10-23-fixed-flip-components/README.md#why-the-components-remain-isolated).
A component with r terms has middle-leg flattening rank r, so a finite
exact sequence of standard shared-factor flips cannot produce a zero
term there. Nonzero factors in distinct component spans cannot become
proportional. Consequently all flips stay inside the initial component
spans. The allowed factor gauges multiply the three factors by nonzero
scalars whose product is one, preserving the full tensor term.

Exactly 47 components have third-factor span of dimension one. Their
directions therefore remain present after every finite such flip sequence.
The verifier selects rational span bases from the original integer rows
and proves their required independence by nonzero minors modulo 101.
The same minors remain nonzero over every characteristic-zero extension.
The 47 fixed directions are distinct and span dimension 20.

The five mobile components are {0,18,25}, {2,47,48,55,73}, {8,17},
{22,29,56,75}, and {43,58,59}. Their third-leg dimensions are 2, 3, 2,
2, and 2. This package does not assign their changing third factors to
the nine spaces below.

## An explicit rational cover

Order the fixed components by least term index. Represent each direction
by that first term's W factor, normalized to a primitive integer vector
with positive first nonzero entry. `cover.json` records this full ordering
and uses indices in the resulting list of 47 directions.

The following equivalent table gives each group using representative
indices in the **original 76-term list**. Every displayed group has
rational rank exactly four, and the union covers all 47 fixed directions.
Repeated directions between groups have zero certificate weight.

| Group | Original term representatives |
| ---: | --- |
| 1 | 27, 28, 30, 32, 33, 35 |
| 2 | 23, 24, 26, 35, 36, 38 |
| 3 | 19, 20, 21, 31, 38, 40 |
| 4 | 1, 6, 16, 44, 54 |
| 5 | 3, 4, 5, 46, 49, 51, 60 |
| 6 | 10, 13, 50, 64, 70 |
| 7 | 11, 61, 65, 67, 69, 71 |
| 8 | 7, 9, 12, 14 |
| 9 | 15, 42, 45, 66 |

Taking the rational span of each row proves the upper bound of nine.
The verifier checks both rank and complete coverage by exact arithmetic.
No mixed-integer optimizer result is needed to accept this witness.

## A matching lower bound

Assign the 47 nonnegative integer weights retained in `cover.json` and
`verify.py`. Their total is 144. The C99 replay examines all
C(47,4) = 178,365 four-subsets over F_101. Of these, 177,997 are
independent. Every resulting rank-four span contains fixed directions
of total weight at most 16. The complete output is retained in
`enumeration.json`; an equality witness is also checked over Q.

Because the full finite-field span has dimension 20, each span of a
smaller subset extends to an enumerated rank-four span. Nonnegative
weights preserve the bound under inclusion. If a subset has rank at
most four over any characteristic-zero extension of Q, all its
five-minors vanish as integers. They also vanish modulo 101, so the
same weight cap applies. Common invertible transformations and nonzero
factor gauges preserve this incidence statement.

The weight of a union is at most the sum of the group weights. Any
cover therefore needs at least ceil(144/16) = 9 groups. Each group in
the displayed rational cover has weight 16, attaining the bound.

The weights and cover were discovered by numerical linear and
mixed-integer optimization. Acceptance uses only these explicit
integers, the rational rank and coverage checks, and the exhaustive
finite-field enumeration. Neither SciPy nor SymPy is required for replay.

## Reproduction and scope

From the repository root:

```sh
python research/ai/2026-10-23-six-split-grid/verify.py
python research/ai/2026-10-23-six-split-grid/verify.py --enumerate
python -m unittest discover -s tests -p 'test_six_split_grid.py' -v
```

The quick verifier checks the pinned source, all component-containment
hypotheses, the exact nine-group cover, and the stored enumeration
counters and rational equality witness. It explicitly reports that it
has not rerun all four-subsets. The full command compiles the preceding
weighted package's C99 program in a temporary directory, repeats all
178,365 subsets, and compares the complete output with the retained run.
`certificate.json` records that completed replay. The focused tests
also perform the full enumeration when a C99 compiler is available;
only that compiler-dependent test is otherwise skipped.

The Q(6,4) application concerns a termwise evaluation-grid assignment
with the 25-dimensional target leg on the first source leg, placing W
on a long leg. This fixed subset now satisfies its nine-group necessary
condition. Completing the construction would require fitting the mobile
factors, satisfying the other long-leg conditions, and constructing the
compatible source maps. None of those steps follows from this cover.
The statement is over the full generic characteristic-zero family;
arbitrary singular specialization can change incidences.

This package contains same-session AI-derived reasoning and exact finite
certificates. Its written-proof status remains unreviewed.
