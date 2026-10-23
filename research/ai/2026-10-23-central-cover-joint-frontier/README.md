# A finite cube closes the one-matrix-plus-scalars coordinate family

The exact SL(2,F5) source cube has a characteristic-two slice cover of
1012332. For a target M(a,b,c) plus r scalar tensors, cyclic tensoring and
finite slice-rank additivity require

    (abc)^2 + 3r*abc*min(a,b,c) + 3r^2*min(ab,bc,ca) + r^3 <= 1012332.

Combining this with the adopted complex rank-locus and full Koszul tests
excludes every strictly improving member of the complete one-copy family
M(a,b,c) plus r scalars in the maintained coefficient-one coordinate/
potential class over C. This is a scoped construction-class exclusion.
No smaller exponent or exclusion of arbitrary complex mixing is claimed.

The frontier includes all positive integer sides, including one, and
r>=0 with largest leg bc+r<=120 after sorting a<=b<=c. It covers 866
matrix shapes and 41132 dimension-compatible family members. Before the
joint cube, exactly three improving targets survived the earlier screens:

| Earlier survivor | Leg dimensions | Target cube slice rank | Gap above source cube |
| --- | --- | ---: | ---: |
| M(9,9,11) plus 11 M1 | 92,110,110 | 1089242 | 76910 |
| M(9,9,11) plus 12 M1 | 93,111,111 | 1119285 | 106953 |
| M(9,9,11) plus 13 M1 | 94,112,112 | 1149886 | 137554 |

All three are now excluded in that class. The new cube caps scalars
beside M(9,9,11) at eight, while the maintained Koszul tests cap them at
thirteen. The exact source certificate is for the actual nonsplit group;
no upper bound is transferred backward from a split degeneration.

The [written proof](proof.md) derives a general joint rank-locus dimension
profile inequality for arbitrary complex semisimple-source degenerations.
It also extends the finite matrix slice-rank reduction to rectangles,
using the externally credited arbitrary-field Flanders/Meshulam theorem.
Gowers's external Theorem 2 supplies direct-sum slice-rank additivity.
The cube cover is verified by a different integer counting method from
the producer: all 1331 class triples, with multiplicity 1728000, are
checked after dense replay of all original source coefficients.

Run from the repository root:

```sh
python research/ai/2026-10-23-central-cover-joint-frontier/frontier.py --output results/local/joint-frontier.json
python research/ai/2026-10-23-central-cover-joint-frontier/verify.py --output results/local/joint-frontier-verification.json
python -m unittest discover -s tests -p test_central_cover_joint_frontier.py -v
```

The separate verifier replays the complex primitive central idempotents,
the full nonsplit F4 source certificate, the source cube cover and the
complete finite frontier. Tests independently construct small joint
Koszul matrices, expand the target cube into its direct summands and
reject changed cover counts and uncovered degree triples. Source files
and inherited proofs are pinned in SOURCES.json.

The saved comparisons at 2.242, 2.233 and 2.223 are conditional controls
for hypothetical arbitrary complex degenerations to the three displayed
targets. They are not achieved exponents. Their premises are excluded
in the coordinate/potential class here and remain unconstructed for
complex maps without the required good reduction.

The two LP reports are optional numerical discovery controls for a wider
relaxation of joint matrix sums. Their floating bounds and fractional
targets are not acceptance premises. That wider problem remains open;
its reproduction script is under `discovery/` and needs NumPy/SciPy.

Further construction work must change the target family, basis maps or
source power. Do not continue the closed one-matrix-plus-scalars search
in this one-copy coordinate/potential class. All written proofs retain
their unreviewed status; no formalization or exponent improvement is claimed.
