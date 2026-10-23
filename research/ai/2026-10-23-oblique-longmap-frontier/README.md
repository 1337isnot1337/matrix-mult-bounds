# A fixed-corner bound and a finite long-map frontier

**Status: written, unreviewed scope proof and exact finite experiments.**
This checkpoint supplies a surjective benchmark at `Q(6,4)`, a universal
bound when its good output rows remain fixed, and two finite screens.
It supplies no smaller matrix-multiplication exponent.

| Item | Precise outcome |
| --- | --- |
| Integer benchmark | Both long maps have rank twenty; the minimum first residual rank is nine. Its displayed residual has rational flattening ranks `(9,18,18)`. |
| Arbitrary fillers with the benchmark's sixteen good rows fixed on each long leg | Every first map has residual rank at least nine, over every field. Equality is not asserted for arbitrary fillers. |
| 384 specified inner-dependent shift pairs | Every integer candidate has rational minimum first residual rank at least nine. Each has a replayed modular rank minor. |
| 81 specified mixed-middle corners | Sixty-one decoders are nonsingular modulo 32003. Each valid corner is exact and injective on the raw thirty-six-dimensional first leg. Twenty singular modular controls are skipped. |

The [proof](proof.md) separates the universal fixed-row result from the
finite screens. The first map is unrestricted in every residual lower
bound. Arbitrary changes of both long maps remain outside the result.
The benchmark's long-leg residual ranks are larger than those of the
earlier [oblique repair](../2026-10-23-oblique-paired-repair/proof.md).
It is a surjective search starting point, not a better scalar repair.
The earlier ordinary nineteen-term and border eighteen-term certificates
remain unchanged.

## Reproduce

Use Python 3.10 or later. This package uses only the standard library.
From the repository root:

```sh
python research/ai/2026-10-23-oblique-longmap-frontier/frontier.py
python -m unittest discover -s tests -p 'test_oblique_longmap_frontier.py' -v
```

The first command reconstructs every native source coefficient needed
by the certificates and checks all saved minors. It also checks the five
local byte pins in [sources.json](sources.json). The compact
[certificate.json](certificate.json) stores parameter tuples, minor
indices and determinants. It does not store large dense matrices.

To regenerate the complete certificate at another path:

```sh
python research/ai/2026-10-23-oblique-longmap-frontier/frontier.py --write /tmp/longmap-frontier.json
```

All 384 shift controls and all 81 corner records must be present, in the
specified order. Tests reject missing controls, changed late-record
minors, false corner statuses, a changed unit-minor record and a false
source pin. Complete native rational controls compare the sparse screen
with the earlier exact first-map optimizer.

## Research boundary

An improvement below first residual nine must change some good output
rows or use a different limiting construction. Merely filling the four
new rows on either long leg cannot work for this fixed corner. The
finite shifts and mixed-middle parameters tested here do not identify
a successful replacement.

Additional local Euler-direction and second-order probes remained
unsuccessful discovery scratch. They are not registered claims, not
part of this certificate, and not used to exclude a general local or
Laurent construction. No unfinished search is counted as coverage.

Claims: `AI-OBLIQUE-FILLER-SCOPE-001` is a written unreviewed proof;
`EXP-OBLIQUE-LONGMAP-FRONTIER-002` is a finite experiment. Coordinated
checks within the generating session are not independent mathematical
review. No historical priority or formalization is claimed.
