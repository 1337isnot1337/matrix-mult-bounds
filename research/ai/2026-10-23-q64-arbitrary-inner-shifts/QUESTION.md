# Arbitrary per-index coordinate shifts on both long legs

**Question.** For the maintained `Q(n,4)` paired source, allow each inner-index coordinate map to use its own integer translation:

\[
B_{y,s}\mapsto b_{s-\beta_y,y},\qquad
C_{z,v}\mapsto c_{v,z-\gamma_v},
\]
with out-of-range target coordinates sent to zero. Can any choices of the eight shifts and any first-leg linear map leave a correction of border rank `O(n)`?

**Answer.** No. The correction's first-leg flattening rank is at least `n(n-1)/2` for every size and every shift profile. The first leg is arbitrary and all eight integer shifts may depend on `n` without restrictions.

The proof uses the target/source subspace intersection. If some adjacent C-shift difference has absolute value at most `floor(n/2)`, a unique off-diagonal term forces most target coordinates to vanish in the intersection. If all three absolute differences exceed `floor(n/2)`, the four matched target slices have a common support of at most `ceil(n/2)` rows. Exact finite replay checks the subspace calculation on deterministic profiles; the all-size proof supplies the theorem.
