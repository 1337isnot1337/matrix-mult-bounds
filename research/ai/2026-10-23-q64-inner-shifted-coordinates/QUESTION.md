# Locate the inner-index shifted long-leg frontier

For each `n`, choose integers `0<=k_B(n),k_C(n)<n`. On the two long
legs of `Q(n,4)`, use `B_(y,s) -> b_(s-k_B*y,y)` and
`C_(z,v) -> c_(v,z-k_C*v)`, sending out-of-range coordinates to zero.
Keep the first-leg map arbitrary. When can an auxiliary tensor of border
rank `O(n)` complete the image to `M(n,4,n)`?

**Answer.** The correction first-leg flattening rank is at least
`n^2-1-k_B*k_C` for every `n`. Therefore an `O(n)` correction requires
`k_B*k_C >= n^2-O(n)`, forcing both multipliers to be `n-O(1)`. This
near-terminal regime remains open.
