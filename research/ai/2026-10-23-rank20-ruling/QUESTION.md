# Linear spaces at the first A4 rank gap

Base: `fc0a139`, the PR125 shared-correction ruling package. That argument
excludes a balanced long-map leading rank at least106 using only source
slices below rank20. At long rank105 its cap is exactly20.

Question: classify the A4 source locus of rank at most20, and prove that
every vector subspace in it has dimension at most eight, below the target
ruling dimension ten. This would extend the same Laurent criterion to
long-map leading rank105, with arbitrary poles in both other maps.

Proposed mechanism: the prior below-rank32 theorem fixes one coherent
middle factor on a linear source space. For the remaining biform g of
bidegree(3,3), the prior splitting formula gives rank R(g)=16+sum min(4,mu_j).
At rank at most20 this forces a quadratic divisor in x or in z. Each
factor family has maximum linear-space dimension eight, attained by a
fixed quadratic times all forms of bidegree(1,3) or(3,1). A generic-pencil
common-factor argument must justify that bound when the divisor varies.

The source rank formula's Grothendieck splitting dependency and PR125's
correction mechanism retain their credit and hypotheses. This is a new
written proof question with exact controls in progress, not independent
review, a matrix construction or an exponent improvement. Rank caps
above20 are not covered by the proposed dimension-eight bound.

Continuation: the argument extends to every a>=2, with source rank cap
a^2+a, binary divisor degree a-2 and sharp linear-space dimension2a.
The proof and the resulting uniform Laurent criterion are in all_sizes.md.
This is a justified extension of the same coefficient-map and generic-pencil
mechanism, not an assumption about higher A4 rank caps.
