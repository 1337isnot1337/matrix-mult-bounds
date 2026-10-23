# Exact coordinate-projection optimization of the component score

This is an R6 continuation, dependent on the recognition package in PR187.
It changes the estimate on an existing monomial degeneration, rather than
claiming a new degeneration or an exponent improvement.

For a finite additive coefficient-one support S, let its components be the
connected components of the bipartite graph on the y and z coordinates.
The x axis remains shared. Let b(S) be the existing component estimate:
P_*(r,s) when the entire component is a convolution, and otherwise the
largest fixed-coordinate slice matching. Let B(S) be the sum of b over
the components. Both estimates retain their previous attribution.

Choose arbitrary subsets Y and Z of the nonshared coordinate sets and
restrict to S[Y,Z]. This is the literal tensor projection deleting those
y and z basis vectors. In particular, it does not independently alter the
shared x basis in different components. Define

    F(S) = max_(Y,Z) B(S[Y,Z]),          B(empty)=0.

**Finite optimization theorem.** If S has more than one component S_i,
then F(S)=sum_i F(S_i). If S is connected and nonempty, then

    F(S) = max(B(S), max_(v in y or z coordinates) F(S with v deleted)).

For the first assertion, components have disjoint y and z coordinates.
Every pair of masks restricts each independently, and the union of masks
chosen within different components introduces no cross-component term.
For the second, an unchanged support has score B(S). Every proper induced
support can be reached by first deleting one unused y or z coordinate;
subsequent deletions give the desired masks. Conversely every branch of
the recurrence is such a projection. Induction on the number of supported
coordinates proves the recurrence and termination at the empty support.
Thus memoized exhaustive evaluation computes exactly this finite objective.

The witness checker does not call the optimizer. From the original weights
it reconstructs the original support, applies the exported y/z masks, and
recomputes its components and rational score. This certifies an achieved
lower score. The finite optimum additionally relies on the exhaustive
recurrence; small cases are checked against direct enumeration of every
pair of coordinate masks. No optimality over arbitrary tensor restrictions,
further weight degenerations or general linear bases is asserted.

## A strict gain on an old support

For wx=(0,0,1) and wy=(0,0,0), the support is

    (0,0,0), (0,1,1), (0,2,2), (1,0,1),
    (1,1,2), (1,2,3), (2,2,4).

Its whole connected component is not a convolution, and the old slice
fallback is 3. Retaining y=0,2 and all z coordinates leaves two components:

    y=0: (0,0,0), (1,0,1),
    y=2: (0,2,2), (1,2,3), (2,2,4).

They are C(1,2) and C(1,3), sharing x, and give score 2+3=5.
The source profile is P_*(3,3)=56/9, so the strengthened ratio is 45/56.
This remains below one. The recurrence certifies 5 as the optimum of the
specified y/z projection and component-score class at this support.

All new work is owner-directed OpenAI Codex research. The archived support,
component score and matching profile and PR187's recognition theorem retain
their credits and byte pins. The recurrence is elementary finite induction;
no new external theorem is imported. The proof is written and unreviewed.
No independent review, formalization or exponent improvement is claimed.
