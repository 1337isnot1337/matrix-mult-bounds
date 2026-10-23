# Source rank below 80 forces dimension at most 50

This continuation of the order-ideal package proves two necessary
bounds for the canonical cyclic A4 source over C:

- Every complex linear source space with all matrix ranks below 80
  has dimension at most 50.
- Every complete Laurent candidate for the Mat_10 tensor I_11 target
  has scalar-balanced leading long-map ranks with sum at most 144.

The first result uses the preceding lowering lemma and 35 explicit
integer minor certificates. Small coherent-block witnesses constrain
the seven nested middle layers. Only 24 size-51 order ideals remain,
and each contains a source slice with a nonzero 80-minor. The second
result follows from the credited saturated target-support inequality:
at sums 145 through 160 it needs kernel dimension at least 51, while
the new source theorem allows at most 50.

## Replay

From the repository root, using the Python standard library:

```sh
python research/ai/2026-10-23-torus-rank80/verify.py
python -m unittest discover -s tests -p 'test_torus_rank80.py' -v
```

The verifier uses the frozen certificates in
`results/torus-rank80-2026-10-23/certificates.json` and checks all
inventories independently. Its source construction, enumeration,
and elimination differ from discovery. It never accepts by rerunning
the random coefficient choices. Every minor is an integer minor;
its nonzero determinant modulo two establishes a nonzero determinant
over C. The preceding geometric reduction remains in characteristic zero.

Optional reproduction of discovery into a separate scratch file:

```sh
python research/ai/2026-10-23-torus-rank80/discover.py --output /tmp/torus-rank80-certificates.json
```

The full coverage is 4096 source terms, 256 coherent terms, 112 block
factorizations, eleven coherent minors, 24 source minors, and 12321
integer rank pairs. It excludes all 2926 pairs above sum 144, including
1096 new pairs with sums 145 through 160.

## Scope and proposed claims

- `AI-A4-RANK80-LINEAR-SPACE-001`: source rank below 80 implies source
  dimension at most 50.
- `AI-A4-BALANCED-LONG-SUM144-002`: balanced leading long-rank sum at
  most 144 for every complete Laurent candidate.

These are written claims with exact finite evidence and internal
cross-checks. No independent external mathematical review, formalization,
sharpness, target construction, or exponent improvement is claimed.
The rank-80 and sum-144 boundaries remain open. Prior files are unchanged.
