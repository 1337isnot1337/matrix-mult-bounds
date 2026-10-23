# An all-size obstruction for the width-two support score

Status: written and unreviewed. This is a bound on the specified search
score, not an upper bound on an actual tensor invariant. No smaller
matrix multiplication exponent follows.

## Statement and convention

Let b>=2 and let S be any subset of the coefficient-one support
`{(i,j,i+j): 0<=i<2, 0<=j<b}` of C(2,b). Partition S into connected
components of its bipartite Y-Z incidence graph. The shared leg is X.
For each component use exactly the historical search convention:

* If its entire support is a convolution C(r,s), after sorting each
  coordinate set and optionally reversing axes, score it by P*(r,s).
* Otherwise score it by its maximum single-slice matching size.

Write sigma(S) for the sum. The same convention defines sigma on
subsets of C(b,2); exchanging inputs changes the component partition.

**Theorem.** For either orientation and every such subset,

`sigma(S) <= P*(2,b) = (4b+2)/3`.

For C(2,b), let R and Z be the numbers of incident Y and Z vertices.
For each component with an odd number of edges, let r be its number
of Y vertices. There is the exact identity

`P*(2,b)-sigma(S) = [2(b-R)+2(b+1-Z)+sum_odd r]/3`. (1)

Thus equality holds precisely when all b Y vertices and b+1 Z vertices
are incident and every component has an even number of edges.
For C(b,2), equality holds precisely for the complete support.

## The path orientation C(2,b)

The entire Y-Z graph is the path

`z0 -- y0 -- z1 -- y1 -- ... -- y_(b-1) -- z_b`.

The two edge labels, i=0 and i=1, alternate along it. Every component
of any nonempty edge subset is therefore a path segment.

A component of 2k edges, k>=1, has part sizes (k,k+1) or (k+1,k)
and exactly k terms with each X label. It is a full C(2,k) support
up to axis permutation and reversal: the consecutive pairs of edges
have precisely the two consecutive output indices in that support.
Its score is `(4k+2)/3 = 2(|Y|+|Z|)/3`. This also holds for k=1,
where the equivalent C(1,2) has score two.

A component of 2r-1 edges has r vertices in each part. If r=1 it
is C(1,1) and has score one. If r>=2 its three leg dimensions are
(2,r,r), so no axis has dimension equal to the sum of the other two
minus one. It is unrecognized. The most common X label occurs r
times, and every Y or Z slice has at most two terms. Consequently
the fallback score is r, including r=2. In both cases this equals
`2(|Y|+|Z|)/3-r/3`.

Sum these formulas over the nonempty components. This gives
`sigma(S)=2(R+Z)/3-sum_odd r/3`, which proves (1). Each term in
its deficit is nonnegative. The empty support also satisfies (1).
The equality characterization follows without a weight assumption.

## The two-hub orientation C(b,2)

The Y-Z graph now has just two Y vertices. Each Z vertex has at most
two incident edges. If the two Y vertices are not connected, there
are at most two nonempty components, each with only one Y vertex.
Within either one, the X and Z coordinates are distinct, so its
support is C(1,r), where r is its edge count. The two components
have disjoint Z coordinates. Their total score is at most b+1,
which is strictly below `(4b+2)/3` for b>=2.

If the two Y vertices are connected, every retained edge lies in
their one component. An unrecognized component has score at most b:
every Y slice has at most b terms and every X or Z slice at most
two. This is strictly below P*(2,b).

It remains to bound a recognized component. Put R=|X|<=b and Z=|Z|<=b+1.
Its dimensions are (R,2,Z). If Z is the convolution output, Z=R+1
and its score is P*(2,R)<=P*(2,b), with equality requiring R=b
and all 2b source terms. If X is the output, R=Z+1 and its score
is P*(2,Z)<=P*(2,b-1)<P*(2,b). When R or Z is one, the notation
P*(2,1)=2 still obeys the same inequalities. If Y is the output,
R+Z=3, so its score is P*(1,2)=2<P*(2,b).
This exhausts the historical recognizer's output choices. Complete
support has score P*(2,b), proving the second equality assertion.

## Consequences, credits, and limits

Every zero support of a diagonal monomial degeneration is a subset
covered above. Arbitrary integer or real weights on all three legs,
additional coordinate deletions, and nonzero diagonal scalings therefore
cannot make this scoring rule exceed P*(2,b), in either input role.
For scalings, undo their nonzero diagonal coefficients on the retained
coordinates before applying the coefficient-one convention.

The recurrence defining P*, the matched-component convention, the
convolution recognizer, and the fallback bound are prior repository work;
their exact pins are in sources.json. PR118 separately improves rational
ranking and replay for finite searches. The path identity and two-hub
case analysis here do not depend on that unmerged implementation.
No external theorem is imported and no historical priority is claimed.

The score gives only the stated lower estimate for an unrecognized
component. A stronger estimate on such a component can exceed its score
and is outside this theorem. General basis changes, other source widths,
other decompositions, tensor powers and a spectral realization of P*
remain outside the result. Exhaustive finite tests are controls for the
written proof, not an independent review or a formalization of it.
