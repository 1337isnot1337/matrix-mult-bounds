# Concurrent work and exact contribution boundary

This checkout began at `e0d7ed5`. Its first selection pass found only the
Koszul/scaling branch. A later remote refresh found two independently
developed branches that overlap parts of this investigation:

- `research/filtration-compatibility-20261020`, proof commit `73b2d20`:
  proves the stronger equivalence of all three fixed-label families with
  separate concavity through zero, and proves the zero boundary for actual
  character profiles. Our simpler implication was developed independently
  and pushed as `712c91a`. It is corroborating work, not an additional
  independent mathematical discovery beyond that branch's result. The
  stronger converse and actual-profile boundary on that branch are its work.
- `research/full-filtration-entropy-20261020`, result commit `e6d33e7`:
  bounds an explicitly optimistic full-support entropy score, including an
  all-size balanced gap and exact simplex upper bounds through dimension
  12. Its weighted tensor-extraction interpretation remains unproved.
  This supersedes any reason to extend our numerical min-entropy probe on
  the same source grid.
- `research/koszul-and-scaling-20261020`, refreshed head `30219d0`:
  owns the general convolution Koszul ranks, rejection of the 85 archived
  packings, and additional scaling/rigidity work. This session does not
  claim those results.

The distinct contribution in this package is the explicit integer-weight
affine-line degeneration of the determinant-adapted product, with exact
coefficient checks. The assignment calculation is an independent finite
certificate for every matching of whole blocks through source dimension 9;
it is not presented as wider coverage than the other branch's entropy bound.

The package directory was renamed after discovering the collision, so that
the other worker's `2026-10-20-filtration/` directory is not overwritten on
integration. Both the historical first pass and all remote branches are left
intact. No main-branch merge or exponent promotion is implied.

## Exploratory entropy probe, not a theorem

A floating SLSQP probe of the optimistic minimum-marginal-entropy expression
found approximate source-normalized 3/4-power scores 0.864075596 for
(2,2,2,2), 0.813793855 for (3,3,3,3), and 0.787482890 for (4,4,4,4).
Those three optimizer calls reported success. Calls at balanced dimensions
6, 9 and 16 hit their iteration limits; they are incomplete optimizations.
No optimizer value was accepted as an exact upper bound or used to claim a
tensor inequality. Another exploratory average-entropy expression gave
0.941101632 at (2,2,2,2), also without a proved weighted transfer theorem.
These observations supply no exponent improvement or exhaustive negative
result. The exact results of this package are in the proof and integer
certificates, independently of these exploratory numerical values.
