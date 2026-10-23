# The canonical candidate passes every B-leg Koszul degree

Date: 2026-10-23. Exact finite coefficient calculations, with a separate
written source-rank formula for the all-degree conclusion. No degeneration
is constructed.

The source is `10 Full(5,10)`. The canonical target is

`7 Full(5,2) + 10 Full(5,3) + 4 SharedOutput(3,3) + 2 SharedOutput(4,2) + 6 Mid(5,2)`.

Both endpoints have format `(5,100,140)`. The literal coefficient conventions
are in the package's discovery record and are independently reconstructed in
`verify_higher.py`. All first coefficient bases in this calculation are the
canonical shared basis. Independent target first identifications can change
these higher ranks and are not enumerated here.

## 1. Rank values

For the map

\[
K_B^p:C^*\otimes\Lambda^pB\longrightarrow A\otimes\Lambda^{p+1}B,
\]

the exact comparisons are:

| Degree | Source rank | Target rank | Source minus target |
| --- | ---: | ---: | ---: |
| 0 | 140 | 140 | 0 |
| 1 | 12735 | 12587 | 148 |
| 2 | 573540 | 559238 | 14302 |
| 3 | 17050935 | 16315992 | 734943 |

The source ranks are given by the separately written common-input formula

\[
\operatorname{rank}K_B^p(S)
=5\binom{100}{p+1}-\max(4-p,0)\binom{90}{p+1}.
\tag{1}
\]

Literal source coefficient calculations at degrees one and two independently
agree with (1). The degree-three source value in the report is evaluated from
(1). For every `p>=4`, the subtraction vanishes, so the source already has
the maximum row rank `5*binom(100,p+1)`. No target of the same format can
exceed it. Together with the ordinary degree-zero flattening and the three
comparisons above, the canonical candidate passes every B-leg degree.

This passing result is a necessary-test outcome. It does not supply maps,
establish a degeneration, or improve an exponent.

## 2. Decomposition by exterior occupancy

Let `B=direct_sum B_i` and `C=direct_sum C_i` be the nonshared block spaces.
For each tuple of nonnegative occupancies `alpha_i` with sum `p+1`, the
codomain has a direct summand

\[
A\otimes\bigotimes_i\Lambda^{\alpha_i}B_i.
\]

Its corresponding domain is the direct sum over indices with `alpha_i>0` of

\[
C_i^*\otimes\Lambda^{\alpha_i-1}B_i
\otimes\bigotimes_{j\ne i}\Lambda^{\alpha_j}B_j.
\tag{2}
\]

The Koszul map preserves this grouping, so ranks add. Degree two uses only
the positive occupancy patterns `(3)`, `(2,1)`, `(1,1,1)`. Degree three uses
`(4)`, `(3,1)`, `(2,2)`, `(2,1,1)`, `(1,1,1,1)`.

The verifier groups equal block types and records each multiplicity. For an
ordered pattern with equal occupancies sorted by block type, the multiplicity
is the product of falling factorials selecting the distinct physical blocks,
divided by factorials for repeated equal `(type,occupancy)` pairs. The tests
check that the weighted domain and codomain dimensions exhaust the full
Koszul matrix in every recorded degree.

## 3. The canonical coefficient grading

Every tensor term has total weight zero with common first weight `i` and
the following nonshared weights:

| Block | B weight | C weight | Coefficient rule |
| --- | --- | --- | --- |
| Full | `j` | `-k` | `k=i+j` |
| Mid | `-j` | `k` | `j=i+k` |
| Shared output | `-j` | `-k` | `i=j+k` |

A domain vector in (2) has weight minus the selected C-coordinate weight
plus the weights of the wedged B coordinates. Its image has weight `i`
plus the weights of all output wedge coordinates. These are equal term by
term. Each occupancy map therefore splits further into integer-weight blocks.

The target calculations use 20 occupancy types and 198 grade matrices at
degree one, 64 types and 766 grade matrices at degree two, and 184 types
and 2537 grade matrices at degree three. These are complete decompositions
of the fixed canonical coefficient maps, not a parameter sample.

## 4. Exact acceptance and independent controls

All retained ranks use standard-library primitive integer row elimination.
Replacing a row by a nonzero multiple and subtracting another row preserves
its rational span; dividing a row by its integer content also preserves that
span. The number of nonzero pivot rows is the exact rank over the rationals,
hence over the complex numbers. No floating-point rank threshold is used.

Seven small unsplit Koszul matrices are built separately from their complete
literal tensors, without occupancy or weight grouping. An independent
`Fraction`-based elimination checks their ranks against the grouped calculation.
The examples include Full/shared-output and shared-output/Mid interactions
and both degrees two and three. These controls test exterior signs, grouping,
and the integer elimination path.

Run from the repository root:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_higher.py \
  --output results/mixed-longlegs-candidate-2026-10-23/higher_verification.json
python -m unittest discover -s tests -p test_mixed_longlegs_higher.py -v
```

The source formula is a written geometric argument supplied in the same
research session, not a consequence of these finite controls. The finite
report supplies no independent mathematical review or formalization.
