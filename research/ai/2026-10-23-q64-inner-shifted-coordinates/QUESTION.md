# Test long-leg shifts proportional to the inner indices

Fix nonnegative integers `k_B,k_C`. On the two long legs of `Q(n,4)`, use
`B_(y,s) -> b_(s-k_B*y,y)` and
`C_(z,v) -> c_(v,z-k_C*v)`, sending out-of-range coordinates to zero.
Keep the first-leg map arbitrary. Can an auxiliary tensor of border rank
`O(n)` complete the image to `M(n,4,n)`?

**Answer.** No. For `n>max(k_B,k_C)`, the correction first-leg
flattening rank is at least `n^2-1-k_B*k_C`. With fixed shifts this is
quadratic in `n`.
