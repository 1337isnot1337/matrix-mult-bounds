# Test the neighboring long-leg coordinate charts

For `epsilon_B,epsilon_C` in `{0,1}`, use
`B_(y,s) -> b_(s-epsilon_B*y,y)` and
`C_(z,v) -> c_(v,z-epsilon_C*v)`, with out-of-range coordinates sent to
zero. Keep the first-leg map arbitrary. Can an auxiliary tensor of border
rank `O(n)` complete the image to `M(n,4,n)`?

**Answer.** No. For `n>=2`, the correction first-leg flattening rank is
at least `n^2-1-epsilon_B*epsilon_C`, hence at least `n^2-2`. Two
off-diagonal blocks leave at most `1+epsilon_B*epsilon_C` source
functionals undetermined; a matched block confines the kernel to that
many target coordinates.
