# The rank91 core and target total198

[proof.md](proof.md) proves that every complex A4 source parameter
space whose slices all have rank strictly below 91 has dimension at
most 67. This cap is not asserted sharp. The four possible dimension-68
equality profiles reduce to eight strip ideals, all containing one
rank91 core or its transpose.

For complete Laurent A4 presentations of M(10,10,11), the new source
theorem forces mixed leading-rank pair sums at most133 and total leading
rank at most198. Every earlier leading-rank202 exclusion is retained.
The screened total198 endpoints are (62,66,70),(62,70,66); no compatible
target presentation is constructed.

## Reproduce exact acceptance

From the repository root, using Python 3.10 or later:

    python -I -S research/ai/2026-10-23-rank91-core/verify.py
    python -m unittest discover -s tests -p 'test_rank91_core.py' -v

Acceptance uses only standard-library integer arithmetic. It rebuilds
the literal source and coherent matrices, verifies four saved odd
minors, independently enumerates the four equality profiles and eight
nested strip ideals, checks all 112 transpose basis identities, and
rebuilds the complete pair and triple survival masks. Source pins and
scope controls are part of acceptance.

The saved census contains 20,706 rank pairs and 1,050,804 rank triples.
It retains all frozen202 exclusions and removes 36 further mixed pairs,
24 further long pairs and 5,250 further triples. The eight focused tests
also compare every inherited survival bit with the earlier package and
reject damaged source witnesses, source pins, census bits and scope.

The [certificate](../../../results/rank91-core-2026-10-23/certificates.json)
contains the two credited coherent20/24 minors, the new coherent26
minor, and the common-core91 minor. The
[report](../../../results/rank91-core-2026-10-23/controls.json) records
coverage and the hash of the canonical uncompressed census. The census
is saved in [census.json.gz](../../../results/rank91-core-2026-10-23/census.json.gz).

## Optional discovery replay

    python research/ai/2026-10-23-rank91-core/discover.py --output results/local/rank91-core/rebuilt.json

Discovery reconstructs matrix entries separately from acceptance,
selects the three fixed coherent minors, and tries at most 64 binary
coefficient masks on the common core. Seed 0 succeeds on its first
mask. Acceptance uses only the saved coefficients and square minors,
with a different pivot convention; it does not run this search.

The [source record](sources.json) pins the complete frozen202 and
source92/96 prerequisites. No frozen proof or evidence file is changed.
The strict threshold91 is essential to this claim: the preceding
dimension68 example has uniform rank at most91, so a weak-rank91
dimension cap67 would be false. No exponent improvement is claimed.
