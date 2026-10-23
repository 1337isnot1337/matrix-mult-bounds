# Complete full-space Koszul atlas for the fixed oblique residual

October 23, 2026. Owner-directed Codex research. Claim
`EXP-OBLIQUE-KOSZUL-ATLAS-001` is a finite exact experiment, without
independent mathematical review or formalization.

For the actual product-oblique residual `E_(6,4)` in concise format
`9 x 11 x 11`, **no full-space Koszul flattening improves the existing
border-rank lower bound of twelve**. Every degree on each of the three
legs gives a bound at most eleven. This closes that finite screening
route for these fixed maps. The border-rank interval remains `[12,18]`;
the ordinary rank remains nineteen.

The [construction and adapted residual](../2026-10-23-oblique-border-repair/full_residual_rank.md)
and the [equalizer bound](../2026-10-23-oblique-border-equalizer/proof.md)
are inherited from pending PR147, pinned at
`29a486ac622261c8b4854fc109fb8ab40dcf91a2`. That work already gave
the first-leg middle-degree analytic ceiling 504. Here its exact rank
is 503; the new finite computation covers every degree and every leg.
No new construction, general lower bound, historical priority, or
matrix multiplication exponent improvement is claimed.

## Exact n6 ranks

On the first leg, the degree is `p=0,...,8`:

| p | Matrix rank | Rank-one divisor | Rounded border lower bound |
| --- | ---: | ---: | ---: |
| 0 | 11 | 1 | 11 |
| 1 | 74 | 8 | 10 |
| 2 | 226 | 28 | 9 |
| 3 | 414 | 56 | 8 |
| 4 | 503 | 70 | 8 |
| 5 | 414 | 56 | 8 |
| 6 | 226 | 28 | 9 |
| 7 | 74 | 8 | 10 |
| 8 | 11 | 1 | 11 |

Both long legs independently give the following ranks:

| p | Matrix rank | Rank-one divisor | Rounded border lower bound |
| --- | ---: | ---: | ---: |
| 0 | 9 | 1 | 9 |
| 1 | 99 | 10 | 10 |
| 2 | 471 | 45 | 11 |
| 3 | 1284 | 120 | 11 |
| 4 | 2248 | 210 | 11 |
| 5 | 2675 | 252 | 11 |
| 6 | 2214 | 210 | 11 |
| 7 | 1266 | 120 | 11 |
| 8 | 479 | 45 | 11 |
| 9 | 108 | 10 | 11 |
| 10 | 11 | 1 | 11 |

The [certificate](certificate.json) also contains complete controls at
`b=2,3`, for the one-dependency family `n=b+2`. The strongest bounds at
`b=2,3,4` are respectively `8,9,11`, compared with the inherited
equalizer bounds `8,10,12`. These are three finite sizes, not an
all-size rank formula.

## Definition, orientation and acceptance

Use the standard [Koszul definition and rank-one calculation](../2026-10-20-koszul/research_note.md#1-definition-and-the-degeneration-test).
For a wedge leg `X` of dimension `d`, the map is

```text
K_p(T): Lambda^p(X) tensor Y* -> Lambda^(p+1)(X) tensor Z.
```

A simple tensor has map rank `binom(d-1,p)`: wedging by a nonzero
vector has exactly that rank, while its other two factors contribute
a rank-one map. Subadditivity bounds this matrix rank for ordinary
tensor decompositions. Polynomial minors then give the same bound
for geometric border rank over an algebraic closure and for formal
degenerations in every characteristic.

The verifier contracts the first remaining leg in increasing index
order. This covers the other contraction choice as well: the perfect
exterior pairing identifies its degree `p` map with the transpose of
the recorded degree `d-1-p` map, up to invertible signed basis changes.
The rank-one divisors agree. Since every degree is present, no leg
orientation is omitted. Padding the wedge leg cannot improve the
maximum ratio: exterior decomposition makes the padded rank a
binomial-weighted sum of the unpadded ranks, and Vandermonde's
identity gives the same weighted sum of their divisors. Padding the
other legs only adds zero rows or columns.

Acceptance reconstructs all **75 matrices**, including zero-row and
zero-column dimensions, from exact residual coefficients. Integer
Gaussian elimination accepts only pivots `+1` or `-1`. Row additions
and sign changes are invertible over every field. Distinct pivot
columns give a triangular unit minor, while every remaining row
reduces to zero. Thus each decision supplies both a lower and an
upper matrix-rank bound, uniformly in characteristic. A nonunit
pivot aborts; reduction modulo one prime is not used as an upper
bound. Pivot hashes bind the deterministic reduction to each saved
record. They are consistency checks; the full row reduction is rerun
and is the rank evidence.

Five [source pins](sources.json) retain the original coefficient
convention and prior credit. Acceptance also calls the pinned native
source replay: it contracts all 576 `Q(6,4)` terms and compares all
10,000 target coordinates with the adapted full residual. The
historical archives and prior construction are unchanged.

## Reproduce and limits

From the repository root:

```sh
python -S research/ai/2026-10-23-oblique-koszul-atlas/verify.py
python -m unittest discover -s tests -p test_oblique_koszul_atlas.py -v
```

The CLI uses only the Python standard library; the independent small
matrix test uses the maintained SymPy dependency. Broader repository
regression, archive replay and final-head hosted CI are separate merge
gates and must be recorded before integration.

This does not exhaust Koszul maps after arbitrary projections, other
Young flattenings, nonlinear equations for secant varieties, different
source maps or general degeneration families. The complete matrix
rank decisions are finite exact results; they do not settle optimal
border rank. See the original [question](QUESTION.md).
