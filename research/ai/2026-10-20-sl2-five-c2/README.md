# Selected finite target in SL(2,5) x C2

Question: construct an exact group-potential degeneration to M(13,13,15)
from the complex group algebra of SL(2,5) x C2. No witness or exponent
improvement is supplied at task selection.

This direct-product lane differs from the concurrent worker's SL(2,5) search
and from our SL(2,7) lane. It permits mixing the two group algebra copies.
The source has order 240 and degrees `(1,2,2,3,3,4,4,5,6)`, each repeated
twice. Rational central idempotents derive the first factor's degrees; the
direct-product representation theorem supplies the repetition. Exact root
intervals certify a conditional omega < 2247/1000 comparison. The source
degeneration is missing.

The search reuses the unchanged SAT/Farkas code pinned in the SL(2,7) package
at concurrent commit 75f453b. Its separate adapter enumerates the direct
product, excludes all central pairs by the proved quotient rule, introduces
60 central-orbit presence variables per leg, and normalizes a large fiber
into an explicitly checked order-48 subgroup of index five. Acceptance still
checks every group product and integer weight. A timeout is no exclusion.

The [structured parent note](structured_note.md) records an exact exclusion
of 1,000 explicitly enumerated ten-point section triples. Every rejection
has an independently replayed positive integer Farkas circuit. This closes
that finite parent class, while the selected (13,13,15) target remains open.
