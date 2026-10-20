# Chebyshev-basis search selected for continued research

The first-pass monomial search fixes monomial coefficient bases. This question
instead changes both polynomial inputs and the output to Chebyshev bases before
assigning weights. It is a new basis ansatz, not a rerun of that search.

For `C(a,B)`, keep first-input basis `T_0/2,T_1,...,T_(a-1)`, discard the
second-input `T_0` coordinate, and keep `T_1,...,T_(B-1)`. Rescale the entire
output by 2. The remaining support has coefficient one at

- `(0,j,j)` for `j>=1`;
- `(i,j,i+j)` and `(i,j,abs(i-j))` for `i,j>=1`.

This follows from `2 T_i T_j=T_(i+j)+T_abs(i-j)` for positive indices.
Output weights chosen as negatives of the minima give a genuine degeneration.
Connected components on the nonshared legs give matched sectors. Full
convolution supports must be recognized and verified; unrecognized blocks use
only a proved slice-rank lower bound, not a conjectural block score.

The selected experiment will record a bounded, seeded search and exact witness
comparisons. A score excluding the finite matching profile is a lead, not an
automatic exponent improvement. The all-scale construction and its implication
must still be proved.

This is also motivated by the symmetric band structure away from the boundary:
`i=abs(k-j)`. Distance-to-a-cut weights can extract a pair of oppositely
oriented output-sharing convolutions. Packing many cuts introduces additional
cross terms; no favorable packing is claimed yet.

## First bounded run

The completed run checks 8,440 normalized binary-weight candidates and 10,000
seeded candidates (5,000 random and 5,000 distance-to-cuts cases). Seed:
`20261020`. It finds no scored violation of the finite matching profile.
The exact best ratio is `10/11`, at source `C(2,5)`, with two recognized
`C(2,2)` sectors. This is a negative result for the specified basis, weights,
recognizer and slice lower bounds, not an all-size obstruction.

The unrecognized-sector fallback uses matrix rank over F2 for a fixed slice.
Its nonzero minors certify lower bounds over the complex numbers for these
integer coefficient matrices. Reusing the old search's count-only slice
fallback would be invalid here because the new support has two output terms
per positive input pair. That fallback was not used.
