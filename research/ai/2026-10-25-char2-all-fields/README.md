# Characteristic-two attainers over every field

For every field K of characteristic two, the three-dimensional attainers
for the complete quadratic source have equivalence classes

    (K/AS(K))_P disjoint-union {N} disjoint-union (K/AS(K))_V,
    AS(K)={z^2+z:z in K}.

The representatives are P_c, N and M_(1,c). This extends the preceding
perfect-field classification. The N integral equations force the needed
square root into K. A left binary action normalizes V over K, and explicit
stabilizers realize all Artin-Schreier shifts without square roots.

Claim `AI-CHAR2-ALL-FIELD-ATTAINERS-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) for the complete source, polynomial rank condition,
permitted actions, field descent and proof. [sources.json](sources.json)
pins the earlier contributions and frozen discovery; all prior packages
retain their evidence status.

From the repository root:

```sh
python -B research/ai/2026-10-25-char2-all-fields/verify.py
python -B -m unittest discover -s tests -p test_char2_all_fields.py -v
python -B -m unittest discover -s tests -v
python -B tools/replay.py
```

The first command reproduces [the exact report](../../../results/char2-all-fields-2026-10-25/controls.json).
It checks twenty-two source pins, N coefficient and forced-root identities,
column covariance, V section normalization, whole-family stabilizer identities,
parameter determinants and the scalar AS invariant. Nine focused tests include
mutation controls for omitted terms, wrong transpose/square/scalar conventions,
inadmissible characteristic-two denominators and damaged source pins.

Geometric rank transfer, primitive-conic parametrization and exhaustion are
written arguments. The exact identities do not computer-certify the full
classification. No new finite census, independent review, formalization,
compatible three-leg tensor map, historical priority or exponent gain is claimed.
The existing exact-five finite-field consequence is unchanged.
