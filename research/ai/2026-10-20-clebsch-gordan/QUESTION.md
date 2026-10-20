# Active question: retain off-leading Clebsch--Gordan blocks

Selected after checkpoint `89ebb78`, 2026-10-20. Goal remains active: prove a
matrix-multiplication exponent strictly below 9/4. No such bound is established.

The concurrent fixed-label compatibility and optimistic entropy bounds
concern the leading associated-graded support k=i+j. Here use SL2-equivariant
Clebsch--Gordan lifts, so actual multiplication also retains blocks k>i+j.
Some of these have a saturated representation triangle and become ordinary
convolutions with a different leg designated as output. They are not scored
by the previous leading-filtration model.

1. Compute every rational coefficient in the full equivariant bases.
2. Recognize saturated convolution blocks by explicit axis changes and exact
   diagonal factorization, not solely their dimensions.
3. Search monomial weights on the outer labels; retain exact supports.
4. Score certified matched sectors and full direct sums. Unknown blocks get
   only a certified dot-product restriction, not an invented convolution value.
5. If an exact violation of P_* appears, propagate its actual tensor inequality
   to all feasible character profiles and bound the parameter t uniformly.

Step 5 is necessary for an exponent improvement. A finite profile violation
does not alone finish the goal. Keep negative searches and their scope.

No other worker's branch is modified. The affine construction and its exact
checks remain in the previous package. This question owns off-leading
recoupling blocks, rather than the other workers' leading rows, full-leading
entropy score, replication limit, or convolution Koszul obstruction.
