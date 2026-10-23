# Two-sided singular conjugation of A4

The [written argument](proof.md) studies all 112 slices after conjugation
by I+t^-1 N, using the existing square-zero source slice N of rank 16.
The complete limiting space acts by scalars on a fixed 12-dimensional
subspace. A constant compression to 110 coordinates can produce the full
M(10,10,11) target only if it loses at least nine leading slice directions.
This is claim `AI-A4-TWOSIDED-RANKLOSS-001`.

A completed finite census covers all 6,216 principal coordinate
compressions. Their projected leading ranks are at least 108 modulo 1009,
so they lose at most four directions and cannot supply the target.
This is computer-assisted claim `AI-A4-TWOSIDED-COORDINATE-002`.

## Evidence

The certificate contains 112 polynomial changes of slice basis, all of
their leading matrices, and the modular rank for every compression pair.
[verify.py](verify.py) rebuilds the literal six-index source, checks the
source normalization, expands every polynomial transformation completely,
checks leading independence and the 12 scalar-action columns, and
recomputes every compressed modular rank. It does not import the discovery
program or another research package.

| Projected rank modulo 1009 | Number of coordinate pairs |
| --- | ---: |
| 108 | 3 |
| 109 | 4 |
| 110 | 221 |
| 111 | 211 |
| 112 | 5,777 |

These are lower bounds on complex dimensions, which suffice for the
exclusion. Equality of complex and modular ranks is not asserted.
The proof allows arbitrary Laurent first maps, including directions
recovered after a projected leading coefficient vanishes.

From the repository root, with the standard library only:

```sh
python research/ai/2026-10-23-conjugation-limit/verify.py
python -m unittest discover -s tests -p 'test_conjugation_limit.py' -v
```

The certificate and accepted report are in
[results/conjugation-limit-2026-10-23](../../../results/conjugation-limit-2026-10-23).
To regenerate discovery independently of the retained certificate:

```sh
python research/ai/2026-10-23-conjugation-limit/discovery.py
python research/ai/2026-10-23-conjugation-limit/verify.py --certificate results/local/conjugation-limit/certificate.json
```

The eight focused tests cover the accepted certificate, literal tensor
indexing, corrupted leading coefficients, hidden later polynomial terms,
false scalar columns, omitted basis rows or coordinate pairs, incorrect
modular ranks, the need to recover lost directions, the target evaluation
formula, and source pins. Source formulas retain their prior attribution
in [sources.json](sources.json).

## Scope and next question

The result excludes this one fixed conjugation family for all principal
coordinate compressions. For arbitrary constant compressions, it gives
the necessary condition dim(PLC) <= 103. It does not exclude that remaining
determinantal locus or moving compression maps. The next constructive
experiment composes noncommuting unipotent factors and checks their full
saturated spaces against the target.

The mathematical status is written and unreviewed. No target construction,
improved exponent, independent review, or formalization is claimed.
Repository-wide validation is recorded separately before publication.
