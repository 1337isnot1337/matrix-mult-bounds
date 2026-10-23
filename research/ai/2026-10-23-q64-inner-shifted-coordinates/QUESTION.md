# Exclude all inner-index proportional long-leg shifts

For each `n`, choose integers `0<=k_B(n),k_C(n)<n`. Use
`B_(y,s) -> b_(s-k_B*y,y)` and
`C_(z,v) -> c_(v,z-k_C*v)`, zeroing out-of-range coordinates, and keep
the first-leg map arbitrary. Can an auxiliary tensor of border rank
`O(n)` complete the source image to `M(n,4,n)`?

**Answer.** No. For every `n>=4`, the correction first-leg flattening
rank is at least `n^2/2`, uniformly in both multipliers and the
first-leg map.
