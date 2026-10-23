# Full-channel paired maps with fixed polynomial-column routing

October 23, 2026. Owner-directed OpenAI Codex continuation.

The active paired construction seeks a degeneration from `Q(n,4)` plus
a subquadratic auxiliary tensor to `M(n-c,4,n-c)`. The existing low-channel
rank proofs do not cover maps whose generic channel rank is four.

Study the following separate class. Each retained source polynomial
column goes to one target outer column, with an arbitrary square channel
matrix. The two routing injections are fixed. Channel matrices may vary
as regular formal series, the first map may have arbitrary Laurent poles,
and an auxiliary tensor may cancel those poles. No two different source
polynomial columns mix in one target outer coordinate.

Can overlapping length-four coefficient windows force a quadratic repair
cost even when all channel matrices are invertible? More generally, how
much leading rank loss is necessary when some channel matrices become
singular at zero?

The proposed proof uses the intersection of the ordinary leading source
slice plane with the target matrix slice plane. Invertible overlapping
windows should force target scalar coefficients to be proportional on
each connected component. A separate saturation dimension budget must
account for every new direction created by singular leading maps.

The deliverable is a quantified all-field statement, a proof that handles
auxiliary pole cancellation, and complete native-source coefficient
controls. Examples must test full channel rank and separated routing
components, so the scope cannot silently collapse to the earlier theorem.

The source and correction criterion are maintained in the paired-source
and correction-budget packages. PR211 supplies the separate Laurent
common-kernel argument; its low-channel hypothesis is not assumed here.
This question does not assert a new exponent or exclude column-mixing
long maps. The A4 compression and aggregation continuations remain
separate investigations.
