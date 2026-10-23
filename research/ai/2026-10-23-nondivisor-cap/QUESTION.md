# Nondivisor source-space cap at A5, ceiling34

Question: is the maximum dimension of a complex linear space of canonical
A5 slices of ordinary matrix rank at most34 exactly10?

A two-row strip has dimension10 and rank ceiling30. PR148 proves the
analogous sharp strip theorem when the width divides the balanced size,
but explicitly leaves this nondivisor case open: the pair1+x^2*z^2 has
rank34, below the proposed threshold35. PR171 separately classifies
two-monomial ranks and does not prove a source-space dimension cap.

Plan: inspect every size11 order ideal in the5-by5 extreme-middle grid.
If each contains a source slice with a nonzero35-minor, give exact
certificates and reconstruct the rank-preserving order-ideal reduction
for arbitrary complex source spaces. If a shape survives, determine its
actual generic rank and prove a universal upper bound before calling it
a counterexample. Random modular failures alone prove neither outcome.

This is a structural source-space question, not a matrix target or an
exponent improvement. Its possible downstream use is a sharper nondivisor
instance of the credited singular-long-leg ruling test. Every source,
rank and dimension hypothesis must remain explicit.

Sources inspected:

- PR148 at673710d3a4284d88e4d24350681b26912831bf7a, divisor proof and its
  stated nondivisor boundary.
- PR171 at0e470a741bf8d6cd9bb0f6ffb19c31e278bf501e, separate binomial
  rank formula; this package does not claim that derivation.
- PR129's order-ideal method, with its exact source pin to be recorded
  when adopted. Main base3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93.
