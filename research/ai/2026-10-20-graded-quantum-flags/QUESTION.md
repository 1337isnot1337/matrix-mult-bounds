# Escaping the closed regular root flags

Owner: product/quantum worker, research/graded-quantum-flags-20261020.
Base: main 4289a7b, after PR25. No bound below 9/4 is established.

The generic quantum family is valid, but the straightforward leading
flags at the tested roots are now excluded by arguments that allow
arbitrarily high regular jets and an arbitrary Laurent map on one leg.
Changing only the jet cutoff or the first-leg coefficients does not
reopen a closed pair of leading maps.

The canonical Cartan profile from PR23 is adopted, not newly claimed.
The order-three/six ungraded slice test leaves ceiling 104, but its
graded central space forces a nonzero rank-at-most-four matrix into the
target. Graded output changes cannot remove that matrix: their only
lost coordinates are in different grades. Sixteen phase pairs are closed
under those precise grading hypotheses.

Next construction front: change the leading flags or break the grading.
In particular, an ungraded matrix-space limit at order six remains open:
its initial projected space has modular dimension 12 in a 112-dimensional
first leg, leaving a possible 100-dimensional complement. This numerical
dimension match is not a matrix-algebra identification or a construction.
Compute actual saturated coefficient limits before fitting or asserting
any such identification. Preserve all required zero coefficients.

The independent scratch exploration also considered suppressing the two
upper leading rows (grades seven and eight), leaving grades four and
five. This removes the constant central term, but the suppressed rows
return low-rank central terms at the next order. No qualifying limit is
verified. Further row-weight choices need a new cancellation mechanism,
not a repeat of the same leading flags or a small masked residual.
