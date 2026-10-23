# Test the fixed long-leg coordinate chart

For the maintained source `Q(n,4)` and target `M(n,4,n)`, keep the two
long-leg maps fixed as `B_(y,s) -> b_(s,y)` and
`C_(z,v) -> c_(v,z)`, with out-of-range coordinates sent to zero. Can
any linear first-leg map and an auxiliary tensor of border rank `O(n)`
complete this to the target?

**Answer.** No. For every linear first-leg map, the target-minus-source
correction has first-leg flattening rank exactly `n^2`. Two projected
blocks force every kernel vector to be zero along each diagonal, starting
from boundary entries killed by one block.
