# Boundary-spanning first jets have no mixed component

Written proof, unreviewed. Canonical extension data are credited to PR45
at 5d4a941. This is a consequence of the new no-second-growth theorem;
it does not exclude every later higher-order lift.

Split the canonical covector spaces as E_B=D_B direct_sum R_B and
E_C=D_C direct_sum R_C. The first16 basis vectors are the boundary
spaces D_B,D_C; the last4 are mixed. Both D spaces contain G, dimension4.
On K, H annihilates G on either factor. Its effective boundary factors
therefore have dimension12.

There are two disjoint source-A coordinate sets:

    L: i in{1,2},s in{0,3},z in{0,3,6};
    M: i in{0,3},s in{1,2},z in{0,3,6}.

The blocks H(D_B,R_C) and H(R_B,D_C) are supported on L and M,
respectively. Both are ordinary 2-by6 times6-by2 matrix multiplication,
with leg dimensions (12,12,4), after quotienting four zero covectors.
For the first block the mixed-v slice is exactly

    [[v3,v1],[v2,v0]] tensor I6 times B,

where B is a fixed surjective12-by16 matrix with a selected determinant-1
minor. The identity is checked in every column, not just that minor.
The other block follows by source short-index reversal and transposition.
In particular every nonzero mixed v gives a first-versus-boundary matrix
of rank at least6. No nonzero mixed covector annihilates the full boundary
space in either block.

Let V_B,V_C be the covector spans of outside-leading rows of the first
derivatives. Suppose

    D_B subset V_B+G,    D_C subset V_C+G.

Since H_actual=0 by `rank_one.md`, its restriction to either full boundary
factor must vanish. The nonzero-rank property just proved forces the
mixed projection of V_C to vanish, and similarly that of V_B. Therefore

    V_B+G=D_B,   V_C+G=D_C.

Thus in this boundary-spanning family every nonzero mixed first-jet
component is excluded, independently of all second and higher jets.
Boundary-only first jets and spans omitting part of D remain construction
questions. The theorem imposes no condition that the four leading output
rows remain in the larger56-dimensional boundary spaces at later orders;
that is the distinct all-order trap owned in PR45.
