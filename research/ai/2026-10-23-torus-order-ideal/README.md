# Order ideals and the sharp A4 dimension bound below rank 64

This package proves a new necessary frontier for the canonical A4
source over C. Every complex linear source space with all slice ranks
below 64 has dimension at most 32, and dimension 32 is attained.
Consequently every scalar-balanced complete Laurent candidate for
the Mat_10 tensor I_11 target has leading long-map ranks whose sum is
at most 160.

The source theorem combines a written geometric reduction with exact
finite certificates. Three explicitly verified lowering operators
reduce any bounded-rank space to a coordinate order ideal. The middle
rank-64 monomials restrict that ideal to a 4-by-3-by-4 box. There are
611 ideals of size 33 in this box, and each saved witness has an odd
integer 64-by-64 minor. The 32-dimensional coordinate plane supported
at middle positions zero and one supplies sharpness.

## Files and verification

- `proof.md` proves the reusable lowering lemma, the source dimension
  theorem, and the balanced rank-sum consequence.
- `discover.py` finds candidate integer minors using a deterministic
  sequence of binary coefficient choices.
- `verify.py` independently enumerates the ideal inventory, rebuilds
  the literal source, and replays the saved minors.
- `sources.json` pins the credited source formula and earlier results.
- `results/torus-order-ideal-2026-10-23/certificates.json` stores all
  611 witnesses as source, row, and column masks.
- `results/torus-order-ideal-2026-10-23/controls.json` records the exact
  replay totals and the claim scope.

From the repository root, using only the Python standard library:

```sh
python research/ai/2026-10-23-torus-order-ideal/verify.py
python -m unittest discover -s tests -p 'test_torus_order_ideal.py' -v
```

To reproduce discovery into a separate scratch artifact:

```sh
python research/ai/2026-10-23-torus-order-ideal/discover.py --output /tmp/torus-order-ideal-certificates.json
```

Discovery is not an acceptance step. Replay uses the frozen integer
witnesses, a different source reconstruction, a different enumeration,
and a different elimination routine. An odd integer determinant gives
a nonzero complex minor. The geometric reduction itself is over C;
it is not inferred from a characteristic-two calculation.

## Coverage and claims

The exact controls cover 4096 literal terms, 12544 matrix positions,
112 monomial slices, 336 infinitesimal identities, all 611 ideals and
their 64-minors, the sharp 32-plane, and all 12321 integer rank pairs.
They exclude 1830 pairs above sum 160, including 840 new pairs in the
interval 161 through 176.

Proposed claim IDs:

- `AI-A4-RANK64-LINEAR-SPACE-001`: source rank below 64 forces source
  dimension at most 32, sharply.
- `AI-A4-BALANCED-LONG-SUM160-002`: every scalar-balanced complete
  Laurent candidate has leading long-rank sum at most 160.

Both are written claims with exact finite evidence. Internal agent
cross-checks are recorded in the proof; independent external review
and formalization are not claimed. The source dimension theorem is
sharp, but the long-rank sum bound is only necessary. This package
does not construct the target or improve the matrix multiplication
exponent. It leaves the strict rank-64 boundary open.
