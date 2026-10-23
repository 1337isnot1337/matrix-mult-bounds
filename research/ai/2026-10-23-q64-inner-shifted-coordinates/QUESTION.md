# Test the inner-index shifted coordinate chart

Keep the first-leg map `U` arbitrary. On the two long legs of `Q(n,4)`,
use `B_(y,s) -> b_(s-y,y)` and `C_(z,v) -> c_(v,z-v)`, sending
out-of-range target coordinates to zero. Can an auxiliary tensor of
border rank `O(n)` complete the image to `M(n,4,n)`?

**Answer.** No. The correction first-leg flattening has rank at least
`n^2-2`: two off-diagonal inner-coordinate blocks force all but two
boundary source functionals to vanish, and a matched block then confines
any kernel vector to two target coordinates.
