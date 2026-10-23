# Joint-target continuation

The complete one-matrix-plus-scalars family is closed in the stated
one-copy complex coefficient-one coordinate/potential class. The exact
SL(2,F5) source cube has slice-rank upper bound 1012332. The three formats
left by the earlier complex screens exceed it by 76910, 106953 and 137554.
No arbitrary-complex exclusion or exponent improvement follows.

Local verification at commit 7857f78: the separate source/frontier verifier
replayed the complex central idempotents, all 1728000 original F4 source
coefficients, all 1331 cube degree-class triples and the complete 41132
format census. All six focused tests passed. PR #114 is a draft with hosted
CI pending. The proof has no independent mathematical review or Lean
formalization.

Next question: does the same cyclic-cube bound, combined with exact complex
rank-profile, Koszul and cost screens, exclude every strict-improving
two-matrix target

    U = M(a1,b1,c1) direct_sum M(a2,b2,c2) direct_sum r M1

with all three leg dimensions at most 120? For each ordered component triple
(i,j,k), cyclic tensoring gives a rectangular matrix multiplication tensor
with dimensions `(a_i*b_j*c_k, b_i*c_j*a_k, c_i*a_j*b_k)`. Gowers additivity
therefore gives an exact integer target-cube slice-rank sum over all
component triples. Derive that sum, build complete exact screens for the
integer family, and keep the coefficient-one good-reduction limitation
explicit. Do not infer that this covers more than two matrix components
unless the complete family is actually enumerated.
