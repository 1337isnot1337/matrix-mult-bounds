# Long-leg Koszul ranks of the paired convolution source

Selected October 23, 2026 from main 539b539 after checking the active
branches and PRs. This investigation is separate from the central-cover,
singular-unit and boundary-incidence continuations.

For P_a with format (a^2,a(2a-1),a(2a-1)), determine the ranks of

    wedge^p B tensor A* -> wedge^(p+1) B tensor C.

The maintained all-power formula covers the short A leg. Its finite
single-target frontier has 28 surviving formats through a=16, first at
a=14. Passing that test supplies no degeneration. Can the long-leg maps
exclude any of them, or can a proved dominance statement close this
particular screening route?

Intended output: an all-size proved rank bound or formula, exact finite
coefficient checks in the original source convention, and a target
comparison with explicit scope. Discovery ranks over a finite field are
lower bounds on complex source ranks, not usable source upper bounds for
excluding a complex degeneration. A field-specific rank comparison alone
will not be promoted to a complex obstruction.

The analytic proof now reaches the first support threshold, `p=a`, using a
full-spark interpolation basis and a two-block compatibility argument. The
degrees `p>=a+1` remain the main question. No claim of a smaller exponent is
made.

## Checkpoint: through `p=a`

The [proof through the support threshold](long_leg_low_degrees.md) establishes
full column rank on both long legs for `0<=p<=a`. This range cannot exclude
any of the 28 saved targets through `a=16`: their target ranks are bounded
by the same source-domain dimensions. Continue with `p>=a+1`.
